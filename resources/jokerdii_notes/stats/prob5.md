Problem set for Lec10.

# 1. Covariance

Compute the $\mathsf{Cov}(X,Y)$ in the following condition.

1. $X,Y$ have the joint probability density function $\,  f(x, y) = 1 , 0 < x < 1, x < y< x+1$. What is the $\mathsf{Cov}(X,Y)$?
2. $X \sim f(x) = \frac{1}{2b} e^{-|x|/b},\  x \in \mathbb {R},\  b > 0 $ and $Y = \textsf{sign}(X)$.
3. $\,  X \sim \textsf{Unif}(0,1) \,$ And given $Y \sim \textsf{Unif}(x,1) $.

> **Solution:** 
>
> 1. To find $\,  \textsf{Cov}(X, Y) = \mathbb E[XY] - \mathbb E[X]\mathbb E[Y] \,$, we need to find out the expectations of $X,Y,$ and $XY$. 
>
>    From the joint distribution, we can derive the marginal distribution: $\,  f_{X}(x) = \int _{x}^{x+1} 1 \  dy = \left.y\right|_{x}^{x+1} = 1 , x \in (0,1)$, and the conditional distribution $f(y|x) = \frac{f(x, y)}{f(x)} = 1, y \in (x,x+1)$.
>
>    On one hand, we have $\mathbb E[X] = \frac{1}{2}$: since $f_X(x)$ does not depend on $x$, this describes the density of a uniform random variable over $[0,1]$. On the other hand, for the mean of $Y$:
>    $$
>    \begin{aligned}
>    \mathbb E[Y\rvert {X}] &= \int _{x}^{x+1} y\ f(y|x)\  dy\\
>    &= \int _{x}^{x+1} y\  dy\\
>    &= \left.\frac{y^2}{2} \right|_{x}^{x+1}\\
>    &=  \frac{2x+1}{2}
>    \end{aligned}
>    $$
>    According to the **law of iterated expectations**,
>    $$
>    \begin{aligned}
>    \mathbb E[Y] &= \mathbb E[\mathbb E[Y\rvert {X}]]\\
>    &= \mathbb E[\frac{2X+1}{2}]\\
>    &= \int _{0}^1 \frac{2x+1}{2} \  dx\\
>    &= 1\\
>    \mathbb E[XY] &= \int _{0}^{1}x\ \mathbb{E}[X|Y]dx\\
>    &= \int _{0}^{1}x \left[\int _ x^{x+1} y\  dy\right]dx\\
>    &= \int _0^1 x\left.\frac{y^2}{2} \right|_{x}^{x+1} dx\\
>    &= \int _0^1\frac{2x^2+x}{2} \  dx\\
>    &= {7 \over 12}
>    \end{aligned}
>    $$
>    Therefore,
>    $$
>    \textsf{Cov}(X, Y) = \mathbb E[XY] - \mathbb E[X]\mathbb E[Y] = \frac{7}{12} - \frac{1}{2}\times 1 = \frac{1}{12}
>    $$
>
> 2. By symmetry, $ \mathbb E[X] = \int _{-\infty }^{\infty }\frac{x}{2b} e^{-|x|/b}\  dx = 0 $. $\mathbb E[Y] = (-1)\cdot P(X < 0) + 1\cdot P(X>0) = -\frac{1}{2} + \frac{1}{2} = 0 $.
>    $$
>    \begin{aligned}
>     \textsf{Cov}(X, Y) = \mathbb E[XY] &= \int _{-\infty }^{\infty } \frac{x\cdot \textsf{sign}(x)}{2b} e^{-|x|/b}\  dx\\
>     &= \int _0^{\infty } \frac{x}{b} e^{-x/b}\  dx
>    \end{aligned}
>    $$
>    We can think of this as the expectation of an **exponential** random variable $Z$ with parameter ${1\over b}$.
>    $$
>     \int _0^{\infty } \frac{x}{b} e^{-x/b}\  dx = \mathbb E[Z]=b 
>    $$
>    where $Z \sim \textsf{Exp}(\frac{1}{b})$.
>
> 3. To find $\,  \textsf{Cov}(X, Y) = \mathbb E[XY] - \mathbb E[X]\mathbb E[Y] \,$, we need to find out the expectations of $X,Y,$ and $XY$. 
>
>    Since $f(x, y) = f(y\rvert {x})f(x) = \frac{1}{1-x}$, we can obtain the expectation of $XY$:
>    $$
>    \begin{aligned}
>    \mathbb E[XY] &= \int _0^1\int _ x^1 \frac{1}{1-x}\cdot xy \  dydx\\
>    &= \int _0^1\frac{x}{1-x}\cdot \left.\frac{y^2}{2}\right|_{x}^1 \  dx\\
>    & =\int _0^1\frac{x}{1-x}( \frac{1}{2} - \frac{x^2}{2} ) \  dx\\
>    &= \frac{1}{2} \int _0^1(x+ x^2) \  dx\\
>    &= {5\over 12}
>    \end{aligned}
>    $$
>    And we compute other expectations
>    $$
>    \mathbb E[X] = \frac{1}{2}, \quad \mathbb E[Y\rvert {X}] = \frac{X+1}{2} 
>    $$
>    By the **law of iterated expectations**
>    $$
>    \mathbb E[Y] = \mathbb E[\mathbb E[Y\rvert {X}]] = \mathbb E[\frac{X+1}{2}] = \int _{0}^{1} \frac{x+1}{2} \  dx = \frac{3}{4}
>    $$
>    Therefore, we have the covariance
>    $$
>    \textsf{Cov}(X,Y) = \mathbb E[XY] - \mathbb E[X]\mathbb E[Y] = \frac{5}{12} - \frac{1}{2}\times \frac{3}{4} = \frac{1}{24}
>    $$

