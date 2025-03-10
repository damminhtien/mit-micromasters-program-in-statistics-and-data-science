# Lecture 9. Introduction to Maximum Likelihood Estimation

There are 7 topics and 5 exercises.

## 1. Maximum Likelihood Estimator

**Review: Maximizing composite functions**:

The arguments of the minima (resp. Arguments of the maxima) of a function $f(x)$, denoted by $\text{argmin} f(x)$ (resp. $\text{argmin}f(x)$), is the value(s) of $x$ at which $f(x)$ is minimum (resp. maximum). We can also restrict to a subset $S$ of the domain $f$, and denote by $\text{argmin}_{x \in S} f(x)$ (resp. $\text{argmin}_{x\in S} f(x)$) the value(s) of $x \in S$ at which $f(x)$ is minimum (resp. maximum) over $S$.

**Definition of maximum likelihood estimator**:

Let $X_1, ..., X_n \stackrel{iid}{\sim} \mathbf{P}_{\theta^*}$ be discrete random variables. We construct a statistical model $(E,(\mathbf{P}_\theta)_{\theta \in \Theta})$ where $\mathbf{P}_\theta$ has PMF $p_\theta$. We observe our sample to be $X_1 = x_1, X_2 = x_2, ...., X_n = x_n$. Let $L$ be the corresponding likelihood.

The *maximum likelihood estimator* of $\theta^*$ is defined as
$$
\hat{\theta}_n^{MLE} = \text{argmax}_{\theta \in \Theta} L(X_1, ..., X_n, \theta)\\
\text{where } \quad L(X_1, ..., X_n, \theta) =  \left( \prod _{i = 1}^ n p_\theta (X_ i) \right)
$$
provided it exists.

**Remark (Log-likelihood estimator)**: In practice, we use the fact that
$$
\hat{\theta}_n^{MLE} = \text{argmax}_{\theta \in \Theta}\log L(X_1, ..., X_n, \theta)
$$
**Interpretation of MLE:**

* MLE is the value of $\theta$ that maximizes the probability $\mathbf{P}_\theta$ of observing the data set $(x_1,..., x_n)$. 

  Since the likelihood is the joint density of $n$ iid samples from $\mathbf{P}_\theta$
  $$
  \mathbf{P}_\theta [X_1 = x_1, \ldots , X_ n = x_ n] = L_ n(x_1, \ldots , x_ n, \theta ).
  $$
  Hence, the MLE finds $\hat{\theta}_n$ that maximizes the probability that $x_1, ..., x_n$ were sampled from $\mathbf{P}_{\hat{\theta}_n}$.

* MLE is the value of $\theta$ that minimizes an estimator of the KL divergence between $\mathbf{P}_\theta$ and the true distribution $\mathbf{P}_{\theta^*}$.

  This is how the MLE was derived from KL divergence.

**Remark:** Under some technical conditions the MLE is a **weakly consistent estimator** for $\theta^*$, meaning that the MLE will converge to $\theta^*$ in probability under these conditions. However, there are examples of statistical models where the maximum likelihood estimator will **not** converge to the true parameter.

## 2. Concavity in 1 Dimension

**Review: Maximizing/minimizing functions**

Optimization is a whole field that is concerned with maximizing or minimizing functions.

Note that
$$
\min_{\theta \in \Theta} -h(\theta) \iff \max_{\theta \in \Theta} h(\theta)
$$
We focus on maximization. Maximization of arbitrary functions can be difficult. For example, $\theta \mapsto \prod\limits^n_{i=1}(\theta - X_i)$.

**A analytical definition of concave and convex functions**:

A function twice differentiable function $h:\Theta \subset \R \rightarrow \R$ is said to be *concave* if its second derivative satisfies
$$
h''(\theta) \leq 0, \quad \forall \theta \in \Theta
$$
It is said to be strictly *concave* if the inequality is strict: $h''(\theta) \leq 0$.

Moreover, $h$ is said to be (strictly) *convex* if $-h$ is (strictly) concave, i.e. $h''(\theta) \geq 0 \,\, (h''(\theta)>0).$ 

Examples:

