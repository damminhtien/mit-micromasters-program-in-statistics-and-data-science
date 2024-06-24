# Lecture 16. Goodness of Fit Tests Continued: Kolmogorov-Smirnov test, Kolmogorov-Lilliefors test, QQ-Plots

There are 6 topics and 2 exercises.

## 1. CDF and Empirical CDF

Let $X$ be a random variable with distribution $\mathbf{P}$. Recall the CDF of $\mathbf{P}$ is given by the function
$$
\begin{aligned}
F: \mathbb {R} &\rightarrow [0,1]\\
t &\mapsto \mathbf{P}(X \leq t)
\end{aligned}
$$
Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X$​. The **empirical cumulative distribution function**, also called the **empirical CDF**, is the random function
$$
\begin{aligned}
F_n : \R &\rightarrow [0,1]\\
t &\mapsto \frac{1}{n} \sum _{i = 1}^ n \mathbf{1}(X_ i \leq t).
\end{aligned}
$$
The empirical CDF depends on $n$​ and the observed data $X_i, \ i=1,...,n$​.

Note that for any $t$​​​​ (in the domain of $F_n$​​​​ i.e. $t \in \R$​​​​), the empirical CDF $F_n(t)$​​​​ is **random**, since $F_n(t)$​​​ is a function of the random variables $X_1, ..., X_n$​​​. For any $t$​​​ (in the domain of $F_n$​​​), the true CDF $F(t) = P(X \leq t)$​​​ is **deterministic**.

#### Pointwise and Uniform Convergence of Functions

A sequence of functions $g_n(x)$ **converges pointwise** to a function $g(x)$ if for each $x$, $\displaystyle \lim _{n\to \infty } g_ n(x)=g(x).$

**Example:** In the region $x> 1$, $g_n(x) = {1\over x^n}$ converges pointwise to $g(x)= 0$. For any fixed $x>1$ ${1\over x^n} \xrightarrow[n \rightarrow \infty]{} 0$.

A sequence of functions $g_n(x)$​ **converges uniformly** to a function $g(x)$​ if $\lim _{n\to \infty } \sup _{x\in \mathbb {R}} |g_ n(x)-g(x)|=0.\, $​ That is, for every $M > 0$​, there exists an $n_M$​ such that $\sup _ x |g_ n(x) - g(x)| < M$​ for all $n \geq n_M$.

**Example:** In the region $x > 2$, $g_n(x) = {1\over x^n}$ converges uniformly to $g(x)=0$, since $\sup _{x>2} g_ n(x)=\sup _{x>2} \frac{1}{x^ n}= \frac{1}{2^ n}\xrightarrow [n\to \infty ]{} 0$​.

**Example of pointwise but not uniform convergence:** (The 1st one does not imply the 2nd one)

The sequence of functions $\, g_ n(x)=\frac{1}{x^ n}\,$ does not converge uniformly to $g(x) =0$ in the region $x > 1$, since $\sup _{x>1} g_ n(x)=\sup _{x>1} \frac{1}{x^ n}= 1,\,$ which does not converge to 0 as $n \rightarrow \infty$.

#### Consistency

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X$ be i.i.d. random variables with CDF $F(t)$ and empirical CDF $F_n(t)$.

By the LLN, for all $t \in \R$​,
$$
F_n(t) \xrightarrow[n \rightarrow \infty]{a.s.} F(t)
$$
**Glivenko-Cantelli Theorem: (aka. The Fundamental Theorem of Statistics)** [LLN uniformly]
$$
\sup _ {t \in \R} |F_ n(x) - F(x)| \xrightarrow[n \rightarrow \infty]{a.s.} 0.
$$
(Note that the 1st convergence does not imply the 2nd convergence.)

This is a **stronger** result than the one happens **uniformly** over $t$​​. This means for all large enough $n$​​ and for any $\delta > 0$​​, the difference $|F_n(t) - F(t)|$​​ is bounded above by $\delta$​​ for all $t$​​. Almost sure convergence means that for all $\delta > 0$​​ and $\epsilon > 0$​​, there exists $N = N(\delta, \epsilon)$​​ such that the event $\sup _{t} |F_ n(t) - F(t)| < \delta$​​ occurs with probability at least $1-\epsilon$​​ for all $n > N$​​. In other words, with probability approaching $1$​​, the function $F_n$​​ is a close $L_{\infty}$​​ (the sup-norm) approximation of $F$.

