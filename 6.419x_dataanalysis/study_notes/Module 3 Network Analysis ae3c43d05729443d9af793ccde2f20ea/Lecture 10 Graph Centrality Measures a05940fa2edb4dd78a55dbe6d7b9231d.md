# Lecture 10: Graph Centrality Measures

In this lecture, we will

- Introduce the notion of **centrality** .
- Introduce **degree centrality** and **eigenvector centrality** and study approaches to computing these measures.
- Understand how eigenvector centrality does not work for **directed acyclic graphs (DAGs)** and introduce **Katz centrality** as a better notion of centrality than eigenvector centrality.
- Further introduce **page-rank centrality** to fix issues with Katz centrality.
- Combine inward and outward importances in one iterative algorithm to compute **hubs and authorities** scores of nodes in a graph.
- Introduce **closeness** and **betweenness** centrality and learn how to compute them.

# **I. Centrality Measures – Introduction**

## 1. Find important nodes

Centrality measure: a measure that captures importance of a nodes’s position in the network

There are many different centrality measures:

- degree centrality (indegree/ outdegree)
- “propagated” degree centrality (score that is proportional to the sum of the score of all neighbors)
- closeness centrality
- betweeness centrality

Choice of centrality measure depends on application!

In a friendship network:

- high degree centrality: most popular person
- high eigenvector centrality: most popular person that is friends with popular people
- high closeness centrality: person that could best inform the group
- high betweeness centrality: person whose removal could best break the network apart

## 2. Degree centrality

The **degree centrality** measures the importance of nodes in terms of the degree of a node. For a directed graph, define the in-degree $k_ i^{\text {in}}$ and the out-degree $k_ i^{\text {out}}$ of a node to be the sum over the ith column or the row of the adjacency matrix respectively:

$$
\displaystyle k_ i^{\text {in}} = \sum _ j A_{ji}, ~ ~ ~ ~ k_ i^{\text {out}} = \sum _ j A_{ij}.
$$

Note that (unlike in the slides) we use the convention where $A_{ij}=1$ indicates an edge going **from node i to node j**. The convention used can differ in different fields applications.

The degree centrality only captures importance up to one-hop neighbors of a node. Depending upon the application, this may not be representative of the importance of a node in the overall graph.

### High Degree

Let an undirected graph have n nodes. Let the edges be selected according to the following random model: every possible edge (including self loop) is present with probability p independent of every other edge.

There is an inequality, known as the *Markov inequality*, that gives an upper bound on the tail probability of a non-negative random variable:

Let X be a nonnegative random variable and $\epsilon > 0$, then $P(X \ge \epsilon ) \le \frac{\mathbb {E}[X]}{\epsilon }.$

1. Using Markov inequality, obtain an upper bound on the probability that, for any given node, there are at least n-1 edges connected to this node in this graph.

Let X represent the random variable that is the number of edges connected to a node in this graph generation model. X is a binomial random variable with parameters n,p. The expected value of a binomial random variable is np. Therefore, $\displaystyle P(X \ge n-1) \le \frac{np}{n-1}.$

1. Now, find the exact probability that, for any given node, there are at least n-1 edges connected to this node in this graph.

This probability is equal to

$$
\displaystyle P(X \ge n-1)\displaystyle = P_{\text {Binomial}(n,p)}(n-1) + P_{\text {Binomial}(n,p)}(n)\displaystyle = n \cdot p^{n-1} (1-p) + p^ n
$$

## 3. Closeness and betweeness centrality

### Closeness centrality

**Closeness centrality** tracks how close a node is to any other node

$$
C_i=(\frac{1}{n-1}\sum_{j \neq i}d_{ij})^{-1}
$$

where $d_{ij}$ is the distance between nodes i and j.

In disconnected networks: average over nodes in same component as i or use **Harmonic centrality**:

$$
H_i=\frac{1}{n-1}\sum_{i \neq j} \frac{1}{d_{ij}}
$$

### Betweeness centrality

**Betweeness centrality** measures the extent to which a node lies on paths between other nodes

$$
B_i=\frac{1}{n^2}\sum_{s,t}\frac{n^i_{st}}{g_{st}}
$$

where $n_{st}^i$ is number of shortest path between s and t that pass through i, and $g_{st}$ is total number of shortest paths between s and t.

# II. Eigenvector Centrality

## **1. Eigenvalues and Eigenvectors**

