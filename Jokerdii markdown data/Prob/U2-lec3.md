# Lecture 3. Independence

* Independence of two events 

  * Definition of independence: $\mathbf{P}(A \cap B ) = \mathbf{P}(A) \cdot \mathbf{P}(B)$. 
    * If $\mathbf{P}(B|A) = \mathbf{P}(B)$, occurrence of $A$ provides no new information about $B$.
  * If $A$ and $B$ are independence, then $A$ and $B^c$ are independent.

* Conditional independence

  * Given $C$, the conditional independence is defined as independence under the probability law $\mathbf{P}(\cdot | C)$.
    $$
    \mathbf{P}(A \cap B | C) = \mathbf{P}(A | C) \mathbf{P}(B | C)
    $$

  * Independence does not imply conditional independence.

    In the case below, $A$ and $B$ have no intersection in the condition of $C$. If $A$ happens, $B$ won't happen in the condition of $C$. This means that $A$ and $B$ are not independent.

    ![condIndependent](../assets/images/condIndependent.png)

* Independence of a collection of events

  * Event $A_1, A_2, ..., A_n$ are independent if $\mathbf{P}(A_i \cap A_j \cap ... \cap A_m) = \mathbf{P}(A_i) \mathbf{P}(A_j) ... \mathbf{P}(A_m)$, for any distinct indices $i,j,...,m$.

* Pairwise independence

  * Independent events must be pairwise independent, but the reverse may not be true.

  * E.g. two independent fair coin tosses. $C$: the two tosses had the same result. $H_1$: first toss is $H$, $H_2$: second toss is $H$, $\mathbf{P}(H_1) = \mathbf{P}(H_2) = 1/2, \mathbf{P}(C) = 1/2$. 

    * $\mathbf{P}(H_1 \cap H_2) = 1/4 =  \mathbf{P}(H_1)\mathbf{P}(H_2)$
    * $\mathbf{P}(H_1 \cap C) = 1/4 = \mathbf{P}(H_1)\mathbf{P}(C)$
    * But, $\mathbf{P}(C| H_1 \cap H_2) = 1 \neq \mathbf{P}(C) = 1/2$

    So $H_1, H_2,C$ are pairwise independent, but not independent.

* Reliability

  * $p_i$: probability that unit $i$ is "up" ; $u_i$: $i$th unit up, $u_i$ are independent; $F_i$: $i$th unit down, $F_i$ are independent.

    ![reliability1](../assets/images/reliability1.png)
    $$
    \begin{aligned}
    \mathbf{P}(\text{system up}) &= \mathbf{P}(u_1 \cap u_2 \cap u_3)\\
    &= \mathbf{P}(u_1) \cap \mathbf{P}(u_2) \cap \mathbf{P}(u_3)\\
    &= p_1 p_2 p_3
    \end{aligned}
    $$
    ![reliability2](../assets/images/reliability2.png)
    $$
    \begin{aligned}
    \mathbf{P}(\text{system up}) &= \mathbf{P}(u_1 \cup u_2 \cup u_3) \\
    &= 1-\mathbf{P}(F_1 \cap F_2 \cap F_3)\\
    &= 1 - \mathbf{P}(F_1) \mathbf{P}(F_2) \mathbf{P}(F_3)\\
    &= 1-(1-p_1)(1-p_2)(1-p_3)
    \end{aligned}
    $$
  
  * In general, if a *serial* sub-system contains $m$ components with success probabilities $p_1, p_2...p_m$, then the probability of success of the entire sub-system is given by
    $$
    \mathbf{P}(\text{whole system secceeds}) = p_1p_2...p_m
    $$
    If a parallel sub-system contains $m$ components with success probabilities $p_1, p_2...p_m$, then the probability of success of the entire sub-system is given by
    $$
    \mathbf{P}(\text{whole system succeeds}) = 1 - (1-p_1)(1-p_2)...(1-p_m)
    $$

---

There are 3 selected exercises and 1 solved problem.

## Exercise 1 Independence of two events

Let $A$ be an event, a subset of the sample space $\Omega$. Are $A$ and $\Omega$ independent?

