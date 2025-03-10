"""Mixture model for matrix completion"""
from copy import deepcopy
from typing import Tuple
import numpy as np
from scipy.special import logsumexp
from common import GaussianMixture


def log_gaussian(x: np.ndarray, mu: np.ndarray, var: float) -> float:
    """Computes the log Gaussian likelihood of a data point.

    Args:
        x: (d,) array holding the observed data for a user
        mu: (d,) array holding the mean vector of the Gaussian
        var: variance of the Gaussian

    Returns:
        float: log Gaussian likelihood
    """
    d = len(x)
    log_likelihood = -0.5 * np.sum((x - mu) ** 2) / var
    log_likelihood -= 0.5 * d * np.log(2 * np.pi * var)
    return log_likelihood


def estep(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step: Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the assignment
    """
    n, d = X.shape
    K = mixture.mu.shape[0]

    log_post = np.zeros((n, K))
    log_likelihood = 0.0

    for u in range(n):
        # Indices of observed entries for user u
        C_u = X[u] != 0
        x_Cu = X[u, C_u]  # Observed ratings

        # Compute log probabilities for each component
        log_probs = np.zeros(K)
        for j in range(K):
            mu_Cu = mixture.mu[j, C_u]
            var = mixture.var[j]
            log_prob = log_gaussian(x_Cu, mu_Cu, var)
            log_probs[j] = np.log(mixture.p[j] + 1e-16) + log_prob

        # Normalize to get the log-posterior using logsumexp
        log_likelihood += logsumexp(log_probs)
        log_post[u, :] = log_probs - logsumexp(log_probs)

    # Convert log-posterior to actual posterior probabilities
    post = np.exp(log_post)

    return post, log_likelihood


def mstep(X: np.ndarray, post: np.ndarray, mixture: GaussianMixture,
          min_variance: float = .25) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        post: (n, K) array holding the soft counts
            for all components for all examples
        mixture: the current gaussian mixture
        min_variance: the minimum variance for each gaussian

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    n, d = X.shape
    K = post.shape[1]

    # Update the mixing proportions
    n_hat = np.sum(post, axis=0)  # Total responsibility for each component
    p_new = n_hat / n

    # Update the means
    mu_new = np.zeros((K, d))
    for j in range(K):
        for i in range(d):
            relevant_indices = X[:, i] != 0
            if np.sum(post[relevant_indices, j]) >= 1:
                mu_new[j, i] = np.sum(
                    post[relevant_indices, j] * X[relevant_indices, i]) / np.sum(post[relevant_indices, j])

    # Update the variances
    var_new = np.zeros(K)
    for j in range(K):
        variance_sum = 0
        total_weight = 0
        for i in range(d):
            relevant_indices = X[:, i] != 0
            if np.sum(post[relevant_indices, j]) >= 1:
                diff = X[relevant_indices, i] - mu_new[j, i]
                variance_sum += np.sum(post[relevant_indices, j] * (diff ** 2))
                total_weight += np.sum(post[relevant_indices, j])
        var_new[j] = variance_sum / \
            total_weight if total_weight > 0 else min_variance
        var_new[j] = max(var_new[j], min_variance)

    return GaussianMixture(mu_new, var_new, p_new)


def run(X: np.ndarray, mixture: GaussianMixture,
        post: np.ndarray) -> Tuple[GaussianMixture, np.ndarray, float]:
    """Runs the mixture model

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the current assignment
    """
    prev_log_likelihood = None
    log_likelihood = None
    threshold = 1e-6

    X_copy = deepcopy(X)

    while prev_log_likelihood is None or log_likelihood - prev_log_likelihood > threshold * abs(log_likelihood):
        prev_log_likelihood = log_likelihood

        # E-step: Calculate the responsibilities and log-likelihood
        post, log_likelihood = estep(X_copy, mixture)

        # M-step: Update the parameters of the mixture model
        mixture = mstep(X_copy, post, mixture)

    return mixture, post, log_likelihood


def fill_matrix(X: np.ndarray, mixture: GaussianMixture) -> np.ndarray:
    """Fills an incomplete matrix according to a mixture model

    Args:
        X: (n, d) array of incomplete data (incomplete entries = 0)
        mixture: a mixture of gaussians

    Returns:
        np.ndarray: a (n, d) array with completed data
    """
    n, d = X.shape
    K = mixture.mu.shape[0]

    # Copy the original matrix to avoid modifying it in place
    X_pred = X.copy()

    for u in range(n):
        # Indices of observed entries for user u
        C_u = X[u] != 0
        x_Cu = X[u, C_u]  # Observed ratings

        # Compute the soft assignments (posteriors) for each Gaussian component
        log_probs = np.zeros(K)
        for j in range(K):
            mu_Cu = mixture.mu[j, C_u]
            var = mixture.var[j]
            log_prob = log_gaussian(x_Cu, mu_Cu, var)
            log_probs[j] = np.log(mixture.p[j] + 1e-16) + log_prob

        # Normalize to get the posteriors using logsumexp
        log_post = log_probs - logsumexp(log_probs)
        post = np.exp(log_post)

        # Fill in the missing values in the current row (user)
        for i in range(d):
            if not C_u[i]:  # If the entry is missing
                X_pred[u, i] = np.dot(post, mixture.mu[:, i])

    return X_pred
