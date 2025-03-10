# Lecture 4. Parametric Estimation and Confidence Intervals

There are 6 topics and 5 exercises.

## 1. Statistics, Estimators, Consistency, and Asymptotic Normality

* **Statistic**: Any *measurable* function of the sample, e.g., $\bar{X}_n, \max_iX_i, X_1 + \log(1+|X_n|)$, sample variance ,etc.
  * *Measurable*: if you can compute it exactly once given data, it is measurable. You may have some issues with things that are implicitly defined (like "$\inf$" or "$\sup$").

    E.g. we do not have a closed form solution for    $\inf_{f \in \mathcal{F}}{1 \over n} \sum^n_{i=1}(Y_i - f(X_i))^2$.

* **Estimator of** $\theta$: Any statistic whose expression does not depend on $\theta$. (since we want to be able to compute it as an estimator once we get data).
  * The question we are interested in is how good an estimator is.
  * The goal is to have an estimator that will converge to the true unknown parameter $\theta$.

* An estimator $\hat{\theta}_n$ of $\theta$ is weakly (resp. strongly) **consistent** if

$$
\hat{\theta}_n \xrightarrow[n \rightarrow \infty]{\mathbf{P}(\text{resp. a.s.})} \theta \qquad (\text{w.r.s}. \mathbb{P}_\theta)
$$

* An estimator $\hat{\theta}_n$ of $\theta$ is **asymptotically normal** if 
  $$
  \sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow[n \rightarrow \infty]{ (d)} \mathcal{N}(0, \sigma^2)
  $$

  * The quantity $\sigma^2$ if then called **asymptotic variance **of $\hat{\theta}_n$.
  * The limit of asymptotic variance is 0: $\mathsf{var}(\hat{\theta}_n) \xrightarrow[n \rightarrow \infty]{} 0$. (think about $\bar{X}_n= \sum_i X_i/n$ )

> #### Exercise 22
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Ber(p)}$. Let $\overline{X}_ n$ be the estimator given by $\frac{1}{n} \sum _{i = 1}^ n X_ i$. What is the smallest constant $c$ such that
> $$
> n^ c \left( \overline{X}_ n - p \right) = n^ c \left( \frac{1}{n} \sum _{i = 1}^ n X_ i - p \right)
> $$
> does NOT converge to $0$ in probability as $n \rightarrow \infty$?
>
> **Answer**: 1/2
>
> **Solution**: 
>
> Let $\sigma = \sqrt{p(1-p)}$ denote the common standard deviation of $X_1, ..., X_n$. By the CLT, 
> $$
> \frac{\sqrt{n}}{\sigma }\left(\overline{X}_ n - p\right) = \frac{\sqrt{n}}{\sigma }\left(\frac{1}{n} \sum _{i = 1}^ n X_ i - p\right) \to N(0,1)
> $$
> where the convergence is in distribution. As a result, we see that for $c < 1/2$,
> $$
> n^ c \left( \overline{X}_ n - p \right) = \frac{\sigma }{n^{1/2 -c}} \frac{\sqrt{n}}{\sigma }\left(\overline{X}_ n - p\right) \approx \frac{\sigma }{n^{1/2 -c}} N(0,1) \to 0
> $$
> in probability as $n \rightarrow \infty$. Hence, $c = 1/2$ is the smallest possible value of $c$ such that
> $$
> n^ c \left( \overline{X}_ n - p \right) = n^ c \left( \frac{1}{n} \sum _{i = 1}^ n X_ i - p \right)
> $$
> does NOT converge to $0$ in probability as $n \rightarrow \infty$.
>
> **Remark**: As defined in the third video in this section, this implies that the estimator $\overline{X}_ n$ is $\sqrt{n}$-**consistent**. This means that the **estimator $\overline{X}_ n$ converges to the true parameter at a relatively fast rate**, so this gives us something stronger than just consistency.

## 2. Bias of Estimators; Jensen's Inequality

* **Bias** of an estimator $\hat{\theta}_n$ of $\theta$:
  $$
  \mathsf{bias}(\hat{\theta}_n) = \mathbb{E}[\hat{\theta}_n] - \theta
  $$
  If $\mathsf{bias}(\hat{\theta}_n)=0$, $\hat{\theta}$ is **unbiased**. 

