# Lecture 7. Conditioning on a random variable ; Independence of r.v's

* Conditional PMFs

| Two r.v.s                                                    | >Two r.v.s                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| $p_{X\|Y}(x\|y) = \frac{p_{X,Y}(x,y)}{p_Y(y)}$               | $p_{X\|Y,Z}(x\|y,z) = \frac{\mathbf{P}_{X,Y,Z}(x, y, z)}{\mathbf{P}_{Y,Z}(y, z)} \\p_{X,Y\|Z}(x,y\|z) = \frac{\mathbf{P}_{X,Y,Z}(x, y, z)}{\mathbf{P}_{Z}(z)} $ |
| $\sum_xp_{X\|Y}(x\|y) = 1$                                   | $\sum_x p_{X\|Y,Z}(x\|y,z) =1 \\ \sum_x \sum_y p_{X,Y\|Z}(x,y\|z)=1$ |
| $p_{X,Y}(x,y) = p_Y(y)p_{X\|Y}(x\|y) \\ p_{X,Y}(x,y) = p_X(x)p_{Y\|X}(y\|x)$ | $p_{X,Y,Z}(x,y,z) = p_X(x)p_{Y\|X}(y\|x)p_{Z\|X,Y}(z\|x,y)$  |

  * Conditional PMFs

      * Conditional expectations

        | Non-conditional                    | Conditional                                     |
        | ---------------------------------- | ----------------------------------------------- |
        | $\rm E[X] = \sum_x x p_X(x)$       | $\rm E[X\|Y=y] = \sum_x x p_{X\|Y}(x\|y)$       |
        | $\rm E[g(X)] = \sum_x g(x) p_X(x)$ | $\rm E[g(X)\|Y=y] = \sum_x g(x) p_{X\|Y}(x\|y)$ |

      * Total probability and expectation theorem

        $p_X(x)=\sum_yp_Y(y)p_{X|Y}(x|y)$

        $\rm E[X] = \sum_y p_Y(y)E[X|Y=y]$

* Independence of r.v.'s

  * Of two events: $\mathbf{P}(A \cap B) = \mathbf{P}(A) \cdot \mathbf{P}(B), \quad \mathbf{P}(A|B) = \mathbf{P}(A)$

  * Of a r.v. and an event: 

    $\mathbf{P}(X=x, A) = \mathbf{P}(X=x) \cdot \mathbf{P}(A), $ for all $x$. 

    $p_{X|A}(x) = p_X(x),$ for all $x$.

    $\mathbf{P}(A|X=x) = \mathbf{P}(A),$ for all $x$.

  * Of two r.v.'s: 

    $\mathbf{P}(X=x, Y=y) = \mathbf{P}(X=x) \cdot \mathbf{P}(Y=y), $ for all $x,y$.

    $p_{X,Y}(x,y) = p_X(x) p_Y(y),$ for all $x,y$.

    $p_{X|Y}(x|y) = p_X(x)$

    $p_{Y|X}(y|x) = p_Y(y)$

  * Of three r.v.'s

    $p_{X,Y,Z}(x,y,z) = p_X(x) p_Y(y) p_Z(z), $ for all $x,y,z$.

* Independence and Expectation

  If $X, Y$ are independent: $\rm E[XY] = E[X] E[Y]$, $g(X)$ and $h(Y)$ are also independent: $\rm E[g(X)h(Y)] = E[g(X)]E[h(Y)]$.

* Independence and Variance

  If $X,Y$ are independent: $\rm{var}(X+Y) = \rm{var}(X) + \rm{var}(Y)$

* The variance of the binomial

* $X \sim \rm Bin(n,p)$ : $\rm{var}(X) = np(1-p)$

