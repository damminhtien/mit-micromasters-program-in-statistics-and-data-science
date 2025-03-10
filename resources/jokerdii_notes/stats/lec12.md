# Lecture 12. M-Estimation

There are 6 topics and 8 exercises.

## 1. Introduction of M-Estimation

* Let $X_1, ..., X_n$ be i.i.d. with some unknown distribution $\mathbf{P}$ and an associated parameter $\mu^*$ in some sample space $E(E \subseteq \R^d$ for some $d \geq 1)$.

* No statistical model / family of distribution needs to be assumed (similar to ML). (Unlike maximum likelihood estimation and the method of moments.)

* **Goal**: estimate some parameter $\mu^*$ associated with $ \mathbf{P}$ , e.g. its mean, variance, median, other quantiles, the true parameter in some statistical model...

  Find a **loss function** $\rho(X,\mu): E \times \mathcal{M} \rightarrow \R$, where $\mathcal{M}$ is the set of all possible values for the unknown $\mu^*$, such that
  $$
  \mathcal{Q}(\mu) := \mathbb{E}[\rho(X_1, \mu)]
  $$
  achieves its minimum at $\mu = \mu^*$. 

  Note that the function $\rho(X,\mu)$ is in particular a function of the random variable $X$, and the expectation in $\mathbb{E}[\rho(X,\mu)]$ is to be taken against the **true distribution** $\mathbf{P}$ of $X$, with associated parameter value $\mu^*$.

  Proved by taking derivative and set it to zero to solve for the minimal parameter: 
  $$
  {\partial \over \partial\mu} \mathbb{E}[(X-\mu)^2] = \mathbb{E}[-2X + 2\mu] = -2 \mu^* + 2\mu = 0 \implies \mu = \mu^*
  $$

* **Formal definition**: An **M-estimator** $\widehat{\mu}$ of the parameter $\mu^*$ is the **argmin of an estimator of a function** $\mathcal{Q}(\mu)$ of the parameter which satisfies the following:

  * $\mathcal{Q}(\mu )\, =\, \mathbb E\left[\rho (X,\mu ) \right] \,$ for some function $\rho:E \times \mathcal{M} \rightarrow \R$, where $\mathcal{M}$ is the set of all possible values of the unknown true parameter $\mu^*$.
  * $\mathcal{Q}(\mu)$ attains a unique minimum at $\mu = \mu^*$, in $\mathcal{M}$. That is, $\text {argmin}_{\mu \in \mathcal{M}}\mathcal{Q}(\mu ) \, =\, \mu ^*$.

* Notes: 

  * Because $\mathcal{Q}(\mu)$ is an expectation, we can construct a (consistent) estimator of $\mathcal{Q}(\mu)$ by **replacing the expectation in its definition by the** **sample mean**.

    * Define $\hat{\mu}_n$ as a minimizer of 
      $$
      \mathcal{Q}_n(\mu) := {1\over n}\sum^n_{i=1} \rho(X_i, \mu)
      $$
      So we have the equation
      $$
      \widehat{\mu } = \text {argmin}_{\mu \in \mathbb {R}} \frac{1}{n} \sum _{i = 1}^ n [\rho (X_ i, \mu )]
      $$
      instead of
      $$
      \mu ^* = \text {argmin}_{\mu \in \mathbb {R}} \mathbb E_{X \sim \mathbf{P}}[ \rho (X, \mu )]
      $$
      Examples: Empirical mean, empirical median, empirical quantiles, MLE, etc.

  * Maximum likelihood estimation is a special case of M-estimation. If we set the loss function to be the **negative log-likelihood**, then the same optimization problem defining the MLE is the one considered for the M-estimator associated to this loss function.

  * M-estimation can be used in both a **parametric** and **non-parametric** context.

#### MLE is an M-estimator

Assume that $(E, \mathbf\{P_{\theta}\}_{\theta \in \Theta})$ is a statistical model associated with the data.

**Theorem**:

Let $\mathcal{M} \in \Theta$ and $\rho(x,\theta) = - \log L(x, \theta)$, provided the likelihood is positive everywhere. Then
$$
\mu^* = \theta^*
$$
Where $\mathbf{P} = \mathbf{P}_{\theta^*}$ (i.e. $\theta^*$ is the true value of the parameter).

**Proof**:

Recall that the MLE is defined by
$$
\widehat{\theta }_ n^{\text {MLE}} = \text {argmax}_{\theta \in \Theta } \frac{1}{n} \sum _{i = 1}^ n \ln p_\theta (X_ i).
$$
By symmetry, we also have
$$
\widehat{\theta }_ n^{\text {MLE}} = \text {argmin}_{\theta \in \Theta } \frac{1}{n} \sum _{i = 1}^ n - \ln p_\theta (X_ i).
$$
Indeed, setting $\rho (x, \theta ) = - \ln p_\theta (x)$, we recover the MLE.

#### Examples:

* If $E = \mathcal{M} = \R$ and $\rho(x,\mu) = (x-\mu)^2$, for all $x \in \R, \mu \in \R$: $\qquad \mu^* = \mathbb{E}[X]$.
* If $E = \mathcal{M} = \R^d$ and $\rho(x,\mu) = ||x - \mu||^2_2$, for all $x \in \R^d, \mu \in \R^d:\qquad \mu^* = \mathbb{E}[X] \in \R^d$.
* If $E = \mathcal{M} = \R$ and $\rho(x, \mu) = |x- \mu|$, for all $x \in \R, \mu \in \R: \quad \mu^*$ is a median of $\mathbf{P}$.

#### Example: multivariate mean as minimizer

