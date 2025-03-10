# Lecture 14. Wald's Test, Likelihood Ratio Test, and Implicit Hypothesis Test

There are 8 topics and 5 exercises.

## 1. Worked Example: Two-Sample T-test with Small Sample Sizes

#### Non-asymptotic Two-Sample Test using t-statistic

Assume

* $\, X_1,\dots ,X_ n\stackrel{iid}{\sim }\mathcal{N}(\mu _ X,\sigma _ X^2),\,$
* $\, Y_1,\dots ,Y_ m\stackrel{iid}{\sim }\mathcal{N}(\mu _ Y,\sigma _ Y^2),\,$
* $X_1,\dots ,X_ n,Y_1,\dots ,Y_ m$ are independent.

Then, for any $n$ and $m$, the distribution of the test statistic below is approximated by a $t$-distribution:
$$
\frac{\overline{X}_ n-\overline{Y}_ m-(\mu _ X-\mu _ Y)}{\sqrt{\hat{\sigma _ X^2}/n+\hat{\sigma _ Y^2}/m}}
$$
where the degrees of freedom $N$​​ Is given by the **Welch-Satterthwaite formula**:
$$
\min (n,m)\, \leq \, {{ N\, =\, \frac{\big (\hat\sigma _ X^2/n + \hat\sigma _ Y^2/m\big )^2}{\frac{\hat\sigma _ X^4}{n^2(n-1)}+\frac{\hat\sigma _ Y^4}{m^2(m-1)}}}} \, \leq \, n+m
$$

#### Example

Given $n=20, m=12, \bar{X}_n=156.4, \bar{Y}_m=132.7,\ hat{\sigma}_d^2 = 5198.4, \hat{\sigma}_c^2 = 3867.0$​​, the test statistic is
$$
{156.4-132.7\over \sqrt{{5198.4\over20 } + {3867.0\over12 }}} = 0.982
$$
We fail to reject the null hypothesis since $0.982$​ is less than $q_{5\%}$​ of a standard Gaussian which is $1.645$.

Since the sample size is small, this may not be a valid test. So this number is suppose to be the realization of a t-distribution. 

* Using the shorthand formula $N = \min(n,m) = 12$​​​, we get $q_{5\%} = 1.78$​​​​ so we fail to reject the null hypothesis as $1.78 > 0.982$. The p-value is
  $$
  \text{p-value} = \mathbf{P}[t_{12}  >0.982] = 17.27\%
  $$
  Note that the t-distribution with $12$ degrees of freedom looks like a Gaussian but with heavier tails.

* Using the W-S formula
  $$
  N = { ({5198.4\over 20} + {3867.0\over 12})^2\over {5198.4^2\over 20^2(20-1)} + {3867.0^2\over 12^2(12- = 26.07)}} = 26.07
  $$
  We round to $26$.

  We get the p-value
  $$
  \text{p-value} = \mathbf{P}[t_{26} > 0.982] = 16.76\%
  $$
  Note that $16.76\%$ is smaller than $17.27\%$ since intuitively we are working with more data and so we have more evidence on rejecting the null hypothesis.

#### Recap: Advantages and Limitations of T-test

* Advantage of Student's test: Non asymptotic / Can be run on small samples.
* Drawback of Student's test: It relies on the assumption that the sample is Gaussian.

## 2. Interlude: Square roots of a positive semi-definite matrices

Recall that a matrix $\mathbf{A}$​ of size $d \times d$​ is **positive semi-definite** if $\, \mathbf{x}^ T\mathbf{A}\mathbf{x}\geq 0\,$​ for all $\, \mathbf{x}\in \mathbb {R}^ d.\, \,$​ Two example classes of positive semi-definite matrices are

* Diagonal matrices with non-negative entries: $\, \mathbf{D}=\begin{pmatrix}  c_1 & 0& \ldots & 0\\ 0& c_2& & 0\\ \vdots & & \ddots & \vdots \\ 0& & \ldots & c_ d\end{pmatrix}\,$ where $c_i \geq 0$ For all $i$.

* Matrix products $\, \mathbf{P}^ T\mathbf{D}\mathbf{P}\,$ where $\mathbf{P}$ is an **invertible** (square) matrix and $\mathbf{D}$​ is a **diagonal** matrix with non-negative entries. Proof:
  $$
  \, \mathbf{x}^ T(\mathbf{P}^ T\mathbf{D}\mathbf{P})\mathbf{x}=(\mathbf{P}\mathbf{x})^ T \mathbf{D}(\mathbf{P}\mathbf{x})=\mathbf{y}^ T\mathbf{D}\mathbf{y}\geq 0 \qquad \text{for all vectors }\mathbf{x}
  $$

The **positive semi-definite square root** (or simply the square root) of a positive semi-definite matrix $\mathbf{A}$ is another positive semi-definite matrix, denoted by $\mathbf{A}^{1/2}$, satisfying $\, \mathbf{A}^{1/2}\mathbf{A}^{1/2}=\mathbf{A}.\, \,$​ It is the case that for any positive semi-definite matrix (positive definite matrix, respectively), the positive semi-definite square root (positive definite square root, respectively) is unique.

