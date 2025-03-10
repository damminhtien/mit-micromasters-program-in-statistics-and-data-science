# Lecture 12: Graphical Models

# Motivation

In this lecture, we will learn the definitions and properties of four graphical models:

1. The definition of the **Erdos-Renyi** model.
    - Number of edges the graph has
    - Random realization be a complete graph
    - The edge probability and degree distributions of the **Erdos-Renyi** model.
    - Graph structure: the phase transitions of the **Erdos-Renyi** model.
2. The definition of the **Configuration** model.
    - The edge probability of the **Configuration** model.
3. The definition of **Price's** preferential attachment model.
4. The definition of the **Small-World** model.

# I. Erdos-Renyi Model

The **Erdos-Renyi (ER) model** is a fundamental model for generating random graphs. It is defined in two primary ways: $G(n, M)$ and $G(n, p)$.

1. **Definitions**:
    - **$G(n, M)$** Model: A graph is constructed by selecting $n$ nodes and randomly adding $M$edges between them.
    - **$G(n, p)$** Model: A graph is constructed by selecting $n$ nodes, and each possible edge between any pair of nodes is included with probability $p$.
2. **Number of Edges**:
    - In the $G(n, M)$ model, the graph has exactly $M$ edges.
    - In the $G(n, p)$ model, the expected number of edges is $\binom{n}{2} p$, where $\binom{n}{2}$ is the number of possible edges in a graph with $n$ nodes.
3. **Random Realization Be a Complete Graph**:
    - In the $G(n, p)$ model, if $p = 1$, every possible edge is included, resulting in a complete graph.
    - As $p$ decreases from 1 to 0, the graph transitions from being a complete graph to an empty graph.

## **Edge Probability**

In the $G(n, p)$ model, the probability that an edge exists between any two given nodes is $p$. **MLE of $p$:**

- The number of edges $M$ in a realization of the graph follows a binomial distribution: $M \sim \text{Binomial}\left(\binom{n}{2}, p\right)$.
- The likelihood function for observing $m$ edges in the graph is given by the probability mass function of the binomial distribution: $P(M = m \mid p) = \binom{\binom{n}{2}}{m} p^m (1 - p)^{\binom{n}{2} - m}$.
- To find the MLE of $p$, we need to maximize the likelihood function with respect to $p$. This is often done by maximizing the log-likelihood function instead: $\log L(p) = \log \left( \binom{\binom{n}{2}}{m} \right) + m \log p + \left( \binom{n}{2} - m \right) \log (1 - p)$ .
- The binomial coefficient $\binom{\binom{n}{2}}{m}$ is a constant with respect to $p$ and can be ignored for the purpose of maximization: $\log L(p) = m \log p + \left( \binom{n}{2} - m \right) \log (1 - p)$ .
- To find the MLE, we take the derivative of the log-likelihood function with respect to $p$ and set it to zero: $\frac{d}{dp} \log L(p) = \frac{m}{p} - \frac{\binom{n}{2} - m}{1 - p} = 0$ .
- Solving for $p$:

$$
\frac{m}{p} = \frac{\binom{n}{2} - m}{1 - p} \to m (1 - p) = p \left( \binom{n}{2} - m \right) \to m - mp = p \binom{n}{2} - mp \to m = p \binom{n}{2} \to p = \frac{m}{\binom{n}{2}}
$$

## **Degree Distribution**

Consider node $j$ in an Erdos-Renyi model $G(n, p)$. Potentially, it could be connected through edges to up to $n-1$ other nodes, where the presence of each edge is distributed according to $\text{Binomial}(1, p)$. Thus, the degree, $k_ j$, of node $j$ is the sum of $n-1$ random variables distributed according to $\text{Binomial}(1, p)$. Therefore, $k_j \sim \text{Binomial}(n-1, p)$. It follows that the expected value of the degree is $\displaystyle \mathbb {E}[k_ j] = p(n-1).$

The sum of all node degrees in the graph is given by: $K = \sum_{j=1}^n k_j$. Since each $k_j$ is distributed as $\text{Binomial}(n-1, p)$, the sum $K$ can be seen as the sum of $n$ Binomial distributions. Hence, $K \sim \text{Binomial}(n(n-1), p)$. The MLE of $K$ is given:

- The likelihood function for a Binomial distribution is given by $L(p) = \binom{n(n-1)}{K} p^K (1-p)^{n(n-1) - K}$.
- To simplify the maximization process, we take the natural logarithm of the likelihood function to obtain the log-likelihood function $\log L(p) = \log \binom{n(n-1)}{K} + K \log p + (n(n-1) - K) \log (1-p)$.
- We need to differentiate the log-likelihood function with respect to $p$: $\frac{d}{dp} \log L(p) = \frac{K}{p} - \frac{n(n-1) - K}{1 - p}$.
- To find the MLE, we set the derivative equal to zero and solve $\frac{K}{p} - \frac{n(n-1) - K}{1 - p} = 0$.
- Rearranging the equation to solve $p = \frac{K}{n(n-1)}$.

## Graph Structure: Phase Transitions of the Erdos-Renyi Model

1. **Phase Transition**:
    - In the context of the ER model, a phase transition refers to a sudden change in the structure of the graph as $p$ changes.
    - **Critical Point**: When $p \approx \frac{1}{n}$, the graph undergoes a phase transition. Below this point, the graph consists of many small components. Above this point, a giant component (a single connected component containing a significant fraction of the nodes) emerges.
    - **Connectivity**: For $p > \frac{\ln(n)}{n}$, the graph is likely to be connected, meaning there is a path between any pair of nodes.

An Erdos-Renyi model, G(n,p), displays, in the large node limit of n\to \infty, a phase transition in the global graph structure at two points.

For p < \frac{1}{n}, there are many small components. The size of these components tends to be bounded above:

\displaystyle P(S_{\text {max}} > c \ln {n} )	\displaystyle \to 0	\displaystyle \text { as } n \to \infty		
where S_{\text {max}} is the size of the largest component in the graph, and c = 2 m / n is the average node degree. Note that this is strictly only a bound as n\to \infty, for any finite n there is a non-zero probability of all nodes being connected.

Between \frac{1}{n} < p < \frac{\ln {n}}{n}, a giant component emerges. This giant component has a size that is a significant fraction of n, around (c-1)n for c\approx 1 (the relation is not linear for larger c). There will only be one of these giant components; other components will exist, but they will observe the S < c \ln {n} bound discussed above.

Above p > \frac{\ln {n}}{n}, the giant component includes all nodes in the graph and the graph becomes connected.

Although these phase transitions are only defined in the n\to \infty limit, you can observe them even for n as small as 100. When n is small, the phase transition points become “fuzzy" in that the transition may not occur at exactly the points described above, but close to them.

Suppose that you are given a graph with n = 1\times 10^6 and m=200\times 10^3.

What would you expect to see if the process that created this graph can be described by an Erdos-Renyi model?
a) Many small connected components.
b) Some small components along with a giant connected component.
c) A single connected component.

If you are given a graph with n=1\times 10^6 and m=20\times 10^6, what would you expect to see if the graph came from an Erdos-Renyi model?
a) Many small connected components.
b) Some small components along with a giant connected component.
c) A single connected component.

```python
import numpy as np

def erdos_renyi_phase(n, m):
    # Calculate p
    p = m / (n * (n - 1) / 2)
    
    # Calculate critical values
    p1 = 1 / n
    p2 = np.log(n) / n
    
    # Determine the phase
    if p < p1:
        phase = "a) Many small connected components."
    elif p1 <= p < p2:
        phase = "b) Some small components along with a giant connected component."
    else:
        phase = "c) A single connected component."
    
    return p, phase

# Given values
n1 = 1 * 10**6
m1 = 200 * 10**3

n2 = 1 * 10**6
m2 = 20 * 10**6

# Calculate phase for the first graph
p1, phase1 = erdos_renyi_phase(n1, m1)
print(f"For n={n1} and m={m1}:")
print(f"p = {p1}")
print(f"Expected phase: {phase1}")

# Calculate phase for the second graph
p2, phase2 = erdos_renyi_phase(n2, m2)
print(f"\nFor n={n2} and m={m2}:")
print(f"p = {p2}")
print(f"Expected phase: {phase2}")

```

# II. Configuration Model

Unfortunately the Erdos-Renyi model does not produce a power-law degree distribution. Power-law degree distributions are commonly observed in natural networks, so we desire a graphical model that will produce such a distribution.

The Configuration model generates a random graph with a specified degree sequence. The procedure involves repeatedly selecting pairs of "stubs" and connecting them to form edges until all stubs are used up. This process ensures that the resulting graph has the desired degree sequence. However, not all degree sequences can be used to construct a valid graph in the Configuration model.

