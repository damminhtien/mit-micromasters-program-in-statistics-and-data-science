Problem set for Lec13-14.

# 1. Implicit hypothesis testing

Given $n$ i.i.d. samples $\,   X_1, \dots , X_ n \sim \mathcal{N}(\mu , \sigma ^2)  \, $ with $\mu \in \R$ and $\sigma^2 > 0$, we want to find a test with asymptotic level $5\%$ for the hypotheses
$$
H_0 \colon \mu \ge \sigma \quad \text {vs} \quad H_1 \colon \mu < \sigma .
$$

1. Define the MLE
   $$
   \hat\mu = \bar X_ n, \quad \widehat{\sigma ^2} = \frac{1}{n} \sum _{i=1}^{n} (X_ i - \bar X_ n)^2.
   $$
   Give a function $g(x,y)$​ such that
   $$
   g(\hat\mu , \widehat{\sigma ^2}) \xrightarrow [n \to \infty ]{\mathrm{\mathbf{P}}} \mu - \sigma .
   $$

2. What is the asymptotic variance $\,   V(g(\hat\mu , \widehat{\sigma ^2}))\,$​of $\,   g(\hat\mu , \widehat{\sigma ^2})  \,$​​ that you found in (1)?

3. Using the result in (2) together with a plug-in estimator for the asymptotic variance, give a test for 
   $$
   H_0 \colon \mu \ge \sigma \quad \text {vs} \quad H_1 \colon \mu < \sigma .
   $$
   that is with asymptotic level $5\%$ and of the form
   $$
     \psi = \mathbf{1} \{  f(\hat\mu , \widehat{\sigma ^2}) > 0\} ,
   $$
   where
   $$
   f(\hat\mu , \widehat{\sigma ^2}) = - T(\hat\mu , \widehat{\sigma ^2}) - q
   $$
   for some function $T$ And $q > 0$.

   Find $\,   f(\hat\mu , \widehat{\sigma ^2}) \,$​​.

4. Using the same test as in (3), give the (asymptotic) p-value of the test given observation $\hat{\mu}$​ and $\hat{\sigma}^2$​.

5. What is the (asymptotic) p-value if the sample size is $n=100,\,   \hat\mu = 3.28  \,$and$\,   \widehat{\sigma ^2} = 15.95  \,$?

   At level $10\%$, do you reject $H_0$? At level $5\%$, do you reject $H_0$?

