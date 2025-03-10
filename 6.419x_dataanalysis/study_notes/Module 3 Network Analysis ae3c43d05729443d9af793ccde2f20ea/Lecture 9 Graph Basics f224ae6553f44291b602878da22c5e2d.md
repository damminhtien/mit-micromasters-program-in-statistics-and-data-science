# Lecture 9: Graph Basics

In this lecture, we will

- Learn the definition of a **graph** and different types of graphs we will use.
- Learn what is an **adjacency matrix** and use it.
- Learn the following graph metrics: **connected components** , **degree distribution** , **path lengths** , **shortest paths** , **diameter** , **average distance** , **clustering coefficient** , and **modularity** .
- Learn how these graph metrics capture real-world notions about networks.

# **I. Graph Model**

A **graph** $G=(V,E)$ is a tuple of two sets $V$ and $E$, where

- $V$ is a set of **nodes** or **vertices** .
- $E$ is a set of **edges** or **links** representing relationships between the nodes in $V$. Each element of this set is either
    - a set $\{ i,j\}$ if the edge is undirected (as a set does not describe any order between the two vertices, so $\{ i,j\}\in E$ implies $\{ i,j\} =\{ j,i\} \in E)$;
    - a tuple $(i,j)$, if the edge is directed from $i$ to $j$ (thus $(i,j)\in E$ does not imply $(j,i)\in E$).

For example, a transportation network of **cities** and **roads** connecting the cities is a graph. In this case, cities are nodes in the graph and the roads connecting the cities are the edges in the graph.

In this module on network analysis we will learn some basic properties of different types of **graphs** . These properties will help us analyze network data and make sense of such data.

## Graph types

- A (directed) **walk** in a graph is a sequence of (directed) edges $(e_1,e_2,\ldots ,e_ k)$ such that every pair $(e_ i,e_{i+1})$ of edges shares a node, $v_ i$. The node (or vertex) sequence of this walk, $(v_0, v_1, \ldots , v_ k)$, is such that every pair $(v_{i-1}, v_ i)$ of nodes are connected by the (directed) edge $e_ i$.
- A (directed) **trail** is a walk where every edge in the sequence is unique.
- A (directed) **path** is a trail where every node in the node sequence is unique.
- A (directed) **cycle** is a (directed) trail that starts and terminates at the same node and such that **all other** nodes in the node sequence are unique.

| Simple network | Undirected network with at most one edge between any pair of vertices, and no self-loops. |
| --- | --- |
| Multigraph | May contain self-loops or multiple links between vertices. |
| Weighted network | Edges have weights or vertices have attributes. |
| Tree | A graph with no cycles. |
| Acyclic network | Graph with no directed cycles. |
| Bipartite | Vertices can be divided into two classes where there are no edges between vertices in the same class (but there can exist edges between vertices in different classes). |
| Hypergraph | Generalized edges which connect more than two vertices together. |

# II.  **Adjacency Matrix**

## **Definition of the adjacency matrix**

In this course module, the adjacency matrix, $A_{ij}$ will be defined as

$$
\displaystyle A_{ij}\displaystyle = 1\displaystyle \text { if there exists an edge from } i \text { to } j; \quad \displaystyle A_{ij}\displaystyle = 0\displaystyle \text { otherwise}
$$

For an undirected graph, $A_{ij} = 1$ implies that $A_{ji} = 1$.

For a directed graph, $A_{ij}$ and $A_{ji}$ are independent.

Note that another convention for the adjacency matrix exists, where $A_{ij} = 1$ implies an edge from $j$ to $i$. That convention will be not be used in this course, instead the above mentioned convention will be used.

## **Powers of the Adjacency Matrix**

**Theorem:** Let A be the adjacency matrix of an unweighted graph (could be directed/undirected, simple/multigraph). For any $\ell \ge 1$, $A^\ell$ contains the following elements: $A^\ell _{ij}$, which is the element in row $i$ and column $j$ of $A^\ell$, is the number of walks of length $\ell$ from node $i$ to node $j$.