Let $\, \mathbf{X}=\begin{pmatrix}  X^{(1)}\\ X^{(2)} \end{pmatrix}\,$ be a continuous random vector with density $\, f: \mathbb {R^2} \to \mathbb {R}.\, \,$ Recall the mean of $X$ is
$$
\mathbb E[\mathbf{X}] = \begin{pmatrix}  \mathbb E[X^{(1)}]\\ \mathbb E[X^{(2)}]\end{pmatrix}
$$
Recall the square of the **Euclidean** norm function on $\R^2$:
$$
\left\|  \cdot  \right\| ^2: \mathbb {R}^2 \rightarrow \R\\
\mathbf{y}\, \, =\, \begin{pmatrix}  y_1\\ y_2 \end{pmatrix} \mapsto \left(y_1\right)^2+\left(y_2\right)^2.
$$
We now show that the (multivariate) mean of $\mathbf{X}$ satisfies
$$
\mathbb E[\mathbf{X}] =  \text {argmin}_{\vec{\mu } \in \mathbb {R^2}} \mathbb E\left[\left\|  \mathbf{X}- \vec{\mu } \right\| ^2\right].
$$
First, expand $ \mathcal{Q}(\vec{\mu })=\mathbb E\left[\left\|  \mathbf{X}- \vec{\mu } \right\| ^2\right]\,$ as an integral expression, and write down both partial derivatives $\frac{\partial \mathcal{Q}}{\partial \mu _1}(\vec{\mu })\,$ and $\frac{\partial \mathcal{Q}}{\partial \mu _2}(\vec{\mu })\,$:
$$
\begin{aligned}
\mathbb E\left[\left\|  \mathbf{X}- \vec{\mu } \right\| ^2\right] & =  \int _{-\infty }^{\infty } \int _{-\infty }^{\infty } \left(\left(x_1-\mu _1\right)^2+\left(x_2-\mu _2\right)^2\right) f(x_1,x_2) dx_1 dx_2 \\
\implies \frac{\partial }{\partial \mu _1}\mathbb E\left[\left\|  \mathbf{X}- \vec{\mu } \right\| ^2\right]& = -2 \int _{-\infty }^{\infty }\int _{-\infty }^{\infty } \left(x_1-\mu _1\right)f(x_1,x_2) dx_1 dx_2\\
\frac{\partial }{\partial \mu _2}\mathbb E\left[\left\|  \mathbf{X}- \vec{\mu } \right\| ^2\right] &=  -2 \int _{-\infty }^{\infty }\int _{-\infty }^{\infty } \left(x_2-\mu _2\right)f(x_1,x_2) dx_1 dx_2.

\end{aligned}
$$
To find the argmin of $\mathbb E\left[\left\|  \mathbf{X}- \vec{\mu } \right\| ^2\right],\,$ we set both partial derivatives to $0$, and obtain
$$
\text {argmin}_{\vec{\mu } \in \mathbb {R^2}} \mathbb E\left[\left\|  \mathbf{X}- \vec{\mu } \right\| ^2\right] = \begin{pmatrix} \displaystyle \int _{-\infty }^{\infty }\int _{-\infty }^{\infty } x_1f(x_1,x_2) dx_1 dx_2 \\ \displaystyle \int _{-\infty }^{\infty }\int _{-\infty }^{\infty } x_2f(x_1,x_2) dx_1 dx_2 \end{pmatrix}\, =\, \begin{pmatrix}  \mathbb E[X^{(1)}]\\ \mathbb E[X^{(2)}]\end{pmatrix}.
$$

#### Median as a minimizer

Assume that $X$ is a continuous random variable with density $f: \mathbb {R} \to \mathbb {R}$. Then a **median** of $X$ is defined to be any point $\text {med}(X) \in \mathbb {R}$ such that
$$
P(X > \text {med}(X)) = P(X < \text {med}(X)) = \frac{1}{2}.
$$
(Recall that for a continuous distribution, $P(X > \text {med}(X)) = P(X \geq \text {med}(X))$ Note: A median of a distribution is not necessarily unique.)

Here, we show that any median satisfies
$$
\text {med}(X) = \text {argmin}_{\mu \in \mathbb {R}} \mathbb E\left[|X - \mu |\right].
$$
First, calculate $\mathbb E\left[|X - \mu |\right]$ in terms of the density $f(x)$.
$$
\begin{aligned}
\mathbb E\left[|X - \mu |\right] & = \int _{-\infty }^\infty |x - \mu | f(x) \,  dx\\
&= \int _{\mu }^\infty (x - \mu ) f(x) \,  dx + \displaystyle \int _{-\infty }^\mu (-x + \mu ) f(x) \,  dx\\
&= \int _{\mu }^\infty x f(x) \,  dx - \displaystyle \int _{-\infty }^\mu x f(x) \,  dx - \mu \left( \displaystyle \int _\mu ^\infty f(x) \,  dx - \displaystyle \int _{-\infty }^\mu f(x) \,  dx \right)
\end{aligned}
$$
Second, let $\, \mathcal{Q}(\mu )=\displaystyle \mathbb E\left[|X - \mu |\right]\,$ denote the expression obtained in the previous question. Then $\, \mathcal{Q}(\mu )$ consists of a sum of terms, each of which can be differentiated with respect to $\mu$. 

We compute $\mathcal{Q}'(\mu )=\frac{d}{d\mu } \mathcal{Q}(\mu )$ by differentiating it term by term. We have, by the fundamental theorem of calculus and the product rule that
$$
\begin{aligned}
\frac{d}{d \mu } \left( \displaystyle \int _{\mu }^\infty x f(x) \,  dx \right) &=-\mu f(\mu )\\
 \frac{d}{d \mu } \left(- \displaystyle \int _{-\infty }^\mu x f(x) \,  dx \right) &= - \mu f(\mu )\\
 \frac{d}{d \mu } \left( -\mu \left( \displaystyle \int _\mu ^\infty f(x) \,  dx - \displaystyle \int _{-\infty }^\mu f(x) \,  dx \right) \right) &= -\displaystyle \int _\mu ^\infty f(x) \,  dx + \displaystyle \int _{-\infty }^\mu f(x) \,  dx + 2\mu f(\mu ).
\end{aligned}
$$
Adding these terms, we have cancellations, yielding
$$
\frac{d}{d \mu } \mathcal{Q}(\mu ) = - \displaystyle \int _\mu ^\infty f(x) \,  dx + \displaystyle \int _{-\infty }^\mu f(x) \,  dx.
$$
Third, compute $\, \mathcal{Q}'(\text {med}(X))\,$. 
$$
\mathcal{Q}'( \text {med}(X) ) = \int _{-\infty }^{\text {med}(X)} f(x) \,  dx - \int _{\text {med}(X)}^\infty f(x) \,  dx = P( X < \text {med}(X)) - P( X > \text {med}(X)) = 0.
$$

