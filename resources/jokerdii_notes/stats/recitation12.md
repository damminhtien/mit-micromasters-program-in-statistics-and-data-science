# Recitation 12 T-test

**Review: Orthogonal matrices:** $\begin{bmatrix} | & & | \\ v_1 & ... & v_n \\ | & & | \end{bmatrix} = V \in \R^{n \times n}$

$v_i^T v_j = 0,\ i \neq j , \ v_i^T v_i = ||v||_2^2 = 1 \implies \{v_i\}_{i=1,...,n}$​​​​​​​​​​ are **orthonormal**, $V$​​ is **orthonormal**.

Then:

$$
V^TV = \begin{bmatrix} - & v_1^T & - \\ & \vdots & \\ - & v_n^T & - \end{bmatrix} \begin{bmatrix} | & & | \\ v_1 & ... & v_n \\ | & & | \end{bmatrix}= \begin{bmatrix} 1& &0\\ & ... & \\ 0 & & 1 \end{bmatrix}= I_n = VV^T
$$


$$
x \in \R^n, \  ||Vx||^2_2 = (Vx)^T(Vx) = x^T V^TVx = x^Tx = ||x||^2_2
$$
$W = \begin{bmatrix} | & & | \\ w_1 & ... & w_l \\ | & & | \end{bmatrix} \in \R^{n \times k}, \{w_i\}_{i = 1,..., l}$ are orthonormal.
$$
||WW^TX||^2_2 = (WW^TX)^T(WW^TX) = X^TWW^TWW^TX  = ||W^TX||^2_2
$$
Let $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim }\mathcal N(\mu ,\sigma ^2)$​, for some **unknown** parameter $(\mu ,\sigma ^2)\in \mathbb {R}\times (0,\infty )$​. We want to test the following hypotheses at non-asymptotic level $\alpha$​ (for some fixed $\alpha \in (0,1)$​):
$$
H_0: \mu \ge 0 \hspace{2mm} \text{vs.} \hspace{2mm} H_1: \mu < 0.
$$

1. Recall the maximum likelihood estimator $(\hat\mu ,\hat\sigma ^2)$​ or $(\mu ,\hat\sigma ^2)$​.
2. Let ${S=\sqrt{n-1}\frac{\hat\mu -\mu }{\sqrt{\hat\sigma ^2}}}$. Prove that $S$ is a Student random variable with $n-1$ degrees of freedom.
3. Propose a test with non-asymptotic level $\alpha$. Prove your answer.

