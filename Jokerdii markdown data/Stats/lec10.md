# Lecture 10. Consistency of MLE, Covariance Matrices, and Multivariate Statistics

There are 8 topics and 5 exercises.

## 1. Maximum Likelihood Estimator of Uniform Statistical Model

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Unif}[0, \theta ^*]$ where $\theta^*$ is an unknown parameter. We constructed the associated statistical model $(\mathbb {R}_{\geq 0}, \{  \text {Unif}[0, \theta ]\} _{\theta > 0})$ (where $\R_{\geq 0}$ denote the nonnegative reals).

For any $\theta > 0$, then density of $\mathsf{Unif}[0,\theta]$ is given by $f(x) = \frac{1}{\theta } \mathbf{1}(x \in [0, \theta ])$. 

Hence we can use the product formula and compute the likelihood to be
$$
L_ n(x_1, \ldots , x_ n, \theta ) = \prod _{i =1}^ n \left(\frac{1}{\theta } \mathbf{1}(x_ i \in [0, \theta ] )\right) = \frac{1}{\theta ^ n} \mathbf{1}(x_ i \in [0, \theta ]\,  \,  \forall \,  1 \leq i \leq n).
$$
For the fixed values $(1,3,2,2.5, 5,0.1)$ (think of these as observations of random variables $X_1, ...,X_6$), the MLE of $\theta$ is $5$.

Observe that
$$
L_6( 1,3,2,2.5, 5,0.1, \theta ) = \frac{1}{\theta ^6} \mathbf{1}(\{ 1,3,2,2.5, 5,0.1\}  \subset [0, \theta ]).
$$
If $\theta < \max \{ 1,3,2,2.5, 5,0.1\}$, then we have $\{ 1,3,2,2.5, 5,0.1\}  \not\subset [0, \theta ]$. By the definition of the indicator function, this means $L_6( 1,3,2,2.5, 5,0.1, \theta ) = 0$ for $\theta < \max \{ 1,3,2,2.5, 5,0.1\}  = 5$. Hence, when maximizing $L_6( 1,3,2,2.5, 5,0.1, \theta )$, we need to consider $\theta \in [5,\infty)$. Restricted to this interval, we observe that
$$
L_6( 1,3,2,2.5, 5,0.1, \theta ) = \frac{1}{\theta ^ n}.
$$
The above is a decreasing function on $[5,\infty)$, so the maximum is attained when $\theta = \max \{ 1,3,2,2.5, 5,0.1\}  = 5.$

**Remark 1:** In general, the MLE for $\theta^*$ in this uniform statistical model is
$$
\widehat{\theta _ n}^{MLE} = \max _{1 \leq i \leq n} X_ i.
$$
**Remark 2:** Sometimes the likelihood equals to zero, so we cannot take the log, or the likelihood is not differentiable, so we cannot take the derivative. But we can plot it and find the MLE.

## 2. Consistency of Maximum Likelihood Estimator

Given i.i.d. samples $X_1, \ldots , X_ n\sim \mathbf{P}_{\theta ^*}$ and an associated statistical model $\left(E,\{ \mathbf{P}_\theta \} _{\theta \in \Theta }\right),\,$ the maximum likelihood estimator $\widehat{\theta }_ n^{\text {MLE}}$ of $\theta^*$ is a consistent estimator under mild regularity conditions (e.g. continuity in $\theta$ of the pdf $p_\theta$ almost everywhere). i.e.
$$
\widehat{\theta }_ n^{\text {MLE}}\xrightarrow[n\rightarrow \infty]{\mathbb{P}}\theta ^*.
$$
This is because for all $\theta \in \Theta$
$$
{1\over n} \log L(X_1, ...,X_n, \theta) \xrightarrow[n\rightarrow \infty]{\mathbb{P}}\text{"constant" } - \text{KL}(\mathbf{P}_\theta^*, \mathbf{P}_\theta)
$$
Moreover, the minimizer of the RHS is $\theta^*$ if the parameter is **identifiable**.

The RHS can be plotted as a concave curve:

![images_u3s03_plot_KL](../assets/images/images_u3s03_plot_KL.png)

Technical conditions allow to transfer this convergence from $y$-axis to and $x$-axis convergence - a convergence of the minimizer. 

Note that this is true even if the parameter $\theta$ is a vector in a **higher dimensional parameter space** $\Theta$, and $\widehat{\theta }_ n^{\text {MLE}}$ is a **multivariate random variable**, e.g. if $\theta =\begin{pmatrix} \mu \\ \sigma ^2\end{pmatrix}\in \mathbb {R}^2$ for a Gaussian statistical model.