#### Quantile as a minimizer

Recall from the lecture that the **check function** is defined as
$$
C_\alpha (x) = \begin{cases} -(1-\alpha)x & \text{if }x < 0\\ \alpha x & \text{if } x \geq 0 \end{cases}
$$
![checkFunction](../assets/images/checkFunction.png)

Assume that $X$ is a continuous random variable with density $f: \R \rightarrow \R$. Define the $\alpha$-**quantile** of $X$ to be $Q_X{\alpha} \in \R$ such that
$$
\mathbf{P}\left(X \leq Q_ X(\alpha )\right) = \alpha
$$
(Here we have used a different convention of the definition of the quantile function from before, where for a standard normal distribution, $q_\alpha$ is such that $P(X > q_\alpha) = \alpha$).

Just like for the median, whether $Q_\alpha$ is unique depends on the distribution.

Here we show that any $\alpha$-quantile of $X$ satisfies
$$
Q_{X}(\alpha ) = \text {argmin}_{\mu \in \mathbb {R}} \displaystyle \mathbb E\left[C_\alpha (X - \mu )\right].
$$
First, compute $F(\mu) = \mathbb E\left[C_\alpha (X - \mu )\right]$ with the form as below. $A,B,C,D$ are coefficients.
$$
\begin{aligned}
F(\mu) =  \mathbb E\left[C_\alpha (X - \mu )\right] =& -\int _{-\infty }^{\mu } (1-\alpha ) (x-\mu ) f(x)\, dx+ \int _{\mu }^{\infty } \alpha (x-\mu ) f(x)\, dx\\
=& -(1-\alpha )\int _{-\infty }^{\mu } x f(x)\, dx+ \alpha \int _{\mu }^{\infty } x f(x)\, dx \\
&+(1-\alpha ) \mu \int _{-\infty }^{\mu } f(x)\, dx-\alpha \mu \int _{\mu }^{\infty } f(x)\, dx.
\end{aligned}
$$
Second, the derivative of $F$ with respect to $\mu$ is
$$
\begin{aligned}
F'(\mu )\, =\, \frac{d}{d\mu }F(\mu ) =& -(1-\alpha )\frac{d}{d\mu }\int _{-\infty }^{\mu } x f(x)\, dx+ \alpha \frac{d}{d\mu }\int _{\mu }^{\infty } x f(x)\, dx\\ &+(1-\alpha ) \frac{d}{d\mu } \left(\mu \int _{-\infty }^{\mu } f(x)\, dx\right)-\alpha \frac{d}{d\mu }\left(\mu \int _{\mu }^{\infty } f(x)\, dx\right)\\
=& -(1-\alpha )\left(\mu f(\mu )\right)+\alpha \left(-\mu )f(\mu )\right) \\
& +(1-\alpha ) \left(\int _{-\infty }^{\mu } f(x)\, dx+ \mu f(\mu )\right) -\alpha \left(\int _{\mu }^{\infty } f(x)\, dx-\mu f(\mu )\right)\\
&(\text {by fundamental theorem of calculus 2})\\
=& (1-\alpha ) \int _{-\infty }^{\mu } f(x)\, dx -\alpha \int _{\mu }^{\infty } f(x)\, dx\\
=& (1-\alpha )\left(\int _{-\infty }^{\mu } f(x)\, dx\right) -\alpha \left(1-\int _{-\infty }^{\mu } f(x)\, dx\right)\\
=& \left(\int _{-\infty }^{\mu } f(x)\, dx\right)-\alpha.
\end{aligned}
$$
Setting $F'(\mu) = 0$ yields
$$
\int _{-\infty }^{\mu } f(x)\, dx = \alpha
$$
Hence, $\text {argmin}_{\mu \in \mathbb {R}} F(\mu )$ is an $\alpha$-quantile of $X$.

#### Convexity of the Expectation of the Loss Function

**Strict convexity** of $\, \mathcal{Q}(\mu )\, =\, \mathbb E\left[\rho (X,\mu ) \right] \,$ ensures that it has a unique **minimum**, and this is guaranteed by strict convexity of $\, \rho (X,\mu )\,$ in $\mu$. **Expectation of a convex function is convex**.

Let $X$ be a random variable with some unknown distribution $\mathbf{P}$ with some associated parameter $\mu^*$ on some sample space $E.$ Let $\rho:E \times \mathcal{M} \rightarrow \R$, where $\mathcal{M}$ is the set of all possible values of the unknown true parameter $\mu^*$ and let $\, \mathcal{Q}(\mu )\, =\, \mathbb E\left[\rho (X,\mu ) \right].\, \,$
$$
\rho (X,\mu )\, \, \text { strictly convex in }\mu \implies \mathbb E\left[\rho (X,\mu ) \right]\, \, \text { strictly convex in }\mu .
$$
**Proof:**

Recall that $\rho$ being strictly convex in $\mu$ means that
$$
t\rho (x,\mu _1)+(1-t)\rho (x,\mu _2)- \rho (x,t\mu _1+(1-t)\mu _2)>0 \quad \text {for all } x.
$$
Taking the expectation of the above inequality gives:
$$
 \mathbb E[t\rho (X,\mu _1)+(1-t)\rho (X,\mu _2)- \rho (X,t\mu _1+(1-t)\mu _2)]\\
= t\mathbb E[\rho (X,\mu _1)]+(1-t)\mathbb E[\rho (X,\mu _2)]- \mathbb E[\rho (X,t\mu _1+(1-t)\mu _2)]>0
$$
For any $\mu_1 \neq \mu_2 \in \mathcal{M}$, and $t \in (0,1)$. This is because $\mathbb E[f(X)]>0$ if $f(X) > 0$. The above inequality exactly implies strict convexity of $\, \mathbb E\left[\rho (X,\mu ) \right]$.

#### Summary of MLE and Moment of Method strategies

* MLE:
  * $\theta \mapsto \text{KL}(\mathbf{P}_{\theta^*}, \mathbf{P}_{\theta})$ is minimized at $\theta = \theta^*$
  * $\text{KL} = - \mathbb{E}[\text{log likelihood}] + $ constant
  * Max log likelihood by ${1\over n} \sum\limits^n_{i=1} \log f_\theta(x_i)$