> #### Exercise 81
>
> Let 
> $$
> \begin{aligned}
> \mathbf{A} =\mathbf{P}^ T\mathbf{D}\mathbf{P}\qquad \text {where } \mathbf{D} &= \begin{pmatrix} 3& 0\\ 0& 0\end{pmatrix}\\
> \mathbf{P} &= \frac{1}{\sqrt{2}}\begin{pmatrix} 1& -1\\ 1& 1\end{pmatrix}.
> \end{aligned}
> $$
> Note that $\, \mathbf{P}^ T=\mathbf{P}^{-1}.$
>
> Find the square root $\, \mathbf{A}^{1/2}\,$ of the matrix $\mathbf{A}$.
>
> Hint: $\mathbf{P}^ T \mathbf{B}^2 \mathbf{P}=\mathbf{P}^ T \mathbf{B}(\mathbf{P}\mathbf{P}^ T)\mathbf{B}\mathbf{P}$
>
> **Solution:**
> $$
> \begin{aligned}
> (\mathbf{P}^ T\mathbf{D}^{1/2}\mathbf{P})(\mathbf{P}^{T} \mathbf{D}^{1/2}\mathbf{P}) &= \mathbf{P}^ T\mathbf{D}^{1/2}(\mathbf{P}\mathbf{P}^{T})\mathbf{D}^{1/2}\mathbf{P}
> \\
> &=\mathbf{P}^ T\mathbf{D}^{1/2}(\mathbf{P}\mathbf{P}^{-1})\mathbf{D}^{1/2}\mathbf{P}\qquad \text {since } \mathbf{P}^ T=\mathbf{P}^{-1}\\
> &= \mathbf{P}^ T\mathbf{D}^{1/2}\mathbf{D}^{1/2}\mathbf{P}\\
> &= \mathbf{P}^ T\mathbf{D}\mathbf{P}
> \end{aligned}
> $$
> Hence, $\, \mathbf{A}^{1/2}\, =\, \mathbf{P}^ T\mathbf{D}^{1/2}\mathbf{P}.\, \,$ Plugging in the values of $\mathbf{D}$ and $\mathbf{P}$, we get
> $$
> \begin{aligned}
> \mathbf{A}^{1/2}\, =\, \mathbf{P}^ T\mathbf{D}^{1/2}\mathbf{P}
> &= \left(\frac{1}{\sqrt{2}}\begin{pmatrix} 1& 1\\ -1& 1\end{pmatrix} \right) \begin{pmatrix} \sqrt{3}& 0\\ 0& 0\end{pmatrix} \left(\frac{1}{\sqrt{2}}\begin{pmatrix} 1& -1\\ 1& 1\end{pmatrix}\right)
> &= \frac{1}{2}\begin{pmatrix} \sqrt{3}& 0\\ -\sqrt{3}& 0\end{pmatrix}\begin{pmatrix} 1& -1\\ 1& 1\end{pmatrix}\\
> &= \frac{\sqrt{3}}{2}\begin{pmatrix} 1& -1\\ -1& 1\end{pmatrix}
> \end{aligned}
> $$

## 3. Wald's Test

#### A test based on the MLE

Consider an i.i.d. sample $X_1, ..., X_n$​​​​ with statistical model $(E, (\mathbf{P}_\theta)_{\theta \in \Theta})$​​​​, where $\Theta \in \R^d(d \geq 1)$​​ and let $\theta_0 \in \Theta$​ be fixed and given.

Consider the following hypotheses:
$$
\begin{cases} 
H_0: & \theta = \theta_0\\
H_1: & \theta \neq \theta_0.
\end{cases}
$$
Let $\hat{\theta}^{MLE}$ be the MLE. Assume the MLE technical conditions are satisfied.

If $H_0$ is true, then
$$
\sqrt{n}\ \mathcal{I}(\theta_0)^{1/2} \times (\hat{\theta}_n^{MLE} - \theta_0) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}_d(0,I_d)\\
\sqrt{n}\ \mathcal{I}(\theta^*)^{1/2} \times (\hat{\theta}_n^{MLE} - \theta_0) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}_d(0,I_d)\\
\sqrt{n}\ \mathcal{I}(\theta^{MLE})^{1/2} \times (\hat{\theta}_n^{MLE} - \theta_0) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}_d(0,I_d)
$$
are all true.

