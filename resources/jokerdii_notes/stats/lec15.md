# Lecture 15. Goodness of Fit Test for Discrete Distributions

There are 8 topics and 3 exercises.

## 1. Introduction to Goodness of Fit Tests

#### Recap of Parametric Hypothesis Testing: The Uniform Statistical Model

Let $X$ be a uniform random variable with the distribution $\text {Unif}\left[0,\theta ^*\right]$.

We would like to test whether $H_0: \theta ^* = 2$ or $H_1: \theta ^* \ne 2$, with $\Theta = (0,\infty )$.

Let $X_1,\dots ,X_ n$ be i.i.d. samples of $X$.

* Let $\overline{X_ n}$ denote sample mean.
* Let $\widetilde{S}_ n$ denote the unbiased sample variance of $X_1, \dots , X_ n$.
* Let $\widehat{\theta _ n}^{\text {MLE}}$ denote the maximum likelihood estimator of $\theta$.
* Let $\ell _ n\left(\widehat{\theta _ n}^{\text {MLE}}\right)$​​ denote the log-likelihood of $n$​​ samples evaluated at the maximum likelihood estimator and $\ell _ n\left(2\right)$​​ denote the log-likelihood of $n$​​ samples under $H_0$.

Select from the tests that are technically correct (that is, can be applied under this scenario) and that have the required level $\alpha \in [0,1]$.

**Note:** By asymptotic level of $\alpha$​, we require the probability of type-1 error under $H_0$​ be at most $\alpha$​ as $n \rightarrow \infty$​. By non-asymptotic level of $\alpha$​, we require the probability of type-1 error under $H_0$​ be at most $\alpha$​ for every $n$.

A. $\mathbf{1}\left\{ \frac{\left| \overline{X_ n} - 1 \right|}{\sqrt{\widetilde{S}_ n/n}} > q_{\alpha /2}\right\}$​ for non-asymptotic level $\alpha$​, where $q_{\alpha /2}$​ is the $(1-\alpha/2)$​-quantile of the Student's T distribution with $n-1$​ degrees of freedom.

B. $\mathbf{1}\left\{ \sqrt{n} \frac{\left| 2 \overline{X_ n} - 2 \right|}{\sqrt{4/3}} > q_{\alpha /2}\right\}$ for asymptotic level $\alpha$, where $q_{\alpha}$ is the $(1-\alpha)$-quantile of the standard normal random variable.

C. $\mathbf{1}\left\{  \widehat{\theta _ n}^{\text {MLE}} > 2 \text { or } \widehat{\theta _ n}^{\text {MLE}} \le 1 \right\}$ for asymptotic level $\alpha$.

D. $\mathbf{1}\left\{ 2\left(\ell _ n\left(\widehat{\theta _ n}^{\text {MLE}}\right) - \ell _ n\left(2\right)\right) > q_{\alpha }\right\}$ for asymptotic level $\alpha$, where $q_\alpha$ is the $(1-\alpha)$-quantile of $\chi_1^2$​.

**Answer:**

BC is technically CORRECT.

A. The first choice is attempting a Student's T test for non-asymptotic level $\alpha$​ and this is technically incorrect because $X$​ is not a Gaussian random variable. **Only if $X$​ is a Gaussian random variable will the test statistic follow a Student's T distribution for a finite number of sample $n$.**

B. This is a test that is both technically correct and has an asymptotic level $\alpha$​. This can be seen from the following:

* $2\overline{X_ n}$​ has an expectation equal to $\theta^*$.

* The variance of $2\overline{X_ n}$ under $H_0$ is
  $$
  \begin{aligned}
  \textsf{Var}_{H_0}\left(2 \overline{X_ n}\right) &= \frac{4}{n}\textsf{Var}_{H_0}(X)\\
  &= \frac{4}{n} \frac{4}{12}\\
  &=\frac{4}{3n}.
  \end{aligned}
  $$

* An application of CLT.

**Remark**: Wald's test cannot be written out because Fisher information does not exist for the uniform random variable.

C. This choice has an asymptotic level 0 because of the following:
$$
\begin{aligned}
P_{H_0}\left[\widehat{\theta _ n}^{\text {MLE}} > 2 \text { or } \widehat{\theta _ n}^{\text {MLE}} \le 1\right] &= P_{H_0}\left[\widehat{\theta _ n}^{\text {MLE}} > 2\right] + P_{H_0}\left[\widehat{\theta _ n}^{\text {MLE}} \le 1\right]\\
&= P_{H_0}\left[\widehat{\theta _ n}^{\text {MLE}} \le 1\right]\\
&= P_{H_0}\left[\max _{i=1,\dots ,n}X_ i \le 1\right]\\
&= \left(\frac{1}{2}\right)^ n \to 0.
\end{aligned}
$$
D. This choice is attempting a likelihood ratio test using the log-likelihoods evaluated at the MLE and under $H_0$ and this choice is also technically incorrect because the MLE technical conditions are not satisfied for the uniform statistical model (recall the technical conditions for asymptotic normality of the MLE). **Only if the MLE conditions are satisfied can this test be applied according to Wilk's theorem.** 

#### Intuition for Goodness of Fit Tests

Let $X$ be a r.v. Given i.i.d. copies of $x$ we want to answer the following types of questions:

* Does $X$ have distribution $\mathcal{N}(0,1)$? (Cf. Student's T distribution)
* Does $X$ have distribution $\mathcal{U}([0,1])$?
* Does $X$ have PMF $p_1 = 0.3, p_2 = 0.5, p_4 = 0.2$?

These are all *goodness of fit* (GoF) tests: we want to know if the hypothesized distribution is a good fit for the data.

Key characteristic of GoF tests: non-parametric modeling.

In practice, a useful tool for making such a decision is to use a **histogram** of the data set. The x-axis, which represents the sample space, is divided into the intervals $[i, i+1]$​​​ for all $i \in \Z$​​. The bar over the interval $[i,i+1]$​ represents how many data points took values in that interval.

#### Terminology

Suppose you observe i.i.d. samples $X_1, \ldots , X_ n \sim P$ from some unknown distribution $\mathbf P$. Let $\mathcal{F}$ denote a parametric family of probability distributions (e.g., $\mathcal{F}$ could be the family of normal distribution $\{  \mathcal{N}(\mu , \sigma ^2) \} _{\mu \in \mathbb {R}, \sigma ^2 > 0}$).

In the topic of **goodness of fit testing**, our goal is to answer the question "**Does** $\mathbf{P}$​​​ **belong to the family** $\mathcal{F}$​​​, **or is** $\mathbf{P}$​​ **any distribution outside of**  $\mathcal{F}$​ **?**"

Parametric hypothesis testing is a particular case of goodness of fit testing (why?). However, in the context of parametric hypothesis testing, we assume that the data distribution $\mathbf{P}$ comes from some **parametric** statistical model $\{ \mathbf{P}_\theta \} _{\theta \in \Theta }$, and we ask if the distribution $\mathbf{P}$ belongs to a submodel $\{ \mathbf{P}_\theta \} _{\theta \in \Theta_0 }$or its complement $\{ \mathbf{P}_\theta \} _{\theta \in \Theta_1 }$. In parametric hypothesis testing, we allow only a small set of alternatives $\{ \mathbf{P}_\theta \} _{\theta \in \Theta_1 }$, where as in the goodness of fit testing, we allow the alternative to be anything.

**Remark**: In general, goodness of fit testing is considered a topic in **non-parametric statistics**, in contrast to the material we have covered so far. You should keep in mind though that the topic of parametric hypothesis testing is a special case of goodness of fit testing. However, to handle non-parametric models we will need to develop new techniques.

#### Goodness-of-Fit

Let $X_1, ..., X_n \stackrel{iid}{\sim}\mathbb{P}_\mathbf{p}$​​, for some unknown $\mathbf{P}\in \Delta_K$​​, and let $\mathbf{p}^0 \in \Delta_K$​​ be fixed.​

We want to test:
$$
H_0: \mathbf{p}=\mathbf{p}^0 \quad \text{vs.} \quad H_1: \mathbf{p} \neq \mathbf{p}^0
$$
With asymptotic level $\alpha \in (0,1)$.

Example: If $\mathbf{p}^0 = (1/K, 1/K, ..., 1/K)$​​, we are testing whether $\mathbb{P}_\mathbf{p}$​​ is the **uniform distribution** on $E$​.

## 2. The Probability Simplex of Discrete Distributions

The probability simplex in $\R^K$​, denoted by $\Delta_K$​, is the set of all vectors $\mathbf{p} = \left[p_1, \dots , p_ K\right]^ T$​ (Note that we are using subscripts for vector indices for simplicity) such that
$$
\displaystyle  \displaystyle \mathbf{p}\cdot \mathbf{1}\, =\, \mathbf{p}^ T \mathbf{1} = 1, ~ ~  p_ i \ge 0 \text { for all } i= 1,\ldots , K
$$
where $\mathbf{1}$ denotes the vector $\, \mathbf{1}=\begin{pmatrix} 1& 1& \ldots & 1\end{pmatrix}^ T$​. 

Equivalently, in more familiar notation, let $E = \{a_1, ..., a_K\}$​​ be a finite space and $(\mathbb{P}_\mathbf{P})_{\mathbf{P} \in \Delta_K}$​​​ be the family of all probability distributions on $E$:

* A set of PMFs: 
  $$
  \Delta_K = \Big\{\mathbf{p} = (p_1, ..., p_K) \in (0,1)^{K}: \sum^K_{j=1} p_j = 1\Big\}
  $$

* For $\mathbf{p} \in \Delta_K$​ and $X \sim \mathbb{P}_\mathbf{P}$​,
  $$
  \mathbb{P}_{\mathbf{P}}[X = a_j] = p_j, \qquad j =  1, ..., K.
  $$

## 3. Goodness of Fit Test - Discrete Distributions

#### Multinomial Distribution

The **multinomial distribution** with $K$​​​ modalities (or equivalently $K$​​ possible outcomes in a trial) is a generalization of the binomial distribution. It models the probability of counts of the $K$ possible outcomes of the experiment in $n'$ i.i.d trials of the experiment.

It is parameterized by the parameters $n', p_1, ..., p_K$ where

* $n'$ is the number of i.i.d trials of the experiment
* $p_i$​ is the probability of observing outcome $i$​ in any trial, and hence the $p_i$​'s satisfy $p_i \geq 0$​ for all $i=1, ..., K$​, and $\displaystyle \sum _{i=1}^ K p_ i = 1$​.

Let $\mathbf{p} \triangleq [p_1~ ~ p_2~ ~ \cdots ~ ~ p_ K]^ T$ and note that $\mathbf{p} \in \Delta _ K$.

The multinomial distribution can be represented by a random vector $\mathbf N\in \mathbb {Z}^ K$ to represent the number of instances $N^{(i)}$ of the outcome $i =1, ..., K$. Note that $\sum _{i=1}^ K N^{(i)} = n'$. The multinomial PMF for all $n$ such that $\sum _{i=1}^ K n^{(i)} = n'$,
$$
\displaystyle  p_{\mathbf N}\left(N^{(1)} = n^{(1)}, \dots , N^{(K)} = n^{(k)}\right) = \frac{n'!}{n^{(1)}! n^{(2)}! \cdots n^{(K)}!} \prod _{i=1}^ K p_ i^{n^{(i)}}.
$$

#### Categorial (Generalized Bernoulli) Distribution and its Likelihood

The multinomial distribution, when specialized to $n'=1$​​​​​ for any $K$​​​​​ gives the **categorical distribution**. When $K=2$​​​​ and the two outcomes are $0$​​​​ and $1$​​​​ the categorical distribution is the Bernoulli distribution, and for any $K > 2$​​ the categorical distribution is also known as the **generalized Bernoulli distribution**.

The categorical distribution, therefore, models the probability of counts of the $K$​​​​ possible outcomes of a discrete experiment in a single trial. Since the total count is equal to $1$​ (only one trial), we can use a random variable $X$ to represent the outcome of the trial. This means the sample space of a categorical random variable $X$ is
$$
  E = \{  a_1, \ldots , a_ K \} .
$$
The vector $\mathbf{p}$​​ is the parameter of a categorical random variable. The PMF of a categorical distribution can be given as
$$
P(X=a_ j) = \prod _{i=1}^ K p_ i^{\mathbf{1}(a_ i=a_ j)} = p_ j, ~ ~ j=1,\dots ,K.
$$
Let $\mathbf{P}_\mathbf {p}$​ denote the distribution of a categorical random variable with sample space $E= \{  a_1, \ldots , a_ K \}$​ and parameter vector $\mathbf{p}$​. Let $\Delta_K$ denote the **probability simplex** in $\R^K$, $p \in \R^K$. The **categorical statistical model** can thus be written as the tuple $\left( \{  a_1, \ldots , a_ K \} , \{ \mathbf{P}_{\mathbf{p}} \} _{\mathbf{p} \in \Delta _ K}\right)$​.

In goodness of fit testing for a discrete distribution, we observe $n$ i.i.d. samples $X_1, \dots , X_ n$ of a categorical random variable $X$ and it is our aim to find statistical evidence of whether a certain distribution $\mathbf{p}^0 \in \Delta _ K$ could have generated $X_1, \dots , X_ n$.

The **categorical likelihood** of observing a sequence of $n$​ i.i.d outcomes $X_1, X_2, \dots , X_ n \sim X$​ can be written using the number of occurrences $N_ i, i=1,\dots ,K$​ of the $K$​ outcomes as
$$
L_ n(X_1,\dots ,X_ n,p_1,\dots ,p_ K) = p_1^{N_1}p_2^{N_2} \cdots p_ K^{N_ K}.
$$
The categorical likelihood of the random variable $X$​, when written as a random function, is
$$
L(X,p_1,\dots ,p_ K) = \prod _{i=1}^ K p_ i^{\mathbf{1}(X = a_ i)}.
$$

#### Maximum Likelihood Estimator for the Categorical Distribution

The log likelihood is
$$
\log L_n(X_1,\dots ,X_ n,p_1,\dots ,p_ K) = N_1 \log(p_1) + ... + N_K \log(1-\sum^{k-1}_{j=1} p_j)
$$
Take the derivative and set it to zero
$$
{\partial \over \partial p_j} \log L_n(X_1,\dots ,X_ n,p_1,\dots ,p_ K) = {N_j \over p_j} + {N_k \over 1- \sum\limits^{k-1}_{j=1} p_j} = 0\\
\implies  {N_j \over p_j} =- {N_k \over 1- \sum\limits^{k-1}_{j=1} p_j}
$$
Let $- {N_k \over 1- \sum\limits^{k-1}_{j=1} p_j} = \gamma$​, we have
$$
p_j  = {N_j \over \gamma}
$$
We know that $\sum\limits_{j=1}^K p_j = 1$​, so that
$$
{\sum\limits^K_{j=1} N_j \over \gamma} =1 \quad \implies \gamma = \sum^K_{j=1} N_j = n
$$
Let $\hat{\mathbf{p}}$​ be the MLE:
$$
\hat{\mathbf{p}}_j = {N_j \over n}, \quad j=1,..., K
$$
$\hat{\mathbf{p}}$​​​​ maximizes $\log L_n(X_1, ..., X_n, \mathbf{p})$​​ **under the constraint**.

> #### Exercise 86
>
> Consider the distribution $\text {Ber}(0.25)$. Consider the categorical statistical model $\left( \{  a_1, \ldots , a_ K \} , \{ \mathbf{P}_{\mathbf{p}}\} \right)$ for this Bernoulli distribution. 
>
> 1. If we get $a_1 = 1$​ and $a_2 = 0$​, then this corresponds to a categorical distribution $\mathbf{P}_{\mathbf{p}}$​ with parameter vector $\mathbf{p}$​ given by ...
>
> 2. Let $a_i = i$​ for $i = 1,...,K$​. The uniform distribution on $E = \{1,2,..., K\}$​ can be expressed asa  categorical distribution $\mathbf{P}_{\mathbf{p}}$​ for some choice of parameter $\mathbf{p}$.
>
>    What is $\sum _{i = 1}^ K p_ i^2$​? 
>
> **Solution:**
>
> 1. Let $X \sim \text{Ber}(0.25)$​. Observe that
>    $$
>    p_1 = P(X = a_1) = P(X = 1) = 0.25\\
>    p_2 = P(X = a_2) = P(X = 0) = 0.75.
>    $$
>    Hence, $\mathbf{p} = [0.25~ ~ 0.75]^ T$​.
>
>    **Remark:** Observe that $\text {Ber}(p)$​​ has a one-dimensional parameter and $\mathbf{P}_{\mathbf{p}}$​​ for this example involves a parameter that is two-dimensional, but such that the second parameter depends on the first one $(p_1 = 1 - p_2)$​​. In general, the categorical distribution for $\mathbf{p} \in \Delta _ K$​​ involves a $K$​​-dimensional parameter, but **categorical distribution has only $K-1$​​ degrees of freedom. This will make our analysis more challenging: the extra constraint on the parameter $\sum _{i = 1}^ K p_ i = 1$​​​​ implies that the Fisher information for the model as specified does not exist. Hence, we cannot apply Wald's test directly.**
>
> 2. By definition, the uniform distribution weighs all elements in $\{ 1, \ldots , K\}$​ equally. Let $\mathbf{P}$​ denote the parameter vector of the uniform distribution on $\{ 1, 2, \ldots , K\}$​. Then
>    $$
>    p_ i = P(X = i) = \frac{1}{K}.
>    $$
>    Thus,
>    $$
>    \sum _{i = 1}^ K p_ i^2 = \sum _{i = 1}^ K \frac{1}{K^2} = \frac{1}{K}.
>    $$

## 4. The Goodness of Fit Test for Discrete Distributions: Chi-Squared Test

Note that 
$$
\sqrt{n}\left(\widehat{\mathbf{p}} - \mathbf{p}^0\right)^ T \mathbf{1} = \sqrt{n}\sum^K_{i=1} \left(\hat{p}_i - p_i^0\right) = \sqrt{n} \ \left(\sum _{i=1}^ K \widehat{p}_ i - \sum _{i=1}^ K p_ i^0\right) = \mathbf{0} \xrightarrow[n \rightarrow 0]{} 0
$$
where $\mathbf{p}^0$​​​​​​​ is the discrete PMF that we wish to test to goodness of fit for an observed sequence of iid samples, and $\hat{\mathbf{p}}$​​​​​​​ is the MLE upon observing the iid samples.

Since all linear combination of a Gaussian vector gives a Gaussian random variable, $\mathbf{0}$​​​ is actually a Gaussian random variable, or say a degenerated Gaussian. 

#### $\chi^2$ test

If $H_0$​​ is true, then $\sqrt{n}(\hat{\mathbf{p} } - \mathbf{p}^0)$​​ is asymptotically normal, and the following holds.

**Theorem:**

Under the null hypothesis:
$$
T_n = n\sum^K_{j=1} {(\hat{\mathbf{p}} - \mathbf{p}^0)^2 \over \mathbf{p}_j^0 } \xrightarrow[n \rightarrow \infty]{(d)} \chi^2_{K-1}
$$

* $\chi^2$​​​ test with asymptotic level $\alpha$: $\psi_\alpha = \mathbb{1}\{T_n > q_\alpha\}$​​​, where $q_\alpha$​ is the $(1-\alpha)$​-quantile of $\chi_{K-1}^2$​.
* Asymptotic p-value of this test: p-value = $\mathbb {P}[Z > T_n | T_n] $​​, where $Z \sim \chi^2_{K-1}$ and $Z \perp T_n$​.

**Informal Ideas with the Theorem above:**



> #### Exercise 87
>
> Let's consider a statistical model with parameter $\theta \in \mathbb {R}^ d$. Let $\theta^*$ be the parameter that generates the $n$ Iid samples $\mathbf X_1,\dots , \mathbf X_ n$. Let $I(\theta )$ be the Fisher information and assume that the MLE $\hat{\theta }_ n^{\text {MLE}}$ is asymptotically normal. Assume that $I(\theta ^0)$ is a diagonal matrix with positive entries $1/t_1, \dots , 1/t_ d$. We wish to perform a test for the hypotheses $H_0: \theta ^* = \theta ^0$ and $H_1: \theta ^* \ne \theta ^0$.
>
> Let the test statistic $T_n$ be
> $$
>   T_ n = n\sum _{i=1}^ d \frac{\left(\theta _ i^0 - \hat{\theta }_{i}\right)^2 }{t_ i},
> $$
> where $\left[\hat{\theta }_{1} ~ ~  \hat{\theta }_{2}~ ~  \cdots ~ ~  \hat{\theta }_{d}\right]^ T = \hat{\theta }_ n^{\text {MLE}}$.
>
> 1. What distribution does the test statistic $T_n$​​​ converge to under $H_0$​​​ as $n \rightarrow \infty$​​​?
> 2. What is the number of degrees of freedom of the asymptotic distribution of $T_n$​? 
>
> **Answer:**
>
> 1. $\chi _ d^2$.
> 2. $d$.
>
> **Solution:**
>
> The test statistic $T_n$ can be seen to be equivalent to
> $$
> n\left(\hat{\theta }_ n^{\text {MLE}} - \theta ^0\right)^ T I(\theta ^0) \left(\hat{\theta }_ n^{\text {MLE}} - \theta ^0\right),
> $$
> which is the test statistic for **Wald's test**, Therefore,
> $$
> T_ n \xrightarrow [n\to \infty ]{(d)} \chi _ d^2.
> $$

## 5. The Chi-Squared Test - Main / Informal Ideas

* Scaling by $\mathbf{p}^0_j$​​​​​​​ but not $(\mathbf{p}^0_j)^2$​​​​​​​​​​​ is coming from the half Fisher information matrix. We have some issues with this **Fisher information matrix: it is not well-defined in the sense of it is not invertible.** 

  The WRONG calculation of Fisher information: 
  $$
  L_n(X_1, ..., X_n ;\mathbf{p}) = p_1^{\sum\limits^n_{i=1}\mathbb{1}_{(X_1 = \theta_1)}} \cdot p_2^{\sum\limits^n_{i=1}\mathbb{1}_{(X_2 = \theta_2)}} ... p_K^{\sum\limits^n_{i=1}\mathbb{1}_{(X_K = \theta_K)}} \\
  \log L_1(X_1, \mathbf{p}) = \log({p_1}) \mathbb{1}_{(X =\theta_1)} + ... + \log({p_K}) \mathbb{1}_{(X =\theta_K)} \\
  I(\mathbf{p})= \begin{pmatrix} {\partial^2\over \partial p_j^2} & {\partial^2\over \partial p_j p_k} \\{\partial^2\over \partial p_k p_j} & {\partial^2\over \partial p_k^2}   \end{pmatrix} = \begin{pmatrix} {1\over p_j} & 0 \\0 & {1\over  p_k}   \end{pmatrix}\\
  $$
  Plugging in and we get
  $$
  n (\hat{\mathbf{p}}- \mathbf{p}^0) I(\mathbf{p}^0)(\hat{\mathbf{p}}- \mathbf{p}^0) = n \sum^K_{i=1} {(\hat{\mathbf{p}}_j - \mathbf{p}_j)^2\over \mathbf{p}_j}
  $$
  However, the LHS is wrong while the RHS is true. The LHS is wrong because the **additional restriction: $\sum^K_{i=1} p_j = 1$​​​ ($p_j$​​​s are dependent)​**, so we cannot take the derivative with respective to $p_j$​​ in this way. 

  The CORRECT calculation of Fisher information:
  $$
  \log L_1(X_1, \mathbf{p}) = \log(\mathbf{p}) \mathbb{1}_{(X =\theta_1)} + ... + \log(1-\mathbf{p}) \mathbb{1}_{(X =\theta_2)} 
  $$
  Take the derivative and take the expectation,
  $$
  {\partial^2 \over \partial \mathbf{p}^2} = -{\mathbb{1}_{(X = \theta_1)}\over \mathbf{p}^2} - {\mathbb{1}_{(X = \theta_2)}\over (1- \mathbf{p})^2} \xrightarrow[\mathbb{E}]{} -{1\over \mathbf{p}} -{1\over1- \mathbf{p}} = - {1\over \mathbf{p}(1-\mathbf{p})}\\
  {\partial^2 \over \partial (1-\mathbf{p})^2} = - {\mathbb{1}_{(X = \theta_2)}\over (1-\mathbf{p})^2} -{\mathbb{1}_{(X = \theta_1)}\over \mathbf{p}^2} \xrightarrow[\mathbb{E}]{} - {1\over \mathbf{p}(1-\mathbf{p})}\\
  {\partial^2 \over \partial \ \mathbf{p}(1- \mathbf{p})} = {\mathbb{1}_{(X = \theta_1)}\over \mathbf{p}^2} + {\mathbb{1}_{(X = \theta_2)}\over (1- \mathbf{p})^2} = {1\over \mathbf{p}(1-\mathbf{p})}\\
  $$
  The Fisher information is
  $$
  I\left(\begin{pmatrix}\mathbf{p}\\1-\mathbf{p} \end{pmatrix}\right) = \begin{pmatrix} {1\over \mathbf{p}(1-\mathbf{p})} & -{1\over \mathbf{p}(1-\mathbf{p})} \\-{1\over \mathbf{p}(1-\mathbf{p})} & {1\over \mathbf{p}(1-\mathbf{p})} \end{pmatrix} = {1\over \mathbf{p}(1-\mathbf{p})} \begin{pmatrix}1 & -1 \\ -1 & 1 \end{pmatrix}
  $$
  It is not invertible since 
  $$
  I\left(\begin{pmatrix}\mathbf{p}\\1-\mathbf{p} \end{pmatrix}\right) \begin{pmatrix}1\\ 1 \end{pmatrix} = \begin{pmatrix}0 \\ 0 \end{pmatrix}
  $$
  Geometrically, this means the MLE estimator does not fluctuate in all $K$​ direction in $\R^K$​.

* As for $\hat{\mathbf{p}}_j$​​, we know $\hat{\mathbf{p}}_j = {N_j \over n} \sim {\text{Bin}(n, p_j) \over n}$​​​​​. By CLT, the following is true:
  $$
  \sqrt{n} {\hat{\mathbf{p}}_j-\mathbf{p}_j^0 \over \sqrt{\mathbf{p}_j^0(1- \mathbf{p}_j^0)}} \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
  $$
  and
  $$
  n \ {(\hat{\mathbf{p}}_j-\mathbf{p}_j^0)^2 \over \mathbf{p}_j^0(1- \mathbf{p}_j^0)} \xrightarrow[n \rightarrow \infty]{(d)} \chi^2_1\\
  n \sum_{i=1}^K {(\hat{\mathbf{p}}_j-\mathbf{p}_j^0)^2 \over \mathbf{p}_j^0(1- \mathbf{p}_j^0)} \xrightarrow[n \rightarrow \infty]{(d)} \chi^2_K
  $$
  which is true but different from the Theorem given above (not the right normalization and not the right degrees of freedom).

  **Therefore, looking at the joint convergence of all of them is not the same as looking at individual convergences. The key is the dependence between individual estimators should not be ignored, otherwise, it would lead to an erroneous conclusion.**

  **Dividing by $\mathbf{p}^0 (1-\mathbf{p}^0)$​​​​ makes the test statistic $T_n$​​​ larger, this would lead us to reject more, reject when we should not. This is a serious mistake because we may conclude to $H_1$​​ when we should not.  So this test is the kind of test where you do not want to conclude to $H_1$.**

* We only have $K-1$​​​​​​​​​ degrees of freedom, since the asymptotic Gaussian vector we have actually lives in $K-1$​​​​​​​​ dimension not $K$​​​​​​​​ dimension. It lives on the linear space that's orthogonal to the $\begin{pmatrix}1\\1\\ \vdots \\ 1\end{pmatrix}$​​​​​​​​​​. **Having $K-1$​​​​ degrees of freedom is more conservative, since we have a smaller critical value $q_\alpha$​, so we are going to reject less.**

## 6. The Chi-Squared Test - Example Problems I

#### Chi-squared Test I

Let $\widehat{\mathbf{p}}$ denote the MLE for a categorical statistical model $( \{  a_1, \ldots , a_ K \} , \{ \mathbf{P}_{\mathbf{p}} \} _{\mathbf{p} \in \Delta _ K})$. Let $\mathbf{p}^*$ denote the true parameter. Then $\sqrt{n}(\widehat{\mathbf{p}} - \mathbf{p}^*)$ is asymptotically normal and
$$
n \sum _{i = 1}^ K \frac{ ( \widehat{ p_ i } - p_ i^*)^2 }{p_ i^*} \xrightarrow [n \to \infty ]{(d)} \chi _{K -1}^2.
$$
Consider the particular categorical distribution, where we have the statistical experiment $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\mathbf{p}}$ and associated statistical model $(\{ 1,2,3\} , \{  \mathbf{P}_{\mathbf{p}} \} _{\mathbf{p} \in \Delta _3})$. We will use the above fact to hypothesis test between the following null and alternative:
$$
H_0: \mathbf{p}^* = [1/3 \quad 1/3 \quad  1/3]^T \\
H_1: \mathbf{p}^* \neq [1/3 \quad 1/3 \quad  1/3]^T.
$$
Consider the test,
$$
\psi = \mathbf{1}\left( n \sum _{i = 1}^3 \frac{ ( \widehat{ p_ i } - \frac{1}{3})^2 }{1/3} >C \right),
$$
for a threshold $C$.

Compute the asymptotic p-value of the test $\psi$ on the data set
$$
\mathbf{x} = 1, 3, 1, 2, 2, 2, 1, 1, 3, 1, 1, 2.
$$
**Solution:**

Since $K=3$​ and $E = \{1,2,3\}$​,
$$
f_{\mathbf{p}}(i) = p_ i, \quad i = 1,2,3.
$$
Next,
$$
L_ n( X_1, \ldots , X_ n, \mathbf{p}) = \prod _{i = 1}^ n f_{\mathbf{p}}(X_ i) = p_1^{N_1} p_2^{N_2} p_3^{N_3}
$$
where 
$$
N_ i = \text {number of times} \,  \,  i \,  \,  \text {appears in } (X_1, \ldots , X_ n) , \quad i = 1,2, 3.
$$
Given the data, we define
$$
L_{12}(\mathbf{x}, \mathbf{p}) = p_1^ A p_2^ B p_3^ C
$$
where $A = N_1 = 6, B = N_2 = 4,$ and $C = N_3 = 2$.

Thus, the log likelihood is 
$$
\log L_ {12}(\mathbf{x}, \mathbf{p}) = 6 \log p_1 + 4 \log p_2 + 2 \log p_3.
$$
Recall the MLE is given by
$$
\widehat{\mathbf{p}}^{MLE}_ n = \text {argmax}_{\mathbf{p} \in \Delta _3} \log L_ n(X_1, \ldots , X_ n, \mathbf{p}).
$$
Hence,
$$
\nabla \log L_ n(\mathbf{x}, \mathbf{p}) = \begin{bmatrix}  \frac{6}{p_1} \\ \frac{4}{p_2} \\ \frac{2}{p_3} \end{bmatrix}.
$$
By the theory of **Lagrange multipliers**, one can show that the maximum occurs at the point $\mathbf{p}$​​ such that there exists $\lambda \neq 0$​ so that
$$
\nabla \log L_ n (X_1, \ldots , X_ n, \mathbf{p}) = \lambda \begin{bmatrix}  1 \\ 1 \\ 1 \end{bmatrix}.
$$
Hence,
$$
\nabla \log L_ n(\mathbf{x}, \mathbf{p}) = \begin{bmatrix}  \frac{6}{p_1} \\ \frac{4}{p_2} \\ \frac{2}{p_3} \end{bmatrix}\\
\begin{bmatrix}  \frac{6}{p_1} \\ \frac{4}{p_2} \\ \frac{2}{p_3} \end{bmatrix} = \lambda \begin{bmatrix}  1 \\ 1 \\ 1 \end{bmatrix}.
$$
Therefore,
$$
p_1 = \frac{6}{\lambda }, \,  \,  p_2 = \frac{4}{\lambda }, \,  \,  p_3 = \frac{2}{\lambda }.
$$
By the constraint $p_1 + p_2 + p_3 = 1$, we see that
$$
\lambda = 6 + 4 + 2 = 12.
$$
Therefore, the MLE is
$$
\widehat{\mathbf{p}}^{MLE}_{12} = \begin{bmatrix}  \frac{1}{2} \\ \frac{1}{3} \\ \frac{1}{6} \end{bmatrix}.
$$
Therefore the test statistic is
$$
n \sum _{i = 1}^3 \frac{ ( \widehat{ p_ i } - \frac{1}{3})^2 }{1/3} = 12\cdot 3 \left( \frac{1}{6^2} + 0 + \frac{1}{6^2} \right) = 2.
$$
By the asymptotic normality, we have
$$
n \sum _{i = 1}^3 \frac{ ( \widehat{ p_ i } - \frac{1}{3})^2 }{1/3} \xrightarrow [n \to \infty ]{(d)} \chi _2^2.
$$
Consulting the link provided, we see that if $X \sim \chi _2^2$ , then $P(X \geq 2) \approx 36.79 \%$. Hence, the asymptotic p-value for the test $\psi$ on this dataset is approximately equal to $0.3679$.

#### Playing Dice

You and your friend play dice games for fun, but one day you suspect that the die your friend uses is not fair. You will gather data and use the tools of hypothesis testing in this problem to provide a plausible answer as to whether or not the die is fair.

Your statistical model is $(\{ 1,2,3,4,5,6\} , \{  \mathbf{P}_{\mathbf{p}} \} _{\mathbf{p} \in \Delta _6})$. You roll the die $15$ times, writing the sample as random variables $X_1, \ldots , X_{15} \stackrel{iid}{\sim } \mathbf{P}_{\mathbf{p}^*}$ where $\mathbf{p}^*$ is the true parameter. Your null and alternative hypothesis are, respectively,
$$
H_0: \mathbf{p}^* = [1/6~ ~ 1/6~ ~ 1/6~ ~ 1/6~ ~ 1/6~ ~ 1/6]^ T\\
H_1: \mathbf{p}^* \neq [1/6~ ~ 1/6~ ~ 1/6~ ~ 1/6~ ~ 1/6~ ~ 1/6]^ T.
$$
Let $\widehat{\mathbf{p} }$​ denote the MLE for the true parameter $\mathbf{p}^*$. You use the following test statistic to test the hypotheses:
$$
T_ n = n \sum _{j = 1}^6 \frac{(\widehat{p}_ j - \frac{1}{6} )^2}{\frac{1}{6} }.
$$

1. What is the distribution does $T_n$​​​ converge to?

2. Use the test of the form
   $$
   \psi _ n = \mathbf{1}\left( T_ n > C \right).
   $$
   What value of $C$​​ should be chosen so that $\psi$ is a test of asymptotic level $5\%$?

3. Suppose you observe that data set
   $$
   5,6,1,6,4,1,2,4,6,6,1,6,6,3,5.
   $$
   Do you reject or fail to reject the null hypothesis that the die is fair?

**Solution:**

1. If the sample space consists of $K$ Elements, and $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\mathbf{p}^0}$, then
   $$
   T_ n = n \sum _{j = 1}^ K \frac{(\widehat{p }_ j - p_ j^0 )^2}{p_ j^0 } \xrightarrow [n \to \infty ]{(d)} \chi _{K -1}^2.
   $$
   Our sample space consists of $6$ elements (recall $E = \{ 1, 2,3,4,5,6\}$), so we conclude that the limiting distribution is $\chi_5^2$.