# 2. A Simple Singular Covariance Matrix

Suppose $\mathbf X$ is a random vector, where $\mathbf{X}= (X^{(1)},\ldots ,X^{(d)})^ T$, with mean $0$ and covariance matrix $\mathbf{v}\mathbf{v}^ T$, for some vector $\mathbf{v}\in \mathbb {R}^ d$.

1. If $d >1$, is the covariance matrix $\mathbf{v}\mathbf{v}^ T$ invertible?

2. Let $\mathbf u$ be a vector in $\R^d$ such that $\mathbf{u}\perp \mathbf{v}$, i.e. $ \mathbf{u}\cdot \mathbf{v}=\mathbf{u}^ T \mathbf{v}=\mathbf{v}^ T \mathbf{u}=0$.

   Find the variance of $\mathbf{u}^ T\mathbf{X}$.

3. Let $\overline{\mathbf{v}} = \frac{\mathbf{v}}{\|  \mathbf{v}\| }$ (i.e. $\overline{\mathbf{v}}$ is the normalized version of $\mathbf{v}$). What is the variance of $ \overline{\mathbf{v}}^ T \mathbf{X}$?

4. Suppose we observe $n$ independent copies of $\mathbf{X}$ and call them $\mathbf{X}_1, ..., \mathbf{X}_ n$. What is the asymptotic distribution of $\overline{\mathbf{X}}_ n=\frac{\sum _{i=1}^ n \mathbf{X}_ i}{n} $?

5. Let $\mathbf{Y}_ i= \overline{\mathbf{v}}(\overline{\mathbf{v}}^ T\mathbf{X}_ i)$, or equivalently $\overline{\mathbf{v}}(\overline{\mathbf{v}}\cdot \mathbf{X}_ i)=(\overline{\mathbf{v}}\cdot \mathbf{X}_ i)\overline{\mathbf{v}}$, where $\overline{\mathbf{v}} = \frac{\mathbf{v}}{\|  \mathbf{v}\| }$ is the same as in part (3). We will compare the asymptotic distribution of $\overline{X}_n$ you obtain in part (4) to the asymptotic distribution of $\overline{Y}_n$ where $\overline{\mathbf{Y}}_ n=\frac{\sum _ i^ n \mathbf{Y}_ i}{n}$. What is the expectation $\mathbb E[\mathbf{Y}_i]$ of $\mathbf{Y}_i$? Find the covariance matrix $\Sigma _{\mathbf{Y}_ I}$ of $\mathbf{Y}_i$ in terms of the vector $\mathbf{v}$.