* $\Theta = \R, h(\theta) = -\theta^2$ is concave.
* $\Theta = (0,\infty), h(\theta) = \sqrt{\theta}$ is concave.
* $\Theta=(0,\infty),h(\theta) = \log \theta$ is concave.
* $\Theta = [0,\pi],h(\theta)=\sin(\theta)$ is concave.
* $\Theta = \R, h(\theta) = 2\theta - 3$ is neither concave nor convex.

**A general/synthetic definition of concave and convex functions:**

A function $g:I \rightarrow \R$ is **concave** (or concave down) on an interval $I$, if for all pairs of real numbers $x_1 < x_2 \in I$
$$
g(tx_1+(1-t)x_2)\geq tg(x_1)+(1-t)g(x_2)\qquad \text {for all } \, 0 < t < 1.
$$
Geometrically, a concave function is shown below

![images_u3s2_concave](../assets/images/images_u3s2_concave.svg)

At $x=x_2-t(x_2-x_1)=tx_1+(1-t)x_2$, the $y$ value of the graph of $g$ is $g(x)=g(tx_1+(1-t)x_2)$, while the $y$ value of the secant line is $tg(x_1)+(1-t)g(x_2)$.

If the inequality is strict, i.e. if 
$$
g(tx_1+(1-t)x_2)> tg(x_1)+(1-t)g(x_2)\qquad \text {for all } \, 0 < t < 1.
$$
then $g$ is **strictly concave**.

The definition for (strictly) **convex** is analogous.

If in addition $g$ is twice differentiable in the interval $I$, i.e. $g''(x)$ exists for all $x \in I$, then $g$ is

* **Concave** if and only if $g''(x)\leq 0$ for all $x \in I$;
* **Strictly concave** if $g''(x) < 0$ for all $x \in I$;
* **Convex** if and only if $g''(x) \geq 0$ for all $x \in I$;
* **Strictly convex** if $g''(x) > 0$ for all $x \in I$;

**Remark:** Note that the synthetic definition above does not require differentiability at every point. In contrast, the analytical definition is less general, using inequality conditions on the second derivative. For example, the function $x↦x^4$ is strictly convex according to the definition above, but has three vanishing derivatives at the origin $x=0$.

## 3. Concavity in Higher Dimensions: Gradients, Hessians, Semi-Definiteness

**Multivariate concave functions**:

More generally for a multivariate function: $h:\Theta \subset \R^d \rightarrow \R, d \geq 2$, define the 

* Gradient vector: 
  $$
  \nabla h(\theta) = \begin{pmatrix}{ \partial h\over \partial \theta_1}(\theta) \\ \vdots \\{ \partial h\over \partial \theta_1}(\theta)  \end{pmatrix} \in \R^d
  $$

* Hessian matrix:
  $$
  \mathbf{H}h(\theta) = \begin{pmatrix} {\partial^2 h \over  \partial \theta_1 \partial \theta_1} (\theta) \dots {\partial^2 h \over  \partial \theta_1 \partial \theta_d} (\theta)\\ \\ \\ {\partial^2 h \over  \partial \theta_d \partial \theta_1} (\theta) \dots {\partial^2 h \over  \partial \theta_d \partial \theta_d} (\theta)\ \end{pmatrix} \in \R^{d \times d}
  $$

$h$ is concave $\iff \quad x^T\mathbf{H}h(\theta)x \leq 0 \quad \forall x \in \R^d, \theta \in \Theta$.

$h$ is strictly concave $\iff \quad x^T\mathbf{H}h(\theta)x < 0 \quad \forall x \in \R^d, \theta \in \Theta$. 

Note that **singular value decomposition (SVD)** can be used to compute $x^T\mathbf{H}h(\theta)x$. $ x^T\mathbf{H}h(\theta)x \leq 0$ is equivalent to that all eigenvalues of the matrix $\mathbf{H}$ are nonpositive. So if $ x^T\mathbf{H}h(\theta)x \geq 0$, the Hessian matrix of a convex function is **positive semidefinite**.