* **Multivariate Random Variables**

  A **multivariate random variable** , or a **random vector**, is a vector-valued function whose components are (scalar) random variables on the same underlying probability space. More specifically, a random vector $\mathbf X= \left(X^{(1)},\dots ,X^{(d)}\right)^ T$ of dimension $d \times 1$  is a vector-valued function from a probability space $\Omega$ to $\R^d$:
  $$
  \begin{aligned}
  \mathbf{X}\, \, :\,  \Omega &\rightarrow \R^d\\
  \omega &\mapsto \begin{pmatrix}  X^{(1)}(\omega ) \\ X^{(2)}(\omega )\\ \vdots \\ X^{(d)}(\omega )\end{pmatrix}
  
  \end{aligned}
  $$
  where each $X^{(k)}$ is a (scalar) random variable on $\Omega$. $k$ denotes the component of a random vector.

  The **probability distribution** of a random vector $X$ is the **joint distribution** of its components $X^{(1)},\, \ldots ,\, X^{(d)}$.

  The **cumulative distribution function (cdf)** of a random vector $X$ is defined as
  $$
  \begin{aligned}
   F: \mathbb {R}^ d &\rightarrow [0,1]\\
   \mathbf{x} &\mapsto \mathbf{P}(X^{(1)}\leq x^{(1)},\ldots ,\, X^{(d)}\leq x^{(d)})
  \end{aligned}
  $$

* **Convergence in Probability in Higher Dimension**

  To make sense of the consistency statement $\, \widehat{\theta }_ n^{\text {MLE}}\xrightarrow [(p)]{n\to \infty } \theta ^*\,$ where the MLE $\widehat{\theta }_ n^{\text {MLE}}$ is a random vector, we need to know that convergence in probability in higher dimensions means convergence in probability for **each** **component**.

  Let $X_1, X_2, ...$ be a sequence of random vectors of size $d \times 1$ i.e. $\, \mathbf{X}_ i\, =\,  \begin{pmatrix}  X_ i^{(1)} \\ \vdots \\ X_ i^{(d)}\end{pmatrix}$.

  Let $\mathbf{X}\, =\,  \begin{pmatrix}  X^{(1)} \\ \vdots \\ X^{(d)}\end{pmatrix}$ be another vector of size $d\times 1$.

  Then
  $$
  \mathbf{X}_ n\xrightarrow [n\to \infty ]{(p)} \mathbf{X} \iff X_ n^{(k)} \xrightarrow [n\to \infty ]{(p)} X^{(k)}\, \, \text {for all } 1\leq k\leq d.
  $$
  In other words, the sequence $X_1, X_2, ... $ converges in probability to $X$ if and only if each component sequence $\, X_1^{(k)},X_2^{(k)},\ldots \,$ converges in probability to $\, X^{(k)}$.

  Hence, for example, in the Gaussian model $\left((-\infty ,\infty ),\{ \mathcal{N}\left(\mu , \sigma ^2\right)\} _{(\mu , \sigma ^2)\in \mathbb {R}\times \mathbb {R}_{>0}}\right)$, consistency of the MLE $\widehat{\theta }_ n^{\text {MLE}}=\begin{pmatrix} \widehat{\mu }\\ \widehat{\sigma ^2}\end{pmatrix}$ means that $\widehat{\mu}$ and $\widehat{\sigma^2}$ are consistent estimators of $\mu^*$ and $(\sigma^2)^*$, respectively.

> #### Exercise 55
>
> Let $\, X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Unif}[0, \theta ^*]$ where $\theta^*$ is an unknown parameter. We construct the associated statistical model $(\mathbb {R}_{\geq 0}, \{  \text {Unif}[0, \theta ]\} _{\theta > 0})$. Consider the maximum likelihood estimator $\widehat{\theta }_ n^{\text {MLE}} = \max _{i=1,\dots ,n}X_ I$. What can we say about $\widehat{\theta }_ n^{\text {MLE}}$.
>
> **Answer**:
>
> $\max _{i=1,\dots ,n} X_ I$ is a consistent estimator.
>
> For any $0 < \epsilon \leq \theta^*$, $\mathbf{P}\left(|\max _{i=1,\dots ,n}X_ i - \theta ^*| \ge \epsilon \right) \rightarrow 0$ as $n \rightarrow \infty$.
>
> For any $0 < \epsilon \leq \theta^*$, $\mathbf{P}\left(|\max _{i=1,\dots ,n}X_ i - \theta ^*| \ge \epsilon \right) = \left(\frac{\theta ^*-\epsilon }{\theta ^*}\right)^ n$.
>
> **Solution:**
> $$
> \begin{aligned}
> \mathbf{P}\left(\left|\max _{i=1,\dots ,n}X_ i - \theta ^*\right| \ge \epsilon \right) &= \mathbf{P}\left(\theta ^*-\max _{i=1,\dots ,n}X_ i \ge \epsilon \right)\\
> &= \mathbf{P}\left(\max _{i=1,\dots ,n}X_ i \le \theta ^*-\epsilon \right)\\
> &= \left(\frac{\theta ^*-\epsilon }{\theta ^*}\right)^ n\, \longrightarrow \,  0 \text { as } n \rightarrow \infty .
> \end{aligned}
> $$