* Moment of Methods
  * $\mu \mapsto \mathbb{E}[\rho(X,\mu)] = \mathcal{Q}(\mu)$ is minimized at $\mu^*$.
  * Estimate $\mathbb{E}[\rho(X,\mu)]$ by ${1\over n} \sum\limits^n_{i=1} \rho(X,\mu)$
  * Minimize the estimator in $\mu$.

## 2. Asymptotic Normality of M-estimators

#### Preparation

Let $\, \mathbf{X}_1,\, \ldots ,\, \mathbf{X}_ n\,$ be i.i.d. random vector in $\R^d$ with some unknown distribution $\mathbf{P}$ with some associated parameter $\, \vec{\mu }^*\in \mathbb {R}^ d\,$ on some sample space $E$. Let $\mathcal{Q}(\vec{\mu })\, =\, \mathbb E\left[\rho (\mathbf{X},\vec{\mu }) \right] \,$ for some function $\, \rho :E\times \mathcal{M}\to \mathbb {R},\,$ where $\mathcal{M}$ is the set of all possible values of the unknown true parameter $\vec{\mu }^*.\,$

* Let the covariance matrix of the loss be $K(\mu) = \mathsf{Cov}\left[{\partial \rho\over\partial \mu }(X_1, \mu)\right]$. 

  Formally,
  $$
  \mathbf{K}\, =\, \textsf{Cov}\left[\nabla \rho (\mathbf{X}_1,\vec{\mu })\right] = \textsf{Cov}\left[\begin{pmatrix} \frac{\partial \rho }{\partial \mu _1 } (\mathbf{X}_1, \vec{\mu })\\ \vdots \\ \frac{\partial \rho }{\partial \mu _ d } (\mathbf{X}_1, \vec{\mu })\end{pmatrix}\right]\qquad (d\times d).
  $$
  If we have one parameter, the covariance is just the variance 
  $$
  K(\mu) = \mathsf{Var}\left[{\partial \rho\over\partial \mu }(X_1, \mu)\right]
  $$

* Let the curvature be $J(\mu) = {\partial^2 \mathcal{Q} \over\partial \mu \partial \mu^T }(\mu)$ ($= \mathbb{E}\left[ {\partial^2\rho \over\partial \mu \partial \mu^T }(X_1, \mu)\right]$ under some regularity conditions).

  Formally,
  $$
  \mathbf{J}\, =\, \mathbb E[\mathbf{H}\rho ] =\mathbb E\left[\begin{pmatrix} \frac{\partial ^2 \rho }{\partial \mu _1 \partial \mu _1} (\mathbf{X}_1, \vec{\mu })& \ldots &  \frac{\partial ^2 \rho }{\partial \mu _1 \partial \mu _ d} (\mathbf{X}_1, \vec{\mu })\\ \vdots & \ddots & \vdots \\ \frac{\partial ^2 \rho }{\partial \mu _ d \partial \mu _1} (\mathbf{X}_1, \vec{\mu })& \ldots &  \frac{\partial ^2 \rho }{\partial \mu _ d \partial \mu _ d} (\mathbf{X}_1, \vec{\mu })\end{pmatrix}\right]\qquad (d\times d)
  $$
  In one dimension (i.e. $d = 1$), the matrices reduce to 
  $$
  J(\mu )= \mathbb E\left[ \frac{\partial ^2 \rho }{\partial \mu ^2} (X_1, \mu ) \right]
  $$

**Remark 1**: In the log-likelihood case (write $\mu = 0$).

$J(\theta) = K(\theta)= \mathcal{I}(\theta) \qquad \text{ Fisher Information}$

Note that in general the functions $J(\mu)$ and $K(\mu)$ will not equal to each other. In the special case where $\rho(x,\mu)$ is defined to be the negative log-likelihood of the statistical model, then it is true that $J(\mu) = K(\mu)$.

**Remark 2**: Under some technical conditions, the functions $J(\mu)$ and $K(\mu)$ determine the asymptotic variance of the M-estimator $\widehat{\mu}$. The asymptotic variance of $\widehat{\mu}_n$ is given by $\, J(\mu ^*)^{-1} K(\mu ^*) J(\mu ^*)^{-1},$  assuming some hypotheses.

**Remark 3 on signs: ** Let's match the signs in the definition of $\mathbf{J}$ and $\mathbf{K}$ with those in the definition of Fisher information. For maximum likelihood estimation,
$$
\rho _ n(\theta )\, :=\, \rho (\mathbf{X}_1,\, \ldots ,\, \mathbf{X}_ n,\, \theta ) = {-} \ell _ n(\theta )\qquad \text {where }\, \ell _ n(\theta )\, =\,  \ln L_ n(\mathbf{X}_1,\, \ldots ,\, \mathbf{X}_ n,\theta ).
$$
For this particular loss function $\rho$, the $\mathbf{J}$ and $\mathbf{K}$ matrices are
$$
\begin{aligned}
\mathbf{J} =& \mathbb E[\mathbf{H}\rho _1(\theta )]\, =\, -\mathbb E[\mathbf{H}\ell _1(\theta )]\\
\mathbf{K} =&  \textsf{Cov}[\nabla \rho _1(\theta )]\, =\, \textsf{Cov}[-\nabla \ell _1(\theta )]\, =\, \textsf{Cov}[\nabla \ell _1(\theta )]\\ 
& (\textsf{Cov}[\mathbf{Y}]=\textsf{Cov}[-\mathbf{Y}]\, \text {for any random vector }\, \mathbf{Y}.
\end{aligned}
$$
Both of these matrices equals the Fisher information matrix.

#### Asymptotic Normality

Let $\mu^* \in \mathcal{M}$ (the true parameter). Assume the following:

1. $\mu^*$ is the only minimizer of the function $\mathcal{Q}$.
2. $J(\mu)$ is invertible for all $\mu \in \mathcal{M}$.
3. A few more technical conditions.

Then, $\hat{\mu}_n$ satisfies:

* $\hat{\mu}_n \xrightarrow[n \rightarrow \infty]{ \mathbf{P}} \mu^*$.
* $\sqrt{n} (\hat{\mu}_n - \mu^*) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N} (0, J(\mu^*)^{-1} K(\mu^*) J(\mu^*)^{-1})$.

