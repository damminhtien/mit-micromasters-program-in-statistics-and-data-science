# Recitation 2: Confidence Intervals of the shift of shifted exponential random variables

Consider a sample of $n$ i.i.d. continuous random variables $X_1,…,X_n$ with density
$$
f(x)=e^{-(x-a)} \mathbf{1}_{x\geq a}
$$
where $a∈\R$ is an unknown parameter.

1. Find an estimator $\hat{a}$ for the unknown shift parameter $a$.
2. Determine the (asymptotic) distribution of $\hat{a}$.
3. Compute a two-sided C.I. for a based on $\hat{a}$.
4. Compare (Q3) results with a different estimator of the same parameter $a$.
5. Compute an one-sided C.I. for a based on $\hat{a}$.

> 1) Consider $\overline{X}_n = {1\over n} \sum^n_{i=1} X_i$, and LLN $\overline{X}_n \xrightarrow[n\rightarrow \infty]{\mathbb{P}} \mathbb[X_1]$, we calculate
> $$
> \begin{aligned}
> \mathbb{E}[X_1] &= \int^\infty_{-\infty} x e^{-(x-a)}\mathbf{1}_{\{x \geq a\}}\\
> &= \int^\infty_{a} xe^{-(x-a)} dx\\
> &= \left[ -e^{-(x-a)}x\right]^\infty_a + \int^\infty_ae^{-(x-a)} dx\\
> &= a - \left[e^{-(x-a)}\right]^\infty_a\\
> &= a + 1\\
> \implies & \hat{a}_1 = \overline{X}_n - 1 \xrightarrow[x\rightarrow \infty]{\mathbb{P}} a
> \end{aligned}
> $$
> 2) Use **CLT** to analyze the asymptotic distribution of $\overline{X}_n$.
>
> By CLT, 
> $$
> {\sqrt{n} \over \sqrt{\mathsf{Var}(X_1)}} \left( \overline{X}_n - \mathbb{E}[X_1] \right) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
> $$
> First we calculate the variance by the formula $\mathsf{Var}(X_1) = \mathbb{E}[X_1^2] - (\mathbb{E}[X_1])^2$.
> $$
> \begin{aligned}
> \mathbb{E}[X_1] &= \int^\infty_{-\infty}x^2 e^{-(x-a)} \mathbf{1}_{\{x \geq a\}} dx \\
> &= \int^\infty_{a}x^2 e^{-(x-a)}dx\\
> &= \left[ -e^{-(x-a)}x^2 \right]^\infty_a + \int 2xe^{-(x-a)} dx\\
> &= a^2 + 2(a+1)
> \end{aligned}
> $$
> Thus
> $$
> \mathsf{Var}(X_1) = a^2 + 2(a+1) - (a+1)^2 = 1
> $$
> Plug it back in and we have the distribution
> $$
> {\sqrt{n}} \left( \hat{a}_1 - a \right) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
> $$
> 3) Consider a two-sided asymptotic C.I., $\mathcal{I}_1 = \hat{a}_1 + [-s, s], s > 0$
> $$
> \begin{aligned}
> \mathbb{P}(a\in\mathcal{I}_1) &= \mathbb{P}\left(a\in \left[\hat{a}_1 -s,\hat{a}_1 +s \right]\right)\\
> &= \mathbb{P}(\hat{a}_1 - s \leq a \leq \hat{a}_1 +s)\\
> &= \mathbb{P} (-s \leq a-\hat{a}_1 \leq s)\\
> &= \mathbb{P} (-s \leq \hat{a}_1 -a \leq s)\\
> &= \mathbb{P}(-\sqrt{n}s \leq \sqrt{n}(\hat{a}_1 - a) \leq \sqrt{n} s)
> \end{aligned}
> $$
> Let $q = \sqrt{n} s$. Thus,
> $$
> \mathbb{P}\left(a\in \left[\hat{a}_1 -s,\hat{a}_1 +s \right]\right) \xrightarrow[n \rightarrow \infty]{(d)} \mathbb{P}(Z \in [-q, q])
> $$
> where $Z \sim \mathcal{N}(0,1)$.
>
> We want 
> $$
> \mathbb{P}\left(a\in \left[\hat{a}_1 -s,\hat{a}_1 +s \right]\right) \xrightarrow[n \rightarrow \infty]{(d)} \mathbb{P}(Z \in [-q, q]) = 1 -\alpha = 2 \Phi(q) -1
> $$
> where $\Phi(\cdot)$ is the cumulative distribution function of a standard Gaussian, and $ q = q_{\alpha/2}$ is the $1-{\alpha/2}$ quantile. Hence, the asymptotic C.I. is 
> $$
> \mathcal{I}_1 = \hat{a}_1 + \left[-{q_{\alpha/2}\over\sqrt{n}}, {q_{\alpha/2}\over\sqrt{n}}\right]
> $$
> 4) Let $\hat{a}_2 = \min\limits_{1\leq i \leq n} X_i$ be an estimator. 
>
> Now calculate the asymptotic distribution of it. Since it is enough to give CDF of a r.v. to characterize the whole distribution. i.e. give $\mathbb{P}(Y \leq t), \forall t \in \R$ to determine distribution of $Y$. In order to have CDF, we apply
> $$
> \mathbb{P}(\hat{a}_i \leq t) = 1 - \mathbb{P}(\hat{a}_i > t)
> $$
> Let $t < a$: $\mathbb{P}(\hat{a}_2 > t) = 1$;
>
> Let $t > a$: 
> $$
> \begin{aligned}
> \mathbb{P}(\hat{a}_2 > t) &= \mathbb{P}(X_i > t, \forall i) \\
> &= \mathbb{P}(\bigcap^n_{i=1} \{X_i > t\}) \\
> &= \prod^n_{i=1} \mathbb{P}(X_i > t)\\
> &= \prod^n_{i=1} \int^\infty_t e^{-(x-a)} dx\\
> &= \prod^n_{i=1}\left[ -e^{-(x-a)} \right]^\infty_t\\
> &= \prod^n_{i=1}e^{-(t-a)}\\
> &= e^{-n(t-a)}
> \end{aligned}
> $$
> Since this is a scaled and shifted exponential distribution, we can scale and shift it back by using $\stackrel{\sim}{t}= (1/n) t + a, \stackrel{\sim}{t} > 0$. Then we have
> $$
> \mathbb{P}(\hat{a}_2 >  {1\over n} t + a) = e^{-\stackrel{\sim}{t}}
> $$
> Therefore, we have
> $$
> n(\hat{a}_2 - a) \sim \mathsf{Exp}(1)
> $$
> Notice that if "1- CDF" looks like $e^{-x}$, it corresponds to an exponential distribution.
>
> 5) Consider one-sided C.I. $\mathcal{I}_2 = [\hat{a}_2 -s , \hat{a}_2]$ 
> $$
> \begin{aligned}
> \mathbb{P}(a \in \mathcal{I}_2) &= 1 - \alpha\\
> &= \mathbb{P}\left(a \in [\hat{a}_2 - s, \hat{a}_2]\right) \\
> &= \mathbb{P}(\hat{a}_2 -s \leq a \leq \hat{a}_2)\\
> &= \mathbb{P} (\hat{a}_2 -a \leq s)\\
> &= \mathbb{P}(n(\hat{a}_2 - a) \leq ns)
> \end{aligned}
> $$
> Let $q = ns$, we have
> $$
> \begin{aligned}
> \mathbb{P}(a \in \mathcal{I}_2) &= \mathbb{P}(Y \leq q), \quad \text{ where } Y \sim \mathsf{Exp}(1)\\
> &= 1- e^{-q} \\
> &= 1 - \alpha\\
> \implies & e^{-q} = \alpha \\
> \implies & q = - \log(\alpha) = \log(1/\alpha)
> \end{aligned}
> $$
> Therefore, we have the one-sided C.I.
> $$
> \mathcal{I}_2 = \left[ \hat{\alpha}_2 - {\log({1\over \alpha})\over n}, \hat{a}_2 \right]
> $$

#### Remark: Comparing two estimators

| $\hat{a}_1 = {1\over n}\sum^n_{i=1}X_i-1; \quad \mathcal{I}_1$ | $\hat{a}_2 = \min\limits_{1\leq i \leq n}X_i; \quad \mathcal{I}_2$ |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Generic approach.                                            | Specifically tailored to the model.                          |
| $\vert\mathcal{I}_1\vert \sim {1\over \sqrt{n}}$             | $\vert \mathcal{I_2} \vert \sim {1\over n}$                  |
| Asymptotic.                                                  | Non-asymptotic.                                              |
| Some robustness properties.                                  | Highly non-robust; sensitive to outliers.                    |