> #### Exercise 23
>
> Assume that $X_1, ...,X_n \stackrel{iid}{\sim} \mathsf{Ber}(p)$ and consider the following estimators for $p$. Compute the biases.
>
> **Answer**: 
>
> 1) $\hat{p}_n = \bar{X}_n: \mathsf{Bias}(\hat{p}_n) = 0$.
>
> 2) $\hat{p}_n = X_1: \mathsf{Bias}(\hat{p}_n) = 0$.
>
> 3) $\hat{p}_n = {X_1+ X_2 \over 2}: \mathsf{Bias}(\hat{p}_n) = 0$.
>
> 4) $\hat{p}_n = \sqrt{\mathbf{1}(X_1 = 1, X_2 = 1)}: \mathsf{Bias}(\hat{p}_n) = p^2 - p$. 
>
> **Solution**: 
>
> The bias is computed by $\mathsf{Bias}(\hat{p}_n) = \mathbb{E}[\hat{p}_n] - p$.
>
> For (4), note that **the square root of expectation is not necessarily the expectation of square root**, or say, **the function of expectation is not necessary the expectation of the function** (See Jenson's Inequality). Even though the square root is taken, it is still a Bernoulli distribution with probability $p^2$, i.e., 
> $$
> \mathbb{E}[\hat{p}_n] = \mathbb{E}\left[\sqrt{\mathbf{1}(X_1 = 1, X_2 = 1)}\right] = p^2
> $$

> #### Exercise 24
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathcal{U}([a, a + 1])$ where $a$ is an unknown parameter. Let $\overline{X}_ n = \displaystyle \frac{1}{n} \sum _{i = 1}^ n X_ i$ denote the sample mean. In terms of $a$, what is $\mathbb{E}[\overline{X}_n]$? What is the bias of $\overline{X}_n$ w.r.t $a$?
>
> **Answer**: $\mathbb{E}[\overline{X}_n] = {2a+1 \over 2}$; $\mathsf{bias}(\overline{X}_n) = {1\over 2}$
>
> **Solution**:
>
> By linearity of expectation,
> $$
> \mathbb E[\overline{X}_ n] = \frac{1}{n} \sum _{i = 1}^ n \mathbb E[X_ i] = \mathbb E[X_1] = a + \frac{1}{2}.
> $$
> Or equivalently,
> $$
> \mathbb E[\overline{X}_ n] =\int^{a+1}_a 1 \cdot x \mathsf{d}x = {1\over 2}((a+1)^2 - a^2) = {2a+1 \over 2} = a + {1 \over 2}
> $$
> The bias is 
> $$
> \mathsf{bias}(\overline{X}_n) = \mathbb{E}[\overline{X}_n] - a = {1\over 2}
> $$
> Note that this implies that $\overline{X}_ n - \frac{1}{2}$ is an unbiased estimator.

* **Convex**: A function $g: \R \rightarrow \R$ is convex if for all pairs of real numbers $x_1 < x_2$
  $$
  g(tx_1+(1-t)x_2)\leq tg(x_1)+(1-t)g(x_2)\qquad \text {for all } \, 0\leq t\leq 1.
  $$
  Geometrically, the graph of convex $g$ is shown below 

  ![images_u3s2_convex](../assets/images/images_u3s2_convex.svg)

  Note that for $x_1 = 0, x_2 = 1$, the inequality above can be reinterpreted as follows. Let $X \sim \mathsf{Ber}(1-t)$ for some parameter $0 \leq t \leq 1$, then the left and right hand sides of inequality above can be rewritten respectively as:
  $$
  g\left(t(0)+(1-t)(1)\right) = g\left(1-t\right)\, =\, g\left(\mathbb E[X]\right)\\
  t g\left(0\right)+(1-t)g\left(1\right) = \mathbb E\left[g\left(X\right)\right]
  $$
  and hence the inequality defining convexity of $g$ implies
  $$
  g(\mathbb E[X])\leq \mathbb E[g(X)]\qquad (\text {for any Bernoulli random variable} X.)
  $$

* **Jensen's inequality**: for any random variable $X$, and any convex function $g$,
  $$
  g(\mathbb E[X])\leq \mathbb E[g(X)].
  $$
  Jensen's Inequality is also true for random vectors and convex functions on $\R^n$.

**Comments**: **Unbiasedness** is a desirable property and may be one of the first properties we want to check about the estimator even before consistency, but when we enforce that an estimator is unbiased, we may not have the best possible estimator because there are estimators that are unbiased but have a lot of **variability**.

## 3. Variance of Estimators

The variance of estimator $X$ is 
$$
\mathsf{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$

> #### Exercise 23 (continued)
>
> Assume that $X_1, ...,X_n \stackrel{iid}{\sim} \mathsf{Ber}(p)$ and consider the following estimators for $p$. Compute the variances.
>
> **Answer**: 
>
> 1) $\hat{p}_n = \bar{X}_n: \mathsf{Var}(\hat{p}_n) = {p(1-p) \over n}$.
>
> 2) $\hat{p}_n = X_1: \mathsf{Var}(\hat{p}_n) = {p(1-p)}$.
>
> 3) $\hat{p}_n = {X_1+ X_2 \over 2}: \mathsf{Var}(\hat{p}_n) = {p(1-p) \over 2}$.
>
> 4) $\hat{p}_n = \sqrt{\mathbf{1}(X_1 = 1, X_2 = 1)}: \mathsf{Var}(\hat{p}_n) = p^2 (1-p^2)$. 
>
> **Solution**: 
>
> The variance of Bernoulli random variable $X \sim \mathsf{Ber}(p)$ is $\mathsf{Var}[X] = p(1-p)$.
>
> The variance of the sum is the sum of variance ( **Variance is addictive**), so
> $$
> \text {Var}(\overline{X}_ n) = \frac{1}{n^2} \sum _{i = 1}^ n \text {Var}(X_ i) = \frac{1}{n} \text {Var}(X_1)
> $$
> For (1) as an example, the variance is 
> $$
> \mathsf{Var}\left[ {1\over n} \sum_i X_i\right] = {1\over n^2}\mathsf{Var}\left[X_1 + X_2 + ... + X_n \right] = {1\over n^2}\mathsf{Var}[X_1] + \mathsf{Var}[X_2] + ... +\mathsf{Var} [X_n] = {np(1-p) \over n^2} = {p(1-p) \over n}
> $$