## 2. Asymptotic Normality of the Empirical CDF

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}$​ for some distribution $\mathbb{\mathbf{P}}$​, and let $F$​ denote its CDF. Let $F_n$​ denote the empirical CDF. 

By the **CLT**, it holds for all $t\in \R$​,
$$
\sqrt{n} (F_n(t)-F(t)) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0, F(t)(1-F(t))).
$$
Note that when $t\rightarrow 0$​​​, the variance goes to $0$​​, and when $t \rightarrow \infty$​​​, the variance goes to $1$.

**Donsker's Theorem: (aka. Uniform Central Limit Theorem)** [CLT uniformly]

A stronger result than the one held by the CLT.

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}$ for some distribution $\mathbb{\mathbf{P}}$, and let $F$ denote its CDF. Let $F_n$ denote the empirical CDF. 

Donsker's Theorem states that if $F$ is continuous, then
$$
\sqrt{n} \sup_{t \in \R} |F_n(t)-F(t)| \xrightarrow[n \rightarrow \infty]{(d)} \sup_{0 \leq t \leq 1} |\mathbb{B}(t)|
$$
where $\mathbb{B}$​ is a random curve called **Brownian bridge** on $[0,1]$​.

**Remark:** $\sup _{0 \leq x \leq 1} |\mathbb {B}(x)|$​ is a **pivotal distribution**, i.e. it does not depend on the unknown distribution of the data, and hence we can look up its quantiles in tables or by using software. This will be important as we develop goodness of fit tests for continuous distributions.

## 3. Goodness of Fit Test of Continuous Distributions: Kolmogorov-Smirnov Test

#### Goodness of fit test of continuous distributions:

Let $X_1, ..., X_n$ be i.i.d. real random variables with unknown CDF $F$ and let $F^0$ be a continuous CDF.

Consider the two hypotheses:
$$
H_0 : F=F^0 \quad v.s. \quad H_1 : F \neq F^0
$$
Let $F_n$ be the empirical CDF of the sample $X_1, ..., X_n$.

If $F=F^0$, then $F_n(t) \approx F^0(t)$, for all $t \in [0,1]$.

#### Kolmogorov-Smirnov Test

Let $T_n = \sqrt{n} \sup_{t \in \R} |F_n(t)-F^0(t)|$​.

By Donsker's theorem, if $H_0$​​​ is true, then $T_n \xrightarrow[n\rightarrow \infty]{(d)} Z$​, where​​ $Z$​ has a known distribution (supremum of a | Brownian bridge |)

**KS test with asymptotic level $\alpha$:**
$$
\delta_\alpha^{KS} = \mathbb{1}\{T_n > q_\alpha\}
$$
where $q_\alpha$​ is the $(1-\alpha)$​-quantile of $Z$​ (obtained in tables).

P-value of KS test: $\mathbf{P}[Z > T_n | T_n]$​, which is the probability that the supremum of the | Brownian bridge| is larger than the data that we observed for $T_n$.

**Remark:** This is an **asymptotic** test and this test will have asymptotic level alpha. We used an asymptotic statement which is **Donsker's theorem**.

#### Computational Issues

In practice, how to compute $T_n$?

$F^0$​​ is non decreasing, $F_n$​​ is piecewise constant, with jumps at $t_i = X_i,\  i = 1, ..., n$​​.

Let $X_{(1)} \leq X_{(2)} \leq ... \leq X_{(n)}$​​​​​ be the reordered sample, so $X_{(i)}$​​​ is the **order statistic**.

The expression for **Kolmogorov-Smirnov test statistic** $T_n$​ reduces to the following practical formula:
$$
\begin{aligned}
T_n &= \sup_{t \in \R}\sqrt{n}\ |F_n(t) - F^0(t)|\\
&=\sqrt{n} \max_{1 \leq i \leq n} \Big\{\max\left(\left|F^0(X_{(i)}) - F_n(X_{(i)})\right|, \left|F^0(X_{(i)})-F_n(X_{(i)})\right|\right)\Big\}\\
&=\sqrt{n} \max_{i = 1,...,n} \left\{\max\left(\left|{i-1 \over n} - F^0(X_{(i)})\right|, \left|{i \over n} - F^0(X_{(i)})\right|\right)\right\}
\end{aligned}
$$
The **Kolmogorov-Smirnov test** is
$$
\displaystyle  \displaystyle \mathbf{1}(T_ n>q_\alpha )\qquad \text {where } q_\alpha =q_\alpha (\sup _{t \in [0,1]}\left| \mathbb {B}(t) \right|).
$$
Here, $q_\alpha =q_\alpha (\sup _{t \in [0,1]}\left| \mathbb {B}(t) \right|)\,$​ is the $(1-\alpha)$​-quantile of the supremum $\sup _{t \in [0,1]}\left| \mathbb {B}(t) \right|$​ of the Brownian bridge as in Donsker's Theorem.