2. Consulting a table, we see that if $X \sim \chi _5^2$, then if $C=11.070$.
   $$
   P(X > C) = 0.05.
   $$
   Therefore,
   $$
   \lim _{n \to \infty } P_{H_0}[T_ n > 11.070] = 0.05.
   $$
   By definition, $\psi_n$ is a test with asymptotic level $5\%$.

3. The MLE is 
   $$
   \widehat{\mathbf{p} } = \frac{1}{15} [3~ ~  1~ ~  1~ ~  2~ ~  2~ ~  6]^ T.
   $$
   We compute that for this data set,
   $$
   T_{15} = 15\left( \frac{( \frac{3}{15} - \frac{1}{6} )^2}{1/6} + \frac{( \frac{1}{15} - \frac{1}{6} )^2}{1/6} + \frac{( \frac{1}{15} - \frac{1}{6} )^2}{1/6} + \frac{( \frac{2}{15} - \frac{1}{6} )^2}{1/6} + \frac{( \frac{2}{15} - \frac{1}{6} )^2}{1/6} + \frac{( \frac{6}{15} - \frac{1}{6} )^2}{1/6} \right)
    = 7
   $$
   Since $C = 11.070$​​, by the previous problem, $\psi$​ fails to reject on the given data set.

**Remark:** This is a rather surprising result given that the number $6$​​​​​ Has appeared an overwhelming $6$​​​​​ times out of $15$​​​ trials and the number $2$​​ and $3$​​ have each appeared only once. Without performing this test, one would have probably concluded that the die is likely not a fair die (would have rejected the null hypothesis).

