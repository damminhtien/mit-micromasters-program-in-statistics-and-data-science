# Lecture 13. Conditional expectation and variance revisited; Application: Sum of a random number of independent r.v.'s

* A more abstract version of the conditional expectation

  * view it as a random variable

    $g(Y) = \mathbf{E}[X|Y]$

    $g(Y):$ is the r.v. that takes the value $\mathbf{E}[X | Y=y]$, if $Y$ happens to take the value $y$.

    | Discrete                                                  | Continuous                                         |
    | --------------------------------------------------------- | -------------------------------------------------- |
    | $g(y) = \mathbf{E}[X|Y=y] = \sum\limits_x x p_{X|Y}(x|y)$ | $g(y) = \mathbf{E}[X|Y=y] = \int x p_{X|Y}(x|y)dx$ |

    Remark: 

    * it is a function of $Y$
    * it is a random variable
    * it has a distribution, mean, variance, etc.

  * the law of iterated expectations

    $g(y) = \mathbf{E}[X | Y =y ], \quad g(Y) = \mathbf{E}[X | Y ]$

    $\mathbf{E}\left[\mathbf{E}[X|Y]\right] = \mathbf{E}[X]$

  * Conditional expectation properties

    * ${\bf E}\big [g(Y)X \, |\,  Y\big ] =g(Y) {\bf E}[X\, |\,  Y]$.

    * If $h$ is an invertible function, then $\mathbf{E}[X|Y] = \mathbf{E}[X|h(Y)]$.

  * Stick example: stick of length $l$ break at uniformly chosen point $Y$, break what is left at uniformly chosen point $X$.

    $\mathbf{E}[X|Y=y] = y/2, \quad \mathbf{E}[X|Y]= y/2$.

    $\mathbf{E}[X] = \mathbf{E}[\mathbf{E}[X|Y]] = \mathbf{E}[Y/2] = {1\over 2} \mathbf{E}[Y] =  {1\over 2} \cdot {l \over 2} = {l \over 4}$

* A more abstract version of the conditional variance

  * view it as a random variable

    $\mathsf{Var}(X) = \mathbf{E}\left[(X -\mathbf{E}[X])^2\right]$

    $\mathsf{Var}(X|Y = y) = \mathbf{E}\left[(X -\mathbf{E}[X|Y=y])^2|Y=y \right]$

    $\mathsf{Var}(X|Y)$ is the r.v. that takes the value $\mathsf{Var}(X|Y=y)$, when $Y=y$.

  * the law of total variance

    $\mathsf{Var}(X) = \mathbf{E}\left[\mathsf{Var}(X|Y)\right] + \mathsf{Var}\left(\mathbf{E}[X|Y]\right)$

    $\mathsf{Var}(X) = $ (average variability **within** sections) + (variability between sections)

* Sum of a random number of independent r.v.'s

  Let $Y = X_1 + ... + X_N$

  * mean

    $\mathbf{E}[Y | N= n] = \mathbf{E}[X_1+ ... + X_n|N=n] =  \mathbf{E}[X_1+ ... + X_n] = n \cdot \mathbf{E}[X] \implies \mathbf{E}[Y|N] = N \cdot \mathbf{E}[X]$

    $\mathbf{E}[Y] = \mathbf{E}[\mathbf{E}[Y|N]] = \mathbf{E}[N \cdot \mathbf{E}[X]] = \mathbf{E}[N] \cdot \mathbf{E}[X]$

  * variance

    $\mathsf{Var}(\mathbf{E}[Y|N]) = \mathsf{Var}(N \cdot \mathbf{E}[X]) = (\mathbf{E}[X])^2\mathsf{Var}(N)$

    $\mathsf{Var}(Y|N=n) = \mathsf{Var}(X_1 + ... + X_n | N=n) = \mathsf{Var}(X_1 + ... + X_n) = n \cdot \mathsf{Var}(X) \implies \mathsf{Var}(Y|N) = N \cdot \mathsf{Var}(X)$

    $\mathbf{E}[\mathsf{Var}(Y|N)] = \mathbf{E}[N \cdot \mathsf{Var}(X)] = \mathbf{E}[N]\cdot \mathsf{Var}(X) $

    $\mathsf{Var}(Y) = \mathbf{E}\left[\mathsf{Var}(Y|N)\right] + \mathsf{Var}\left(\mathbf{E}[Y|N]\right) = \mathbf{E}[N]\mathsf{Var}(X) + (\mathbf{E}[X])^2\mathsf{Var}(N)$