For a matrix of size $n \times n$ a value $\lambda$ is called an **eigenvalue** that corresponds to an **eigenvector** $\mathbf{x}$ if $\displaystyle A\mathbf{x} = \lambda \mathbf{x}.$

Technically, the vector $\mathbf{x}$ in the above is a right eigenvector of A. One can also define a left eigenvector as a row vector $\mathbf{y}^ T$ that satisfies $\mathbf{y}^ TA = \lambda ' \mathbf{y}^ T$ for a corresponding eigenvalue $\lambda '$. Note that all vectors are column vectors and hence $\mathbf{y}^ T$ is a row vector.

## **2. Eigenvector Centrality**

The **eigenvector centrality** of a node is the weighted importance of the nodes pointing to it (left eigenvector centrality) or the nodes that it points to (right eigenvector centrality). Let us consider, for sake of simplicity, the left eigenvectors in this discussion and the description for the case of right eigenvectors follows in a similar fashion with the interpretation that the importance of a particular node captured using right eigenvectors is an indication of how important the neighbors it points to are.

We define **eigenvector centrality** for a directed graph using the left eigenvector corresponding to the largest eigenvalue of all left eigenvectors. Formally, let $\mathbf{v}^ T$ be the left eigenvector corresponding to the largest left eigenvalue $\lambda _{\text {max}}$. Then, the eigenvector centrality of node i is the value at the $i^{\text {th}}$ index of $\mathbf{v}$ and is denoted $v_ i$.

The interpretation of eigenvector centrality is that the ranking of a particular node i satisfies

$$
\displaystyle \sum _ j v_ j A_{ji}\displaystyle = \lambda _{\text {max}} v_ i
$$

and this implies

$$
\displaystyle v_ i = \frac{1}{ \lambda _{\text {max}}} \sum _ j v_ j A_{ji}.
$$

To understand the role of the eigenvector corresponding to the largest eigenvalue in defining centrality of a node based on the centrality of its neighbors, we turn to the Perron-Frobenius theorem. Let $\mathbf{y}^0 = \mathbf{1}$ denote the assginment of same centrality value to all the nodes. Let

$$
\displaystyle \left(\mathbf{y}^ k\right)^ T = \left(\mathbf{y}^0\right)^ T A^ k
$$

denote the updated (left) centrality vector after k iterations of updating the centrality of every node based on the centrality of its neighbors. We can show, under some conditions of the adjacency matrix A, that

$$
\displaystyle \text {as } k \to \infty , ~ ~ \left(\frac{\mathbf{y}^ k}{\lambda _{\text {max}}^ k}\right)^ T \to \alpha \mathbf{v}^ T.
$$

The value $\lambda _{\text {max}}$ is the largest eigenvalue of A and $\mathbf{v}^ T$ is its corresponding left eigenvector. The constant $\alpha$ depends upon the choice of the initial centrality vector. Perron-Frobenius theorem ensures that the eigenvector $\mathbf{v}^ T$, which corresponds to the largest eigenvalue, is a non-negative, non-zero vector. This satisfies a key requirement that our ranking of importance of every node be non-negative and that there is at least one node that has a non-zero importance.

For these exercises we will require that the left eigenvectors be normalized as follows: $\sqrt{\sum _ i v_ i^2} = 1,$ as not all linear algebra libraries use the same normalization conventions.

### Interpretation

- node is important if it has important neighbors
- node is important if it has many neighbors
- eigenvector corresponding to largest eigenvalue of A provides a ranking of all nodes

What happens when G is directed?

- right eigenvector: $v_i=\frac{1}{\lambda_{max}}\sum_{j=1}^nA_{ij}v_{j}$
    - importance comes from nodes i points to
    - Example: determining malfunctioning genes
- left eigenvector: $w_i=\frac{1}{\lambda_{max}}\sum_{j=1}^nw_jA_{ji}$
    - important comes from nodes pointing to i
    - Example: ranking websites

# III. **Katz Centrality**

There is an issue with eigenvector centrality. Consider the adjacency matrix of a **directed, acyclic graph (DAG)** . A DAG is a directed graph with no cycles (no self loops as well). The issue with eigenvector centrality in the case of DAGs is that the adjacency matrix A of a DAG has the property that $A^\ell$ contains all entries equal to 0 for some value $\ell$ (and hence for all values greater than $\ell$). This leads to an issue in the application of the Perron-Frobenius theorem that we alluded to in the definition of eigenvector centrality – there is no convergence to a non-zero vector in the series of updates starting with an initial centrality vector. In particular, $\left(\mathbf{y}^ k\right)^ T \to \mathbf{0}^ T as k \to \infty$.

