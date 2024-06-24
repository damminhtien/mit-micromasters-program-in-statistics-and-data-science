# Lecture 6. Variance; Conditioning on an event; Multiple r.v.'s

* Variance and its properties

  * Definition of variance: $\rm{var}(X) = E[(X-\mu)^2]$

  * Properties

    * $\rm{var}(aX+b) = a^2\rm{var}(X)$
    * $\rm{var}(X) = E[X^2] - (E[X])^2$

  * Variance of the Bernoulli

    * $\rm{var}(X) = \sum_x(x-E[X])^2p_X(x) = (1-p)^2p + (0-p)^2(1-p) = p(1-p)$
    * $\rm{var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)$

  * Variance of the uniform PMFs

    $\begin{aligned}&\rm{var}(X) \\&= E[X^2] - (E[X])^2 \\&= \frac{1}{n+1} (0^2 + 1^2 + 2^2 + ... + n^2) - ({n \over 2})^2 \\&= \frac{1}{n+1} ({1 \over 6} n(n+1)(2n+1)) - ({n \over 2})^2 \\&= {1 \over 12} n (n+2) \quad \text{ where }n = b-a \end{aligned}$

* Conditioning a r.v. on an event
  
    * Conditional PMF, mean, variance
      
        | Non-conditional              | Conditional                          |
        | ---------------------------- | ------------------------------------ |
        | $p_X(x) = \mathbf{P}(X=x)$   | $p_{X\|A}(x) = \mathbf{P}(X=x\|A)$   |
        | $p_X(x) = \mathbf{P}(X=x)$   | $p_{X\|A}(x) = \mathbf{P}(X=x\|A)$   |
      | $E[X] = \sum_xx p_X(x)$      | $E[X\|A] = \sum_x x p_{X\|A}(x)$     |
      | $E[g(X)] = \sum_xg(x)p_X(x)$ | $E[g(X)\|A] = \sum_xg(x)p_{X\|A}(x)$ |
      
    * Total expectation theorem
    
    $E[X] = \mathbf{P}(A_1)E[X|A_1] + ... +\mathbf{P}(A_n)E[X|A_n] $
  
* Geometric PMF

  * **Memorylessness**: 

    * number of remaining coin tosses, conditioned on Tails in the first toss, is Geometric, with parameter $p$. 

      $p_X(k) = (1-p)^{k-1}p, \quad k=1,2,3...$

    * Conditioned on $X > 1$, $X - 1$ is geometric with parameter $p$.

      $p_{X-1|X>1}(k) = p_X(k) = p_{X-n|X>n}(k) $

    * Conditioned on $X > n$, $X - n$ is geometric with parameter $p$.

      $p_{X-n|X>n}(k) = p_X(k) $

  * Mean of Geometric PMF

    $E[X] = \sum^\infty_{k=1}k p_X(k) = \sum^{\infty}_{k=1} k(1-p)^{k-1}p = \frac{1}{p}$
    
  * Variance of Geometric PMF

    * Given $X > 1, X-1$ has the same geometric PMF (unconditional PMF of $X$)

    * Given $X>1$, conditional PMF of $X$: same as unconditional PMF of $X+1$

      $E[X|X>1] = 1 + E[X]$

    $\begin{aligned}E[X^2] &= P(X=1)E[X^2|X=1] + P(X >1)E[X^2|X>1]\\ &= p \cdot 1 + (1-p) \cdot (E[X^2] + 2 E[X]+1)\\&={2-p \over  p^2}\end{aligned}$

    $\mathsf{Var}(X) = E[X^2] - (E[X])^2 = {2-p \over p^2} - {1 \over p^2} = {1-p \over p^2}$

* Multiple random variables

  * Joint and marginal PMFs

    | Joint and marginal PMFs                                      | Properties                                                   |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | $p_{X,Y}(x,y) = \mathbf{P}(X=x \text{ and } Y = y)$          | $\sum_x\sum_y p_{X,Y}(x,y) = 1\\p_X(x) = \sum_yp_{X,Y}(x,y)\\p_Y(y) = \sum_xp_{X,Y}(x,y)$ |
    | $p_{X,Y,Z}(x,y,z) = \mathbf{P}(X=x \text{ and } Y = y \text{ and } Z = z)$ | $\sum_x\sum_y\sum_z p_{X,Y,Z}(x,y,z) = 1\\p_X(x) = \sum_y\sum_zp_{X,Y,Z}(x,y,z)\\p_{X,Y}(x,y) = \sum_zp_{X,Y,Z}(x,y,z)$ |

  * Expected value rule

    $E[g(X,Y)] = \sum_x \sum_y g(x,y) p_{X,Y}(x,y)$

  * Linearity of expectations

    $E[aX+b] = aE[X] + b\\ E[X+Y] = E[X] + E[Y] \\E[X_1 + ... + X_n] = E[X_1] + ... + E[X_n]$