> #### Exercise 24 (continued)
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathcal{U}([a, a + 1])$ where $a$ is an unknown parameter. Let $\overline{X}_ n = \displaystyle \frac{1}{n} \sum _{i = 1}^ n X_ i$ denote the sample mean. In terms of $a$, what is $\mathsf{Var}[\overline{X}_n]$?
>
> **Answer**:  $\mathsf{Var}[\overline{X}_n] = {1 \over 12n}$
>
> **Solution**: 
> $$
> \text {Var}(X_1) = \mathbb E[X_1^2] - (\mathbb E[X_1])^2 = \int _{a}^{a +1} 1 \cdot x^2 \,  dx - \left( a + \frac{1}{2} \right)^2 = a^2 + a + 1/3 - a^2 - a - 1/4 = 1/12.\\
> \text {Var}(\overline{X}_ n) = \frac{1}{n} \text {Var}(X_1) = \frac{1}{12n}.
> $$

## 4. Quadratic Risk of Estimators

We want estimators to have low bias and low variance. Bias and variance are combined through **quadratic risk**. 

The **Risk** (or **quadratic risk**) of an estimator $\hat{\theta}_n\in \R$ is 
$$
R(\hat{\theta}_n) = \mathbb{E}\left[ (\hat{\theta}_n - \theta)^2\right]
$$
Low quadratic risk means that both bias and variance are small. $\rm{Quadratic~risk} =\rm{variance} + \rm{bias}^2$.

**Proof**:
$$
\begin{aligned}
R(\hat{\theta}_n) &= \mathbb{E}\left[ (\hat{\theta}_n - \theta)^2\right]\\
&= \mathbb{E}\left[ (\hat{\theta}_n  - \mathbb{E}[\hat{\theta}_n] + \mathbb{E}[\hat{\theta}_n] - \theta)^2\right]\\
&= \mathbb{E}\left[ (\hat{\theta}_n  - \mathbb{E}[\hat{\theta}_n])^2\right] + \mathbb{E}\left[(\mathbb{E} [\hat{\theta}_n] - \theta)^2\right] + 2 \mathbb{E}\left[(\hat{\theta}_n  - \mathbb{E}[\hat{\theta}_n])(\mathbb{E} [\hat{\theta}_n] - \theta)\right]\\
&= \mathbb{E}\left[ (\hat{\theta}_n  - \mathbb{E}[\hat{\theta}_n])^2\right] + \mathbb{E}\left[(\mathbb{E} [\hat{\theta}_n] - \theta)^2\right] \quad \text{Since }\mathbb{E}\left[(\hat{\theta}_n  - \mathbb{E}[\hat{\theta}_n])\right] = 0\\
&= \mathbb{E}\left[ (\hat{\theta}_n  - \mathbb{E}[\hat{\theta}_n])^2\right] + (\mathbb{E} [\hat{\theta}_n] - \theta)^2
\end{aligned}
$$
The first quantity is $\rm{variance}$, the second quantity is $\rm{Bias}^2$.

> #### Exercise 24 (continued)
>
> What is the quadratic risk of the estimator $\overline{X}_ n - \frac{1}{2}$?
>
> **Answer**: $1 \over 12n$
>
> **Solution**: 
>
> Since estimator $\overline{X}_ n - \frac{1}{2}$ is unbiased, and $\text {quadratic risk} = \text {variance} + \text {bias}^2.$
> $$
> \text {Var}(\overline{X}_ n) = \text {Var}(\overline{X}_ n - \frac{1}{2}) = \frac{1}{12 n}
> $$
> which is the quadratic risk.
>
> **Remark**: When the sample size is larger, the quadratic risk is lower.

## 5. Exercise: Strengths and Weaknesses of Estimators

You observe samples $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Ber} (\theta )$ where $\theta \in (0,1)$ is an unknown parameter. Suppose that $n$ is much larger than $1$ so we have access to many samples from the specified distribution. Consider three candidate estimators for $\theta$.

* $\overline{X}_ n = \frac{1}{n} \sum _{i = 1}^ n X_ i$
* $0.5$
* $X_1$

Let's consider potential strengths and weaknesses of these estimators.

In this particular section, “**efficiently computable**" refers to the existence of an explicit formula. More precisely, here we say that an estimator $\hat{\theta}_n$ is efficiently computable if there's a formula that takes as input $X_1,\ldots ,X_ n$ whose output is $\hat{\theta}_n$ (Not all estimators are efficiently computable).