* **The hat problem**: 

     $n$ people throw their hats in a box and then pick one at random

     * All permutations equally likely, equivalent to picking one hat at a time: $\frac{1}{n!}$.

     * $X$: number of people who get their own hat, $X = X_1 + X_2 +... + X_n$, where $X_i$ is the indicator function.

       * Find $\rm E[X]$:

         $\rm E[X_i] = \mathbf{P}(X_1 = 1) = {1 \over n}$.

         $\rm E[X] = E[X_1 + X_2 +... + X_n] = E[X_1] + E[X_2] +... + E[X_n] = n \cdot {1 \over n} = 1$.

       * Find $\rm{var}(X)$: Note that $X_i$ are dependent.

         To compute $\rm{var}(X) = E[X^2] - (E[X])^2$, we have to compute the following quantities first:

         $X^2 = \sum_i X_i^2 + \sum_{i,j,L i\neq j} X_i X_j$.

         $\rm E[X_i^2] = E[X_1^2]=E[X_1] = 1/n, \quad \text{since it is an indicator}$.

         For $i \neq j$: $\rm E[X_iX_j] = E[X_1 X_2] = \mathbf{P}(X_1X_2 = 1) = \mathbf{P}(X_1 =1, X_2 = 1) = \mathbf{P}(X_1 = 1) \mathbf{P}(X_2  = 1| X_1 = 1) = {1\over n}{1\over n-1}$.

         Therefore, $\rm{var}(X) = E[X^2] - (E[X])^2 = n \cdot {1 \over n} + (n^2 - n) \cdot { 1\over n} {1 \over n-1 } - 1 = 1 + 1 - 1 = 1$.

There are 2 selected exercises and 5 solved problems.

---

## Exercise 1 The expected value rule with conditioning

The following equations are all true: 

${{\bf E}[g(X,Y)\mid Y=2]=\sum _ x g(x,2) \frac{p_{X,Y}(x,2)}{p_ Y(2)}}$

${{\bf E}[g(X,Y)\mid Y=2]=\sum _ x g(x,2) \frac{p_{X,Y}(x,2)}{p_ Y(2)}}$

$ {{\bf E}[g(X,Y)\mid Y=2]=\sum _ x \sum _ y g(x,y) p_{X,Y\mid Y}(x,y\mid 2)}$

Note that $p_{X,Y\mid Y}(x,y\mid 2)$ will be zero for any $y \neq 2$. And for $y =2$.

$p_{X,Y\mid Y}(x,2\mid 2)=\mathbf{P}(X=x, Y=2\mid Y=2)=\mathbf{P}(X=x\mid Y=2)=p_{X\mid Y}(x\mid 2),$

So that the sixth formula agrees with the fourth one.

## Exercise 2 Independence and variances

The pair of random variables $(X,Y)$ is equally likely to take any of the four pairs of values $(0,1), (1,0), (−1,0), (0,−1)$. Note that $X$ and $Y$ each have zero mean. Find $\textsf{Var}(X+Y)$.

**Answer**: $\textsf{Var}(X+Y)=\textsf{Var}(X)+\textsf{Var}(Y)$

**Solution**: ${\bf E}[X+Y]=0, \textsf{Var}(X)={\bf E}[X^2], \textsf{Var}(Y)={\bf E}[Y^2]$,
$$
\begin{aligned}
\textsf{Var}(X+Y) &= {\bf E}[(X+Y)^2] - ({\bf E}[X+Y])^2\\
&= {\bf E}[(X+Y)^2]\\
&={\bf E}[X^2]+2{\bf E}[XY]+{\bf E}[Y^2]\\
&= {\bf E}[X^2]+{\bf E}[Y^2]\\
&= \textsf{Var}(X)+\textsf{Var}(Y).
\end{aligned}
$$
**Remark**: If $X$ and $Y$ are independent, $\textsf{Var}(X+Y)=\textsf{Var}(X)+\textsf{Var}(Y)$. But the converse is not true. That is, the condition $\textsf{Var}(X+Y)=\textsf{Var}(X)+\textsf{Var}(Y)$ does not imply independence.

## Problem 1 Indicator variables: the number of inversions

There are $n$ persons, numbered $1$ to $n$. Each person $i$ is assigned a seat number $X_i$. The seat numbers are distinct integers in the range $1,…,n$. We assume that the seating is “completely random", that is, the sequence ($X_1,…,X_n$) is a permutation of the numbers $1,…,n$, and all permutations are equally likely.

For any $i$ and $j$, with $ 1 \leq i < j \leq n$, we say that we have an inversion if $X_ i>X_ j$. Let $N$ be the number of inversions. Find $E[N]$.

**Answer**: $E[N] = {1 \over 2}  {n \choose 2} $

**Solution**: 