**Note:**

* Under $H_0$​, $T_n$​ converges to the **supremum** of a Brownian bridge. A Brownian motion is a **random curve** while its supremum over the interval $[0,1]$​ is a **random variable**. 

* Under $H_0$​, $T_n$​ converges to a **pivotal distribution**, since the limiting distribution is **independent** of the distribution of the $X_1, ..., X_n$​ (as long as $F$​ is continuous). Recall we have
  $$
  \sqrt{n}\sup _{t \in \mathbb {R}} |F_ n(t) - F(t)| \xrightarrow [n \to \infty ]{(d)} \sup _{x \in [0,1]} |\mathbb {B}(x)|.
  $$

* Under $H_0$, $T_n$ converges to a distribution whose quantiles we can either look up in tables or estimate very well using simulations. In general, **pivotal distributions can be understood by consulting a table of quantiles**. Using computational tools, Brownian motions (and their suprema) can be simulated, so this is another approach to computing the quantiles.

**Example:**

![images_u4s6_KSstat](../assets/images/images_u4s6_KSstat.svg)

An example of the empirical cdf $\, F_ n(x_{(1)},x_{(2)},x_{(3)},x_{(4)})\,$​​ for a specific data set $x_{(1)},x_{(2)},x_{(3)},x_{(4)}$​​ of sample size $4$​​, and the cdf $F_X(x)$​​ under the null hypothesis. We see that because $F^0(t)$​​ is increasing, and $F_n(t)$​​ is piecewise constant, $\bigg| F_ n(t) - F^0(t) \bigg|$​​ can only possibly achieve its maximum at $t=x_{(i)}$​.

#### Pivotal distribution

$T_n$​​​ is called a **pivotal statistic**: If $H_0$​​​ is true, the distribution of $T_n$​​​ does not depend on the distribution of the $X_i$​​​'s and it is easy to reproduce it in simulations. 

Indeed, let $U_i=F^0(X_i), i=1, ... n$​ and let $G_n$ be the empirical CDF of $U_1, ..., U_n$.

If $H_0$​​​​​​​​ is true, then $U_1, ..., U_n \stackrel{iid}{\sim} \text{Unif}([0,1])$​​ and the test statistic is calculated by letting $x = F(t),\ F = F^0$:
$$
\begin{aligned}
T_n 
&= \sup\limits_{0 \leq x \leq 1} \sqrt{n} \ |F_n(F^{-1}(x)) -x|\\
&= \sup\limits_{0 \leq x \leq 1} \sqrt{n} \ \left|{1\over n}\sum^n_{i=1} \mathbb{1}(X_i \leq F^{-1}(x)) -x\right|\\
&= \sup\limits_{0 \leq x \leq 1} \sqrt{n} \ \left|{1\over n}\sum^n_{i=1} \mathbb{1}(F(X_i) \leq x) -x\right|\\
&= \sup\limits_{0 \leq x \leq 1} \sqrt{n} \ \left|{1\over n}\sum^n_{i=1} \mathbb{1}(U_i \leq x) -x\right|\\
&= \sup\limits_{0 \leq x \leq 1} \sqrt{n} \ |G_n(x) -x|

\end{aligned}
$$
**Note:** 

* Pivotal means it's a universal distribution. We can compute and reproduce in simulation, and it's always the same.

* Let's generate data $X$​​​ with a given CDF $F$​​​. We start with $U \sim \text{Unif}\ ([0,1])$​​​ and apply $X = F^{-1}(U)$.
  $$
  \begin{aligned}
  \mathbf{P}(X \leq t) &= \mathbf{P}(F^{-1}(U) \leq t)\\
  &= \mathbf{P}(U \leq F(t))\\
  &= F(t)\\
  \end{aligned}
  $$
  The distribution of $F(X)$ is​ uniform $F(X) \sim \text{Unif}\ ([0,1])$.