* The mean of the binomial PMF

  * $X$: binomial with parameters $n,p$
  
    $E[X] = \sum^n_{k=0} k {n \choose k} p_x(k)= \sum^n_{k=0} k {n \choose k}p^k(1-p)^{n-k}$
  
    $E[X] = np$

---

There are 4 selected exercises and 3 solved problems.

## Exercise 1 Total expectation calculation

We have two coins, A and B. For each toss of coin A, we obtain Heads with probability $1/2$; for each toss of coin B, we obtain Heads with probability $1/3$. All tosses of the same coin are independent. We select a coin at random, where the probability of selecting coin A is $1/4$, and then toss it until Heads is obtained for the first time. What's the expected number of tosses until the first Heads?

**Answer**: $11/4$

**Solution**: 

Let $T$ be the number of tosses until the first Heads. Once a coin is selected, the conditional distribution of $T$ is **geometric**, with a mean of $1/p$, where $p$ is the probability of Heads for the selected coin. Let $C_A$ and $C_B$ denote the events that coin A or B, respectively, is selected.
$$
{\bf E}[T]=\mathbf{P}(C_ A) {\bf E}[T\mid C_ A]+\mathbf{P}(C_ B){\bf E}[T\mid C_ B]=\frac{1}{4}\cdot 2 +\frac{3}{4}\cdot 3=\frac{11}{4}.
$$

## Exercise 2 Memorylessness of the geometric

Let $X$ be a geometric random variable, and assume that $\rm{Var}(X)=5$. What is the conditional variance $\textsf{Var}(X-4\mid X>4)$.

**Answer**: $\textsf{Var}(X-4\mid X>4) = 5$

**Solution**: The conditional distribution of $X−4$ given $X>4$ is the same geometric PMF that describes the distribution of $X$. Hence, $\textsf{Var}(X-4\mid X>4)=\textsf{Var}(X)=5$.

## Exercise 3 Joint PMF calculation

The random variable $V$ takes values in the set $\{0,1\}$ and the random variable $W$ takes values in the set $\{0,1,2\}$. Their joint PMF is of the form.
$$
p_{V,W}(v,w)=c\cdot (v+w),
$$
where $c$ is some constant, for $v$ and $w$ in their respective ranges, and is zero everywhere else.

Find the value $c$ and $p_V(1)$.

**Answer**: $c = 1/9; p_V(1)  =2/3$

**Solution**: 

The sum of the entries of the PMF is
$$
p_{V,W}(v,w) = c\cdot (0+0)+c\cdot (0+1)+c\cdot (0+2)+c\cdot (1+0)+\ldots = 9c
$$
Since this sum must be equal to 1, we have $c = 1/9$.
$$
p_ V(1)=\sum _{w=0}^2 p_{V,W}(1,w)= p_{V,W}(1,0)+p_{V,W}(1,1)+p_{V,W}(1,2) =\frac{1}{9}(1+2+3)=\frac{6}{9}.
$$

## Exercise 4 Expected value rule

Let $X$ and $Y$ be discrete random variables. For each one of the formulas below, state whether it is true or false.

a) ${\bf E}[X^2]=\sum _ x x^2 p_ X(x)$

b) ${\bf E}[X^2]=\sum _ x\sum _ y x^2 p_{X,Y}(x,y)$

Since ${\bf E}[g(X,Y)]=\sum _ x \sum _ y g(x,y) p_{X,Y}(x,y),$ for the function $g(x,y)=x^2$.

c) ${\bf E}[X^2]=\sum _ z z p_{X^2}(z)$

Since ${\bf E}[Z]=\sum _ z z p_ Z(z)$ where $Z$ is the random variable $X^2$

## Problem 1 Coupon collector problem

A particular professor is known for his arbitrary grading policies. Each paper receives a grade from the set $\{A,A−,B+,B,B−,C+\}$, with equal probability, independently of other papers. How many papers do you expect to hand in before you receive each possible grade at least once?

