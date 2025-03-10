Problem set for Lec11-12.

# 1. Asymptotic Variance of MLE for Curved Gaussian

Let $X_1, ..., X_n$​​ be $n$​ i.i.d. random variables with distribution $\mathcal{N}(\theta, \theta)$​ for some unknown $\theta > 0$.

In the last homework, you have computed the MLE $\hat{\theta}$​ for $\theta$​ in terms of the sample averages of the linear and quadratic means, i.e. $\overline{X}_n$​ and $\overline{X^2_n}$​, and applied the CLT and delta method to find its asymptotic variance. 

In this problem, you will compute the asymptotic variance of $\hat{\theta}$ Via the Fisher Information.

1. Denoting the log likelihood for one sample by $\ell(\theta,x)$​, compute the second derivative $\,   \frac{d^2}{d \theta ^2} \ell (\theta , x)  \,$​.
2. Then, compute the Fisher information $\mathcal{I}(\theta)$​.
3. Finally, what does this tell us about the asymptotic variance of $\hat{\theta}$​?

> **Solution:**
>
> Let $\ell(\theta, x)$​ denote the log likelihood for one sample. Recall its first derivative
> $$
> \begin{aligned}
> \ell (\theta ,x) &= -\frac{1}{2} \left( \log (2) + \log (\pi ) + \log (\theta ) \right) - \left( \frac{1}{2 \theta } X^2 - X + \frac{1}{2} \theta \right)\\
> \Longrightarrow \frac{d}{d \theta } \ell (\theta ,x) &= - \frac{1}{2 \theta } + \frac{1}{2 \theta ^2} X^2 - \frac{1}{2}.
> \end{aligned}
> $$
> Differentiating one more time yields
> $$
> \frac{d^2}{d \theta ^2} \ell (\theta , x) = \frac{1}{2 \theta ^2} - \frac{x^2}{\theta ^3}.
> $$
> Since
> $$
> I(\theta ) =-\mathbb E\left[ \frac{d^2}{d \theta ^2} \ell (\theta , X) \right] = \frac{2 \theta + 1}{2 \theta ^2}.
> $$
> By the theorem about the asymptotic variance of the MLE from class, we finally have
> $$
> V(\hat\theta ) = I(\theta )^{-1} = \frac{2 \theta ^2}{(2 \theta + 1)}
> $$

# 2. Maximum Likelihood Estimators and Fisher Information

For each of the following distribution, compute the MLE based on $n$​ i.i.d. observations $X_1,...,X_n$​ and the Fisher information, if defined.

1. Let $X_ i \sim \textsf{Ber}(p),\ p \in (0, 1)$​, what is the MLE $\hat{p}$​, Fisher information $\mathcal{I}(p)$​, and the asymptotic variance $V(\hat{p})$​ of the MLE $\hat{p}$​.
2. Let $X_ i \sim \textsf{Poiss}(\lambda ), \lambda > 0,$​​ what is the MLE $\hat{\lambda}$​​, Fisher information $\mathcal{I}(\lambda)$​​, and the asymptotic variance $V(\hat{\lambda})$​​ of the MLE $\hat{\lambda}$​.
3. Let $X_ i \sim \textsf{Exp}(\lambda ),\ \lambda > 0,$ what is the MLE $\hat{\lambda}$, Fisher information $\mathcal{I}(\lambda)$, and the asymptotic variance $V(\hat{\lambda})$ of the MLE $\hat{\lambda}$​.
4. Let $X_ i \sim \mathcal{N}(\mu , \sigma ^2), \ \mu \in \mathbb {R}, \,  \sigma ^2 > 0,$​​​​ what is the MLE $\hat{\mu}$​​​, and $\widehat{\sigma^2}$​​​, Fisher information $\mathcal{I}(\lambda)$​​​, and the asymptotic variance $V(\widehat{\sigma^2})$​​​ of the MLE $\widehat{\sigma^2}$​​​​.
5. $X_i$ follows a shifted exponential distribution with parameters $a \in \R$ and $\lambda > 0$. What is the MLE $\hat{a}$ and $\hat{\lambda}$, Fisher information $\mathcal{I}(\lambda)$, and the asymptotic variance $V(\hat{\lambda})$ of the MLE $\hat{\lambda}$.