This leads **Katz centrality** , a centrality measure that corrects this issue with eigenvector centrality in the case of DAGs. 

The update equation is modified to be $\displaystyle \left(\mathbf{y}^{k+1}\right)^ T = \alpha \left(\mathbf{y}^ k\right)^ T A + \beta \mathbf{1}^ T,$ where $\alpha$ is chosen in the interval $(0,1/\lambda _{\text {max}}(A))$. 

We can show that with this update equation $\displaystyle \text {as } k \to \infty , ~ ~ ~ \left(\mathbf{y}^ k\right)^ T \to \mathbf{v}^ T,$ where $\mathbf{v}^ T = \beta \mathbf{1}^ T (\mathbf{I} - \alpha A)^{-1}$. For the case of DAGs, $\lambda _{\text {max}} = 0$ and hence we can simply choose any value of $\alpha$; for example, $\alpha = 1$.

# IV. Page Rank

Katz centrality and eigenvector centrality assign a relatively high importance value to a node i that has an incoming edge from a node j that is of high importance and has no other incoming edges. If node j has a very high out-degree then node i is just one of the many neighbors that node j points to. In some applications, we may require that such a node i not have very high importance simply because it has an incoming edge from a node of very high importance.

**Page-rank centrality** modifies Katz centrality to obtain a centrality measure that addresses this requirement. In particular, page-rank centrality weighs the contributions of all neighbors of a node by their respective out-degree values:

$$
\displaystyle \left(\mathbf{y}^{k+1}\right)^ T = \alpha \left(\mathbf{y}^ k\right)^ T D^{-1}A + \beta \mathbf{1}^ T, ~ ~ ~ \text {where }D=\text {diag}(k_1^{\text {out}},\dots ,k_ n^{\text {out}}).
$$

With a choice of $\alpha$ in the interval $(0,1/\lambda _{\text {max}}(D^{-1}A))$, we can show that the recursive updates converge to $\mathbf{v}^ T$, where $\mathbf{v}^ T = \beta \mathbf{1}^ T (\mathbf{I} - \alpha D^{-1} A)^{-1}$.

The library **networkx** does not enforce a normalization condition on the page-rank centrality vector, and so we will follow that convention here.

# V. Hubs and Authorities

We now define two interdependent notions of centrality and combine them in a mutual recursion. An important **hub** is a node that points to many important **authorities** . An important authority is one that is pointed to by many important hubs.

We begin with an initial assignment of hub and authority scores for every node $\mathbf{x}^0$ and $(\mathbf{y}^0)^ T$, respectively. The updates are as follows:

$$
\displaystyle \mathbf{x}^{k+1} = \alpha A \mathbf{y}^ k,~ ~ ~ ~ (\mathbf{y}^{k+1})^ T = \beta (\mathbf{x}^{k+1})^ T A.
$$

Choosing $\alpha \beta = 1/\lambda _{\text {max}}(AA^ T)$, we can show that $\mathbf{x}^ k \to \mathbf{v}$ and $(\mathbf{y}^ k)^ T \to \mathbf{w}^ T$, where $AA^ T \mathbf{v} = \lambda _{\text {max}}(AA^ T) \mathbf{v}$ and $A^ T A \mathbf{w} = \lambda _{\text {max}}(A^ T A) \mathbf{w}$. In fact, the non-zero eigenvalues of $AA^ T$ and $A^ T A$ are the same and $\mathbf{w} = A^ T \mathbf{v}$.

# Conclusion (GAI)

## Code

```python
import networkx as nx

# Create a sample graph
G = nx.karate_club_graph()

# Degree Centrality
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality)

# Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)
print("Closeness Centrality:", closeness_centrality)

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)
print("Betweenness Centrality:", betweenness_centrality)

# Eigenvector Centrality
eigenvector_centrality = nx.eigenvector_centrality(G)
print("Eigenvector Centrality:", eigenvector_centrality)

# Katz Centrality
katz_centrality = nx.katz_centrality(G, alpha=0.1, beta=1.0)
print("Katz Centrality:", katz_centrality)

# PageRank
pagerank = nx.pagerank(G)
print("PageRank:", pagerank)

# Hubs and Authorities
hubs, authorities = nx.hits(G)
print("Hubs:", hubs)
print("Authorities:", authorities)
```

## Comparison