1. Which of the following is a potential <u>disadvantage</u> of using $\hat{θ}_n=.5$ as an estimator for $θ$? (Choose all that apply.)

   a. Unless $\theta = 0.5$, this estimator is biased.

   b. Unless $\theta = 0.5$, this estimator is not consistent.

   c. This estimator does not use any of the samples.

   d. This estimator is efficiently computable.

2. Which of the following is a potential <u>disadvantage</u> of using $\hat{θ}_n=X_1$ as an estimator for $θ$? (Choose all that apply.)

   a. This estimator is unbiased.

   b. This estimator is not consistent.

   c. This estimator uses only information given by only one sample, even though we have access to many samples.

   d. The quadratic risk of this estimator does not tend to $0$ as the sample size $n \rightarrow \infty$.

3. Which of the following are potential <u>advantages</u> of using $\hat{\theta}_n = \overline{X}_n$ as an estimator for $θ$? (Choose all that apply.)

   a. This estimator is unbiased.

   b. This estimator is consistent.

   c. This estimator is efficiently computable.

   d. The quadratic risk of this estimator tends to $0$ as the sample size $n \rightarrow \infty$.

> **Answer**:
>
> 1) abc
>
> - **Biased estimators inherently introduce errors in parameter estimation**. Hence, having non-zero bias is a potential disadvantage of an estimator.
> - If the estimator does not converge to the true parameter as the sample size $n$ grows very large, this is also a potential disadvantage. **Estimators that are not consistent have inherently limited accuracy in approximating the true parameter, regardless of how many samples are taken**. 
> - We haven't used any information given to us so we can't expect to learn anything new about the true parameter with this estimator.
> - The given estimator is indeed efficiently computable, and this is in general an *advantage* of certain estimators. In contrast, there are estimators that often **don't have an explicit formula (for example, estimators for Generalized Linear Models), and often requires approximate computation via a computer program.**
>
> 2) bcd
>
> * Unbiasedness is in general an advantage of an estimator, and the estimator $X_1$ is unbiased because $\mathbb{E}[X_1] = \theta$.
> * Since $X_1$ is Bernoulli, it is either $0$ or $1$, it is not equal to the true parameter $\theta$ which is assumed to lie in $(0,1)$. Hence, $\hat{\theta}_n = X_1$ is not consistent. Inconsistency is in general a disadvantage.
> * **It is generally best to use all information that is given about a distribution for parameter estimation**. One sample (which we know is either $0$ or $1$) does not tell much about the underlying distribution. Hence, it is a potential disadvantage that the samples $X_2, \ldots , X_ n$ were not used to construct the estimator $\hat{\theta }_ n = X_1$.
> * Note that $\text {Var}[X_1] = \theta (1 - \theta )$, and $X$ is unbiased, so the quadratic risk is equal to the variance $\theta(1-\theta)$. This estimator does not tend to $\theta$ as $n \rightarrow \infty$. This is a potential disadvantage, because **if the quadratic risk does not go to $0$, then $\hat{\theta}_n$ does not converge to $\theta$ in $L^2$. Intuitively, an estimator that does not converge in $L^2$ inherently has limited accuracy no matter how many samples are collected.**
>
> 3) abcd
>
> * Unbiased estimators avoid inherent inaccuracies of approximation that result from biasedness.
>
> * Consistent estimators become better and better approximations to the true parameter as the sample size increases.
>
> * **Averages can be computed in linear time from the dat**a, so is a computationally efficient estimator.
>
> * The estimator is unbiased, so its variance is the same as its quadratic risk. By independence and the i.i.d. assumption,
>   $$
>   \text {Var}(\overline{X}_ n) = \frac{1}{n^2} \sum _{i = 1}^ n \text {Var}(X_1) = \frac{\theta (1 - \theta )}{n}
>   $$
>   which tends to $0$ as $n \rightarrow \infty$. Thus, $\hat{\theta }_ n \stackrel{L^2}{\sim } \theta$, which ensures consistency. 
>
> **Remark:** 
>
> Convergence in $L^2$ is, mathematically speaking, a stronger guarantee than convergence in probability. That is, if $\hat{\theta }_ n \stackrel{L^2}{\to } \theta$, then also, $\hat{\theta }_ n \stackrel{\text {prob}}{\to } \theta$. 

## 6. Confidence Intervals (CI)

C.I. is to tell precisely where the true $\theta$ will be.

Let $(E, (\mathbb{P}_\theta)_{\theta \in \Theta})$ be a statistical model based on observations $X_1, ..., X_n$, and assume $\Theta \subseteq \R$. Let $\alpha \in (0,1)$.

* C.I. of level $1-\alpha$ for $\theta$: 

  Any random (depending on $X_1, ..., X_n$) interval $\mathcal{I}$ whose boundaries do not depend on $\theta$ and such that:
  $$
  \mathbb{P}_{\theta}[\mathcal{I} \ni \theta] \geq 1 - \alpha, \quad \forall \theta \in \Theta
  $$

* C.I. of **asymptotic** level $1- \alpha$ for $\theta$: 

  Any random interval $\mathcal{I}$ whose boundaries do not depend on $\theta$ and such that:
  $$
  \lim_{n \rightarrow \infty} \mathbb{P}_\theta[\mathcal{I} \ni \theta] \geq 1- \alpha, \quad \forall \theta \in \Theta
  $$