> **Solution:**
>
> 1. For $d > 1$, the matrix $\mathbf{v}\mathbf{v}^ T$ where $\mathbf{v}$ is a vector in $\R^d$ is not invertible.
>
>    Take an example in $2$ dimensions
>    $$
>    \mathbf{v}=\begin{pmatrix} 1\\ 0\end{pmatrix} \implies \mathbf{v}\mathbf{v}^ T\, =\, \begin{pmatrix} 1& 0\\ 0& 0\end{pmatrix}
>    $$
>    The matrix $\begin{pmatrix} 1& 0\\ 0& 0\end{pmatrix}$ is not invertible. One way to see this is that its determinant is $1(0)-(0)(0)= 0$. Another way to see it is that for any $2\times 2$ matrix $\begin{pmatrix}  a& b\\ c& d\end{pmatrix}$:
>    $$
>    \begin{pmatrix} 1& 0\\ 0& 0\end{pmatrix}\begin{pmatrix}  a& b\\ c& d\end{pmatrix} = \begin{pmatrix} a& b\\ 0& 0\end{pmatrix}\neq \begin{pmatrix} 1& 0\\ 0& 1\end{pmatrix}.
>    $$
>    In fact, the above argument works in general after a change of variables. Given $\mathbf{v}\in \mathbb {R}^ d$, change coordinates of $\R^d$ so that the first axis points in the direction of $\mathbf{v}$ (and so that $\mathbf{v}$ has unit length). In this new coordinate system, $\mathbf{v}$ can be rewritten as $\begin{pmatrix} 1\\ 0\\ \vdots \\ 0\end{pmatrix},$ and the matrix
>    $$
>    \begin{pmatrix} 1\\ 0\\ \vdots \\ 0\end{pmatrix}\begin{pmatrix} 1& 0& \ldots & 0\end{pmatrix} = \begin{pmatrix} 1& 0& \ldots & 0\\ 0& & & \\ \vdots & & \ddots & \vdots \\ 0& & \ldots & 0\end{pmatrix}
>    $$
>    is not invertible because no $d \times d$ matrix when multiplied by it will give the identity matrix.
>
> 2. Given two vectors, $\mathbf{u, X} \in \R^d$, the inner product $\mathbf{u^T X}$ is a scalar, and its variance is also a scalar. Using the covariance matrix formula, we get
>    $$
>    \begin{aligned}
>    \textsf{Var}(\mathbf{u}^ T \mathbf{X}) \, =\, \textsf{Cov}(\mathbf{u}^ T \mathbf{X}) &=\mathbf{u}^ T \textsf{Cov}(\mathbf{X}) \mathbf{u}\\
>    &=  \mathbf{u}^ T(\mathbf{v}\mathbf{v}^ T)\mathbf{u}\\
>    &=(\mathbf{u}^ T\mathbf{v})(\mathbf{v}^ T\mathbf{u})\, \\
>    &=\, 0.
>    \end{aligned}
>    $$
>
> 3. Similarly,
>    $$
>    \begin{aligned}
>    \textsf{Var}(\overline{\mathbf{v}}^ T \mathbf{X})\, =\,  \textsf{Cov}(\overline{\mathbf{v}}^ T \mathbf{X}) &= \overline{\mathbf{v}}^ T \textsf{Cov}(X) \overline{\mathbf{v}}\\
>    &=  \left(\frac{\mathbf{v}}{\left\|  \mathbf{v} \right\| }\right)^ T(\mathbf{v}\mathbf{v}^ T)\left(\frac{\mathbf{v}}{\left\|  \mathbf{v} \right\| }\right)\\
>    &= \frac{(\mathbf{v}^ T\mathbf{v})(\mathbf{v}^ T\mathbf{v})}{\left\|  \mathbf{v} \right\| ^2}\,\\
>    &=\, \left\|  \mathbf{v} \right\| ^2.
>    \end{aligned}
>    $$
>
> 4. By multivariate CLT,
>    $$
>    \sqrt{n}(\overline{\mathbf{X}}_ n - \mathbf{0}) \xrightarrow [n\rightarrow \infty ]{(d)} \mathcal{N}(\mathbf{0}, \mathbf{v}\mathbf{v}^ T)
>    $$
>    However, $\mathbf{v}\mathbf{v}^ T$ is not invertible, so the pdf of $ \mathcal{N}(\mathbf{0}, \mathbf{v}\mathbf{v}^ T)$ is not given by the usual formula that involves the inverse of the determinant of the covariance matrix of the multivariate Gaussian variable.
>
> 5. The expectation $\mathbb E[\mathbf{Y}_ i]$ is
>    $$
>    \mathbb E[\mathbf{Y}_ i] = \mathbb E[\overline{\mathbf{v}}(\overline{\mathbf{v}}^ T\mathbf{X}_ i)] = \overline{\mathbf{v}}\overline{\mathbf{v}}^T \  \mathbb E[\mathbf{Y}_ i]  = 0
>    $$
>    which is a zero vector in $\R^d$.
>
>    Since $ \mathbf{Y}_ i= \overline{\mathbf{v}}(\overline{\mathbf{v}}^ T\mathbf{X}_ i)$, the covariance matrix of $\mathbf{Y}_i$ is
>    $$
>    \begin{aligned}
>    \textsf{Cov}(\mathbf{Y}_ i) &=\overline{\mathbf{v}}\overline{\mathbf{v}}^ T\textsf{Cov}(\mathbf{X}_ i)(\overline{\mathbf{v}}\overline{\mathbf{v}}^ T)^ T\\
>    &=\overline{\mathbf{v}}\overline{\mathbf{v}}^ T\mathbf{v}\mathbf{v}^ T(\overline{\mathbf{v}}\overline{\mathbf{v}}^ T)^ T\\
>    &= \frac{\mathbf{v}(\mathbf{v}^ T\mathbf{v}\mathbf{v}^ T\mathbf{v})\mathbf{v}^ T }{\left\|  \mathbf{v} \right\| ^4}\, \\
>    &=\, \mathbf{v}\mathbf{v}^ T.
>    \end{aligned}
>    $$
>    This implies
>    $$
>    \sqrt{n}(\overline{\mathbf{Y}}_ n - \mathbf{0}) \, =\,  \sqrt{n}(\overline{\mathbf{Y}}_ n ) \xrightarrow [n\rightarrow \infty ]{(d)} \mathcal{N}(\mathbf{0}, \textsf{Cov}(\mathbf{Y}_ i))=\mathcal{N}(\mathbf{0},\mathbf{v}\mathbf{v}^ T).
>    $$
>    Observe that $\mathcal{N}(\mathbf{0},\mathbf{v}\mathbf{v}^ T)$ is also the asymptotic distribution of $\overline{X}_n$. 