## 3. Covariance

We can say $\overline{X}_n$ is asymptotically normal and $\widehat{S}_n$ is asymptotically normal, how about asymptotic normality of a maximum likelihood vector $\hat{\theta} = \begin{pmatrix} \overline{X}_n\\ \widehat{S}_n \end{pmatrix}$?

In general, when $\theta \subset \R^d, d\geq2$, its coordinates are not necessarily **independent**.

The covariance between two random variables $X$ and $Y$ is
$$
\begin{aligned}
\mathsf{Cov}(X,Y) &= \mathbb{E}\left[(X -\mathbb{E}[X])(Y -\mathbb{E}[Y])\right]\\
&= \mathbb{E}\left[XY - X\mathbb{E}[Y] - \mathbb{E}[X]Y + \mathbb{E}[X]\mathbb{E}[Y]\right]\\
&=\mathbb{E}[X Y] - \mathbb{E}[X]\mathbb{E}[Y]\\
&= \mathbb{E}[X (Y-\mathbb{E}[Y])] \quad \text{or }\quad \mathbb{E}[(X-\mathbb{E}[X])Y]
\end{aligned}
$$
This means if each of the random variable is center, we only need to compute the expectation of the product.

**Bilinearity of Covariance**

Let $X,Y,Z$ be random variables and $a,b$ be constant, then $\textsf{Cov}(aX + bY, Z) = a\textsf{Cov}(X,Z) + b\textsf{Cov}(Y,Z)$.

This can be seen by using the trick of centering only $Z$ when computing covariance. First, note that $\textsf{Cov}(aX,Z) = \mathbb E[(aX)(Z-\mu _ Z)] = a\mathbb E[(X)(Z-\mu _ Z)] = a\textsf{Cov}(X,Z)$. Then
$$
\begin{aligned}
\textsf{Cov}(aX+ bY, Z) &=  \mathbb E[(aX+ bY)(Z - \mu _ Z)]\\
&=\mathbb E[(aX)(Z)] - \mu _ Z \mathbb E[aX] + \mathbb E[(bY)(Z)] - \mu _ Z \mathbb E[bY]\\
&= \mathbb E[(aX)(Z)] - \mu _ Z \mathbb E[aX] + \mathbb E[(bY)(Z)] - \mu _ Z \mathbb E[bY]\\
&= a\textsf{Cov}(X,Z) + b\textsf{Cov}(Y,Z)
\end{aligned}
$$

## 4. Covariance and Independence

Properties of covariance:

* $\mathsf{Cov}(X,X) = \mathsf{Var}(X)$
* $\mathsf{Cov}(X,Y) = \mathsf{Cov}(Y,X)$
* If $X$ and $Y$ are independent, $\mathsf{Cov}(X,Y)=0$, but **the converse is not true.** 

In general, the converse is not true, except if $(X,Y)^T$ is a **Gaussian vector**, i.e. $\alpha X + \beta Y$ is Gaussian for all $(\alpha, \beta)\in \R^2$ and $(\alpha, \beta) \notin \{(0,0)\}$.

* **Prove**: $(X,Y)^T$ is not a Gaussian, and the converse is not true:

  Take $X \sim \mathcal{N}(0,1), \quad B\sim \mathsf{Ber}(1/2), \quad R=2B-1 \sim \mathsf{Rad}(1/2)$. $X$ and $B$ are independent. Then
  $$
  Y =R \cdot X \sim \mathcal{N}(0,1)
  $$
  But taking $\alpha = \beta = 1$, we get
  $$
  X + Y = \begin{cases} 2X & \text{with prob. }1/2\\ 0 & \text{with prob. }1/2 \end{cases}
  $$
  Actually $\mathsf{Cov}(X,Y)=0$ but they are not independent: $|X| = |Y|$.
  $$
  \begin{aligned}
  \mathsf{Cov}(X,Y) &= \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]\\
  &= \mathbb{E}[XY] - 0\\
  &= \mathbb{E}[XRX]\\
  &= \mathbb{E}[RX^2]\\
  &= \mathbb{E}[R] \mathbb{E}[X^2]\\
  &= 0
  \end{aligned}
  $$
  Note that $X$ is Gaussian, $Y$ is Gaussian, but the vector $(X,Y)$ is not Gaussian because a particular linear combination of the two $X+Y$ is even not continuous.