| **Centrality Measure** | **Description** | **Main Difference** | **Merit** | **Demerit** |
| --- | --- | --- | --- | --- |
| **Degree Centrality** | Number of edges connected to a node. | Measures immediate connectivity. | Simple to compute and understand. | Ignores indirect connections and the overall network structure. |
| **Closeness Centrality** | Measure of how close a node is to all other nodes. | Measures average shortest path length to all other nodes. | Identifies nodes that can quickly interact with all others. | Can be misleading in disconnected graphs; computation can be intensive for large graphs. |
| **Betweenness Centrality** | Measure of how often a node appears on shortest paths between other nodes. | Measures control over information flow in the network. | Identifies nodes that are crucial for information flow. | Can be computationally intensive; sensitive to the existence of alternative paths. |
| **Eigenvector Centrality** | Measure of the influence of a node based on the influence of its neighbors. | Measures influence in terms of the entire network structure. | Identifies nodes with influential neighbors; considers the quality of connections. | Can be dominated by nodes with high degrees; computationally intensive for large graphs. |
| **Katz Centrality** | Measure of the relative influence of a node within a network. | Considers all paths in the network with a damping factor. | Extends eigenvector centrality to handle directed networks and prevent zero centrality. | Requires choosing appropriate parameters; can be sensitive to parameter selection. |
| **PageRank** | Measure of the importance of nodes in a graph, used by Google Search. | Similar to Katz but with a specific damping factor and designed for web pages. | Identifies important nodes with a clear probabilistic interpretation; robust to varying graph sizes. | Sensitive to the damping factor; computation can be intensive for very large networks. |
| **Hubs and Authorities** | Measure of nodes as hubs (distributors) and authorities (sources). | Separates nodes into hubs (linking to authorities) and authorities (linked by hubs). | Identifies distinct roles of nodes in terms of distribution and sourcing of information. | Can be sensitive to the structure of the graph; requires iterative computation. |

## Road Network Use cases

**Degree Centrality**

- **Identifying Major Intersections**: Intersections with many connecting roads (high degree) are critical points in the network. Monitoring and managing these intersections can help in maintaining smooth traffic flow.
- **Traffic Signal Placement**: High degree intersections may require more sophisticated traffic signals to manage the higher volume of intersecting roads efficiently.
- **Logistics**:
    - **Identifying Distribution Hubs**: High degree nodes indicate major distribution centers, crucial for efficient logistics operations.
    - **Vehicle Dispatching**: Nodes with high degree centrality can serve as key points for dispatching delivery vehicles.
- **Path Planning**:
    - **Critical Intersections**: High degree nodes represent critical intersections that need to be managed for smooth traffic flow.
    - **Optimizing Traffic Flow**: Implementing measures to manage traffic at high degree intersections can reduce congestion.
- **Military**:
    - **Supply Route Nodes**: High degree nodes are key points in supply routes, essential for maintaining supply chains.
    - **Strategic Points**: High degree nodes can be strategic locations for setting up military bases or checkpoints.

**Closeness Centrality**

- **Optimal Emergency Response Locations**: Emergency services such as hospitals, fire stations, and police stations can be optimally placed at nodes with high closeness centrality for faster response times.
- **Traffic Flow Analysis**: Roads and intersections with high closeness centrality ensure quick access to various parts of the city, helping in traffic planning and route optimization.
- **Logistics**:
    - **Optimal Location of Depots**: Placing depots at nodes with high closeness centrality ensures quick access to all delivery points.
    - **Minimizing Delivery Times**: High closeness centrality nodes can help minimize delivery times by providing efficient routing.
- **Path Planning**:
    - **Shortest Path Routing**: Nodes with high closeness centrality facilitate efficient path routing for shortest travel times.
    - **Emergency Response**: High closeness centrality nodes ensure quick response times in emergencies.
- **Military**:
    - **Command and Control Centers**: Nodes with high closeness centrality ensure rapid communication and coordination.
    - **Quick Deployment**: Efficient troop movements can be planned using nodes with high closeness centrality.

**Betweenness Centrality**

- **Identifying Bottlenecks**: Intersections or roads with high betweenness centrality are likely to be bottlenecks where congestion occurs. Managing traffic at these points is crucial for overall traffic flow.
- **Infrastructure Improvement**: Investing in infrastructure improvements at high betweenness nodes, such as adding lanes or constructing bypasses, can significantly reduce congestion and improve traffic flow.
- **Logistics**:
    - **Identifying Bottlenecks**: High betweenness centrality nodes can indicate potential bottlenecks in the supply chain.
    - **Routing Optimization**: Avoiding routes through high betweenness nodes can help in optimizing the routing of deliveries.
