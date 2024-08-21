from em import run
from common import GaussianMixture, init
import numpy as np
from common import GaussianMixture, init, rmse
from em import run, fill_matrix

# Load the complete and incomplete matrices
X_gold = np.loadtxt('netflix_complete.txt')
X_incomplete = np.loadtxt('netflix_incomplete.txt')


# Load the incomplete Netflix data
X = np.loadtxt('netflix_incomplete.txt')

# Define values of K and seeds
K_values = [12]
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

        X_pred = fill_matrix(X_incomplete, mixture)

        # Calculate the RMSE between the predicted and actual matrices
        error = rmse(X_gold, X_pred)
        print(f"RMSE = {error}")