> #### Exercise 56
>
> Let $(X_1,Y_1), (X_2,Y_2),\ldots ,(X_ n,Y_ n) \stackrel{\text {iid}}{\sim } (X,Y)$ with $\mathbb E[X]=\mu _ X,\mathbb E[Y]=\mu _ Y$, and $\mathbb E[XY]=\mu _ {XY}$. That is, each random variable pair $(X_ i,Y_ i)$ has the same distribution as the random variable pair $(X,Y)$, and the pairs are independent of one another.
>
> Estimating the covariance of $X$ and $Y$ is a useful exercise because non-zero covariance implies statistical dependence of $X$ and $Y$. In this problem, we study one way to obtain an unbiased estimator for $\mathsf{Cov}(X,Y)$.
>
> Consider the following estimator of the covariance:
> $$
> \widetilde{S}_{XY} = \frac{1}{n}\left(\sum _{i=1}^ n (X_ i - \overline{X}_ n)(Y_ i - \overline{Y}_ n )\right)
> $$
> where $\overline{X}_n$ and $\overline{Y}_n$ denote the sample means estimators of $\mu_X$ and $\mu_Y$.
>
> 1. What is $\mathbb E\left[\frac{\left(\sum _{i=1}^ n X_ i\right) \left(\sum _{j=1}^ n Y_ j\right)}{n}\right]$? 
> 2. What is $\mathbb E[\widetilde{S}_{XY}]$?
> 3. Is $\widetilde{S}_{XY}$ an estimator of $\textsf{Cov}(X,Y)$?
>
> **Solution**:
>
> 1. Since $X_i$ And $Y_i$ are independent whenever $i \neq j$.
>    $$
>    \mathbb E\left[\frac{(\sum _{i=1}^ n X_ i)(\sum _{j=1}^ n Y_ j)}{n}\right] = \frac{1}{n}\mathbb E\left[\sum _{i=1}^ nX_ iY_ i + \sum _{i=1}^ n\sum _{j=1,j\neq i}^{n}X_ i Y_ j\right] = \mu _{XY}+(n-1)\mu _ X\mu _ Y
>    $$
>
> 2. $$
>    \begin{aligned}
>     \mathbb E[\widetilde{S}_{XY}] &= \frac{1}{n}\mathbb E\left[\sum _{i=1}^ n \left(X_ i - \overline{X}_ n\right)\left(Y_ i - \overline{Y}_ n \right)\right]\\
>     &=\frac{1}{n}\mathbb E\left[ \sum _{i=1}^ n X_ i Y_ i - \frac{\sum _{i=1}^ n X_ i}{n}\sum _{j=1}^ n Y_ j - \frac{\sum _{i=1}^ n Y_ i}{n}\sum _{j=1}^ n X_ j + \frac{\sum _{i=1}^ n X_ i \sum _{j=1}^ n Y_ j}{n} \right]\\
>     &= \frac{1}{n}\mathbb E\left[ \sum _{i=1}^ n X_ i Y_ i - \frac{\sum _{i=1}^ n X_ i \sum _{j=1}^ n Y_ j}{n} \right].
>    \end{aligned}
>    $$
>
>    Use the result in (1), we get
>    $$
>    \begin{aligned}
>     \mathbb E[\widetilde{S}_{XY}] &= \frac{1}{n}\left[n\mu _{XY} - \left( \mu _{XY}+(n-1)\mu _ X\mu _ Y\right)\right]\\
>     &=\frac{n-1}{n}\left[\mu _{XY} - \mu _ X \mu _ Y\right]\\
>     &= \frac{n-1}{n}\textsf{Cov}(X,Y).
>    \end{aligned}
>    $$
>
> 3. From the above, we can see that the estimator is **biased** because $\mathbb E[\widetilde{S}_{XY}] \ne \textsf{Cov}(X,Y)$.
>
>    However, the bias can be fixed by multiplying $\widetilde{S}_{XY}$ by $\frac{n}{n-1}$ to obtain the following unbiased estimator of $\mathsf{Cov}(X,Y)$:
>    $$
>    \widehat{S}_{XY} = \frac{1}{n-1}\left[\sum _{i=1}^ n \left(X_ i - \overline{X}_ n\right)\left(Y_ i - \overline{Y}_ n \right)\right].
>    $$

## 5. Covariance Matrices

Let $\mathbf X= \begin{pmatrix} X^{(1)}\\ \vdots \\ X^{(d)}\end{pmatrix}\,$ be a random vector of size $d \times 1$. Let $\mu \triangleq \mathbb E[\mathbf X]$ denote the **entry-wise** mean, i.e.
$$
\mathbb E[\mathbf X]=\begin{pmatrix} \mathbb E[X^{(1)}]\\ \vdots \\ \mathbb E[X^{(d)}]\end{pmatrix}.
$$
The covariance matrix $\Sigma$ can be written as
$$
\Sigma = \mathbf{Cov}(\mathbf{X}) = \mathbb{E}[(\mathbf{X} - \mu)(\mathbf{X}-\mu)^T]
$$
This is a matrix of size $d \times d$.

The term on the $i$-th row and $j$-th column is 
$$
\Sigma_{ij} = \mathbb{E}[(X^{(i)} - \mathbb{E}(X^{(i)}))(X^{(j)} - \mathbb{E}(X^{(j)}))] = \mathsf{Cov}(X^{(i)},X^{(j)})
$$
**Affine transformation**:

In particular, on the diagonal, we have
$$
\Sigma_{ij} = \mathsf{Cov}(X^{(i)},X^{(j)}) = \mathsf{Var}(X^{(i)})
$$
Recall that for $X \in \R, \mathsf{Var}(aX+b) = a^2 \mathsf{Var}(X).$ Actually, if $X \in \R^d$ and $A,B$ are matrices
$$
\mathsf{Cov}(AX+B) = \mathsf{Cov}(AX) = A \mathsf{Cov}(X)A^T=A \Sigma A^ T.
$$
**Properties:**

* Let $\mathbf{X}$ be a random vector and let $\mathbf Y= \mathbf X+B$, where $B$ is a constant vector. Let $\mu_{\mathbf{X}}$ be the mean vector of $\mathbf{X}$ and let $\Sigma_{\mathbf{X}}$ be the covariance matrix of $X$.

  * **$\Sigma_{\mathbf{Y}}$ and $\Sigma_{\mathbf{X}}$ are the same for all vector $B$, and they have the same size.**

  Note that $\mathbb E[\mathbf X+B] = \mu _{\mathbf X} + B$ for any vector $B$.
  $$
  \Sigma _{\mathbf Y} = \mathbb E\left[(\mathbf X+B - \mu _{\mathbf X} - B)(\mathbf X+B - \mu _{\mathbf X} - B)^ T\right] = \Sigma _{\mathbf X}
  $$

* Let $\mathbf X$ be a random vector of size $d \times 1$ and let $\mathbf Y= A\mathbf X+B$, where $A$ is a constant matrix of size $n \times d$ and $B$ is a constant vector of size $n \times 1$. Let $\mu_{\mathbf{X}}$ be the mean vector of $\mathbf{X}$ and let $\Sigma _{\mathbf X}$ be the covariance matrix of $\mathbf{X}$. Let $\mu _{\mathbf Y}$ be the mean vector of $\mathbf Y$ and let $\Sigma _{\mathbf Y}$ be the covariance matrix of $\mathbf Y$.

  * **$\Sigma _{\mathbf Y}$ is the same as covariance matrix of $A\mathbf X$.**

  * **$\Sigma _{\mathbf Y}$ Is of size $n \times n$.**

  * **$\Sigma _{\mathbf Y}=A \Sigma _{\mathbf X}A^ T$.**

  As $\mathbf Y$ is an $n \times 1$ random vector, $\Sigma _{\mathbf Y}$ is of size $n \times n$.

  From previous problem we know that $\Sigma _{\mathbf Y}$ is the same as the covariance matrix of $A \mathbf X$. Therefore, it suffices to find this matrix, which we denote $\Sigma _{A\mathbf X}$.
  $$
  \begin{aligned}
  \Sigma _{A\mathbf X} & =\mathbb E\left[\left(A\mathbf X- A \mu _ X\right)\left(A \mathbf X- A\mu _ X\right)^ T\right]\\
  &= \mathbb E\left[A\left(\mathbf X- \mu _ X\right)\left(\mathbf X^ T A^ T - \mu _ X^ T A^ T\right)\right]\\
  &= \mathbb E\left[A\left(\mathbf X- \mu _ X\right)\left(\mathbf X- \mu _ X\right)^ TA^ T\right]\\
  &= A\mathbb E\left[\left(\mathbf X- \mu _ X\right)\left(\mathbf X- \mu _ X\right)^ T\right]A^ T\\
  &= A \Sigma _{\mathbf X} A^ T.
  \end{aligned}
  $$

> #### Exercise 57
>
> Given random variables $X^{(1)}, X^{(2)}, \ldots , X^{(d)}$, one can write down the covariance matrix $\Sigma$, where $\Sigma _{i,j} = \textsf{Cov}(X^{(i)}, X^{(j)})$.
>
> Let $X,Y$ be random variables such that
>
> * $X$ takes the values $\pm 1$ each with probability $0.5$
> * (Conditioned on $X$) $Y$ is chosen uniformly from the set $\{  -3X-1, -3X, -3X+1 \}$.
>
> What is covariance matrix $\Sigma$?
>
> **Solution:**
>
> Observe that $\mathbb E[X]$ and $\mathbb E[Y]$ are both zero, since $X$ is uniformly distributed over $\{\pm 1\}$ and $Y$ is uniformly distributed over the set $\{ -4,-3,-2,2,3,4\}$.
>
> * $\textsf{Cov}(X,X)$ is the variance of $X$, which equals $\mathbb E[X^2] - \mathbb E[X]^2 = p + (1-p) = 1.$
> * $\textsf{Cov}(Y,Y)$ is the variance of $Y$, which equals $\mathbb E[Y^2] - \mathbb E[Y]^2 = \frac{16+9+4+4+9+16}{6} = \frac{29}{3} \approx 9.67.$
> * $\textsf{Cov}(X,Y) = \textsf{Cov}(Y,X)$. Observe the joint density of $(X,Y)$ is uniform over the pairs $(1,-4), (1,-3), (1,-2), (-1,2), (-1,3), (-1,4)$. Thus, either covariance can be computed as $\mathbb E[XY] - \mathbb E[X]\mathbb E[Y] = \frac{-4-3-2-2-3-4}{6}-0 = -3.$
>
> From above, we get 
> $$
> \begin{aligned}
> \Sigma _{1,1}  &= \textsf{Cov}(X,X)=1\\
> \Sigma _{1,2}  &= \textsf{Cov}(X,Y) = -3\\
> \Sigma _{2,1}  &= \textsf{Cov}(Y,X)=-3\\
> \Sigma _{2,2}  &= \textsf{Cov}(Y,Y)=9.67
> \end{aligned}
> $$
> Therefore, 
> $$
> \Sigma = \begin{pmatrix}  \Sigma _{1,1} &  \Sigma _{1,2} \\ \Sigma _{2,1} &  \Sigma _{2,2} \end{pmatrix} = \begin{pmatrix}  1 &  -3 \\ -3 &  \tfrac {29}{3} \end{pmatrix}
> $$

