# Lecture 11: Spectral Clustering

# Motivation

In this lecture, we will

- Describe the use and purpose of **Steiner trees** .
- Learn how to construct an **approximate Steiner tree** solution.
- Introduce the notion of **clustering**.
- Introduce **graph Laplacian** matrix.
- Conceptualize mathematically an **ideal** version of clustering as an optimization problem.
- Relax the ideal clustering problem to obtain a computationally tractable problem.
- Understand the importance of **eigenvalues and eigenvectors** of the graph Laplacian and learn **spectral clustering** .
- Introduce **modularity maximization** for the purpose of clustering.

### Steiner Trees

- **Use and Purpose**: The Steiner tree problem seeks to connect a given set of nodes (called terminals) in a weighted graph with the minimum total edge weight. This is useful in network design, such as minimizing the cost of laying cables or pipelines connecting specific locations.
- **Application**: Useful in designing efficient networks in telecommunications, transportation, and logistics, where minimizing infrastructure cost is crucial.

### Approximate Steiner Tree Solution

- **Construction**: Constructing an exact Steiner tree is an NP-hard problem, meaning it's computationally infeasible for large graphs. Approximate solutions are therefore used, employing heuristics and algorithms that provide near-optimal solutions within a reasonable time frame.
- **Example Algorithms**: Examples include the Minimum Spanning Tree (MST) heuristic, which connects terminals using an MST and then prunes unnecessary edges.

### Clustering

- **Definition**: Clustering involves grouping nodes in a graph such that nodes within the same cluster are more densely connected to each other than to nodes in other clusters. This technique is used to identify community structures within networks.
- **Application**: Clustering is widely used in social network analysis, image segmentation, pattern recognition, and bioinformatics to identify natural groupings in data.

### Graph Laplacian Matrix

- **Introduction**: The graph Laplacian is a matrix representation of a graph that is used to study its properties. For a graph G with n nodes, the Laplacian matrix L is defined as L = D - A, where D is the degree matrix (a diagonal matrix where each diagonal element $d_{ii}$ is the degree of node i), and A is the adjacency matrix of the graph.
- **Importance**: The graph Laplacian is fundamental in many graph algorithms and is closely linked to the graph's spectral properties, which are crucial for tasks like clustering.

### Ideal Clustering as an Optimization Problem

- **Conceptualization**: Mathematically, ideal clustering aims to partition a graph into k clusters such that the intra-cluster edges are maximized and inter-cluster edges are minimized. This can be framed as an optimization problem, typically involving the minimization of a cut function.
- **Challenge**: The ideal clustering problem is often NP-hard, making it difficult to solve exactly for large graphs.

### Relaxation of the Clustering Problem

- **Purpose**: To make the clustering problem computationally tractable, it is relaxed into a form that can be solved using efficient algorithms. This involves approximations or simplifications that transform the original NP-hard problem into one that can be handled by polynomial-time algorithms.
- **Methods**: Techniques like spectral clustering and semi-definite programming are used to relax the clustering problem.

### Eigenvalues and Eigenvectors of the Graph Laplacian

- **Importance**: The eigenvalues and eigenvectors of the graph Laplacian provide deep insights into the structure of the graph. The smallest eigenvalues and their corresponding eigenvectors are particularly important for clustering and partitioning the graph.
- **Spectral Clustering**: This clustering method uses the eigenvectors of the graph Laplacian to perform dimensionality reduction before applying a traditional clustering algorithm (like k-means). It leverages the properties of the Laplacian's eigenvalues and eigenvectors to find a good approximation to the optimal clustering.

### Modularity Maximization

- **Purpose**: Modularity is a measure of the strength of the division of a network into clusters (or communities). High modularity indicates dense connections within clusters and sparse connections between clusters.
- **Method**: Modularity maximization involves finding a division of the network that maximizes the modularity score. This is an NP-hard problem, so heuristic methods like the Louvain algorithm are commonly used to find high-modularity partitions.
- **Application**: Used in network science to detect community structures in social networks, biological networks, and other complex systems.

# I. Introduction to Steiner trees

When examining a network, we may have identified a few nodes of particular interest. We may then want to ask the question: what is the smallest sub-network that connects all of these interest nodes? If we define “smallest" to mean the sum of all edge weights in the sub-network, then the this problem is known as the Steiner tree problem in graphs.

For example, we may have a weighted graph where each node is a city, and the weighted edges represent the costs to build an electrical distribution line between the connected cities. If the goal is to connect all cities on the graph while minimizing costs, then we should find the minimum spanning tree of the graph — which can be done in polynomial time.

However, suppose the goal is instead to connect just a few nodes of this graph together at minimum cost, perhaps due to a mandate or government contract. Then, the problem is the Steiner tree problem, and the computational complexity for finding the solution is NP-hard.