# 3. Asymptotic Variance

Let $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim }\mathcal{N}(0,\sigma ^2)$, for some $\sigma^2 > 0$. Let
$$
\widehat{\sigma ^2}=\frac{1}{n}\sum _{i=1}^ n X_ i^2, \quad \text {and} \quad \widetilde{\sigma ^2}=\frac{1}{n}\sum _{i=1}^ n(X_ i-\overline{X}_ n)^2.
$$
Argue that both proposed estimators $\widehat{\sigma ^2}$ and $ \widetilde{\sigma ^2}$ below are consistent and asymptotically normal.

Then, give their asymptotic variances $V(\widehat{\sigma ^2})$ and $V(\widetilde{\sigma ^2})$ and decide if one of them is always bigger than the other.

> **Solution:**
>
> Note that 
> $$
> \widehat{\sigma ^2} = \overline{Y}_ n, \quad \text {for } Y_ i = X_ i^2.
> $$
> By the **LLN**,
> $$
> \overline{Y}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[Y_1] = \sigma ^2.
> $$
> By the **CLT**,
> $$
> \sqrt{n} (\overline{Y}_ n - \sigma ^2) \sim \mathcal{N}(0,\textsf{Var}(Y_1)) = \mathcal{N}(0,2 (\sigma ^2)^2),
> $$
> hence,
> $$
> V(\widehat{\sigma ^2}) = 2(\sigma ^2)^2.
> $$
> For $\widetilde{\sigma ^2}$, first observe that we can write it as
> $$
> \begin{aligned}
> \widetilde{\sigma ^2} &= \frac{1}{n} \sum _{i = 1}^ n (X_ i - \overline{X}_ n)^2\\
> &= \frac{1}{n} \sum _{i = 1}^{n} (X_ i^2 - 2 \overline{X}_ n X_ i + \overline{X}_ n^2)\\
> &= \frac{1}{n}\left( \sum _{i = 1}^{n} X_ i^2 \right) - \overline{X}_ n^2 = \widehat{\sigma ^2} - \overline{X}_ n^2.
> \end{aligned}
> $$
> Again, by the **LLN**,
> $$
> \overline{X}_ n^2 \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[X_1]^2 = 0,
> $$
> So
> $$
> \widetilde{\sigma ^2} = \widehat{\sigma ^2} - \overline{X}_ n^2 \xrightarrow [n \to \infty ]{\mathbf{P}} \sigma ^2.
> $$
> Now, we can consider $\widetilde{\sigma ^2}$ as
> $$
> \widetilde{\sigma ^2} = g \left( \frac{1}{n} \sum _{i=1}^{n} \begin{pmatrix}  X_ i\\ X_ i^2 \end{pmatrix} \right),
> $$
> where
> $$
> g(x, y) = y - x^2.
> $$
> By the above, we have a **multidimensional CLT** for the first and second moments of a Gaussian together,
> $$
> \sqrt{n} \left[ \begin{pmatrix}  \overline{X}_ n\\ \overline{Y}_ n \end{pmatrix} - \begin{pmatrix}  0\\ \sigma ^2 \end{pmatrix}\right] \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}\left( \begin{pmatrix}  0\\ 0 \end{pmatrix}, \begin{pmatrix}  \sigma ^2 &  0\\ 0 &  2(\sigma ^2)^2 \end{pmatrix}\right),
> $$
> where the $0$ s off the diagonal come from the fact that
> $$
> \mathbb E[X_ i \times X_ i^2] = \mathbb E[X_ i^3] = 0.
> $$
> Now, apply the **multidimensional Delta Method**, computing
> $$
> Dg(x,y) = \begin{pmatrix}  -2x &  1 \end{pmatrix},
> $$
> to obtain
> $$
> \begin{aligned}
> \sqrt{n} (\widetilde{\sigma ^2} - \sigma ^2) \xrightarrow [n \to \infty ]{\mathrm{(D)}} & \mathcal{N}\left( 0, Dg(0, \sigma ^2) \begin{pmatrix}  \sigma ^2 &  0\\ 0 &  2 (\sigma ^2)^2 \end{pmatrix} Dg(0, \sigma ^2)^\top \right)\\
> =& \mathcal{N}\left( 0, \begin{pmatrix}  0 &  1 \end{pmatrix}\begin{pmatrix}  \sigma ^2 &  0\\ 0 &  2 (\sigma ^2)^2 \end{pmatrix}\begin{pmatrix}  0\\ 1 \end{pmatrix} \right) = \mathcal{N}(0, 2 (\sigma ^2)^2).
> \end{aligned}
> $$
> Combined, we see that both estimators have the same asymptotic variance.