**Answer**: 

Let $K = 6, Y_i = $ the number of papers till $i$'th new grade. $X_i = Y_{i+1} - Y_i$. so $Y_6 = \sum^5_{i=0}X_i$.
$$
X_i = \mathsf{Geo}(\frac{6-i}{6})\\
\mathbb{E}(X_i) = \frac{6-i}{6}\\
\mathbb{E}(\sum^5_{i=0} X_i) = \sum^5_{i=0} \mathbb{E}[X_i] = 6 \cdot \sum^5_{i=1} \frac{1}{6-i} = 6 \cdot \sum^6_{i=1} \frac{1}{i} = 14.7\\
\mathbb{E}[Y_k] = k \sum^{k-1}_{i=1}\frac{1}{i} \approx k \ln k
$$
$\mathbb{E}[Y_k] \approx k \ln k$ is known as the scaling law for the coupon collector's problem that it takes about $k \ln k$ trials until we collect all $k$ coupons.

## Problem 2 Conditioning example 

Suppose that $X$ and $Y$ are independent, identically distributed, geometric random variables with parameter $p$. Show that
$$
\mathbf{P}(X=i \mid X+Y=n)=\frac{1}{n-1}, \qquad \text{for }i=1,2,\ldots ,n-1.
$$
**Answer**:

Consider repeatedly and independently tossing a coin with probability of heads $p$. We can interpret $\mathbf{P}(X=i | X + Y =n)$ as the probability that we obtained heads for the first time on the $i$th toss given that we obtained heads for the second time on the $n$th toss. (Specifically, the condition part states that it take $n$ trials to get the first two heads. The main part means that it takes $i$ trials to get the first head.)

We can argue that given that the second heads occurred on the $n$th toss, the first heads is equally likely to have come up at any toss between $1$ and $n-1$.
$$
\begin{aligned}
\mathbf{P}(X =i | X + Y = n) &= \frac{\mathbf{P}(X = i, X+Y = n)}{\mathbf{P}(X + Y = n)} \\
&= \frac{\mathbf{P}(X = i, Y =n-i)}{\mathbf{P}(X + Y = n)} \\
&= \frac{\mathbf{P}(X = i) \mathbf{P}(Y = n-i)}{\mathbf{P}(X + Y = n)}\\
\end{aligned}
$$
where the last step follows from the assumption that $X$ and $Y$ are independent. Also,
$$
\mathbf{P}(X = i) = p (1-p)^{i-1}, \quad \text{for } i\geq 1,
$$
and
$$
\mathbf{P}(Y = n-i) = p(1-p)^{n-i-1},\quad \text{for }n-i \geq 1.
$$
It follows that
$$
\mathbf{P}(X=i) \mathbf{P}(Y = n-i) = \begin{cases}p^2(1-p)^{n-2}, & \text{if }i = 1, ..., n-1\\0, & \text{otherwise} \end{cases}
$$

$$
\begin{aligned}
\mathbf{P}(X + Y =n ) &= \sum^{n-1}_{k=1} \mathbf{P}(X =k) \mathbf{P}(X+Y =n | X=k)\\
&= \sum^{n-1}_{k=1} \mathbf{P}(X =k) \mathbf{P}(X+Y = n)\\
&= \sum^{n-1}_{k=1} \mathbf{P}(X =k) \mathbf{P}(Y = n-k)\\
&= \sum^{n-1}_{k=1}(1-p)^{k-1} p (1-p)^{n-k-1}p\\
&= \sum^{n-1}_{k=1} (1-p)^{n-2} p^2
\end{aligned}
$$

To put everything together
$$
\begin{aligned}
\mathbf{P}(X =i | X + Y = n)&= \frac{\mathbf{P}(X = i) \mathbf{P}(Y = n-i)}{\mathbf{P}(X + Y = n)}\\
&=\frac{(1-p)^{n-2}p^2}{(n-1)(1-p)^{n-2}p^2}\\
&=\frac{1}{n-1}
\end{aligned}
$$
Note that for $i \in \{1, ..., n-1\}$, this expression does not depend on $i$. Additionally, $\mathbf{P}(X + Y =n )$ does not depend on $i$ either. Therefore, for any $i \in \{1, ..., n-1\}, \mathbf{P}(X = i| X + Y =n)$ has the same value. Hence 
$$
\mathbf{P}(X=i| X+Y=n)= \frac{1}{n-1}, \quad i=1,...,n-1
$$