> #### Exercise 82
>
> Suppose 
> $$
> \mathbf{M} = \begin{pmatrix} \cos \phi & -\sin \phi \\ \sin \phi & \cos \phi \end{pmatrix}.
> $$
>
> 1. Is it true that $\, \mathbf{M}^ T\mathbf{M}=\mathbf{I}_{2}$​​? (Here $\mathbf{I}_{2}=\begin{pmatrix} 1& 0\\ 0& 1\end{pmatrix}$​​ is the identity matrix in 2 dimensions).
> 2. Now, let $\, \mathbf{Z}\sim \mathcal{N}_2(\mathbf{0},\mathbf{I}_{2}),\,$ i.e. $\mathbf{Z}$ is a standard Gaussian in $2$ dimensions. Is it true that $\, \mathbf{M}\mathbf{Z}\, \sim \mathcal{N}_2(\vec{\mu },\Sigma _{\mathbf{M}\mathbf{Z}})$, for some $\vec{\mu },\Sigma _{\mathbf{M}\mathbf{Z}}$?
> 3. Find the mean $\, \vec{\mu }=\mathbb E[\mathbf{M}\mathbf{Z}]\,$​ and covariance matrix $\, \Sigma _{\mathbf{M}\mathbf{Z}}\,$​ of $\mathbf{MZ}$​. 
>
> **Answer:**
>
> 1. True.
> 2. True.
> 3. $\begin{pmatrix} 0\\ 0\end{pmatrix}$ and $\begin{pmatrix} 1& 0\\ 0& 1\end{pmatrix}$.
>
> **Solution:**
>
> 1. Since
>    $$
>    \begin{aligned}
>    \mathbf{MM}^T &= \begin{pmatrix} \cos \phi & -\sin \phi \\ \sin \phi & \cos \phi \end{pmatrix}\begin{pmatrix} \cos \phi & \sin \phi \\ -\sin \phi & \cos \phi \end{pmatrix}\\
>    &= \begin{pmatrix} \cos ^2\phi +\sin ^2\phi & \cos \phi \sin \phi -\cos \phi \sin \phi \\ \cos \phi \sin \phi -\cos \phi \sin \phi & \sin ^2\phi +\cos ^2\phi \end{pmatrix}\, \\
>    &=\, \begin{pmatrix} 1& 0\\ 0& 1\end{pmatrix}.
>    \end{aligned}
>    $$
>    Hence $\, \mathbf{M}^{T}\mathbf{M}=\mathbf{I}_{2}\,$ or equivalently $\, \mathbf{M}^ T=\mathbf{M}^{-1}\,$
>
>    **Remark:** Geometrically, $\mathbf{M}$ rotates a vector $\mathbf{z}$ by an angle $\phi$ counterclockwise. Hence $\left\|  \mathbf{M}\mathbf{z} \right\| =\left\|  \mathbf{z} \right\| \,$ for any nonzero $\mathbf{z}$.
>
> 2. Since a main property of (multivariate) Gaussian variables is that any linear transformation of them remain (multivariate) Gaussian.
>
> 3. Compute the mean and covariance of $\mathbf{MZ}$.
>    $$
>    \begin{aligned}
>    E[\mathbf{M}\mathbf{Z}] &= \mathbf{M0} = 0\\
>    \Sigma _{\mathbf{M}\mathbf{Z}} &= \mathbb{E}[(\mathbf{MZ})(\mathbf{MZ})^T]= \mathbb{E}[\mathbf{MZZ^T M^T}] = \mathbf{M} \cdot \mathbb{E}[\mathbf{ZZ^T}]\mathbf{M}^T\\
>    &=  \mathbf{M}\Sigma _{\mathbf{Z}}\mathbf{M}^ T\, =\, \mathbf{M}\mathbf{I}_{2} \mathbf{M}^ T\, =\, \mathbf{M}\mathbf{M}^{-1}\, =\, \mathbf{I}_{2}.
>          
>    \end{aligned}
>    $$
>    Hence, $\, \mathbf{M}\mathbf{Z}\, \sim \mathcal{N}_ d\left(\mathbf{0},\mathbf{I}_{2}\right),\,$​i.e. a **standard** Gaussian vector.
>
>    **Remark:** Real matrices satisfying $\, \mathbf{M}^{T}=\mathbf{M}^{-1}\,$​​ (Or equivalently $\mathbf{M}\mathbf{M}^ T=\mathbf{M}^ T\mathbf{M}=\mathbf{I}_{d}$​​) are called **orthogonal** matrices. In general, in $d$​ dimensions and for any orthogonal matrix $\mathbf{M}$​, $\mathbf{MZ}$ is also a **standard** multivariate Gaussian vector if $\mathbf{Z}$ is a standard multivariate Gaussian.

#### Review: Asymptotic Normality of the MLE

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\theta ^*}$​ for some true parameter $\theta ^* \in \mathbb {R}^ d$​. We construct the associated statistical model $(\mathbb {R}, \{  \mathbf{P}_\theta \} _{\theta \in \mathbb {R}^ d } )$​ and the MLE $\widehat{\theta }_ n^{MLE}$​ for $\theta^*$.

Recall that, under some technical conditions,
$$
\sqrt{n}(\widehat{\theta }_ n^{MLE} - \theta ^*) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0, \mathcal{I}(\theta ^*)^{-1})
$$
where $\mathcal{I}(\theta ^*)$​ denotes the Fisher information. That is, the MLE $\widehat{\theta }_ n^{MLE}$​ is asymptotically normal with asymptotic covariance matrix $\mathcal{I}(\theta ^*)^{-1}$​.

Standardize the statement of asymptotic normality above, we find that
$$
\sqrt{n}\,  \mathcal{I}(\theta ^*)^{1/2} (\widehat{\theta }_ n^{MLE} - \theta ^*) \xrightarrow [n \to \infty ]{(d)} \mathcal{I}(\theta ^*)^{1/2} \mathbf{N}(\mathbf{0}, \mathcal{I}(\theta ^*)^{-1}) = \mathbf{N}(0, \mathbf{I}_{d}).
$$
**Proof:**

By the result of *Exercise 82*, if $\mathbf{X}\sim \mathcal{N}(\mathbf{0}, \mathcal{I}(\theta ^*)^{-1})$​​, the $\mathcal{I}(\theta ^*)^{1/2} \mathbf{X}$​​ is mean $0$​​ and has covariance matrix
$$
\mathcal{I}(\theta ^*)^{1/2} \mathcal{I}(\theta ^*)^{-1} \left(\mathcal{I}(\theta ^*)^{1/2}\right)^ T = \mathcal{I}(\theta ^*)^{1/2} \mathcal{I}(\theta ^*)^{-1} \mathcal{I}(\theta ^*)^{1/2} = \mathbf{I}_{d}.
$$
Indeed, $\mathcal{I}(\theta ^*)^{1/2} \mathbf{X}\sim \mathcal{N}(\mathbf{0}, \mathbf{I}_{d})$.

By the asymptotic normality of the MLE,
$$
\sqrt{n}(\widehat{\theta }_ n^{MLE} - \theta ^*) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(\mathbf{0}, \mathcal{I}(\theta ^*)^{-1})
$$
So that by continuity,
$$
\sqrt{n}\,  \mathcal{I}(\theta ^*)^{1/2} (\widehat{\theta }_ n^{MLE} - \theta ^*) \xrightarrow [n \to \infty ]{(d)} \mathcal{I}(\theta ^*)^{1/2} \mathcal{N}(\mathbf{0}, \mathcal{I}(\theta ^*)^{-1}) = \mathcal{N}(0, \mathbf{I}_{d}).
$$

#### Review: Chi-Squared Distribution