> **Solution:**
>
> 1. The likelihood for one sample can be written as
>    $$
>    L_1(X_1,p) = p^{X_1} (1-p)^{1-X_1}.
>    $$
>    That means that the log likelihood for one sample is
>    $$
>    \ell _1(X_1, p) = X_1 \ln (p) + (1-X_1) \ln (1-p),
>    $$
>    and for $n$​​ samples this yields
>    $$
>    \ell _ n(X_1, \dots , X_ n, p) = \ln (p) \sum _{i=1}^{n} X_ i + \ln (1-p) \left(n - \sum _{i=1}^{n} X_ i \right).
>    $$
>    Differentiating with respect to $p$ yields
>    $$
>    \frac{\partial }{\partial p} \ell _ n(p) = \frac{1}{p} \sum _{i=1}^{n} X_ i - \frac{1}{1-p} \left(n - \sum _{i=1}^{n} X_ i\right).
>    $$
>    Setting this to zero to find the MLE $\hat{p}$​ then gives
>    $$
>    \begin{aligned}
>    0&=(1-\hat p) \sum _{i=1}^{n} X_ i - \hat p \left( n - \sum _{i=1}^{n} X_ i \right)\\
>    \iff \hat{p} &= \frac{1}{n} \sum _{i=1}^{n} X_ i = \overline{X}_ n.
>    \end{aligned}
>    $$
>    That this is indeed the global maximum can be verified by checking the concavity of the log likelihood, which in turn can be seen from the negativity of the second derivative.
>
>    The second derivative for one sample is
>    $$
>    \frac{\partial ^2}{\partial p^2} \ell _1(p) = -\frac{X_1}{p^2}-\frac{1-X_ i}{(1 - p)^2} < 0,
>    $$
>    and by $\mathbb{E}[X_i]=p$, we obtain
>    $$
>    I(p) = -\mathbb E\left[ \frac{\partial ^2}{\partial p^2} \ell _1(p) \right] = \frac{1}{p} + \frac{1}{1-p} = \frac{1}{p(1-p)}.
>    $$
>    Take the inverse of this to obtain the (asymptotic) variance: $V(\hat{p}) = p(1-p)$​.
>
> 2. Each $X_i$ has distribution
>    $$
>    \mathbf{P}_\lambda (X = k) = e^{-\lambda } \frac{\lambda ^ k}{k!}, \quad k \in \mathbb {N}.
>    $$
>    The likelihood for one sample can be written as
>    $$
>    L_1(X_1,\lambda ) = e^{-\lambda } \frac{\lambda ^{X_1}}{X_1!}.
>    $$
>    That means that the log likelihood for one sample is
>    $$
>    \ell _1(X_1, \lambda ) = -\lambda + X_1 \ln (\lambda ) - \ln (X_1!),
>    $$
>    and for $n$​ samples this yields
>    $$
>    \ell _ n(X_1, \dots , X_ n, p) = -n \lambda + n \overline{X}_ n \ln (\lambda ) - \sum _{i=1}^{n} \ln (X_ i!).
>    $$
>    Differentiating with respect to $\lambda$ yields
>    $$
>    \frac{\partial }{\partial \lambda } \ell _ n(\lambda ) = -n + n \overline{X}_ n \frac{1}{\lambda }
>    $$
>    Setting this to zero to find the MLE $\hat{\lambda}$​​ then gives
>    $$
>    \hat\lambda = \overline{X}_ n.
>    $$
>    That this is indeed the global maximum can be verified by checking the concavity of the log likelihood, which in turn can be seen from the negativity of the second derivative.
>
>    The second derivative for one sample is
>    $$
>    \frac{\partial ^2}{\partial \lambda ^2} \ell _1(\lambda ) = - \frac{X_ i}{\lambda ^2} < 0,
>    $$
>    and by $\,   \mathbb E[X_ i] = \lambda  \,$​, we obtain
>    $$
>    I(\lambda ) = -\mathbb E\left[ \frac{\partial ^2}{\partial \lambda ^2} \ell _1(\lambda ) \right] = \frac{\lambda }{\lambda ^2} = \frac{1}{\lambda }.
>    $$
>    Take the inverse of this to obtain the (asymptotic) variance: $V(\hat{p}) = \lambda$​​.
>
> 3. Each $X_1$ has density
>    $$
>    f_{\lambda }(x)= \lambda e^{-\lambda x}, \quad x > 0.
>    $$
>    The likelihood for one sample can be written as
>    $$
>    L_1(X_1,\lambda ) = \lambda e^{-\lambda X_1}.
>    $$
>    The log likelihood for one sample is
>    $$
>    \ell _1(X_1, \lambda ) = \ln (\lambda ) - \lambda X_1,
>    $$
>    and for $n$ samples this yields
>    $$
>    \ell _ n(X_1, \dots , X_ n, p) = n \ln (\lambda ) - n \lambda \overline{X}_ n.
>    $$
>    Differentiating with respect to $\lambda$ yields
>    $$
>    \frac{\partial }{\partial \lambda } \ell _ n(\lambda ) = \frac{n}{\lambda } - n \overline{X}_ n.
>    $$
>    Setting this to zero to find the MLE $\hat{\lambda}$​ then gives
>    $$
>    \hat\lambda = \frac{1}{\overline{X}_ n}.
>    $$
>    That this is indeed the global maximum can be verified by checking the concavity of the log likelihood, which in turn can be seen from the negativity of the second derivative.
>
>    The second derivative for one sample is
>    $$
>    \frac{\partial ^2}{\partial \lambda ^2} \ell _1(\lambda ) = -\frac{1}{\lambda ^2}.
>    $$
>    and hence
>    $$
>    I(\lambda ) = -\mathbb E\left[ \frac{\partial ^2}{\partial \lambda ^2} \ell _1(\lambda ) \right] = \frac{1}{\lambda ^2}.
>    $$
>    Take the inverse of this to obtain the (asymptotic) variance: $V(\widehat{\sigma^2}) = \lambda^2$​.
>
> 4. Each $X_1$ Has density
>    $$
>    f_{\mu , \sigma ^2}(x)= \frac{1}{\sqrt{2 \pi \sigma ^2}} \exp \left( -\frac{(x - \mu )^2}{2 \sigma ^2} \right).
>    $$
>    The likelihood for one sample can be written as
>    $$
>    L_1(X_1,\mu ,\sigma ^2) = \frac{1}{\sqrt{2 \pi \sigma ^2}} \exp \left( -\frac{(X_1-\mu )^2}{2 \sigma ^2} \right).
>    $$
>    The log likelihood for one sample is
>    $$
>    \ell _1(X_1, \mu , \sigma ^2) = -\frac{1}{2} \left( \ln (2) + \ln (\pi ) + \ln (\sigma ^2) \right) - \frac{(X_1 - \mu )^2}{2 \sigma ^2},
>    $$
>    and for $n$ samples this yields
>    $$
>    \ell _ n(X_1, \dots , X_ n, \mu , \sigma ^2) = -\frac{n}{2} \left( \ln (2 \pi ) + \ln (\sigma ^2) \right) - \sum _{i=1}^{n} \frac{(X_ i - \mu )^2}{2 \sigma ^2}.
>    $$
>    Differentiating with respect to $\mu$ yields
>    $$
>    \frac{\partial }{\partial \mu } \ell _ n(\mu , \sigma ^2) = \sum _{i=1}^{n} \frac{X_ i - \mu }{2 \sigma ^2}.
>    $$
>    Setting this to zero to find the MLE $\hat{\mu}$​ then gives
>    $$
>     \hat\mu = \overline{X}_ n.
>    $$
>    Similarly, differentiating the log likelihood with respect to $\sigma^2$​​, we find
>    $$
>    \frac{\partial }{\partial \sigma ^2} \ell _ n(\mu , \sigma ^2) = -\frac{n}{2 \sigma ^2} + \sum _{i=1}^{n} \frac{(X_ i - \mu )^2}{2 \sigma ^4}.
>    $$
>    Setting this to zero gives
>    $$
>    \widehat{\sigma ^2} = \frac{1}{n} \sum _{i=1}^{n} (X_ i - \hat\mu )^2 = \frac{1}{n} \sum _{i=1}^{n} (X_ i - \overline{X}_ n)^2 = \overline{X_ n^2} - \overline{X}_ n^2.
>    $$
>    That this is indeed the global maximum can be verified by checking the concavity of the log likelihood, which in turn can be seen from the negative definiteness of the Hessian.
>
>    We compute the second derivatives:
>    $$
>    \begin{aligned}
>    \frac{\partial ^2}{\partial \mu ^2} \ell _1(\mu , \sigma ^2) &= -\frac{1}{\sigma ^2},\\
>    \frac{\partial ^2}{\partial \mu \partial (\sigma ^2)} &= - \frac{1}{(\sigma ^2)^2} (X_1 - \mu ),\\
>    \frac{\partial ^2}{\partial (\sigma ^2)^2} &= \frac{1}{2 (\sigma ^2)^2} - \frac{1}{(\sigma ^2)^3} (X_1 - \mu )^2,
>    \end{aligned}
>    $$
>    from where negative definiteness can be checked by testing $\,   \operatorname {tr}H \ell _1 < 0  \,$​​ and $\,   \mathrm{det}H \ell _1 > 0  \,$​. Moreover,
>    $$
>    \begin{aligned}
>    I(\mu , \sigma ^2) &= - \begin{pmatrix}  \mathbb E\left[ \frac{1}{\sigma ^2} \right] &  \frac{\mathbb E[X_1 - \mu ]}{(\sigma ^2)^2}\\ \frac{\mathbb E[X_1 - \mu ]}{(\sigma ^2)^2} &  \mathbb E\left[ \frac{1}{2 (\sigma ^2)^2} - \frac{(X_1 - \mu )^2}{(\sigma ^2)^3} \right] \end{pmatrix}\\
>    &= \begin{pmatrix}  \frac{1}{\sigma ^2} &  0\\ 0 &  \frac{1}{2 \sigma ^4} \end{pmatrix}. 
>    \end{aligned}
>    $$
>    Take the inverse of this to obtain the (asymptotic) variance: $V(\widehat{\sigma^2}) = 2\sigma^4$​​.​
>
> 5. Each $X_i$ has density
>    $$
>    f_{a, \lambda }(x) = \lambda e^{-\lambda (x-a)} \mathbf{1}\{ x \geq a\} , \quad x \in \mathbb {R}.
>    $$
>    The likelihood for one sample can be written as
>    $$
>    L_1(X_1,a,\lambda ) = \lambda e^{-\lambda (X_ i - a)} \mathbf{1}\{ X_ i \geq a\} .
>    $$
>    The likelihood for $n$​​ samples is
>    $$
>    L_ n(X_1, \dots , X_ n, a, \lambda ) = \lambda ^ n \exp \left(-\lambda \sum _{i=1}^{n} (X_ i - a)\right) \mathbf{1}\{  \min X_ i \geq a\} .
>    $$
>    Consider two cases, we note that if $a > \min{X_i}$, then $\mathbb{1}\{\min X_i \geq a\}=0$ and hence 
>
>    $$
>    \,   L_ n(X_1, \dots , X_ n, a, \lambda ) = 0  \,
>    $$
>
>    On the other hand, if $a \leq \min X_i$​, then $\mathbb{1}\{\min X_i \geq a\}$, and
>    $$
>    L_ n(X_1, \dots , X_ n,a, \lambda ) = e^{n \lambda a} \lambda ^ n \exp \left( -\lambda \sum _{i=1}^{n} X_ i \right),
>    $$
>    which is an increasing function of $a$. Hence, for any fixed value of $\lambda$, the MLE for $a$ is
>    $$
>    \hat a = \min _{1 \leq i \leq n} X_ i.
>    $$
>     For this value of $a$, we can now optimize the log likelihood
>    $$
>    \ln L_ n(X_1, \dots , X_ n, \hat a, \lambda ) = n \ln (\lambda ) - \lambda (n \overline{X}_ n - n \hat a), \\
>    \frac{\partial }{\partial \lambda } \ln L_ n(\hat a, \lambda ) = \frac{n}{\lambda } - n (\overline{X}_ n - \hat a).
>    $$
>    
>    Setting the first derivative to zero then yields
>    $$
>    \hat\lambda = \frac{1}{\overline{X}_ n - \min X_ i}.
>    $$
>    For this example, the Fisher information is not well-defined since the support of the distribution depends on the parameter $a$.