> #### Exercise 67
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}$. Let $\rho(x,\mu)$ denote a loss function satisfying 
> $$
> \mu^* = \text{argmin}_{\mu \in R} \mathbb{E}[\rho(X_1, \mu)]
> $$
> Where $\mu^* \in \R$ is some unknown one-dimensional parameter associated with $\mathbf P$ that we would like to estimate. Let 
> $$
> J(\mu ) =\mathbb E\left[ \frac{\partial ^2 \rho }{\partial \mu ^2} (X_1, \mu ) \right]\\
> K(\mu ) = \text {Var}\left[ \frac{\partial \rho }{\partial \mu }(X_1, \mu ) \right]
> $$
> You construct the M-estimator $\hat{\mu}_n$ associated $\rho$.
>
> 1. Assuming that the conditions for the asymptotic normality of this M-estimator hold, we have
>    $$
>    \sqrt{n} \frac{\widehat{\mu }_ n - \mu ^*}{\sqrt{ J(\mu ^*)^{-2} K(\mu ^*)} } \xrightarrow [n \to \infty ]{(d)} Q
>    $$
>    For some distribution $Q$. What is $Q$?
>
> 2. Let $q_\alpha$ denote the $(1-\alpha)$-quantile of the distribution $Q$. For what value of $q_\alpha$ is it true that
>    $$
>    \mu ^* \in \left[ \widehat{\mu }_ n - q_{\alpha } \sqrt{\frac{J(\mu ^*)^{-2} K(\mu ^*)}{n}} , \widehat{\mu }_ n + q_{\alpha } \sqrt{\frac{J(\mu ^*)^{-2} K(\mu ^*)}{n}} \right]
>    $$
>    with probability $95\%$ as $n \rightarrow \infty$?
>
> 3. Let 
>    $$
>    \mathcal{I} := \left[ \widehat{\mu }_ n - q_{\alpha } \sqrt{\frac{J(\mu ^*)^{-2} K(\mu ^*)}{n}} , \widehat{\mu }_ n + q_{\alpha } \sqrt{\frac{J(\mu ^*)^{-2} K(\mu ^*)}{n}} \right]
>    $$
>    denote the interval in the previous questions.
>
>    Is $\mathcal{I}$ and asymptotic confidence interval for $\mu^*$ of confidence level $95\%$?
>
> **Answer:**
>
> 1. Standard normal
> 2. 1.96
> 3. No, because the endpoints of $\mathcal{I}$ depend on the true parameter.
>
> **Solution:**
>
> 1. $Q$ is a standard normal distribution. Referring to the theorem regarding the asymptotic normality of the M-estimators, we see that the asymptotic variance of $\widehat{\mu}_n$ is $J(\mu ^*)^{-2} K(\mu ^*)$. Hence,
>    $$
>    \sqrt{n} \frac{\widehat{\mu _ n} - \mu ^*}{\sqrt{J(\mu ^*)^{-2} K(\mu ^*)}} \xrightarrow [(d)]{n \to \infty } \mathcal{N}(0,1).
>    $$
>
> 2. $q_\alpha = 1.96$.
>    $$
>    \begin{aligned}
>    P\left( \sqrt{n} \bigg| \frac{\widehat{\mu }_ n - \mu ^*}{\sigma } \bigg| \geq q_{0.025} \right) &= 1 - P \left( \mu ^* \in \left[ \widehat{\mu }_ n - q_{0.025} \sqrt{\frac{J(\mu ^*)^{-2} K(\mu ^*)}{n}} , \widehat{\mu }_ n + q_{0.025} \sqrt{\frac{J(\mu ^*)^{-2} K(\mu ^*)}{n}} \right] \right)\\ &= 0.05
>    \end{aligned}
>    $$
>    where $q_{0.025}=1.96$ is the $95\%$-quantile of a standard Gaussian.
>
> 3. By definition, the endpoints of a confidence interval should be estimators, and this is not the case for $\mathcal{I}$ because $K^{-1}(\mu ^*)$ and $J(\mu ^*)$ depend on the true parameter.

## 3. Robust Statistics and Cauchy's Distribution

Example: **Location parameter**

If $X_1, ..., X_n$ are i.i.d. with density $f(\cdot -m)$, where

* $f$ is an unknown, positive, even function (e.g. the Cauchy density);

  * **Cauchy distribution** is a continuous distribution with a parameter $m$, the PDF is: 
    $$
    f_m(x) = {1\over \pi} {1 \over 1 + (x-m)^2}
    $$
    Set $m=0$ and compute the mean,
    $$
    \int _{-\infty }^{\infty } \frac{1}{\pi } \cdot \frac{x}{1 + x^2} \,  dx  =  \frac{1}{2\pi } \ln (1 + x^2)
    $$
    which is unbounded as $|x|\rightarrow \infty$.

    Hence, $\mathbb{E}[X]$ is not defined.
    $$
    \int \vert x \vert f_m(x)dx= \infty
    $$

* $m$ is a real number of interest, a **location parameter**.

How to estimate $m$?

* M-estimators: empirical mean, empirical median,...
* Compare their risks or asymptotic variances;
* The empirical median is more robust.

Some estimators are more resilient to corruptions or mistakes in the data than others. They are referred to as **robust**. 

* For example, **median** is more robust than mean in describing the average of the data especially when there is a typo in one data point.