## 6. Multivariate Gaussian Distribution

A random vector $\mathbf{X}=(X^{(1)},\ldots ,X^{(d)})^ T\,$ is a **Gaussian vector**, or **multivariate Gaussian or normal variable**, if any linear combination of its components is a (univariate) Gaussian variable or a constant (a "Gaussian" variable with zero variance), i.e., if $\alpha^T\mathbf X$ is (univariate) Gaussian or constant for any constant non-zero vector $\alpha \in \R^d$.

The distribution of $\mathbf{X}$, the **$d$-dimensional Gaussian or normal distribution**, is completely specified by the vector mean $\mu =\mathbb E[\mathbf{X}]= (\mathbb E[X^{(1)}],\ldots ,\mathbb E[X^{(d)}])^ T$ and the $d\times d$ covariance matrix $\Sigma$.  We write
$$
X \sim \mathcal{N}_d(\mu,\Sigma)
$$
If $\Sigma$ is invertible, then the pdf of $\mathbf{X}$ is
$$
f_{\mathbf X}(\mathbf x) = \frac{1}{\sqrt{\left(2\pi \right)^ d \text {det}(\Sigma )}}\exp \left(-\frac{1}{2}(\mathbf x-\mu )^ T \Sigma ^{-1} (\mathbf x-\mu )\right), ~ ~ ~ \mathbf x\in \mathbb {R}^ d
$$
where $\text{det}(\Sigma)$ is the determinant of the $\Sigma$, which is positive when $\Sigma$ is invertible.

If $\mu =0 $ and $\Sigma$ is the identity matrix, then $\mathbf{X}$ is called a **standard normal random vector**.

Note that when the covariant matrix $\Sigma$ is diagonal, the pdf factors into pdfs of univariate Gaussians, and hence the components are independent.

> #### Exercise 58
>
> Consider the $2$-dimensional Gaussian $\mathbf X=\begin{pmatrix} X^{(1)}\\ X^{(2)}\end{pmatrix}$ with covariance matrix $\Sigma _ X = \begin{pmatrix}  1 &  2 \\ 2 &  5\end{pmatrix}$ and mean $\Sigma _ X = \begin{pmatrix}  1 &  2 \\ 2 &  5\end{pmatrix}$.
>
> Consider the vector $\alpha = \begin{pmatrix}  1 \\ -1 \end{pmatrix}$, so that $Y = \alpha ^ T \mathbf X$ is a 1-dimensional Gaussian.
>
> What is the variance $\textsf{Var}(Y)$ of $Y$?
>
> **Answer:** $\textsf{Var}(Y)=2$
>
> **Solution:**
>
> Method 1:
>
> Since $Y = X^{(1)} - X^{(2)}$, 
> $$
> \begin{aligned}
> \textsf{Var}(Y) &=\textsf{Cov}(Y,Y) \\
> &= \textsf{Cov}(X^{(1)} - X^{(2)},X^{(1)} - X^{(2)}) \\
> &= \textsf{Cov}(X^{(1)},X^{(1)}) +\textsf{Cov}(X^{(1)},X^{(1)})  -\textsf{Cov}(X^{(1)},X^{(2)})-\textsf{Cov}(X^{(2)},X^{(1)}) \\
> & = \textsf{Var}(X^{(1)}) + \textsf{Var}(X^{(2)}) - 2\textsf{Cov}(X^{(1)},X^{(2)})\\
> &= 1+5-4 = 2.
> \end{aligned}
> $$
> Method 2:
>
> Define the matrix $\, M\triangleq \alpha ^ T=\begin{pmatrix}  1 &  -1 \end{pmatrix},\,$ and apply the formula $\Sigma _ Y = M\Sigma _\mathbf XM^ T = 2.$

**Diagonalization of the Covariance Matrix**