# 3. Method of Moments Estimators

For each of the following distributions, give the method of moments estimator in terms of the sample average $\overline{X_n}$​​ and $\overline{X^2_n}$​, assuming we have access to $n$​ i.i.d. observations $X_1,..., X_n$​. In other words, express the parameters as functions of $\mathbb{E}[X_1]$​ and $\mathbb{E}[X_1^2]$​ and then apply these functions to $\overline{X_n}$ and $\overline{X_n^2}$​.​

1. Let $X_ i \sim \textsf{Ber}(p), \ p \in (0, 1)$​​​​, what is the method of moments estimator $\hat{p} \ $?
2. Let $X_ i \sim \textsf{Poiss}(\lambda ), \ \lambda > 0$​​​​ what is the method of moments estimator $\hat{\lambda} \ $?​​​​
3. Let $X_ i \sim \textsf{Exp}(\lambda ), \ \lambda > 0,$​​ what is the method of moments estimator $\hat{\lambda} \ $?​
4. Let $X_ i \sim \mathcal{N}(\mu , \sigma ^2), \ \mu \in \mathbb {R}, \,  \sigma ^2 > 0$​​​, what is the method of moments estimator $\hat{\mu}$​​ and $\hat{\sigma} \ $​​​?
5. Let $X_i$​​ Follows a shifted exponential distribution with parameters $a \in \R$​​ And $\lambda > 0$​​. what is the method of moments estimator $\hat{a}$​​ and $\hat{\lambda} \ $?