> #### Exercise 68
>
> Recall that the **median** of a continuous distribution is any number $M$ such that $P(X > M) = P(X < M) = 1/2$. For the Cauchy distribution, it turns out that the median is unique.
>
> 1. If the location parameter is set to be $m=1/2$, what is med$(X)$?
>
> 2. As in the previous problem, set $X$ denote a random variable distributed as the Cauchy distribution with location parameter $m$. Which of the following are true about the random variable $X-m$?
>
>    a. The expectation (first moment) of $X-m$ is not defined.
>
>    b. $X-m$ Is distributed as a Cauchy random variable with location parameter set to be $0$.
>
>    c. $X-m$ Is symmetric in the sense that $X-m$ and $m-X$ both have the same distribution.
>
>    d. The method of moments can be used to estimate the location parameter $m$.
>
> **Answer:** 
>
> 1. 0.5
> 2. abc
>
> **Solution:**
>
> 1. The answer is $1/2$ since
>    $$
>    P(X > 1/2) = \displaystyle \int _{1/2}^{\infty } \frac{1}{\pi } \cdot \frac{1}{1 + (x-1/2)^2} \,  dx = - \displaystyle \int _{1/2}^{-\infty } \frac{1}{\pi } \cdot \frac{1}{1 + (-y + 1/2)^2} \,  dy = P(X < 1/2).
>    $$
>    It follows from making the substitution $x = -y + 1$.
>
> 2. a. The improper integral (to compute the mean)
>    $$
>    \int _{-\infty }^\infty \frac{1}{\pi } \cdot \frac{x}{1 + (x - m)^2} \,  dx
>    $$
>    does not converge, so the expectation of $X$ is not defined.
>
>    b. $X-m$ has the same CDF as a Cauchy random variable $Y$ with location parameter set to be $0$.
>    $$
>    P( X - m < t) = \displaystyle \int _{-\infty }^{t + m} \frac{1}{\pi } \cdot \frac{1}{1 + (x - m)^2} \,  dx = \displaystyle \int _{-\infty }^{t} \frac{1}{\pi } \cdot \frac{1}{1 + y^2} \,  dy = P(Y < t).
>    $$
>    Here we made the substitution $y=x-m$.
>
>    c. $X-m$ has a density given by $f(x) = \frac{1}{\pi } \frac{1}{1 + x^2}$. This is an even function, so it follows that $X-m$ and $m-X$ have the same distribution.
>
>    d. Since the moments of a Cauchy random variable do not exit, the method of moments cannot be used for parameter estimation for this family of distribution.

## 4. Robust Statistics and Huber's Loss

Huber's loss:
$$
h_\delta(x) = \begin{cases} {x^2 \over 2} & \text{if }|x| \leq \delta\\ \delta(|x| - {\delta \over 2}) & \text{if } |x| > \delta \end{cases}
$$
![images_u3s5_huberloss](../assets/images/images_u3s5_huberloss.svg)

The first derivative of Huber's loss is the **clip function**:
$$
h_\delta'(x) = \text{clip}_\delta(x) = \begin{cases} -\delta & \text{if }x < -\delta\\ x& \text{if }|x| \leq \delta \\ \delta & \text{if }x > \delta \end{cases}
$$
The second derivative is
$$
h_\delta''(x) = \mathbf{1}_{(|x| \leq \delta)}
$$

M-estimation tries to estimate a parameter by minimizing some loss function.

In the univariate case with data $X_i$, this procedure takes the form
$$
\hat{\mu} = \text{argmin}_{b \in \R}\sum^n_{i=1}\rho(x_i - m)
$$
for some choice of function $\rho$​. Some examples include $\rho(x) = x^2$​, which yields the sample mean; $\rho(x)=|x|$, which yields the sample median, and 
$$
\rho(x) = \begin{cases}|x-m|, & |x-m| \geq \delta \\ {(x-m)^2 \over 2\delta} + {\delta \over 2}, & |x-m| < \delta \end{cases}
$$
for some parameter $\delta$​, which is called the **Huber loss function**.

## 5. Applying Huber's loss to the Laplace distribution

#### The Laplace Distribution

The **Laplace distribution** (also known as the **double-exponential distribution**) is a continuous distribution with location parameter $m \in \R$ and density given by
$$
f_m(x)={1\over 2} \exp(-|x-m|)
$$
The likelihood for $n$ observations is given by
$$
\prod _{i = 1}^ n f_ m(X_ i) = \frac{1}{2^ n} \prod _{i = 1}^ n e^{-|x - m|}.
$$
Therefore, the log likelihood is
$$
\log L(X_1, ...,X_n;m) = \sum^n_{i=1} \log \left( {1\over 2} \exp(-|x-m|) \right) = - n \log 2 - \sum^n_{i=1} |X_i - m|
$$
The MLE estimator is
$$
\hat{m}^{MLE} = \text{argmin}_{m}\sum^n_{i=1}|X_i - m|
$$
where $|X_i - m|$ is called **empirical median**.

> #### Exercise 69
>
> Let $X$ denote a Laplace variable with location parameter set to be $m=0$.
>
> 1. What is $\mathbb{E}[X]$?
>
> 2. Does the variance $\sigma ^2 = \mathbb E[(X - \mathbb E[X])^2]$ exist?
>
> 3. Which of the following are true about $X$? (Hint: The function $x^ k e^{-|x|}$ is integrable, i.e. $\int _{-\infty }^{\infty }x^ k e^{-|x|} dx$ is finite for all $k$.)
>
>    a. The distribution of $X$ is symmetric in the sense that $X$ and $-X$ have the same distribution.
>
>    b. The function $\ln f_m(x)$ has a continuous first derivative
>
>    c. For any integer $k>0$, the $k$-th moment $\mathbb{E}[X^k]$ exists.
>
> **Answer:**
>
> 1. $\mathbb{E}[X]=0$
> 2. Yes.
> 3. ac.
>
> **Solution:**
>
> 1. We observe that the function $x e^{-|x|}$ is odd and also integrable. Therefore,
>    $$
>    \mathbb E[X] = \int _{-\infty }^\infty \frac{1}{2} x e^{-|x|} \,  dx = 0.
>    $$
>
> 2. The function $x^2 e^{-|x|}$ is integrable. Hence,
>    $$
>    \mathbb E[(X - \mathbb E[X])^2] = \mathbb E[X^2] = \displaystyle \int _{-\infty }^\infty \frac{1}{2} x^2 e^{-|x|} \,  dx
>    $$
>
> 3. a. Yes because the density $\frac{1}{2} e^{-|x|}$ is an even function.
>
>    b. No because $\ln f_ m(x) = -|x - m|$ is not differentiable at $x=m$.
>
>    c. Yes because the function $x^ k e^{-|x|}$ is integrable on $\R$, so the $k$-th moment $x^ k e^{-|x|}$ exists for all $k > 0$.