## 7. The Chi-Squared Test for Two Modalities

Consider the $\chi^2$ test statistic for $K=2$:
$$
T_ n = n \sum _{j = 1}^2 \frac{(\widehat{p}_ j - p_ j^0 )^2}{p_ j^0 }.
$$
We can use this statistic in a chi-squared test with $1$ degree of freedom to determine, with an asymptotic level $\alpha$, whether the observed iid samples follow the distribution $\text {Ber}(p_2^0)$ under the null hypothesis $H_0$, with the sample space being the two values $a_1 = 0$ and $a_2=1$. The chi-squared test with asymptotic level $\alpha$ is
$$
\mathbf{1}\left\{  T_ n > q_\alpha \right\} ,
$$
where $q_\alpha$ is the $(1-\alpha)$-quantile of the chi-squared distribution with $1$ degree of freedom.

**This test is identical (asymptotically) to Wald's test of the Bernoulli statistical model with parameter $p$, null hypothesis $H_0: p = p_2^0$ and alternative hypothesis $H_1 : p \neq p_2^0$, where $p_2^0$, as defined above, is the probability of $a_2=1$​ under the null hypothesis.**

Wald's test in the above statement is:
$$
\displaystyle  \mathbf{1}\left\{  n \frac{\left(\widehat{p}_2 - p_2^0 \right)^2}{p_2^0\left(1 - p_2^0\right)} > q_\alpha \right\} ,
$$
where $q_\alpha$ is the $(1-\alpha)$-quantile of the chi-squared distribution with $1$ degree of freedom.