> #### Exercise 89
>
> Let $X$ be a random variable with invertible CDF $F_X$. Define another random variable $Y = F_X(X)$. Find the CDF $F_Y$ of $Y$.
>
> 1. For $t < 0$
> 2. For $t \geq 0$
> 3. For $ 0 \leq t < 1$
>
> **Solution:**
>
> Given $\, Y=F_ X(X)\,$ where $F_X$ is a CDF, $Y$ only takes values between $0$ and $1$. This means that $F_Y(t) = 0$ for all $t \leq 0$ and $F_Y(t) = 1$ for all $t > 1$.
>
> In the region $0 \leq t < 1$
> $$
> F_ Y(t)\, =\, P(F_ X(X)\leq t)\, =\, P(X\leq F^{-1}(t))\, =\, F(F^{-1}(t))\, =\,  t.
> $$
> We see that the CDF of $Y$ is that of a uniform distribution with support in $[0,1]$, i.e. $Y \sim \text{Unif}(0,1)$.
>
> **Remark 1:** Note that $Y=F_ X(X)\sim \textsf{Unif}(0,1)$ regardless of the distribution of $X$ as long as $F_X$ is invertible.
>
> **Remark 2:** Inverting the result gives $X\sim F_ X^{-1}(Y)$​​​​​ where $Y\sim \textsf{Unif}(0,1)$​​​​. This is useful for simulating data from a given distribution with CDF​ $F_X$​​. Start by sampling from $\text{Unif}(0,1)$​​, and apply $F_X^{-1}$​​ to the sample. The resulting sample will be from a distribution with CDF $F_X$.

#### Quantiles of the pivotal distribution and p-values

For same large integer $M$:

* Simulate $M$​​ i.i.d. copies $T_n^1,...,T_n^M$​​ of $T_n$​​​ (capable since we can just pretend that $F^0 \sim \text{Unif}([0,1])$​​);
* Estimate the $(1-\alpha)$​-quantile $q_\alpha^{(n)}$​ of $T_n$​ by taking the sample $(1-\alpha)$​-quantile $\hat{q}_\alpha^{(n,M)}$​ of $T_n^1,...,T_n^M$​.