> #### Exercise 50
>
> Suppose $\theta = \begin{pmatrix}\theta_1 \\ \theta_2 \end{pmatrix}, \quad -h(\theta) = -\theta^2_1 - 2 \theta_2^2$, is the function $f(\theta)$ concave or convex?
>
> **Answer:** Concave
>
> **Solution:**
>
> First compute the gradient vector
> $$
> \nabla f(\theta) = \begin{bmatrix}-2\theta_1 \\ -4\theta_2 \end{bmatrix}
> $$
> Then compute the Hessian matrix
> $$
> \mathbf{H}h(\theta) = \begin{bmatrix}-2 & 0 \\ 0 & -4 \end{bmatrix}
> $$
> Hessian matrix is a **diagonal** matrix, which is good, since we can directly determine whether the function is concave or convex by observing whether the diagonal entries are all negative or all positive.
>
> Suppose $x = \begin{bmatrix}x_1 \\ x_2 \end{bmatrix}$, we compute
> $$
> x^T\mathbf{H}h(\theta)x = \begin{bmatrix}x_1 & x_2 \end{bmatrix} \begin{bmatrix}-2 & 0 \\ 0 & -4 \end{bmatrix} \begin{bmatrix}x_1 \\ x_2 \end{bmatrix} = -2x_1^2 - 4x_2^2 \leq 0
> $$

**Review: Compute the Hessian Matrix**:

Let
$$
f:\R^d \rightarrow \R \quad \theta = \theta =\begin{pmatrix} \theta _1\\ \theta _2\\ \vdots \\ \theta _ d\end{pmatrix} \mapsto f(\theta)
$$
denote a **twice-differentiable** function.

The Hessian of $f$ is the matrix
$$
\mathbf{H} f: \R^d \rightarrow \R^{d \times d}
$$
whose entry in the $i$-th row and $j$-th column is defined by
$$
\left(\mathbf{H}\, f\right)_{ij} :=\frac{\partial ^2}{\partial \theta _ i \partial \theta _ j} f, \quad 1 \leq i, j \leq d.
$$
The Hessian matrix of $f$ in this context is also denoted by $\nabla ^2 f$, the **second derivative** of $f$. This is not to be confused with the "Laplacian" of $f$, which is also denoted the same way.

> #### Exercise 51
>
> Consider the function $\, f(\theta )=-c_1 \theta _1^2-c_2 \theta _2^2-c_{3}\theta _3^2\,$ where $c_1, c_2, c_3 > 0$ as in the previous problem. Compute the Hessian matrix $\mathbf{H}f$.
>
> **Answer**:
>
> $\mathbf{H}f(\theta)=\begin{pmatrix}  -2c_1& 0& 0\\ 0& -2c_2& 0\\ 0& 0&  -2c_3\\ \end{pmatrix}.$
>
> **Solution**:
>
> First compute the gradient vector:
> $$
> \, f(\theta )=-c_1 \theta _1^2-c_2 \theta _2^2-c_{3}\theta _3^2\,\\
> \nabla f (\theta )=\left.\begin{pmatrix}  \frac{\partial f }{\partial \theta _1}\\ \frac{\partial f }{\partial \theta _2}\\ \frac{\partial f }{\partial \theta _3}\end{pmatrix}\right|_{\theta }\, =\, \begin{pmatrix}  -2c_1\theta _1\\ -2c_2 \theta _2\\ -2c_3\theta _3 \end{pmatrix}.
> $$
> Second compute the Hessian. One way to compute the Hessian is to start in $j$-th column of the Hessian matrix by the gradient of the $j$-th component of $\nabla f$. We obtain
> $$
> \, f(\theta )=-c_1 \theta _1^2-c_2 \theta _2^2-c_{3}\theta _3^2\,\\
> \begin{aligned}
> \mathbf{H}f(\theta ) &= \begin{pmatrix}  |& |& |\\ \nabla (-2c_1\theta _1)& \nabla (-2c_2 \theta _2)&  \nabla (-2c_3\theta _3)\\ |& |& |\\ \end{pmatrix}\\
> &= \begin{pmatrix}  -2c_1& 0& 0\\ 0& -2c_2& 0\\ 0& 0& -2c_3\\ \end{pmatrix}.
> \end{aligned}
> $$

**Semi-Definiteness**:

A symmetric (real-valued) $d\times d$ matrix $\mathbf{A}$ is **positive semi-definite** if 
$$
\mathbf{x}^ T \, \mathbf{A}\, \mathbf{x} \geq 0 \qquad \forall x \in \R^d
$$
If the inequality above is strict, i.e., if $\mathbf{x}^ T \, \mathbf{A}\, \mathbf{x} > 0$ for all non-zero vectors $\mathbb{x} \in \R^d$, then $\mathbf{A}$ is **positive definite**.

