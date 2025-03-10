# Lecture 17. Linear least mean squares (LLMS) estimation

* LLMS

  * Minimize $\mathbb{E}[(\widehat{\Theta} - \Theta)^2]$​​.

  * Estimators $\widehat{\Theta}=g(X) \rightarrow \widehat{\Theta}_{LMS} = \mathbb{E}[\Theta |X]$​​.

  * Consider estimators of $\Theta$​​ of the form $\widehat{\Theta} =  aX+b$​​​.

  * Minimize $\mathbb{E}[(\Theta-aX-b)^2]$​​, w.r.t. $a,b$​​​.

  * If $\mathbb{E}[\Theta|X]$​ is linear in $X$​, then $\widehat{\Theta}_{LMS} = \widehat{\Theta}_{LLMS}$​.

* Solution to LLMS: 

  * $\widehat{\Theta}_L = \mathbb{E}[\Theta] + {\text{Cov}(\Theta, X) \over \text{var}(X) } (X - \mathbb{E}[X]) = \mathbb{E}[\Theta] + \rho {\sigma_{\Theta} \over \sigma_X}(X-\mathbb{E}[X])$.

    where $a = {\text{Cov}(\Theta, X) \over \text{var}(X) } =\rho {\sigma_{\Theta} \over \sigma_X}$​​, and $\rho={\text{Cov}(\Theta,X)\over \sigma_\Theta \sigma_X }$​​​.

  * $\mathbb{E}[(\widehat{\Theta}_L - \Theta)^2]=(1-p^2)\text{var}(\Theta)$​.​

* LLMS with multiple observations

  * Unknown $\Theta$; observations $X=(X_1, ..., X_n)$

  * Consider estimators of the form: $\widehat{\Theta} = a_1X_1 + ... + a_nX_n+b$

  * Find best choices of $a_1, ..., a_n,b$

    Minimize: $\mathbb{E}[(a_1X_1 + ... + a_nX_n+b-\Theta)^2]$​​​

  * If $\mathbb{E}[\Theta|X]$ is linear in $X$, then $\widehat{\Theta}_{LMS} = \widehat{\Theta}_{LLMS}$.

  * Solve linear system in $b$ and the $a_i$.

  * Only means, variances, covariances matter.

  * If multiple unknown $\Theta_j$, apply to each one, separately.

* The simplest LLMS example with multiple observations

  * Given $X_1 =\Theta  +W_1, ..., X_n =\Theta  +W_n$​​​​, $\Theta \sim x_0, \sigma_0^2,\ W_i \sim 0, \sigma_i^2$​​. 

  * Suppose $\Theta, W_1, ..., W_n$ are independent normal
    $$
    \hat{\theta}_{LMS} = \mathbb{E}[\Theta| X=x] = {\sum\limits^n_{i=0} {x_i\over \sigma_i^2} \over \sum\limits^n_{i=0} {1 \over \sigma_i^2}}\\
    \hat{\theta}_{LMS} = \mathbb{E}[\Theta| X]  = {{x_0\over \sigma_0^2} + \sum\limits^n_{i=1}{X_i \over \sigma_i^2} \over \sum\limits^n_{i=0} {1\over \sigma_i^2}} = \widehat{\Theta}_{LLMS}
    $$

* The representation of the data matters in LLMS

  Estimation based on $X$ vs. $X^3$.

  * LMS: $\mathbb{E}[\Theta |X]$ is the same as $\mathbb{E}[\Theta | X^3]$
  * LLMS is different: estimator $\widehat{\Theta} = aX + b$​ vs. $\widehat{\Theta}=aX^3 + b$​. (Since $\text{cov}(\Theta, X^3), \text{var}(X^3)$​​).
  * Can also consider:
    * $\widehat{\Theta} = a_1 X + a_2 X^2 + a_3X^3 + b$
    * $\widehat{\Theta} = a_1 X + a_2 e^X + a_3 \log X + b$​​

