# Module 2: High-Dimensional Data

At the end of this lecture, you should be able to:

1. Recognize the different features of the three dimension reduction techniques: **principal component analysis (PCA), multi-dimensional scaling (MDS), and stochastic neighbor embedding (SNE)** .
2. Implement the PCA and the classical- MDS algorithms using elementary linear algebra.
3. Decide between using covariance and correlation for the dimension reduction analysis.
4. Explore how to use explained variance to choose the number of dimensions of the projection.
5. Describe **Stochastic Neighbor Embedding (SNE)** and **t-distributed Stochastic Neighbor Embedding (t-SNE)** as minimization of the Kullback-Leibler divergence (KL-divergence) between the probability distributions on data pairs in both the original high-dimensional and the target low-dimensional space.
6. Recognize that t-SNE alleviates crowding of data points in low-dimension.
7. Analyze the results of PCA, MDS, t-SNE together to identify patterns of the data.

### Lecture Goals and Key Concepts (generated)

1. **Recognize the different features of the three dimension reduction techniques: PCA, MDS, and SNE.**
    
    **Principal Component Analysis (PCA):** A linear dimensionality reduction technique that transforms the data into a new coordinate system where the greatest variances lie on the first coordinates (principal components).
    
    **Multi-Dimensional Scaling (MDS):** A technique used to place each object in N-dimensional space such that the between-object distances are preserved as well as possible.
    
    **Stochastic Neighbor Embedding (SNE):** A technique that minimizes the divergence between a probability distribution that measures pairwise similarity of the input objects and a probability distribution that measures pairwise similarity of the corresponding low-dimensional points.
    
2. **Implement the PCA and the classical-MDS algorithms using elementary linear algebra.**
    
    **PCA Implementation:**
    
    - Center the data by subtracting the mean of each feature.
    - Compute the covariance matrix.
    - Compute the eigenvectors and eigenvalues of the covariance matrix.
    - Sort the eigenvalues and their corresponding eigenvectors.
    - Select the top k eigenvectors to form a new subspace.
    
    **Classical MDS Implementation:**
    
    - Compute the pairwise distance matrix.
    - Apply double centering to the distance matrix to get the Gram matrix.
    - Compute the eigenvalues and eigenvectors of the Gram matrix.
    - Select the top k eigenvectors to form a new subspace.
3. **Decide between using covariance and correlation for the dimension reduction analysis.**
    
    **Covariance:** Measures the extent to which two variables change together. Use covariance when the scales of the variables are similar.
    
    **Correlation:** Measures the linear relationship between variables, standardized to fall between -1 and 1. Use correlation when the variables are on different scales.
    
4. **Explore how to use explained variance to choose the number of dimensions of the projection.**
    
    **Explained Variance:** The amount of variance captured by each of the principal components. Choose the number of dimensions such that the cumulative explained variance reaches a satisfactory threshold (e.g., 95%).
    
5. **Describe Stochastic Neighbor Embedding (SNE) and t-distributed Stochastic Neighbor Embedding (t-SNE) as minimization of the Kullback-Leibler divergence (KL-divergence) between the probability distributions on data pairs in both the original high-dimensional and the target low-dimensional space.**
    
    **SNE:** Uses a probability distribution to measure similarities between data points in high-dimensional space and aims to preserve these similarities in the low-dimensional embedding.
    
    **t-SNE:** An extension of SNE that uses a Student's t-distribution to measure similarities in the low-dimensional space, which helps to alleviate the crowding problem.
    
6. **Recognize that t-SNE alleviates crowding of data points in low-dimension.**
    
    **Crowding Problem:** In low-dimensional space, points tend to crowd together, making it difficult to distinguish between different clusters. t-SNE addresses this by using a t-distribution, which allows for better separation of points in the low-dimensional space.
    
7. **Analyze the results of PCA, MDS, t-SNE together to identify patterns of the data.**
    
    **Pattern Analysis:** By comparing the visualizations from PCA, MDS, and t-SNE, you can identify different aspects of the data structure, such as clusters, outliers, and relationships between variables.
    

### Detailed Explanation of Key Concepts

1. **Principal Component Analysis (PCA):**
    - **Key Concept:** PCA reduces the dimensionality of data by transforming the original data to a new set of variables (principal components) that are uncorrelated and ordered by the amount of variance they capture.
    - **Implementation:**
        - Center the data: \(X_{centered} = X - \mu\)
        - Compute the covariance matrix: \(C = \frac{1}{n-1} X_{centered}^T X_{centered}\)
        - Eigen decomposition: \(C = V \Lambda V^T\)
        - Select top k eigenvectors: \(V_k\)
        - Project data: \(X_{projected} = X_{centered} V_k\)