Analogously, a symmetric (real-valued) $d \times d$ matrix $\mathbf{A}$ is **negative semi-definite** (resp. **negative definite**) if $\mathbf{x}^T \mathbf{A}\mathbf{x}$ is **non-positive** (resp. negative) for all $\mathbf{x} \in \R^d - \{0\}$.

Note that by definition, positive (or negative) definiteness implies positive (or negative) semi-definiteness.

> #### Exercise 52
>
> Consider the same function
> $$
> \, f(\theta )=-c_1 \theta _1^2-c_2 \theta _2^2-c_{3}\theta _3^2\,
> $$
> Compute $\mathbf{x}^ T \, \left(\mathbf{H}f\right)\,  \mathbf{x}\,$ where $\mathbf{x}=\begin{pmatrix} x_1\\ x_2\\ x_3\end{pmatrix}$.
>
> **Answer**:
>
> $\mathbf{x}^ T \, \left(\mathbf{H}f\right)\,  \mathbf{x}\,= -2c_1x_1^2-2c_2x_2^2-2c_3x_3^2$
>
> **Solution**:
>
> Recall from the previous problems that
> $$
> \mathbf{H}f (\theta ) = \begin{pmatrix}  -2c_1& 0& 0\\ 0&  -2c_2& 0\\ 0& 0& -2c_3\\ \end{pmatrix}.
> $$
> Then, 
> $$
> \begin{aligned}
> \mathbf{x}^ T\, \left(\mathbf{H}f\right) \, \mathbf{x} &= \begin{pmatrix}  x_1& x_2& x_3 \end{pmatrix}\begin{pmatrix}  -2c_1 &  0 &  0\\ 0 &  -2c_2 &  0\\ 0 &  0& &  -2c_3\\ \end{pmatrix}\begin{pmatrix}  x_1\\ x_2\\ x_3 \end{pmatrix}\\
> &= -2c_1x_1^2-2c_2x_2^2-2c_3x_3^2\, <\, 0.
> \end{aligned}
> $$
> Since $c_1,c_2, c_3 > 0$, this means the $\mathbf{H}f$ is negative definite, (also negative semi-definite), and hence $f$ is strictly concave (also concave).

## 4. Worked Example: Concavity and Composition of Functions

Suppose $\Theta = (0,\infty), f(\theta) = \log(\theta_1 + \theta_2).$ Let's compute $\mathbf{x}^ T \, \left(\mathbf{H}f\right)\,  \mathbf{x}\,$.

First compute $\nabla f(\theta)$:
$$
\nabla f(\theta) = \begin{pmatrix} {1\over \theta_1 + \theta_2} \\{1\over \theta_1 + \theta_2} \end{pmatrix}
$$
Then compute $\mathbf{H}f(\theta)$
$$
\mathbf{H}f(\theta) =\begin{pmatrix}-{1\over (\theta_1 + \theta_2)^2} & -{1\over (\theta_1 + \theta_2)^2} \\-{1\over (\theta_1 + \theta_2)^2} & -{1\over (\theta_1 + \theta_2)^2} \end{pmatrix}
$$
Finally, compute $\mathbf{x}^ T \, \left(\mathbf{H}f\right)\,  \mathbf{x}\,$
$$
\begin{pmatrix}x_1 & x_2 \end{pmatrix} \left(\mathbf{H}f(\theta)\right) \begin{pmatrix}x_1\\x_2 \end{pmatrix} = \begin{pmatrix}x_1 & x_2 \end{pmatrix} \begin{pmatrix} -{x_1 + x_2 \over (\theta_1 + \theta_2)^2}\\ -{x_1 + x_2 \over (\theta_1 + \theta_2)^2}\end{pmatrix} = {x_1^2 + x_2x_1 \over (\theta_1 + \theta_2)^2} - {x_2^2 + x_1x_2 \over (\theta_1 + \theta_2)^2} = -{(x_1 + x_2)^2 \over (\theta_1 + \theta_2)^2}
$$
Therefore, it is a non-positive number,
$$
\mathbf{x}^ T \, \left(\mathbf{H}f\right)\,  \mathbf{x}\, = -{(x_1 + x_2)^2 \over (\theta_1 + \theta_2)^2} \leq 0
$$
which means the function $f (\theta)$ is concave.