There are 3 selected exercises and 5 solved problems.

---

## Exercise 1 Iterated expectations

1. The law of iterated expectations tells us that ${\bf E}\big [{\bf E}[X\, |\, Y]\big ]={\bf E}[X]$. Suppose that we want apply this law in a conditional universe, given another random variable $Z$, in order to evaluate ${\bf E}[X \, |\, Z]$. Then which is true

   a. ${\bf E}\big [{\bf E}[X\, |\, Y,Z] \, |\, Z\big ]={\bf E}[X\, |\, Z]$

   b. ${\bf E}\big [{\bf E}[X\, |\, Y] \, |\, Z\big ]={\bf E}[X\, |\, Z]$

   c. ${\bf E}\big [{\bf E}[X\, |\, Y,Z] \big ]={\bf E}[X\, |\, Z]$

2. Determine which of the following statements are true about the quantity ${\bf E}\big [g(X,Y)\, |\, Y,Z \big ]$.

   a. A random variable

   b. A number

   c. A function of $(X,Y)$

   d. A function of $(Y,Z)$

   e. A function of $Z$ only

**Solution**:

1. a.

2. ad.

   A conditional expectation is generally a random variable, a function of the random variables on which we are conditioning, and so a function of $(Y,Z)$ in this case.

## Exercise 2 Conditional expectation and variance

1. The random variable $Q$ is uniform on $[0,1]$. Conditioned on $Q=q$, the random variable $X$ is Bernoulli with parameter $q$. Then what is the conditional expectation $\mathbf{E}[X|Q]$?
2. The random variable $Q$ is uniform on $[0,1]$. Conditioned on $Q=q$, the random variable $X$ is Bernoulli with parameter $q$. Then what is the conditional variance $\textsf{Var}(X\, |\, Q)$?
3. Recall that a uniform random variable on $[0,1]$ has a variance of $1/12$ and satisfies ${\bf E}[Q^2]=1/3$. Then what are $\textsf{Var}\big ({\bf E}[X\, |\, Q]\big )$ and ${\bf E}\big [\textsf{Var}(X\, |\, Q)\big ]$? 

**Solution**: 

1. ${\bf E}[X\, |\, Q]=Q$.

   Since ${\bf E}[X\, |\, Q=q]=q$, for all $q \in [0,1]$, the abstract statement ${\bf E}[X\, |\, Q]=Q$.

2. $\textsf{Var}(X\, |\, Q)=Q(1-Q)$.

   Since $\textsf{Var}(X\, |\, Q=q)=q(1-q)$, for all $q \in [0,1]$.

3. Since ${\bf E}[X\, |\, Q]=Q$, we have $\textsf{Var}\big ({\bf E}[X\, |\, Q]\big )=\textsf{Var}(Q)=1/12$.

   Since $\textsf{Var}(X\, |\, Q)=Q(1-Q)$, we have
   $$
   {\bf E}\big [\textsf{Var}(X\, |\, Q)\big ]={\bf E}\big [Q(1-Q)\big ]={\bf E}[Q]-{\bf E}[Q^2\big ]=\frac{1}{2}-\frac{1}{3}=\frac{1}{6}.
   $$

## Exercise 3 Second generation offspring

Every person has a random number of children, drawn from a common distribution with mean 3 and variance 2. The numbers of children of each person are independent. Let $M$ be the number of grandchildren of a certain person. Then what are ${\bf E}[M]$ and $\textsf{Var}(M)$?

**Answer**:

${\bf E}[M] = 9 ; \quad \textsf{Var}(M)= 24$. 

**Solution**:

Let $N$ be the number of children and let $X_i$ be the number of children of the $I$th child. Then $M = X_1 + ... + X_N$. And ${\bf E}(N) = 3, \quad \mathsf{Var}(N) = 2$ according to the problem statement.