The cities that must be connected are called the terminals of the graph. The difficulty of the problem comes from the need to decide which additional cities should be used to create the subgraph that connects these terminals. If the mandate specified a few cities, and required that no other cities should be connected, then we could just discard the remaining nodes from the graph and the problem reduces to the minimum spanning tree.

# **II. Graph Laplacian**

We now introduce the **graph Laplacian matrix** of a graph. Throughout the remainder of this lecture, we assume only that the graph is *simple and undirected*. Everything discussed here also works for undirected, *weighted*, simple graphs.

The **graph Laplacian matrix** L is defined as $\displaystyle L = D-A,$ where $A$ is the adjacency matrix and $D$ is the degree matrix. The **degree matrix** for an undirected, unweighted graph is a matrix whose off-diagonal elements are equal to 0 and whose diagonal elements are given by $\displaystyle D_{ii} = \sum _{j} A_{ij}.$

In other words, the degree matrix of an undirected, unweighted, simple graph is simply a diagonal matrix whose diagonal entries are the degrees of the nodes. In the case of a weighted, undirected, simple graph the definition is the same but the interpretation no longer concerns the degree of the nodes, but rather the sum weight of the edges emanating from the nodes.

# **III. Ideal Clustering**

### Goal of Clustering

The goal of clustering in this module is to identify groups of nodes in a graph that are more densely connected within themselves compared to their connections to nodes outside the group. This involves minimizing the inter-group edges while maximizing the intra-group edges.

### Clustering into Two Subsets

To this end, let us first consider clustering of nodes into two clusters. Let us split an $n$-node graph into two subsets each of size $n_1$ and $n_2$ such that the goal is to minimize the sum of weights of links between them. Define $s_ i, i=1,\dots ,n$ as 

$$
\displaystyle s_ i = \begin{cases} 1& ~ ~ \text {if vertex } i \text { belongs to group 1,}\\ -1& ~ ~ \text {if vertex } i \text { belongs to group 2.} \end{cases}
$$

Then, let us define the optimization problem to obtain an optimal clustering as 

$$
\displaystyle C= \min _{\mathbf{s} \in \{ -1,1\} ^ n} \sum _{i,j} A_{i,j} (1-s_ i s_ j), ~ ~ ~ \text {such that } \sum _ k s_ k = n_1-n_2.
$$

**Self exercise:** Show that we can equivalently write the above optimization problem as

$$
\displaystyle C= \min _{\mathbf{s} \in \{ -1,1\} ^ n} \mathbf{s}^ T L \mathbf{s}, ~ ~ ~ \text {such that } \sum _ k s_ k = n_1-n_2,
$$

where $L$ is the graph Laplacian.

**Solution**

1. Original Objective Function: ****$C = \min_{\mathbf{s} \in \{ -1,1\}^n} \sum_{i,j} A_{i,j} (1 - s_i s_j)$
2. Expanding the Sum: **$\sum_{i,j} A_{i,j} (1 - s_i s_j) = \sum_{i,j} A_{i,j} - \sum_{i,j} A_{i,j} s_i s_j$**
3. Graph Properties:
    - $\sum_{i,j} A_{i,j}$ is the sum of all edge weights in the graph.
    - $\sum_{i,j} A_{i,j} s_i s_j$ relates to how $s$ aligns with the graph structure.
4. Simplifying**:** Since the term $\sum_{i,j} A_{i,j}$ is constant with respect to $\mathbf{s}$, we focus on minimizing $\sum_{i,j} A_{i,j} s_i s_j$
5. Using Graph Laplacian: ****The graph Laplacian $L$ is defined as: $L = D - A$ where $D$ is the degree matrix and $A$ is the adjacency matrix.
    
    The quadratic form involving the Laplacian is: $\mathbf{s}^T L \mathbf{s} = \mathbf{s}^T (D - A) \mathbf{s} = \mathbf{s}^T D \mathbf{s} - \mathbf{s}^T A \mathbf{s}$ 
    
6. Quadratic Form:
Since $D$ is diagonal with $D_{ii} = \sum_j A_{ij}$, so $\mathbf{s}^T D \mathbf{s} = \sum_i s_i^2 \sum_j A_{ij} = \sum_i \sum_j A_{ij} s_i^2$ 
Because $s_i^2 = 1$, so $\mathbf{s}^T D \mathbf{s} = \sum_i \sum_j A_{ij} = \sum_{i,j} A_{ij}$ 
    
    For $\mathbf{s}^T A \mathbf{s}$:  $\mathbf{s}^T A \mathbf{s} = \sum_{i,j} A_{ij} s_i s_j$ 
    
    Thus:  $\mathbf{s}^T L \mathbf{s} = \sum_{i,j} A_{ij} - \sum_{i,j} A_{ij} s_i s_j$ 
    
    This matches the form $\sum_{i,j} A_{i,j} (1 - s_i s_j)$.
    