* Comparing LMS and LLMS:

  * It's true that LMS estimator is guaranteed to take values only in the interval $[0,1]$​. But LLMS estimator is NOT guaranteed to take values only in the interval $[0,1]$​.

    The conditional expectation ${\bf E}[\Theta \mid X=x]$ is a weighted average of the values of $\Theta$, weighted according to the posterior PDF. A weighted average of values in $[0,1]$ must lie in $[0,1]$.

    On the other hand, there is no such guarantee for the LLMS estimator. Consider the example where $X=\Theta + W$, where $W$ can take any real value. Then, the term $aX$ can take any real value, and can therefore fall outside the range $[0,1]$.

  * The MAP estimator for the problem of estimating the bias of a coin is $X/n$​​, which is different from the LLMS estimator $(X+1)/(n+2)$​​. LLMS has a smaller MSE.

    The LLMS estimator coincides with the LMS estimator and therefore achieves the smallest possible mean squared error.
    
  * The relationship is linear in $X$ when the RVs are normal and have the same mean. The LMS and LLMS estimators would be the same no matter what distribution we have, as long as the RVs have the same mean.
  
* (Supplement) The Beta formula: For any nonnegative integers $\alpha$ and $\beta$, we have
  $$
  \int _0^1 \theta ^\alpha (1-\theta )^{\beta }\,  d\theta =\frac{\alpha !\,  \beta !}{(\alpha +\beta +1)!},
  $$

There are 2 selected exercises and 2 solved problems.

---

## Exercise 1 LLMS drill

Suppose that $\Theta$​​​​​ and $W$​​​​​ are independent, both with variance $1$​​​​​, and that $X=\Theta + W$​​​​​. Furthermore, $\mathbb{E}[\Theta] =1$​​​​​ and $\mathbb{E}[W]=2$​​​​​. What is the LLMS estimator $\widehat{\Theta}$​​​​​?

Hint: Recall the formula $\textsf{Cov}(X+Y,Z)=\textsf{Cov}(X,Z)+\textsf{Cov}(Y,Z)$​.

**Solution:**

We have ${\bf E}[X] = {\bf E}[\Theta ] + {\bf E}[W] = 3$ and $\textsf{Var}(X)=\textsf{Var}(\Theta )+\textsf{Var}(W)=2$. Also,
$$
\textsf{Cov}(X,\Theta )=\textsf{Cov}(\Theta ,\Theta )+\textsf{Cov}(\Theta ,W)=\textsf{Var}(\Theta )+0=1.
$$
Therefore, the LLMS estimator is
$$
\widehat\Theta = 1+\frac{1}{2}(X-3)=\frac{1}{2}X-\frac{1}{2}.
$$

## Exercise 2 LLMS with multiple observations

Suppose that $\Theta, X_1, $ and $X_2$ have zero means. Furthermore,
$$
\textsf{Var}(X_1)=\textsf{Var}(X_2)=\textsf{Var}(\Theta )=4,
$$
and
$$
\textsf{Cov}(\Theta ,X_1)=\textsf{Cov}(\Theta ,X_2)=\textsf{Cov}(X_1,X_2)=1.
$$
The LLMS estimator of $\Theta$ based on $X_1$ and $X_2$ is of the form $\widehat\Theta = a_1X_1 + a_2X_2 + b$. Find the coefficients $a_1, a_2$, and $b$.

**Solution:**

By the same argument as in the case of a single observation, we will have $b={\bf E}[\Theta -a_1X_1-a_2X_2]=0$. Using the variance and covariance information we are given, the expression we want to minimize is
$$
{\bf E}\left[(a_1X_1+a_2X_2-\Theta )^2\right]=4a_1^2+4a_2^2+4+2a_1a_2 -2a_1-2a_2.
$$
Because of symmetry, we see that the optimal solution will satisfy $a_1 = a_2 = a$​​, so the expression is of the form $8a^2+4+2a^2-4a$​​. By setting the derivative to zero, we find that $20a=4$, or $a=1/5$.

## Problem 1 LLMS estimation

Let $N$ be a random variable with mean ${\bf E}[N]=m$, and $\textsf{Var}(N)=v$; let $A_1,A_2,\dots$ be a sequence of i.i.d. random variables, all independent of $N$, with mean $1$ and variance $1$; let $B_1, B_2, ...$ be another sequence of i.i.d. random variables, all independent of $N$ and of $A_1, A_2, ...$, also with mean $1$ and variance $1$. Let $A=\sum _{i=1}^ N A_i $ and $B=\sum _{i=1}^ N B_ i$.