Test with approximate level $\alpha$:
$$
\delta_\alpha = \mathbb{1}\{T_n > \hat{q}_\alpha^{(n,M)}\}
$$
Approximate p-value of this test
$$
\text{p-value} \approx {\# \{j = 1, ..., M: T_n^j > T_n\}\over M}
$$

> #### Exercise 90
>
> Let $X_1, ..., X_n$​ be i.i.d samples with CDF $F$​, and let $F^0$​ denote the CDF of $\text{Unif}\ (0,1)$​. Recall that
> $$
> F^0(t) = t \cdot \, \mathbf{1}(t \in [0,1]) + 1 \cdot \mathbf{1}(t > 1) .
> $$
> We want to use goodness of fit testing to determine whether or not $X_1, \ldots , X_ n \stackrel{iid}{\sim } \textsf{Unif}(0,1)$. To do so, we will test between the hypotheses
> $$
> H_0: F(t) = F^0\\
> H_1: F(t) \neq F^0
> $$
> To make computation of the test statistic easier, let us first reorder the samples from smallest to largest, so that
> $$
> X_{(1)} \leq X_{(2)} \leq \ldots \leq X_{(n)}
> $$
> is the reordered sample. In this set-up, the Kolmogorov-Smirnov test statistic is given by the formula
> $$
> T_ n = \sqrt{n} \max _{i = 1, \ldots , n} \left\{  \max \left(\bigg| \frac{i -1}{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|, \bigg| \frac{i }{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|\right) \right\} .
> $$
> You observe the data set $\mathbf{x}$​​ consisting of $5$​ samples:
> $$
> \mathbf{x}= 0.8, 0.7, 0.4, 0.7, 0.2
> $$
>
> 1. Using the formula above, what is the value of $T_n$​​​ for this data set?
>
> 2. You will use the KS test
>    $$
>    \psi _5 = \mathbf{1}( T_5 > C ).
>    $$
>    What value of $C$​​​​ should be chosen so that $\psi_5$​​​ has (non-asymptotic) level $5\%$​​​​​? Would you reject or fail to reject the null hypothesis on the above data set? Note that the number $x$​ in the $n$-th row of the column labeled by the level $\alpha$ table in the slide "K-S table" is such that
>    $$
>    P_ n^{KS}\left(\frac{T_ n}{\sqrt{n}} > x \right) = \alpha .
>    $$
>
> **Solution:**
>
> 1. First we reorder the given data set to get $0.2, 0.4, 0.7, 0.7, 0.8.$​
>
>    Now $X_{(i)}$​​ is defined to be the $i$​​-th element in the list above. To compute $T_n$​​ for $n=5$​ and plug in the above reordered data set, we compute the maximum of the following list of numbers
>    $$
>     \max (|0 - 0.2|,|0.2 - 0.2|) = 0.2\\
>     \max (|0.2 - 0.4|,|0.4 - 0.4|) = 0.2\\
>     \max (|0.4 - 0.7|, |0.6 - 0.7|) = 0.3\\
>     \max (|0.6 - 0.7|,|0.8 - 0.7|) = 0.1\\
>     \max (|0.8 - 0.8|,|1 - 0.8|) ) = 0.2
>    $$
>    which comes out to be $0.3$. Therefore, $T_5 = \sqrt{5} \cdot 0.3 \approx 0.6708$.
>
> 2. The number in the $5$'S row and column labeled by $0.05$ is $0.56328$. Therefore, we need to set $C = \sqrt{5} \cdot 0.56328 \approx 1.2595.$ 
>
>    Since $0.6708 < 1.2596$, the test $\psi_5$ will fail to reject the null hypothesis that $X_1, \ldots , X_5 \stackrel{iid}{\sim } U([0,1])$ on the given data.

## 4. Other Goodness of Fit Tests

We want to measure the distance between two functions: $F_n(t)$​​​ and $F(t)$​​​. There are other ways, leading to other tests. What's important is that we find a distance such that the distance between $F_n$​​ and $F$​​ has a distribution that's **pivotal**.

* Kolmogorov-Smirnov: [$L_\infty$ distance]
  $$
  d(F_n, F) = \sup_{t \in \R} |F_n(t) -F(t)|
  $$

* Cramer-Von Mises: [$L_2$​ distance]
  $$
  d^2(F_n,F) = \int_{\R}[F_n(t) - F(t)]^2 dt
  $$
  or
  $$
  d^2(F_n,F) = \int_{\R}[F_n(t) - F(t)]^2 dF(t) := \mathbb{E}_{X \sim F}[|F_n(t) - F(t)|^2]
  $$

* Anderson-Darling:
  $$
  d^2(F_n,F) = \int_\R {[F_n(t) - F(t)]^2\over F(t)(1-F(t))} dt
  $$
  or
  $$
  d^2(F_n,F) = \int_\R {[F_n(t) - F(t)]^2\over F(t)(1-F(t))}dF(t)
  $$

## 5. Kolmogorov-Lilliefors Test

#### Motivation: Goodness of Fit Testing for a Gaussian Distribution

Let $X_1, \ldots , X_ n$ be iid random variables with continuous CDF $F$. Let $\{  \mathcal{N}(\mu , \sigma ^2) \} _{\mu \in \mathbb {R}, \sigma ^2 > 0}$ denote the family of all **Gaussian** distribution. We want to test whether or not $F \in \{  \mathcal{N}(\mu , \sigma ^2) \} _{\mu \in \mathbb {R}, \sigma ^2 > 0}$.

Let $\Phi _{\mu , \sigma ^2}$ denote the CDF of $\mathcal{N}(\mu , \sigma ^2)$. We formulate the null and alternative hypotheses
$$
  H_0 :  F = \Phi _{\mu , \sigma ^2} \,  \text {for some} \,  \mu \in \mathbb {R}, \sigma ^2 > 0\\
  H_1 :  F \neq \Phi _{\mu , \sigma ^2} \,  \text {for some} \,  \mu \in \mathbb {R}, \sigma ^2 > 0
$$
Motivated by the Kolmogorov-Smirnov test, you define a test-statistic using the sample mean $\hat{\mu} = \overline{X}_n$​ and sample variance $\hat{\sigma}^2 = S_n^2$​​​ :
$$
\widetilde{T}_ n = \sup _{t \in \mathbb {R}} \sqrt{n} |F_ n(t) - \Phi _{\hat{\mu }, \hat{\sigma ^2}}|.
$$
Assume that the null hypothesis is true. Is it true that
$$
\widetilde{T}_ n \xrightarrow [n \to \infty ]{(d)} \sup _{x \in [0,1]} |\mathbb {B}(x)|
$$
where $\mathbb {B}(x)$​​​ is NOT a **Brownian bridge**.

Moreover, the statistic $\widetilde{T}_ n$ converges in distribution as $n \rightarrow \infty$. The quantiles of $\widetilde{T}_ n$ can be found in tables, and the test based on $\widetilde{T}_ n$ is known as the **Kolmogorov-Lilliefors test**.

**Explanation of not being a Brownian bridge:**

It is true that for any fixed $\mu , \sigma ^2$ that
$$
T_ n = \sup _{t \in \mathbb {R}}\sqrt{n} |F_ n(t) - \Phi _{\mu , \sigma ^2}| \xrightarrow [n \to \infty ]{(d)} \sup _{x \in [0,1]} |\mathbb {B}(x)|.
$$
This result follows by Donsker's theorem as the Gaussian CDF is continuous over the real time.

But if we plug in **estimators** for $\mu$​ and $\sigma^2$​ (and not their true values), then this convergence result no longer holds.

#### Kolmogorov-Lilliefors Test

The quantiles for the test statistic
$$
\widetilde{T}_ n = \sup _{t \in \mathbb {R}} \sqrt{n} |F_ n(t) - \Phi _{\hat{\mu }, \hat{\sigma ^2}}(t)|.
$$
do not depend on true unknown parameters, so the test statistic is **pivotal** (so one can compute its quantiles using a table or computational software). 

This is the **Kolmogorov-Lilliefors Test**.
$$
\psi _ n = \mathbf{1}( T_ n > q_\eta )
$$
where $q_\eta$ denotes the $1-\eta$ quantile of the distribution $T_n$​.

#### Kolmogorov-Smirnov vs. Kolmogorov-Lilliefors Test

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathcal{N}(\mu , \sigma ^2)$, the empirical distribution $F_ n(t) = \frac{1}{n} \sum _{i =1}^ n \mathbf{1}(X_ i \leq t)$, and the CDF of the Gaussian distribution $\mathcal{N}(\mu, \sigma^2)$ which is denoted by $\Phi _{\mu , \sigma ^2}$.

The test statistic in the Kolmogorov-Smirnov test:
$$
T_ n = \sqrt{n}\sup _{t \in \mathbb {R}} |F_ n(t) - \Phi _{\mu , \sigma ^2}|
$$
The test statistic in the Kolmogorov-Lilliefors test:
$$
\widetilde{T}_ n = \sqrt{n}\sup _{t \in \mathbb {R}} |F_ n(t) - \Phi _{\widehat{\mu }, \widehat{\sigma }^2}|
$$
**Remark 1:** Note that $T_n$ and $\widetilde{T}_ n $ will have different distribution for all $n$, since we plug in the actual values of parameters for $T_n$, while we plug in estimators $\hat{\mu}$ and $\hat{\sigma}^2$ for the true parameter.

**Remark 2:** The **Kolmogorov-Smirnov** test was designed to test **if the data has a specific distribution**; it is not useful for deciding whether or not the true distribution $\mathbf{P}$​ lies in a given family of distributions, in which scenario we should apply **Kolmogorov-Lilliefors** test. 

**Remark 3:** The **student's T test** is only valid if we know that the data has a Gaussian distribution. If the **Kolmogorov-Lilliefors** test fail to reject the null hypothesis that the data has a Gaussian distribution, then we know our data is likely to be Gaussian, then the student's T test can be applied to test if the true mean of our data is $\mu=0$. In practice, many of the methods for statistical inference, such as the student's T test, rely on the assumption the data is Gaussian. Hence, before performing such a test, we need to evaluate whether or not the data is Gaussian.

Let $q_\eta$ denote the $1-\eta$ quantile of $T_n$ (i.e. $P(T_n \geq q_\eta) = \eta$) and let $q_\eta'$ denote the $1-\eta$ quantile of $\widetilde{T}_ n$ (i.e., $P(\widetilde{T}_ n \geq q_\eta ') = \eta$), we expect
$$
q_\eta > q_\eta '
$$
**Explanation:**