> **Solution:**
>
> 1. For Bernoulli variables, we have
>    $$
>    \mathbb E_ p[X_1] = p,
>    $$
>    hence,
>    $$
>    \hat p = \overline{X}_ n.
>    $$
>
> 2. For a Poisson random variable, we have
>    $$
>    \mathbb E_{\lambda }[X_1] = \lambda ,
>    $$
>    hence,
>    $$
>    \hat\lambda = \overline{X}_ n.
>    $$
>
> 3. For an Exponential random variable, we have
>    $$
>    \mathbb E_\lambda [X_1] = \frac{1}{\lambda },
>    $$
>    so
>    $$
>    \lambda = \frac{1}{\mathbb E_\lambda [X_1]}.
>    $$
>    Hence, the method of moments estimator is
>    $$
>    \hat\lambda = \frac{1}{\overline{X}_ n}.
>    $$
>
> 4. For a Gaussian distribution, we have
>    $$
>    \begin{aligned}
>    \mathbb E_{\mu , \sigma ^2}[X_1] &= \mu \\
>    \mathbb E_{\mu , \sigma ^2}[X_1^2] &= \textsf{Var}_{\mu , \sigma ^2}(X_1) + \mathbb E[X_1]^2 = \mu ^2 + \sigma ^2,
>    \end{aligned}
>    $$
>    which we can invert to obtain
>    $$
>    \begin{aligned}
>    \mu &= \mathbb E_{\mu , \sigma ^2}[X_1]\\
>    \sigma^2 &= \mathbb E_{\mu , \sigma ^2}[X_1^2] - \mathbb E_{\mu , \sigma ^2}[X_1]^2.
>    \end{aligned}
>    $$
>    Plugging in the estimator $\overline{X_n}$​ and $\overline{X^2_n}$​ then yields
>    $$
>    \begin{aligned}
>    \hat{\mu} &= \overline{X_n}\\
>    \widehat{\sigma^2} &= \overline{X_n^2} - \overline{X_n}^2.
>    \end{aligned}
>    $$
>
> 5. Since $X_1$ Is a shifted exponential random variable
>    $$
>    \mathbb E_{a, \lambda }[X_1] = \mathbb E_{0, \lambda }[a + X_1] = a + \frac{1}{\lambda },
>    $$
>    and
>    $$
>    \begin{aligned}
>     \mathbb E_{a, \lambda }[X_1^2] &= \textsf{Var}_{0, \lambda }(X_1) + \mathbb E_{a, \lambda }[X_1]^2\\
>     &= \frac{1}{\lambda ^2} + \left( \frac{1}{\lambda } + a \right)^2.
>    \end{aligned}
>    $$
>    That means
>    $$
>    a = \mathbb E_{a, \lambda }[X_1] - \frac{1}{\lambda },
>    $$
>    and plugging this into the equation for the second order moment, we obtain
>    $$
>    \begin{aligned}
>    \frac{1}{\lambda ^2} + \left( \frac{1}{\lambda } + \mathbb E_{a, \lambda }[X_1] - \frac{1}{\lambda } \right)^2  &=  \mathbb E_{a, \lambda }[X_1^2]\\
>    \iff {1\over \lambda} &= \left( \mathbb E_{a, \lambda }[X_1^2] - \mathbb E_{a, \lambda }[X_1]^2 \right)^{1/2}\\
>    \iff {\lambda} &=  \left( \mathbb E_{a, \lambda }[X_1^2] - \mathbb E_{a, \lambda }[X_1]^2 \right)^{-1/2},
>    \end{aligned}
>    $$
>    which plugged back into the first equation yields
>    $$
>    a = \mathbb E_{a, \lambda }[X_1] - \left( \mathbb E_{a, \lambda }[X_1^2] - \mathbb E_{a, \lambda }[X_1]^2 \right)^{1/2}.
>    $$
>    Hence, the method of moment estimators are
>    $$
>    \begin{aligned}
>    \hat\lambda =&\left( \overline{X_ n^2} - (\overline{X}_ n)^2 \right)^{-1/2}\\
>    \hat a =& \overline{X}_ n - \left( \overline{X_ n^2} - (\overline{X}_ n)^2 \right)^{1/2}. 
>    \end{aligned}
>    $$

# 4. Maximum Likelihood Estimation, Tests, and Confidence Intervals

Let $\, X_1, \dots , X_ n\stackrel{iid}{\sim } X\,$​ be distributed i.i.d. with probability density function
$$
f_\theta (x)=(x/\theta ^2)\exp (-x^2/2\theta ^2)\, \mathbf{1}(x\ge 0), \theta >0.
$$

1. Let $l(\theta )=\ln L(X_1,\ldots ,X_ n,\theta )$ denote the log likelihood. Find the critical point of $l(\theta)$. (The critical point is unique because KL divergence is definite.). Find the second derivative $l^{\prime \prime }=\frac{d^2l}{d\theta ^2}\,$ of $l(\theta)$. Determine whether the critical point is a global maximum or a global minimum, or neither of $l(\theta)$ in the domain $\theta >0$? What can you conclude about the maximum likelihood estimator $\hat{\theta}$ for $\theta$?