# **IV. Relaxation of Ideal Clustering**

The optimization problem for a given $n_1,n_2$

$$
\displaystyle C= \min _{\mathbf{s} \in \{ -1,1\} ^ n} \mathbf{s}^ T L \mathbf{s}, ~ ~ ~ \text {such that } \sum _ k s_ k = n_1-n_2,
$$

is computationally hard to solve for any real-life graph of decent size. We can therefore relax the integer constraints on the $\mathbf{s}$ vector and consider the relaxed problem

$$
\displaystyle \hat{C}= \min _{\mathbf{x} \in \mathbb {R}^ n} \mathbf{x}^ T L \mathbf{x},~ ~ \| \mathbf{x}\| =1.
$$

where we have also ignored the constraint that the components of $\mathbf{x}$ have to sum up to $n_1-n_2$. The normalization of $\mathbf{x}$ is necessary or otherwise there is only one trivial solution to the problem – the all-zeros vector.

**Spectral Clustering: Eigenvector Corresponding to Second Smallest Eigenvalue**

The relaxed problem leads to an approximate but intuitive solution to the ideal clustering problem.

**Self-exercise:** First, we can show that $\displaystyle \mathbf{x}^ T L \mathbf{x} = \frac{1}{2} \sum _{i,j} A_{ij} (x_ i-x_ j)^2.$

**Derivation**

$$
\displaystyle \displaystyle x^ TLx\displaystyle = \sum _{i,j=1}^ n L_{ij}x_ ix_ j\displaystyle =\sum _{i,j=1}^ n (D_{ij}-A_{ij})x_ ix_ j\displaystyle =\sum _{i=1}^ n D_{ii}x_ i^2 - \sum _{i,j=1}^ n A_{ij}x_ ix_ j\displaystyle =\frac{1}{2}\sum _{i=1}^ n D_{ii}x_ i^2 + \frac{1}{2}\sum _{j=1}^ n D_{jj}x_ j^2 - \sum _{i,j=1}^ n A_{ij}x_ ix_ j\displaystyle =\frac{1}{2}\sum _{i,j=1}^ n A_{ij}(x_ i^2+x_ j^2-2x_ ix_ j)\displaystyle = \frac{1}{2}\sum _{i,j=1}^ n A_{ij}(x_ i-x_ j)^2,
$$

where we use the fact that $D_{ii}=\sum _{j=1}^ n A_{ij}, and D_{jj}=\sum _{i=1}^ n A_{ij}$

Minimizing the above would lead to a solution $\mathbf{x}$ that can be interpreted as follows: In the original ideal clustering setup, the multiplier to $A_{ij}$ is equal to 0 when two nodes $i,j$ belong to the same cluster. The same way, we can treat any two nodes $i,j$ whose $x_ i,x_ j$ values are close as being in the same cluster. And, if the $x_ i,x_ j$ values are far apart we can classify them into different clusters.

Beyond this intuitive understanding of the relaxed problem, the relaxed problem also has important properties. First the graph Laplacian $L$ is a symmetric matrix. Then, using the above expansion we can clearly see that if $A_{ij} \ge 0,~ \forall i,j$ (which is the likely scenario in most applications) $L$ is a **positive semi-definite** matrix. For a positive semidefinite matrix, the eigenvalues are nonnegative.

In particular, for the Laplacian the smallest eigenvalue is equal to 0. This can be seen from the fact that $\displaystyle L \mathbf{1} = 0,$ where $\mathbf{1}$ is a vector of ones. 

**Self-exercise:** It can also be shown that the multiplicity of the zero eigenvalue is the number of connected components of the simple, undirected graph.

Getting back to the optimization problem

$$
\displaystyle \hat{C}= \min _{\mathbf{x} \in \mathbb {R}^ n} \mathbf{x}^ T L \mathbf{x},~ ~ \| \mathbf{x}\| =1,
$$

we now know that the optimal value of this problem is equal to 0 since there is an eigenvector (which can be normalized) with 0 eigenvalue. This solution is not satisfying for our clustering since the eigenvector(s) corresponding to the zero eigenvalue(s) pick out essentially the connected components of the graph. In particular, if there is only one component in the graph then $\mathbf{1}$ is the optimal vector that obtains the optimal cost of $\hat{C} = 0$ and this vector provides no information as to how to pick out different clusters in the graph.