**Proof:** The proof of this statement follows from induction with the following base cases: For $\ell = 1$, the statement is true by the definition of an adjacency matrix. For $\ell = 2$, let $r_ i$ be row i of A and $c_ j$ be column j of A. By definition, the entries of $r_ i$ are the number of walks of length 1 from node i to any other node. Similarly, the entries of $c_ j$ are the number of walks of length 1 from any other node to node j. Since entry $A^2_{ij}$ is the vector inner product of $r_ i$ and $c_ j$ it is then also equal to the number of walks of length 2 from node i to j via all possible intermediate nodes.

Inductively, we assume that $A^\ell _{kj}$ is equal to the number of walks with length $\ell$ from node k to node j. Then

$$
\displaystyle A^{\ell +1}_{ij}\displaystyle = \left[ A A^\ell \right]_{ij}\displaystyle = \sum _{k} A_{ik}A^\ell _{kj}.
$$

We can see now that $A_{ik}A^\ell _{kj}$ will be zero if there is no walk from i to k, and it will be equal to $A^\ell _{kj}$ if there is. Thus $A^{\ell +1}_{ij}$ is equal to the number of walks of length $\ell +1$ from node i to j and the proof is completed.

# **III. Graph Properties and Metrics**

## **1. Connected Components**

Given an **undirected graph** a **connected component** is a subset of nodes $V' \subset V$ such that the induced graph on $V'$ has the following properties: There exists a walk from $v_ i$ to $v_ j$ whenever $v_ i, v_ j \in V'$ and there is no walk from $v_ i$ to $v_ j$ whenever $v_ i \in V'$ and $v_ j \in V \setminus V'$.

The notion of a connected component as defined for an undirected graph does not translate directly to the case of a directed graph where walks have directions. In a **directed graph** a related notion we can define is **strong connectivity** . A set of nodes $V' \subset V$ is said to be **strongly connected** if every vertex in $V'$ is reachable from every other vertex in $V'$ and there exists some vertex in $V'$ and some vertex in $V \setminus V'$ such that there is no directed path between such vertices in at least one direction.

## **2. Power Law Distribution**

The **power law** distribution is defined by the following $\log-\log$ relationship between $k$ and $p_ k$:

$$
\displaystyle \log p_ k = -\alpha \log k + c, ~ ~ ~ \alpha ,c > 0.
$$

The distribution models scenarios that require the tail of the distribution to decay polynomially rather than exponentially. With a simple transformation, one can see that $p_ k$ decays as $k^{-\alpha }$.

## **3. Edge Density**

The **edge density** $\rho$ of a graph with n nodes and m edges is defined as $\displaystyle \rho = \frac{m}{{n \choose 2}}.$

Here ${n \choose k}$ is the binomial coefficient given by ${n \choose k}=\frac{n!}{k!(n-k)!}.$

This is a metric that captures the fraction of (all possible) edges present in an undirected graph.

## **4. Length of a Path, Diameter, and Average Distance**

Let $d_{ij}$ be the length of the shortest path (or the path with the smallest weight in the case of a weighted graph) between node i and j. The **diameter** of a graph is the largest distance between any two nodes:

$$
\displaystyle \text {diameter} = \text {max}_{i,j \in V}~ d_{i,j}.
$$

We can also define the notion of **average shortest path length** :

$$
\displaystyle \text {average path length} = \frac{1}{{n \choose 2}} \sum _{i \le j} d_{ij}.
$$

These notions are defined component-wise in case the graph is not connected. The definition of what constitutes a component, as we have seen before, varies between an undirected graph and a directed graph.

## **5. Triangle Density and Clustering Coefficient**

The **triangle density** of a graph is the ratio of number of triangles in the graph to the number of possible triangles:

$$
\displaystyle \text {triangle density} \triangleq \frac{\# \text { of triangles}}{{n \choose 3}}
$$

Triangle density is not an appropriate metric to measure clustering for several reasons. First, it does not take into account that the graph could have several connected components, in which case the denominator might be much larger than the numerator. Second, even in the case of a connected graph any three nodes need not be present in the same cluster (the shortest path lengths connecting them may be much larger).

A better metric for clustering is the **clustering coefficient** , denoted C, which measures the ratio of triangles in the network to the number of connected triples:

$$
\displaystyle C\displaystyle = \frac{\# \text { of closed triplets}}{\# \text { of closed and open triplets}}\displaystyle = \frac{3 \cdot \# \text { of triangles}}{\# \text { of connected triples}}.
$$

where an open triplet is three nodes connected by two edges, and a closed triplet is three nodes connected by three edges. This can be written in terms of the adjacency matrix as

$$
\displaystyle C\displaystyle = \frac{\sum _{i,j,k}A_{ij}A_{jk}A_{ki}}{\sum _ i k_ i (k_ i - 1)},
$$

where $k_ i = \sum _ j A_{ij}$ is the degree of node i.

To understand this formula, first consider the numerator. Note that $\sum _{i,j,k}A_{ij}A_{jk}A_{ki} = \sum _ i \left[ A^3 \right]_{ii} = \operatorname {tr}{A^3}$, that is, the trace of $A^3$. We know that $\left[ A^3 \right]_{ii}$ is equal to the number of walks of length 3 from node i to itself, which will be two if it is part of a closed triplet (there are two paths around the triplet) and zero otherwise. So the sum of the diagonal elements of $A^3$ is exactly twice the number of closed triplets (and six times the number of triangles, as each node in the triangle is counted once).

As for the denominator, let us examine how the degree of a node informs the number of connected triplets. If a node has degree zero, then it can't be part of a triplet, and the same is true for degree one. For a node of degree two, it must be part of one triplet (which may be closed or open). For degree three, the node is part of three triplets. We conclude that for a node of degree k, the node is part of ${k \choose 2} = k(k-1)/2$ connected triplets. Therefore the total number of connected triplets is the sum of this formula for all nodes: $\sum _ i k_ i (k_ i-1)/2$.

One can also define the same node-wise. For node i, the local clustering coefficient $C_ i$ is defined as

$$
\displaystyle C_ i\displaystyle = \frac{\# \text { of triangles at node }i}{\# \text { of connected triples centered at node }i}\displaystyle = \frac{\sum _{j,k} A_{ij}A_{jk}A_{ki}}{k_ i (k_ i - 1)}
$$

## **6. Modularity**

The **modularity** of an undirected graph with node types $t_ i, i = 1,\dots , n$ is defined as

$$
\displaystyle \frac{1}{2m} \sum _{i,j} \left(A_{ij} - \frac{k_ i k_ j}{2m}\right) \delta (t_ i,t_ j),
$$

where A is the adjacency matrix, m is the number of edges, and $\delta (t_ i,t_ j) = 1 if t_ i = t_ j$ and is equal to 0 if $t_ i \ne t_ j$. A few things to note:

- The definition of modularity is a little abstract, but the main thing to note here is that the expected number of edges between a node i with degree $k_ i$ and a node j with degree $k_ j$ in a random graph with m edges according to the *configuration model* (to be explained in a later lecture) is equal to $\frac{k_ i k_ j}{2m}$.
- For a given pair of nodes i,j, a positive value of $\left(A_{ij} - \frac{k_ i k_ j}{2m}\right) \delta (t_ i,t_ j)$ indicates that nodes i,j have an affinity that is more than the expected affinity that they would otherwise have in a truly random graph obtained according to the configuration model with given node types and m edges.
- Likewise, a negative value of $\left(A_{ij} - \frac{k_ i k_ j}{2m}\right) \delta (t_ i,t_ j)$ indicates that nodes i,j have lesser than expected affinity when compared to a random graph with the same characteristics.