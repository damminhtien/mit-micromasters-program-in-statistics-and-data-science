"""Mixture model for matrix completion"""
from typing import Tuple
import numpy as np
from scipy.special import logsumexp
from common import GaussianMixture


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

    # Extract mixture parameters
    mu = mixture.mu
    var = mixture.var
    pi = mixture.p

    # Initialize responsibilities (posterior probabilities)
    post = np.zeros((n, K))

    # Initialize log-likelihood
    log_likelihood = 0.0

    for i in range(n):
        # Calculate the probability for each component
        probs = np.zeros(K)
        for j in range(K):
            exponent = -0.5 * np.sum((X[i] - mu[j]) ** 2) / var[j]
            coeff = (2 * np.pi * var[j]) ** (-d / 2)
            probs[j] = pi[j] * coeff * np.exp(exponent)

        # Sum over all components to get the total probability for this data point
        total_prob = np.sum(probs)
        log_likelihood += np.log(total_prob)

        # Calculate responsibilities (soft counts)
        post[i] = probs / total_prob

    return post, log_likelihood


def mstep(X: np.ndarray, post: np.ndarray) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    n, d = X.shape
    K = post.shape[1]

    # Update mixing proportions
    n_hat = np.sum(post, axis=0)  # shape (K,)
    p = n_hat / n

    # Update means
    mu = np.dot(post.T, X) / n_hat[:, np.newaxis]  # shape (K, d)

    # Update variances
    var = np.zeros(K)
    for j in range(K):
        diff = X - mu[j]
        var[j] = np.sum(post[:, j] * np.sum(diff**2, axis=1)) / (n_hat[j] * d)

    return GaussianMixture(mu, var, p)


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

    while prev_log_likelihood is None or log_likelihood - prev_log_likelihood > threshold * abs(log_likelihood):
        prev_log_likelihood = log_likelihood

        # E-step: Calculate responsibilities and log-likelihood
        post, log_likelihood = estep(X, mixture)

        # M-step: Update the parameters of the mixture model
        mixture = mstep(X, post)

    return mixture, post, log_likelihood


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