Yes, they are. Because $\mathbf{P}(A\cap \Omega )=\mathbf{P}(A)=\mathbf{P}(A)\cdot 1 =\mathbf{P}(A)\cdot \mathbf{P}(\Omega )$. Intuitively $\mathbf{P}(A)$ represents our beliefs about the likelihood that $A$ will occur. If we are told that $Ω$ occurred, this does not give us any new information; we already knew that $Ω$ is certain to occur. For this reason, $\mathbf{P}(A\mid \Omega )=\mathbf{P}(A)$.

When is an event $A$ independent of itself ?

If and only if $\mathbf{P}(A)$ is either 0 or 1. Since $\mathbf{P}(A\cap A) = \mathbf{P}(A) =\mathbf{P}(A)\cdot \mathbf{P}(A).$

## Exercise 2 Conditional independence

Suppose that $A$ and $B$ are conditionally independent given $C$. Suppose that $\mathbf{P}(C) > 0$ and $\mathbf{P}(C^c) > 0$.

1) Are $A$ and $B^c$ guaranteed to be conditionally independent given $C$? Yes

2) Are $A$ and $B$ guaranteed to be conditionally independent given $C^c$? No

Given $A$ and $B$ are conditionally independent given $C$, $A$ and $B$ must have intersection in $C$.  

For 1) we have seen that in any probability model, independence of $A$ and $B$ implies independence of $A$ and $B^c$. The conditional model (given $C$) is just another probability model, so this property remains true.

For 2) the counter example is that: events $A$ and $B$ have nonempty intersection inside $C$, and are conditionally independent, but have empty intersection inside $C^c$, which would make them dependent (given $C^c$).

## Exercise 3 Reliability

Suppose that each unit of a system is up with probability $2/3$ and down with probability $1/3$. Different units are independent. For each one of the systems shown below, calculate the probability that the whole system is up (that is, that there exists a path from the left end to the right end, consisting entirely of units that are up). What is the probability that the following system is up?

1) $16/27$

![ex_reliability1](../assets/images/ex_reliability1.jpg)

The probability of the parallel units fail = $(1/3) \cdot (1/3) = 1/9$.

The probability of the parallel connection is up = $1 - 1/9 = 8/9$.

The probability of the whole system is up = $(2/3) \cdot (8/9) = 16/27.$ 

2) $22/27$

![ex_reliability2](../assets/images/ex_reliability2.jpg)

The whole system is up only when the parallel both units are up.

The probability of the upper units up = $(2/3) \cdot (2/3) = 4/9$.

The probability of the upper units fail = $1- (4/9) = 5/9$.

The probability of the bottom units fail = $(1/3)$.

The probability of the system fail = $(5/9) \cdot (1/3) = 5/27$.

The probability of the whole system up = $1- (5/27) = 22/27$.

## Problem 1 Network reliability

An electrical system consists of identical components, each of which is operational with probability $p$, independent of other components. The components are connected in three subsystems, as shown in the figure. The system is operational if there is a path that starts at point $A$, ends at point $B$, and consists of operational components. What is the probability of this happening?

![reliability-prob3](../assets/images/reliability-prob3.jpg)

$\mathbf{P}(A \rightarrow B) = \mathbf{P}(A\rightarrow C)\mathbf{P}(C \rightarrow E) \mathbf{P}(E \rightarrow B)$ (since they are in series)

$\mathbf{P}(A \rightarrow C) = p$

$\mathbf{P}(C \rightarrow E) = 1 - (1-p)(1-\mathbf{P}(C \rightarrow D) \mathbf{P}(D \rightarrow E))$

$\mathbf{P}(E \rightarrow B) = 1-(1-p)^2$

The probability $\mathbf{P}(C \rightarrow D), \mathbf{P}(D \rightarrow E)$ can be similarly computed as

$\mathbf{P}(C \rightarrow D) = 1-(1-p)^3$

$\mathbf{P}(D \rightarrow E) = p$

The probability of success of the entire system can be obtained by substituting the subsystem success probabilities:

$\mathbf{P}(A \rightarrow B)\\ = \mathbf{P}(A\rightarrow C)\mathbf{P}(C \rightarrow E) \mathbf{P}(E \rightarrow B)\\ = p\{1-(1-p)[1-p[1-(1-p)^3]]\}[1-(1-p)^2]$

