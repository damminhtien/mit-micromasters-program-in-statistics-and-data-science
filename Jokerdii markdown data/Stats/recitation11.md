# Recitation 11. Review: Comparisons of Two Proportions

You are interested in comparing the proportions of people in their 20's that smoke in France and in the US. After you sample randomly and independently $n$​ people in their 20's in both countries, you observe that $N_{US}$​ sampled US Americans and $N_F$ sampled French are smokers. Based on such an experiment, how would you test whether there is a significant difference between the proportions of smokers in both countries ?

The formal definition of a **pivotal quantity** (or a **pivot**) is as follows. Let $X_1, ..., X_n$ be random samples and let $T_n$ be a function of $X$ and a parameter vector $\theta$. That is, $T_n$ is a function of $X_1, ...., X_n, \theta$. Let $g(T_n)$ be a random variable whose distribution is the same for all $\theta$. Then, $g$ is called a pivotal quantity or a pivot.

Let $X$​ be a random variable with mean $\mu$ and variance $\sigma^2$. Let $X_1, ..., X_n$ be i.i.d sample of $X$. Then,
$$
g_ n \triangleq \frac{\overline{X_ n} - \mu }{\sigma }
$$
is a **pivot** with $\theta = [\mu \ \ \sigma^2]^T$​​​ being the parameter vector. The notion of a parameter vector here is not to be confused with the set of parameters that we use to define a statistical model.

> **Solution:**
>
> According to the scenario, let $X_1, ..., X_n \stackrel{iid}{\sim} \text{Be}(p_x)$ and $Y_1, ..., Y_n  \stackrel{iid}{\sim} \text{Be}(p_y)$.  We have the hypothesis:
> $$
> H_0: p_X= p_Y, \ \ H_1: p_X \neq p_Y
> $$
>
> 1. First find the statistic $T_n(X_1, ...,X_n, Y_1, ..., Y_n)$​​​, and define hypothesis test $\psi = \mathbb{1}\{T_n > s\}$​​.
>
>    By LLN,
>    $$
>    \hat{p}_X = {1\over n} \sum^n_{i=1} X_i \xrightarrow[n \rightarrow \infty]{\mathbf{P}} p_X\\
>    \hat{p}_Y = {1\over n} \sum^n_{i=1} Y_i \xrightarrow[n \rightarrow \infty]{\mathbf{P}} p_Y\\
>    $$
>    Consider $\hat{p}_X-\hat{p}_Y = g(\hat{p}_X,\hat{p}_Y)$​,  $g(x,y) = x-y$​. By CLT,
>    $$
>    \sqrt{n} \left(\begin{pmatrix}\hat{p}_X \\\hat{p}_Y  \end{pmatrix} - \begin{pmatrix}\hat{p}_X \\\hat{p}_Y  \end{pmatrix} \right) \xrightarrow[n\rightarrow \infty]{D} \mathcal{N}(0,\Sigma)
>    $$
>    where $\begin{pmatrix}\hat{p}_X \\\hat{p}_Y  \end{pmatrix}  = {1\over n} \sum\limits^n_{i=1} \begin{pmatrix}X_i \\Y_i  \end{pmatrix}$​,  $\Sigma = \begin{pmatrix}p_X(1-p_X) & 0\\ 0 & p_Y(1-p_Y) \end{pmatrix}$​.​
>
>    **Delta** Method:
>    $$
>    \sqrt{n}\left(g(\hat{p}_X,\hat{p}_Y) - g({p}_X,{p}_Y)\right) \rightarrow \mathcal{N}(0, \nabla g({p}_X,{p}_Y)^T\Sigma \  g({p}_X,{p}_Y) )
>    $$
>    Let $\sigma^2_g = \nabla g({p}_X,{p}_Y)^T\Sigma \  g({p}_X,{p}_Y)$​, we know
>    $$
>    \nabla g(x,y) = \begin{pmatrix}1 \\ -1 \end{pmatrix}
>    $$
>    Then the covariance is
>    $$
>    \hat{\sigma}^2_g = (1 \ -1)\begin{pmatrix}p_X(1-p_X) & 0\\ 0 & p_Y(1-p_Y) \end{pmatrix} \begin{pmatrix}1 \\ -1 \end{pmatrix} = p_X(1-p_X) + p_Y(1-p_Y)
>    $$
>    Therefore, we have
>    $$
>    \sqrt{n} {(\hat{p}_X) - \hat{p}_Y) - (p_X - p_Y) \over \sqrt{p_X(1-p_X) + p_Y(1-p_Y)}} \xrightarrow[n \rightarrow \infty]{D} \mathcal{N}(0,1)
>    $$
>    For $H_0$​​, set $p_X = p_Y = p \in (0,1) $​​, thus $ p_X(1-p_X) + p_Y(1-p_Y) =  2p(1-p)$​​​.
>    $$
>    \hat{p} = {1\over 2} (\hat{p}_X + \hat{p}_Y) \xrightarrow[n \rightarrow \infty]{\mathbf{P}} P
>    $$
>    By **Slutsky's method**, 
>    $$
>    \sqrt{n} {\hat{p}_X-\hat{p}_Y \over \sqrt{2 \hat{p} (1-\hat{p})}} \xrightarrow[n\rightarrow \infty]{D} \mathcal{N}(0,1)
>    $$
>    Therefore,
>    $$
>    T_n =\left|\sqrt{n} {\hat{p}_X-\hat{p}_Y \over \sqrt{2 \hat{p} (1-\hat{p})}}\right| \xrightarrow[n\rightarrow \infty]{D} \mathcal{N}(0,1) \ \ \text{under } H_0: p_X = p_Y
>    $$
>
> 2. Second adjust $s$​ to guarantee asymptotic level $\alpha$​​.
>
>    Since we have to guarantee that when we cut off at level $s$, when we decide to reject the null hypothesis, that this, under the null hypothesis itself, has asymptotic probability $\alpha$. 
>    $$
>    \mathbf{P}(T_n > s) = \mathbf{P}(\sqrt{n} {\hat{p}_X-\hat{p}_Y \over \sqrt{2 \hat{p} (1-\hat{p})}}  >s) \xrightarrow[n\rightarrow \infty]{} \mathbf{P}(|Z| >s) = 2\cdot (1- \Phi(s))
>    $$
>    where $Z \sim \mathcal{N}(0,1)$​, $\Phi(s)$​ is the CDF of a standard normal random variable.​​
>
>    So $s = q_{\alpha/2}$, which is $1-\alpha/2$ quantile of $\mathcal{N}(0,1)$.
>
> 3. Then find the type II error.
>
>    We have consistency of estimators
>    $$
>    \hat{p}_X \xrightarrow[n \rightarrow \infty]{\mathbf{P}} p_X,\quad  \hat{p}_Y \xrightarrow[n \rightarrow \infty]{\mathbf{P}} p_Y,\quad \hat{p} = {1\over 2} (\hat{p}_X + \hat{p}_Y) \xrightarrow[n \rightarrow \infty]{\mathbf{P}} {1\over 2}(p_X + p_Y) =: \tilde{p}
>    $$
>    which means 
>    $$
>    T_n =\left|\sqrt{n} {\hat{p}_X-\hat{p}_Y \over \sqrt{2 \hat{p} (1-\hat{p})}}\right| =\left|\sqrt{n} {{p}_X-{p}_Y \over \sqrt{2 \tilde{p} (1-\tilde{p})}}\right| \xrightarrow[n \rightarrow \infty]{\mathbf{P}} + \infty\\
>    \implies \text{type II error} \xrightarrow[n\rightarrow \infty]{\mathbf{P}} 0
>    $$