> #### Exercise 70
>
> Let $\widehat{m}_ n^{\text {MLE}}$ denote the MLE for an unknown parameter $m^*$ of a Laplace distribution.
>
> Can we apply the theorem for the asymptotic normality of the MLE to $\widehat{m}_ n^{\text {MLE}}$?
>
> **Answer:** No because the log-likelihood is not twice-differentiable, so the Fisher information does not exist.
>
> **Solution:** This is because $\ell _ n(X_1, \ldots , X_ n; m)$ has discontinuities in its first derivative with respect to $m$ at $m=X_i$ for $i=1,...,n.$

#### Asymptotic Normality

In the framework of M-estimation, our loss function is not Huber's loss itself, but rather,  
$$
\rho(X,m) = h_\delta(X-m)
$$
Since $\rho(x,m)$ is **twice-differentiable**, functions $K$ and $J$ exist for a Laplace statistical model.

$J(m)$ is
$$
\begin{aligned}
J(m) &= \mathbb{E}[h_\delta''(X)] = \mathbb{E}[\mathbf{1}(|X-m| \leq \delta)] = \mathbf{P}(|X-m|\leq \delta)\\
&= 2 \int^\delta_0 f_0(x)dx = \int^\delta_0 e^{-x} dx = 1-e^{-\delta}
\end{aligned}
$$
$K(m)$ is
$$
\begin{aligned}
K(m) &= \mathsf{Var}(\text{Clip}_\delta(X-m))\\
&= \mathbb{E}[\text{clip}_\delta^2(X-m)] - \mathbb{E}[\text{clip}_\delta(X-m)]^2\\

\end{aligned}
$$
We know that
$$
\begin{aligned}
\mathbb{E}[\text{clip}_\delta(X-m)] &= 0\\
\mathbb{E}\left[\text{clip}_\delta^2(X-m)\right] &= 2 \left[\int^\delta_0 x^2 f_0(x)dx + \int^\infty_\delta \delta^2 f_0(x)dx\right]\\
&= 2\int^\delta_0 x^2 {e^{-x}\over 2} dx + \delta^2 \int^{\infty}_\delta e^{-x} dx\\
&= \int^\delta_0 x^2 e^{-x} dx + \delta^2 \int^{\infty}_\delta e^{-x} dx\\
\end{aligned}
$$
Apply the formula of **integration by parts**.
$$
\begin{aligned}
\int^\delta_0 x^2 e^{-x} dx &= - x^2 e^{-x} |^{\delta}_0 + 2 \int^{\delta}_0 x e^{-x}dx\\
&= \delta^2 e^{-\delta} + 2\left[ -x e^{x}|^\delta_0 + \int^\delta_0 e^{-x}dx \right]\\
&= -\delta^2 e^{-\delta} - 2 \delta e^{-\delta} + 2 - 2e^{-\delta}
\end{aligned}
$$
We have $K(m)$,
$$
K(m) =-\delta^2 e^{-\delta} - 2 \delta e^{-\delta} + 2 - 2e^{-\delta} + \delta^2 e^{-\delta} = - 2 \delta e^{-\delta} + 2 - 2e^{-\delta}
$$
Therefore, for $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Lap}(m^*)$, the M estimator is
$$
\widehat{m}(\delta) = \text{argmin}_{m\in \R} {1\over n} \sum^n_{i=1} h_{\delta} (X_i - m)
$$
where we emphasize the dependence on the parameter $\delta \in (0,\infty)$.

$\widehat{m}$ is **asymptotic normal** since $m^*$ is the **unique minimizer** of the function $m \mapsto \mathbb E_{X \sim P_{m^*}}[\rho (X, m)]$, and $J(m)$ is **invertible**, given $J(m) = 1 - e^{-\delta }$.
$$
\sqrt{n}( \widehat{ m}(\delta ) - m^*) \xrightarrow [n \to \infty ]{(d)} N\left( 0 \,  , \,  g(\delta ) \right).
$$
where 
$$
g(\delta ) = \frac{2(1 - \delta e^{-\delta } - e^{-\delta })}{(1 - e^{-\delta })^2}.
$$
We can extend $g$ to be a continuous function with domain $[0,\infty]$ by setting $g(0)=1$ and $g(\infty) =2$.

By graphing, $g(\delta)$ is an **increasing** function on $[0,\infty]$. The minimum asymptotic variance is for $\delta \rightarrow 0$, where $\hat{m}_0 = 1$, implying that $\hat{m}_0 = \hat{m}^{MLE}$. While the maximum asymptotic variance is for $\delta \rightarrow \infty$, where $\hat{m}_\infty = \overline{X}_n$. 

> #### Exercise 71
>
> Find the value of 
> $$
> \frac{\partial }{\partial m} \mathbb E_{X \sim P_{m^*}}[ h_{\delta }(X - m) ] \bigg|_{m = m^*}.
> $$
> where $h_\delta(X-m)$ is the Huber's loss.
>
> **Answer:** 0
>
> **Solution:**
>
> Observe that
> $$
> \begin{aligned}
> \frac{\partial }{\partial m} \mathbb E_{X \sim P^*_ m}[h_\delta (X-m)] &= \mathbb E_{X \sim P^*_ m}\left[ \frac{\partial }{\partial m} h_\delta (X-m) \right] \\
> &= \frac{1}{2} \displaystyle \int _{-\infty }^\infty \text {clip}_\delta (x - m) e^{-|x - m^*|} \,  dx\\
> &=  \frac{1}{2} \left( -\delta \displaystyle \int _{m + \delta }^\infty e^{-|x - m^*|} \, dx + \delta \displaystyle \int _{-\infty }^{-\delta + m} e^{-|x - m^*|} \, dx + \displaystyle \int _{-\delta + m}^{\delta + m} \,  (x-m) e^{-|x-m^*|} dx \right).
> \end{aligned}
> $$
> Applying the change of variables $y = x-m$, we have
> $$
> = \frac{1}{2} \left( -\delta \displaystyle \int _\delta ^\infty e^{-|y + m - m^*|} \, dy + \delta \displaystyle \int _{-\infty }^{-\delta } e^{-|y + m - m^*|} \, dy + \displaystyle \int _{-\delta }^\delta y e^{-|y + m - m^*|} \,  dy \right).
> $$
> Setting $m=m^*$, we have
> $$
> \frac{\partial }{\partial m} \mathbb E_{X \sim P^*_ m}[h_\delta (X)] \bigg|_{m = m^*} = \frac{1}{2} \left( -\delta \displaystyle \int _\delta ^\infty e^{-|y|} \, dy + \delta \displaystyle \int _{-\infty }^{-\delta } e^{-|y|} \, dy + \int _{-\delta }^\delta y e^{-|y|} \,  dy \right) = 0.
> $$
> **Remark:** The function $m \mapsto \mathbb E_{X \sim P^*_ m}[h_\delta (X)]$ is strictly convex, so this means the loss function has a unique critical point, and this is where the minimum is attained. The above calculation guarantees that the minimum is at $m=m^*$, the value of the true parameter.

