# Lecture 1. Probability Models and Axioms

* Sample space

  * Set ($\Omega$) must be
    * Mutually exclusive
    * Collectively exhaustive
    * At the right granularity
  * Event: a subset of the sample space

* Probability laws

  * Axioms	
    * Nonnegativity: $P(A) \geq 0$
    * Normalization: $P(\Omega) = 1$
    * (Finite) additivity: if $A \cap B = \empty$ (disjoint), then $P(A \cup B) = P(A) + P(B)$
  * Properties
    * From nonnegativity: $P(A) \leq 1$
    * From normalization: $P(\empty) = 0$
    * For A, B, C disjoint: $P(A \cup B \cup C) = P(A) + P(B) + P(C)$.
    * For $k$ disjoint events: $P(\{s_1, s_2, ..., s_k\}) = P(\{s_1\}) +... + P(\{s_k\}) = P(s_1) +... + P(s_k) $.
    * If $A \subset B$, then  $P(A) \leq P(B)$. 
    * $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, where $P(A \cap B) \geq 0$.
    * $P(A \cup B) \leq P(A) + P(B)$.
    * $P(A \cup B \cup C) = P(A \cup (A^c \cap B) \cup (A^c \cap B^c \cap C)) =P(A) + P(A^c \cap B) + P(A^c \cap B^c \cap C).$

* Examples

  * Discrete but infinite sample space

    Given $P(n) = \frac{1}{2^n}, n = 1,2,...$, 
    $$
    P(\{2,4,6,...\}) = P(\{2\} \cup \{4\} ...) = P(2) + P(4) + ... = \frac{1}{2^2} + \frac{1}{2^4} + ... = \frac{1}{4}(1 + \frac{1}{4} + \frac{1}{4^2} + ...) = \frac{1}{4} \cdot \frac{1}{1-1/4} = \frac{1}{3}
    $$
    Using the formula:
    $$
    \sum^\infty_{n=1} = \frac{1}{2^n} = \frac{1}{2}\sum^\infty_{n=0} = \frac{1}{2}\cdot \frac{1}{1-1/2} = 1
    $$

* Discussion

  * Countable additivity

    If $A_1, A_2, ...$ is an infinite **sequence** of **disjoint** events, then $P(A_1 \cup A_2 \cup ...) = P(A_1) + P(A_2) + ...$

    This axiom only applies for a countable "sequence" of events. This requires that the infinite sets should be discrete rather than continuous.

    * A case when it does not apply: The sample space is the 2D plane. For any real number $x$, let $A_x$ be the subset of the plane that consists of all points of the vertical line through the point $(x,0)$ i.e. $A_ x=\{ (x,y): y\in \mathrm{Re\, }\}$.
      $$
      P(\bigcup A_x) \neq \sum P(A_x)
      $$

  * Mathematical subtleties

* Interpretations of probabilities

  ![roleOfProb](../assets/images/U1-lec1-role.png)

* Mathematical background

  * Sets: a collection of distinct elements

    * For some sets $S_n, n=1,2,...$,

      $x \in \bigcup_n S_n$ iff $x\in S_n$ for some $n$; $x \in \bigcap_n S_n$ iff $x \in S_n$, for all $n$.

    * Properties: 

      $S \cup T = T \cup S, \quad S \cup (T \cup U) = (S \cup T) \cup U$

      $S \cap (T \cup U) = (S \cap T) \cup (S \cap U), \quad S \cup(T \cap U) = (S \cup T) \cap (S \cap U)$

      $(S^c)^c = S, \quad S \cap S^c = \empty$

      $S \cup \Omega = \Omega, \quad S \cap \Omega = S$

    * De Morgan's Law

      $\Big(\bigcap_{n} S_n\Big)^c = \bigcup_n S_n^c; \quad \Big( \bigcup_n S_n\Big)^c = \bigcap_n S_n^c$

  * Convergence:

    * If $a_i \leq a_{i+1}$, for all $i$, then either

      1. the sequence “converges to $\infty$”

      2. the sequence converges to some real number $a$

    * If $|a_i - a| \leq b_i$ for all $i$ and $b_i \rightarrow 0$, then $a_i \rightarrow a$.

  * Infinite series: 

    $\sum^{\infty}_{i=1} a_i =  \lim\limits_{n \rightarrow \infty} \sum^n_{i=1}a_i$ provided limit exists.

    * If $a_i \geq 0$, limit exists.

    * If terms $a_i$ do not all have the same sign

      * Limit may exist but be different if we sum in a different order

      * Limit exists and independent of order of summation of $\sum^\infty_{i=1}|a_i| < \infty$.

  * Geometric series

    $\sum^\infty_{i=0}\alpha^i = 1 + \alpha + \alpha^2 + ... = \frac{1}{1-\alpha}, \quad |\alpha| < 1$

    Proof: 

    Set $S =1+ \alpha + \alpha^2 + ...$, Compute $(1-\alpha)S = 1 - \alpha^{n+1}$. When $n \rightarrow \infty$, $(1-\alpha)S = 1$.