# 4. Maximum Likelihood Estimator for Curved Gaussian

Let $X_1, \dots , X_ n$ be $n$ i.i.d. random variables with distribution $\mathcal{N}(\theta, \theta)$ for some unknown $\theta > 0$.

1. Compute the MLE $\hat{\theta}$ for $\theta$ in terms of the sample averages of the linear and quadratic means, i.e. $\overline{X}_n$ and $\overline{X^2_n}$.

There are two methods to compute the asymptotic variance of $\hat{\theta}$. One is applying the **CLT** and the **1-dimensional Delta method**. The other is using the **Fisher information**.

2. First, compute the limit to which $ \overline{X_ n^2}$ converges in probability, also known as its **P-limit**.
3. What is the asymptotic variance $V(\overline{X_ n^2})$ of $\overline{X_n^2}$, which is equal to $\mathsf{Var}(X_1^2)$?
4. Now, write $\hat{\theta}$ as the function of $\overline{X_n^2}$ you found in (1) as $\hat\theta = g( \overline{X_ n^2} )$ and give its first derivative $g'(x)$.
5. What can you conclude about the asymptotic variance $V(\hat\theta ) $ of $\hat{\theta}$?

> **Solution:**
>
> 1. The log likelihood is
>    $$
>    \begin{aligned}
>    \ell _ n(\theta ) &= \sum _{i=1}^{n} \log \left[ \frac{1}{\sqrt{2 \pi \theta }} \exp \left( -\frac{(X_ i-\theta )^2}{2 \theta } \right) \right]\\
>    &= -\frac{n}{2} \left( \log (2) + \log (\pi ) + \log (\theta ) \right) - \sum _{i=1}^{n} \frac{(X_ i - \theta )^2}{2 \theta }\\
>    &= -\frac{n}{2} \left( \log (2) + \log (\pi ) + \log (\theta ) \right) - \sum _{i=1}^{n} \left[ \frac{1}{2 \theta } X_ i^2 - X_ i + \frac{1}{2} \theta \right].
>    \end{aligned}
>    $$
>    Differentiating yields 
>    $$
>    \frac{d}{d \theta } \ell (\theta ) = - \frac{n}{2 \theta } + \frac{1}{2 \theta ^2} \sum _{i=1}^{n} X_ i^2 - \frac{n}{2},
>    $$
>    which we set to zero to obtain the equation
>    $$
>    \hat\theta ^2 +\hat\theta - \frac{1}{n} \sum _{i=1}^{n} X_ i^2 = 0.
>    $$
>    Employing the quadratic formula and picking the result that gives a positive $\hat{\theta}$ then leads to
>    $$
>    \hat\theta = -\frac{1}{2} + \frac{1}{2} \sqrt{4 \overline{X_ n^2} + 1}.
>    $$
>
> 2. Compute the limit by the LLN,
>    $$
>    \overline{X_ n^2} \xrightarrow [n \to \infty ]{\mathrm{\mathbf{P}}} \mathbb E[X_1^2] = \textsf{Var}(X_1) + \mathbb E[X_1]^2 = \theta + \theta ^2.
>    $$
>    
>
> 3. Compute the asymptotic variance by the CLT,
>    $$
>    \sqrt{n} (\overline{X_ n^2} - (\theta + \theta ^2)) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, \textsf{Var}(X_1^2)),
>    $$
>    and
>    $$
>    \begin{aligned}
>     \mathsf{Var}(\overline{X_n^2}) = \textsf{Var}(X_1^2) &= \mathbb E[X_1^4] - \mathbb E[X_1^2]^2\\
>     &= \mathbb E[(\theta + \sqrt{\theta }Z)^4] - (\theta + \theta ^2)^2\\
>     &= \theta ^4 + 4 \theta ^3 \sqrt{\theta } \underbrace{\mathbb E[Z]}_{= 0} + 6 \theta ^2 \theta \underbrace{\mathbb E[Z^2]}_{= 1} + 4 \theta \sqrt{\theta }^3 \underbrace{\mathbb E[Z^3]}_{= 0} + \theta ^2 \underbrace{\mathbb E[Z^4]}_{= 3} - \theta ^4 - 2 \theta ^3 - \theta ^2\\
>     &= 2 \theta ^2 (2 \theta + 1)
>    \end{aligned}
>    $$
>    where $Z \sim \mathcal{N}(0,1)$ is a standard Normal variable.
>
> 4. From the previous part, we get
>    $$
>    g(x) = \frac{1}{2} \left( \sqrt{4 x + 1} - 1 \right),
>    $$
>    so
>    $$
>    g'(x) = \frac{1}{\sqrt{4 x + 1}}.
>    $$
>
> 5. Finally, by the Delta Method,
>    $$
>    \sqrt{n}(g(\overline{X_ n^2}) - g(\theta + \theta ^2)) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, 2 \theta ^2 (2 \theta + 1) g'(\theta + \theta ^2)^2) = \mathcal{N}\left(0, \frac{2 \theta ^2}{2 \theta + 1}\right).
>    $$
>    So 
>    $$
>    \mathsf{Var}(\hat{\theta}) =\frac{2 \theta ^2}{2 \theta + 1}
>    $$





 