The $\chi^2$​ distribution with $d$​ degrees of freedom is by definition the distribution of
$$
Z_1^2+Z_2^2\ldots +Z_ d^2\qquad \text {where}\, Z_ i\stackrel{iid}{\sim }\mathcal{N}(0,1)
$$
or equivalently the distribution of
$$
\left\|  \mathbf{Z} \right\| ^2 \qquad \text {where }\, \mathbf{Z}\sim \mathcal{N}_ d(\mathbf{0},\mathbf{I}1),
$$
whose components are independent because the off-diagonal elements of the covariance matrix $\mathbf{1}$​ are all $0$.

**Remark:** The vector $\mathbf{MZ}$​​​​, where $\, \mathbf{M}^{T}=\mathbf{M}^{-1}\,$​​​​ (or equivalently $\, \mathbf{M}\mathbf{M}^ T=\mathbf{M}^ T\mathbf{M}=\mathbf{1}_{d\times d},\,$​​​​) is also a **standard multivariate Gaussian vector**. Hence, $||\mathbf{MZ}||^2$​​​ also follows a $\chi^2_d$ distribution.

#### Review: Norm Squared

Given a squared norm $\, \left\|  \mathbf{A}\mathbf{x} \right\| ^2\,$​​​​​​ of the vector $\mathbf{Ax}$​​​​​, where $\mathbf{A}$​​​ is a symmetric $d\times d$​ matrix and $\mathbf{x}$ is a vector in $\R^d$, we have
$$
\begin{aligned}
\left\|  \mathbf{A}\mathbf{x} \right\| ^2 &= (\mathbf{A}\mathbf{x})^ T(\mathbf{A}\mathbf{x})\, =\, \mathbf{x}^ T\mathbf{A}^ T\mathbf{A}\mathbf{x}\\
&=\mathbf{x}^ T\mathbf{A}^ T\mathbf{A}\mathbf{x}\qquad (\text {since } \mathbf{A}^ T=\mathbf{A})\, =\, \mathbf{x}^ T\mathbf{A}^2\mathbf{x}
\end{aligned}
$$

#### Wald's test

Hence, 
$$
T_n = n\left(\hat{\theta}_n^{MLE} - \theta_0\right)^T \mathcal{I}(\hat{\theta}^{MLE}) \left(\hat{\theta}_n^{MLE} - \theta_0\right) \xrightarrow[n \rightarrow \infty]{(d)}\chi_d^2
$$
Wald's test with asymptotic level $\alpha \in (0,1)$:
$$
\psi = \mathbb{1}\{T_n > q_\alpha\}
$$
where $q_\alpha$​ is the $(1-\alpha)$​-quantile of $\chi_d^2$​.

**Proof:**

Knowing that
$$
\sqrt{n}\,  \mathcal{I}(\hat{\theta})^{1/2} (\widehat{\theta }_ n - \theta_0) \xrightarrow [n \to \infty ]{(d)} = \mathcal{N}(0, \mathbf{I}_{d\times d}).
$$
Let $\mathbf{V} = \mathcal{I}(\hat{\theta})^{1/2}(\hat{\theta} - \theta_0)$​​, which is a standard Gaussian random variable. 

By definition of the $\chi^2$ distribution with $d$ degrees of freedom.  $||V||^2= V^T V$ is $\chi^2_d$​​​ distributed. Thus by continuity, we have
$$
||V||^2= V^TV = (\mathcal{I}(\theta_0)^{1/2}(\hat{\theta} - \theta_0))^T(\mathcal{I}(\theta_0)^{1/2}(\hat{\theta} - \theta_0)) = (\hat{\theta} - \theta_0)\mathcal{I}(\theta_0) (\hat{\theta}- \theta_0)
$$
is $\chi^2_d$​ distributed.

Equivalently,
$$
\left\|  \sqrt{n} \mathcal{I}({\theta_0})^{1/2} (\widehat{\theta }_ n^{MLE} - \theta_0) \right\| _2^2 \xrightarrow [n \to \infty ]{(d)} \chi _ d^2.
$$
**Remark:** Wald's test is also valid if $H_1$​​​ has the form "$\theta > \theta_0$​​​" or "$\theta < \theta_0$​​​" or "$\theta = \theta_0$​​​"...

> #### Exercise 83
>
> Let $\, X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\theta ^*}$ for some true parameter $\theta ^* \in \mathbb {R}^ d$. We construct the associated statistical model $(\mathbb {R}, \{  \mathbf{P}_\theta \} _{\theta \in \mathbb {R}^ d } )$ and the maximum likelihood estimator $\hat{\theta}^{MLE}_n$ for $\theta^*$.
>
> We have hypotheses:
> $$
> H_0: \theta^* = 0\\
> H_1: \theta^* \neq 0
> $$
> Assuming that the null hypothesis is true, the asymptotic normality of the MLE $\widehat{\theta }_ n^{MLE}\,$ implies that the following random variable
> $$
> \left\|  \sqrt{n}\, \mathcal{I}(\mathbf{0})^{1/2}(\widehat{\theta }_ n^{MLE}- \mathbf{0})  \right\| ^2
> $$
> converges to a $\chi^2_k$ distribution.
>
> Derive the Wald's Test. 
>
> **Solution:**
>
> Under the assumption $X_1, \ldots , X_ n \stackrel{iid}{\sim } P_{\mathbf{0}}$,
> $$
> \sqrt{n} \mathcal{I}(\mathbf{0})^{1/2} (\widehat{\theta }_ n^{MLE} - \mathbf{0}) \xrightarrow [n \to \infty ]{(d)} = \mathcal{N}(\mathbf{0}, I_{d \times d}).
> $$
> Next, by definition of the $\chi^2$​​​​​ distribution and  by continuity, we have
> $$
> \left\|  \sqrt{n} \mathcal{I}(\mathbf{0})^{1/2} (\widehat{\theta }_ n^{MLE} - \mathbf{0}) \right\| _2^2 \xrightarrow [n \to \infty ]{(d)} \chi _ d^2.
> $$
> To derive the Wald's test for the given hypotheses, we define the **test statistic** $W_n$
> $$
> W_ n := \left\|   \sqrt{n}\mathcal{I}(\mathbf{0})^{1/2}(\widehat{\theta }_ n^{MLE}- \mathbf{0})  \right\| ^2 = n (\widehat{\theta }_ n^{MLE}- \mathbf{0})^ T \mathcal{I}(\mathbf{0}) (\widehat{\theta }_ n^{MLE}- \mathbf{0}).
> $$
> Then, Wald's test of level $\alpha$ is the test
> $$
> \psi _\alpha = \mathbf{1}(W_ n > q_\alpha (\chi ^2_ d)),
> $$
> where $\, q_\alpha (\chi ^2_ d)\,$​is the $1-\alpha$-quantile of the (pivotal) distribution $\chi^2_d$. 

