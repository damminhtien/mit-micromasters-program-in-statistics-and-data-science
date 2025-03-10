# Recitation 9. (Review) Multivariate Gaussian

The PDF of the **bivariate Gaussian distribution** is
$$
f(x, y, \mu_x, \mu_y, \sigma_x^2, \sigma_y^2, \rho) = {1 \over 2\pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp\left[ -{1\over 2(1-\rho^2)} \left( {(x - \mu_x)^2 \over \sigma_x^2} + {(y - \mu_y)^2 \over \sigma_y^2}- {2\rho(x - \mu_x)(y - \mu_y) \over \sigma_x \sigma_y} \right) \right].
$$
The PDF for the general $d$​​​​​-dimensional **multivariate Gaussian distribution** with mean $\mathbf{\mu}$​​​​​ and covariance matrix $\mathbf{\Sigma}$​​​​​ is given by
$$
f(\mathbf{x};\mu, \mathbf{\Sigma}) = {1\over (2\pi)^{d/2} \det(\Sigma)^{1/2}} \exp \left[ -{1\over 2} (\mathbf{x} - \mu)^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mu) \right].
$$

1. Show that the marginal distribution of $X$​​​ and $Y$​​​ are $\mathcal{N}(\mu_x, \sigma_x^2)$​​​ and $\mathcal{N}(\mu_y, \sigma_y^2)$​​.
2. What is $\rm{Cov}(X,Y)$?
3. Show that $X$ and $Y$ can equivalently be defined in the following way. Let $Z_1$ and $Z_2$ be independent $\mathcal{N}(0,1)$ random variables. Then $X = \sigma_x Z_1 + \mu_x$ and $Y = \sigma_y[\rho Z_1 + \sqrt{1-\rho^2} Z_2]+ \mu_y$.
4. Show that the multivariate case in (2) reduces to the PDF in (1) when $d=2$.