The chi-squared test statistic can be re-written as
$$
\begin{aligned}
T_n &=  n \sum _{j = 1}^2 \frac{(\widehat{p}_ j - p_ j^0 )^2}{p_ j^0 }\\
&= n \frac{(\widehat{p}_1 - p_1^0 )^2}{p_1^0 } + n\frac{(\widehat{p}_2 - p_2^0 )^2}{p_2^0 }\\
&= n \frac{((1-\widehat{p}_2) - (1-p_2^0) )^2}{1-p_2^0 } + n\frac{(\widehat{p}_2 - p_2^0 )^2}{p_2^0 }\\
&= n \frac{\left(\widehat{p}_2 - p_2^0 \right)^2 (p_2^0 + 1 - p_2^0)}{p_2^0\left(1 - p_2^0\right)}\\
&= n \frac{\left(\widehat{p}_2 - p_2^0 \right)^2}{p_2^0\left(1 - p_2^0\right)},
\end{aligned}
$$
which is the same as the test statistic for Wald's test.

## 8. Chi-Squared Test for a Family of Discrete Distributions

In the following problems, we will apply the $\chi^2$ goodness of fit test to determine whether or not a sample has a binomial distribution. 

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X\sim \mathbf{P}$ denote iid discrete random variables supported on $\{0,..., K\}$. We will decide between the following null and the alternative hypotheses:
$$
H_0:  \mathbf{P}\in \{  \text {Bin}(K, \theta ) \} _{\theta \in (0,1)}\\
H_1:  \mathbf{P}\notin \{  \text {Bin}(K, \theta ) \} _{\theta \in (0,1)},
$$
where the null hypothesis can be rephrased as
$$
H_0: \quad \text {there exists } \, \theta \in (0,1)\, \text {such that for all }\, j = 0, \ldots , K, \, \text {we have } P(X = j) = \binom {K}{j} \theta ^{j} (1 - \theta )^{K -j}.
$$
Let $(\{ 0, \ldots , K\} , \{  \text {Bin}(K, \theta ) \} _{\theta \in (0,1)})$ denote a binomial statistical model. Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Bin}(K, \theta ^*)$ for some unknown parameter $\theta ^* \in (0,1)$.

