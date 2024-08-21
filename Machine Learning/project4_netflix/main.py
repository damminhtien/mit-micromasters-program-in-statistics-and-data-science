import numpy as np
import common
import kmeans
import naive_em
import em

# Load the 2D toy dataset
X = np.loadtxt('toy_data.txt')

# K_values = [1, 2, 3, 4]
# seeds = [0, 1, 2, 3, 4]
# best_costs = []

# for K in K_values:
#     best_cost = float('inf')
#     best_mixture = None

#     for seed in seeds:
#         np.random.seed(seed)

#         # Initialize mixture and post
#         mixture, post = common.init(X, K, seed)

#         # Run the K-means algorithm
#         mixture, post, cost = kmeans.run(X, mixture, post)

#         if cost < best_cost:
#             best_cost = cost
#             best_mixture = mixture

#     # Save the best cost for the current K
#     best_costs.append(best_cost)

#     # Plot the best mixture model for the current K
#     common.plot(X, best_mixture, post, f'K={K}_best_plot.png')

#     print(f"Best cost for K={K}: {best_cost}")

# # Report the best costs for each K
# print(f"Cost|_K=1 = {best_costs[0]}")
# print(f"Cost|_K=2 = {best_costs[1]}")
# print(f"Cost|_K=3 = {best_costs[2]}")
# print(f"Cost|_K=4 = {best_costs[3]}")

K_values = [1, 2, 3, 4]
seeds = [0, 1, 2, 3, 4]
best_bic = float('-inf')
best_K = None

for K in K_values:
    best_log_likelihood = float('-inf')
    best_mixture = None
    best_post = None

    for seed in seeds:
        np.random.seed(seed)

        # Initialize mixture and post
        mixture, post = common.init(X, K, seed)

        # Run the EM algorithm
        mixture, post, log_likelihood = em.run(X, mixture, post)

        if log_likelihood > best_log_likelihood:
            best_log_likelihood = log_likelihood
            best_mixture = mixture
            best_post = post

    # Compute BIC for the best model found
    current_bic = common.bic(X, best_mixture, best_log_likelihood)

    if current_bic > best_bic:
        best_bic = current_bic
        best_K = K

    print(f"BIC for K={K}: {current_bic}")

# Report the best K and best BIC
print(f"Best K = {best_K}")
print(f"Best BIC = {best_bic}")