#### Comparing quantiles

Let $\, Z\sim \mathcal{N}(0,1).\, \,$Then $\, Z^2\sim \chi ^2_1$.

The quantile $\, q_{\alpha }(\chi ^2_1)$ of the $\chi_1^2$-distribution is then umber such that
$$
\mathbf{P}\left(Z^2>q_{\alpha }(\chi ^2_1)\right)=\alpha .
$$
The quantiles of the $\chi_1^2$​​​ distribution in terms of the quantiles of the normal distribution is $q_{\alpha/2}^2$.

**Proof:** 

Since $Z^2 > q$​ for​ any $q > 0$​ if and only if $|Z| > \sqrt q$​, we have
$$
P(Z^2> q_{\alpha }(\chi ^2_1))\, =\, P(\left| Z \right|> \sqrt{q_{\alpha }(\chi ^2_1)})\, =\, \alpha .
$$
Since $\, Z\sim \mathcal{N}(0,1),\, P(\left| Z \right|> \sqrt{q_{\alpha }(\chi ^2_1)})\, =\, \alpha \,$​if and only if
$$
\sqrt{q_{\alpha }(\chi ^2_1)}=q_{\alpha /2}(\mathcal{N}(0,1))
$$
Hence $\, q_{\alpha }(\chi ^2_1)=q_{\alpha /2}(\mathcal{N}(0,1))^2$.

For example, for $\alpha = 5\%$, using a table or software, we have
$$
q_{0.05}(\chi ^2_1) \approx 3.84\\
q_{0.025}(\mathcal{N}(0,1))^2 \approx (1.96)^2  \approx 3.84
$$

## 4. Wald's Test in 1 dimension

**In 1 dimension, Wald's Test coincides with the two-sided test based on on the asymptotic normality of the MLE.**

Given the hypotheses
$$
H_0: \theta^* = \theta_0\\
H_1: \theta^* \neq \theta_0\\
$$
a two-sided test of level $\alpha$, based on the asymptotic normality of the MLE, is
$$
\psi _\alpha =\mathbf{1}\left(\sqrt{nI(\theta _0)} \left| \widehat{\theta }^{\text {MLE}} -\theta _0 \right|>q_{\alpha /2}(\mathcal{N}(0,1))\right)
$$
where the Fisher information $\, I(\theta _0)^{-1}\,$​ is the asymptotic variance $\hat{\theta}^{MLE}$​ under the null hypothesis. 

On the other hand, a Wald's test of level $\alpha$ is
$$
\begin{aligned}
\psi_\alpha^{Wald} &= \mathbf{1}\left(nI(\theta _0) \left(\widehat{\theta }^{\text {MLE}} -\theta _0\right)^2\, >\, q_{\alpha }(\chi ^2_1)\right)\\
&= \mathbf{1}\left(\sqrt{nI(\theta _0)} \, \left| \widehat{\theta }^{\text {MLE}} -\theta _0 \right|\, >\, \sqrt{q_{\alpha }(\chi ^2_1)}\right).
\end{aligned}
$$
Using the result from the problem above, we see that the two-sided test of level $\alpha$​​ is the same as Wald's test at level $\alpha$.

## 5. Review: Power of a test for different alternative hypotheses

Recall that the **power** $\pi_\psi$ of a test $\psi$​ for the hypotheses
$$
H_0: \theta^* \in \Theta_0\\
H_1: \theta^* \in \Theta_1
$$
is defined to be
$$
\pi_\psi = \inf_{\theta\in\theta_1} (1- \beta_\psi(\theta))
$$
where $\beta_\psi(\theta) = \mathbf{P}_\theta(\psi = 0)$, defined for $\theta \in \Theta_1$, is the **type 2 error rate** of test $\psi$.

Suppose $X_1, ..., X_n$ are i.i.d. random variable (in 1 dimension). Assume the theorem of MLE applies so that $\hat{\theta }^{\text {MLE}}$ is asymptotically normal. You use the test
$$
\psi =\mathbf{1}\left(\sqrt{nI}\, \left| \hat{\theta }^{\text {MLE}}-0 \right|>C_\alpha \right),
$$
which has level $\alpha$​ for some threshold $C_\alpha$​ to test the hypotheses
$$
H_0: \theta^* = 0\\
H_1: \theta^* \neq 0
$$
As
$$
\begin{aligned}
\pi_\psi &= \inf _{\theta \neq 0} \left(1-\beta _\psi (\theta )\right)\\
&=\inf _{\theta \neq 0} \mathbf{P}_\theta (\psi =1)\, =\, \inf _{\theta \neq 0} \mathbf{P}_\theta \left(\sqrt{nI}\, \left| \hat{\theta }^{\text {MLE}}-0 \right|>C_\alpha \right)
\end{aligned}
$$
$\, \sqrt{nI}\, \left(\hat{\theta }^{\text {MLE}}-\theta \right)\sim \mathcal{N}(0,1)\,$ (Asymptotically if $\theta^* = \theta$), $\, \mathbf{P}_\theta \left(\sqrt{nI}\, \left| \hat{\theta }^{\text {MLE}}-0 \right|>C_\alpha \right)\,$ decrease as $\theta \rightarrow 0$ and approaches $\, \mathbf{P}_0\left(\sqrt{nI}\, \left| \hat{\theta }^{\text {MLE}}-0 \right|>C_\alpha \right)\, =\alpha \,$​. 