> **Solution:**
>
> 1. Notice that
>    $$
>    {1\over (1-\rho^2)} \left( {(x- \mu_x)^2\over \sigma_x^2}  + {(y-\mu_y)^2 \over \sigma_y^2}-{ 2 \rho (x - \mu_x)(y - \mu_y) \over \sigma_x \sigma_y}\right) = {(x - a(y))^2 \over (1-\rho^2)\sigma_x^2}  + {(y - \mu_y)^2 \over \sigma_y^2}
>    $$
>    where $a(y) = \mu_x + \rho {\sigma_x \over \sigma_y}(y - \mu_y)$​​. Therefore, the marginal distribution of $y$ is
>    $$
>    \begin{aligned}
>    f(y; \mu_x, \mu_y, \sigma_x^2, \sigma_y^2, \rho)&= \int{1\over 2\pi \sigma_x \sigma_y \sqrt{1-\rho^2}} \exp\left[ - {1\over 2(1-\rho^2)} \left({(x-\mu_x)^2 \over \sigma_x^2 } + {(y-\mu_y)^2 \over \sigma_y^2 }-{2\rho(x-\mu_x)(y-\mu_y) \over \sigma_x \sigma_y } \right)\right] dx\\
>    &={1\over \sqrt{2\pi}\sigma_y} \exp \left[ -{1 \over2 } { (y - \mu_y)^2\over \sigma_y^2} \right] \int {1\over \sqrt{2\pi} \sigma_x \sqrt{1-\rho^2}} \exp \left( - {1\over 2} {(x - a(y))^2 \over (1-\rho^2)\sigma_x^2} \right)dx\\
>    &= {1\over \sqrt{2\pi}\sigma_y} \exp\left[ -{1\over 2} {(y-\mu_y)^2 \over \sigma_y^2} \right].
>    \end{aligned}
>    $$
>    This means $Y \sim \mathcal{N}(\mu_y, \sigma_y^2), \ \ X \sim \mathcal{N}(\mu_x, \sigma_x^2)$​​​​.
>
> 2. We have
>    $$
>    \text{Cov}(X,Y) = \mathbb{E}(XY) - \mathbb{E}(X) \mathbb{E}(Y)
>    $$
>    Since the marginal distributions are $\mathcal{N}(\mu_x, \sigma_x^2)$​​​ and $\mathcal{N}(\mu_y, \sigma_y^2)$​​​, we know that $\mathbb{E}[X] = \mu_x$​​​ and $\mathbb{E}[Y] = \mu_y$​​​. Using the answer to (1), the random variable $X|Y$​​ has PDF
>    $$
>    f(X=x | Y=y) \propto \exp \left[ -{1\over 2} {(x - a(y))^2 \over \sigma_x^2(1-\rho^2)} \right]
>    $$
>    where again $a(y) = \mu_x + \rho {\sigma_x \over \sigma_y}(y - \mu_y)$. Thus, $X|Y \sim \mathcal{N}(a(Y), \sigma_x^2(1-\rho^2))$.
>
>    The law of total expectation yields
>    $$
>    \begin{aligned}
>    \mathbb{E}[XY] &= \mathbb{E}[\mathbb{E}(XY|Y)] \\
>    &= \mathbb{E}\left[ Y \left( \mu_x + \rho {\sigma_x \over \sigma_y}(Y - \mu_y) \right)\right]\\
>    &= \mathbb{E}\left[Y \mu_x + \rho {\sigma_x \over \sigma_y}(Y^2 - Y \mu_y)\right]\\
>    &= \mu_y \mu_x  +\rho {\sigma_x \over \sigma_y} (\sigma_x^2 + \mu_y^2 - \mu_y^2)\\
>    &= \mu_y \mu_x + \rho \sigma_x \sigma_y
>    \end{aligned}
>    $$
>    Therefore, the covariance is
>    $$
>    \text{Cov}(X,Y) = \mathbb{E}(XY) - \mathbb{E}(X) \mathbb{E}(Y) = \mu_y \mu_x + \rho \sigma_x \sigma_y -\mu_y \mu_x = \rho \sigma_x \sigma_y
>    $$
>    The correlation is
>    $$
>    \text{Corr}(X,Y) = \rho
>    $$
>
> 3. Show that marginal distribution of $X$ and $Y$ are $\mathcal{N}(\mu_x, \sigma_x^2)$ and $\mathcal{N}(\mu_y, \sigma_y^2)$​.
>
>    The expectations:
>    $$
>    \begin{aligned}
>    \mathbb{E}(X) &= \mathbb{E}(\sigma_xZ_1 + \mu_X) = \mathbb{E}(\sigma_xZ_1)+ \mathbb{E}(\mu_x) = \mu_x\\
>    \mathbb{E}(Y) &= \mathbb{E}(\sigma_y(\rho Z_1 + \sqrt{1-p^2}Z_2 )+ \mu_y) = \mathbb{E}(\sigma_y \rho Z_1)  +\mathbb{E}(\sigma_y \sqrt{1-\rho^2}Z_2) + \mathbb{E}(\mu_y) = \mu_y
>    \end{aligned}
>    $$
>    The variances:
>    $$
>    \begin{aligned}
>    \text{Var}(X) &= \text{Var}(\sigma_x Z_1 + \mu_x)\\
>    &= \text{Var}(\sigma_x Z_1)\\
>    &= \sigma_x^2 \text{Var}(Z_1)\\
>    &= \sigma_x^2\\
>    \text{Var}(Y) &= \text{Var}(\sigma_y\rho Z_1  +\sigma_y \sqrt{1-\rho^2}Z_2)\\
>    &= \text{Var}(\sigma_y \rho Z_1) + \text{Var}(\sigma_y \sqrt{1-\rho^2} Z_2)\\
>    &= \sigma_y^2 \rho^2 + \sigma_y^2(1-\rho^2)\\
>    &= \sigma_y^2
>    \end{aligned}
>    $$
>    The covariance:
>    $$
>    \begin{aligned}
>    \text{Cov}(X,Y) &= \text{Cov}(\sigma_x Z_1 +\mu_x, \sigma_y (\rho Z_1 + \sqrt{1-\rho^2} Z_2) + \mu_y)\\
>    &= \text{Cov}(\sigma_x Z_1, \sigma_y \rho Z_1 + \sigma_y\sqrt{1-\rho^2} Z_2)\\
>    &=\text{Cov}(\sigma_x Z_1 , \sigma_y \rho Z_1) + \text{Cov}(\sigma_x Z_1 ,\sigma_y\sqrt{1-\rho^2} Z_2)\\
>    &= \sigma_x \sigma_y \rho \text{Cov}(Z_1, Z_1) + \sigma_x \sigma_y \sqrt{1-\rho}\ \text{Cov}(Z_1, Z_2)\\
>    &= \sigma_x \sigma_y \rho \text{Var}(Z_1) + 0\\
>    &= \sigma_x \sigma_y \rho 
>    \end{aligned}
>    $$
>    As we see, this completely specifies the parameters of the bivariate Gaussian distribution, and therefore $(X, Y)$​​ has the distribution specified in (1).
>
> 4. First, recall that for a matrix
>    $$
>    A = \begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}
>    $$
>    we have
>    $$
>    \det(A) = a_{11} a_{22} - a_{21} a_{22}, \quad A^{-1} = {1\over \det(A)}\ \begin{pmatrix}a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix}
>    $$
>    When $d=2$​​, let $x = \begin{pmatrix}X \\ Y \end{pmatrix}$​​ , $\mu = \begin{pmatrix}\mu_x \\ \mu_y \end{pmatrix}$​​, 
>
>    Let
>    $$
>    \mathbf{\Sigma} = \begin{pmatrix}\text{Cov}(X,X) & \text{Cov}(X,Y) \\ \text{Cov}(Y,X) & \text{Cov}(Y,Y)\end{pmatrix}= \begin{pmatrix}\sigma_x^2 & \rho\sigma_x \sigma_y \\ \rho\sigma_x \sigma_y & \sigma_y^2\end{pmatrix}
>    $$
>    which is the covariance matrix in the bivariate case. Its inverse is
>    $$
>    \mathbf{\Sigma}^{-1} = {1\over (1-\rho)^2 \sigma_x^2 \sigma_y^2}\ \begin{pmatrix}\sigma_y^2 & -\rho\sigma_x \sigma_y \\ -\rho\sigma_x \sigma_y & \sigma_x^2\end{pmatrix}
>    $$
>    where $(1-\rho)^2 \sigma_x^2 \sigma_y^2 = \det(\mathbf{\Sigma})$​​​​​. 
>
>    Let $\mathbf{X}=(X,Y)^T$ be​ the two-dimensional multivariate Gaussian random vector, and $\mathbf{x} =(x,y)^T$. Then,
>    $$
>    \begin{aligned}
>    (\mathbf{x} - \mu)^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mu) &= \left( \begin{pmatrix}X \\ Y \end{pmatrix} - \begin{pmatrix}\mu_x \\ \mu_y \end{pmatrix}\right)^T {1\over (1-\rho)^2 \sigma_x^2 \sigma_y^2}\ \begin{pmatrix}\sigma_y^2 & -\rho\sigma_x \sigma_y \\ -\rho\sigma_x \sigma_y & \sigma_x^2\end{pmatrix} \left( \begin{pmatrix}X \\ Y \end{pmatrix} - \begin{pmatrix}\mu_x \\ \mu_y \end{pmatrix}\right)\\
>    &= {1\over (1-\rho)^2 \sigma_x^2 \sigma_y^2} \begin{pmatrix}X - \mu_x \\ Y - \mu_y \end{pmatrix}^T \ \begin{pmatrix}\sigma_y^2 (x - \mu_x) & -\rho\sigma_x \sigma_y (y - \mu_y) \\ -\rho\sigma_x \sigma_y(x - \mu_x) & \sigma_x^2(y - \mu_y)\end{pmatrix}\\
>    &= -{1\over 2(1- \rho^2)} \left[ {(x- \mu_x)^2\over \sigma_x^2}  + {(y-\mu_y)^2 \over \sigma_y^2}-{ 2 \rho (x - \mu_x)(y - \mu_y) \over \sigma_x \sigma_y} \right]
>    \end{aligned}
>    $$