Note that $\mathcal{I} \ni \theta$ means $\mathcal{I}$ contains $\theta$. This notation emphasizes the randomness of $\mathcal{I}$ but we can equivalently write $\theta \in \mathcal{I}$.

**Example**:

* We observe $R_1, ..., R_n \stackrel{iid}{\sim} \mathsf{Ber}(p)$ for some unknown $p \in (0,1)$.

* Statistical model: $\left(\{0,1\}, (\mathsf{Ber}(p))_{p \in (0,1)}\right)$.

* The estimator for $p$ is $\hat{p} = \bar{R}_n$

* From CLT (CLT gives asymptotic normality):
  $$
  \sqrt{n} {\bar{R}_n - p \over \sqrt{p(1-p)}} \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
  $$
  This means that:

  * $\Phi(x): $ cdf of $\mathcal{N}(0,1); \Phi_n(x): $ cdf of $\sqrt{n} {\bar{R}_n - p \over \sqrt{p(1-p)}}$.

  * Then: $\Phi_n(x) \approx \Phi(x)$ (CLT) when $n$ becomes large. Hence, for all $x > 0$,
    $$
    \begin{aligned}
    &\mathbb{P}\left(\sqrt{n} {\bar{R}_n - p \over \sqrt{p(1-p)}} \leq x\right) \approx \Phi(x)\\
    &\implies \mathbb{P} \left(|\bar{R}_n - p| > {x\sqrt{p(1-p)} \over \sqrt{n}}\right) = 2 \Phi(-x) = 2 \Phi(-{x\sqrt{n} \over \sqrt{p(1-p)}})\\
    &\implies \mathbb{P}\left(|\bar{R}_n - p| \geq x \right) \simeq 2 \left(1 - \Phi\left({x\sqrt{n} \over \sqrt{p(1-p)}}\right)\right)
    \end{aligned}
    $$
    Note that convergence in distribution can be characterized by convergence of the cdf's at each point.

**C.I.**

* Find $x$ such that 
  $$
  \begin{aligned}
  &2\left( 1 - \Phi\left({x\sqrt{n} \over \sqrt{p(1-p)}}\right)\right) = {\alpha}\\
  &\implies \Phi\left({x\sqrt{n} \over \sqrt{p(1-p)}}\right) = 1 - {\alpha \over 2}\\
  &\implies{x\sqrt{n} \over \sqrt{p(1-p)}} = \Phi^{-1}\left(1 - {\alpha \over 2}\right) = q_{\alpha/2}\\
  &\implies x = {q_{\alpha/2 }\sqrt{p(1-p)} \over \sqrt{n}}
  \end{aligned}
  $$
  Hence, 
  $$
  \begin{aligned}
  &\mathbb{P}[|\bar{R}_n - p| \leq x] \simeq 1 - \alpha\\
  &\mathbb{P}[\bar{R}_n - x \leq p \leq \bar{R}_n + x] \simeq 1 - \alpha\\
  \end{aligned}
  $$

* For a fixed $\alpha \in (0,1)$, if $q_{\alpha/2}$ is the $(1-\alpha/2)$-quantile of $\mathcal{N}(0,1)$, then with probability $\simeq 1- \alpha$ (if $n$ is large enough).
  $$
  \bar{R}_n \in \left[ p - {q_{\alpha/2 }\sqrt{p(1-p)} \over \sqrt{n}}, p + {q_{\alpha/2 }\sqrt{p(1-p)} \over \sqrt{n}}\right].
  $$

* It yields
  $$
  \lim_{n\rightarrow \infty} \mathbb{P} 
   \left(\left[ \bar{R}_n - {q_{\alpha/2 }\sqrt{p(1-p)} \over \sqrt{n}}, \bar{R}_n + {q_{\alpha/2 }\sqrt{p(1-p)} \over \sqrt{n}}\right] \ni p \right) = 1 - \alpha.
  $$
  where $\bar{R}_n$ is random, $p, n, q_{\alpha/2}$ are deterministic.

* But this is not a C.I. because it depends on $p$. To fix this, there are $3$ solutions.

### (1) Conservative Bound

Recall that by the CLT, for any $p,(0 < p < 1)$:
$$
\lim _{n\to \infty } \mathbf{P}\left(\left|\sqrt{n}\frac{\overline{R}_ n-p}{{{\sigma _ p}} }\right|< q_{\alpha /2}\right) =\lim _{n\to \infty } \mathbf{P}\left( \overline{R}_ n-q_{\alpha /2}\frac{{{\sigma _ p}} }{\sqrt{n}}\, <\, p\, <\, \overline{R}_ n+q_{\alpha /2}\frac{{{\sigma _ p}} }{\sqrt{n}}\right) {{=}} \, 1-\alpha
$$
where $\sigma _ p=\sqrt{p(1-p)}$.