It follows that
$$
{\bf E}[M]={\bf E}[N]\cdot {\bf E}[X]=3\cdot 3=9
$$
Furthermore,
$$
\textsf{Var}(M)={\bf E}[N]\textsf{Var}(X)+\big ({\bf E}[X]\big )^2\textsf{Var}(N)=3\cdot 2+9\cdot 2 =24.
$$

## Problem 1 Using conditional expectation and variance

The random variables $X$ and $Y$ are described by a joint PDF which is constant within the unit area quadrilateral with vertices $(0,0),(0,1),(1,2),$ and $(1,1)$. Use the law of total variance to find the variance of $X + Y$.

**Solution**:

Recall the formula of variance
$$
\mathsf{Var}(X+Y) = \mathsf{Var}(\mathbf{E}[X+Y | X]) + \mathbf{E}[\mathsf{Var}(X+Y | X)]\\
\mathsf{Var}(X+Y) = \mathsf{Var}(\mathbf{E}[X+Y | Y]) + \mathbf{E}[\mathsf{Var}(X+Y | Y)]
$$
We pick the first one (condition on $X$), because when $x$ is fixed, the PDF of $Y$ conditioning on $X$ is uniformly distributed between $[x,x+1]$, as shown in the figure below. 

![u6-lec13-prob1](../assets/images/u6-lec13-prob1.png)

First compute $\mathbf{E}[X+Y | X] $,
$$
\mathbf{E}[X+Y | X] = x +\mathbf{E}[Y | X] = x + {2x+1\over 2} = 2x + {1\over 2}
$$
Recall that the variance of Uniform distribution (uniformly distributed between $a$ and $b$) is $\mathsf{Var}(X) = {(b-a)^2\over 12}$. We then compute $\mathsf{Var}(X+Y | X)$,
$$
\mathsf{Var}(X+Y | X) = \mathsf{Var}(Y|X) = {1\over 12}
$$
Therefore,
$$
\mathsf{Var}(X + Y) = \mathsf{Var}(2x + {1\over 2}) + \mathbb{E}[{1\over 12}] = 4 \mathsf{Var}(x) + {1\over 12}
$$
To figure out $\mathsf{Var}(X)$, we need PDF of $X$ given a joint PDF. Note that if we fix $X$ and integrate over $Y$, we get $1$. Thus, the PDF of $X$ $f_X(x)$ is uniformly distributed between $[0,1]$.

Therefore,
$$
\mathsf{Var}(X + Y)  = 4 \mathsf{Var}(x) + {1\over 12} = 4 \times ({1\over 12}) + {1\over 12} = {5\over 12}
$$

## Problem 2 The variance in the stick-breaking problem

We start with a stick of length $\ell$ . We break it at a point which is chosen randomly and uniformly over its length, and keep the piece that contains the left end of the stick. We then repeat the same process on the piece that we were left with.

1. What is the expected value of the length of the piece that we are left with after breaking twice?
2. What is the variance of the length of the piece that we are left with after breaking twice?

**Solution**:

1. Let $Y$ be the length of the left stick after the first break, and $X$ be the length of the left stick after the second break. We have $Y \sim \mathsf{Unif}[0,\ell]$. We know that $\mathbb{E}[Y] = {l \over 2}, \mathsf{Var}(Y) = {l^2\over 12}$. If we were given $Y=y$, $X \sim \mathsf{Unif}[0,y]$. We then know $\mathbb{E}[X|Y] = {Y\over 2}, \mathsf{Var}(X|Y) = {Y^2\over 2} $.

   Therefore,
   $$
   \mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X|Y]] = \mathbb{E}[{Y\over 2}] = {l\over 4}
   $$

2. Recall that $\mathsf{Var}(X) = \mathbb{E}[\mathsf{Var}(X|Y)] + \mathsf{Var}(\mathbb{E}[X|Y])$

   For the first part,
   $$
   \begin{aligned}
   \mathbb{E}[\mathsf{Var}(X|Y)] &= \mathbb{E}[{Y^2\over12}] = {1\over 12} \mathbb{E}[Y^2]\\
   &= {1\over 12}\left(\mathsf{Var}(Y) + (\mathbb{E}[Y])^2\right)\\
   &= {1\over 12}\left({l^2\over 12} + {l^2 \over 4}\right)\\ 
   &= {l^2 \over 36}
   \end{aligned}
   $$
   For the second part,
   $$
   \mathsf{Var}(\mathbb{E}[X|Y]) = \mathsf{Var}({Y\over 2}) = {1\over 4} \mathsf{Var}(Y) = {l^2\over 48}
   $$
   Combined together, we obtain
   $$
   \mathsf{Var}(X) = {l^2 \over 36} + {l^2 \over 48} = {7 l^2 \over 144 }
   $$