1. Find the expectations ${\bf E}[AB]$ and ${\bf E}[NA]$ using the law of iterated expectations.
2. Let $\hat{N}=c_1 A + c_2$ be the LLMS estimator of $N$ given $A$. Find $c_1$ and $c_2$ in terms of $m$ and $v$.

**Solution:**

1. Compute ${\bf E}[AB]$:
   $$
   \begin{aligned}
   {\bf E}[AB] &= {\bf E}[(A_1+\dots +A_ N)(B_1+\dots +B_ N)]\\
   &= {\bf E}[{\bf E}[(A_1+\dots +A_ N)(B_1+\dots +B_ N)\mid N]]\\
   &= {\bf E}[{\bf E}[(A_1+\dots +A_ N)\mid N]{\bf E}[(B_1+\dots +B_ N)\mid N]]\\
   &= {\bf E}[N{\bf E}[A_1]N{\bf E}[B_1]]\\
   &= {\bf E}[N^2]\\
   &= \textsf{Var}(N)+({\bf E}[N])^2\\
   &= m^2 + v
   \end{aligned}
   $$
   Similarly,
   $$
   \begin{aligned}
   {\bf E}[NA] &= {\bf E}[{\bf E}[N(A_1+\dots +A_ N)\mid N]]\\
   &= {\bf E}[N{\bf E}[A_1+\dots +A_ N\mid N]]\\
   &= {\bf E}[N(N{\bf E}[A_1])]\\
   &= {\bf E}[N^2]\\
   &= m^2 + v
   \end{aligned}
   $$

2. $A$ is the sum of a random number, $N$, of iid random variables $A_1, ..., A_N$. Therefore,
   $$
   {\bf E}[A]={\bf E}[{\bf E}[A\mid N]] = {\bf E}[{\bf E}[A_1]N]=m,
   $$
   and
   $$
   \textsf{Var}(A)=\textsf{Var}(A_ i){\bf E}[N] + ({\bf E}[A_ i])^2 \textsf{Var}(N) = m + v.
   $$
   Similarly, ${\bf E}[B]=m$, and $\textsf{Var}(B)=m + v$. Furthermore,
   $$
   \begin{aligned}
   \text{cov}(N,A) &= {\bf E}[NA]-{\bf E}[N]{\bf E}[A]\\
   &= (m^2 + v) -m^2\\
   &= v.
   \end{aligned}
   $$
   Finally, 
   $$
   \begin{aligned}
   \hat{N} &= {\bf E}[N]+\frac{{\rm cov}(N,A)}{\textsf{Var}(A)}(A-{\bf E}[A])\\
   &=  m + \frac{v}{m+v}(A-m)\\
   &= \frac{m^2}{m+v}+\frac{v}{m+v}A.
   \end{aligned}
   $$

## Problem 2 Estimating the parameter of a uniform r.v.

The random variable $X$ is uniformly distributed over the interval $[\theta, 2\theta]$. The parameter $\theta$ is unknown and is modeled as the value of a continuous random variable $\Theta$, uniformly distributed between zero and one.

1. Given an observation $x$ of $X$, find the posterior distribution of $\Theta$. Express your answers below in terms of $\theta$  and $x$. 
2. Find the MAP estimate of $\Theta$ based on the observation $X=x$ and assuming that $0 \leq x \leq 1$. 

3. Find the LMS estimate of $\Theta$ based on the observation $X=x$ and assuming that $0 \leq x \leq 1$.
4. Find the linear LMS estimate $\hat{\theta }_{\text {LLMS}}$ of $\Theta$ based on the observation $X=x$. 

**Solution:**