We use the method of indicator functions. 
$$
Y_{ij} = \begin{cases}1, &X_i > X_j \\ 0, &X_i \leq X_j  \end{cases}
$$
Then we have
$$
N = \sum_{i<j} Y_{ij}
$$
By the linearity of expectation, we have:
$$
\begin{aligned}
E[N] &= \mathbf{E}\left[\sum_{i < j} Y_{ij}\right]\\
&= \sum_{i<j} \mathbf{E}[Y_{ij}]\\
&= \sum_{i<j} \mathbf{P}(X_i > X_j)\\
&= \sum_{i<j} {1 \over 2} \quad \text{Since }\mathbf{P}(X_i > X_j) \text{ and } \mathbf{P}(X_i < X_j) \text{ are the same}\\
&=\sum^{n-1}_{i=1} \sum^n_{j = i+1} {1 \over 2}\\
&= {1 \over 2} {n(n-1) \over n} = {1 \over 2} {n \choose 2}
\end{aligned}
$$
Another way to see this is to observe that there are $n \choose 2$ pairs total, and by symmetry, the expected number of pairs in inverted order will be half of the total number of pairs.

## Problem 2 Indicator variables: the problem of joint lives

Consider $2m$ persons forming $m$ couples who live together at a given time. Suppose that at some later time, the probability of each person being alive is $p$, independently of other persons. At that later time, let $A$ be the number of persons that are alive and let $S$ be the number of couples in which both partners are alive. For any number of total surviving persons $a$, find $\mathbf{E}[S∣A=a]$.

**Answer**: $\frac{a(a-1)}{2(2m-1)}$

**Solution**: 

Let $X_i$ be the random variable taking the value $1$ or $0$ depending on whether the first partner of the $i$th couple has survived or not. Let $Y_i$ be the corresponding random variable for the second partner of the $i$th couple.  So $X_i$ and $Y_i$ are indicator variables:
$$
X_i = \begin{cases}1, &\text{if 1st partner in coulple alive} \\0, &\text{otherwise}  \end{cases}\\
Y_i = \begin{cases}1, &\text{if 2nd partner in coulple alive} \\0, &\text{otherwise}  \end{cases}
$$
Then, $Z_i = X_iY_i$ is also an indicator variable.
$$
Z_i = \begin{cases}1, &\text{if coulple is alive} \\0, &\text{otherwise}  \end{cases}
$$
So we have $S = \sum^m_{i=1} X_iY_i$. By using linearity of expectations and the total expectation theorem,
$$
\begin{aligned}
\mathbf{E}(S|A = a) &= \sum^m_{i=1} \mathbf{E}[X_iX_j|A=a]\\
&= m\mathbf{E}[X_1Y_1 | A=a]\\
&=m\mathbf{E}[Y_1 = 1 | X_1 = 1, A=a] \mathbf{P}(X_1 = 1 | A=a)\\
&=m\mathbf{P}(Y_1 = 1 | X_1 = 1, A=a) \mathbf{P}(X_1 = 1 | A=a)\\
\end{aligned}
$$
Note that given indicator variable $X_iY_i$, $\mathbf{E}[X_1Y_1 | A=a]  = \mathbf{P}(X_1Y_1 = 1 | A=a)$.

We have
$$
\mathbf{P}(X_1 = 1 | A =a ) = {a \over 2m}, \qquad \mathbf{P}(Y_1=1|X_1 = 1, A= a) = {a-1 \over 2m-1}
$$
Hence,
$$
\mathbf{E}[S | A=a] = m {a-1 \over 2m-1} \cdot {a \over 2m} = {a(a-1) \over 2(2m-1)}
$$
Note that $\mathbf{E}[S|A=a]$ does not depend on $p$.

## Problem 3

Let $N$ be a positive integer random variable with PMF of the form
$$
p_ N(n)=\frac{1}{2}\cdot n\cdot 2^{-n},\qquad n=1,2,\ldots .
$$
Once we see the numerical value of $N$, we then draw a random variable $K$ whose (conditional) PMF is uniform on the set $\{1,2,...,2n\}$. 

1. Write down an expression for the joint PMF $p_{N,K}(n,k)$, for $n=1,2,...$ and $k = 1,2,...,2n$.