Hence, the asymptotic power $\pi_\psi$​​ with $H_1: \theta^* \neq0$​​ is $\alpha$​​. 

If we use the same test $\, \psi =\mathbf{1}\left(\sqrt{nI}\, \left| \hat{\theta }^{\text {MLE}}-0 \right|>C_\alpha \right)\,$​​ to test a different alternative hypothesis against the same null hypothesis:
$$
H_0: \theta^* = 0\\
H_1: \theta^* = 1
$$
then
$$
\pi_\psi = \mathbf{P}_{\theta =1}\left(\sqrt{nI}\, \left| \hat{\theta }^{\text {MLE}}-0 \right|>C_\alpha \right)
$$
which is greater than $\, \mathbf{P}_{\theta =0}\left(\sqrt{nI}\, \left| \hat{\theta }^{\text {MLE}}-0 \right|>C_\alpha \right)=\alpha .\,$ 

The (smallest) asymptotic level of $\psi$​ stays the same (since the alternative hypothesis has no effect on the level of the test once the test has been fixed), and the asymptotic power of $\psi$​ increases.

## 6. Performing Wald's Test on a Gaussian Data Set

Suppose $X_1, \ldots , X_ n \stackrel{iid}{\sim } N(\mu , \sigma ^2)$. Your goal is to hypothesis test between
$$
H_0: (\mu, \sigma^2) = (0,1)\\
H_1: (\mu, \sigma^2) \neq (0,1)
$$
Recall Wald's test from a previous problem, which, under the above hypothesis, takes the form
$$
\psi _\alpha := \mathbf{1}\left(W_ n > q_\alpha (\chi _2^2) \right) = \mathbf{1}\left( n \left(\widehat{\theta }_ n^ T-\begin{pmatrix} 0& 1\end{pmatrix}\right)\mathcal{I}((0,1))\left(\widehat{\theta }_ n- \begin{pmatrix} 0\\ 1\end{pmatrix}\right) > q_\alpha (\chi _2^2) \right)
$$
where $q_\alpha(\chi_2^2)$​​ is the (1-$\alpha$​)-quantile of $\chi_2^2$. You are given that the technical conditions required for the MLE to be asymptotically normal are satisfied for a Gaussian statistical model with unknown mean and variance.

Tthe smallest value of $q_\alpha(\chi_2^2 )$​​ so that $\psi_\alpha$​ is a test with asymptotic level $5\%$​ : $q_\alpha(\chi_2^2 ) \geq 5.991$​. 

Since we have assumed that the MLE is asymptotically normal, we have
$$
W_ n \xrightarrow [n \to \infty ]{(d)} \chi _2^2.
$$
There are precisely two degrees of freedom since we have two unknowns. The test $\psi_\alpha$​​​​​ has asymptotic level $5\%$​​​ if $\alpha = 5\%$​​​. Consulting a table, we see that the $0.05$​-quantile for $\chi_2^2$ is $q_\alpha = 5.991$.

Suppose you observe the data set
$$
0.2, -0.1, -1.9, -0.4, -1.8
$$
Recall that the MLE of a Gaussian $\mathcal{N}(\mu,\sigma^2)$ is given by 
$$
\begin{pmatrix} \widehat{\mu }_ n^{MLE}\\ (\widehat{\sigma ^2})_ n^{MLE}\end{pmatrix} = \begin{pmatrix}  \overline{X}_ n\\ \frac{1}{n} \sum _{i = 1}^ n ( X_ i - \overline{X}_ n )^2 \end{pmatrix}
$$
and the Fisher information is given by
$$
\mathcal{I}(\mu , \sigma ^2) = \begin{pmatrix}  \frac{1}{\sigma ^2} &  0 \\ 0 &  \frac{1}{2 \sigma ^4} \end{pmatrix}.
$$
To compute the test statistic $W_5$​​​ for the given data set, we first compute 
$$
\begin{pmatrix} \widehat{\mu }_ n^{MLE}\\ (\widehat{\sigma ^2})_ n^{MLE}\end{pmatrix} = \begin{pmatrix}  \overline{X}_ n\\ \frac{1}{n} \sum _{i = 1}^ n ( X_ i - \overline{X}_ n )^2 \end{pmatrix} = \begin{pmatrix} -0.8\\ 0.772\end{pmatrix} 
$$
The Fisher information, under the null hypothesis $(\mu, \sigma^2) = (0,1)$​, is
$$
\begin{pmatrix}  1 &  0 \\ 0 &  \frac{1}{2} \end{pmatrix}.
$$
Therefore,
$$
W_5 = 5 \cdot ( (-0.8, 0.772 ) - (0,1)) \begin{pmatrix}  1 &  0 \\ 0 &  \frac{1}{2} \end{pmatrix} \left( \begin{pmatrix} -0.8\\ 0.772\end{pmatrix} - \begin{pmatrix} 0\\ 1\end{pmatrix}\right)^ T \approx 3.33.
$$
Since $q_{0.05}=5.991 > 3.33$, we would fail to reject the null hypothesis for the given sample.​