For $\widetilde{T}_ n$, the mean and variance of the empirical distribution are $\widehat{\mu}$ and $\widehat{\sigma}^2$, respectively. Hence, it is natural to expect $\mathcal{N}( \widehat{\mu }, \widehat{\sigma }^2)$ to be a good approximation to $F_n(t)$, at least amongst all Gaussian distributions.

For $T_n$, the mean and variance of the empirical distribution do NOT match the mean and variance of $\mathcal{N}(\mu , \sigma ^2)$. This again leads reason to believe that the CDF $\Phi _{\widehat{\mu }, \widehat{\sigma }^2}$ will approximate the empirical distribution $F_n(t)$ better than $\Phi _{\mu , \sigma ^2}$.

Therefore, on average, we expect $\widetilde{T}_ n$ to be smaller than $T_n$. 

Hence, the CDF of $\widetilde{T}_ n$ will be more shifted to the left, and the CDF of $T_n$ will be more shifted to the right. This means that the quantiles of $T_n$ will be larger than the quantiles of $\widetilde{T}_ n$. That is, we are more likely to fail to reject the null hypothesis when applying **Kolmogorov-Lilliefors** test.

## 6. Quantile-Quantile (QQ) Plots

Provide a visual way to perform GoF tests. Not formal test but quick and easy check to see if a distribution is plausible.