The PMF of $\text {Bin}(K, \theta )$ is
$$
j \mapsto \binom {K}{j} \theta ^ j (1 - \theta )^{K - j}
$$
for $j \in \{0, ..., K\}$​.

Therefore, the likelihood is given by
$$
\begin{aligned}
L_ n(X_1, \ldots , X_ n, \theta ) &= \prod _{i = 1}^ n \left(\binom {K}{X_ i} \theta ^{X_ i} (1 - \theta )^{K - X_ i} \right)\\
&=  \left( \prod _{i = 1}^ n \binom {K}{X_ i} \right) \theta ^{\sum _{i = 1}^ n X_ i} (1 - \theta )^{nK - \sum _{i = 1}^ n X_ i }.
\end{aligned}
$$
Taking the logarithm, we have
$$
\begin{aligned}
\log L_ n(X_1, \ldots , X_ n, \theta ) &= \log \left( \prod _{i = 1}^ n \binom {K}{X_ i} \right) + \left( \sum _{i = 1}^ n X_ i \right) \log \theta + \left( nK - \sum _{i = 1}^ n X_ i \right) \log (1 - \theta )\\
&= C + \left( \sum _{i = 1}^ n X_ i \right) \log \theta + \left( nK - \sum _{i = 1}^ n X_ i \right) \log (1 - \theta ).
\end{aligned}
$$
where $C$ does not depend on $\theta$.