## 7. Likelihood Ratio Test

#### Basic Form

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\theta ^*}$​​, and consider the associated statistical model $(E, \{  \mathbf{P}_{\theta } \} _{\theta \in \mathbb {R}^ d} )$​​. Suppose that $\mathbf{P}_\theta$​​ is a discrete probability distribution with PMF given by $p_\theta$​.

In its most basic form, the likelihood ratio test can be used to decide between two hypotheses of the following form:
$$
H_0: \theta^* = \theta_0\\
H_1: \theta^* = \theta_1
$$
Recall the likelihood function
$$
L_n: \R^n \times \R^d \rightarrow \R\\
(x_1, ..., x_n; \theta) \mapsto \prod _{i =1}^ n p_\theta (x_ i).
$$
The **likelihood ratio test** in this set-up is of the form
$$
\psi _ C = \mathbf{1}\left( \frac{L_ n(x_1, \ldots , x_ n; \theta _1 )}{L_ n(x_1, \ldots , x_ n; \theta _0 )} > C \right).
$$
where $C$ is a threshold to be specified.

> #### Exercise 84
>
> In this problem, you have an unfair coin. It comes up heads with probability either $25\%$​ or $75\%$​, but you don't know which is true. You design a test to decide between the two possibilities. First, you model the results of $n$​ coin flips as $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Ber}(p^*)$​ where Heads is $+1$​ and Tails is $0$​. The associated model is $(\{ 0,1 \} , \{ \text {Ber}(p)\} _{p \in (0,1)})$​.
>
> You formulate the hypotheses
> $$
> H_0: p^* = 0.25\\
> H_1: p^* = 0.75.
> $$
> You decide to use the likelihood-ratio test described above with threshold $C=1$. Suppose you observe a single coin-flip: $X_1 = 1$.
>
> 1. Should you reject or fail to reject the null hypothesis?
>
> 2. Now suppose you observe the data set
>    $$
>    X = \{1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0\}
>    $$
>    Using the specified likelihood ratio test, would you reject or fail to reject the null hypothesis?
>
> **Answer:**
>
> 1. Reject.
> 2. Fail to reject.
>
> **Solution:**
>
> 1. If we observe $X_1 = 1$, then
>    $$
>    L_1( 1; 0.25) = 0.25, \quad L_1(1; 0.75) = 0.75.
>    $$
>    Hence,
>    $$
>    \frac{L_1(1; 0.75)}{L_1( 1; 0.25)} > 1,
>    $$
>    and we would reject the null hypothesis.
>
> 2. Now consider the given data set, which consists of $6$​​​​ heads, $10$​​​ tails, and $16$​​ total coin flips. Intuitively, since there are more tails than heads, it seems more likely that the parameter $p^*$​​ is closer to $0$​​ than $1$​. And indeed, the likelihood ratio test we designed confirms this heuristic​
>    $$
>    L_{16}( \mathbf{X}; 0.25) = \left( \frac{1}{4} \right)^{6} \left( \frac{3}{4} \right)^{10} , \quad L_{16}( \mathbf{X}; 0.75) = \left( \frac{3}{4} \right)^{6} \left( \frac{1}{4} \right)^{10}.
>    $$
>    Since $L_{16}( \mathbf{X}; 0.25) > L_{16}( \mathbf{X}; 0.75)$​, we see that $\psi = 0$. For this data set, we fail to reject the null hypothesis.

#### A test based on the log-likelihood

Consider an i.i.d. sample $X_1, ..., X_n$​​ with statistical model $(E, (\mathbf{P}_\theta )_{\theta \in \Theta})$​​, where $\Theta \subseteq \R^d (d\geq 1)$​.

Suppose the null hypothesis has the form
$$
H_0: (\theta_{r+1}, ..., \theta_{d}) = (\theta_{r+1}^{(0)}, ..., \theta_{d}^{(0)})
$$
for some fixed and given numbers $\theta_{r+1}^{(0)}, ..., \theta_{d}^{(0)}$​.

Let
$$
\hat{\theta}_n = \text{argmax}_{\theta \in \Theta} \ \  \ell_n(\theta) \quad \text{(MLE)}
$$
and
$$
\hat{\theta}_n^c = \text{argmax}_{\theta \in \Theta_0} \ \ell_n(\theta) \quad \text{("constrained MLE")}
$$
where $\Theta_0 = \{\theta \in \Theta: (\theta_{n+1}, ..., \theta_d) =  (\theta^{(0)}_{n+1}, ..., \theta^{(0)}_{d})\}$​.

#### Likelihood ratio test

**Test statistic:**
$$
T_n = 2\left(\ell_n (\hat{\theta}_n)-\ell_n (\hat{\theta}_n^c)\right).
$$

*  $\ell_n (\hat{\theta}_n)$​ is the completely unconstrained MLE and is defined by the optimization problem
  $$
  \widehat{\theta _ n^{MLE}} = \text {argmax}_{\theta \in \Theta } \ell _ n(X_1, \ldots , X_ n; \theta )
  $$
   In particular, we find the maximizer over the entire parameter space $\Theta$. 

* $\ell_n (\hat{\theta}_n^c)$​ is the **constrained MLE** and is defined to be
  $$
  \widehat{\theta _ n^{c}} = \text {argmax}_{\theta \in \Theta _0} \ell _ n(X_1, \ldots , X_ n ; \theta ).
  $$

* The difference is non-negative, that is
  $$
  \ell_n (\hat{\theta}_n) \geq \ell_n (\hat{\theta}_n^c)
  $$

* **Remark:** The likelihood ratio test is a natural test in a situation where we only care about some (e.g. the last $d-r$ coordinates) of the unknowns involved in the parameter $\theta^* \in \R^d$.