2. Find the marginal PMF $p_K(k)$ as a function of $k$, for $k=2,4,6,...$ For simplicity, provide the answer **only for the case when** $k$ **is an even number**. 

   *Hint*: $ \sum _{i=0}^{\infty } r^ i = \frac{1}{1-r}$

3. Let $A$ be the event that $K$ is even. Find $\mathbf{P}(A|N=n)$ and $\mathbf{P}(A)$.

**Solution**:

1) $p_{N,K}(n,k)= {1 \over 2^{n+2}}$

Since $K$ is uniform distributed from $1$ to $2n$, we have
$$
p_{K \mid N}(k \mid n) = \frac{1}{2n}, \qquad k = 1,2,\dots , 2n.
$$
By definition, the joint PMF is 
$$
p_{N,K}(n, k) = p_{K \mid N}(k \mid n) p_{N}(n) = \frac{1}{2n} \frac{1}{2} \cdot n \cdot 2^{-n} = (\frac{1}{2})^{n+2}, \qquad n=1,2,\dots , \quad k=1,2,\dots , 2n
$$
2) $p_ K(k)= {1 \over 2^{k/2+1}}$

By definition of $p_{K}(k) = \sum _{n=1}^{\infty } p_{N,K}(n,k)$, and only the terms from $n = k/2$ and above have non-zero probability. Hence,
$$
\begin{aligned}
p_K(k) &= \sum _{n=k/2}^{\infty } p_{N,K}(n,k) = \sum _{n=k/2}^{\infty } (\frac{1}{2})^{n+2}\\
&=\sum _{n=k/2}^{\infty } (\frac{1}{2})^{n+2} = \frac{1}{4} \sum _{n=k/2}^{\infty } (\frac{1}{2})^ n\\
&= \frac{1}{4} \Big[\sum _{n=0}^{\infty } (\frac{1}{2})^ n - \sum _{0}^{k/2-1} (\frac{1}{2})^ n \Big]\\
&= \frac{1}{4} \Big[\frac{1}{1-\frac{1}{2}} - \frac{1-(\frac{1}{2})^{k/2-1+1}}{1-\frac{1}{2}} \Big]\\
&=(\frac{1}{2})^{k/2+1} \qquad \text {for} k = 2, 4, \dots
\end{aligned}
$$

3)  $\mathbf{P}(A|N=n)=\mathbf{P}(A) = 1/2$.

We need to check the **independence** between $A$ and $N$ by checking whether $\mathbf{P}(A|N=n)=\mathbf{P}(A)$. 

Now because $p_{K|N}(k|n)$ is uniform over the $2n$-size set $\{1,2,...,2n\}$ and there are exactly $n$ even numbers in this set, we have that
$$
P(A \mid N=n) = \frac{n}{2n} = \frac{1}{2}, \qquad n \geq 1.
$$
Intuitively, knowledge of $n$ does not affect the beliefs about $A$, and we have **independence**. A full, formal argument goes as follows
$$
P(A)= \sum _{n=1}^{\infty }P(A\mid N=n) P(N=n)= \frac{1}{2}\sum _{n=1}^{\infty }P(N=n)=\frac{1}{2}
$$
where the last step follows because PMFs always sum to 1. So, $P(A\mid N=n)=P(A)$ for all $n$.

Equivalently, $P(A \  {\rm and} \  N=n) = P(A\mid N=n)\cdot P(N=n) = P(A)\cdot P(N=n)$.

## Problem 4 Joint PMF

The joint PMF, $p_{X,Y}(x,y)$ of the random variables $X$ and $Y$ is given by the following table:

![u4-prob1-table](D:/git/fundamentals-of-statistics-notes/docs/assets/images/u4-prob1-table.png)

1. Find the value of the constant $c$.
2. Find $p_X(1)$.
3. Consider the random variable $Z = X^2 Y^3$. Find $\mathbf{E}(Z|Y=-1)$.
4. Conditioned on the event that $Y\neq 0$, are $X$ and $Y$ independent?
5. Find the conditional variance of $Y$ given that $X=0$.

**Solution**: 

