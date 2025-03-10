# Recitation 6. Maximum Likelihood Estimator for Multinomial

Consider a finite space $E=\{ a_1,a_2,\ldots ,a_ r\}$ of size $r \geq 2$ and let $X$ be a random variable taking values in $E$. For $j = 1,..., r$, let $p_ j^*=\mathbf{P}[X=a_ j]$. Consider a sample of $n$ i.i.d. copies $X_1, ..., X_n$ of $X$. Based on this example, we would like to estimate the multivariate parameter $p^*=(p_1^*,\ldots ,p_ r^*)$.

1. What is the parameter space ?
2. Write the likelihood associated with the model described above.
3. Compute the maximum likelihood estimator $\hat{p}$ or $p^*$,
4. Using the CLT, show that $\hat{p}$ is asymptotically normal. Compute the asymptotic covariance matrix. Denote it by $\Sigma$.
5. Prove that $\Sigma$ is not invertible. Conclude that the theorem for the MLE could not have been applied here. What condition is not satisfied?

> **Solution:**
>
> 1. Parameter space $\{p_j \geq 0,\ \ \sum\limits^r_{j=1} p_j = 1\} = P$.
>
> 2. The likelihood is
>    $$
>    \begin{aligned}
>    L = \mathbf{P}(X_1 = x_1, ..., X_n = x_n) &=\prod_{i=1}^n \mathbb{P}(X_i = x_i)\\
>    &= \prod_{i=1}^n \prod_{j=1}^r p_j^{\mathbf{1}\{x_i = j\}}\\
>    &= \prod_{j=1}^r \prod_{i=1}^n  p_j^{\mathbf{1}\{x_i = j\}}\\
>    &=\prod_{j=1}^r  p_j^{\sum\limits_{i=1}^n\mathbf{1}\{x_i = j\}}\\
>    & = \prod_{j=1}^r  p_j^{T_j} 
>    \end{aligned}
>    $$
>    where $T_j =  \sum\limits_{i=1}^n\mathbf{1}\{x_i = j\}$.
>
>    The log likelihood is
>    $$
>    \log L = \log \mathbf{P}(X_1 = x_1, ..., X_n = x_n) = \log \prod^{r}_{j=1} p_j^{T_j} = \sum^r_{j=1} T_j \log p_j
>    $$
>
> 3. Let $f(p) = \log \prod^{r}_{j=1} p_j^{T_j} = \sum^r_{j=1} T_j \log p_j$. 
>
>    Calculating MLE:  $\max\limits_{p\in P} f(p) \ \iff \ \max f(p) \ s.t. \ h(p) = \sum\limits^r_{j=1}p_j - 1 = 0$.
>
>    Assume $T_j > 0, \ \ \forall j$.
>
>    Necessary conditions: $0 = \nabla f(\hat{p}) + \lambda \cdot \nabla h(\hat{p}), \ \lambda \in \R$.
>
>    If we set the necessary condition to be $0 = \nabla f(\hat{p})$, the partial derivative is 
>    $$
>    \partial _{p_j} f(p) = {T_j\over p_j } = 0, \ \text{when }p_j \rightarrow \infty
>    $$
>    Which is not correct since we have parameter space $\{p_j \geq 0,\ \ \sum\limits^r_{j=1} p_j = 1\} = P$.
>
>    So we set the necessary condition to be $0 = \nabla f(\hat{p}) + \lambda \cdot \nabla h(\hat{p}), \ \lambda \in \R$, applying **Lagrange multiplier**.
>    $$
>    \begin{aligned}
>    &\partial _{p_j} h(p) = 1\\
>    \implies&  0 = {T_j \over \hat{p}_j} + \lambda\\
>    \implies& \lambda \neq 0\\
>    \implies& \hat{p}_j = -{T_j \over \lambda}
>    \end{aligned}
>    $$
>    Plug it into the parameter space
>    $$
>    \begin{aligned}
>    1 = \sum^r_{j=1}\hat{p}_j &= \sum^r_{j=1}\left (-{T_j \over \lambda}\right) = - {1\over \lambda} \sum^r_{j=1} T_j = - {n \over \lambda}\\
>    &\implies  \lambda = -n\\
>    &\implies \hat{p}_j = {T_j \over n}
>    \end{aligned}
>    $$
>    To show that it is the global maximum, we show that the likelihood is concave. The second derivative of the likelihood is
>    $$
>    \partial_{p_k} \partial_{p_j} f(p) = \partial_{p_k} {T_j \over p_j} = \begin{cases}- { T_j\over p_j^2} & j = k \\ 0 & j \neq k \end{cases} \implies  \nabla^2 f(p) < 0  \implies f \ \text{is concave.}
>    $$
>    To handle the condition where $T_j = 0$. We use  **Karush-Kuhn-Tucker conditions**, a generalization of the Lagrange multiplier.
>    $$
>    \mathbf{P}(X_1 = x_1, ..., X_n = x_n) = \prod_{j=1}^r  p_j^{T_j} \implies  \hat{p}_j = {T_j \over n}
>    $$
>    which is the global maximum.
>
> 4. (1) The MLE is
>    $$
>    \hat{p}_j = {T_j \over n} = {1\over n} \sum^n_{i=1} \mathbf{1} \{x_i = j\}
>    $$
>    Let  $(Y_i)_j = \mathbf{1} \{x_i = j\}$, by CLT,
>    $$
>    \sqrt{n} (\hat{p} - \mathbb{E}[Y_1]) \xrightarrow[n \rightarrow \infty]{ (d)} \mathcal{N}(0, \mathsf{Cov}(Y_1))
>    $$
>    where $\mathbb{E}[(Y_i)_j] = \mathbb{E}[\mathbf{1}\{x_i = j\}] = \mathbf{P}(x_i = j) = p_j$, since $\mathbf{1} \{x_i = j\} \sim \mathsf{Ber}(p_j)$. Let $\Sigma = \mathsf{Cov}(Y_1)$.
>
>    Recall that the covariance matrix is
>    $$
>    \Sigma_{j,k} = \begin{cases}\mathsf{Var}(Y_1)_j, & j = k\\\mathsf{Cov}((Y_1)_j,(Y_1)_k), & j \neq k \end{cases}
>    $$
>    The variance of Bernoulli is
>    $$
>    \mathsf{Var}((Y_1)_j) = p_j(1-p_j)
>    $$
>    The expectation is
>    $$
>    \mathbb{E}[(Y_1)_j(Y_1)_k] = \mathbb{E}[\mathbf{1}\{x_1 = j\}\mathbf{1}\{x_1 = k\}] = 0
>    $$
>    The covariance is
>    $$
>    \mathsf{Cov}\left((Y_1)_j, (Y_1)_k\right ) = \mathbb{E}[(Y_1)_j, (Y_1)_k] - \mathbb{E}[(Y_1)_j]\mathbb{E}[(Y_1)_k] = 0 - p_j p_k, \ \ j \neq k
>    $$
>    Therefore, the covariance matrix is
>    $$
>    \Sigma_{j,k} = \begin{cases}p_j(1-p_j), & j = k\\- p_j p_k, & j \neq k \end{cases}
>    $$
>    (2) Another more disciplined way of calculating asymptotic covariance matrices for MLE.
>
>    Recall that
>    $$
>    \sqrt{n} (\hat{\theta} - \theta^*) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0, \mathcal{I}(\theta^*)^{-1})\\
>    \text{where }\ \mathcal{I}(\theta) = - \mathbb{E}[\nabla^2 f(\theta)]
>    $$
>    The Fisher information is
>    $$
>    \mathcal{I}(p)_{jk} = -\mathbb{E}[(\nabla^2\ f(p))_{jk}] = \begin{cases} {p_j \over p_j^2} = {1 \over p_j}, & j = k \\ 0, & j \neq k \end{cases}
>    $$
>    So the inverse is
>    $$
>    \mathcal{I}(p)_{jk}^{-1} = \begin{cases} {p_j} , & j = k \\ 0, & j \neq k \end{cases}
>    $$
>    This is NOTs equal to the asymptotic covariance matrix calculated previously
>    $$
>    \Sigma_{j,k} \neq \mathcal{I}(p)_{jk}^{-1}
>    $$
>
> 5. Now we have to check the assumptions.
>
>    (1) The model need to be identified. (Satisfied)
>
>    (2) The support of the probability distribution does depend on theta. (Satisfied)
>
>    (3) $\theta^*$ does not lie on the boundary of the parameter set $\Theta$. (Not satisfied)
>
>    (4) $\mathcal{I}(\theta)$ is invertible in a neighborhood of $\Theta^*$. (Not satisfied)
>
>    (5) Technical assumptions - continuous differential. 
>
>    To solve this problem, try
>    $$
>    \tilde{P} = \{p \in \R^{r-1}: p_j > 0, 1- \sum^{r-1}_{j=1}p_j > 0 \}\\
>    \tilde{\mathcal{I}}(p)^{-1}  = (\Sigma)_{j=1, ..., r-1; k = 1, ..., r-1}
>    $$
>    where $p_j > 0$ satisfies (4) and $1- \sum^{r-1}_{j=1}p_j > 0$ satisfies (3).
>
>    **Remark:** **Explanation of why $1- \sum^{r-1}_{j=1}p_j > 0$ satisfies (3):** 
>
>    If we consider the case where there are three options that occur with probabilities $p_1$, $p_2$, and $p_3$, the parameter space will be some subset of 3D space. A few examples of subsets of 3D space are volumes, such as spheres and cubes and pyramids. These examples of volumes all have interiors as well as boundaries (the boundaries are the surfaces that enclose the volumes; i.e., the surface of the sphere or the faces of the cube or pyramid). However, the surfaces themselves (just the boundaries of the volumes, excluding the interiors of the volumes) are also subsets of 3D space. Similarly, you could have a circle or a square floating in 3D space; these would certainly be subsets of 3D space, but would be surfaces rather than volumes.
>
>    The positivity constraints ($p_1, p_2, p_3 > 0$) lead to a parameter space that is a giant cube with its boundaries at $0$ and $\infty$ on all three axes. If these were our only constraints, then the requirement for our MLE theorem would be that none of the parameters are $0$ or $\infty$, i.e., that the true parameter $(p_1, p_2, p_3)$ is not on the boundary of our parameter space.
>
>    However, once we add the constraint $p_1 + p_2 + p_3 = 1$ , we say that the parameter space is the intersection of this plane and the cube described above. We get a triangle lying in the plane defined by $p_1 + p_2 + p_3 = 1$ with its three edges on the planes $p_1 = 0$, $p_2 = 0$, and $p_3 = 0$. (See it drawn here.)
>
>    ![reci6-boundary](../assets/images/reci6-boundary.png)
>
>    Since the parameter space is a triangle, it is a surface and it is "all boundary." Our theorem for MLE requires the true parameter to be a point on the interior of the parameter space volume, which is impossible when there is no real interior, as in our case.
>
>    Our real problem is that the equality constraint brings our parameter space down a dimension. We have $r$ variables, but only $r-1$ degrees of freedom, so our parameter space is a surface instead of a volume. If we could represent our problem in terms of only $r-1$ variables, we'd have a parameter space that was volume in $\R^{r-1}$. We can do that by inverting our equality constraint to solve for one of the variables in terms of the other $r-1$, then substituting that in to eliminate that variable and get down to only $r-1$.
>
>    Since our equality constraint is linear, the inversion is very easy; it's $p_r = 1 - \sum_{i=1}^{r-1}p_i$. Now, we need to express all our inequality constraints (we've already taken care of the equality constraint by the substitution) in terms of only $p_1, \ldots, p_{r-1}$. The first $r-1$ are simple: $p_i > 0 \forall i \in \{1,\ldots,r-1\}$. The last one is also not too bad; we're just substituting in our new expression for $p_r$ to get $1 - \sum_{i=1}^{r-1}p_i > 0$. With this substitution, our parameter space is a volume again and we've avoided the trouble of the parameter space being all boundary, since now the parameter space is a volume in $\R^{r-1}$ instead of a surface in $\R^r$.