**Remark:** If you have a linear function composed with a concave function, then you end up with a concave function.

> #### Exercise 53
>
> Let $f_1, f_2$ be convex functions on $\R$. Determine if the following functions are necessarily convex or concave.
>
> 1. $3f_1 + 2f_2$
>
> 2. $-10f_1$
>
> 3. $f_2f_1$
>
> **Answer**: 
>
> 1. Convex
>
> 2. Concave
>
> 3. Cannot be determined without more information
>
> **Solution**:
>
> 1. Given $f_1, f_2$ are convex we have
>    $$
>    f_1(tx_1+(1-t)x_2)\leq tf_1(x_1)+(1-t)f_1(x_2)\qquad \text {for all } \, 0\leq t\leq 1
>    $$
>    and the same holds for $f_2$.
>
>    The same inequality holds for $g=3f_1+2f_2$:
>    $$
>    \begin{aligned}
>    g(tx_1+(1-t)x_2) &= 3f_1(tx_1+(1-t)x_2)+2f_2(tx_1+(1-t)x_2)\\
>    &\leq 3\left(tf_1(x_1)+(1-t)f_1(x_2)\right)+2\left(tf_2(x_1)+(1-t)f_2(x_2)\right)\\
>    &=tg(x_1)+(1-t)g(x_2).
>    \end{aligned}
>    $$
>    Hence, $3f_1 + 2f_2$ is also convex.
>
>    **Remark:** In general, any function $c_1f_1 + c_2f_2$ where $c_1, c_2>0$ is convex of $f_1, f_2$ are.
>
> 2. $-10f_1$ is concave, because it is negative of a convex function.
>
> 3. For example, $f_1(x) = x$ and $f_2=x^2$, then $(f_1 f_2)(x) = x^3$ which is neither convex nor concave. Other examples of $f_1$ and $f_2$, e.g. $f_1 = f_2 = x^2$ will lead to $f_1 f_2$ being convex. 

## 5. Concavity in Higher Dimensions and Eigenvalues

**Concavity in 2 dimensions: Compute the Hessian**

Compute the Hessian $\mathbf{H}f$ of the function $f(x,y) = -2x^2 + \sqrt{2}xy - {5\over 2} y^2$? 

We compute that
$$
(\mathbf{H}f)_{11} = \frac{\partial ^2 f }{\partial x^2} = -4, \quad  (\mathbf{H}f)_{12} = \frac{\partial ^2 f }{\partial x \partial y} = \sqrt{2}\\
(\mathbf{H}f)_{21} = \frac{\partial ^2 f }{\partial x \partial y} = \sqrt{2}, \quad (\mathbf{H}f)_{22} = \frac{\partial ^2 f }{\partial y^2} = -5.
$$
Therefore,
$$
\mathbf{H}f = \begin{pmatrix} {\partial^2 f \over \partial x^2} & {\partial^2 f \over \partial x \partial y} \\ {\partial^2 f \over \partial y \partial x} & {\partial^2 f \over \partial y^2} \end{pmatrix}  = \begin{pmatrix}  -4 &  \sqrt{2} \\ \sqrt{2} &  -5 \end{pmatrix}.
$$

**Concavity in 2 dimensions: Positive Definiteness and Eigenvalues**

Consider $f(x,y) = -2x^2 + \sqrt{2}xy - {5\over 2} y^2$. What are the eigenvalues $\lambda_1, \lambda_2$ of $\mathbf{H}f$? Assume that $\lambda_1 < \lambda_2$. Is $f$ concave or convex?

Recall the Hessian calculated previously is
$$
\mathbf{H}f = \begin{pmatrix}  -4 &  \sqrt{2} \\ \sqrt{2} &  -5 \end{pmatrix}.
$$
To find the eigenvalues, we need to solve for $\lambda$ such that
$$
\mathrm{det}\left( \mathbf{H}f - \lambda I \right) = \mathrm{det}\left(\begin{pmatrix}  -4 - \lambda &  \sqrt{2} \\ \sqrt{2} &  -5 - \lambda \end{pmatrix} \right) = \lambda ^2 + 9\lambda + 18 = 0.
$$
Factoring the quadratic: $\lambda ^2 + 9\lambda + 18 = (\lambda + 6)(\lambda +3)$ shows that $\lambda_1 = -6$ and $\lambda_2 = -3$.