Let $\Sigma$ be a covariance matrix of size $d \times d$. Note that its entries are all real numbers with diagonal elements being non-negative. $\Sigma$ has the following properties

* $\Sigma$ is symmetric. That is $\Sigma = \Sigma ^ T$.
* $\Sigma$ is diagonalizable to a diagonal matrix $D$ via a transformation $D = U\Sigma U^T$, where $U$ is an orthogonal matrix (recall that a square matrix $A$ is orthogonal if $AA^T = A^TA= I$, where $I$ is the identity matrix). This implies that $\Sigma = U^TDU$.
* $\Sigma $ is positive semidefinite. That is, the diagonal matrix $D$ has diagonal entries that are all non-negative.
* $\Sigma$ Has a unique positive semidefinite square root matrix. That is, there exists a positive semi-definite matrix $\Sigma^{1/2}$ that is unique such that $\Sigma^{1/2} \cdot \Sigma^{1/2} = \Sigma$.
* If $\Sigma $ is of size $d \times d$, then it has $d$ orthonormal eigenvectors (even if there are repeated eigenvalues). Furthermore, if $U$ is a matrix with rows corresponding to the orthonormal eigenvectors, then the diagonal matrix $D = U \Sigma U^T$ contains the eigenvalues of $\Sigma$ along its diagonal. Therefore, diagonalization of a symmetric matrix involves finding its eigenvalues and the orthonormal eigenvectors.
* If $\Sigma$ is positive definite, i.e. the diagonal matrix $D = U\Sigma U^T$ has diagonal entries that are all strictly positive, then it is invertible and the inverse $\Sigma^{-1}$ satisfies the following: $\Sigma ^{-\frac{1}{2}}\cdot \Sigma ^{-\frac{1}{2}} = \Sigma ^{-1}$, where $\Sigma ^{-\frac{1}{2}}$ is the inverse of the square root of $\Sigma$.

> #### Exercise 59
>
> Recall from an earlier part of this lecture that the covariance between two random variables being 0 does not necessarily imply that the random variables are independent. However, this is true if the random variables are multivariate Gaussian.
>
> Let $\mathbf X$ be a Gaussian random vector with mean $\mu$ and covariance $\Sigma$. Assume that $\Sigma$ is positive definite. How to prove that "there exists a vector $B$ and a matrix $A$ such that $A(\mathbf X + B)$ is a Gaussian random vector whose components are independent and each of mean 0".
>
> **Solution:**
>
> First, in order to remove the effect of $\mu$ we can set $B = -\mu$ to make the individual Gaussian random variables be of zero mean. Let $\widehat{\mathbf X} = \mathbf X- \mu$. From an earlier problem we know that the covariance matrix of $\widehat{\mathbf X}$ is the same as $\Sigma$.
>
> From the above note on covariance matrices we can see that there exists an orthogonal matrix $U$ such that $D = U \Sigma U^ T$. 
>
> Consider the following transformation: $\mathbf Y= U \widehat{\mathbf X}$.
>
> The covariance matrix of $\mathbf Y$ is 
> $$
> \mathsf{Cov}(\mathbf{Y}) = U\Sigma U^T
> $$
> which is precisely equal to the diagonal matrix $D$.
>
> Therefore, $\mathbf Y$ has component Gaussian random variables that are uncorrelated and hence independent.

## 7. Multivariate Central Limit Theorem

The CLT may be generalized to averages or random vectors (also vectors of averages). Let $X_1, ...,X_n \in \R^d$ be independent copies of a random vector $X$ such that $\mathbb{E}[X] =\mu, \quad \mathsf{Cov}(X)= \Sigma$,
$$
\sqrt{n} (\bar{X}_n - \mu) \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}_d(0, \Sigma)
$$
Equivalently,
$$
\sqrt{n} \Sigma^{-1/2} (\bar{X}_n - \mu) \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}_d(0,I_d)
$$
where $I_d$ is a $d \times d$ identity matrix.

**Convergence in Distribution in Higher Dimensions**

Convergence in distribution of a random vector is NOT implied by convergence in distribution of each of its components.

A sequence $\, \mathbf{T}_1,\mathbf{T}_2,\ldots$ of random vectors in $\R^d$ **converges in distribution** to a random vector $\mathbf{T}$ if
$$
\mathbf{v}^ T \mathbf{T}_ n \xrightarrow [(d)]{n\to \infty } \mathbf{v}^ T \mathbf{T} \qquad \text {for all }\, \mathbf{v}\in \mathbb {R}^ d \qquad (\text {multivariate convergence in distribution}).
$$
That is, the vector sequence $\, \left(\mathbf{T}_ n\right)_{n\geq 1}\,$ converges in distribution only if its dot product $\mathbf{v}^ T\mathbf{T}_ n$ with **any** constant vector $\mathbf{v}$, which is a scalar random variable, converges in distribution (or equivalently, if the projection of the vector sequence onto **any** line converges in distribution.)

