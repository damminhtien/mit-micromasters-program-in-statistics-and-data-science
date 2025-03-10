# Recitation 7. M-Estimation

1. Derive the asymptotic variance of the sample median.
2. Compare the asymptotic variance for sample mean and median under Laplace $(\mu,1)$​​​.
3. Compare the asymptotic variance for sample mean, median under Cauchy ($\mu,1$​​).
4. Compare the asymptotic variance for those in (3) and Huber estimator under Cauchy ($\mu,1$).

> **Solution:**
>
> 1. Let $m_n$​ be the sample median and suppose that we observe data $X_1, ..., X_n \sim F$​, where $F$​ is a continuous distribution, and let $\mu$​ be the population median $F(\mu)=1/2$​​. For the following, assume that $n$​ is odd, so that the sample median is the unique point $m_n = X_{(n+1)/2}$​. Then,
>
>    We will show that
>    $$
>    P(\sqrt{n}(m_n - \mu) \leq a) \rightarrow \mathcal{N}(0,\sigma^2)
>    $$
>    For some asymptotic variance $\sigma^2$. To this end, notice that
>    $$
>    \{m_n \leq \mu + a/\sqrt{n}\} = \{\#(X_i \leq \mu + a/ \sqrt{n}) \geq {n+1 \over 2}\} = \{\overline{Y_n} \geq {n+1 \over 2}\}
>    $$
>    where the random variables $Y_i$ are defined by $Y_i = \mathbb{1}(X_i \leq \mu + a/ \sqrt{n})$​. Then we have
>    $$
>    \begin{aligned}
>    P(\sqrt{n} (m_n - \mu )\leq a) &= P\left(\overline{Y_n} \geq {n+1 \over 2} \right)\\
>    &= P\left(\overline{Y_n} - p_n n \geq {n+1 \over 2} - p_n n\right)\\
>    &= P\left( {\overline{Y_n} - p_n n \over \sqrt{n p_n (1-p_n)}} \geq {{n+1 \over 2} - p_n n \over \sqrt{n p_n (1 - p_n)}} \right)
>    \end{aligned}
>    $$
>    where $p_n = F(\mu + 1/ \sqrt{n})$​​ is the probability that $Y_i = 1$​ (Notice that $Y_i$​ is a Bernoulli ($p_n$) random variable).
>
>    Let $p = F(\mu) = 1/2$. Notice that
>    $$
>    {\overline{Y_n} - p_n n \over \sqrt{n p_n (1-p_n)}} -  {\overline{Y_n} - p n \over \sqrt{n p (1-p)}}  \xrightarrow[n \rightarrow \infty]{p}0
>    $$
>    which then yields
>    $$
>    {\overline{Y_n} - p_n n \over \sqrt{n p_n (1-p_n)}}\xrightarrow[n \rightarrow \infty]{d}\mathcal{N}(0,1)
>    $$
>    Let ${\overline{Y_n} - p_n n \over \sqrt{n p_n (1-p_n)}} = Z$​, we have
>    $$
>    P(\sqrt{n} (m_n - \mu )\leq a)= P(m_n \leq \mu + a/\sqrt{n}) = P\left( Z \geq {{n+1 \over 2} - p_n n \over \sqrt{n p_n (1 - p_n)}} \right)
>    $$
>    Finally, we notice that
>    $$
>    \begin{aligned}
>    {{n+1 \over 2} - p_n n \over \sqrt{n p_n (1 - p_n)}} &= {{n \over 2} + {1\over 2} - F(\mu + a/\sqrt{n}) n \over \sqrt{n p_n (1- p_n)}} \\
>    &= {{n \over 2} - F(\mu + a/\sqrt{n}) n \over \sqrt{n p_n (1- p_n)}} + {{1\over 2}\over \sqrt{n p_n (1- p_n)} }\\
>    &= {F(\mu) - F(\mu + a/\sqrt{n}) \over a/\sqrt{n}} \cdot {a \over \sqrt{p_n(1-p_n)}} + {{1\over 2} \over \sqrt{n p_n (1- p_n)}}\\
>    &\xrightarrow[]{d} -2a F'(\mu) 
>    \end{aligned}
>    $$
>    Therefore, 
>    $$
>    P(Z \geq -2a F'(\mu) ) = P(-Z \leq 2a F'(\mu)) = P(Z \leq 2a F'(\mu)) = P({Z\over 2 f(\mu)} \leq a) \sim \mathcal{N}\left(0,{1\over 4f(\mu)^2}\right)
>    $$
>    Equivalently,
>    $$
>    \sqrt{n}(m_n - \mu) \xrightarrow[]{d}\mathcal{N}\left(0,{1\over 4f(\mu)^2}\right)
>    $$
>
> 2. For the Laplace distribution, the likelihood of $X_1, ..., X_n$ is
>    $$
>    L(X_1, ..., X_n; \mu) = \prod^n_{i=1} {1\over 2} \exp\left(-|x_i - \mu|\right)
>    $$
>    The log-likelihood is
>    $$
>    \ell(X_1, ..., X_n;\mu) = -n \log(2) - \sum^n_{i=1}|x_i - \mu|
>    $$
>    Notice that maximizing $\ell$​ is equivalent to minimizing $-\ell$, and so
>    $$
>    \hat{\mu}_{MLE} = \min_\mu \sum^n_{i=1}|x_i - \mu|
>    $$
>    This is an M-estimator that corresponds to the sample median.
>
>    The asymptotic variance of sample mean is
>    $$
>    \mathsf{avar}(\overline{X_n})=\mathsf{Var}(X_1) = 2
>    $$
>    Since Laplace$(\mu, 1)$​ and Laplace$(0, 1)$​ must have the same variance, we can use integration by parts twice on the Laplace$(0, 1)$​ to obtain the variance of the Laplace$(\mu, 1)$​​ distribution.
>    $$
>    \begin{aligned}
>    \mathsf{Var}(X) &= \mathbb{E}[X^2] = \int^\infty_{-\infty} {x^2 \over 2} \exp(-|x|)dx\\
>    &= 2 \int^{\infty}_0 {x^2 \over 2} \exp(-x) dx\\
>    &= 2 \left( -{x^2 \over 2} \exp (-x) |^{\infty}_0 - \int^{\infty}_0 x \exp (-x)dx \right)\\
>    &= 2 \left( -\int^{\infty}_0 x \exp(-x) dx \right)\\
>    &= 2 \left( x \exp (-x)|^{\infty}_0 + \int^{\infty}_0  \exp(-x) dx \right)\\
>    &= 2 \left( -\exp(-x)|^{\infty}_0 \right)\\
>    &= 2
>    \end{aligned}
>    $$
>    On the other hand, we derive the asymptotic variance of the sample median in (1), which is
>    $$
>    \text{avar}(m_n) = {1\over 4 f(\mu)^2} = {1\over 4} \cdot {1 \over \left[ {1\over 2} \exp\left(-|\mu - \mu|\right) \right]^2} = 1
>    $$
>    Therefore,
>    $$
>    \text{avar}(m_n) < \text{avar}(\overline{X})
>    $$
>    This gives some evidence that using the sample median at least for the Laplace distribution, would give you better performance, at least asymptotically.
>
> 3. For $X \sim \text{Cauchy}(\mu, 1)$​, we have PDF
>    $$
>    f_X(x) = {1\over \pi (1 + (x - \mu)^2)}
>    $$
>    and CDF
>    $$
>    \begin{aligned}
>    F_X(x) &= \int^x_{-\infty} f(t)dt\\
>    &=\int^x_{-\infty}{1\over \pi(1 + (t-\mu)^2)} dt\\
>    &={\text{arctan}(t-\mu)|^x_{-\infty} \over\pi } \\
>    &=  {1\over 2} + {1\over \pi} \text{arctan}(x-\mu)
>    \end{aligned}
>    $$
>    Note that $F(\mu) = {1\over2}$.
>
>    And its inverse
>    $$
>    F_X^{-1}(t)= \text{tan}\left(\pi \left(t - {1\over2}\right)\right) + \mu
>    $$
>    Notice that these are both continuous on $\R$.
>
>    The asymptotic variance of the sample mean $\overline{X}$​​​ diverges.
>    $$
>    \text{avar}(\overline{X_n}) = n \text{Var}(\overline{X_n}) = \text{Var}(X_i) = \infty
>    $$
>    On the other hand, the asymptotic variance of the sample median is
>    $$
>    \text{avar}(\tilde{X_n}) = {1/4 \over f_X(F_X^{-1}(1/2))^2} = {1/4 \over f_X(\mu)^2} = {\pi^2 \over 4}
>    $$
>    Therefore, we see that the median gives us a better estimator than the mean is the case of the Cauchy distribution. It has a finite asymptotic variance, while 
>
> 4. The Huber loss function is
>    $$
>    \rho(x) = \begin{cases} {x^2 \over 2}, & |x| < \delta\\ \delta|x| - {\delta^2 \over 2}, &|x| > \delta \end{cases}
>    $$
>    The first derivative
>    $$
>    \rho'(x) = \begin{cases}x, & |x| < \delta \\ \delta \ \text{sign}(x), & |x| \geq \delta \end{cases}
>    $$
>    The second derivative
>    $$
>    \rho''(x) = \begin{cases}1, & |x| < \delta \\ 0, & |x| \geq \delta \end{cases}
>    $$
>    The Huber estimator
>    $$
>    \hat{\mu}_{huber} = \text{argmin}_{b \in \R}\sum^n_{i=1} \rho(X_i - b)
>    $$
>    The asymptotic normal distribution is
>    $$
>    \sqrt{n}(\hat{\mu}_{huber} - \mu) \xrightarrow[]{(d)} \mathcal{N}\left(0, {\rm{Var}(\rho'(x))\over [\mathbb{E}\rho''(x)]^2 }\right)
>    $$
>    To compute $\mathbb{E}\rho''(x)$​​​​,
>    $$
>    \begin{aligned}
>    \mathbb{E}\rho''(x) &= \int^{\delta}_{-\delta} 1 \cdot f(x) dx\\
>    &= \int^{\delta}_{-\delta}{1\over \pi(1 + x^2)}dx\\
>    &= {1\over \pi}(\text{arctan}\ \delta - \text{arctan}\ (-\delta))\\
>    &= {2\over \pi} \text{arctan} \ \delta
>    
>    \end{aligned}
>    $$
>    To compute $\rm{Var}(\rho'(x))$​,​
>    $$
>    \begin{aligned}
>     \mathbb{E}(\rho'(x))^2
>    &= \int^{-\delta}_{-\infty} \delta^2 {1\over \pi(1 + x^2)}dx + \int^{\delta}_{-\delta} \delta^2 {1\over \pi(1 + x^2)}dx + \int^{\infty}_{\delta} \delta^2 {1\over \pi(1 + x^2)}dx \\
>    &= {\delta^2 \over \pi} \left(\text{arctan}(-\delta) - \left(-{\pi \over 2}\right)\right) + {\delta^2 \over \pi}\left({\pi \over 2} - \text{arctan}\ \delta \right) + {2\delta \over \pi} - {2 \arctan \delta \over \pi}
>    \end{aligned}
>    $$
>    Since $1+ \tan^2 x = \sec^2 x$​, let $x = \tan u$, then $\sec^2 u\ du = dx$.
>    $$
>    \begin{aligned}
>    \int{x^2 \over \pi (1 + x^2)} dx &= \int{\tan^2u \ \sec^2u du\over \pi (\sec^2u)}\\
>    &={1\over \pi} \int (\sec^2 u - 1 )du\\
>    &={1\over \pi} (\tan u - u)\\
>    \implies\int^{\delta}_{-\delta} {x^2 \over \pi (1 + x^2)} dx &= {1\over \pi}(x - \arctan x)|^\delta_{-\delta}\\
>    &= {1\over \pi} (\delta - \arctan \ \delta - (-\delta - \arctan(-\delta)))\\
>    &= {2\delta \over \pi} - {2 \arctan \delta \over \pi}
>    \end{aligned}
>    $$
>    So the asymptotic variance is
>    $$
>    \begin{aligned}
>    \text{avar}(\hat{\mu}_{huber}) &= {\rm{Var}(\rho'(x))\over [\mathbb{E}\rho''(x)]^2 } = {\mathbb{E}(\rho'(x)^2) \over [\mathbb{E}\rho''(x)]^2}\\
>    &={{\delta^2 \over \pi} \left(\text{arctan}(-\delta) - \left(-{\pi \over 2}\right)\right) + {\delta^2 \over \pi}\left({\pi \over 2} - \text{arctan}\ \delta \right) + {2\delta \over \pi} - {2 \arctan \delta \over \pi} \over \left[{2\over \pi} \text{arctan}\ (\delta)\right]^2}\\
>    &= {\delta^2 + {2\delta \over \pi} - {2 \arctan \delta \over \pi} - 2{\delta^2 \over \pi} \arctan(\delta) \over \left[{2\over \pi} \text{arctan}\ (\delta)\right]^2}
>    \end{aligned}
>    $$
>    By **L'Hopital's rule**,
>    $$
>    \begin{aligned}
>    \text{avar}(\hat{\mu}_{huber}) &\xrightarrow[s\rightarrow 0]{} {\pi^2 \over 4} = \text{avar}(m_n)\\
>    \text{avar}(\hat{\mu}_{huber}) &\xrightarrow[s\rightarrow \infty]{} \text{diverges}
>    \end{aligned}
>    $$