---

There are 3 selected exercises and 4 solved problems.

## Exercise 1 Continuous probability calculations

Consider a sample space that is the rectangular region $[0,1]×[0,2]$, i.e., the set of all pairs $(x,y)$ that satisfy $0≤x≤1$ and $0≤y≤2$. Consider a “uniform" probability law, under which the probability of an event is half of the area of the event. Find the probability of the following events:

a) The two components $x$ and $y$ have the same values. 

b) The value, $x$, of the first component is larger than or equal to the value, $y$, of the second component.

c) The value of $x^2$ is larger than or equal to the value of $y$.

**Answer**: 

a) 0; b) 1/4; c) 1/6

**Solution**: 

a) This event is a line, and since a line has zero area, the probability is 0.

b) This event is a triangle with vertices at $(0,0), (1,0), (1,1)$. Its area is $1/2$, and therefore the probability is $1/4$.

c) This event corresponds to the region below the curve $y=x^2$, where $x$ ranges from 0 to 1. The area of this region is
$$
\int _0^1 x^2\,  dx= \left.\frac{x^3}{3}\right|_0^1 =\frac{1}{3},
$$
and therefore the corresponding probability is $1/3 * 1/2 = 1/6$.

## Exercise 2 Using countable additivity

Let the sample space be the set of positive integers and suppose that $P(n)=1/2^n$, for $n=1,2,….$ Find the probability of the set $\{3,6,9,…\}$, that is, of the set of of positive integers that are multiples of 3.

Using countable additivity, and with $α=2^{−3}=1/8$, the desired probability is
$$
\frac{1}{2^3}+\frac{1}{2^6}+\frac{1}{2^9}+\cdots =\alpha +\alpha ^2+\alpha ^3+\cdots =\frac{\alpha }{1-\alpha }=\frac{1/8}{1-(1/8)}=\frac{1}{7}.
$$

## Exercise 3 Uniform probabilities on the integers

Let the sample space be the set of all positive integers. Is it possible to have a “uniform" probability law, that is, a probability law that assigns the same probability $c$ to each positive integer?

**Answer**: No

**Solution**: 

Suppose that $c=0$. Then by countable additivity 
$$
1=\mathbf{P}(\Omega )=\mathbf{P}\big (\{ 1\} \cup \{ 2\} \cup \{ 3\} \cdots \big ) =\mathbf{P}(\{ 1\} )+\mathbf{P}(\{ 2\} )+\mathbf{P}(\{ 3\} )+\cdots = 0+0+0+\cdots =0,
$$
which is a contradiction.

Suppose that $c > 0$. Then there exists an integer $k$ that $kc > 1$. By additivity, 
$$
\mathbf{P}\big (\{ 1,2,\ldots ,k\} ) =kc>1,
$$
which contradicts the normalization axiom.

## Problem 1 Uniform probabilities on a square

Romeo and Juliet have a date at a given time, and each will arrive at the meeting place with a delay between 0 and 1 hour, with all pairs of delays being “equally likely," that is, according to a uniform probability law on the unit square. The first to arrive will wait for 15 minutes and will leave if the other has not arrived. What is the probability that they will meet?

**Answer**: 7/16

**Solution**: 

First assume Romeo and Juliet arrive in 15min interval and we can draw the sample space in a discrete way.

![U1-lec1-prob1](../assets/images/U1-lec1-prob1.png)

So that the probability of meeting each other is 
$$
\mathbf{P}(\text{meet}) = 13/25
$$
Now we draw the sample space in a continuous way

![U1-lec1-prob1-2](../assets/images/U1-lec1-prob1-2.png)