**Main idea**: we want to check visually if the plot of $F_n$ is close to that of $F$ or equivalently if the plot of $F_n^{-1}$ is close to that of $F^{-1}$.

More convenient to check if the points
$$
(F^{-1}({1\over n}), F^{-1}_n({1\over n})),(F^{-1}({2\over n}), F^{-1}_n({2\over n})),...,(F^{-1}({n-1\over n}), F^{-1}_n({n-1\over n}))
$$
are near the line $y=x$.

$F_n$ is not technically invertible but we define
$$
F_n^{-1}(i/n) = X_{(i)}
$$
the $i$​​​​​th largest observation. 

The **quantile-quantile (QQ) plot** is constructed in the following way from a data set:

1. Reorder the samples to be in increasing order. Denote the reordered sample by $X_{(1)}, X_{(2)}, \ldots , X_{(n)}$.

2. Plot the points
   $$
   \bigg(F^{-1}\left(\frac{1}{n}\right), X_{(1)}\bigg), \,  \,  \bigg(F^{-1}\left(\frac{2}{n}\right), X_{(2)}\bigg), \,  \,  \ldots , \,  \,  \bigg(F^{-1}\left(\frac{i}{n}\right), X_{(i)}\bigg), \,  \,  \ldots , \,  \,  \bigg(F^{-1}\left(\frac{n-1}{n}\right), X_{(n-1)}\bigg).
   $$
   Note that above we omit plotting the $n$​th point because $F^{-1}(n/n) = F^{-1}(1) = \infty$​. 

The x-values above $(\Phi = F)$.
$$
\Phi ^{-1}(1/n), \Phi ^{-1}(2/n), \ldots , \Phi ^{-1}(i/n), \ldots , \Phi ^{-1}((n-1)/n)
$$
are referred to as the **theoretical quantiles**, and the y-values above given by the reordered sample
$$
X_{(1)}, X_{(2)}, \ldots , X_{(n)}
$$
are referred to as the **empirical quantiles**.

#### The Four Patterns of Quantiles-Quantile (QQ) Plots

A distribution $\mathbf{P}$​​​​ has a **heavier right tail** if
$$
P(X \geq t) \geq P(Y \geq t) \quad \text {for} \,  \,  t> 0 \,  \,  \text {sufficiently large},
$$
where $X \sim P$​​​ and $Y \sim Q$​​​. (Otherwise, $\mathbf{P}$ is said to have a lighter right tail than $Q$.)

Similarly, $\mathbf{P}$​​ has a **heavier left tail** if
$$
P(X \leq -t) \geq P(Y \leq -t) \quad \text {for} \,  \,  t> 0 \,  \,  \text {sufficiently large},
$$
where $X \sim P$​ and $Y \sim Q$​. (Otherwise, $\mathbf{P}$​ is said to have a lighter left tail than $Q$​.)

Four patterns of QQ plots:

* Heavier tails
* Lighter tails
* Right skewed
* Left skewed

![How to interpret a QQ plot - Cross Validated](../assets/images/qqplot4p.png)