> **Solution:**
>
> 1. Simply set
>    $$
>    g(x,y) = x - \sqrt{y}.
>    $$
>    By the consistency of the MLE and continuity of $g$, we get
>    $$
>    g(\hat\mu , \widehat{\sigma ^2}) \xrightarrow [n \to \infty ]{} g(\mu , \sigma ^2) = \mu - \sigma .
>    $$
>
> 2. By the **Theorem giving asymptotic normality for MLE**, we have
>    $$
>    \sqrt{n} \begin{pmatrix}  \hat\mu \\ \widehat{\sigma ^2} \end{pmatrix} - \sqrt{n} \begin{pmatrix}  \mu \\ \sigma ^2 \end{pmatrix} \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}\left( \begin{pmatrix}  0\\ 0 \end{pmatrix}, I(\mu , \sigma ^2)^{-1} \right),
>    $$
>    where $\,   I(\mu , \sigma ^2)  \,$ denotes the Fisher information that we computed earlier to be
>    $$
>    I(\mu , \sigma ^2) = \begin{pmatrix}  \frac{1}{\sigma ^2} &  0 \\ 0 &  \frac{1}{2 \sigma ^4} \end{pmatrix}.
>    $$
>    Hence,
>    $$
>    \sqrt{n} \begin{pmatrix}  \hat\mu \\ \widehat{\sigma ^2} \end{pmatrix} -\sqrt{n} \begin{pmatrix}  \mu \\ \sigma ^2 \end{pmatrix} \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}\left( \begin{pmatrix}  0\\ 0 \end{pmatrix}, \begin{pmatrix}  \frac{1}{\sigma ^2} &  0 \\ 0 &  \frac{1}{2 \sigma ^4} \end{pmatrix}^{-1} \right).
>    $$
>    Now, defining
>    $$
>    g \colon \mathbb {R}\times (0, \infty ) \to \mathbb {R}, \quad (x, y) \mapsto x - \sqrt{y},
>    $$
>    We can compute
>    $$
>    \nabla g (x, y) = \begin{pmatrix}  1 \\ - \frac{1}{2 \sqrt{y}}. \end{pmatrix}
>    $$
>    Then, apply the **multivariate Delta method** to obtain
>    $$
>    \sqrt{n}\left(\hat\mu - \sqrt{\widehat{\sigma ^2}} - (\mu - \sigma )\right) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, \nabla g(\mu , \sigma ^2)^ T I(\mu , \sigma ^2)^{-1} \nabla g(\mu , \sigma ^2)) = \mathcal{N}\left(0, \frac{3}{2} \sigma ^2\right).
>    $$
>    That means
>    $$
>    V\left(g\left(\hat\mu , \widehat{\sigma ^2}\right)\right) = \frac{3}{2} \sigma ^2.
>    $$
>
> 3. By **Slutsky's Theorem**, we know that
>    $$
>    \frac{\sqrt{n}}{\sqrt{\frac{3}{2} \widehat{\sigma ^2}}} (\hat\mu - \sqrt{\widehat{\sigma ^2}} - (\mu - \sigma )) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0,1).
>    $$
>    Therefore, set
>    $$
>    T = \sqrt{n} \frac{\hat\mu - \sqrt{\widehat{\sigma ^2}}}{\sqrt{\frac{3}{2} \widehat{\sigma ^2}}},
>    $$
>    and
>    $$
>    \psi = \mathbf{1}\{  - T - q > 0\} ,
>    $$
>    For some $q > 0$​​. If $\mu = \sigma$​​, the above means that we reject $H_0$​ if $T < -q$, which has probability
>    $$
>    \mathbf{P}_{\mu , \sigma ^2}(T < -q) \xrightarrow [n \to \infty ]{} 1 - \Phi (q).
>    $$
>    To achieve asymptotic level $5\%$​​​​​​​​​​, we therefore must set $q$​​​​​​​​​​ to be at least $q_{5\%}$​​​​​​​​​​. It turns out that this value is sufficient. Indeed, if $\mu > \sigma$​​​​​​​ (or equivalently, $\mu - \sigma>0$​​​​​​), then by the **LLN** $T$​​​​ has mean approaching $\infty$​​​​ due to the extra $\sqrt{n}$​​​ scaling:
>    $$
>    T = T_ n(\hat\mu , \widehat{\sigma ^2}) \to +\infty , \text { as } \quad n \to \infty ,
>    $$
>    so in that case
>    $$
>    \mathbf{P}_{\mu , \sigma ^2}(T < -1.65) \xrightarrow [n \to \infty ]{} 0.
>    $$
>    Hence the (asymptotic) supremum of rejecting $H_0$ over $(\mu ,\sigma ^2) \in \Theta _0$ is exactly $0.05$ if we set the threshold to be $q_{5\%}$. All in all, we have found a hypothesis test with asymptotic level $5\%$ of the form
>    $$
>    \psi \{  f(\hat\mu , \widehat{\sigma ^2}) > 0\} ,
>    $$
>    where
>    $$
>    f(\hat\mu , \widehat{\sigma ^2}) = -\sqrt{n} \frac{\hat\mu - \sqrt{\widehat{\sigma ^2}}}{\sqrt{\frac{3}{2} \widehat{\sigma ^2}}} - 1.65.
>    $$
>
> 4. By the same considerations as in (3), we only have to control the level under the assumption $\mu = \sigma$. Looking for a p-value means that we are looking for the smallest $\alpha$ such that the test with level $\alpha$ would have rejected the null-hypothesis. Note that in our notation, this is often an infimum, so we might not be rejecting the null-hypothesis at the p-value $\alpha$, but at any $\alpha + \epsilon, \epsilon > 0$.
>
>    As the asymptotic normality result in (3), if $\mu=\sigma$​​, we have
>    $$
>    \mathbf{P}_{\mu , \sigma ^2}(T < -q) \xrightarrow [n \to \infty ]{} 1 - \Phi (q).
>    $$
>    That means if we are looking for
>    $$
>    \alpha (T) = \inf \{ \alpha : \exists q > 0 \text { such that } T < -q \text { and } \alpha = 1 - \Phi (q)\} .
>    $$
>    By the monotonicity of $\Phi$, this comes down to
>    $$
>    \alpha (T) = 1 - \Phi (-T).
>    $$
>    Plugging in the form we found for $T$​ in (3) yields
>    $$
>    \text {p-value} = 1 - \Phi \left( -\sqrt{n} \frac{\hat\mu - \sqrt{\widehat{\sigma ^2}}}{\sqrt{\frac{3}{2} \widehat{\sigma ^2}}} \right).
>    $$
>
> 5. We compute 
>    $$
>    T = \sqrt{n} \frac{\hat\mu - \sqrt{\widehat{\sigma ^2}}}{\sqrt{\frac{3}{2} \widehat{\sigma ^2}}} \approx -1.46,
>    $$
>    Which leads to a p-value of roughly $0.07$​. 
>
>    This means that at $10\%$​, we can reject $H_0$, while at $5\%$, we cannot.