So that the probability of meeting each other is 
$$
\mathbf{P}(\text{meet}) = 1 - 1/2 * 3/4 * 3/4 * 2 = 7/16
$$

## Problem 2 Bonferroni's Inequality

(a) Prove that for any two events $A_1$ and $A_2$, we have
$$
\mathbf{P}(A_1 \cap A_2) \geq \mathbf{P}(A_1) + \mathbf{P}(A_2)-1.
$$
(b) Generalize to the case of $n$ events $A_1,A_2,…,A_n$, by showing that
$$
\mathbf{P}(A_1 \cap A_2 \cap \cdots \cap A_ n)\geq \mathbf{P}(A_1)+\mathbf{P}(A_2)+\cdots +\mathbf{P}(A_ n)-(n-1).
$$
Proof: 

With $\mathbf{P}(A_1 \cup A_2) \leq \mathbf{P}(A_1) + \mathbf{P}(A_2) $, we can prove (a) and (b), for example,
$$
\begin{aligned}
&\mathbf{P}((A_1 \cap A_2)^c) = \mathbf{P}(A_1^c \cup A_2^c) \leq \mathbf{P}(A_1^c) + \mathbf{P}(A_2^c)\\
&\implies 1-\mathbf{P}(A_1 \cap A_2) \leq 1-\mathbf{P}(A_1) + 1-\mathbf{P}(A_2)\\
&\implies -\mathbf{P}(A_1 \cap A_2) \leq 1-\mathbf{P}(A_1) -\mathbf{P}(A_2)\\
&\implies \mathbf{P}(A_1 \cap A_2) \geq \mathbf{P}(A_1) +\mathbf{P}(A_2)-1
\end{aligned}
$$

## Problem 3 Parking lot problem

Mary and Tom park their cars in an empty parking lot with $n≥2$ consecutive parking spaces (i.e, $n$ spaces in a row, where only one car fits in each space). Mary and Tom pick parking spaces at random; of course, they must each choose a different space. (All pairs of distinct parking spaces are equally likely.) What is the probability that there is at most one empty parking space between them?

**Answer**: $\mathbf{P}(A) = \frac{4n-6}{n(n-1)}.$

**Solution**: 

The sample space is $Ω=\{(i,j):i≠j,1≤i,j≤n\}$, where outcome $(i,j)$ indicates that Mary and Tom parked in slots $i$ and $j$, respectively. We apply the **discrete uniform probability law** to find the required probability. We are interested in the probability of the event.
$$
A = \{  (i,j) \in \Omega : |i-j| \leq 2 \}
$$
We first find the cardinality of $Ω$. There are $n^2$ pairs $(i,j)$, but since the set $Ω$ excludes outcomes of the form $(i,i)$, the cardinality of $Ω$ is $n^2−n=n(n−1)$.

![U1-lec1-prob3](../assets/images/U1-lec1-prob3.png)

If $n≥3$, event $A$ consists of the four lines indicated in the figure above and contains $2(n−1)+2(n−2)=4n−6$ elements. If $n=2$, event $A$ contains exactly $2$ elements, namely, $(1,2)$ and $(2,1)$, which agrees with the formula $4(2)−6=2$. Therefore,
$$
\mathbf{P}(A) = \frac{4n-6}{n(n-1)}.
$$

## Problem 4 Upper and lower bounds on the probability of intersection

Given two events $A,B$ with $P(A)=3/4$ and $P(B)=1/3$, what is the smallest possible value of $P(A∩B)$? The largest? That is, find $a$ and $b$ such that,
$$
a\leq \mathbf{P}(A\cap B)\leq b,
$$
holds and any value in the closed interval [a,b] is possible.

**Answer**: a = 1/12; b = 1/3

**Solution**: 

From Bonferroni Inequality, we have the lower bound,
$$
\mathbf{P}(A\cap B)\geq \mathbf{P}(A)+\mathbf{P}(B)-1 = \frac{1}{12}.
$$
Since $A\cap B\subset A$ and $A\cap B\subset B$, we have the higher bound,
$$
\mathbf{P}(A\cap B)\leq \mathbf{P}(A) \quad \text {and}\quad \mathbf{P}(A\cap B)\leq \mathbf{P}(B)\\
\mathbf{P}(A\cap B)\leq \frac{1}{3}.
$$