## Problem 3

Compute $\mathbf{E}(X)$ for the following random variable $X$:
$$
 X=\, \text {Number of tosses until all 10 numbers are seen (including the last toss) by tossing a fair 10-sided die}.
$$
To answer this, we will use induction and follow the steps below:

Let $\mathbf{E}(i)$ be the expected number of additional tosses until all $10$ numbers are seen (including the last toss) **given** $i$ **distinct numbers have already been seen**.

1. Find $\mathbf{E}(10)$

2. Write down a relation between $\mathbf{E}(i)$ and $\mathbf{E}(i+1)$, for $i = 0,1,...,9$, as 
   $$
   {\bf E}(i)={\bf E}(i+1)+ f(i)
   $$

3. Find $\mathbf{E}(X)$

**Answer**: 

1) $\mathbf{E}(10)=0$

2) The induction step is as follows, for $i=1,2,...,9$:
$$
\begin{aligned}
{\bf E}(i) &=({\bf E}(i)+1)\times \frac{i}{10} + ({\bf E}(i+1)+1) \times \left( 1-\frac{i}{10} \right)\\
\Longleftrightarrow {\bf E}(i) &= {\bf E}(i+1) + {10 \over 10-i}
\end{aligned}
$$
3) Using $\mathbf{E}(10)=0$, we have
$$
\frac{10}{10}+\frac{10}{9}+\ldots +\frac{10}{2}+\frac{10}{1}+0\approx 29.28968.
$$
**Explanation of Q2:**

The solution is making use of *conditional expectations*. For convenience, let $Y_i$ denote the **number of tosses required to get all 10 numbers given that we have already seen $i$ distinct numbers**, $i=0,1,...,9$. So, we are asked to find $\mathbf{E}[Y_i]=\mathbf{E}(i).$

Now, let $A_{i+1}$ denote **the event of getting a distinct number on the next toss, given that we have already seen $i$ distinct numbers**. Then the probability of this event is $\mathbf{P}(A_{i+1})=\frac{10-i}{10}=1-\frac{i}{10}$, and the probability of its complement (NOT seeing a distinct number on the next toss, given that we have already seen $i$ distinct numbers), is $\mathbf{P}(A_{i+1}^\mathsf{c})=\frac{i}{10}$.

Recall that by the conditional expectation rule, 
$$
\begin{aligned}\mathbf{E}[Y_i]&=\mathbf{P}(A_{i+1})\mathbf{E}[Y_i|A_{i+1}]+\mathbf{P}(A_{i+1}^\mathsf{c})\mathbf{E}[Y_i|A_{i+1}^\mathsf{c}]\end{aligned}.
$$
Substituting the probabilities above, we have 
$$
\begin{aligned}\mathbf{E}[Y_i]&=\left(1-\frac{i}{10}\right)\mathbf{E}[Y_i|A_{i+1}]+\left(\frac{i}{10}\right)\mathbf{E}[Y_i|A_{i+1}^\mathsf{c}].\end{aligned}
$$
Notice that if $A_{i+1}$ happens, we change to the state of having seen $(i+1)$ distinct numbers. Hence, **the expected number of tosses until we see all $10$ numbers conditioned on $A_{i+1}$ and having seen $i$ distinct numbers before that**, which is given by $\mathbf{E}[Y_i|A_{i+1}]$ can be written as $\mathbf{E}[Y_i|A_{i+1}] = 1 + \mathbf{E}[Y_{i+1}]$, where $1$ indicates the toss that led to even $A_{i+1}$. Similarly, if we do not see a distinct number on the next toss when we had seen $i$ distinct numbers already, i.e., if $A^c_{i+1}$ happens, our count of distinct numbers seen so far stays at $i$ itself, and hence $\begin{aligned}\mathbf{E}[Y_i|A_{i+1}^\mathsf{c}]&=1+\mathbf{E}[Y_i].\end{aligned}$

Substituting the values of the two expectations into our conditional expectation formula, we get 
$$
\begin{aligned}\mathbf{E}[Y_i]&=\left(1-\frac{i}{10}\right)\left(1+\mathbf{E}[Y_{i+1}]\right)+\left(\frac{i}{10}\right)\left(1+\mathbf{E}[Y_i]\right),\end{aligned}
$$
which is the recursion given in the answer.