1. The prior PDF of $\Theta$ is
   $$
   f_{\Theta }(\theta ) = \begin{cases}  1, &  \text{if } 0\leq \theta \leq 1, \\ 0, &  \text{otherwise,} \end{cases}
   $$
   and the conditional PDF of the observation $X$ is
   $$
   f_{X\mid \Theta }(x\mid \theta ) = \begin{cases}  1/\theta , &  \text{if } \theta \leq x\leq 2\theta , \\ 0, &  \text{otherwise.} \end{cases}
   $$
   Using Bayes' rule, we find that for any $x \in [0,1]$ and for $\theta \in [x/2,x]$, the posterior PDF is
   $$
   \begin{aligned}
   f_{\Theta \mid X}(\theta \mid x) & = \frac{f_{\Theta }(\theta )f_{X\mid \Theta }(x\mid \theta )}{\displaystyle \int _{x/2}^{x}f_{\Theta }(\tilde{\theta })f_{X\mid \Theta }(x\mid \tilde{\theta }) d \tilde{\theta }}\\
   &= \frac{1/\theta }{\displaystyle \int _{x/2}^{x}\frac{1}{\tilde{\theta }}d \tilde{\theta }}\\
   &= \frac{1}{\theta \cdot (\ln (x) - \ln (x/2))}\\
   &= \frac{1}{\theta \cdot \ln (2)}.
   \end{aligned}
   $$

2. For $x\in [0,1]$ and $x/2 \leq \theta \leq x$, the posterior PDF is
   $$
   f_{\Theta \mid X}(\theta \mid x) = \frac{1}{\theta \cdot \ln (2)},
   $$
   which is decreasing in $\theta$ over the range $[x/2, x]$ of possible values of $\Theta$. Thus, the MAP estimate for this case is equal to $x/2$.

3. The LMS estimate is the conditional expectation estimate. For $x \in [0,1]$,
   $$
   {\bf E}[\Theta \mid X = x] = \int _{x/2}^{x}\theta \frac{1}{\theta \cdot \ln (2)}d\theta = \frac{x}{2\cdot \ln (2)}.
   $$

4. The LLMS estimate is of the form
   $$
   \hat{\theta }_{LLMS}(x) = {\bf E}[\Theta ] + \frac{{\rm cov}(\Theta , X)}{\textsf{Var}(X)} (x - {\bf E}[X]).
   $$
   Here, 
   $$
   \begin{aligned}
   {\bf E}[\Theta ] &= 1/2,\\
   {\bf E}[\Theta ] &= {\bf E}[{\bf E}[X\mid \Theta ]]\\
   &= {\bf E}\left[\frac{3}{2} \Theta \right]\\
   &= {\bf E}\left[\int_\Theta^{2\Theta}xf_{X|\Theta}(X|\Theta) dx \right]\\
   &= {\bf E}\left[\int_\Theta^{2\Theta}{x\over \Theta} dx \right]\\
   &= {\bf E}\left  .\left [{x^2\over 2\Theta} \right|_\Theta^{2\Theta} \right]\\
   &= {3\over 4}\\
   {\bf E}[X^2] & = {\bf E}[{\bf E}[X^2\mid \Theta ]]\\
   &= {\bf E}\left[\int_\Theta^{2\Theta}x^2f_{X|\Theta}(X|\Theta) dx \right]\\
   &= {\bf E}\left[\int_\Theta^{2\Theta}{x^2\over \Theta} dx \right]\\
   &= {\bf E}\left  .\left [{x^3\over 3\Theta} \right|_\Theta^{2\Theta} \right]\\
   & = {\bf E}\left[\frac{7}{3} \Theta ^2\right]\\
   &= {7 \over 9}\\
   \end{aligned}
   $$
   Hence,
   $$
   \begin{aligned}
   \textsf{Var}(X) & = {\bf E}[X^2] - ({\bf E}[X])^2\\
   & = \frac{31}{144},\\
   {\bf E}[\Theta X] & = {\bf E}[{\bf E}[X \Theta \mid \Theta ]]\\
   & = {\bf E}\left[\frac{3}{2} \Theta ^2\right]\\
   &= {1\over 2},\\
   {\rm cov}(\Theta , X) & = {\bf E}[\Theta X] - {\bf E}[\Theta ] {\bf E}[X]\\
   & = \frac{1}{2} - \frac{1}{2} \cdot \frac{3}{4}\\
   &= {1\over 8}
   \end{aligned}
   $$
   Finally, we have
   $$
   \begin{aligned}
   \hat{\Theta }_{LLMS} & = {\bf E}[\Theta ] + \frac{{\rm cov}(\Theta , X)}{\textsf{Var}(X)} (x - {\bf E}[X])\\ 
   &= \frac{1}{2} + \frac{1/8}{31/144} \left(x-\frac{3}{4} \right)\\
   &= \frac{2}{31} + \frac{18}{31}x.
   \end{aligned}
   $$
   