To construct a confidence interval, we need to replace $σ_p$ above by a number $c$ that does not depend on the unknown parameter $p$, so that it guarantees that all $p$ in $(0,1)$,
$$
\lim _{n\to \infty } \mathbf{P}\left(\left|\sqrt{n}\frac{\overline{R}_ n-p}{{\color{blue}{c}} }\right|< q_{\alpha /2}\right) {\color{blue}{\geq }} \, 1-\alpha ?
$$
The condition $c$ should satisfy is that 
$$
\left(\overline{R}_ n-q_{\alpha /2}\frac{{{c}} }{\sqrt{n}},\, \overline{R}_ n+q_{\alpha /2}\frac{{{c}} }{\sqrt{n}}\right) {{\supseteq }}  \left(\overline{R}_ n-q_{\alpha /2}\frac{{{\sigma _ p}} }{\sqrt{n}},\, \overline{R}_ n+q_{\alpha /2}\frac{{{\sigma _ p}} }{\sqrt{n}}\right) \qquad \text {for all } p
$$
Hence any $c \geq \max_p(\sigma_p^2)$ works. For Bernoulli example above, 
$$
\max _{p}\left(\sigma _ p\right)= \max _{p}\left(\sqrt{p(1-p)}\right) \, =\,  1/2
$$
That is, no matter the (unknown) value of $p$,  $p(1-p) \leq {1\over 4}$. Thus, roughly with probability at least $1-\alpha$
$$
\bar{R}_n \in \left[ p - {q_{\alpha/2}\over 2\sqrt{n}}, p + {q_{\alpha/2}\over 2\sqrt{n}}\right]
$$
We get the asymptotic confidence interval:
$$
\mathcal{I}_{conserv} = \left[ \bar{R}_n - {q_{\alpha/2}\over 2\sqrt{n}}, \bar{R}_n + {q_{\alpha/2}\over 2\sqrt{n}}\right]
$$
Indeed, 
$$
\lim_{n\rightarrow \infty} \mathbb{P}(\mathcal{I}_{conserv} \ni p) \geq 1 - \alpha
$$
This is the widest possible C.I., since when $p = 1/2$ we have the most uncertainty.

### (2) Solving the (quadratic) equation for $p$

We have the system of two inequalities in $p$:
$$
\overline{R}_ n-q_{\alpha /2}\frac{{{\sqrt{p(1-p)}}} }{\sqrt{n}}\, \leq\, p\, \leq\, \overline{R}_ n+q_{\alpha /2}\frac{{{\sqrt{p(1-p)}}} }{\sqrt{n}}
$$
Equivalently,
$$
\left|\sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\right|< q_{\alpha /2}
$$
Each is a quadratic inequality in $p$ of the form
$$
\begin{aligned}
\left|\sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\right|< q_{\alpha /2} &\implies \left(\sqrt{n} \frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\right)^2< q_{\alpha /2}^2\\
& \implies  \left(\overline{R}_ n-p\right)^2< \frac{p(1-p) q_{\alpha /2}^2}{n}\\
& \implies p^2\left(1+ \frac{q_{\alpha /2}^2}{n}\right)-p\left(2\overline{R}_ n+\frac{q_{\alpha /2}^2}{n}\right)+\left(\overline{R}_ n\right)^2<0
\end{aligned}
$$
We need to find the roots $p_1 < p_2$ of 
$$
p^2\left(1+ \frac{q_{\alpha /2}^2}{n}\right)-p\left(2\overline{R}_ n+\frac{q_{\alpha /2}^2}{n}\right)+\left(\overline{R}_ n\right)^2 = 0
$$
Solving by $p = \frac{-B\pm \sqrt{B^2-4AC}}{2A}$, this leads to a new confidence interval $\mathcal{I}_{solve} = [p_1, p_2]$ such that
$$
\lim_{n \rightarrow \infty} \mathbb{P}(\mathcal{I}_{solve} \ni p) = 1- \alpha
$$
The quadratic function $Ap^2+Bp+C<0$ where $A>0$ is convex, so the parabola opens up, and the region in which the parabola is below the x-axis is the interval between the two roots. Given $0<p_1<p_2<1$, the region is $p_1<p<p_2$.

### (3) Using Slutsky Theorem: Plug-in

Recall by the **LLN** $\hat{p} = \bar{R}_n \xrightarrow[n \rightarrow \infty]{\mathbb{P}, a.s.} p $.

By **Slutsky**, ( if I have a convergence of distribution, multiply by a convergence in probability, or in convergence of distribution to a deterministic number, I can actually multiply the limits. )
$$
\begin{aligned}
&\sqrt{n} {\bar{R}_n - p \over \sqrt{\hat{p}(1-\hat{p})}} = \sqrt{n} {\bar{R}_n - p \over \sqrt{{p}(1-{p})}} {\sqrt{{p}(1-{p})}\over \sqrt{\hat{p}(1-\hat{p})}}\\
&{\sqrt{{p}(1-{p})}\over \sqrt{\hat{p}(1-\hat{p})}} \xrightarrow[n \rightarrow \infty]{} 1 \quad \text{by LLN and continuous mapping theorem (CMT)}\\ 
&\implies 
\sqrt{n} {\bar{R}_n - p \over \sqrt{\hat{p}(1-\hat{p})}} \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
\end{aligned}
$$
This leads to a new confidence interval
$$
\mathcal{I}_{\text{plug-in}} = \left[ \bar{R}_n - {q_{\alpha/2 }\sqrt{\hat{p}(1-\hat{p})} \over \sqrt{n}}, \bar{R}_n + {q_{\alpha/2 }\sqrt{\hat{p}(1-\hat{p})} \over \sqrt{n}}\right]
$$
such that
$$
\lim_{n \rightarrow \infty} \mathbb{P}(\mathcal{I}_{\text{plug-in}} \ni p) = 1-\alpha
$$
This approach is slightly less precise than the second solution.