2. What is the Fisher information $I(\theta)$​​​ of the random variables $X_i$​?

3. Use the theorem for the MLE to write down the asymptotic distribution of the MLE $\hat{\theta}$​. Specifically, give an asymptotic $95\%$​ C.I. $\, \mathcal{I}_{\text {plug-in}}\,$​ for $\theta$ using the plug-in method. 

4. Use the results from the previous parts to give a test with asymptotic level $\alpha$ for testing
   $$
   H_0: \theta = 1 \quad \mbox{ v.s. } \quad H_1: \theta \neq 1 .
   $$
   Suppose $n=100$​​ and the data gives $\overline{X}_ n=1.5$​​ and $\overline{X_ n^2}=4.0$​. Find the $p$-value associated to this data for this hypothesis test.

> **Solution:**
>
> 1. Given $f_\theta (x)=(x/\theta ^2)\exp (-x^2/2\theta ^2)\mathbf{1}(x\ge 0), \theta >0.$​
>
>    The log-likelihood is
>    $$
>    l_ n(\theta ) \, =\, \ln \prod _ i^ n f_\theta (x_ i)=\sum _{i=1}^ n \ln x_ i -2n\ln \theta -\frac{1}{2\theta ^2}\sum _{i=1}^{n} (x_ i)^2
>    $$
>    Now, find the critical point of $\, \ln L(x_1,\ldots ,x_ n, \theta )\,$​ (there is a unique one because the KL divergence is definite):
>    $$
>    \begin{aligned}
>    \frac{dl_ n}{d\theta } &=-\frac{2n}{\theta }+\frac{\sum _{i=1}^{n} (x_ i)^2}{\theta ^3}\, =\, 0\\
>    \iff \theta &= \sqrt{\frac{\sum _{i=1}^{n} (x_ i)^2}{2n}}.
>    \end{aligned}
>    $$
>    Check that the critical point is indeed a maximum of $l_n(\theta)$:
>    $$
>    \begin{aligned}
>    \frac{d^2l_ n}{d\theta ^2} &= \frac{2n}{\theta ^2}-3\frac{\sum _{i=1}^{n} (x_ i)^2}{\theta ^4}\, =\, \frac{1}{\theta ^2}\left(2n-3\frac{\sum _{i=1}^{n} (x_ i)^2}{\theta ^2}\right)\\
>    \left.\frac{d^2l_ n}{d\theta ^2}\right|_{\theta =\sqrt{\frac{\sum _{i=1}^{n} (x_ i)^2}{2n}}} &=\frac{2n}{\sum _{i=1}^{n} (x_ i)^2}\left(2n-6n\right)\\
>    &=-{8n^2}{\sum _{i=1}^{n} (x_ i)^2}<0.
>    
>    \end{aligned}
>    $$
>    This means that the critical point we found is a local maximum.
>
>    Finally, check that the critical point is a global maximum. Since $l'_n(\theta)$​​ is defined for all $\theta > 0$​, and there is only one critical point, it follows that this critical point is a global maximum in $\theta > 0$​. (The function $l_n(\theta)$​ is strictly increasing to the left of the critical point and strictly decreasing to the right of the critical point.) Hence, the MLE of $\theta$ is
>    $$
>    \widehat{\theta } = \sqrt{\frac{\overline{X_ n^2}}{2}}.
>    $$
>
> 2. Setting $n=1$​​ in the expression for $l''_n(\theta)$​ computed above, we get
>    $$
>    l_1^{\prime \prime }(\theta ) = \frac{2}{\theta ^2}-\frac{3x^2}{\theta ^4}.
>    $$
>    This gives Fisher information $I(\theta)$:
>    $$
>    I(\theta )\, =\, -\mathbb E(l_1^{\prime \prime }(\theta )) = -\frac{2}{\theta ^2}+\frac{3}{\theta ^4}\mathbb E[x^2].
>    $$
>    It remains to compute the second moment $\, \mathbb E[x^2]$:
>    $$
>    \begin{aligned}
>    \, \mathbb E[x^2] &= \int _0^\infty \frac{x^3}{\theta ^2} e^{-\frac{x^2}{2\theta ^2}}\, dx\\
>    &=\int _0^\infty (x^2)\left( \frac{x}{\theta ^2} e^{-\frac{x^2}{2\theta ^2}}\right)\, dx\\
>    &= \left.Cx^2e^{-\frac{x^2}{2\theta ^2}}\right|_0^\infty + \int _0^\infty (2x)\left(e^{-\frac{x^2}{2\theta ^2}}\right)\, dx\qquad (\text {Integration by part})\\
>    &= 0+2\theta ^2\left[-e^{-\frac{x^2}{2\theta ^2}} \right]_0^\infty\\
>    &= 2\theta ^2.
>    \end{aligned}
>    $$
>    Plugging this back into the expression for the Fisher information, we got
>    $$
>    I(\theta )\, =\, \frac{4}{\theta ^2}.
>    $$
>
> 3. Since the asymptotic variance is given by $I^{-1}(\theta )=\frac{\theta ^2}{4}$​, a plug-in C.I. at confidence level  $95\%$ is
>    $$
>    \begin{aligned}
>    \mathcal{I} &= \left[\hat{\theta }-\frac{q_{0.025}}{\sqrt{n I}},\,  \hat{\theta }+\frac{q_{0.025}}{\sqrt{n I}}\right]\\
>    &= \left[\hat{\theta }-\frac{q_{0.025}}{\sqrt{n}}\frac{\hat{\theta }}{2},\,  \hat{\theta }+\frac{q_{0.025}}{\sqrt{n}}\frac{\hat{\theta }}{2}\right]
>    \end{aligned}
>    $$
>
> 4. The desired test is
>    $$
>    \Psi =\mathbf{1}\left(|T_ n|>q_{\alpha /2}\right)\quad \text {where } T_ n
>    $$
>    where $\theta_0=1$ is the value under the null hypothesis, and with $n=100, \overline{X}_n=1.5$ And $\overline{X_ n^2}=4.0, \hat{\theta }=\sqrt{\frac{\overline{X_ n^2}}{2}}\, =\,  \sqrt{2},\,$and $I(\theta _0)=\frac{4}{\theta _0^2}=4$. This gives the associated $p$-value of
>    $$
>    \begin{aligned}
>    2\left(1-\Phi (T_ n)\right) &= 2\left(1-\Phi \left(\sqrt{n I(\theta _0)}\left(\hat{\theta }-1\right)\right)\right)\\
>    &= 2\left(1-\Phi \left(\sqrt{(100)(4)}\left(\sqrt{2}-1\right)\right)\right)
>    \end{aligned}
>    $$
>    Hence, for any test with level larger than this expression, the test will reject the null hypothesis.

