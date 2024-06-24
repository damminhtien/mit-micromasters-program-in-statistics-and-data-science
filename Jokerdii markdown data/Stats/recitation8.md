# Recitation 8. (Review) Mean Squared Error

The MSE of an estimator is given by
$$
\text{mse}(\hat{\theta}) = \mathbb{E}(\hat{\theta} - \theta_0)^2
$$
where $\theta_0$​ is the true parameter in our model.

The **bias-variance decomposition** of the MSE is
$$
\begin{aligned}
\text{mse}(\hat{\theta}) &= \mathbb{E}(\hat{\theta} - \theta_0)^2\\
&= \mathbb{E}\hat{\theta}^2 + \mathbb{E}\theta_0^2 - 2 \mathbb{E}\hat{\theta} \theta_0\\
&= \text{var}(\hat{\theta}) + (\mathbb{E}\hat{\theta})^2 + 2 \mathbb{E}\hat{\theta}\theta_0\\
&= \text{var}(\hat{\theta}) + (\mathbb{E}\hat{\theta})^2 + \theta_0^2 - 2 \theta_0 \mathbb{E}\hat{\theta}\\
&= \text{var}(\hat{\theta}) + (-\theta + \mathbb{E \hat{\theta}})^2.\\
&= \text{var}(\hat{\theta}) + (\text{bias}(\hat{\theta}))^2.
 \end{aligned}
$$
For two unbiased estimators of $\theta$​, $\hat{\theta}_1$​ and $\hat{\theta}_2$​, the **relative efficiency** of $\hat{\theta}_1$​ versus $\hat{\theta}_2$ is
$$
\text{eff}(\hat{\theta}_1,\hat{\theta}_2) = {\text{var}(\hat{\theta}_1) \over \text{var}(\hat{\theta}_2)}.
$$
Small efficiency means the $\hat{\theta}_1$ is a much better estimator than $\hat{\theta}_2$.

1. Calculate the bias, variance and MSE for the following distributions and estimators

   a. $X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Poisson}(\lambda), \hat{\lambda}_1 = \overline{X_n}$.

   b. $X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Poisson}(\lambda), \hat{\lambda}_2 = X_1$.

   c. $X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Unif}([0,\theta]), \hat{\theta} = \max_i X_i$​​​.

   d. $X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Unif}([0,\theta]), \hat{\theta} = 2 \overline{X_n}$​​​.

   e. $X_1, ..., X_n \stackrel{iid}{\sim} f(x;\sigma) = {1\over 2 \sigma} \exp \left(- {|x| \over \sigma} \right), \hat{\sigma} = {\sum_i|X_i| \over n }$​​​.

2. What is the relative efficiency of (a) vs (b)? What about the unbiased estimator based on (c) vs (d)?

3. Find the minimum MSE shrinkage estimators of the mean and variance for the $\mathcal{N}(\mu, \sigma^2)$ distribution.