> #### Exercise 25
>
> Show the convergence of different quantities:
>
> a) $\overline{R}_n$
>
> b) $\sqrt{n} \left(\overline{R}_n - p\right)$
>
> c) $\sqrt{n} {\overline{R}-p \over \sqrt{p(1-p)}}$
>
> d) $ \sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)}$
>
> e) $\frac{\sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)}}{\sqrt{p(1-p)}}$
>
> f) $\left(\sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\right) \left(\displaystyle \frac{\sqrt{p(1-p)}}{\sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)}}\right)$
>
> **Answer**: 
>
> a) $\overline{R}_n \xrightarrow [n\longrightarrow \infty ]{{{(\mathbf{P})}} } {{p}}$, and it approximated by (in distribution) $\mathcal{N}({{p}} ,{{\frac{p(1-p)}{n}}} )$
>
> b) $\sqrt{n}\left(\overline{R}_ n-p\right) \xrightarrow [n\longrightarrow \infty ]{{{(d)}} } \mathcal{N}({{0}} ,{{p(1-p)}} )$
>
> c) $\sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}} \xrightarrow [n\longrightarrow \infty ]{{{(d)}} } \mathcal{N}({{0}} ,{{1}} )$
>
> d) $ \sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)} \xrightarrow [n\longrightarrow \infty ]{{{(\mathbf{P})}} } {{\sqrt{p(1-p)}}}$
>
> e) $\frac{\sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)}}{\sqrt{p(1-p)}}\xrightarrow [n\longrightarrow \infty ]{{{(\mathbf{P})}} } {{1}}$
>
> f) $\left(\sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\right) \left(\displaystyle \frac{\sqrt{p(1-p)}}{\sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)}}\right) \xrightarrow [n\longrightarrow \infty ]{{{(d)}} } \mathcal{N}({{0}} ,{{1}} )$
>
> **Solution**: 
>
> a) $\overline{R}_ n\xrightarrow [n\longrightarrow \infty ]{{{(\mathbf{P})}} } \mathbb E\left[\overline{R}_ n\right] = {{p}}$ by the (weak) LLN.
>
> $\overline{R}_ n\xrightarrow [n\longrightarrow \infty ]{{{(d)}} } \mathcal{N}\left(\mathbb E\left[\overline{R}_ n\right], \textsf{Var}\left(\overline{R}_ n\right)\right)=\mathcal{N}\left(p,\frac{p(1-p)}{n}\right)$ by the CLT.
>
> b) $\sqrt{n}\left(\overline{R}_ n-p\right)\xrightarrow [n\longrightarrow \infty ]{{{(d)}} } \mathcal{N}\left(\mathbb E\left[\sqrt{n}\left(\overline{R}_ n-p\right)\right], n\textsf{Var}\left(\overline{R}_ n\right)\right)=\mathcal{N}\left(0,p(1-p)\right)$ by the CLT. Note that with an asymptotic variance that does not depend on $n, \sqrt{n}\left( \overline{R}_n - p\right)$ does not converge in probability to a constant.
>
> c) $ \sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\xrightarrow [n\longrightarrow \infty ]{{{(d)}} } \mathcal{N}\left(0,1)\right)$ by the CLT.
>
> d) $ \sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)} \xrightarrow [n\longrightarrow \infty ]{{{(\mathbf{P})}} } {{\sqrt{p(1-p)}}}$ by the continuous mapping theorem.
>
> e) $\frac{\sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)}}{\sqrt{p(1-p)}}\xrightarrow [n\longrightarrow \infty ]{{{(\mathbf{P})}} } {{1}}$ since constant multiple of sequences that converge in probability still converge in probability.
>
> f) $\left(\sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\right) \left(\displaystyle \frac{\sqrt{p(1-p)}}{\sqrt{\overline{R}_ n\left(1-\overline{R}_ n\right)}}\right) \xrightarrow [n\longrightarrow \infty ]{{{(d)}} } \mathcal{N}({{0}} ,{{1}} )$ by Slutsky.