1) Since the probability of the entire sample space equals to 1.
$$
\begin{aligned}
1 &= \sum ^1_{x=-2}\displaystyle \sum ^1_{y=-1} p_{X,Y}(x,y)\\
&=2c + 3c + 4c + 2c + c + 2c + 4c + 2c + 8c\\
&=28c
\end{aligned}
$$
Therefore, $c = 1/28$.

2) $p_ X(1) = \displaystyle \sum ^1_{y=-1}p_{X,Y}(1,y) = 4c + 2c + 8c = 14c = \frac{1}{2}.$

3) 
$$
\begin{aligned}
{\bf E}[Z \mid Y=-1] &= {\bf E}[X^2Y^3 \mid Y=-1]\\
&= {\bf E}[X^2(-1)^3 \mid Y=-1]\\
&=-{\bf E}[X^2 \mid Y=-1]
\end{aligned}
$$
In order to calculate this conditional expectation, we need the conditional PMF of $X$ given $Y=-1$.
$$
p_{X\mid Y}(x \mid -1) = \frac{p_{X,Y}(x,-1)}{p_ Y(-1)}=\left\{ \begin{array}{ll} \frac{2c}{7c} = \frac{2}{7},\;  \;  &  \textrm{if } x = -2, \\ \frac{c}{7c} = \frac{1}{7},\;  \;  &  \textrm{if } x = 0, \\ \frac{4c}{7c} = \frac{4}{7},\;  \;  &  \textrm{if } x = 1, \\ 0, &  \text{otherwise.} \end{array} \right.
$$
Therefore,
$$
\begin{aligned}
{\bf E}[Z \mid Y=-1] &= - \sum ^1_{x=-2}x^2p_{X\mid Y}(x \mid -1)\\
&=-\left((-2)^2\cdot \frac{2}{7} + 1^2\cdot \frac{4}{7}\right)\\
&=-{12\over 7}
\end{aligned}
$$
4) Yes. Given $Y \neq 0$,, the conditional distribution $Y$ given $X =x$ is the same for all $x \in \{-2,-1,0,1\}$: $\mathbf{P}(Y=y \mid X=x,Y\neq 0) = \mathbf{P}(Y=y \mid Y\neq 0)$, for all $x \in \{-2,-1,0,1\}$

For example,
$$
\begin{aligned}
\mathbf{P}(Y=1 \mid X=-2, Y\neq 0) &=\mathbf{P}(Y=1 \mid X=0, Y\neq 0)\\
&=\mathbf{P}(Y=1 \mid X=1, Y\neq 0)\\
&=\mathbf{P}(Y=1 \mid Y \neq 0) = \frac{2}{3}.
\end{aligned}
$$
5) We first find the conditional PMF of $Y$ given $X=0$:
$$
p_{Y\mid X}(y\mid 0) = \frac{p_{X,Y}(0,y)}{p_ X(0)} = \begin{cases}  \frac{c}{c+2c}=\frac13, &  \text{if } y=-1,\\ \frac{2c}{c+2c}=\frac23, &  \text{if } y=1,\\ 0, &  \text{otherwise.} \end{cases}
$$
We can then calculate the conditional expectation:
$$
{\bf E}[Y\mid X=0] = \sum _{y=-1}^1 yp_{Y\mid X}(y\mid 0) = (-1)\cdot \frac{1}{3}+(1)\cdot \frac23 = \frac13.
$$
Finally, the conditional variance can be calculated as
$$
\begin{aligned}
\textsf{Var}(Y\mid X=0) &= {\bf E}[(Y-{\bf E}[Y\mid X=0])^2 \mid X=0]\\
&={\bf E}\left[\left(Y-\frac13\right)^2\mid X=0\right]\\
&=\sum _{y=-1}^1 \left(y-\frac13\right)^2p_{Y\mid X}(y\mid 0)\\
&=\left(-1-\frac13\right)^2\cdot \left(\frac13\right) + \left(1-\frac13\right)^2\cdot \left(\frac23\right)\\
&= {8 \over 9}
\end{aligned}
$$

## Problem 5 Indicator Variables

Consider a sequence of $n+1$ independent tosses of a biased coin, at times $k=0,1,2,…,n$. On each toss, the probability of Heads is $p$, and the probability of Tails is $1−p$.

A reward of one unit is given at time $k$, for $k∈\{1,2,…,n\}$, if the toss at time $k$ resulted in Tails and the toss at time $k−1$ resulted in Heads. Otherwise, no reward is given at time $k$.

