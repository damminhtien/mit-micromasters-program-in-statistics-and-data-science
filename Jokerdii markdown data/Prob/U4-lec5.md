# Lecture 5. Probability mass functions and expectations

* Random variables: 

  * A random variable $X$ associates a value $x$ to every possible outcome. Mathematically, it is a function from the sample space $\Omega$ to the real numbers.
  * Discrete: take values in finite or countable set.

* Probability mass function (PMF):

  * PMF is the probability distribution of $X$.
  * $p_X(x) = \mathbf{P}(X = x) = \mathbf{P}(\{w \in \Omega~s.t. X(w) = x\})$.
  * Properties: $p_X(x) \geq 0, \quad \sum_x p_X(x) = 1$.

* Random variable examples:

  * Bernoulli with parameter $p \in [0,1]$

    $x = \begin{cases} 1, &\quad w.p.\quad p \\0 &\quad w.p.\quad 1-p \end{cases}$

  * Uniform with parameters integer $a, b$

    $p_X(x_i)  =\frac{1}{b-a+1}$

  * Binomial with parameters $n, p$

    $p_X(k) = {n \choose k} p^k (1-p)^{n-k}, \quad \text{for }k = 0,1,...,n$

  * Geometric with parameter $p$

    $p_X(k) = \mathbf{P}(X = k) = (1-p)^{k-1}p, \quad k=1,2,3$

* Expectation (mean) and its properties:

  * The expected value rule

    $\mathbb{E}[X] = \sum_xx p_X(x)$.

    Caution: If we have an infinite sum, it needs to be well-defined. We assume $\sum_x |x|p_X(x) < \infty$.

  * Expectation of Bernoulli r.v.: $\mathbb{E}[X] = p$

  * Expectation of Uniform r.v.: $\mathbb{E}[X] = 0 \cdot \frac{1}{n+1}+ 1\cdot \frac{1}{n+1}+ ... + n\cdot \frac{1}{n+1}= \frac{1}{n+1}(0+1+...+n) = \frac{1}{n+1} \cdot \frac{n(n+1)}{2} = \frac{n}{2} \quad \text{where }n = b-a$

  * Let $X$ be a r.v. and let $Y = g(X)$. 

    $\mathbb{E}[g(X)] = E[Y] = \sum_y y p_Y(y) = \sum_x g(x) p_X(x)$.

    e.g. If $g(x)= x^2, \mathbb{E}[X^2] = \sum_x x^2 p_X(x)$

    Caution: $\mathbb{E}[g(X)] \neq g(\mathbb{E}[X]), \mathbb{E}[X^2] \neq (\mathbb{E}[X])^2$.

  * Linearity of expectation

    $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$
  
* The inclusion-exclusion formula

  * Let $A_1,A_2,\ldots ,A_ n$ be events.
    $$
    \mathbf{P}\left(\bigcup _{k=1}^ nA_ k\right) = \sum _{i}\mathbf{P}(A_ i)-{\sum _{i_1<i_2} \mathbf{P}(A_{i_1}\cap A_{i_2})}+{\sum _{i_1<i_2<i_3}\mathbf{P}(A_{i_1}\cap A_{i_2}\cap A_{i_3})} -\cdots +(-1)^{n-1}\mathbf{P}\left(\bigcap _{k=1}^ nA_ k\right).
    $$
    Here a sum such as $\displaystyle \sum _{i_1<i_2<i_3}$ stands for a triple sum, over all triples $(i_1, i_2, i_3)$ that satisfy $i_1 < i_2 < i_3$.

  * Example:

    $P(A_1 \cup A_2) = P(A_1) + P(A_2) - P(A_1 \cap A_2)$

    $P(A_1 \cup A_2\cup A_3) = P(A_1) + P(A_2)+ P(A_3) - (P(A_1 \cap A_2)+P(A_1 \cap A_3)+P(A_2 \cap A_3))\\ + P(A_1 \cap A_2 \cap A_3)$

There is 1 selected exercise and 3 solved problems.

---

## Exercise 1 The binomial PMF

You roll a fair six-sided die (all 6 of the possible results of a die roll are equally likely) 5 times, independently. Let X be the number of times that the roll results in 2 or 3. Find the numerical values of the following.

**Answer**: 

a) $p_ X(2.5)=\, 0$

b) $p_ X(1)=\,80/243$

**Solution**: 

a) A value of $2.5$ is not possible for $X$ since the number of rolls must be an integer.