# 5. Censored data

In a given population, $n$ individuals are sampled randomly, with replacement, and each sampled individual is asked whether his/her salary is greater than some fixed threshold $z$. Assume that the salary of a randomly chosen individual has the exponential distribution with unknown parameter $\lambda$. Asking whether the salary overcomes a given threshold rather than directly asking for the salary increases the number people that are willing to answer and decreases the number of mistakes in the collected answers.

Denote by $\,  X_1,\ldots ,X_ n \,$​​​ the binary responses of the $n$​​ sampled individuals, so that $\,   X_ i \in \{ 0, 1\}   \,$​. We call the $X_i$ **censored data**.

1. What kind of distribution do the $X_i$​​​'s follow? Give the parameter of this distribution in terms of $\lambda$​ and $z$:
2. Let $\overline{X}_n$ be the proportion of sampled individuals whose response was $1$ (Corresponding to Yes). Convince yourself that $\overline{X}_n$​ is asymptotically normal. What is its asymptotic variance?
3. Find a function $f$​​ such that $\,  f(\overline{X}_ n) \,$​​ is a consistent estimator of $\lambda$​.
4. Convince yourself that $\,  f(\overline{X}_ n) \,$​ Is asymptotically normal and compute its asymptotic variance.
5. What equation must $z$​ satisfy in order to minimize the asymptotic variance computed in (4)? Write the equation in the form $g_\lambda(z)=z$​.​
6. Let $Y_1, ..., Y_n$ be the salaries of the $n$ sampled people. If one could actually observe $Y_1, ..., Y_n$, what would be the Fisher information of $Y, I_Y(\lambda)$, depending on $\lambda$​?
7. In the model where only the $X_i$​'S are observed (with fixed threshold $z$​), what is the Fisher information $I_X(\lambda)$​​​?
8. Compare $\,  I_ Y(\lambda ) \,$​​ and $\,  I_ X(\lambda ) \,$​. How to interpret this in this model?