Let $R$ be the sum of the rewards collected at times $1,2,..., n$.

1. Find $\mathbf{E}[R]$.
2. Find $\mathsf{Var}(R)$, assuming that $p = 3/4, n = 10$.

**Solution**: 

1) First find $\mathbf{E}(I_k)$. Since $I_k$ is a Bernoulli indicator variable and the tosses are independent, we have
$$
{\bf E}[I_ k] = \mathbf{P}(I_ k = 1) = \mathbf{P}(\text {Tails at time k and Heads at time } k-1) = p(1-p).
$$
Given the total reward over all the tosses $R$ is the sum of all the $I_k$'s, for $k=1,2,...,n.$ To find $\mathbf{E}[R]$, by linearity of expectations, we have
$$
{\bf E}[R] = {\bf E}\left[ \sum _{k=1}^ n I_ k \right] = \sum _{k=1}^ n {\bf E}\left[ I_ k \right] = np(1-p).
$$
2) First find $\mathbf{E}[I_k^2]$. Since $I_k$ can only be $0$ or $1$, we have
$$
\mathbf{E}[I_k^2]=\mathbf{E}[I_k]=p(1-p)
$$
Then find $\mathbf{E}[I_kI_{k+1}]$. Since $I_kI_{k+1} = 1$ if $I_k = 1$ and $I_{k+1} = 1$. i.e. if a reward was given at time $k $ and at time $k+1$ which is impossible. Therefore
$$
\mathbf{E}[I_kI_{k+1}] = 0
$$
Next find $\mathbf{E}[I_kI_{k+l}]$ if $k\geq 1, l \geq 2, k+l \geq n$. Since the reward at time $k$ depends only on the tosses at times $k$ and $k−1$, the rewards at times that are at least $2$ periods apart depend on different, non-overlapping pairs of coin tosses, and hence $I_k$ and $I_{k+l}$ are independent for $l≥2$. Therefore, 
$$
\mathbf{E}[I_kI_{k+l}] = {\bf E}[I_ k]{\bf E}[I_{k+\ell }]  = p^2 \cdot (1-p)^2
$$
Now find $\mathbf{E}[R^2]$. We have
$$
{\bf E}[R^2] = {\bf E}\left[\left(\sum _{k=1}^ n I_ k\right)\left(\sum _{m=1}^ n I_ m\right)\right] = {\bf E}\left[\sum _{k=1}^ n\sum _{m=1}^ nI_ kI_ m\right] = \sum _{k=1}^ n \sum _{m=1}^ n {\bf E}[ I_ k I_ m ]
$$
There are $n^2$ terms in this double summation. We can divide them into three groups:

1. There are $n$ terms where $k=m$. From previous calculation, we know $\mathbf{E}[I_kI_m] = \mathbf{E}[I_k^2]=\mathbf{E}[I_k]=p(1-p)$
2. There are $n-1$ terms where $k= m+1$ and another $n-1$ terms where $m = k+1$. From previous calculation, we know that ${\bf E}[I_ kI_ m]=p^2(1-p)^2$.
3. The remaining $n^2 - n - 2(n-1) = n^2 - 3n + 2$ terms are those where $k$ and $m$ differ by at least 2. From previous calculation, we know that ${\bf E}[I_ kI_ m]=p^2(1-p)^2$.

Putting together, we have
$$
{\bf E}[R^2] = n\cdot p(1-p) + 2(n-1)\cdot 0 + (n^2-3n+2)\cdot p^2(1-p)^2.
$$
Therefore, we can find $\mathsf{Var}(R)$ from formula $\textsf{Var}(R) = {\bf E}[R^2] - ({\bf E}[R])^2$,
$$
\begin{aligned}
\textsf{Var}(R) &= {\bf E}[R^2] - ({\bf E}[R])^2\\
&=np(1-p) + (n^2-3n+2)p^2(1-p)^2 - n^2p^2(1-p)^2\\
&= np(1-p) - (3n-2)p^2(1-p)^2.
\end{aligned}
$$
Assuming that $p = 3/4, n = 10$, we obtain
$$
\mathsf{Var}(R) = 57/64 = 0.890625
$$
