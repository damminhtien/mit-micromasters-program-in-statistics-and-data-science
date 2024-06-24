# Recitation 5. Inference for the variance of a Gaussian distribution

Consider a sample of $n$ i.i.d. Gaussian random variables $X_1,\ldots ,X_ n$ with known mean $\mu = 0$ and unknown variance $\sigma^2 > 0$.

1. Let $\hat\sigma ^2$ be the sample variance of $X_1,\ldots ,X_ n$. Recall an expression of $\hat\sigma ^2$.
2. Prove that $\hat\sigma ^2$ is a consistent estimator of $\sigma^2$.
3. Using the CLT, prove that ${\left(\frac{1}{n}\sum _{i=1}^ n X_ i,\frac{1}{n}\sum _{i=1}^ n X_ i^2\right)'}$ is asymptotically normal.
4. Conclude that $\hat\sigma ^2$ is asymptotically normal and compute its asymptotic variance.
5. Using the previous questions, find a C.I. for $\sigma^2$ with asymptotic level $95\%$ (use two methods).

> **Solution:**
>
> To find asymptotic C.I. for $\sigma^2$, we go through the following three steps:
>
> 1. Find estimator $\widehat{\sigma^2}$ for $\sigma^2$.
> 2. Determine the asymptotic distribution of $\widehat{\sigma^2}$
> 3. Construct C.I. based on $\widehat{\sigma^2}$.
>
> ---
>
> 1. Since $\mathsf{Var}(X_1) = \mathbb{E}[(X_1 - \mathbb{E}[X_1])^2]= \mathbb{E}[X_1^2] - (\mathbb{E}[X_1])^2$, the estimator can be written as
>    $$
>    \widehat{\sigma^2} = {1\over n} \sum_{i=1}^n X_i^2 - \left( {1 \over n} \sum^n_{i=1} X_i\right)^2
>    $$
>     $\widehat{\sigma^2}$ is **consistent** since by LLN, 
>    $$
>    {1\over n} \sum_{i=1}^n X_i^2  \xrightarrow[n\rightarrow \infty]{\mathbb P} \mathbb{E}[X_1^2]\\
>    {1\over n} \sum_{i=1}^n X_i  \xrightarrow[n\rightarrow \infty]{\mathbb P} \mathbb{E}[X_1]\\
>    \implies \widehat{\sigma^2} \xrightarrow[n\rightarrow \infty]{\mathbb P} \mathsf{Var}(X_1)
>    $$
>
> 2. Let $Y_1, ..., Y_n$ be i.i.d random variables, then by CLT.
>    $$
>    \sqrt{n} \left( {1\over n} \sum^n_{i=1} Y_i - \mathbb{E}[Y_1] \right) \xrightarrow[n \rightarrow \infty]{ (d)} \mathcal{N}(0, \mathsf{Var}(Y_1))
>    $$
>    Let $\begin{pmatrix}Y_1\\W_1 \end{pmatrix}, ..., \begin{pmatrix}Y_n\\W_n \end{pmatrix}$ be i.i.d random variables, then by 2D CLT.
>    $$
>    \sqrt{n} \left( \begin{pmatrix}{1\over n} \sum^n_{i=1} Y_i\\{1\over n} \sum^n_{i=1} W_i \end{pmatrix} - \begin{pmatrix} \mathbb{E}[Y_1]\\\mathbb{E}[W_1]\end{pmatrix} \right) \xrightarrow[n \rightarrow \infty]{ (d)} \mathcal{N}\left(\begin{pmatrix}0\\0 \end{pmatrix},\begin{pmatrix} \mathsf{Var}(Y_1)& \mathsf{Cov}(Y_1,W_1)\\\mathsf{Cov}(Y_1, W_1) &\mathsf{Var}(W_1) \end{pmatrix}\right)
>    $$
>    Let $Y_i = X_i^2, \quad W_i = X_i$, we now compute the covariance matrix.
>
>    $\mathsf{Var}(W_i) = \sigma^2\\\mathsf{Var}(Y_1) = \mathbb{E[(X_1^2)^2]} - (\mathbb{E}[X_1^2])^2  =3 \sigma^4 - (\sigma^2)^2 = 2 \sigma^4\\ \mathsf{Cov}(Y_1, W_1) = \mathbb{E}[X_1^2 X_1] - \mathbb{E}[X_1^2]\mathbb{E}[X_1] = 0 - \sigma^2 0 = 0$
>
>    To obtain the asymptotic distribution of $\widehat{\sigma^2} = {1\over n} \sum_{i=1}^n X_i^2 - \left( {1 \over n} \sum^n_{i=1} X_i\right)^2$ , we use **multivariate delta method**
>
>    Let $T_n = {1\over n} \sum^n_{i=1} \begin{pmatrix}X_i^2 \\ X_i\end{pmatrix},\quad \widehat{\sigma^2}=g(T_n),$ we can write
>    $$
>    \widehat{\sigma^2}=g(y,w) = y - w^2
>    $$
>    
>
>    Calculate the gradient
>    $$
>    \nabla g(y,w) = \begin{pmatrix} 1 \\ -2w \end{pmatrix}\\
>    $$
>    Calculate the mean
>    $$
>    \mathbb{E}[T_n] = \begin{pmatrix}\mathbb{E}[Y_1] \\ \mathbb{E}[W_1] \end{pmatrix} = \begin{pmatrix}\sigma^2 \\ 0\end{pmatrix}
>    $$
>    Therefore, applying **multivariate delta method**, we have
>    $$
>    \sqrt{n} (\widehat{\sigma^2}-\sigma^2 )\xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}\left(0, \begin{pmatrix}1\\0 \end{pmatrix}^T \begin{pmatrix}2\sigma^2 & 0\\0& \sigma^2 \end{pmatrix}\begin{pmatrix}1\\0 \end{pmatrix} \right) = \mathcal{N}(0,2\sigma^4)
>    $$
>
> 3. Write the **two-sided** C.I. as $\mathcal{I} = [\hat{\sigma}^2 - s, \hat{\sigma}^2 + s]$.
>    $$
>    \begin{aligned}
>    &\mathbf{P}\left(\sigma^2 \in \mathcal{I}\right)\\
>    \iff& \mathbf{P}\left(\sigma^2 \in \left[\widehat{\sigma^2}-s, \widehat{\sigma^2} + s\right]\right)\\
>    \iff& \mathbf{P}\left(\sigma^2- \widehat{\sigma^2} \in [-s, s]\right)\\
>    \iff& \mathbf{P}\left(\widehat{\sigma^2}-\sigma^2 \in [-s, s]\right)\\
>    \iff& \mathbf{P}\left(\sqrt{{n \over 2}} {\widehat{\sigma^2} - \sigma^2 \over  \sigma^2} \in \left[-\sqrt{{n\over 2}} \cdot {s\over\sigma^2 },\sqrt{{n\over 2}} \cdot {s\over\sigma^2 }\right]\right)
>    \end{aligned}
>    $$
>    Let $\sqrt{{n\over 2}} \cdot {s\over\sigma^2 } = q$, we can write
>    $$
>    \mathbf{P}\left(\sigma^2 \in \mathcal{I}\right) \xrightarrow[n\rightarrow \infty]{} \mathbf{P}(Z \in [-q,q])
>    $$
>    where $Z \sim \mathcal{N}(0,1)$.
>
>    With confidence level $\alpha$, we write
>    $$
>    \mathbf{P}(Z \in [-q,q]) = 1-\alpha
>    $$
>    We want $q = q_{\alpha/2}$, $1 - \alpha/2$ quantile of $\mathcal{N}(0,1)$.
>
>    Since $\sqrt{{n\over 2}} \cdot {s\over\sigma^2 } = q$, we can write $s $ as $s = q_{\alpha/2} {\sigma^2 \sqrt{2}\over \sqrt{n} }$.
>
>    Therefore the C.I. is
>    $$
>    \mathcal{I} = \widehat{\sigma^2} + \left[ -\sqrt{{2\over n}} q_{\alpha/2} \sigma^2,\sqrt{{2\over n}} q_{\alpha/2} \sigma^2 \right]
>    $$
>    By Slutsky's theorem, since
>    $$
>    \sqrt{n} {\widehat{\sigma^2} - \sigma^2 \over \sqrt{2} \widehat{\sigma^2}} \xrightarrow[x\rightarrow \infty]{(d)} \mathcal{N}(0,1)
>    $$
>    We can write the asymptotic C.I. as
>    $$
>    \mathcal{I} = \widehat{\sigma^2} + \left[ -\sqrt{{2\over n}} q_{\alpha/2} \widehat{\sigma^2},\sqrt{{2\over n}} q_{\alpha/2} \widehat{\sigma^2} \right]
>    $$