**Remark:** The function $f$ is twice-differentiable, so it is concave if $x^ T \mathbf{H}f x \leq 0$ for all $x \in \R^2$. By the remark in the problem statement, this is equivalent to all of the eigenvalues of $\mathbf{H}f$ being negative. Hence, $f$ is concave (in fact it is strictly concave).

## 6. Strictly Concave Functions and Unique Maximizer

**Optimality conditions**:

Strictly concave functions are easy to maximize: if they have a maximum, then it is **unique**. It is the unique solution to
$$
h'(\theta) = 0
$$
or, in the multivariate case
$$
\nabla h(\theta) = 0 \in \R^d
$$
There are many algorithms to find it numerically: this is the theory of "**convex optimization**". In this class, often a **closed form formula** for the maximum.

> #### Exercise 54
>
> Let $f:\R^2 \rightarrow \R$ be a twice-differentiable function, such that the top-left element of the Hessian matrix $\mathbf{H}f(0,0)_{1,1} > 0$ is positive. Is $f$ concave?
>
> **Answer**: No
>
> **Solution**:
>
> Recall that $f$ is concave at $(0,0)$ if for all $(x,y) \in \R^2$,
> $$
> (x, y) \mathbf{H}f(0,0) \begin{pmatrix}  x \\ y \end{pmatrix} < 0.
> $$
> By expanding and using the definition of the Hessian, we see that
> $$
> (x, y) \mathbf{H}f(0,0) \begin{pmatrix}  x \\ y \end{pmatrix} = x^2 \frac{\partial ^2}{\partial x^2} f(0,0) + xy \left( \frac{\partial ^2}{\partial x \partial y}f(0,0) + \frac{\partial ^2}{\partial y \partial x}f(0,0) \right) + y^2 \frac{\partial ^2}{\partial y^2}f(0,0).
> $$
> By assumption, we know that $\frac{\partial ^2}{\partial x^2} f(0,0) > 0$. Hence,
> $$
> (1, 0)^ T \mathbf{H}f(0,0) \begin{pmatrix}  1 \\ 0 \end{pmatrix} = \frac{\partial ^2}{\partial x^2} f(0,0) >0.
> $$
> This violates the definition of concavity.

## 7. Maximum Likelihood Estimator of Bernoulli, Poisson, Gaussian Trials

