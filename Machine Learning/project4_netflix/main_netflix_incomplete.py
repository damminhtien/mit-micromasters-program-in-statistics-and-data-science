import numpy as np
from common import GaussianMixture, init
from em import run

# Load the incomplete Netflix data
X = np.loadtxt('netflix_incomplete.txt')

# Define values of K and seeds
K_values = [1, 12]
seeds = [0, 1, 2, 3, 4]
best_log_likelihoods = {}

for K in K_values:
    best_log_likelihood = float('-inf')
    
    for seed in seeds:
        np.random.seed(seed)
        
        # Initialize the mixture and post
        mixture, post = init(X, K, seed)
        
        # Run the EM algorithm
        mixture, post, log_likelihood = run(X, mixture, post)
        
        # Track the best log-likelihood
        if log_likelihood > best_log_likelihood:
            best_log_likelihood = log_likelihood
    
    best_log_likelihoods[K] = best_log_likelihood
    print(f"Best log-likelihood for K={K}: {best_log_likelihood}")

# Reporting the results
print(f"Log-likelihood|_K=1 = {best_log_likelihoods[1]}")
print(f"Log-likelihood|_K=12 = {best_log_likelihoods[12]}")