> **Solution:**
>
> 1. If $Y_1, ..., Y_n$ denote the salaries of the sampled individuals, then
>    $$
>    Y_ i \sim \textsf{Exp}(\lambda ), \quad 1 \leq i \leq n, 
>    $$
>    and
>    $$
>    X_ i = \mathbf{1}\{ Y_ i \geq z\} , \quad 1 \leq i \leq n.
>    $$
>    Hence, $X_i$ follows a Bernoulli distribution with parameter
>    $$
>    \mu (\lambda ) = p(\lambda ) = \mathbb E[X_1] = \mathbf{P}_\lambda (Y_ i \geq z) = e^{-\lambda z}.
>    $$
>
> 2. $\overline{X}_n$​ is just the sample average and hence asymptotically normal by the CLT.
>
>    As a Bernoulli variable, the variance of $X_i$ is
>    $$
>    \textsf{Var}(X_ i) = p(\lambda ) (1-p(\lambda )) = e^{-\lambda z} (1 - e^{-\lambda z}).
>    $$
>    Hence, we have
>    $$
>    \sqrt{n} (\overline{X}_ n - e^{-\lambda z}) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, e^{-\lambda z} (1 - e^{-\lambda z})).
>    $$
>
> 3. By the LLN, we have
>    $$
>    \overline{X}_ n \xrightarrow [n \to \infty ]{\mathrm{\mathbf{P}}} \mathbb E[X_1] = e^{-\lambda z}.
>    $$
>    Hence, we can solve for $\lambda$​ with a continuous function,
>    $$
>    \lambda = -\frac{1}{z} \ln (\mathbb E[X_1]),
>    $$
>    and obtain a consistent estimator by setting
>    $$
>    f(\overline{X}_ n) = -\frac{1}{z} \ln (\overline{X}_ n).
>    $$
>
> 4. Since we have
>    $$
>    \sqrt{n} (\overline{X}_ n - e^{-\lambda z}) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, e^{-\lambda z} (1 - e^{-\lambda z}))
>    $$
>    by Delta method, we obtain
>    $$
>    \sqrt{n}(f(\overline{X}_ n) - f(e^{-\lambda z})) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, (f'(e^{-\lambda z}))^2 e^{- \lambda z}(1 - e^{-\lambda z})),
>    $$
>    with
>    $$
>    f(u) = -\frac{1}{z} \ln (u).
>    $$
>    Computing the first derivative yields
>    $$
>    f'(u) = -\frac{1}{zu}, \quad \text {so } f'(e^{-\lambda z}) = -\frac{1}{z e^{-\lambda z}}.
>    $$
>    Plugging this into the above Delta Method formula gives
>    $$
>    \sqrt{n}(f(\overline{X}_ n) - \lambda )) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, e^{2 \lambda z} e^{- \lambda z}(1 - e^{-\lambda z}) \frac{1}{z^2}),
>    $$
>    so the asymptotic variance is
>    $$
>    V(f(\overline{X}_ n)) = \frac{e^{\lambda z} - 1}{z^2}.
>    $$
>
> 5. Differentiating the asymptotic variance yields
>    $$
>    V'(z) = \frac{2 + e^{\lambda z}(-2 + \lambda z)}{z^{3}}.
>    $$
>    We solve for stationarity by setting $\,   V'(z) = 0  \,$​, which is equivalent to
>    $$
>    \begin{aligned}
>    0 &=2 + e^{\lambda z}(-2 + \lambda z)\\
>    z&=\frac{2}{\lambda } (1 - e^{-\lambda z}).
>    \end{aligned}
>    $$
>    Since
>    $$
>    \lim _{z \rightarrow 0} \frac{e^{\lambda z} - 1}{z^2} = \infty,\\
>     \lim _{z \rightarrow \infty } \frac{e^{\lambda z} - 1}{z^2} = \infty,
>    $$
>    one of the solutions to
>    $$
>    z = \frac{2}{\lambda } (1 - e^{-\lambda z})
>    $$
>    will have to be the global minimizer of $V$. Hence, we can set $g_\lambda(z)$ to be the right hand side above. Note that we could also rearrange this equation and then apply a logarithm
>    $$
>    \begin{aligned}
>    \frac{2-\lambda z}{2} &=e^{-\lambda z}\\
>    \frac{\ln \left(\frac{2}{2-\lambda z}\right)}{\lambda }  &= z
>    \end{aligned}
>    $$
>    Hence, a different answer for $g_\lambda (z)$​ is the left hand side above.
>
>    In the following, we show that there is only one solution apart from $z=0$.
>
>    Let
>    $$
>    h(z) = z - \frac{2}{\lambda } (1 - e^{-\lambda z}).
>    $$
>    Then $h(0) = 0$ and 
>    $$
>    h'(z) = 1 - 2 e^{-\lambda z}.
>    $$
>    The function $h'$ has a unique zero at
>    $$
>    z^\ast = -\frac{1}{\lambda } \ln \left( \frac{1}{2} \right).
>    $$
>    Hence, $h$​​ is first monotonically decreasing from $0$​​ and then strictly monotonically increasing. That means there can only be a unique crossing point with $0$​ apart from $z=0$​.​
>
> 6. The likelihood for one sample can be written as
>    $$
>    L_1(Y_1,\lambda ) = \lambda e^{-\lambda Y_1}.
>    $$
>    That means that the log likelihood for one sample is
>    $$
>    \ell _1(Y_1, \lambda ) = \ln (\lambda ) - \lambda Y_1.
>    $$
>    The second derivative is then given by
>    $$
>    \frac{\partial ^2}{\partial \lambda ^2} \ell _1(\lambda ) = -\frac{1}{\lambda ^2}.
>    $$
>    and hence
>    $$
>    I(\lambda ) = -\mathbb E\left[ \frac{\partial ^2}{\partial \lambda ^2} \ell _1(\lambda ) \right] = \frac{1}{\lambda ^2}.
>    $$
>
> 7. The likelihood for one sample can be written as
>    $$
>    L_1(X_1,\lambda ) = e^{-\lambda z X_1}(1 - e^{-\lambda z})^{1 - X_1}
>    $$
>    That means that the log likelihood for one sample is
>    $$
>    \ell _1(X_1, \lambda ) = -\lambda z X_1 + (1-X_1) \ln (1 - e^{-\lambda z})
>    $$
>    Its first derivative is
>    $$
>    \frac{\partial }{\partial \lambda } \ell _1(X_1, \lambda ) = -z X_1 + \frac{z e^{-\lambda z}(1-X_1)}{1 - e^{-\lambda z}}.
>    $$
>    The second derivative is then given by
>    $$
>    \frac{\partial ^2}{\partial \lambda ^2} \ell _1(X_1, \lambda ) = -\frac{z^2(1-X_1)e^{\lambda z}}{(e^{\lambda z}-1)^2},
>    $$
>    and hence,
>    $$
>    \begin{aligned}
>    I(\lambda) &= -\mathbb E\left[ \frac{\partial ^2}{\partial \lambda ^2} \ell _1(\lambda ) \right]\\
>    &= \displaystyle  \frac{(1 - e^{-\lambda z})z^2}{(e^{\lambda z} - 1)(1 - e^{-\lambda z})}\\
>    &= \frac{z^2}{(e^{\lambda z} - 1)}.
>    \end{aligned}
>    $$
>
> 8. $\,   I_ Y(\lambda ) \geq I_ X(\lambda )  \,$​ for all $\lambda$. 
>
>    In order to show this, we need to show 
>    $$
>    e^{u} - 1 - u^2 \geq 0, \quad \text {for all } u > 0,
>    $$
>    By setting $u = \lambda z$.
>
>    We know
>    $$
>    \exp (u) - 1 \geq u, \quad \text {for all } u > 0,
>    $$
>    and since $u^2 > u$​ for $u \in (0,1)$, we have
>    $$
>    \exp (u) - 1 \geq u^2, \quad \text {for } u \in (0,1).
>    $$
>    **Interpretation:**
>
>    The actual data always provides a better estimate.
>
>    This means that in terms of asymptotic statistical performance, the actualy observations beat the censored data, which is what we expected. On the other hand, if the actual data is not available (or at a much lower sample size), it might still be better to use the $X_i$.

# 6. Maximum Likelihood Estimation for a Multivariate Standard Normal