To compute the MLE, we maximize the above with respect to the parameter $\theta$. We set the derivative to be $0$.
$$
0 = \frac{\sum _{i = 1}^ n X_ i}{\theta } - \frac{nK - \sum _{i = 1}^ n X_ i}{1 - \theta }.
$$
The above holds when
$$
p = \frac{1}{nK} \sum _{i = 1}^ n X_ i.
$$
Therefore, the right-hand side is the MLE for this statistical model.

#### $\chi^2$-Test for a Family of Distribution

Now, we return to the following more general statistical set-up.

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}$ denote iid discrete random variables supported on ${0,..., K}$. We will decide between the following null and alternative hypotheses.
$$
H_0:  \mathbf{P}\in \{  \text {Bin}(K, \theta ) \} _{\theta \in (0,1)}\\
H_1:  \mathbf{P}\notin \{  \text {Bin}(K, \theta ) \} _{\theta \in (0,1)},
$$
Let $f_\theta$​ denote the PMF of the distribution $\text {Bin}(K, \theta )$​, and let $\hat{\theta}$​ denote the MLE of the parameter $\theta$ from the previous problem.

Further, let $N_j$​ denote the number of times that $j (j \in \{0,1,..., K\})$​ appears in the data set $\, X_1, \ldots , X_ n\,$​ (So that $\sum _{j=0}^{K} N_ j =n$​) The $\chi^2$ test statistic for this hypothesis test is defined to be 
$$
T_ n := n\sum _{j =0}^ K \frac{\left( \frac{N_ j}{n} - {{f_{\widehat{\theta }}(j)}}  \right)^2}{{{f_{\widehat{\theta }}(j)}}  }.
$$
This statistic is different from before. Previously, under the null hypothesis, $\mathbf{P}(X=j)=p_ j\,$ for some fixed $p_j$. Here, instead, we use $f_{\widehat{\theta }}(j)\,$ to estimate $\mathbf{P}(X=j)\,$. This statistic still converges in distribution to a $\chi^2$​ distribution, but the number of degrees of freedom is smaller.