> **Solution:**
>
> 1. a.
>    $$
>    \mathbb{E}[\overline{X}_n] = {1 \over n } \sum^n_{i=1} \mathbb{E}(X_i) = \lambda\\
>    \text{var}(\overline{X_n}) = {1\over n^2} \sum^n_{i=1} \text{var}(X_i) = {\lambda \over n}\\
>    \text{mse}(\overline{X_n}) = {\lambda \over n} + 0 = {\lambda \over n}
>    $$
>    b. 
>    $$
>    \mathbb{E}[X_1] = \lambda\\
>    \text{var}(X_1) = \lambda\\
>    \text{mse}(\overline{X_n}) = \lambda + 0 = \lambda
>    $$
>    We see that $\hat{\lambda}_1$ will probably be a much better estimator of the parameter $\lambda$​​​ in this model than just using one of the $X_i$'s to estimate the $\lambda$​.
>
>    c. 
>
>    The CDF of $\hat{\theta}$ is given by
>    $$
>    \begin{aligned}
>    F(x) &= \mathbf{P}(\hat{\theta} \leq x)\\
>    &= \mathbf{P}(\max_i X_i \leq x)\\
>    &= (\mathbf{P}(X_i \leq x))^n\\
>    &= \left({x \over \theta}\right)^n
>    \end{aligned}
>    $$
>    where $x \in [0,\theta]$​​. The PDF is
>    $$
>    f(x) = F'(x) = {n x^{n-1} \over \theta^n}, \ x \in [0,\theta].
>    $$
>    We find
>    $$
>    \mathbb{E}[\hat{\theta}] = \int^{\theta}_0 {n x^n\over \theta^n} dx = {n \over n+1}{x^{n+1} \over \theta^n} |^\theta_0 = {n \over n+1} \theta
>    $$
>    and
>    $$
>    \mathbb{E}[\hat{\theta}^2] = \int^{\theta}_0 {n x^{n+1} \over \theta^n} dx = {n \over n+2} {x^{n+2} \over \theta^n} |^\theta_0 = {n \over n+2} \theta^2
>    $$
>    The MSE is
>    $$
>    \begin{aligned}
>    \text{mse}(\hat{\theta}) &= \text{var}(\hat{\theta}) + (\text{bias}(\hat{\theta}))^2\\
>    &= \left({n \over n+2} \theta^2 - \left( {n \over n+1} \theta \right)^2\right) + \left({1\over n+1} \theta\right)^2\\
>    &= \theta^2 \left[ {n \over n+2} - {n^2 \over (n+1)^2} + {1^2 \over (n+1)^2} \right] \\
>    &= \theta^2 \left[{n(n+1)^2 - n^2 (n+2) + (n+2) \over (n+2)^2(n+1)}\right]\\
>    &= \theta^2 {n+3 \over (n+2)^2(n+1)}
>    \end{aligned}
>    $$
>    d.
>    $$
>    \mathbb{E}[\hat{\theta}]= {2\over n}\sum^n_{i=1}\mathbb{E}[X_i] = 2 {\theta \over 2} = \theta\\
>    \text{var}(\hat{\theta})= {4 \over n^2} \sum^n_{i=1}\text{var}(X_i) = {4\theta^2 \over 12n} = {\theta^2 \over 3n}\\
>    \text{mse}(\hat{\theta}) = \text{var}(\hat{\theta}) + (\text{bias}(\hat{\theta}))^2 = {\theta^2 \over 3n} + 0 = {\theta^2 \over 3n}
>    $$
>    Although the $\hat{\theta} = \max_i X_i$​ is a biased estimator, the MSE of it is actually smaller than the MSE of $2\overline{X}_n$.
>
>    e. 
>    $$
>    \mathbb{E}[\hat{\sigma}] = {1\over n}\sum^n_{i=1} \mathbb{E}|X_i|
>    $$
>    We have
>    $$
>    \mathbb{E}|X_i| = \int^\infty_{-\infty} {|x| \over 2 \sigma} \exp(-|x|/\sigma)dx = \int^\infty_0 {x \over \sigma} \exp(-x/\sigma) dx = \sigma
>    $$
>    Thus $\mathbb{E}[\hat{\sigma}] = \sigma$.
>    $$
>    \text{var}(\hat{\sigma}) = {1\over n^2}\sum^n_{i=1} \text{var}(|X_i|)
>    $$
>    Notice,
>    $$
>    \mathbb{E}|X_i|^2 = \int^\infty_0 {x^2 \over \sigma }\exp(-x/\sigma) = \sigma^2  +\sigma^2 = 2 \sigma^2
>    $$
>    Thus, $\text{var}(\hat{\sigma}) = {\sigma^2 \over n}$​​.
>    $$
>    \text{mse}(\hat{\sigma}) = {\sigma^2 \over n} + 0 = {\sigma^2 \over n}
>    $$
>
> 2. For (a) and (b),
>    $$
>    \text{eff}(\hat{\lambda}_1, \hat{\lambda}_2) = {\text{var}(\hat{\lambda}_1) \over \text{var}(\hat{\lambda}_2)} = {{\lambda / n}\over \lambda} = {1\over n}
>    $$
>    Thus, $\hat{\lambda}_1$​​ is a much efficient estimator than $\hat{\lambda}_2$​​ when $n$ is large.
>
>    For (c) and (d),
>
>    The unbiased estimator based on (c) is
>    $$
>    \hat{\theta} = {n+1 \over n} \max_i X_i
>    $$
>    This estimator has variance
>    $$
>    \text{var}(\hat{\theta}) = \left({n+1 \over n}\right)^2 \text{var}(\hat{\theta}) = \left(n+1 \over n\right)^2 {n(n+1)^2 - n^2(n+2) \over (n+2)(n+1)^2 } \theta^2 = {1\over n(n+2)}\theta^2
>    $$
>    Thus, we have a relative efficiency of
>    $$
>    \text{eff}(\hat{\theta}_1,\hat{\theta}_2) = {\text{var}(\hat{\theta}_1) \over \text{var}(\hat{\theta}_2)} = {\theta^2/(n(n+1)) \over \theta^2/(3n)} = {3\over n+2}
>    $$
>    Thus, $\hat{\theta}_1$​​​​ is a much efficient estimator than $\hat{\theta}_2$​​​​ when $n$​ is large.
>
> 3. a. If $X_1, ..., X_n \stackrel{i.i.d.}{\sim} \mathcal{N}(\mu, \sigma^2)$​, then we know that $\overline{X}_n$​ is an unbiased​ estimator of $\mu$. We have
>    $$
>    \begin{aligned}
>    \text{MSE}(\overline{X_n}) &= \text{Var}(\overline{X}_n) + \text{Bias}(\overline{X_n})^2\\
>    &= {1\over n^2} \sum^n_{i=1}\text{Var}(X_i) + (\mu - \mu)^2\\
>    &= {\sigma^2 \over n}.
>    \end{aligned}
>    $$
>    Instead, consider the estimator $a\overline{X}_n, a \in (0, \infty)$.
>    $$
>    \begin{aligned}
>    \text{MSE}(a\overline{X}_n) &= \text{Var}(a \overline{X}_n) + \text{Bias}(a\overline{X})^2\\
>    &= a^2 {\sigma^2 \over n} +(a \mu - \mu)^2\\
>    &= a^2 ({\sigma^2 \over n} + \mu^2) - 2 a \mu^2 + \mu^2
>    \end{aligned}
>    $$
>    Since it is quadratic, it is minimized at
>    $$
>    \hat{a} = {2 \mu ^2 \over 2({\sigma^2 \over n} + \mu^2)} = {\mu^2 \over {\sigma^2 \over n} + \mu^2} < 1
>    $$
>    Plug it in the MSE equation
>    $$
>    \begin{aligned}
>    MSE(\hat{a} \overline{X}_n) & = \left( {\mu^2 \over {\sigma^2 \over n} + \mu^2}  \right)^2 ({\sigma^2 \over n} + \mu^2) - 2 \mu^2 \left( {\mu^2 \over {\sigma^2 \over n} + \mu^2}  \right) + \mu^2\\
>    &= {\mu^4 \over {\sigma^2 \over n} + \mu^2} - {2\mu^4 \over {\sigma^2 \over n} + \mu^2} + {\mu^2 \left({\sigma^2 \over n} + \mu^2\right) \over {\sigma^2 \over n} + \mu^2} \\
>    &= {\sigma^2 \over n}  \cdot {\mu^2 \over {\sigma^2 \over n} + \mu^2} \\
>    &= \hat{a}\ \ \text{MSE}(\overline{X}_n) \ <\text{MSE}(\overline{X}_n)
>    \end{aligned}
>    $$
>    The reason we call this a **shrinkage estimator** is that $\hat{a} < 1$​​​. So we are shrinking the sample mean a little bit toward $0$​​​​, and adding a little bit of bias. By adding this bias, we're actually decreasing the variance by a lot more than we add in the bias. This leads to a smaller MSE than we originally had with our unbiased estimator.
>
>    b. Now we will consider estimation of the variance for a $\mathcal{N}(0,\sigma^2)$​​ distribution. In this case, the unbiased estimator of the variance is given by
>    $$
>    \hat{\sigma}^2 = {1\over n}\sum^n_{i=1}X_i^2
>    $$
>    Since the distribution has a fixed mean parameter of $0$. We have
>    $$
>    \text{MSE}(\hat{\sigma}^2) = \text{Var}(\hat{\sigma}^2) = {1\over n^2} \sum^n_{i=1} \text{Var}(X_i^2) = {2\sigma^4 \over n}
>    $$
>    Repeating the shrinkage procedure as before, we find
>    $$
>    \begin{aligned}
>    \text{MSE}(\hat{\sigma}^2) &= a^2 {2\sigma^4 \over n} + ((1-a)\sigma^2)^2\\
>    &= \left( {2 \sigma^4 \over n} + \sigma^4\right) a^2 - 2 \sigma^4 a + \sigma^4
>    \end{aligned}
>    $$
>    This is minimized when
>    $$
>    \hat{a} = {\sigma^4 \over 2\sigma^4/n  +\sigma^4} = {1\over 2/n + 1} = {n \over 2+n}
>    $$
>    and it results in an MSE of
>    $$
>    \begin{aligned} 
>    \text{MSE}(\hat{\sigma}^2) &= \left( {2 \sigma^4 \over n} + \sigma^4\right) \left({n \over 2+n}\right)^2 - 2 \sigma^4 \left({n \over 2+n}\right) + \sigma^4\\
>    &= \sigma^4\left(\left({n \over 2 + n} \right) - {2n\over n+2} + 1 \right)\\
>    &= {2\sigma^4 \over 2 + n}
>    \end{aligned}
>    $$