> #### Exercise 26: Confidence Intervals of the mean of Gaussian random variables
>
> Let $X_1, ..., X_n$ be i.i.d. Gaussian random variables, with unknown mean $\mu$ and known variance 1.
>
> 1. Find an estimator $\hat{\mu}$ of $\mu$, based on $X_1, ..., X_n$.
> 2. Determine the distribution of $\hat{\mu}$.
> 3. Compute a confidence interval for $\mu$ with level $95\%$ that is centered about $\hat{\mu}$.
> 4. Propose two other confidence intervals for $\mu$ with level $95\%$, which are unbounded either to the left or to the right.
>
> **Answer**: 
>
> 1) $\hat{\mu} = \overline{X}_n = {1 \over n }\sum^n_{i=1}X_i$ (LLN: $\overline{X_n} \xrightarrow[n \rightarrow \infty]{\mathbb{P}} \mathbb{E}[X_1] = \mu$)
>
> 2) Since the sum of Gaussian variables is also Gaussian, $\overline{X}_n$ is Gaussian distributed.
> $$
> \begin{aligned}
> \mathbb{E}[\overline{X}_n] &= \mathbb{E}\left[{1\over n}\sum^n_{i=1}X_i\right] = {1\over n}\sum^n_{i=1}\mathbb{E}[X_i] = {n \over n} \mu = \mu\\
> \mathsf{Var}(\overline{X}_n) &= \mathsf{Var}({1\over n} \sum^n_{i=1}X_i) ={1\over n^2}\sum^n_{i=1}\mathsf{Var}(X_i) = {n \over n^2} = {1 \over n}
> \end{aligned}
> $$
> Thus, the distribution is 
> $$
> \begin{aligned}
> &\overline{X}_n \sim \mathcal{N}(\mu, {1\over n})\\
> \implies& \sqrt{n}(\hat{\mu} - \mu) \sim \mathcal{N}(0,1)
> \end{aligned}
> $$
> where $\sqrt{n}(\hat{\mu} - \mu)$ is called **pivot**.
>
> 3) The **two sided** C.I. $\mathcal{I}$ can be written as 
> $$
> \mathcal{I} = \hat{\mu} + [-s,s] = [\hat{\mu} - s, \hat{\mu} + s]
> $$
> Given level $1-\alpha =0.95$, we have
> $$
> \begin{aligned}
> & 1- \alpha = \mathbb{P}(\mu \in \mathcal{I})\\
> & \Leftrightarrow \mu \in [\hat{\mu} -s, \hat{\mu} + s]\\
> & \Leftrightarrow \hat{\mu} - s \leq \mu \leq \hat{\mu} +s\\
> & \Leftrightarrow -s \leq \mu - \hat{\mu} \leq s\\
> & \Leftrightarrow -s \leq  \hat{\mu}-\mu \leq s\\
> & \Leftrightarrow -s\sqrt{n} \leq  \sqrt{n}(\hat{\mu}-\mu) \leq s\sqrt{n}\\
> \end{aligned}
> $$
> Let $q = s\sqrt{n}, Z = \sqrt{n}(\hat{\mu}-\mu)$, then this can be rewritten as
> $$
> \begin{aligned}
> 1- \alpha &= \mathbb{P}(Z \in [-q,q])\\
> & = \mathbb{P}(Z \leq q) - \mathbb{P}(Z \leq -q)\\
> & = \mathbb{P}(Z \leq q) - (1-\mathbb{P}(Z \leq q))\\
> & = 2 \cdot \mathbb{P}(Z \leq q ) - 1\\
> & = 2 \cdot \Phi(q) - 1\\
> \implies & \Phi(q) = 1 - {\alpha \over 2}\\
> \implies & q = q_{\alpha/2}
> \end{aligned}
> $$
> Therefore, the C.I. is 
> $$
> \mathcal{I} = \hat{\mu} + \left[ - {q_{\alpha/2} \over \sqrt{n}}， {q_{\alpha/2} \over \sqrt{n}} \right] ,\quad  \alpha/2=0.025, q_{\alpha/2} \approx 1.96 
> $$
> The one sided C.I. $\mathcal{J}$ can be written as
> $$
> \mathcal{J} = (-\infty, \hat{\mu} + s]
> $$
> Given level $1 - \alpha = 0.95$, we have
> $$
> \begin{aligned}
> & 1- \alpha = \mathbb{P}(\mu \in \mathcal{J})\\
> & \Leftrightarrow \mu \in (-\infty, \hat{\mu} + s ]\\
> & \Leftrightarrow  \mu \leq \hat{\mu} +s\\
> & \Leftrightarrow -s \leq \mu - \hat{\mu}\\
> & \Leftrightarrow -s \sqrt{n} \leq  (\hat{\mu}-\mu)\sqrt{n} 
> \end{aligned}
> $$
> Let $q = s\sqrt{n}, Z = \sqrt{n}(\hat{\mu}-\mu)$, then this can be rewritten as
> $$
> \begin{aligned}
> 1- \alpha &= \mathbb{P}(Z \geq -q)\\
> & = \mathbb{P}(Z \leq q)\\
> & = \Phi(q)\\
> \implies & q = q_{\alpha}
> \end{aligned}
> $$
> Therefore, the C.I. is 
> $$
> \mathcal{J} = ( -\infty, \hat{\mu} + {q_{\alpha} \over \sqrt{n}}],\quad  \alpha=0.05, q_{\alpha} \approx 1.65
> $$

