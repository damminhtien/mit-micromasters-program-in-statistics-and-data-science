import numpy as np
import common
import kmeans

# Load the 2D toy dataset
X = np.loadtxt('toy_data.txt')

K_values = [1, 2, 3, 4]
seeds = [0, 1, 2, 3, 4]
best_costs = []

for K in K_values:
    best_cost = float('inf')
    best_mixture = None

    for seed in seeds:
        np.random.seed(seed)

        # Initialize mixture and post
        mixture, post = common.init(X, K, seed)

        # Run the K-means algorithm
        mixture, post, cost = kmeans.run(X, mixture, post)

        if cost < best_cost:
            best_cost = cost
            best_mixture = mixture

    # Save the best cost for the current K
    best_costs.append(best_cost)

    # Plot the best mixture model for the current K
    common.plot(X, best_mixture, post, f'K={K}_best_plot.png')

    print(f"Best cost for K={K}: {best_cost}")

# Report the best costs for each K
print(f"Cost|_K=1 = {best_costs[0]}")
print(f"Cost|_K=2 = {best_costs[1]}")
print(f"Cost|_K=3 = {best_costs[2]}")
print(f"Cost|_K=4 = {best_costs[3]}")