Let $\,  \mathbf{X}_1,\ldots ,\mathbf{X}_ n \stackrel{i.i.d.}{\sim } \mathcal{N}(\mathbf{\mu },\mathbf{1})  \,$​​​, where $\mu \in \R^d$​​ and $\mathbf{1}$​ is the $d \times d$​ identity matrix. (The $X_i$​ are random vectors.)

Recall the PDF defining the distribution $\mathcal{N}(\mu, \mathbf{1})$ is
$$
f(\mathbf{x}) =\frac{1}{(2\pi )^{d/2}} \exp \left(-\frac{1}{2}(\mathbf{x}-\mu )^ T\mathbf{1} (\mathbf{x}-\mu )\right)
$$

1. What is the likelihood function $\,  L(\mathbf{X}_1, \dots , \mathbf{X}_ n, \mathbf{\mu }) \,$​​ for $\mu$?
2. Compute the maximum likelihood estimator $\,  \hat\mu _{MLE} \,$​ for $\mu$​.
3. What is the distribution of $\,  \hat{\mu }_{MLE} \,$​?
4. What is the asymptotic variance of $\,  \mathbf{A}\hat{\mu }_{MLE} \,$​​? (here, A is a fixed $m \times d$​ matrix)
5. What is the asymptotic variance of $\,  \left\|  \hat{\mu }_{MLE} \right\| ^2 \,$​?

> **Solution:**
>
> 1. The likelihood function is
>    $$
>    \begin{aligned}
>    L(\mathbf{X}_1, \dots , \mathbf{X}_ n, \mathbf{\mu }) &= \prod _{i=1}^ n \frac{1}{(2\pi )^{d/2}} \exp (-\frac{1}{2}(\mathbf{x}_ i-\mu )^ T\mathbf{1}(\mathbf{x}_ i-\mu )\\
>    &= \prod _{i=1}^ n \frac{1}{(2\pi )^{d/2}} \exp (-\frac{1}{2}\| \mathbf{x}_ i-\mu \| _2^2)\\
>    &=(2\pi )^{-nd/2} \exp (-\frac{1}{2}\sum _{i=1}^ n\| \mathbf{x}_ i-\mu \| _2^2)
>    \end{aligned}
>    $$
>
> 2. The log likelihood is
>    $$
>    \ell (\mu ) = \frac{nd}{2}\ln 2\pi - \frac{1}{2}\sum _{i=1}^ n\| \mathbf{x}_ i-\mu \| _2^2
>    $$
>    The gradient of the log likelihood function is
>    $$
>    \nabla \ell (\mu ) = \sum _{i=1}^ n(\mathbf{x}_ i - \mu )
>    $$
>    Setting the gradient to zero
>    $$
>    \begin{aligned}
>    \sum _{i=1}^ n(\mathbf{x}_ i - \mu ) &= 0 \\
>    \sum _{i=1}^ n\mathbf{x}_ i- n\mu &= 0 \\
>    \mu &= \frac{1}{n}\sum _{i=1}^ n\mathbf{x}_ i\\
>    \hat\mu _{MLE} &= \bar{X}_n
>    \end{aligned}
>    $$
>
> 3. When the distribution of the population is normal, then the distribution of the sample mean is also normal. For a normal population distribution with mean $\mu$​ and variance $\sigma^2$, the distribution of the sample mean is normal, with mean $\mu$ and variance ${\sigma^2 \over n}$​. So in this multivariate case,
>    $$
>    \hat{\mu }_{MLE} \sim \mathcal{N}(\mu , \frac{1}{n}\mathbf{1})
>    $$
>
> 4. $\,  \mathbf{A}\hat{\mu }_{MLE} \in \mathbb {R}^ m \,$​​, so its variance is actually a $m \times m$​ covariance matrix
>    $$
>    \begin{aligned}
>    \textsf{Cov}(\mathbf{A}\hat{\mu }_{MLE}) &= \mathbf{A}\textsf{Cov}(\hat{\mu }_{MLE})\mathbf{A}^ T\\
>    &=  \mathbf{A}\frac{1}{n}\mathbf{1} \mathbf{A}^ T\\
>    &= \frac{1}{n}\mathbf{A}\mathbf{A}^ T
>    \end{aligned}
>    $$
>    Therefore, the asymptotic covariance is the covariance of $\sqrt{n}\left(\mathbf{A}\hat{\mu }_{MLE}\right)$​​, which is equal to $\mathbf{A}\mathbf{A}^ T$​.
>
> 5. Define the function $\,  g(\mathbf{X}) = \mathbf{X}^ T \mathbf{X} \,$​​ (i.e. $g(\mathbf{X})$​ is the squared norm of a vector $\mathbf{X}$).
>    $$
>    \begin{aligned}
>    g(\mathbf{X}) &= \mathbf{X}^ T \mathbf{X}\\
>    \nabla g(\mathbf{X}) &= 2\mathbf{X}
>    \end{aligned}
>    $$
>    We know from (3) that 
>    $$
>    \hat{\mu }_{MLE} \sim \mathcal{N}(\mu , \frac{1}{n}\mathbf{1})
>    $$
>    So
>    $$
>    \sqrt{n}(\hat{\mu }_{MLE} - \mu ) \sim \mathcal{N}(0, \mathbf{1})
>    $$
>    Note that this is stronger than saying that convergence in distribution.
>
>    By multivariate delta method,
>    $$
>    \sqrt{n}(g(\hat{\mu }_{MLE}) - g(\mu )) \xrightarrow [n\rightarrow \infty ]{(d)}\mathcal{N}(0, \nabla g(\mu )^ T\mathbf{1}\nabla g(\mu ))=\mathcal{N}(0, (2\mu )^ T (2\mu ))=
>    \mathcal{N}(0, 4\left\|  \mu  \right\| ^2)
>    $$
>    Therefore, the asymptotic variance is $\,  4\left\|  \mu  \right\| ^2 \,$​.