To determine if any list of samples drawn from a power-law distribution can be used to construct the Configuration model, we need to consider the conditions that a degree sequence must satisfy to be graphical (i.e., realizable as a simple graph):

1. **Even Sum Condition**: The sum of the degrees must be even. This ensures that it is possible to pair all stubs into complete edges.
2. **Handshaking Lemma**: For the degree sequence to be graphical, it must be possible to pair all stubs such that each node gets the desired degree without violating the simple graph constraints (no multiple edges between the same pair of nodes and no loops).

A necessary and sufficient condition for a degree sequence to be graphical is given by the Erdős–Gallai theorem:

- **Erdős–Gallai Theorem**: A non-increasing sequence of non-negative integers $(d_1, d_2, \ldots, d_n)$ is graphical if and only if:
    1. The sum of the degrees is even, and
    2. For every $k$ $( 1 \leq k \leq n)$: $\sum_{i=1}^k d_i \leq k(k-1) + \sum_{i=k+1}^n \min(d_i, k)$ 

When sampling from a power-law distribution, the resulting degree sequence often follows a non-increasing order due to the nature of the distribution, where many nodes have low degrees, and a few nodes have very high degrees.

**Answer:**

No, not any list of samples drawn from a power-law distribution can be used to construct the Configuration model. The degree sequence must satisfy the Erdős–Gallai conditions to be graphical. If the sampled degree sequence does not meet these conditions, it cannot be used to construct a valid graph using the Configuration model.

In practice, while many power-law distributions may yield graphical degree sequences, it is not guaranteed for every possible sample. Verification of the degree sequence is necessary to ensure it meets the graphical conditions before attempting to construct a graph using the Configuration model.

1. **Definition**:
    - The **Configuration model** generates random graphs with a given degree sequence. Each node $i$ is assigned a degree $k_i$, and the graph is constructed by randomly pairing these stubs (half-edges) to form edges.
2. **Edge Probability**:
    - The probability that an edge exists between any two nodes depends on their degrees. If nodes $i$ and $j$ have degrees $k_i$ and $k_j$, respectively, the expected number of edges between them in a large graph is $P_{ij} \approx \frac{k_i k_j}{2m}$, where $m$ is the total number of edges.

# III. Price's Preferential Attachment Model

1. **Definition**:
    - The **Preferential Attachment model** (introduced by Price and later popularized by Barabási and Albert) generates graphs by adding new nodes that preferentially attach to existing nodes with high degrees.
    - New nodes are added sequentially. Each new node connects to $m$ existing nodes with a probability proportional to the degree of those nodes.
2. **Mechanism**:
    - If a node $i$ has degree $k_i$, the probability $\Pi(i)$ that a new node will connect to $i$ is $\Pi(i) = \frac{k_i}{\sum_j k_j}$.
    - This mechanism results in a scale-free network where the degree distribution follows a power law: $P(k) \sim k^{-\gamma}$ with $\gamma \approx 3$.

# IV. Small-World Model

1. **Definition**:
    - The **Small-World model** (introduced by Watts and Strogatz) describes networks that have high clustering coefficients like regular lattices and short average path lengths like random graphs.
    - The model starts with a regular lattice and then rewires each edge with a probability $p$.
2. **Mechanism**:
    - **Regular Lattice**: Start with a ring lattice where each node is connected to its $k$ nearest neighbors.
    - **Rewiring**: For each edge, with probability $p$, rewire one end of the edge to a randomly chosen node, avoiding duplicate edges and self-loops.
3. **Characteristics**:
    - For $p \approx 0$, the network remains a regular lattice with high clustering and long path lengths.
    - For $p \approx 1$, the network becomes a random graph with low clustering and short path lengths.
    - For intermediate values of $p$, the network exhibits the small-world phenomenon: high clustering and short average path lengths.

**Summary**. These four graphical models provide foundational frameworks for understanding the structure and behavior of various types of networks:

- **Erdos-Renyi Model**: Models random graphs and phase transitions.
- **Configuration Model**: Generates graphs with a given degree sequence.
- **Preferential Attachment Model**: Generates scale-free networks with power-law degree distributions.
- **Small-World Model**: Captures networks with high clustering and short path lengths, characteristic of many real-world networks.

Understanding these models helps in analyzing and simulating networks in various domains, from social networks to biological systems.