## Problem 3 A coin with random bias

We toss $n$ times a biased coin whose probability of heads, denoted by $q$, is the value of a random variable $Q$ with given mean $\mu$ and positive variance $\sigma^2$. Let $X_i$ be a Bernoulli random variable that models the outcome of the $i$th toss (i.e. $X_i=1$ if the $i$th toss is a head). We assume that $X_1,...,X_n$ are conditionally independent, given $Q=q$. Let $X$ be the number of head obtained in the $n$ tosses.

1. Use the law of iterated expectations to find $\mathbf{E}[X_i]$ and $\mathbf{E}[x]$.
2. Find $\mathsf{Cov}(X_i, X_j)$. Are $X_1, ..., X_n$ independent?
3. Use the law of total variance to find $\mathsf{Var}(X)$. Verify your answer using the covariance results of (1).

**Solution**:

1. By the law of iterated expectations and the fact $\mathbf{E}[X_i|Q] = Q$, we have
   $$
   \mathbf{E}[X_i] = \mathbf{E}[\mathbf{E}[X_i|Q]] = \mathbf{E}[Q]=\mu
   $$
   Since $X=X_1 + ... + X_n$, it follows that
   $$
   \mathbf{E}[X] = \mathbf{E}[X_1] + ... + \mathbf{E}[X_n] = n \mu
   $$

2. We have, for $ i \neq j$, using the conditional independence assumption,
   $$
   \mathbf{E}[X_iX_j|Q] = \mathbf{E}[X_i|Q]\mathbf{E}[X_j|Q] = Q^2
   $$
   and 
   $$
   \mathbf{E}[X_iX_j] = \mathbf{E}[\mathbf{E}[X_iX_j|Q]] = \mathbf{E}[Q^2]
   $$
   Thus, 
   $$
   \mathsf{Cov}(X_i, X_j) = \mathbf{E}[X_iX_j] - \mathbf{E}[X_i]\mathbf{E}[X_j] = \mathbf{E}[Q^2] - \mu^2 = \sigma^2
   $$
   Since $\mathsf{Cov}(X_i, X_j) > 0, X_1, ...,X_n$ are not independent,

   Also, for $i=j$, using the observation that $X_i^2 = X_i$,
   $$
   \begin{aligned}
   \mathsf{Var}(X_i) &= \mathbf{E}[X_i^2] - (\mathbf{E}[X_i])^2\\
   &= \mathbf{E}[X_i] - (\mathbf{E}[X_i])^2\\
   &= \mu -\mu^2
   \end{aligned}
   $$

3. Using the law of total variance, and the conditional independence of $X_1, ...,X_n$, we have
   $$
   \begin{aligned}
   \mathsf{Var}(X) &= \mathbf{E}[\mathsf{Var}(X|Q)] + \mathsf{Var}(\mathbf{E}[X|Q])\\
   &=\mathbf{E}[\mathsf{Var}(X_1 + ... + X_n|Q)] + \mathsf{Var}(\mathbf{E}[X_1 + ... + X_n|Q])\\
   &= \mathbf{E}[nQ(1-Q)]+ \mathsf{Var}(nQ)\\
   &= n \mathbf{E}[Q-Q^2] + n^2 \mathsf{Var}(Q)\\
   &= n(\mu - \mu^2 - \sigma^2) + n^2 \sigma^2\\
   &= n(\mu - \mu^2) + n(n-1)\sigma^2.
   \end{aligned}
   $$
   To verify the result using the covariance formulas of (2), we write
   $$
   \begin{aligned}
   \mathsf{Var}(X) &= \mathsf{Var}(X_1 + ... + X_n)\\
   &= \sum^n_{i=1}\mathsf{Var}(X_i) + \sum_{\{(i,j) | i \neq j\}} \mathsf{Cov}(X_i, X_j)\\
   &= n \mathsf{Var}(X_1) + (n^2-n)\mathbf{Cov}(X_1, X_2)\\
   &= n(\mu - \mu^2) + (n^2-n)\sigma^2s
   \end{aligned}
   $$