# 2. Student's T Test

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X \sim \mathcal{N}(\mu _1, \sigma _1^2)$​. Consider the null and alternative hypotheses
$$
H_0: \mu_1 = 5\\
H_1: \mu_1 \neq 5
$$

1. Assume that $\mu_1$ is not known, but $\sigma^2$ is known. The test statistic $T_n'$ for the likelihood ratio test associated to the above hypothesis can be expressed in terms of $n$, $\bar{X}_n$, and $\sigma_1^2$. What is $T_n'$?

2. If $\sigma_1^2$ were unknown and we used the estimator $\widetilde{\sigma _1^2} = \frac{1}{n-1}\sum _{i} (X_ i - \overline{X}_ n)^2$ in both log-likelihoods, what would be the distribution of $\sqrt{T_ n'}$​ under the null hypothesis?

3. Let $Y_1, \ldots , Y_ m \stackrel{iid}{\sim } Y \stackrel{iid}{\sim } N(\mu _2, \sigma _2^2)$​ denote another sample, and assume that $X$​'S are independent of the $Y$​'s. What is the distribution of $\overline{X}_ n - \overline{Y}_ m$​?

4. Recall that $X_1, \ldots , X_ n \stackrel{iid}{\sim } N(\mu _1, \sigma _1^2)$, and the two samples are independent of one another. Consider the null and alternative hypotheses
   $$
   H_0: \mu_1 \leq \mu_2\\
   H_1: \mu_1 > \mu_2
   $$
   What is the test statistic $T_n$ for the two-sample student's T test associated to $H_0$ and $H_1$?

5. Suppose we observe $\overline{X}_ n = 6.2, \overline{Y}_ m = 6, \hat{\sigma _1}^2 = 0.1$, and $\hat{\sigma _2}^2 = 0.2$ with $n=50$ and $m=50$.

   Using the Welch-Satterthwaite formula, what is the approximate number of degrees of freedom for the test statistic $T_n$?

   What is the p-value for this test?

> **Solution:**
>
> 1. Recall that the MLE for a Gaussian statistical model is $(\overline{X}_ n, \hat{\sigma }^2)$.
>
>    Therefore, by the definition of the likelihood-ratio test,
>    $$
>    \begin{aligned}
>    T_n' &= 2 \left( \ell (X_1, \ldots , X_ n ; \overline{X}_ n, \hat{\sigma }^2) - \ell (X_1, \ldots , X_ n ; 5, \hat{\sigma }^2) \right)\\
>    & = 2 \left( \frac{-1}{2 \hat{\sigma }^2} \sum _{i = 1}^ n (X_ i - \overline{X}_ n)^2 + \frac{1}{2 \hat{\sigma }^2} \sum _{i =1 }^ n (X_ i - 5)^2 \right)\\
>    &= \frac{1}{\hat{\sigma }^2} \left(\sum _{i = 1}^ n ( - X_ i^2 + 2 X_ i \overline{X}_ n - \overline{X}_ n^2 + X_ i^2 - 10 X_ i + 25) \right)\\
>    &= \frac{1}{\hat{\sigma }^2} \left(2n \overline{X}_ n^2 - n \overline{X}_ n^2 - 10 n \overline{X}_ n + 25 n\right)\\
>    &= \frac{n}{\hat{\sigma }^2} \left(\overline{X}_ n^2 - 10 \overline{X}_ n + 25 \right)\\
>    &= \frac{n}{\sigma ^2} \left(\overline{X}_ n - 5\right)^2.
>    \end{aligned}
>    $$
>
> 2. Observe that
>    $$
>    \sqrt{T_ n'} = \frac{\sqrt{n}}{\sigma } |\overline{X}_ n - 5|.
>    $$
>    Plugging in the estimator for $\sigma_1^2$, since
>    $$
>    \frac{\sqrt{n}}{\widetilde{\sigma _1}} (\overline{X}_ n - 5) \sim t_{n-1},
>    $$
>    We conclude that $\sqrt{T_n'}= |t_{n-1}|$.
>    
> 3. Since $X_1, \ldots , X_ n, Y_1, \ldots , Y_ m$​ are mutually independent, we know that $\overline{X}_ n - \overline{Y}_ m$​ will have a normal distribution. It remains to compute the mean and variance.
>
>    By linearity of expectation,
>    $$
>    \mathbb {E}[\overline{X}_ n - \overline{Y}_ m] = \mu _1 - \mu _2
>    $$
>    By independence, the variances are additive, so
>    $$
>    \text {Var}(\overline{X}_ n - \overline{Y}_ m) = \text {Var}(\overline{X}_ n) + \text {Var}(\overline{Y}_ m) = \frac{\sigma _1^2}{n} + \frac{\sigma _2^2}{m}.
>    $$
>    Therefore, the distribution of $\overline{X}_ n - \overline{Y}_ m$ is $N\left(\mu _1 - \mu _2, \frac{\sigma _1^2}{n} + \frac{\sigma _2^2}{m}\right)$.
>
> 4. Under the null hypothesis, we observe that
>    $$
>    \mathbf{P}\left( \frac{\overline{X}_ n - \overline{Y}_ m - (\mu _1 - \mu _2)}{ \sqrt{\frac{\hat{\sigma _1}^2}{n} + \frac{\hat{\sigma _2}^2}{m}} } > \tau \right) \leq \mathbf{P}\left( \frac{\overline{X}_ n - \overline{Y}_ m}{\sqrt{ \frac{\hat{\sigma _1}^2}{n} + \frac{\hat{\sigma _2}^2}{m} }} > \tau \right)
>    $$
>    Therefore, we define the test statistic to be 
>    $$
>    T_ n = \frac{\overline{X}_ n - \overline{Y}_ m}{\sqrt{ \frac{\hat{\sigma _1}^2}{n} + \frac{\hat{\sigma _2}^2}{m} }}.
>    $$
>
> 5. Applying to the WS-formula, under $H_0$​, $T_n$​ is approximately distributed as $t_{88}$​ because
>    $$
>    \frac{\left( \frac{0.1}{50} + \frac{0.2}{50} \right)^2}{ \frac{0.1^2}{50^2(50-1)} + \frac{0.2^2}{50^2(50-1)} } \approx 88.2
>    $$
>    Hence, the approximate number of degrees of freedom for the test statistic is $88$​.
>
>    For the second question, we compute
>    $$
>    T_ n = \frac{6.2 - 6}{\sqrt{\frac{0.1}{50} + \frac{0.2}{50}}} \approx 2.582.
>    $$
>    Consulting a table for the student's T distribution, we observe that $P(t_{88} > 2.582 ) \approx 0.0057$. Therefore,  the p-value for this test is ${0.0057}$.
>

# 3. Likelihood Ratio Test

We consider a sample $X_1, \ldots , X_ n \stackrel{\text {iid}}{\sim } \text {ShiftExp}(\lambda , a)$​​, where $\text {ShiftExp}(\lambda , a)$​​ is a continuous probability distribution with parameters $\lambda > 0$, $a \in \R$ and PDF
$$
f_{\lambda , a}(x) = \lambda e^{-\lambda (x - a)} \mathbf{1}_{x \geq a}.
$$

1. What is the likelihood function $L(X_1, \ldots , X_ n ;\lambda , a)$​​ for the shifted exponential statistical model?

2. Let $(\hat{\lambda }, \hat{a})$ denote the MLE for the shifted exponential model. What is $\hat{a}$​? What is $\hat{\lambda}$?

3. While we cannot formally take the log of zero, it makes sense to define the log-likelihood of a shifted exponential to be
   $$
   \ell (\lambda , a) = (n \ln \lambda - \lambda \sum _{i = 1}^ n (X_ i - a)) \mathbf{1}_{\min _ i(X_ i) \geq a} + (-\infty )\mathbf{1}_{\min _ i(X_ i) < a} .
   $$
   Keep in mind that the likelihood is $0$​ when $\min _ i(X_ i) < a$​​, so that the log-likelihood is infinite and negative.

   Assume now that $a$​ is known and that $a=0$. Consider the hypotheses
   $$
   H_0: \lambda = 1 \quad \text{vs} \quad H_1: \lambda \neq 1
   $$
   What is the likelihood-ratio test statistic $T_n$​?

   Assume that Wilk's theorem applies. What is the distribution of $T_n$?

4. We assume that $\lambda =1$ and is known. The parameter $a \in \R$ is now unknown.

   As in the previous problem, you should use the following definition of the log-likelihood:
   $$
   \ell (\lambda , a) = (n \ln \lambda - \lambda \sum _{i = 1}^ n (X_ i - a)) \mathbf{1}_{\min _ i(X_ i) \geq a} + (-\infty )\mathbf{1}_{\min _ i(X_ i) < a} .
   $$
   Consider the following null and alternative hypotheses:
   $$
   \displaystyle  H_0 : a \leq 1 \quad \text {vs} \quad H_1 : a > 1.
   $$
   What is the log-likelihood ratio test statistic $\widetilde{T_ n}$ for the above hypotheses? Note that if we observe $\min _ i(X_ i) < 1$, then we should clearly fail to reject the null. Furthermore, the restricted and the unrestricted likelihoods for such samples are equal, and therefore have $\widetilde{T_ n} = 0$. Hence, we should assume $\min _ i(X_ i) \ge 1$. 

5. What is the distribution of $\hat{a} = \min _{i = 1, \ldots , n}(X_ i)$​ assuming that $a = 1$ and $\lambda =1$​?

   Recall the test statistic $\widetilde{T_ n} $ from (4). Suppose that $n=100$ and $\widetilde{T_{100}} = 1.03$. What is the p-value associated to this observation.

> **Solution:**
>
> 1. By definition, the likelihood is computed to be
>    $$
>    \begin{aligned}
>    L(X_1, \ldots , X_ n; \lambda , a) &= \prod _{i = 1}^ n \lambda e^{-\lambda (X_ i - a)} \mathbf{1}_{X_ i \geq a}\\
>    &= \lambda ^ n \exp \left( -\lambda \sum _{i = 1}^ n (X_ i - a) \right) \mathbf{1}_{\min _{i = 1, \ldots , n}(X_ i) \geq a}.
>    \end{aligned}
>    $$
>
> 2. Observe that the likelihood $L=0$ if $a > \min_i(X_i)$, so let's restrict to $a \leq \min_i(X_i)$. Taking the log, then we need to maximize the function
>    $$
>    \ell (\lambda , a) := n \ln \lambda - \lambda \sum _{i = 1}^ n X_ i + n \lambda a
>    $$
>    With respect to $\lambda$ and $a$.
>
>    Since $\lambda > 0$, we see that this function is monotone increasing in $a$, so we choose $a$​ to be as large as possible given the constraint $a \leq \min_i(X_i)$. Accordingly, we set
>    $$
>    \hat{a} = \min _{i =1, \ldots , n}(X_ i).
>    $$
>    To compute $\hat{\lambda}$, we set $a = \min _{i =1, \ldots , n}(X_ i)$, and need to maximize the function
>    $$
>    f(\lambda ) = n \ln \lambda - \lambda \sum _{i = 1}^ n X_ i + n \lambda \min _{i}(X_ i).
>    $$
>    Take the derivative and set it to $0$,
>    $$
>    f'(\lambda ) = \frac{n}{\lambda } - \sum _{i = 1}^ n X_ i + n \min _{i}(X_ i)
>    $$
>    We get
>    $$
>    \lambda = \frac{n}{\sum _{i = 1}^ n (X_ i - \min _{j}(X_ j))} = \frac{1}{\overline{X}_ n - \hat{a}}.
>    $$
>    Hence, we have
>    $$
>    \hat{\lambda } = \frac{1}{\overline{X}_ n - \hat{a}}.
>    $$
>
> 3. Since we are given that $a=0$ is known, we may write
>    $$
>    \ell (\lambda , 0) = (n \ln \lambda - \lambda \sum _{i = 1}^ n (X_ i)) \mathbf{1}_{\min _ i(X_ i) \geq 0} = n \ln \lambda - \lambda \sum _{i = 1}^ n (X_ i),
>    $$
>    Because the generated data will certainly satisfy $\min _ i(X_ i) \geq 0$.
>
>    The likelihood-ratio test statistic is
>    $$
>    \begin{aligned}
>    T_n &= 2 ( \ell (\hat{\lambda }, 0) - \ell (1, 0) )\\
>    &= 2( n \ln (1/\overline{X}_ n) - n - 0 + n \overline{X}_ n )\\
>    &= 2( - n \ln ( \overline{X}_ n ) - n + n \overline{X}_ n).
>    \end{aligned}
>    $$
>    By Wilks's theorem,
>    $$
>    T_ n \xrightarrow [(d)]{n \to \infty } \chi _1^2,
>    $$
>    Because the parameter $\lambda$​ is 1-dimensional.
>
> 4. We compute that
>    $$
>    \begin{aligned}
>    \widetilde{T_ n} &= 2( \ell (1, \hat{a}) - \ell (1, 1) )\\
>    & = 2\left(n \ln 1 - (1) \sum _{i = 1}^ n (X_ i - \hat{a})\right)\mathbf{1}_{\min _ i(X_ i) \geq \hat{a}} - 2\left( n \ln 1 - (1) \sum _{i = 1}^ n (X_ i - 1) \right) \mathbf{1}_{\min _ i(X_ i) \geq 1}.
>    \end{aligned}
>    $$
>    Recall that $\hat{a} = \min _ i(X_ i)$. Hence $\mathbf{1}_{\min _ i(X_ i) \geq \hat{a}} = 1$. Moreover, by our assumption $\mathbf{1}_{\min _ i(X_ i) \geq 1} =1$. We may further simplify
>    $$
>    \begin{aligned}
>    \widetilde{T_ n} &= 2\left(n \ln 1 - (1) \sum _{i = 1}^ n (X_ i - \hat{a})\right) - 2\left( n \ln 1 - (1) \sum _{i = 1}^ n (X_ i - 1) \right)\\
>    & = 2n(\hat{a} - 1).
>    \end{aligned}
>    $$
>
> 5. By independence, compute the CDF of $\hat{a} = \min _ i(X_ i)$:
>    $$
>    \begin{aligned}
>    P( \min _ i(X_ i) \geq t ) & = \left( \int _ t^\infty e^{-(x - 1)} \,  dx \right)^ n\\
>    & = e^{-n(t - 1)}\\
>    &= \int _ t^\infty -n e^{-n(x - 1)} \,  dx\\
>    & = \int _ t^\infty f_{n, 1}(x) \,  dx.
>    \end{aligned}
>    $$
>    Therefore, $\mathbf{\hat{a} \sim \text {ShiftExp}(n,1)}$ if we assume that $a= 1$ and $\lambda = 1$.
>
>    Compute the p-value:
>    $$
>    \begin{aligned}
>    P( \widetilde{T_{100}} > 1.03 ) & = P( \hat{a} > 1 + \frac{1.03}{200} )\\
>    & = \int _{ 1 + \frac{1.03}{200} }^\infty 100 e^{-100(x - 1)} \,  dx\\
>    & = e^{-1.03/2}\\
>    & \approx 0.5975.
>    \end{aligned}
>    $$

# 4. One-sided Test vs Wald's Test

Given $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Exp}(\lambda )$, where $\lambda > 0$ is an unknown parameter. In this series of problems, we will compare two tests for the following null and alternative hypotheses:
$$
\displaystyle  H_0 : \lambda \leq 1 \quad \text {vs} \quad H_1 : \lambda > 1.
$$

1. What is the MLE $\hat{\lambda}$ And the Fisher information $I(\lambda)$ for an exponential statistical model? 

2. Assume that the technical conditions hold so that the MLE $\hat{\lambda }_ n^{MLE}$ of an exponential statistical model is asymptotically normal. Then it follows that
   $$
   \frac{\sqrt{n} ( \hat{\lambda }_ n^{MLE} - \lambda ) }{g(\hat{\lambda }_ n^{MLE})} \xrightarrow [n \to \infty ]{(d)} N(0,1)
   $$
   where $g(\hat{\lambda }_ n^{MLE})$ is and expression that depends on $\hat{\lambda }_ n^{MLE}$. What is $g(\hat{\lambda }_ n^{MLE})$?

3. Let us define the test statistic
   $$
   T_ n = \frac{\sqrt{n} ( \hat{\lambda }_ n^{MLE} - 1) }{g(\hat{\lambda }_ n^{MLE})}
   $$
   where $g(\hat{\lambda }_ n^{MLE})$ is the expression from (2).

   We define the test $\psi = \mathbf{1}( T_ n > \tau )$​, where $\tau$​ is a chosen so that $\psi$​ is a test at asymptotic level $\alpha = 0.05$​. Suppose we observe $\overline{X}_ n = 0.83$​.

   Does the test $\psi$​ reject or fail to reject $H_0$​ on this data set? Use $n=100$​.

4. Recall the test statistic $T_n$​ from (3), and let $T_ n^{Wald}$​ denote the test statistic associated to Wald's test for the hypotheses $H_0$​ and $H_1$​. Express $T_ n^{Wald}$​ in terms of $T_n$​. What is $T_ n^{Wald}$​ asymptotically distributed to if we assume $\lambda = 1$​?

5. Consider the test $\psi ^{Wald} = \mathbf{1}( T_ n^{Wald} > \tau )$ where $\tau$ is set so that the test $\psi ^{Wald}$ has asymptotic level $0.05$. Suppose you observe $\overline{X}_ n = 0.83$.

   Does the test $\psi ^{Wald}$ Reject or fail to reject on the given data set? Use $n=100$.

> **Solution:**
>
> 1. Recall the MLE for an exponential statistical model which is precisely
>    $$
>    \hat{\lambda }_ n^{MLE} = \frac{1}{\overline{X}_ n}.
>    $$
>    To compute the Fisher information, the log-likelihood for a single observation is
>    $$
>    \ell (\lambda ) = \ln ( \lambda e^{-x \lambda } ) = \ln (\lambda ) - \lambda x.
>    $$
>    The second derivative is
>    $$
>    \ell ^{\prime \prime }(\lambda ) = - \frac{1}{\lambda ^2},
>    $$
>    and the Fisher information is given by
>    $$
>    \mathcal{I}(\lambda ) = - \mathbb {E}_\lambda [ \ell ^{\prime \prime }(\lambda ) ] = \frac{1}{\lambda ^2}.
>    $$
>
> 2. The asymptotic variance of the statistic
>    $$
>    \sqrt{n} ( \hat{\lambda }_ n^{MLE} - \lambda )
>    $$
>    is given by $\mathcal{I}(\lambda )^{-1} = \lambda ^2$. Therefore,
>    $$
>    \frac{\sqrt{n} ( \hat{\lambda }_ n^{MLE} - \lambda ) }{\lambda } \xrightarrow [n \to \infty ]{(d)} N(0,1)
>    $$
>    Moreover, by Slutsky's theorem,
>    $$
>    \frac{\sqrt{n} ( \hat{\lambda }_ n^{MLE} - \lambda ) }{\hat{\lambda }_ n^{MLE}} \xrightarrow [n \to \infty ]{(d)} N(0,1).
>    $$
>    Therefore ${g(\hat{\lambda }_ n^{MLE}) = \hat{\lambda }_ n^{MLE}}$​​.
>
> 3. Recall that the $5\%$​ quantile of $\mathcal{N}(0,1)$​ is approximately $1.65$​. If $\bar{X}_n = 0.83$, then
>    $$
>    T_ n = \frac{\sqrt{n} ( \frac{1}{0.83} - 1) }{1/0.83} \approx 1.7.
>    $$
>    Therefore, the test as designed above will reject $H_0$​.
>
> 4. By definition of Wald's Test, we have that
>    $$
>    T_ n^{Wald} = n (\hat{\lambda }_ n^{MLE} - 1)^ T I(\hat{\lambda }_ n^{MLE}) (\hat{\lambda }_ n^{MLE} - 1).
>    $$
>    Since the MLE is 1-dimensional,
>    $$
>    T_ n^{Wald} = n (\hat{\lambda }_ n^{MLE} - 1)^2 \cdot \frac{1}{(\hat{\lambda }_ n^{MLE})^2}.
>    $$
>    Observe that $T_ n^{Wald} = T_ n^2$.
>
>    Since 
>    $$
>    T_ n \xrightarrow [n \to \infty ]{(d)} N(0,1),
>    $$
>    We have that
>    $$
>    T_ n^{Wald} = T_ n^2 \xrightarrow [n \to \infty ]{(d)} \chi _1^2.
>    $$
>
> 5. Consulting a table of values, we see that the $0.05$​-quantile of $\chi^2_1$​ is $3.84$​. Now observe that
>    $$
>    T_ n^{Wald} = (T_ n^2) \approx (1.7)^2 \approx 2.89
>    $$
>    Therefore, using Wald's test, we would fail to reject $H_0$​ on observing $\overline{X}_ n = 0.83$​.

