"""Mixture model for matrix completion"""
from typing import Tuple
import numpy as np
from scipy.special import logsumexp
from common import GaussianMixture


def estep(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step: Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data
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


def fill_matrix(X: np.ndarray, mixture: GaussianMixture) -> np.ndarray:
    """Fills an incomplete matrix according to a mixture model

    Args:
        X: (n, d) array of incomplete data (incomplete entries =0)
        mixture: a mixture of gaussians

    Returns
        np.ndarray: a (n, d) array with completed data
    """
    raise NotImplementedError