**Wilk's Theorem:**

Assume $H_0$​​ is true and the MLE technical conditions are satisfied.

Then, 
$$
T_n \xrightarrow[n \rightarrow \infty]{(d)} \chi^2_{d-r}
$$

* Note that first $r$​​​​​ coordinates are not fixed. While the parameter space corresponding to $H_0$​ is $\Theta_0 = \R^r$ which, intuitively, has $r$ free variables, the test statistic $T_n$ converges to a $\chi^2$ distribution with $d-r$ degrees of freedom. 
* $T_n$​​ is a pivotal statistic; i.e., it converges to a pivotal distribution, since the distribution $\chi_{d-r}^2$​​ does not depend on the specific value of the true parameter $\theta^*$​​.

Likelihood ratio test with asymptotic level $\alpha \in (0,1)$:
$$
\psi = \mathbb{1}\{T_n > q_\alpha\},
$$
where $q_\alpha$​ is the $(1-\alpha)$​-quantile of $\chi^2_{d-r}$​.

## 8. Testing Implicit Hypotheses

Let $X_1, .., X_n$​ be i.i.d. random variables and let $\theta \in \R^d$​ be an **unknown** parameter associated with the distribution of $X_1$​ (e.g. a moment, the parameter of a statistical model, etc...)

Let $g : \R^d \rightarrow \R^k$​​ be **continuously differentiable** (with $k < d$​​).

Consider the following hypotheses:
$$
\begin{cases}H_0 : g(\theta) = 0\\ H_1 : g(\theta) \neq 0\end{cases}
$$
E.g. $g(\theta) = g(\theta_1, \theta_2)\ (k=2), \text{or } \ g(\theta) = \theta_1 - \theta_2  (k=1), \ \text{or } ...$

#### Delta Method

Suppose an **asymptotic normal estimator** $\hat{\theta}_n$​ is available:
$$
\sqrt{n} \left( \hat{\theta}_n - \theta \right) \xrightarrow[n\rightarrow \infty]{ (d)} \mathcal{N}_d(0, \Sigma(\theta)), \quad \Sigma(\theta) \in \R^{d \times d}
$$
By **delta method**, that $g(\hat{\theta}_n)$​ is also asymptotically normal, i.e., 
$$
\sqrt{n}\left(g(\hat{\theta}_n)- g(\theta))\right) \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}_k(0, \Gamma(\theta))
$$
where $\Gamma(\theta) = \nabla g(\theta)^T \Sigma (\theta) \nabla g(\theta) \in \R^{k \times k}$​​​.

By the properties of **multivariate Gaussians**, if $\mathbf{Z} \sim \mathcal{N}(\mathbf{0}, \Gamma (\theta ^*))$, then
$$
\Gamma (\theta ^*)^{-1/2} \mathbf{Z} \sim \mathcal{N}(\mathbf{0}, I_k)
$$
provided that $\Gamma(\theta)^{1/2}$​​​ exists. 

Assume $\Sigma(\theta)$​​​​ is invertible and $\nabla g(\theta)$​​ has rank $k$. So, $\Gamma (\theta)$ is invertible and
$$
\sqrt{n}\ \Gamma(\theta)^{-1/2}\left( g(\hat{\theta}_n) - g(\theta)\right) \xrightarrow[n\rightarrow \infty]{ (d)} \mathcal{N}_k(0,{I}_k)
$$
**Remark:** For a square matrix $M$​​, we are guaranteed that $M^{1/2}$​​ exists if $M$​​ is **positive-definite**. In particular, since $\Gamma (\theta ^*)$​​ is a covariance matrix, it is guaranteed to be **positive semidefinite**. So then $\Gamma (\theta ^*)^{-1/2}$​​ exists if and only if $\Gamma (\theta ^*)$​​ is invertible. 

#### Renormalizing 

**Wald's test for implicit hypotheses**

By **Slutsky's theorem**, if $\Gamma(\theta)$​ Is continuous in $\theta$​,
$$
\sqrt{n}\ \Gamma(\hat{\theta}_n)^{-1/2} \left(g(\hat{\theta}_n) - g(\theta)\right) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}_k(0, I_k)
$$
To test between the null and alternative hypotheses, we consider the test statistic (if $H_0$ is true, i.e., $g(\theta) = 0$)
$$
T_ n := \left| \sqrt{n} \Gamma (\widehat{\theta }_ n)^{-1/2} (g(\widehat{\theta }_ n)) \right|_2^2 = n g(\widehat{\theta }_ n)^ T \Gamma (\widehat{\theta }_ n)^{-1} g(\widehat{\theta }_ n)
$$
Under the null hypothesis, the test statistic converges to 
$$
n g(\hat{\theta}_n)^T \Gamma^{-1} (\hat{\theta}_n) g(\hat{\theta}_n) \xrightarrow[n \rightarrow \infty]{(d)} \chi_k^2
$$
Test with asymptotic level $\alpha$:
$$
\psi = \mathbb{1}\{T_n > q_\alpha\},
$$
where $q_\alpha$​ is the $(1-\alpha)$​-quantile of $\chi^2_{k}$​.

> #### Exercise 85
>
> Supposing that $d=6$ and $k=3$, what value of $C$ should be chosen so that $\psi$ is a test of asymptotic level $5\%$?
>
> **Answer:** 7.815
>
> **Solution:** 
>
> When $k=3$​, then $T_ n \xrightarrow [n \to \infty ]{(d)} \chi _3^2$​. The test $\psi = \mathbf{1}(T_ n > C)$​ will have asymptotic level $5\%$​ precisely when $C$​ is the $5\%$​-quantile $q_{0.05}$ of $\chi_3^2$. Consulting a table, we have that $q_{0.05} = 7.815$.

