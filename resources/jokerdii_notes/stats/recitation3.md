# Recitation 3: Hypothesis Testing

Let $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim }\text {Poiss}(\lambda )$, for some unknown $\lambda > 0$ and let $\lambda_0$ be a fixed (known) positive number.

1. Consider the following hypotheses: $H_0: \lambda =\lambda _0 \quad \text {vs.} \quad H_1: \lambda \neq \lambda _0.$ Give a test with asymptotic level $5\%$.
2. Consider the following hypotheses: $H_0: \lambda \leq \lambda _0 \quad \text {vs.} \quad H_1: \lambda >\lambda _0 .$ Give a test with asymptotic level (at most) $5\%$.
3. Consider the following hypotheses: $H_0: \lambda \geq \lambda _0 \quad \text {vs.} \quad H_1: \lambda <\lambda _0 .$ Give a test with asymptotic level (at most) $5\%$.
4. Consider the following hypotheses: $H_0: |\lambda -2|\leq 1 \quad \text {vs.} \quad H_1: |\lambda -2|> 1 .$ Give a test with asymptotic level (at most) $5\%$.

> **Solution**:
>
> 1. Let $\lambda_0 = 2$. This is a two-sided test.
>
>    The mean and variance of Poisson r.v. is $\mathbb{E}[X_i] = \lambda, \quad \mathsf{Var}(X) = \lambda$. 
>
>    According to LLN, 
>    $$
>    \hat{\lambda} = {1\over n}\sum^n_{i=1}X_i \xrightarrow[n \rightarrow \infty]{R_\lambda} \lambda
>    $$
>    According to CLT,
>    $$
>    \sqrt{n} {\hat{\lambda} - \lambda \over\sqrt{\lambda} }\xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
>    $$
>    The **test statistic** for the test is
>    $$
>    T_n = \left\vert \sqrt{n}{\hat{\lambda} - 2 \over \sqrt2} \right\vert
>    $$
>    If we define $\psi = \mathbf{1}\{T_n > s\}$, the **type 1 error** with test statistic plugged in is
>    $$
>    \begin{aligned}
>    \alpha_\psi(2) = \mathbb{P}_2(\psi(X_1, ..., X_n) = 1) &= \mathbb{P}_2(T_n > s) \\
>    &= \mathbb{P}_2\left(\left\vert \sqrt{n}{\hat{\lambda} - 2 \over \sqrt2} \right\vert > s\right) \xrightarrow[n \rightarrow \infty]{} \mathbb{P}(|Z| > s) \\ 
>    & \left(\text{By LLN: } \quad \left( {\hat{\lambda} -2  \over \sqrt2} \right) \xrightarrow[n \rightarrow \infty]{R_\lambda} \left({\lambda -2  \over \sqrt2} \right)\neq 0\right)\\
>    &= 2(1-\Phi(s)) = \alpha\\
>    &\implies \Phi(s) = 1 - {\alpha \over 2}\\
>    &\implies s = q_{\alpha/2}, \quad 1-{\alpha \over 2 } \text{ quantile of }\mathcal{N}(0,1)
>    \end{aligned}
>    $$
>    where $Z \sim \mathcal{N}(0,1)$.
>
>    Type 2 error: if $\lambda \neq 2$, 
>    $$
>    \mathbb{P}_\lambda(T_n \leq s) = \mathbb{P}_\lambda\left( \left\vert \sqrt{n}{\hat{\lambda} - 2 \over \sqrt2} \right\vert \leq s\right) \xrightarrow[n \rightarrow \infty]{} 0
>    $$
>
> 2. /
>
> 3. This is a one-sided test.
>
>    According to CLT,
>    $$
>    \sqrt{n} {\hat{\lambda} - \lambda \over\sqrt{\lambda} }\xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
>    $$
>    If we define $\psi = \mathbf{1}\{T_n < -s\}$, for $\lambda > 2$, the **type 1 error** is 
>    $$
>    \begin{aligned}
>    \alpha_\psi(\lambda) &= \mathbb{P}_\lambda(T_n < -s) = \mathbb{P}_\lambda\left(\left\vert \sqrt{n}{\hat{\lambda} - 2 \over \sqrt2} \right\vert < -s\right) \xrightarrow[n \rightarrow \infty]{} 0\\
>    & \left(\text{By LLN: } \quad \left( {\hat{\lambda} -2  \over \sqrt2} \right) \xrightarrow[n \rightarrow \infty]{R_\lambda} \left({\lambda -2  \over \sqrt2}\right) < 0\right)
>    \end{aligned}
>    $$
>    When $\lambda = 2$, the type 1 error is 
>    $$
>    \begin{aligned}
>    \alpha_\psi(2) &= \mathbb{P}_2(T_n < -s) = \mathbb{P}_2\left(\left\vert \sqrt{n}{\hat{\lambda} - 2 \over \sqrt2} \right\vert < -s\right) \xrightarrow[n \rightarrow \infty]{} \mathbb{P}(Z < -s)\\
>    &= 1 - \Phi(s) = \alpha\\
>    &\implies \Phi(s) = 1 - {\alpha }\\
>    &\implies s = q_{\alpha}, \quad 1-{\alpha} \text{ quantile of }\mathcal{N}(0,1)
>    \end{aligned}
>    $$
>    Note that it is easier to reject the null hypothesis in one-sided test than in two-sided test.
>
> 4. **Composite test**
>
>    The **test** is defined as 
>    $$
>    \psi = \mathbf{1}\{ T_n^l < -s_l \quad \text{ or } \quad T_n^r > s_r\}
>    $$
>    The **test statistics** are
>    $$
>    T_n^l = \sqrt{n} {\hat{\lambda} - 1 \over \sqrt1} = \sqrt{n} \left(\hat{\lambda} - 1\right); \quad T_n^r = \sqrt n{ \hat{\lambda} - 3 \over\sqrt{3} }
>    $$
>    For $\lambda = 1$, the **type 1 error** is
>    $$
>    \begin{aligned}
>    \alpha_\psi(1) &= \mathbb{P}_1(T_n^l < -s_l \quad \text{or} \quad T_n^r > s_r)\\
>    &= \mathbb{P}_1(T_n^l < -s_l) + \mathbb{P}_1(T_n^r > s_r)
>    \end{aligned}
>    $$
>    where
>    $$
>    \begin{aligned}
>    &\mathbb{P}_1(T_n^l < -s_l) = \mathbb{P}_1\left(\sqrt n (\hat{\lambda} -1)< -s_l\right) \xrightarrow[n \rightarrow \infty]{} \mathbb{P}(Z < -s_l) = \alpha\\
>    & \left(\text{By LLN: } \quad \left({\hat{\lambda} -1} \right)\xrightarrow[n \rightarrow \infty]{R_\lambda} (\lambda -1 ) \right)\\
>    &\mathbb{P}_1(T_n^r > s_r) = \mathbb{P}_1\left(\sqrt{n} {\hat{\lambda}-3 \over \sqrt 3} > s_r\right) \xrightarrow [n \rightarrow \infty]{} 0 \quad \text{ by LLN}\\
>    & \left(\text{By LLN: } \quad \left( {\hat{\lambda} -3  \over \sqrt3} \right) \xrightarrow[n \rightarrow \infty]{R_\lambda} \left({\lambda -3  \over \sqrt3}\right) < 0\right)
>    \end{aligned}
>    $$
>    So we only need to adjust the level at the **left** boundary.
>
>    For $\lambda = 3$, similarly, we only need to adjust the level at the **right** boundary
>    $$
>    \mathbb{P}_3\left(T_n^r > s_r\right) = \mathbb{P}_3\left(\sqrt n {\hat{\lambda} - 3 \over \sqrt 3} > s_r\right) \xrightarrow [n \rightarrow \infty]{} \mathbb{P}(Z > s_r) = \alpha\\
>    \left(\text{By LLN: } \quad \left( {\hat{\lambda} -3  \over \sqrt3} \right) \xrightarrow[n \rightarrow \infty]{R_\lambda}\left( {\lambda -3  \over \sqrt3} \right)\right)
>    $$
>    For $\lambda \in (1,3)$: 
>    $$
>    \begin{aligned}
>    &\mathbb{P}_\lambda\left(T_n^l < -s_l\right) = \mathbb{P}_\lambda\left(\sqrt n (\hat{\lambda} - 1) < -s_l\right) \xrightarrow[n\rightarrow \infty]{} 0\\
>    &\left(\text{By LLN: } \quad \left({\hat{\lambda} -1} \right)\xrightarrow[n \rightarrow \infty]{R_\lambda} \left(\lambda -1 \right) > 0 \right)\\
>    &\mathbb{P}_\lambda\left(T_n^r > s_r\right) = \mathbb{P}_\lambda\left(\sqrt{n} {\hat{\lambda}-3 \over \sqrt 3} > s_r\right) \xrightarrow [n \rightarrow \infty]{} 0 \\
>    &\left(\text{By LLN: } \quad \left( {\hat{\lambda} -3  \over \sqrt3} \right) \xrightarrow[n \rightarrow \infty]{R_\lambda} \left({\lambda -3  \over \sqrt3}\right) < 0\right)
>    \end{aligned}
>    $$
>    In this case, the type 1 error will vanish.