> #### Exercise 72
>
> If $\delta = \infty$, it makes sense to extend the definition of Huber's loss to be
> $$
> h_\infty (x) = \frac{x^2}{2}.
> $$
> Setting $\delta = \infty$, we have
> $$
> \widehat{m}(\infty ) = \text {argmin}_{m \in \mathbb {R}} \frac{1}{2n} \sum _{i = 1}^ n (X_ i - m)^2.
> $$
> What is another name for $\widehat{m}(\infty )$?
>
> **Answer:** The sample average.
>
> **Solution:** 
>
> Let differentiate and find the value of $m$ that is a critical point of the function
> $$
> F(m) := \frac{1}{2n} \sum _{i = 1}^ n (X_ i - m)^2.
> $$
> Observe that
> $$
> F'(m) = -\frac{1}{n} \sum _{i = 1}^ n (X_ i - m).
> $$
> Setting $m = \frac{1}{n} \sum _{i = 1}^ n X_ i$, we see that $F'(m) = 0$. By strict convexity, this implies that the sample average is the unique global minimizer of $F(m)$.

#### The Sample Median

Let $S=x_1 < x_2 < ... < x_n$ denote a sorted list of numbers. We define the elementary median med$_e(S)$ to be 
$$
\text {med}_ e(S) := \begin{cases}  x_{\lceil n/2 \rceil } & \text {if} \,  \,  \,  n \,  \text {is odd} \\ \frac{1}{2}(x_{n/2} + x_{n/2 + 1}) & \text {if} \,  \,  \,  n \,  \text {is even} \end{cases}
$$
A more advanced definition, useful for statistical purposes, is to define the sample median med$_s(S)$ of a sample $S:= X_1, X_2, ..., X_n$ to be
$$
\text {med}(S) := \text {argmin}_ m \sum _{i =1 }^ n \left| X_ i - m \right|.
$$
While the elementary median is unique, this is not always the case for the sample median.

## 6. Review of Methods of Estimation

Recap

* Three principled methods for estimation: maximum likelihood, Method of moments, M-estimators.
* Maximum likelihood is an example of M-estimation.
* Method of moments inverts the function that maps parameters to moments.
* All methods yield to asymptotic normality under regularity conditions.
* Asymptotic covariance matrix can be computed using multivariate delta-method.
* For MLE, asymptotic covariance matrix is the inverse Fisher information matrix.

> #### Exercise 73
>
> Which of the following estimators are defined in terms of an optimization problem?
>
> a. Maximum likelihood estimator
>
> b. Method of moments estimator
>
> c. M-estimator
>
> **Answer:** ac
>
> **Solution:**
>
> The MLE is defined by maximizing the log-likelihood, and an M-estimator is defined by minimizing a loss function. However, the method of moments estimator is constructed by solving a system of equations.

> #### Exercise 74
>
> All three method of estimation studied in this unit: maximum likelihood estimation, the method of moments, and M-estimation, lead to asymptotically normal estimators if certain technical conditions are satisfied.
>
> In general, an asymptotically normal estimator $\widehat{\theta }_ n$ can be used to construct a confidence interval for an unknown parameter.
>
> What quantity related to the estimator $\hat{\theta}$ determines the length of an asymptotic confidence interval at level $95\%$ (Assume that you use the plug-in method and that $n$ is very large.)
>
> a. The asymptotic variance of $\hat{\theta}_n$.
>
> b. The rate of convergence of $\hat{\theta}_n$ to the normal distribution $\mathcal{N}(0,1)$.
>
> c. The mean of $\hat{\theta}_n$.
>
> **Answer:** a
>
> **Solution:**
>
> Consider an asymptotically normal estimator $\widehat{\theta_n}$, which satisfies
> $$
> \sqrt{n} (\widehat{\theta _ n} - \theta ) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0, \sigma ^2)
> $$
> for some asymptotic variance $\sigma^2 > 0$. Let $q_{\alpha/2}$ denote the $\alpha/2$-quantile of a standard Gaussian. Then we have that
> $$
> P\left( \sqrt{n} \frac{\bigg| \widehat{\theta _ n} - \theta \bigg|}{\sigma } \geq q_{\alpha /2} \right) \xrightarrow {n \to \infty } \alpha
> $$
> which implies that 
> $$
> P\left( \theta \notin \left[ \widehat{\theta _ n} - q_{\alpha /2} \frac{\sigma }{\sqrt{n}}, \widehat{\theta _ n} + q_{\alpha /2}\frac{\sigma }{\sqrt{n}} \right] \right) \xrightarrow {n \to \infty } \alpha .
> $$
> Therefore, using the plug-in method, we have that
> $$
> P\left( \theta \notin \left[ \widehat{\theta _ n} - q_{\alpha /2}\frac{\widehat{\sigma }}{\sqrt{n}}, \widehat{\theta _ n} + q_{\alpha /2}\frac{\widehat{\sigma }}{\sqrt{n}} \right] \right) \xrightarrow {n \to \infty } \alpha ,
> $$
> Setting $\alpha=0.05$, we have that
> $$
> \mathcal{I} := \left[ \widehat{\theta _ n} - q_{\alpha /2}\frac{\widehat{\sigma }}{\sqrt{n}}, \widehat{\theta _ n} + q_{\alpha /2}\frac{\widehat{\sigma }}{\sqrt{n}} \right]
> $$
> If $n$ is very large, we have that $\widehat{\sigma }_ n \approx \sigma$, so the length of $\mathcal{I}$ is approximately $2 q_{0.025} \sigma /\sqrt{n}$. That is, the length depends only on the $\alpha/2$ quantile, the sample size, and the asymptotic variance. 

