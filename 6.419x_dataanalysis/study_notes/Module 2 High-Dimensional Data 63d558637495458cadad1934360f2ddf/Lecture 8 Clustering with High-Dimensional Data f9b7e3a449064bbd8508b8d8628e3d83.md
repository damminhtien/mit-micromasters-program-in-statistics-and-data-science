# Lecture 8: Clustering with High-Dimensional Data

> **Status: source-grounded summary.** This page paraphrases the local clustering lecture and makes the distance, objective, model-selection, and failure assumptions explicit.

Source: [local clustering lecture](../../lectures/M1%20L3%20Clustering%20of%20Hig-Dimensional%20Data.pdf).

## 1. What clustering means

Clustering seeks groups in unlabeled data such that observations within a group are similar and observations across groups are dissimilar. “Similar” is defined by a distance or dissimilarity; changing it can change the scientific conclusion.

For observations x_i in p dimensions, common distances include Euclidean, Manhattan, and maximum distance. Center and scale features when their units are not comparable, and question whether Euclidean distance remains meaningful when p is very large.

## 2. K-means

For a fixed K, K-means minimizes within-cluster squared Euclidean variation. With cluster assignments C_i and centroids mu_k, the objective is the sum over k and i assigned to k of squared distance from x_i to mu_k.

The algorithm alternates between assigning each point to its closest centroid and recomputing centroids. The global optimum is hard to find, so use multiple random restarts and record the seed. K-means favors roughly spherical clusters with similar scale and is sensitive to outliers.

The elbow heuristic runs several K values and looks for the point after the last large reduction in within-group sum of squares. It is a diagnostic, not a theorem.

## 3. Alternatives

- **PAM / k-medoids:** centers must be observed points, which can make the result more robust to outliers and easier to interpret.
- **Gaussian mixtures:** assume each cluster has a Gaussian distribution and estimate mixing weights and parameters, often with EM. Posterior assignments are soft; BIC can compare candidate K values.
- **Hierarchical clustering:** agglomerative methods merge clusters bottom-up and divisive methods split them top-down. Single, complete, and average linkage encode different between-cluster distances; choose a cut on the dendrogram later.
- **DBSCAN:** groups dense regions and can label sparse observations as noise. It is useful when clusters are not spherical but depends on neighborhood radius and minimum points.

## 4. Quality checks

For a point x_i, let a(i) be its average dissimilarity to its own cluster and b(i) the smallest average dissimilarity to another cluster. The silhouette score is s(i) = (b(i) - a(i)) / max(a(i), b(i)), between -1 and 1.

Large positive values suggest good separation; values near zero indicate overlap; negative values suggest a questionable assignment. Combine silhouette or elbow diagnostics with domain knowledge and stability across seeds, not with a single score alone.

## 5. High-dimensional failure modes

1. Distance concentration can make nearest and farthest points look similarly far away.
2. Unscaled high-variance features can dominate every cluster.
3. PCA or feature selection before clustering changes the geometry and must be documented.
4. A visually appealing 2-D t-SNE plot is not proof of global cluster structure.
5. Choosing K after inspecting held-out labels turns an unsupervised exercise into leakage.

The [high-dimensional project notebooks](../../projects/Analysis1.ipynb) and [clustering project](../../projects/Spectral_Clustering.ipynb) show how these ideas become code.