## Problem 4 Random number of coin flips

1. You roll a fair six-sided die, and then you flip a fair coin the number of times shown by the die. Assuming that the coin flips are independent, find the expected value and the variance of the number of heads obtained.
2. Repeat part (1) for the case where you roll two dice, instead of one.

**Solution**:

1. Let $X_i$ be independent Bernoulli random variable that are equal to $1$ if the $i$th flip results in heads. Let $N$ be the number of coin flips, and let $H$ be the number of heads. 

   Using the notation, we have $H = X_1 + ... + X_N$. We also know $\mathbf{E}[X_i] = 1/2, \mathsf{Var}(X) = 1/4$ for all $i$ since the coin if fair.

   Since $N$ follows a **discrete uniform distribution** from $1$ to $6$ with $p = 1/6$, we have $\mathbf{E}[N] = 7/2, \mathsf{Var}(N)=35/12$.

   Therefore, the expected number of heads is
   $$
   \mathbf{E}[H] = \mathbf{E}[X_i]\mathbf{E}[N] = {1\over 2}\cdot {7 \over 2} = {7 \over 4}
   $$
   and the variance is
   $$
   \mathsf{Var}(H) = \mathsf{Var}(X_i)\mathbf{E}[N] + (\mathbf{E}(X_i))^2\mathsf{Var}(N) = {1\over 4} \cdot {7\over 2} + {1\over 4} \cdot {35 \over 12} = {77\over 48}
   $$

2. Let $N_1$ denotes the 1st die, $N_2$ denotes the 2nd dies, $H_1$ denotes the number of heads for $N_1$ coin flips, $H_2$ denotes the number of heads for $N_2$ coin flips.

   $N^* = N_1 + N_2 $ represents the total coin flips, $H^* = H_1 + H_2$ represents the total heads.

   Therefore, 
   $$
   \mathsf{Var}(H^*) = 2 \mathsf{Var}(H) = {7 \over 2} \\ 
   \mathbf{E}[H^*] = \mathbf{E}[H_1] + \mathbf{E}[H_2] = 2 \mathbf{E}[X]={77\over 24}
   $$

## Problem 5 Sum of a random number of r.v.'s

A fair coin is flipped independently until the first Heads is observed. Let the random variable $K$ be the number of tosses until the first Heads is observed **plus 1**. For example, if we see TTTHTH, so that the first head is observed after $4$ tosses, then $K=4+1=5$. For $k=1,2,...,K$, let $X_k$ be a continuous random variable that is uniform over the interval $[0,5]$. The $X_k$ are independent of one another and of the coin flips. Let $X=\sum _{k=1}^ K X_ k$. Find the mean and variance of $X$.

**Solution:**

Recall the mean and variance of a geometric random variable with parameter $p $ are $1/p$ and $(1-p)/p^2$.

Since $X_k$ is uniform over $[0,5]$, we have ${\bf E}[X_ k]=5/2$ and $\textsf{Var}(X_ k)=5^2/12=25/12$.

Note that $K-1$ is geometric with parameter $p = 1/2$. So ${\bf E}[K-1]=2$ and ${\rm Var}(K-1)=2$, which implies ${\bf E}[K]=3$ and $\textsf{Var}(K)=2$.

Since $X = \sum ^{K}_{k=1}X_ k$ is the sum of a random number of independent and identically distributed random variables, we have
$$
{\bf E}[X]={\bf E}[X_1]{\bf E}[K] = \frac{5}{2}\cdot 3 = 15/2,
$$
and
$$
\textsf{Var}(X)= \textsf{Var}(X_1){\bf E}[K] + ({\bf E}[X_1])^2 \textsf{Var}(K) = \frac{25}{12}\cdot 3+\frac{25}{4}\cdot 2= 75/4.
$$