> **Solution:**
>
> 1. The likelihood is
>    $$
>    f(\mu, \sigma^2, X_1, ..., X_n) =  \prod^n_{i=1} {1\over \sqrt{2 \pi \sigma^2}} e ^{-{1\over 2 \sigma^2}(X_i - \mu)^2}
>    $$
>    The log likelihood is
>    $$
>    \begin{aligned}
>    \ell(\mu, \sigma^2) = \log f &= \sum^n_{i=1}\left[ -{1\over 2}\log 2 \pi - {1\over 2} \log \sigma^2 - {1\over 2\sigma^2} (X_i - \mu)^2 \right]\\
>    &= -{n \over 2} \log 2\pi - {n \over 2} \log \theta^2 - {1\over 2\sigma^2} \sum^n_{i=1}(X_i - \mu)^2
>    \end{aligned}
>    $$
>    Take the derivative and set it to zero, we get
>    $$
>    {\partial \ell(\mu, \sigma^2)\over \partial \mu} = -{1\over 2\sigma^2} \sum^n_{i=1} 2 \cdot (X_i - \mu) (-1) = 0\\
>    \implies \hat{\mu} = {1\over n} \sum^n_{i=1} X_i\\
>    {\partial \ell(\mu, \sigma^2) \over \sigma^2} = - {n \over 2\sigma^2} + {1\over 2 \sigma^4} \sum^n_{i=1} (X_i - \mu)^2 = 0\\
>    \implies \hat{\sigma}^2 = {1\over n}\sum^n_{i=1} (X_i - \hat{\mu})^2
>    $$
>
> 2. The variance is $\hat{\sigma}^2 = {1\over n}\sum\limits^n_{i=1} (X_i-\hat{\mu})^2$​​. 
>
>    Since $\hat{\mu} = {1\over n} \mathbb{1}^T X, \  \begin{pmatrix} \hat{\mu} \\ \vdots \\ \hat{\mu} \end{pmatrix} = {1\over n} \mathbb{1}\mathbb{1}^TX = {1\over \sqrt{n}}\mathbb{1} \left({1\over \sqrt{n}}\mathbb{1}\right)^T X = v_1 v_1^T X$​​​, we can write 
>    $$
>    \begin{aligned}
>    n \hat{\sigma}^2 &= \left|\left| \begin{pmatrix} X_1 \\ \vdots \\ X_n \end{pmatrix}-\begin{pmatrix} \hat{\mu} \\ \vdots \\ \hat{\mu} \end{pmatrix} \right|\right|^2_2\\
>    &= || X - v_1v_1^TX ||^2_2\\
>    &= || X-\mu \cdot \mathbb{1} - (v_1v_1^TX - \mu \mathbb{1}) ||^2_2\\
>    &= || X-\mu \cdot \mathbb{1} - v_1v_1^T(X - \mu \mathbb{1})||^2_2\\
>    \end{aligned}
>    $$
>    Since $Y = {X - \mu \mathbb{1} \over \sigma} = \begin{pmatrix}{X - \mu \over \sigma}\\\vdots \\{X - \mu \over \sigma} \end{pmatrix} \sim \mathcal{N}(0, I_n)$, and for orthogonal matrix $V = \begin{bmatrix} | & & | \\ v_1 & ... & v_n \\ | & & | \end{bmatrix} \in \R^{n \times n}$.
>    $$
>    \begin{aligned}
>    I_n &= VV^T =  \begin{bmatrix} - & v_1^T & - \\ & \vdots & \\ - & v_n^T & - \end{bmatrix} \begin{bmatrix} | & & | \\ v_1 & ... & v_n \\ | & & | \end{bmatrix}\\
>    &= \left(\sum^n_{i=1} v_ie_i^T\right)\left(\sum^n_{j=1} v_je_j^T\right)^T\\
>    &= \sum^n_{i,j=1} v_ie_i^Te_j v_j^T\\
>    &= \sum^n_{i=1} v_i v_i^T \qquad \text{where }e_i^Te_j = \begin{cases}1, &i=j\\0,&i \neq j \end{cases}
>    \end{aligned}
>    $$
>    We can write
>    $$
>    \begin{aligned}
>    {n\hat{\sigma}^2\over \sigma^2} & = ||Y - v_1v_1^T Y||^2_2\\
>    &= ||\sum^n_{i=1} v_iv_i^TY - v_1v_1^T Y||^2_2\\
>    &= ||\sum^n_{i=2} v_iv_i^TY ||^2_2\\
>    \end{aligned}
>    $$
>    Let $w = \begin{bmatrix} | & & | \\ v_2 & ... & v_n \\ | & & | \end{bmatrix}, w \in \R^{n \times (n-1)}$​​​​, so $\sum\limits^n_{i=2}= v_iv_i^T = WW^T$​​. Then
>    $$
>    \begin{aligned}
>    {n\hat{\sigma}^2\over \sigma^2} 
>    &= ||\sum^n_{i=2} v_iv_i^TY ||^2_2\\
>    &= ||WW^TY ||^2_2\\
>    &= ||W^TY ||^2_2, \qquad W^TY \in \R^{n-1}\\
>    \end{aligned}
>    $$
>    We now try to understand the distribution of $W^TY$​. The covariance of $W^TY$ is
>    $$
>    \text{Cov}(W^TY) = W^T \text{Cov}(Y) (W^T)^T = W^T I_nW = I_{n-1}\\
>    \implies {n \hat{\sigma}^2 \over (n-1)\sigma^2} \sim \chi^2_{n-1}
>    $$
>    We know that $T_n^{(1)} = {(\mu - \hat{\mu})\sqrt{n}\over \sqrt{\sigma^2}}\sim\mathcal{N}(0,1)$​​​​, where the $\hat{\mu}$​​​ can be written as
>    $$
>    \hat{\mu} = {1\over \sqrt{n} }v_1^T X = \mu + \sigma {1\over \sqrt{n} }v_1^T Y
>    $$
>    The covariance $\text{Cov}(W^TY, v_1^TY)$ is
>    $$
>    \begin{aligned}
>    \text{Cov}(W^TY, v_1^TY) &= \mathbb{E}[W^TYY^Tv_1] \qquad \text{where } W^TY \in \R^{n-1}, v_1^TY \in \R\\
>    &= W^T\mathbb{E}[YY^T]v_1\\
>    &= W^Tv_1\\
>    &= \begin{pmatrix}0 \\ \vdots \\ 0 \end{pmatrix} \in \R^{n-1}
>    \end{aligned}
>    $$
>    Thus $W^TY$​ and $v_1^TY$​​ are uncorrelated. And since they are jointly Gaussian, they are independent. So 
>    $$
>    W^TY \perp v_1^TY \implies \hat{\sigma}^2 \perp \hat{\mu}
>    $$
>    Therefore
>    $$
>    \tilde{T}_n^{(2)} = {{(\mu - \hat{\mu})\sqrt{n} \over \sqrt{\sigma^2}}\over \sqrt{{n \hat{\sigma}^2\over (n-1)\sigma^2}} } = {(\mu - \hat{\mu})\sqrt{n-1} \over \sqrt{\hat{\sigma}^2}} \sim t_{n-1}\\
>    $$
>    For $H_0$, we plug in $\mu = 0$, the true pivot is
>    $$
>    T_n = { -\sqrt{n-1} \hat{\mu} \over \sqrt{\hat{\sigma}^2}}
>    $$
>
> 3. For $\mu = 0$​, 
>    $$
>    \mathbf{P}_{(0,\sigma^2)}(\psi = 1) = \mathbf{P}_{(0,\sigma^2)}(T_n > S) = \mathbf{P}(Z > S) = \alpha ,\quad \text{where } Z \sim t_{n-1}\\
>    \implies S = q_{1-\alpha}(t_{n-1})
>    $$
>    For $\mu > 0$,
>    $$
>    \begin{aligned}
>    \mathbf{P}_{(\mu, \sigma^2)} (\psi = 1) &= \mathbf{P}_{(\mu, \sigma^2)} (T_n > S)\\
>    & = \mathbf{P}_{(\mu, \sigma^2)}({-\hat{\mu} \sqrt{n-1} \over \sqrt{\hat{\sigma}^2}} > S)\\
>    &=  \mathbf{P}_{(\mu, \sigma^2)}({(\mu-\hat{\mu}) \sqrt{n-1} \over \sqrt{\hat{\sigma}^2}} > S+{\mu \sqrt{n-1}\over \sqrt{\hat{\sigma}^2}})\\
>    &=  \mathbf{P}_{(\mu, \sigma^2)}(Z > S+{\mu \sqrt{n-1}\over \sqrt{\hat{\sigma}^2}}) \quad \text{where } Z \sim t_{n-1}\\
>    & \leq \mathbf{P}_{(\mu, \sigma^2)}(Z > S) = \alpha
>    \end{aligned}
>    $$
>    