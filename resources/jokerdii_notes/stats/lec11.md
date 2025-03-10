# Lecture 11. Fisher Information, Asymptotic Normality of MLE, and the Method of Moments

There are 7 topics and 7 exercises.

## 1. Fisher Information

**Definition 1:**

Define the log-likelihood for one observation as:
$$
\ell(\theta) = \log L_1(X,\theta), \quad \theta \in \Theta \subset \R^d
$$
Assume that $\ell$ is a.s. twice differentiable. Under some regularity conditions, the Fisher information of the statistical model is defined as
$$
I(\theta) =\mathsf{Cov}(\nabla \ell(\theta)) = \mathbb{E}[\nabla \ell(\theta) \nabla\ell(\theta)^T] - \mathbb{E}[\nabla \ell(\theta)]\mathbb{E}[\nabla \ell(\theta)]^T = - \mathbb{E}[\mathbf{H}\ell(\theta)]
$$
The log-likelihood is a concave function with a negative Hessian, so $ \mathbb{E}[\mathbf{H}\ell(\theta)]$ is negative and the fisher information is positive.

If $\Theta \subset \R$, we get 
$$
I(\theta) = \mathsf{var}[\ell'(\theta)] = -\mathbb{E}[l''(\theta)]
$$
**Definition 2:**

Let $(\mathbb {R}, \{ \mathbf{P}_\theta \} _{\theta \in \mathbb {R}})$ denote a continuous statistical model. Let $f_\theta (x)$ denote the pdf (probability density function) of the continuous distribution $\mathbf{P}_\theta$. Assume that $f_\theta (x)$ is twice-differentiable as a function of the parameter $\theta$.

Recall that
$$
\int _{-\infty }^\infty f_\theta (x) \,  dx = 1
$$
for all $\theta \in \R$.

Take the derivative,
$$
\frac{\partial }{\partial \theta }  \int _{-\infty }^\infty f_\theta (x) \,  dx  = 0\\
$$
Therefore,
$$
\int _{-\infty }^\infty \frac{\partial }{\partial \theta } f_\theta (x) \,  dx  = 0\\
\int _{-\infty }^\infty \frac{\partial ^2}{\partial \theta ^2} f_\theta (x) \,  dx =0
$$
The first derivative of the likelihood is
$$
\ell '(\theta ) = \frac{\partial }{\partial \theta } \ln f_\theta (X) = \frac{\frac{\partial }{\partial \theta } f_\theta (X)}{f_\theta (X)}.
$$
The expectation of it is
$$
\mathbb{E}[\ell'(\theta)]=\mathbb {E}\left[\frac{\frac{\partial }{\partial \theta } f_\theta (X)}{f_\theta (X)}\right] = \int _{-\infty }^\infty \left( \frac{\frac{\partial }{\partial \theta } f_\theta (x)}{f_\theta (x)} \right) f_\theta (x) \,  dx = \int _{-\infty }^\infty \frac{\partial }{\partial \theta } f_\theta (x) \,  dx = 0,
$$
The variance of it is by definition the fisher information
$$
\textsf{Var}(\ell '(\theta )) = \mathcal{I}(\theta)
$$
By definition of variance,
$$
\textsf{Var}(\ell '(\theta )) = \mathbb {E}[\ell '(\theta )^2] - \mathbb {E}[\ell '(\theta )]^2 = \mathbb {E}[\ell '(\theta )^2]  - 0 = \mathbb {E}[\ell '(\theta )^2] 
$$
Hence, the variance can be written as
$$
\begin{aligned}
\textsf{Var}\left(\ell '(\theta )\right) &=\mathbb {E}\left[(\ell '(\theta ))^2\right]\\
&= \mathbb {E}\left[\left( \frac{\frac{\partial }{\partial \theta }f_\theta (X)}{f_\theta (X)} \right)^2\right]\\
&= \int _{-\infty }^\infty \frac{(\frac{\partial }{\partial \theta } f_\theta (x))^2}{f_\theta (x)} \,  dx.
\end{aligned}
$$
Alternatively, the fisher information can be computed from 
$$
\mathcal{I}(\theta) = -\mathbb{E}[l''(\theta)]
$$
By computing $-\mathbb{E}[l''(\theta)]$ we can prove
$$
\mathsf{var}[\ell'(\theta)] = -\mathbb{E}[l''(\theta)]
$$
The second derivative of the likelihood is
$$
\ell''(\theta) = {{\partial^2 \over \partial \theta^2 }f_\theta(x) f_\theta(x) - ({\partial \over \partial \theta }f_\theta(x) )^2 \over (f_\theta(x))^2 }
$$
The negative expectation is
$$
\begin{aligned}
-\mathbb{E}[l''(\theta)] &= -\mathbb{E}\left[{{\partial^2 \over \partial \theta^2 }f_\theta(x) f_\theta(x) - ({\partial \over \partial \theta }f_\theta(x) )^2 \over (f_\theta(x))^2 }\right]\\
&= -\int {{\partial^2 \over \partial \theta^2 }f_\theta(x) f_\theta(x) - ({\partial \over \partial \theta }f_\theta(x) )^2 \over (f_\theta(x))^2 } f_\theta(x)\ dx\\
&= -\int {{\partial^2 \over \partial \theta^2 }f_\theta(x) f_\theta(x) - ({\partial \over \partial \theta }f_\theta(x) )^2 \over f_\theta(x) } \ dx\\
&= -\int  {\partial^2 \over \partial \theta^2 }f_\theta(x)\ dx + \mathsf{Var}(\ell'(\theta))\\
&= - 0 + \mathsf{Var}(\ell'(\theta))\\
&=\mathsf{Var}(\ell'(\theta))
\end{aligned}
$$
**Remark:** A convenient way to compute the Fisher information is to use 
$$
\mathcal{I}(\theta ) = \int _{-\infty }^\infty \frac{(\frac{\partial }{\partial \theta } f_\theta (x))^2}{f_\theta (x)} \,  dx.
$$

## 2. Examples of Fisher Information Computation

**Fisher Information of the Bernoulli Random Variable**

Let $X \sim \mathsf{Ber}(p)$, the PDF is 
$$
f_p(x) = p^x(1-p)^{1-x}
$$
The likelihood is
$$
\ell(p) = x\log p  + (1-x) \log(1-p)
$$
The first derivative of the likelihood is
$$
\ell'(\theta) = {x \over p} - {1-x\over 1-p}
$$
The second derivative of the likelihood is
$$
\ell''(\theta) = -{x \over p^2} - {1-x \over (1-p)^2}
$$
The fisher information can be computed from 
$$
\begin{aligned}
\mathsf{Var}(\ell'(\theta)) &= \mathsf{Var}(x({1\over p}+ {1\over 1-p}) - {1\over 1-p})\\
&= \mathsf{Var} (x({1\over p}+ {1\over 1-p}))\\ 
&= {p(1-p) \over p^2 (1-p)^2}\\ 
&= {1 \over {p(1-p)}}
\end{aligned}
$$
Alternatively,
$$
\begin{aligned}
\mathbb{E}[\ell''(\theta)] &= - {\mathbb{E}[X]\over p^2} - {1-\mathbb{E}[X] \over (1-p)^2}\\
&= -{1\over p} - {1\over 1-p}\\
&= -{1 \over p(1-p)}
\end{aligned}
$$
**Remark:** Computing by $\mathbb{E}[\ell''(\theta)]$ is actually the fast method in most cases.

> #### Exercise 60
>
> Let $\mathbf{X}$ be a Gaussian random vector with **independent** components $X^{(i)} \sim \mathcal{N}(\alpha + \beta t_ i,1)$ for $i = 1,...,d$, where $t_i$ are known constants and $\alpha$ and $\beta$ are unknown parameters.
>
> Compute the Fisher information matrix $\mathcal{I}(\theta )$ using the formula $\mathcal{I}(\theta ) = -\mathbb E\left[\mathbf{H}\ell (\theta )\right]$.
>
> **Solution:**
>
> Let $\theta = [\alpha ~ ~ \beta ]^ T$ denote the parameters of the statistical model. The **joint distribution** of the random vector $\mathbf {X}$ is equal to the product of the marginal distribution of its components $(2\pi ^{-1/2}e^{-(x^{(i)} - \alpha - \beta t_ i)/2}$, by independence. Therefore, the random vector $\mathbf X$ has the density
> $$
> f_\theta (\mathbf x) = (2\pi )^{-\frac{d}{2}} e^{-\frac{1}{2}\sum _{i=1}^ d \left(x^{(i)} - \alpha - \beta t_ i \right)^2}, \quad \text {where} \quad \mathbf x= \left[x^{(1)}~ ~ x^{(2)}~ ~ \cdots ~ ~ x^{(d)}\right]^ T \in \mathbb {R}^ d.
> $$
> Taking the log of the pdf yields (written as a random function)
> $$
>  \ell (\theta ) = -\frac{d}{2}\ln (2\pi ) - \frac{1}{2}\left[\sum _{i=1}^ d \left( (X^{(i)} - \beta t_ i)^2 - 2 \alpha (X^{(i)} - \beta t_ i) + \alpha ^2\right)\right]
> $$
> Therefore, the gradient of the likelihood with respect to $\theta$ is
> $$
> \nabla \ell (\theta ) = \begin{bmatrix}  \sum _{i=1}^ d \left(X^{(i)} - \beta t_ i - \alpha \right)\\ \sum _{i=1}^ d \left(t_ i X^{(i)} - \beta t_ i^2 - \alpha t_ i\right) \end{bmatrix},
> $$
> from which we can obtain the Hessian
> $$
> \mathbf{H}\ell (\theta ) = \begin{bmatrix}  \sum _{i=1}^ d (-1) &  \sum _{i=1}^ d (-t_ i)\\ \sum _{i=1}^ d (-t_ i) &  \sum _{i=1}^ d (-t_ i^2) \end{bmatrix}.
> $$
> Therefore,
> $$
> \mathcal{I}(\theta ) = -\mathbb E\left[\mathbf{H}\ell (\theta )\right] = \begin{bmatrix}  d &  \sum _{i=1}^ d t_ i\\ \sum _{i=1}^ d t_ i &  \sum _{i=1}^ d t_ i^2 \end{bmatrix},
> $$
> where the expectation is taken with respect to the pdf of the random vector $\mathbf X$. Since none of the entries of the hessian contained any $X^{(i)}$, the expectation was simply the Hessian matrix itself.

## 3. Fisher Information and the Asymptotic Normality of the ML Estimator

**Theorem**:

Let $\theta^* \in \Theta$ (the true parameter). Assume the following:

1. The parameter is identifiable.
2. For all $\theta \in \Theta$, the support of $\mathbb {P}_\theta$ does not depend on $\theta$.
3. $\theta^*$ Is not on the boundary of $\Theta$.
4. $\mathcal{I}(\theta)$ Is invertible in a neighborhood of $\theta^*$.
5. A few more technical conditions.

Then $\hat{\theta}_n^{MLE}$ satisfies

* $\hat{\theta}_n^{MLE} \xrightarrow[n\rightarrow \infty]{(d)} \theta^*$ w.r.t. $\mathbb{P}_{\theta^*}$
* $\sqrt{n}\left( \hat{\theta}_n^{MLE} - \theta^*\right) \xrightarrow[n\rightarrow \infty]{(d)}\mathcal{N}_d(0, \mathcal{I}(\theta^*)^{-1})$ w.r.t $\mathbb{P}_{\theta^*}$.

**Proof:**

The likelihood is
$$
l_i(\theta) = \log f_\theta(x_i)
$$
To find the MLE, we take the derivative and set it to zero
$$
{\partial\over \partial \theta} \sum^n_{i=1} l_1(\hat{\theta}) = \sum^n_{i=1} l_1'(\hat{\theta}) = 0
$$
We also know that $\mathbf{E}[l'(\theta^*)] = 0$.

By Taylor Series,
$$
\begin{aligned}
0 = \sum^n_{i=1}l_1'(\hat{\theta}) & \simeq \sum^n_{i=1}\left[ l_1'(\theta^*) + (\hat{\theta} - \theta^*) l''(\theta^*)\right]\\
&= {1\over \sqrt{n}} \sum^n_{i=1} \left[l_1'(\theta^*)-\mathbb{E}[l_1'(\theta^*)] + (\hat{\theta} - \theta^*) l''(\theta^*) \right]
\end{aligned}
$$
By CLT
$$
{1\over \sqrt{n}} \sum^n_{i=1} \left(l_1'(\theta^*)-\mathbb{E}[l_1'(\theta^*)]\right) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0, \mathsf{Var}(l'(\theta)))=\mathcal{N}(0, \mathcal{I}(\theta^*))
$$
Thus
$$
0 \simeq \mathcal{N}(0, \mathcal{I}(\theta^*)) + \sqrt{n}(\hat{\theta} - \theta^*) {1\over n} \sum^n_{i=1} l_1''(\theta^*)
$$
By LLN,
$$
{1\over n} \sum^n_{i=1} l_1''(\theta^*) \xrightarrow[n \rightarrow \infty]{(p)} \mathbb{E}[l_1''(\theta^*)] = - \mathcal{I}(\theta^*)
$$
Thus
$$
\begin{aligned}
0 &\simeq \mathcal{N}(0, \mathcal{I}(\theta^*)) - \sqrt{n}(\hat{\theta} - \theta^*) \mathcal{I}(\theta^*)\\
\implies& \sqrt{n}(\hat{\theta} - \theta^*) \sim \mathcal{N}(0, {\mathcal{I}(\theta^*)\over (\mathcal{I}(\theta^*))^2})\\
\implies& \sqrt{n}\left( \hat{\theta}_n^{MLE} - \theta^*\right) \xrightarrow[n\rightarrow \infty]{(d)}\mathcal{N}_d(0, \mathcal{I}(\theta^*)^{-1})
\end{aligned}
$$
**Conclusion:**

The **asymptotic normality of the ML estimator** depends upon the Fisher information. For a one-parameter model (like the exponential and Bernoulli), the asymptotic normality result will say something along the lines of following: that the asymptotic variance of the ML estimator is **inversely** proportional to the value of Fisher information at the true parameter of the statistical model. This means that if the value of Fisher information at is high, then the asymptotic variance of the ML estimator for the statistical model will be low.

> #### Exercise 61
>
> Let $(\mathbb {R}, \{ \mathbf{P}_\theta \} _{\theta \in \mathbb {R}})$ denote a statistical model. Recall that the MLE for one observation maximizes the log-likelihood for one observation, which is the random variable $\ell (\theta ) = \ln L_1(X, \theta )$ where $X \sim \mathbf{P}_\theta$. Suppose we observe $X_1 = x_1$, and now consider the graph of the function $\theta \mapsto \ln L_1(x_1, \theta )$.
>
> What does the Fisher information $\mathcal{I}(\theta )$ represent?
>
> **Solution:**
>
> It tells you, on average, how curved the function $\theta \mapsto \ln L(x_1, \theta )$ is.
>
> Recall $\mathcal{I}(\theta ) = -\mathbb {E}[\ell ^{\prime \prime }(\theta )]$. Since the second-derivative measures concavity/convexity (how curved a function is at a particular point), $\mathcal{I}(\theta )$ measures the *average* curvature of the function $\theta \mapsto \ell (\theta ) = \ln L_1(x_1, \theta )$.
>
> **Remark:**
>
> It turns out that the Fisher information tells how curved (on average) the log-likelihood $\ln L_ n(x_1, \ldots , x_ n, \theta )$ for several samples $X_1 = x_1, \ldots , X_ n = x_ n$ is. In particular, $\mathcal{I}(\theta ^*)$ tells how curved (on average) the log-likelihood is near the true parameter. As a rule of thumb, if the Fisher information $\mathcal{I}(\theta ^*)$ is large, then we expect the MLE to give a good estimate for $\theta^*$.

## 4. Method of Moments

Let $X_1, ..., X_n$ be an i.i.d. sample associated with a statistical model $(E, (\mathbb{P}_\theta)_{\theta \in \Theta})$.

* Assume that $E \subseteq \R$ and $\Theta \subseteq \R^d$, for some $d \geq 1$.

* Population moments: Let $m_k(\theta) = \mathbb{E}_\theta[X_1^k], 1 \leq k \leq d$.

* Empirical moments: Let $\hat{m}_k = \overline{X_n^k} = {1\over n} \sum\limits^n_{i=1} X_i^k, 1\leq k \leq d.$

* From LLN, they are consistent estimators
  $$
  \hat{m}_k \xrightarrow[n \rightarrow \infty]{\mathbb{P}/a.s} m_k(\theta)
  $$
  More compactly, we say that the whole vector converges
  $$
  (\hat{m}_1, ..., \hat{m}_d) \xrightarrow[n \rightarrow \infty]{\mathbb{P}/a.s} (m_1(\theta), ..., m_d(\theta))
  $$

**Moments estimator**

Let 
$$
\begin{aligned}
M : \Theta &\rightarrow \R^d\\
\theta &\mapsto M(\theta)= (m_1(\theta), ..., m_d(\theta))
\end{aligned}
$$
Assume $M$ is one to one:
$$
\theta = M^{-1}(m_1(\theta), ..., m_d(\theta))
$$
Definition: Moments estimator of $\theta$:
$$
\hat{\theta}_n^{MM} = M^{-1}(\hat{m}_1, ..., \hat{m}_d)
$$
provided it exists.

> #### Exercise 62
>
> Let $(\mathbb {R}, \{ N(\mu , \sigma ^2)\} _{\mu \in \mathbb {R}, \sigma > 0})$ be the statistical model of a normal random variable $X$. Let
> $$
> m_ k(\mu , \sigma ) = \mathbb {E}[X^ k]
> $$
> denote the $k$-th moment of $X$. Let $\psi : \mathbb {R} \times (0, \infty ) \to \mathbb {R}^2$ be defined by $\psi (\mu , \sigma ) = (m_1(\mu , \sigma ), m_2(\mu , \sigma ))$. (Since we have two parameters of interest, $\mu$ and $\sigma$, it makes sense to work with the first two moments. The hope is that the two moments will uniquely determine the parameters of interest $\mu$ and $\sigma$)
>
> Express $m_1(\mu,\sigma)$ and $m_2(\mu, \sigma)$ in terms of $\mu$ and $\sigma$.
>
> **Solution:**
>
> Note that
> $$
> \begin{aligned}
> m_1(\mu , \sigma ) &= \mathbb{E}[X] = \mu\\
> m_2(\mu, \sigma) &= \mathbb {E}[X^2] = (\mathbb {E}[X])^2 + \left(\mathbb {E}[X^2] - (\mathbb {E}[X])^2 \right) = \mu ^2 + \sigma ^2.
> \end{aligned}
> $$
> Hence,$\psi (\mu , \sigma ) = (\mu , \mu ^2 + \sigma ^2)$.

> #### Exercise 63
>
> Let 
> $$
> \begin{aligned}
> \psi : \mathbb {R} \times (0, \infty ) &\rightarrow \R^2\\
> (\mu , \sigma ) &\mapsto (m_1(\mu , \sigma ), m_2(\mu , \sigma )).
> \end{aligned}
> $$
> denote the moments map considered in the previous problem, where $m_k(\mu, \sigma)$ denotes the $k$-th moment of the distribution $\mathcal{N}(\mu,\sigma^2)$.
>
> 1. Is $\psi$ one-to-one on the domain $\R \times (0,\infty)$? (Equivalently, given the outputs $m_1$ and $m_2$, can we use them to uniquely reconstruct $\mu \in \R$ and $\sigma > 0$?)
> 2. If $\psi$ is one-to-one on the given domain and $\psi (\mu , \sigma ) = (m_1, m_2)$, what is $\mu$ and $\sigma$ expressed in terms of $m_1$ and $m_2$? 
>
> **Solution:**
>
> 1. From previous exercise we know $\psi (\mu , \sigma ) = (\mu , \mu ^2 + \sigma ^2)$. Hence, this function is one-to-one on the domain $\R \times (0,\infty)$. 
>
> 2. Since $m_1(\mu, \sigma) = \mu$, we can reconstruct the first parameter directly from the first moment: $\mu = m_1$.
>
>    Next since we know $m_2(\mu , \sigma ) = \sigma ^2 + \mu ^2$, we can back-solve for $\sigma$:
>    $$
>    \sigma = \sqrt{m_2 - \mu ^2} = \sqrt{m_2 - m_1^2}.
>    $$
>
> **Remark:** Assume $m_1$ and $m_2$ are one of the outputs of $\psi$, we have essentially shown how to construct $\psi ^{-1}(m_1, m_2)$.

> #### Exercise 64
>
> Let $(E, \{ \mathbf{P}_{\theta }\} _{\theta \in \Theta })$ denote a statistical model associated to a statistical experiment $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\theta ^*}$ where $\theta^* \in \Theta$ is the true parameter. Assume that $\Theta \subset \R^d$ for some $d \geq 1$. Let $m_k(\theta):=\mathbb{E}[X^k]$ where $X \sim \mathbf{P}_\theta$. $m_k(\theta)$ Is referred to as the $k$-th moment of $\mathbf{P}_\theta$. Also define the moments map:
> $$
> \begin{aligned}
> \psi : \Theta &\rightarrow \R^d\\
> \theta &\mapsto (m_1(\theta ), m_2(\theta ), \ldots , m_ d(\theta )).
> \end{aligned}
> $$
> Assume that $\psi$ is one-to-one (and hence, invertible).
>
> 1. What is $\theta^*$?
> 2. What is the method of moments estimator for $\theta^*$?
>
> **Solution:**
>
> 1. Observe that $\psi (\theta ^*) = (m_1(\theta ^*), m_2(\theta ^*), \ldots , m_ d(\theta ^*))$ by definition of $\psi$. Since $\psi$ is invertible, then we know that $\psi ^{-1}(m_1(\theta ^*), m_2(\theta ^*), \ldots , m_ d(\theta ^*)) =\theta ^*$. Hence, 
>    $$
>    \theta^* = \psi ^{-1}(m_1(\theta ^*), m_2(\theta ^*), \ldots , m_ d(\theta ^*)
>    $$
>
> 2. The method of moments estimator is given by
>    $$
>    \widehat{\theta }_ n^{\text {MM}} = \psi ^{-1}\left( \frac{1}{n} \sum _{i = 1}^ n X_ i, \frac{1}{n} \sum _{i = 1}^ n X_ i^2, \ldots , \frac{1}{n} \sum _{i = 1}^ n X_ i^ d \right),
>    $$

> #### Exercise 65
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } N(\mu ^*, (\sigma ^*)^2)$ and consider the associated statistical model $(\mathbb {R}, \{ N(\mu , \sigma ^2)\} _{\mu \in \mathbb {R}, \sigma > 0})$. Let
> $$
> \begin{aligned}
> \psi : \mathbb {R} \times (0,\infty) &\rightarrow \R^2\\
> (\mu , \sigma ) &\mapsto (m_1(\mu , \sigma ), m_2(\mu , \sigma )).
> \end{aligned}
> $$
> denote the moments map considered in the previous problem, where $m_k(\mu, \sigma)$ denotes the $k$-th moment of the distribution $\mathcal{N}(\mu, \sigma^2)$.
>
> Suppose we observe the dataset $X_1 = 0.5 , X_2 = 1.8 , X_3 = -2.3, X_4 = 0.9$.
>
> 1. What is the method of moments estimator $\widehat{\mu }^{\text {MM}}$ for $\mu^*$ evaluated on this dataset?
> 2. What is the method of moments $\widehat{\sigma }^{\text {MM}}$ estimator for $\sigma^*$ evaluated on this dataset?
>
> **Solution:**
>
> Since we computed $\psi^{-1}$ explicitly in the previous problem, we can apply the method of moments to estimate the true parameters $\mu^*$ and $\sigma^*$. Let
> $$
> \widehat{m}_1 = \frac{1}{n} \sum _{i = 1}^ n X_ i, \quad \widehat{m}_2 = \frac{1}{n} \sum _{i = 1}^ n X_ i^2
> $$
> denote the first and second sample moments, respectively. Then the **method of moments estimator** is defined to be
> $$
> (\widehat{\mu }_ n^{\text {MM}}, \widehat{\sigma }_ n^{\text {MM}}) := \psi ^{-1}(\widehat{m}_1, \widehat{m}_2) = (\widehat{m}_1, \sqrt{\widehat{m}_2 - \widehat{m}_1^2} ).
> $$
> Using a calculator to compute
> $$
> \widehat{m}_1(0.5, 1.8, -2.3, 0.9) = \frac{0.5 + 1.8 -2.3 + 0.9}{4} \approx 0.225
> $$
> and
> $$
> \widehat{m}_2(0.5, 1.8, -2.3, 0.9) = \frac{(0.5)^2 + (1.8)^2 + (-2.3)^2 + (0.9)^2}{4} \approx 2.3975.
> $$
> Applying the method of moments
> $$
> \widehat{\mu }_ n^{\text {MM}}(0.5, 1.8, -2.3, 0.9)= \widehat{m}_1(0.5, 1.8, -2.3, 0.9) \approx 0.225.
> $$
> and
> $$
> \widehat{\sigma }_ n^{\text {MM}}(0.5, 1.8, -2.3, 0.9) = \sqrt{\widehat{m_2} - (\widehat{m_1})^2} \approx \sqrt{2.3975 - (0.225)^2} \approx 1.532.
> $$

## 5. Generalized Method of Moments Estimator

#### Statistical analysis:

* Recall $M(\theta) = (m_1(\theta), ..., m_d(\theta))$;

* Let $\hat{M} = (\hat{m}_1, ...,\hat{m}_d)$.

* Let $\Sigma(\theta) = \mathsf{Cov}_\theta(X_1, X_1^2, ...,X_1^d)$ be the covariance matrix of the random vector $(X_1, X_1^2, ..., X_1^d)$, which we assume to exist.

  * Recall CLT
    $$
    \sqrt{n} \left( \overline{X_n^k} - m_k(\theta)\right) \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}(0,\mathsf{Var}(X_1^k))
    $$
    The multivariate CLT is
    $$
    \sqrt{n} \left(\begin{pmatrix} \overline{X_n^k}\\ \vdots \\\overline{X_n^k} \end{pmatrix} - M(\theta)^T \right) \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}(0,\mathsf{Cov}\begin{pmatrix} \overline{X_1^1}\\ \vdots \\\overline{X_1^d} \end{pmatrix})
    $$

* Assume $M^{-1}$ is continuously differentiable at $M(\theta)$.

#### Method of moments:

**Remark:** The method of moments can be extended to more general moments, even when $E \not \subset \R$.

* Let $g_1, ..., g_d: E \rightarrow \R$ be given functions, chosen by the practitioner.
* Previously, $g_k(x)=x^k, x \in E = \R$, for all $k=1,...,d$.
* Define $m_k(\theta) = \mathbb{E}_\theta [g_k(X)]$, for all $k = 1, ..., d$.
* Let $\Sigma(\theta) = \mathsf{Cov}_\theta(g_1(X_1), g_2(X_1), ...,g_d(X_1))$ be the covariance matrix of the random vector $g_1(X_1), g_2(X_1), ..., g_d(X_1)$, which we assume to exist.
* Assume $M$ is **one-to-one** and $M^{-1}$ is **continuously differentiable** at $M(\theta)$.

#### Generalized method of moments

$$
\sqrt{n} \left( \hat{m} - M(\theta) \right) \xrightarrow[n \rightarrow \infty]{ (d)} \mathcal{N}_d(0, \Sigma(\theta))
$$

Applying the **multivariate CLT** and **Delta method** yields:
$$
\sqrt{n} \left( M^{-1}(\hat{m}) -M^{-1}( M(\theta)) \right) \xrightarrow[n \rightarrow \infty]{ (d)} \mathcal{N}_d(0, \nabla (M^{-1})^T\ \Sigma(\theta)\ \nabla M^{-1})\\
\implies \sqrt{n}\left( \hat{\theta}^{MM}_n - \theta \right) \xrightarrow[n \rightarrow \infty]{ (d)} \mathcal{N}(0, \Gamma(\theta)) \quad \text{(w.r.t. } \mathbb{P}_\theta),\\
\text{where }\quad \Gamma(\theta) = \left[ { \partial M^{-1}\over \partial \theta }(M(\theta))\right]^T \Sigma(\theta) \left[ { \partial M^{-1}\over \partial \theta }(M(\theta))\right].
$$

## 6. Asymptotic Normality of the Method of Moments Estimator 

Let $(E, \{  \mathbf{P}_\theta \} _{\theta \in \Theta })$ denote a statistical model associated to a statistical experiment $ X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\theta ^*} $ for some unknown parameter $\theta^*$. Under some technical conditions, the method of moments estimator $\widehat{\theta }_ n^{\text {MM}}$ is **asymptotically normal**, which means that
$$
\sqrt{n}(\widehat{\theta }_ n^{\text {MM}} - \theta ^*) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0, \sigma ^2).
$$
The quantity $\sigma^2$ above is referred to as the **asymptotic variance**.

> #### Exercise 66
>
> Let $X_1, \ldots , X_ n \sim \text {Exp}(\lambda ^*)$ denote a statistical experiment where $\lambda^*$ is the true, unknown parameter. You construct the associated statistical model $((0, \infty ), \{ \text {Exp}(\lambda )\} _{\lambda \in (0,\infty )})$. Since the parameter $\lambda$ is one-dimensional, we only consider the first moment with moment map:
> $$
> \begin{aligned}
> \psi : \mathbb {R} &\rightarrow \R\\
> \lambda &\mapsto m_1(\lambda) := \mathbb{E}[X], \quad (X \sim \rm{Exp}(\lambda))
> \end{aligned}
> $$
>
> 1. [**Step 1: Moments Map for an Exponential Statistical Model**] What is $\psi(\lambda)$ and $\psi^{-1}(m_1)$? 
>
> 2. [**Step 2a: Deriving the Method of Moments Estimator**] What is the method of moments estimator $\widehat{\lambda }_ n^{\text {MM}}$ for $\lambda^*$?
>
> 3. [**Step 2b: Deriving the Method of Moments Estimator**] By the CLT, 
>    $$
>    \sqrt{n}\left( \widehat{m}_1(\lambda ^*) - \frac{1}{\lambda ^*}\right)= \sqrt{n}\left(\frac{1}{n}\sum _{i = 1}^ n X_ i - \frac{1}{\lambda ^*}\right)
>    $$
>    Converges to a normal random variable $\mathcal{N}(0,\sigma^2)$, where $\sigma^2$ can be written in terms of $\lambda^*$. What is $\sigma^2$?
>
> 4. [**Step 3: Computing the Asymptotic Variance of the Method of Moments Estimator**] Suppose that
>    $$
>    \sqrt{n}(\widehat{m}_1 - m_1(\theta )) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0, \sigma ^2).
>    $$
>    where $\widehat{m_1}$ and $m_1$ are first sample moment and first moment, respectively,
>
>     Recall that the **Delta method** states that if the above holds, then for any $g: \R \rightarrow \R$ that has a continuous first derivative,
>    $$
>    \sqrt{n}(g(\widehat{m}_1) - g(m_1(\theta ))) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0, g'(m_1(\theta ))^2 \sigma ^2)
>    $$
>    By the CLT for the method of moments estimator, $\widehat{\lambda }_ n^{\text {MM}}$ is asymptotically normal, meaning that 
>    $$
>    \sqrt{n}(\widehat{\lambda }_ n^{\text {MM}} - \lambda ^*) \stackrel{(d)}{\to } \mathcal{N}(0, \tau ^2)
>    $$
>    Applying the last problem and the delta method, what is the asymptotic variance $\tau^2$ in terms of $\lambda^*$?
>
> **Solution:** 
>
> 1. The first moment is
>    $$
>    \begin{aligned}
>    m_1(\lambda) & = \mathbb{E}[X]\\
>    &= \int _{0}^\infty \lambda x e^{-\lambda x} \,  dx\\
>    &= - x e^{-\lambda x} \bigg|_{0}^\infty - \int _0^\infty - e^{-\lambda x}\,  dx = 1/\lambda .
>    \end{aligned}
>    $$
>    Hence, $\psi(\lambda) = 1/\lambda$. Since $\psi$ is its own inverse, we also have $\psi ^{-1}(m_1) = 1/m_1$.
>
> 2. Since $\psi(\lambda) = 1/\lambda$,
>    $$
>    \widehat{\lambda }_ n^{\text {MM}} = \psi ^{-1}\left(\frac{1}{n} \sum _{i = 1}^ n X_ i\right) = \frac{n}{\sum _{i = 1}^ n X_ i}.
>    $$
>
> 3. By the CLT, $\sigma ^2 = \textsf{Var}(X)$.
>
>    The second moment is
>    $$
>    \begin{aligned}
>    \mathbb{E}[X^2] &=\int _0^\infty x^2 \lambda ^* e^{-\lambda ^* x} \,  dx\\
>    &= - x^2 e^{-\lambda ^* x} \bigg|_{0}^\infty - \int _{0}^\infty - 2 x e^{-\lambda ^* x} \,  dx\\
>    &= 2/(\lambda ^*)^2
>    \end{aligned}
>    $$
>    Since we showed in the solution of the last question that $\int _0^\infty \lambda ^* x e^{-\lambda ^* x} \,  dx = 1/\lambda ^*$. Thus,
>    $$
>    \textsf{Var}(X) = 2/(\lambda ^*)^2 - 1/(\lambda ^*)^2 = 1/(\lambda ^*)^2.
>    $$
>    Therefore, $\sigma ^2 = 1/(\lambda ^*)^2$.
>
> 4. From (3) we have
>    $$
>    \sqrt{n}( \frac{1}{n} \sum _{i = 1}^ n X_ i - 1/\lambda ^*) \stackrel{(d)}{\to } \mathcal{N}(0, 1/(\lambda ^*)^2).
>    $$
>    Letting $g = \psi^{-1}$ in the statement of the delta method, and noting that 
>    $$
>    (\psi ^{-1})'(m) = -1/m^2, \ m_1(\lambda) = 1/\lambda \\
>    \implies (\psi ^{-1})'(m_1(\lambda )) = (\psi ^{-1})'(1/\lambda) = -1/(1/\lambda)^2 =-\lambda ^2
>    $$
>    Therefore
>    $$
>    \tau^2 = (\psi ^{-1})'(m_1(\lambda ))^2 \sigma^2 = (-\lambda^2)^2\ 1/\lambda^2 = (\lambda^*)^2
>    $$
>    we see that 
>    $$
>    \sqrt{n}(\widehat{\lambda }_ n^{\text {MM}} - \lambda ^*) \stackrel{(d)}{\to } \mathcal{N}(0, (\lambda ^*)^2).
>    $$

## 7. MLE versus Method of Moments

* Comparison of the quadratic risks: In general, the MLE is more accurate.
  * MLE is asymptotically unbiased.
  * **Cramer-Rao lower bound** states that no unbiased estimator may have an (asymptotic) variance that is smaller than the inverse Fisher information.
* MLE still gives good results if model is misspecified.
  * This is not going to be the case in general for the method of moments (MM).
  * The expression of the moments map $\psi$ in terms of the parameter $\theta$ can be quite complicated, so it may be difficult to deduce how many moments (or *degrees of freedom*) are needed to uniquely recover the true distribution from moments. MM requires you to find $d$ so that the first $d$ moments uniquely determine the distribution of interest. To compute the MLE, this step is not necessary.
* Computational issues: Sometimes, the MLE is intractable but MM is easier (polynomial equations)
  * Optimizing the likelihood function can be very inefficient if the likelihood function is complicated and has several local maxima which require testing.