* Bernoulli trials: $\hat{p}_ n^{MLE} = \bar{X}_n$.

  Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Ber}(p^*)$ for some unknown $p^* \in (0,1)$. You construct the associated statistical model $(\{ 0,1\} , \{ \text {Ber}(p)\} _{p \in (0,1)})$. Let $L_n$ denote the likelihood of this statistical model. The **likelihood** of a Bernoulli statistical model has the formula 
  $$
  L_ n(x_1, \ldots , x_ n, p) = \prod _{i = 1}^ n p^{x_ i}(1 - p)^{1 - x_ i} = p^{\sum _{i = 1}^ n x_ i} (1 -p)^{n - \sum _{i = 1}^ n x_ i}.
  $$
  Oftentimes for computing the MLE it is more convenient to work with and optimize the **log-likelihood** 
  $$
  \ell (p) := \ln L_ n(x_1, \ldots , x_ n, p)
  $$
  Observe that
  $$
  \begin{aligned}
  \ln L_ n(x_1, \ldots , x_ n, p) &= \ln \left( p^{\sum _{i = 1} x_ i} (1 -p)^{n - \sum _{i = 1} x_ i} \right)\\
  &= \left( \sum _{i = 1}^ n x_ i \right) \ln p + \left(n - \sum _{i = 1}^ n x_ i \right) \ln (1 - p).
  \end{aligned}
  $$
  Taking the derivative with respect to $p$,
  $$
  \frac{\partial }{\partial p} \ln L_ n(x_1, \ldots , x_ n, p) = \frac{\sum _{i = 1}^ n x_ i}{p} - \frac{n - \sum _{i = 1}^ n x_ i}{1- p}.
  $$
  We set this to be $0$ and solve for $p$:
  $$
  \begin{aligned}
  \frac{\sum _{i = 1}^ n x_ i}{p} - \frac{n - \sum _{i = 1}^ n x_ i}{1- p} &= 0 \iff\\
  \frac{(1 - p) \sum _{i = 1}^ n x_ i - p\left(n - \sum _{i = 1}^ n x_ i\right) }{p(1 - p)} &= 0 \iff\\
  \frac{\sum _{i = 1}^ n x_ i - np}{p(1- p)} &= 0 .
  
  \end{aligned}
  $$
  Since the derivative blows up at $p=0,1$, we can assume $0<p < 1$ and ignore denominator for the purpose of solving for $p$. Hence $\hat{p} = {1 \over n} \sum^n_{i=1} x_i$ is the **unique critical point** of the log-likelihood.

  Take the second derivative
  $$
  \frac{\partial }{\partial p } \left( \frac{\sum _{i = 1}^ n X_ i}{p} - \frac{n - \sum _{i = 1}^ n X_ i}{1- p} \right) = - \frac{\sum _{i = 1}^ n x_ i}{p^2} - \frac{n - \sum _{i = 1}^ n x_ i}{(1 - p)^2}.
  $$
  Since the expression is always negative, this implies that the critical point $\hat{p}$ is a **local maximum**.

  Testing the endpoints we see
  $$
  L_ n(x_1, \ldots , x_ n, 0) = 0^{\sum _{i = 1}^ n x_ i} (1)^{n - \sum _{i = 1}^ n x_ i} = 0\\
  L_ n(x_1, \ldots , x_ n, 1) = 1^{\sum _{i = 1}^ n x_ i} (0)^{n - \sum _{i = 1}^ n x_ i} = 0
  $$
  Since the likelihood is non-negative, the endpoints are actually **global minima**.

  Hence, the global maximum is achieved at $\hat{p} = \displaystyle \frac{1}{n} \sum _{i = 1}^ n x_ i$. Plugging in the random variables $X_1, ...,X_n$, we derive the MLE true parameter $p^*$:
  $$
  \hat{p}_ n^{MLE} = \frac{1}{n } \sum _{i = 1}^ n X_ i
  $$
  which is the **sample mean**.

  **Remark**: **MLE** for a Bernoulli statistical model is the **sample mean**.

* Poisson model: $\hat{\lambda}_ n^{MLE} = \bar{X}_n$.

  Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Poiss}(\lambda^*)$ for some unknown $\lambda^* \in (0,\infty)$. You construct the associated statistical model $(\N \subset\{ 0\} , \{ \text {Poiss}(\lambda)\} _{\lambda \in (0,\infty)})$. Let $L_n$ denote the likelihood of this statistical model. The **likelihood** of a Poisson statistical model has the formula 
  $$
  L_ n(x_1, \ldots , x_ n, \lambda ) = \prod _{i = 1}^ n e^{-\lambda } \frac{\lambda ^{x_ i}}{{x_ i}!} = e^{-n \lambda } \frac{\lambda ^{\sum _{i = 1}^ n x_ i}}{x_1 ! \cdots x_ n !}
  $$
  Observe that
  $$
  \ln L_ n(x_1, \ldots , x_ n, \lambda ) = \ln \left(e^{-n \lambda } \frac{\lambda ^{\sum _{i = 1} x_ i}}{x_1! \cdots x_ n!} \right) = -n \lambda + (\sum _{i = 1}^ n x_ i) \ln \lambda - \ln \left(x_1! \cdots x_ n! \right)
  $$
  Taking the derivative with respect to $\lambda$,
  $$
  \frac{\partial }{\partial \lambda } \ln L_ n(x_1, \ldots , x_ n, \lambda ) = -n + \frac{\sum _{i = 1}^ n x_ i}{\lambda }.
  $$
  Setting this equal to $0$, we recover the **critical point**
  $$
  \hat{\lambda } = \frac{1}{n} \sum _{i =1 }^ n x_ i.
  $$
  Perform the second derivative test and verify that this critical point is indeed a **global maximum**. 
  $$
  \frac{\partial^2 }{\partial \lambda } \ln L_ n(x_1, \ldots , x_ n, \lambda ) = - \frac{\sum _{i = 1}^ n x_ i}{\lambda^2 }.
  $$
  which is non-positive, so that the likelihood the concave.

  Moreover, it is a global maximum since $\lim _{\lambda \to 0}L_ n(X_1, \ldots , X_ n, \lambda ) = -\infty$ and $\lim _{\lambda \to \infty}L_ n(X_1, \ldots , X_ n, \lambda ) = 0$.

  This verifies that the MLE is
  $$
  \hat{\lambda }_ n^{MLE} = \frac{1}{n} \sum _{i =1 }^ n x_ i,
  $$
  Which is the **sample mean**.

  **Remark**: **MLE** for a Poisson statistical model is the **sample mean**.