**Univariate CLT Implies Multivariate CLT**

Let $\, \mathbf{X}_1, \ldots ,\, \mathbf{X}_ n\stackrel{i.i.d.}{\sim } \mathbf{X}\,$ be random vectors in $\R^d$ with (vector) mean $\mathbb{E}[\mathbf{X}] = \mu_\mathbf{X}$ and covariance matrix $\Sigma_{\mathbf{X}}$. Let $\mathbf{v} \in \R^d$ and define $Y_ i=\mathbf{v}^ T\mathbf{X}_ i$. Then

* $Y_i$ is a scalar random variable;
* Its mean and variance are $\mathbb E[Y_ i]= \mathbf{v}^ T\mathbb E[\mathbf{X}_ i]\,$ and $\, \sigma ^2_{Y_ i}=\mathbf{v}^ T \Sigma _{\mathbf{X}_ i} \mathbf{v}\,$

Hence $Y_i$ satisfies the univariate CLT:
$$
\sqrt{n}\left(\overline{Y_ n}-\mathbf{v}^ T\mu _\mathbf X\right) \xrightarrow [(d)]{n\to \infty }\mathcal{N}\left(0, \mathbf{v}^ T \Sigma _{\mathbf{X}} \mathbf{v}\right)
$$
On the other hand, consider a multivariate Gaussian variable $\, \mathbf{Z}\sim \mathcal{N}\left(\mathbf{0}, \Sigma _{\mathbf{X}}\right)$. For any constant vector $\, \mathbf{v}\in \mathbb {R}^ d,\, \, \mathbf{v}^ T \mathbf{Z}\,$ is a univariate Gaussian with variance $\, \mathbf{v}^ T\Sigma _{\mathbf{X}}\mathbf{v}.\,$ Hence, $\mathbf{v}^ T \mathbf{Z}\sim \mathcal{N}\left(0, \mathbf{v}^ T\Sigma _{\mathbf{X}}\mathbf{v}\right),\,$ which is the distribution on the RHS above. Therefore, $\overline{\mathbf{X}_ n}$ converges in distribution:
$$
\begin{aligned}
\sqrt{n}\left(\mathbf{v}^ T\overline{\mathbf{X}_ n}-\mathbf{v}^ T\mu _\mathbf X\right)\, =\, \sqrt{n}\left(\overline{Y_ n}-\mathbf{v}^ T\mu _\mathbf X\right) &\xrightarrow [(d)]{n\to \infty } \mathcal{N}\left(0, \mathbf{v}^ T \Sigma _{\mathbf{X}} \mathbf{v}\right)\, =\, \mathbf{v}^ T \mathcal{N}\left(0, \Sigma _{\mathbf{X}}\right)\\
\iff\sqrt{n}\left(\overline{\mathbf{X}}_ n-\mu _\mathbf X\right)&\xrightarrow [(d)]{n\to \infty }\mathcal{N}\left(0, \Sigma _{\mathbf{X}}\right).

\end{aligned}
$$

## 8. Multivariate Delta Method

Let $(T_n)_{n \geq 1}$ sequence of random vectors in $\R^d$ such that
$$
\sqrt{n} (\mathbf{T}_n - \theta) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}_d(0, \Sigma)
$$
for some $\theta \in \R^d$ and some covariance $\Sigma \in \R^{d \times d}.$

Let $\mathbf{g}: \R^d \rightarrow \R^k (k \geq 1)$ be continuously differentiable at $\theta$. The **gradient** or the **gradient matrix** of $\mathbf{g}$, denoted by $\nabla \mathbf{g}$, is the $d\times k$ matrix
$$
\nabla \mathbf{g} =  \begin{pmatrix} |& |& |& |\\ \nabla \mathbf{g}_1&  \nabla \mathbf{g}_2& \ldots & \nabla \mathbf{g}_ k\\ |& |& |& |\\ \end{pmatrix} = \begin{pmatrix} \frac{\partial \mathbf{g}_1}{\partial \theta_1}& \ldots & \frac{\partial \mathbf{g}_ k}{\partial \theta_1}\\ \vdots & \ldots & \vdots \\ \frac{\partial \mathbf{g}_1}{\partial \theta_ d}& \ldots & \frac{\partial \mathbf{g}_ k}{\partial \theta_ d} \end{pmatrix}.
$$
This is also the transpose of what is known as the **Jacobian matrix** $J_g$ of $g$.

Then,
$$
\sqrt{n}(\mathbf{g}(\mathbf{T}_n) - \mathbf{g}(\theta)) \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}_k(0, \nabla \mathbf{g}(\theta)^T \Sigma \nabla \mathbf{g}(\theta))
$$
where $\nabla \mathbf{g}(\theta) = {\partial \mathbf{g}\over\partial \theta }(\theta) = \left({\partial \mathbf{g}_j \over \partial \theta_i } \right)_{1\leq i \leq d; 1\leq j\leq k} \in \R^{d \times k}$.