2. **Multi-Dimensional Scaling (MDS):**
    - **Key Concept:** MDS places each object in a low-dimensional space such that the pairwise distances are preserved as much as possible.
    - **Implementation:**
        - Compute the distance matrix: \(D_{ij} = \|x_i - x_j\|\)
        - Double center the distance matrix: \(B = -\frac{1}{2} H D^2 H\)
        - Eigen decomposition: \(B = V \Lambda V^T\)
        - Select top k eigenvectors: \(V_k\)
        - Project data: \(X_{projected} = V_k \Lambda_k^{\frac{1}{2}}\)
3. **Stochastic Neighbor Embedding (SNE) and t-SNE:**
    - **Key Concept:** SNE and t-SNE minimize the divergence between probability distributions of pairwise similarities in high-dimensional and low-dimensional spaces.
    - **Implementation of t-SNE:**
        - Compute pairwise affinities in high-dimensional space: \(p_{ij} = \frac{\exp(-\|x_i - x_j\|^2 / 2 \sigma^2)}{\sum_{k \neq l} \exp(-\|x_k - x_l\|^2 / 2 \sigma^2)}\)
        - Compute pairwise affinities in low-dimensional space: \(q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k \neq l} (1 + \|y_k - y_l\|^2)^{-1}}\)
        - Minimize KL divergence: \(KL(P \| Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}\)

### Related Knowledge or Questions

[1] Explain the concept of eigenvectors and eigenvalues and their role in PCA.
[2] Describe how to handle missing data in dimension reduction techniques.
[3] Discuss the computational complexity of PCA, MDS, and t-SNE.

Great work in exploring these complex concepts! Please let me know which related topic you would like to delve into further, or if you have any other questions.

# Introduction

Dimension reduction refers to a set of techniques which can transform high-dimensional data into their representative low-dimensional data. During the process, some information of the original data is discarded but some main characteristics of the original data is preserved.

Dimension reduction is important because processing and analyzing high-dimensional data can be computationally intractable. Dimension reduction is very useful in dealing with a large number of observations and variables, hence it is widely used in many fields such as signal processing, machine learning, and bioinformatics.

Three dimension reduction techniques will be introduced:

- Principal Component Analysis (PCA)
- Multidimensional Scaling (MDS), and
- Stochastic Neighbor Embedding (SNE).

PCA tries to project the original high-dimensional data into lower dimensions by capturing the most prominent variance in the data.

MDS is a technique for reducing data dimensions while attempting to preserve the relative distance between high-dimensional data points.

SNE is a non-linear technique to “cluster" data points by trying to keep similar data points close to each other.

PCA and classical MDS share similar computations: they both use the spectral decomposition of symmetric matrices, but on different input matrices.

You will think through some of the mathematics in this lecture. For demonstration of implementations, see the recitation at the end of this module.

# Lecture 1: Linear Algebraic Preparations

We will start with some linear algebra exercises before continuing with the lecture.

At the end of this series of exercises, you will be able to:

- Compute the **expectation** and **covariance matrix** of a random vector.
- Compute the **empirical mean** and **empirical covariance matrix** of a vector data set.
- Compute the **variance in a given direction** of a random vector.
- Compute the **empirical variance in a given direction** of a vector-valued sample.
- Describe the fundamental properties of **projection matrices** .
- State the **decomposition theorem** for symmetric matrices.

**Note:** These exercises were optional in the final ungraded unit on Principal Component Analysis in the course *Fundamentals of Statistics*. They are graded here. We encourage you to work on these again as a refresher.

[Lecture 6: Visualization of High-Dimensional Data](Module%202%20High-Dimensional%20Data%2063d558637495458cadad1934360f2ddf/Lecture%206%20Visualization%20of%20High-Dimensional%20Data%20ffe82eb00fa942139f7f627bc12dac0e.md)

[Lecture 7: Methods of Classification on High-Dimensional Data](Module%202%20High-Dimensional%20Data%2063d558637495458cadad1934360f2ddf/Lecture%207%20Methods%20of%20Classification%20on%20High-Dimens%2087923f6b12a44286b5dab9557c5c0e5d.md)

[Lecture 8: Clustering with High-Dimensional Data ](Module%202%20High-Dimensional%20Data%2063d558637495458cadad1934360f2ddf/Lecture%208%20Clustering%20with%20High-Dimensional%20Data%20f9b7e3a449064bbd8508b8d8628e3d83.md)