#### Degrees of Freedom for Test for a Family of Distribution

More generally, to test if a distribution $\mathbf{P}$​ is described by some member of a family of discrete distributions $\{  \mathbf{P}_{\theta } \} _{\theta \in \Theta \subset \mathbb {R}^ d}$​ where $\Theta \subset \mathbb {R}^ d$​ is $d$​-dimensional, with support $\{0,1,2,...,K\}$​ and PMF $f_\theta$​, i.e. to test the hypotheses:
$$
H_0: \mathbf{P}\in \{  \mathbf{P}_\theta \} _{\theta \in \Theta }\\
H_1: \mathbf{P}\notin \{  \mathbf{P}_\theta \} _{\theta \in \Theta }\\
$$
then if indeed $\mathbf{P}\in \{  \mathbf{P}_{\theta } \} _{\theta \in \Theta \subset \mathbb {R}^ d}$​ (i.e. the null hypothesis $H_0$ holds), and if in addition some technical assumption hold, then we have that
$$
T_ n:= n\sum _{j =0}^ K \frac{\left( \frac{N_ j}{n} - f_{\widehat{\theta }}(j) \right)^2}{ f_{\widehat{\theta }}(j) } \xrightarrow [n \to \infty ]{(d)} \chi ^2_{(K+1) - d - 1}.
$$
Note that $K+1$​​​ is the support size of $\mathbf{P}_\theta$​​​ (for all $\theta$​​).

In our example testing for a binomial distribution, the parameter $\theta$ is one-dimensional, i.e. $d=1$. Therefore, under the null hypothesis $H_0$, it holds that 
$$
T_ n \xrightarrow [n \to \infty ]{(d)} \chi ^2_{(K+1) - 1 - 1} = \chi ^2_{K-1}.
$$

> #### Exercise 88
>
> Consider the same statistical set-up as above. In particular, we have the test statistic
> $$
> T_ n := n \sum _{j =0}^ K \frac{\left( \frac{N_ j}{n} - f_{\widehat{\theta }}(j) \right)^2}{ f_{\widehat{\theta }}(j) }.
> $$
> where $\hat{\theta}$ is the MLE for the binomial statistical model $(\{ 0,1, \ldots , K\} , \{  \text {Bin}(K, \theta ) \} _{\theta \in (0,1)})$.
>
> We define our test to be
> $$
> \psi _ n = \mathbf{1}( T_ n > \tau ),
> $$
> where $\tau$​ is a threshold that you will specify. For the remainder of this page, we will assume that $K=3$​ (The sample space is $\{0,1,2,3\}$​).
>
> 1. What value of $\tau$​​ should be chosen so that $\psi_n$​​ is a test of asymptotic level $5\%$​​​?
>
> 2. Suppose we observe a data set consisting of $1000$​​ Observations as described in the following format: $N_i$​​, number of observations of $i$​):
>    $$
>    \begin{aligned}
>    i \quad & \quad N_i\\
>    0 \quad & \quad 339\\
>    1 \quad & \quad 455\\
>    2 \quad & \quad 180\\
>    3 \quad & \quad 26\\
>    \end{aligned}
>    $$
>    What is the value of the test statistic $T_n$​ for this data set? What is the p-value of this data set with respect to the test $\psi_{1000}$​? If $\psi_n$ is designed to have level $5\%$, would you reject or fail to reject on the given data set?
>
> **Solution:**
>
> 1. Since $K=3$​ and $d=1$​, we know that the limiting distribution of $T_n$​ is $\chi^2_2$​. Thus, the asymptotic level is the value $\tau$​ such that 
>    $$
>    \lim _{n \to \infty } P( T_ n > \tau ) = P( Z > \tau ) = 0.05
>    $$
>    Where $Z \sim \chi_2^2$. Hence, $\tau$ should be chosen to be $5.991$.
>
> 2. Observe that the MLE is given by
>    $$
>    \widehat{\theta } = \frac{1}{3 \cdot 1000} (455 + 2 \cdot 180 + 3 \cdot 26 ) \approx 0.29767.
>    $$
>    Thus for this data set,
>    $$
>    \begin{aligned}
>    T_n &= 1000 \cdot \bigg( \frac{\left(\frac{339}{1000} - \binom {3}{0} (0.2977^0) (0.7023)^{3 - 0} \right)^2}{\binom {3}{0} (0.2977^0) (0.7023)^{3 - 0} } + \frac{\left(\frac{455}{1000} - \binom {3}{1} (0.2977^1) (0.7023)^{3 - 1} \right)^2}{\binom {3}{1} (0.2977^1) (0.7023)^{3 - 1} } + \\
>    &\frac{\left(\frac{180}{1000} - \binom {3}{2} (0.2977^2) (0.7023)^{3 - 2} \right)^2}{\binom {3}{2} (0.2977^2) (0.7023)^{3 - 2} } + \frac{\left(\frac{26}{1000} - \binom {3}{3} (0.2977^3) (0.7023)^{3 - 3} \right)^2}{\binom {3}{3} (0.2977^3) (0.7023)^{3 - 3} } \bigg)\\
>    & \approx 0.8829
>    \end{aligned}
>    $$
>    The asymptotic p-value for this data set is given by
>    $$
>    \lim _{n \to \infty } P(T_ n > 0.8829) = P(Z > 0.8829).
>    $$
>    where $Z \sim \chi _2^2$. Consulting the suggested link, we see that $P(Z > 0.8829) \approx 0.6431$.
>
>    According to the golden rule of p-values, since $0.6431 > 0.05$​, we should **fail to reject** the null hypothesis that $X_1, ..., X_{1000}$​ are distributed as $\text {Bin}(3, \theta )$​ for some value of the parameter $\theta$​.