Let $0=\lambda _1 \le \lambda _2 \le \dots \le \lambda _ n$ be the n eigenvalues of $L$ and let $\hat{\lambda }$ be the second smallest eigenvalue or the smallest non-zero eigenvalue of $L$. If there is only one connected component in the graph, this value is also equal to $\lambda _2$. The eigenvector corresponding to this eigenvalue, denoted $\hat{\mathbf{x}}$, turns out to be a good heuristic vector to cluster the graph according to the following rule: nodes whose corresponding $x_ i$ values are close to each other can be assigned a cluster. We can use this procedure to obtain any number of clusters that we wish to in the graph. With $\hat{\mathbf{x}}$ the cost of the relaxed clustering problem becomes $\hat{\mathbf{x}}^ T L \hat{\mathbf{x}}$.

# **V. Modularity Maximization**

**Modularity** is a measure of the strength of the division of a network into clusters (or communities). It quantifies how well a network decomposes into densely connected subgroups, which have sparse connections between them. The goal of **modularity maximization** is to find a partition of the network that maximizes this modularity measure, indicating a strong community structure.

### Modularity Formula

For a given partition of the graph, modularity $Q$ is defined as:

$$
Q = \frac{1}{2m} \sum_{i,j} \left[ A_{ij} - P_{ij} \right] \delta(c_i, c_j)
$$

Where:

- $A_{ij}$ is the adjacency matrix of the graph.
- $P_{ij}$ is the expected number of edges between nodes $i$ and $j$ in a random graph model with the same degree distribution.
- $\delta(c_i, c_j)$ is 1 if nodes $i$ and $j$ are in the same community, and 0 otherwise.
- $m$ is the total number of edges in the graph.
- $c_i$ is the community to which node $i$ belongs.

### Modularity Maximization Objective

The problem of maximizing modularity can be formulated as:

$$
C = \max_{\mathbf{s} \in \{ -1, 1\}^n} \sum_{i,j} B_{i,j} (1 + s_i s_j), \quad \text{where } B_{ij} = A_{ij} - P_{ij}, \quad \text{such that } \sum_k s_k = n_1 - n_2.
$$

Here:

- $s_i$ is 1 if node $i$ belongs to group 1 and -1 if it belongs to group 2.
- $B_{ij}$ is the modularity matrix defined as $B_{ij} = A_{ij} - P_{ij}$.

### Random Graph Models

$P_{ij}$ is the expected number of edges between nodes $i$ and $j$ in a random graph model. Different models provide different expectations:

- **Erdos-Renyi Model**: Each pair of nodes is connected with a fixed probability $p$, leading to $P_{ij} = \frac{2m}{n(n-1)}$.
- **Configuration Model**: Nodes are connected based on a given degree sequence, leading to $P_{ij} = \frac{k_i k_j}{2m-1}$, where $k_i$ is the degree of node $i$.

### Reformulation Using Modularity Matrix

1. **Objective Function**:
The modularity maximization can be reformulated to find the optimal partition by maximizing the following: $C = \max_{\mathbf{s} \in \{ -1, 1\}^n} \sum_{i,j} B_{ij} (1 + s_i s_j)$
2. **Modularity Matrix**:
The modularity matrix $B$ captures the difference between the actual adjacency matrix $A$ and the expected adjacency matrix $P$.
3. **Partition Vector**:
The partition vector $\mathbf{s}$ indicates the cluster assignment for each node, and the objective function sums up the contributions of pairs of nodes based on their modularity value and whether they are in the same cluster.

The problem of finding the exact solution to modularity maximization is NP-hard, meaning it is computationally infeasible for large graphs. Therefore, approximate algorithms and heuristics are used.

### Approximation Methods - Louvain Method

One of the most popular methods for approximate modularity maximization is the **Louvain method**, introduced by Blondel et al. in 2008. The Louvain method is an efficient heuristic for community detection in large networks.

1. **Initialization**: Each node starts in its own community.
2. **Phase 1 - Local Modularity Optimization**:
    - For each node, move it to the community of one of its neighbors if this move increases the modularity.
    - Repeat until no further improvement is possible.
3. **Phase 2 - Community Aggregation**:
    - Aggregate nodes belonging to the same community into a single node.
    - Build a new network where nodes represent communities from the previous phase.
4. **Repeat**: Repeat phases 1 and 2 on the new aggregated network until no further improvement is possible.

### Summary

Modularity maximization is a powerful approach for detecting community structure in networks. By maximizing modularity, we can identify clusters of nodes that are more densely connected internally than with the rest of the network. This approach is computationally challenging, but approximate methods like the Louvain algorithm provide efficient and effective solutions for large networks. Understanding modularity and its maximization is crucial for network analysis in various domains, including social networks, biological networks, and infrastructure networks.