* Gaussian model: $(\hat{\mu}_n, \hat{\sigma}^2_n) = (\bar{X}_n, \hat{S}_n)$, where $\hat{S}_n = {1\over n}\sum\limits^n_{i=1}(X_i - \bar{X}_n)^2$

  Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathcal{N}(\mu,\sigma^2)$ for some unknown $\mu, \sigma^2$. You construct the associated statistical model $(\mathbb {R}, \{ N(0, \tau )\} _{\tau > 0})$. Let $L_n$ denote the likelihood of this statistical model. The **likelihood** of a Gaussian statistical model has the formula 
  $$
  L_ n(x_1, \ldots , x_ n, (\mu , \sigma ^2)) = \frac{1}{(\sigma \sqrt{2 \pi })^ n} \exp (-\frac{1}{2 \sigma ^2} \sum _{i = 1}^ n (x_ i - \mu )^2).
  $$
  Now compute the Hessian and verify $\mathbf{x^THx} \leq 0$.

  We first take the partial derivative and set it to $0$,
  $$
  \begin{aligned}
  \nabla L_n(\hat{\mu}, \hat{\sigma}^2) = \begin{pmatrix}{\partial \over \partial \mu} L(\hat{\mu}, \hat{\sigma}^2) \\ {\partial \over \partial \sigma^2} L(\hat{\mu}, \hat{\sigma}^2) \end{pmatrix} = 0
  \end{aligned}
  $$
  For the first entry, we get
  $$
  {\partial \over \partial \mu} L(\hat{\mu}, \hat{\sigma}^2) = {1\over 2 \hat{\sigma}^2} \sum^n_{i=1} 2(x_i -  \hat{\mu}) = 0\\
  \implies \hat{\mu}  = {1\over n} \sum^n_{i=1}x_i
  $$
  For the second entry, it is more convenient to work on log likelihood,
  $$
  \begin{aligned}
  \ln L_ n(x_1, \ldots , x_ n,\mu, \sigma^2 )=& \ln \left( \frac{1}{( \sqrt{2 \pi \sigma^2 })^ n} \exp (-\frac{1}{2 \sigma^2 } \sum _{i = 1}^ n (x_ i-\mu)^2) \right)\\
  =&- \frac{n}{2} \ln ( 2 \pi \sigma^2 ) - \frac{1}{2 \sigma^2 } \sum _{i = 1}^ n (x_ i-\mu)^2\\
  =&- \frac{n}{2} \ln (  \sigma^2 ) - n \ln(\sqrt {2\pi}) - \frac{1}{2 \sigma^2 } \sum _{i = 1}^ n (x_ i-\mu)^2
  \end{aligned}
  $$
  Taking derivatives with respect to $\sigma^2$ and we get
  $$
  {\partial \over \partial \mu}  \ln L_ n(x_1, \ldots , x_ n,\mu, \sigma^2 ) = -\frac{n}{2 \sigma^2 } + \frac{ \displaystyle \sum _{i = 1}^ n (x_ i-\mu)^2}{2 \sigma ^4} = 0\\
  \implies 
  $$
  Setting this equal to $0$, we get
  $$
  \widehat{S}_n = \sigma^2 = \frac{1}{n} \sum _{i = 1}^ n (X_ i-\hat{\mu})^2 = \frac{1}{n} \sum _{i = 1}^ n (X_ i-\bar{X}_n)^2
  $$