- **Path Planning**:
    - **Traffic Bottlenecks**: Identifying potential traffic bottlenecks and managing them can improve traffic flow.
    - **Path Diversity**: Ensuring multiple route options to avoid congestion.
- **Military**:
    - **Strategic Control Points**: Nodes with high betweenness centrality control critical routes and can be strategic points.
    - **Supply Chain Security**: Protecting key supply routes that pass through high betweenness nodes.

**Eigenvector Centrality**

- **Identifying Influential Intersections**: Intersections connected to other important intersections (high eigenvector centrality) play a key role in maintaining the efficiency of the entire network. These intersections can be focal points for traffic management.
- **Strategic Placement of Facilities**: Facilities such as gas stations, parking lots, and service areas can be placed near intersections with high eigenvector centrality to maximize accessibility and convenience.
- **Logistics**:
    - **Influential Depots**: Identifying depots that have a high influence on the network due to their connections.
    - **Strategic Alliances**: Partnering with influential distribution centers to enhance logistics operations.
- **Path Planning**:
    - **Influential Routes**: Identifying critical routes that are influential in the network.
    - **Planning Major Roads**: Ensuring connectivity to influential nodes for effective path planning.
- **Military**:
    - **Key Strategic Locations**: Identifying influential strategic locations that are critical for operations.
    - **Collaboration Nodes**: Nodes critical for multi-unit operations and collaboration.

**Katz Centrality**

- **Influence of Intersections Over Time**: Katz centrality can help assess the long-term influence of intersections by considering both direct and indirect connections, useful for long-term urban planning and development.
- **Evolution of Road Networks**: Understanding how changes in the network, such as new roads or closures, affect the importance of intersections can help in adaptive traffic management and planning.
- **Logistics**:
    - **Long-term Network Influence**: Assessing the long-term influence of depots and routes on the logistics network.
    - **Dynamic Network Planning**: Adapting to network changes by understanding the influence of nodes over time.
- **Path Planning**:
    - **Long-term Path Planning**: Assessing the influence of paths over time for long-term planning.
    - **Adapting to Network Changes**: Dynamic path planning by understanding changing influences.
- **Military**:
    - **Influence Over Time**: Understanding the long-term influence of strategic locations.
    - **Dynamic Operations**: Adapting to changing military landscapes by assessing long-term influences.

**PageRank**

- **Importance of Road Segments**: Similar to its use in ranking web pages, PageRank can identify important road segments that are frequently traversed. This can help in prioritizing maintenance and upgrades.
- **Tourism and Commercial Zones**: Identifying routes frequently used by tourists or commercial traffic can help in planning for seasonal variations in traffic and ensuring these routes are well-maintained.
- **Logistics**:
    - **Importance of Distribution Centers**: Identifying key distribution centers that are crucial for the logistics network.
    - **Optimizing Deliveries**: Prioritizing important routes to optimize delivery schedules.
- **Path Planning**:
    - **Importance of Routes**: Identifying frequently used and important routes for effective path planning.
    - **Tourist Path Optimization**: Optimizing paths for high-traffic areas, such as tourist routes.
- **Military**:
    - **Strategic Importance**: Assessing the strategic importance of routes and locations for military operations.
    - **Resource Allocation**: Prioritizing resource allocation to important routes and locations.

**Hubs and Authorities**

- **Identification of Major Road Hubs**: Hubs in the road network distribute traffic to many destinations, similar to major intersections or transit points. Enhancing these hubs can improve overall network efficiency.
- **Supporting Road Authorities**: Authorities can represent critical endpoints such as city centers or important districts. Ensuring these areas are well-connected and served by multiple routes enhances accessibility and economic activity.
- **Logistics**:
    - **Identifying Major Hubs**: Hubs as major distribution centers, and authorities as critical delivery points.
    - **Optimizing Supply Chains**: Ensuring connectivity between hubs and authorities for efficient supply chains.
- **Path Planning**:
    - **Major Junctions and Destinations**: Hubs as major junctions, and authorities as key destinations.
    - **Path Optimization**: Ensuring connectivity between key points for optimized path planning.
- **Military**:
    - **Major Supply Hubs**: Hubs as major supply points, and authorities as key strategic locations.
    - **Coordinating Operations**: Ensuring effective coordination between hubs and authorities for military operations.