b) For each die roll, there is a probability $2/6=1/3$ of obtaining a $2$ or a $3$. Hence, the random variable $X$ is binomial with parameters $n=5$ and $p=1/3$, so that $p_X(1)={5 \choose 1}⋅(1/3)⋅(2/3)^4≈0.32922$.

## Problem 1 Sampling people on buses

Four buses carrying $148$ job-seeking MIT students arrive at a job convention. The buses carry $40, 33, 25,$ and $50$ students, respectively. One of the students is randomly selected. Let $X$ denote the number of students that were on the bus carrying this randomly selected student. One of the $4$ bus drivers is also randomly selected. Let $Y$ denote the number of students on his bus.

1. Which of $\mathbb{E}[X]$ or $\mathbb{E}[Y]$ do you think is larger? Give your reasoning in words.
2. Compute $\mathbb{E}[X]$ and $\mathbb{E}[Y]$.

**Answer**:

1. We expect $\mathbb{E}[X]$ to be higher than $\mathbb{E}[Y]$ since if we choose the student, we are more likely to pick a bus with more students.

2. The PMF of $X$ is 
   $$
   p_X(x) = \begin{cases}40/148, &x=40 \\33/148, &x=33 \\ 25/148, &x=25\\ 50/148, &x=50\\ 0, &\text{otherwise} \end{cases}
   $$
   and $\mathbb{E}[X] = 40 \times {40 \over 138} + 33 \times {33 \over 148} + 25 \times { 25 \over 148} + 50 \times { 50 \over 148} = 39.28$

   The PMF of $Y$ is 
   $$
   p_Y(y) = \begin{cases}1/4 ,&y \in \{40,33,25,50\},\\0, & \text{otherwise} \end{cases}
   $$
   and $\mathbb{E}(Y) = 40 \times {1 \over 4} + 33 \times {1 \over 4} + 25 \times {1 \over 4} + 50 \times {1 \over 4} = 37$.

## Problem 2.1 From tail probabilities to expectations

Let $X$ be a random variable that takes nonnegative integer values. Show that 
$$
{\bf E}[X]=\sum _{k=1}^{\infty }\mathbf{P}(X\geq k).
$$
**Answer**: 

Recall the expectation formula:
$$
\mathbf{E}[X] = \sum_{k}k p_X(k)
$$
Note that 
$$
\mathbf{P}(X \geq k) = \sum^{\infty}_{i = k}p_X(i)
$$
and proceed as follows
$$
\sum^{\infty}_{k=1} \mathbf{P}(X \geq k) = \sum^{\infty}_{k=1}\sum^{\infty}_{i=k} p_X(i) = \sum^{\infty}_{i=1}\sum^i_{k=1} p_X (i) = \sum^{\infty}_{i=1} i p_X(i) = \mathbf{E}[X]
$$
This can be understood from the diagram below

![lec5_prob2](../assets/images/lec5_prob2.png)

## Problem 2.2 From tail probabilities to expectations

Find the expectation of a random variable $Y$ whose PMF is defined as follows:
$$
p_ Y(y)= \frac{1}{b-a+1}, \qquad y=a,a+1,\ldots ,b
$$
where $a$ and $b$ are nonnegative integers with $b > a$. Note that for $y = a,a+1,...,b$, $p_Y(y)$ does not depend explicitly on $y$ since it is a uniform PMF.

**Answer**: 

First compute
$$
\mathbf{P}(Y \geq k) = \begin{cases} 1, & k \leq a \\ \frac{b-k+1}{b-a+1}, & a+1 \leq k \leq b \\ 0, & k \geq b+1 \end{cases}
$$
Hence,
$$
\begin{aligned}
{\bf E}[Y]=\sum _{k=1}^{\infty }\mathbf{P}(Y\geq k) &= \sum^a_{k=1} a + \sum^b_{k = a+1} \frac{b-k+1}{b-a+1}\\
&=a + \frac{1}{b-a+1}\sum^{b-a}_{k=1}k \\
&= a+ \frac{1}{b-a+1} \frac{(b-a+1)(b-a)}{2}\\
&=a + {b-a \over 2} \\
&= {b+a \over 2}
\end{aligned}
$$

## Problem 3 True or False

Let $X $ and $Y$ be two binomial random variables

a. If $X$ and $Y$ are independent, then $X+Y$ is also a binomial random variable. [FALSE: parameters may be different.]

b. If $X$ and $Y$ have the same parameters, $n$ and $p$, then $X+Y$ is a binomial random variable. [FALSE: they may be dependent.]

c. If $X$ and $Y$ have the same parameters, $p$, and are independent, then $X+Y$ is a binomial random variable. [TRUE]

