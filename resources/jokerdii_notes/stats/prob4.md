Problem set for Lec8-9.

# 1. Kullback-Leibler divergence

For the following pairs of distribution $(\mathbf{P}, \mathbf{Q})$, compute the Kullback-Leibler divergence KL$(\mathbf{P}, \mathbf{Q})$

1. $\mathbf{P}= \mathcal{N}(a, \sigma ^2), \quad \mathbf{Q}= \mathcal{N}(b, \sigma ^2), \quad a, b \in \mathbb {R},\,  \sigma ^2 > 0.$

2. $\mathbf{P}= \textsf{Ber}(a), \quad \mathbf{Q}= \textsf{Ber}(b), \quad a, b \in (0, 1)$.
3. $\mathbf{P} = \textsf{Unif}([0, \theta _1]), \quad \mathbf{Q} = \textsf{Unif}([0, \theta _2]), \quad 0 < \theta _1 < \theta _2.$
4. $\mathbf{P} = \textsf{Exp}(\lambda ), \quad \mathbf{Q} = \textsf{Exp}(\mu ), \quad \lambda , \mu \in (0, \infty ).$

> **Solution**:
>
> 1. If we write $X \sim \mathbf{P}$, to estimating KL by expectation, we can compute
>    $$
>    \begin{aligned}
>    \text{KL}(\mathbf{P}, \mathbf{Q}) &= \mathbb E_{\mathbf{P}} \left[ \ln \left( \frac{\frac{1}{\sqrt{2 \pi }} \exp \left( - \frac{-(X - a)^2}{2\sigma ^2} \right)}{\frac{1}{\sqrt{2 \pi }} \exp \left( - \frac{(X - b)^2}{2\sigma ^2} \right)} \right) \right]\\
>    &= \mathbb E_{\mathbf{P}} \left[ -\frac{(X - a)^2}{2 \sigma ^2} + \frac{(X-b)^2}{2 \sigma ^2}\right]\\
>    &= \frac{1}{2 \sigma ^2} \mathbb E_{\mathbf{P}} \left[ b^2 -a^2 - 2bX + 2aX \right]\\
>    &= \frac{1}{2 \sigma ^2} \mathbb E_{\mathbf{P}} \left[ - 2bX + 2aX + (2ab - 2a^2) - (2ab - 2a^2) + b^2 - a^2 \right]\\
>    &= \frac{1}{2 \sigma ^2} \mathbb E_{\mathbf{P}} \left[ (- 2bX + 2aX + 2ab - 2a^2 )+ (- 2ab + b^2 + a^2 ) \right]\\
>    &= \frac{1}{2 \sigma ^2} \mathbb E_{\mathbf{P}} \left[ 2 (a - b)(X - a) + (a - b)^2 \right]\\
>    &= \frac{(a-b)^2}{2 \sigma ^2}
>    \end{aligned}
>    $$
>    Because $\,   \mathbb E_{\mathbf{P}}[(X - a)] = 0  \,$.
>
> 2. If we write $X \sim \mathbf{P}, Y \sim \mathbf{Q}$, since
>    $$
>    \text{KL}(\mathbf{P}, \mathbf{Q}) = \sum\limits _{x \in E} p(x) \ln \left( \frac{p(x)}{q(x)} \right)
>    $$
>    We have
>    $$
>    \begin{aligned}
>    \textsf{KL}(\mathbf{P},\, \mathbf{Q}) &= \mathbf{P}(X = 0) \ln \frac{\mathbf{P}(X = 0)}{\mathbf{P}(Y = 0)} + \mathbf{P}(X = 1) \frac{\mathbf{P}(X = 1)}{\mathbf{P}(Y=1)}\\
>    &= \displaystyle  a \ln \frac{a}{b} + (1-a) \ln \frac{1-a}{1-b}.\\
>    \end{aligned}
>    $$
>
> 3. We compute
>    $$
>    \begin{aligned}
>    \text{KL}(\mathbf{P},\mathbf{Q}) &= \mathbb E_{\mathbf{P}}\left[\ln \frac{\frac{1}{\theta _1}}{\frac{1}{\theta _2}}\right]\\
>    &= \ln \left( \frac{\theta _2}{\theta _1} \right).
>    \end{aligned}
>    $$
>    If we try to compute the KL divergence the other way round, we notice that $\mathbf{P}$ is not supported between for $\theta _1<X<\theta _2$, when $\mathbf{P} = 0$ in the denominator. Thus we compute the expectation by integrating explicitly:
>    $$
>    \begin{aligned}
>    \textsf{KL}(\mathbf{Q},\, \mathbf{P}) &= \mathbb E_{\mathbf{Q}}\left[\ln \frac{q}{p}\right]\quad \text {where } p,q ,\text {are the pdfs of }\mathbf{P},\mathbf{Q}\, \text {respectively}\\
>    &= \int _{0}^{\theta _1} \frac{1}{\theta _2}\ln \frac{1/\theta _2}{1/\theta _1} dx+ \int _{\theta _1}^{\theta _2} \frac{1}{\theta _2}\ln \frac{1/\theta _2}{0} dx\\
>    &= + \infty
>    \end{aligned}
>    $$
>    because the second term diverges to $+\infty$.
>
>    In general $\textsf{KL}(\mathbf{P},\mathbf{Q})\neq \textsf{KL}(\mathbf{Q},\mathbf{P})$.
>
> 4. If $X \sim \mathbf{P}$, then
>    $$
>    \begin{aligned}
>    \textsf{KL}(\mathbf{P},\, \mathbf{Q}) &= \mathbb E_ P \left[ \ln \frac{\lambda e^{-\lambda x}}{\mu e^{-\mu x}} \right]\\
>    &= \mathbb E_ P \left[ \ln \frac{\lambda }{\mu } + (\mu - \lambda ) X \right]\\
>    &=  \ln \frac{\lambda }{\mu } + (\mu - \lambda ) \frac{1}{\lambda }\\
>    &=  \ln \frac{\lambda }{\mu } + \frac{\mu }{\lambda } - 1
>    \end{aligned}
>    $$
>    Because $\mathbb{E}_p[X] = {1\over \lambda}$.

# 2. Compute Total Variation Distance

Compute the total variation distance $\textsf{TV}(\mathbf{P},\mathbf{Q})$ between
$$
\mathbf{P}= X \quad \text {and} \quad \mathbf{Q}= X+c, \quad \text {where } X \sim \textsf{Ber}(p), p\in (0,1), \text {and } c\in \mathbb {R}.
$$

1. For $c \in \{-1,0,1\}$.
2. For $c=0$.
3. For $c=1$ or $c=-1$.

> **Solution**:
>
> 1. $\textsf{TV}(\mathbf{P},\mathbf{Q})=1$
>
>    For $c \notin \{-1,0,1\}$, the support of $X$ and $X+c$ are disjoint, hence $\textsf{TV}(X,X+c)=1$
>
> 2. $\textsf{TV}(\mathbf{P},\mathbf{Q})=0$
>
>    For $c=0$, by the definiteness property $\textsf{TV}(X,X)=0$.
>
> 3. $\textsf{TV}(\mathbf{P},\mathbf{Q})={1\over 2}(1 + |1-2p|)$ 
>
>    For $c=1$ (resp. $c = -1$), the support of $X$ and $X+c$ intersect at $X=1$ (resp. at $X=0$). Hence
>    $$
>    \begin{aligned}
>    \textsf{TV}(X,X+c) &= {1\over 2} (|p(0) - q(0)| + |p(1) - q(1)| + |p(2) - q(2)|)\\
>    & = \frac{1}{2} (|(1-p)-0|+|p-(1-p)|+|0 - p|)\\
>    &=  \frac{1}{2} (1+|1-2p|)\qquad \text {where } c=1, \, \text {or }-1.
>    \end{aligned}
>    $$

Compute the total variation distance $\textsf{TV}(\mathbf{P},\mathbf{Q})$ between
$$
\mathbf{P}= \textsf{Ber}(p) \quad \text {and} \quad \mathbf{Q}= \textsf{Ber}(q), \quad \text {where } p, q \in [0,1].
$$
Let $X_1 ,...,X_n$ be $n$ i.i.d. Bernoulli random variables with some parameter $p \in [0,1]$, and $\bar{X}_n$ be their empirical average. Consider the total variation distance $\textsf{TV}(\textsf{Ber}(\bar X_ n), \textsf{Ber}(p))$ between $\textsf{Ber}(\bar X_ n)$ and $\textsf{Ber}(p)$ as a function of the random variable $\bar{X}_n$, and hence a random variable itself. Does $\textsf{TV}(\textsf{Ber}(\bar X_ n), \textsf{Ber}(p))$ necessarily converge in probability to a constant ?

>**Solution:**
>
>The TV is
>$$
>\textsf{TV}(\textsf{Ber}(p), \textsf{Ber}(q)) = \frac{1}{2} \left[ | p - q | + | (1-p) - (1-q) | \right] = |p-q|
>$$
>Intuitively, the two distributions: $\textsf{Ber}(\bar X_ n) $ and $\textsf{Ber}(p) $ should behave similarly since
>$$
>\bar X_ n \xrightarrow [n \to \infty ]{\  i.p.} p.
>$$
>Recall that by definition, the convergence in probability means
>$$
>P( | \bar X_ n - p | > \epsilon ) \xrightarrow [n \to \infty ]{} 0.
>$$
>By the Law of Large Numbers, we can say that the total variation distance will converge in probability to $0$ as goes to infinity.
>$$
>\textsf{TV}(\textsf{Ber}(\bar X_ n), \textsf{Ber}(p)) = | \bar X_ n - p | \xrightarrow [n \to \infty ]{\  p.} 0.
>$$

Compute the total variation distance $\textsf{TV}(\mathbf{P},\mathbf{Q})$ between
$$
P = \textsf{Unif}([0,s]) \quad \text {and} \quad Q = \textsf{Unif}([0,t]), \quad \text {where } 0 < s < t.
$$

> **Solution:**
>
> The densities of the two distributions are
> $$
> f_ s(x) = \frac{1}{s} \mathbf{1}\{ 0 \leq x \leq s\} , \quad f_ t(x) = \frac{1}{t} \mathbf{1}\{ 0 \leq x \leq t\} .
> $$
> We have
> $$
> \begin{aligned}
> \textsf{TV}(\textsf{Unif}([0,s]), \textsf{Unif}([0,t])) &= \frac{1}{2} \int _{\mathbb {R}} |f_ s(x) - f_ t(x)| \,  dx\\
> &= \frac{1}{2} \left[ \int _0^ s \left| \frac{1}{s} - \frac{1}{t} \right| \,  dx + \int _ s^ t \left| \frac{1}{t} \right| \,  dx \right]\\
> &= \frac{1}{2} \left[ \left( 1 - \frac{s}{t} \right) + \left( 1 - \frac{s}{t} \right) \right]\\
> &=  1 - \frac{s}{t}.
> \end{aligned}
> $$
> Hence, $\textsf{TV}(\textsf{Unif}([0,s]), \textsf{Unif}([0,t]))$ is a continuous function in $t$ that decreases to $0$ as $t$ approaches $s$.

Let $X \sim \mathcal{N}(\mu, \sigma^2)$ and $Y \sim \mathsf{Ber}(p)$. Compute the total variation distance between the distributions of sign $(X)$ and $Y-1$: $\textsf{TV}(\text {sign}(X),Y-1)$. Note that sign $(X)$ is a function of the random variable with
$$
\text{sign}(X) = \begin{cases}1 &\text{if } X>0\\0 &\text{if } X=0\\-1 &\text{if } X<0 \end{cases}
$$

> **Solution:**
>
> Observe that $\frac{X-\mu }{\sigma }\sim \mathcal{N}(0,1)$. Hence
> $$
> \text {sign}(X)\, =\, \begin{cases} -1&  \, \text {with probability}\, \, \Phi \left(-\frac{\mu }{\sigma }\right)\\ 1& \, \text {with probability}\, \, 1-\Phi \left(-\frac{\mu }{\sigma }\right)\, =\, \Phi \left(\frac{\mu }{\sigma }\right)\\ \end{cases}
> $$
> Hence, 
> $$
> \begin{aligned}
> 2\textsf{TV}(\text {sign}(X),Y-1) &= |f(1) - p(1)| + |f(0) - p(0)| + |f(-1) - p(-1)|\\
> & = \lvert \Phi \left(\frac{\mu }{\sigma }\right) - 0\rvert +\lvert 0-p \rvert +\lvert \Phi \left(-\frac{\mu }{\sigma }\right)-(1-p)\rvert\\
> &=\Phi \left(\frac{\mu }{\sigma }\right)+p+\lvert 1-p-\Phi \left(-\frac{\mu }{\sigma }\right)\rvert .
> \end{aligned}
> $$

Compute the total variation distance $\textsf{TV}(\mathbf{P},\mathbf{Q}) $ between
$$
\mathbf{P}= \textsf{Ber}(p) \quad \text {and} \quad \mathbf{Q}= \textsf{Poiss}(p), \quad \text {where } p\in (0,1).
$$

> **Solution:**
>
> The PMF $f_X(x)$ for $X \sim \mathsf{Poiss}(p)$ is
> $$
> f_ X(x)=e^{-p}\frac{p^ x}{x!}\qquad \text {for } x=0,1,2\ldots .
> $$
> Hence,
> $$
> \begin{aligned}
> 2\textsf{TV}(\textsf{Ber}(p), \textsf{Poiss}(p)) &= \lvert e^{-p}-(1-p)\rvert +\lvert pe^{-p} -p \rvert + e^{-p}\left(\frac{p^2}{2!}+ \frac{p^3}{3!}+\cdots \right)\\
> &=\left( e^{-p}-(1-p)\right)+\left( p\left(1-e^{-p}\right)\right)+e^{-p}\left(e^{p}-(1+p) \right)\quad \text {since }e^{-p}>(1-p) \, \text {for } p>0\\
> &=  2 \left(p\left(1-e^{-p}\right)\right)\\
> \implies \textsf{TV}(\textsf{Ber}(p), \textsf{Poiss}(p))&=p\left(1-e^{-p}\right).
> \end{aligned}
> $$

# 3. Concave Functions

A symmetric $2 \times 2$ matrix $\mathbf{A}$(i.e. $\mathbf{A}^T=\mathbf{A}$) is negative semi-definite, i.e. $\,  \mathbf{x}^ T \mathbf{A}\mathbf{x}\leq 0 \,$ for all $\,  \mathbf{x}\in \mathbb {R}^2 \,$, if and only if both of the following is true:

* $\text{tr}(\mathbf{A})\leq 0$
* $\text{det}(\mathbf{A}) \geq 0$

This fact can be explained in terms the eigenvalues of $\mathbf{A}$. Let $\lambda_1$ and $\lambda_2$ be the eigenvalues of $\mathbf{A}$, then $\text{tr}(\mathbf{A}) = \lambda_1 + \lambda_2$ while $\text{det}(\mathbf{A}) = \lambda_1 \lambda_2$. The two conditions above ensure that $\lambda_1, \lambda_2 \leq 0$.

Use the fact given above to determine whether the following functions concave, convex, or neither.s

1. $f_1(\theta _1, \theta _2) = -\theta _1^2 + \frac{1}{2}(\theta _1 - \theta _2)^2 - 3 \theta _2^2, \quad (\theta _1, \theta _2) \in \mathbb {R}^2$
2. $f_2(\theta _1, \theta _2) = -\theta _1^4-\theta _2^4 - (\theta _2 - \theta _1)^3, \quad (\theta _1, \theta _2) \in \mathbb {R}^2, \text { with } \theta _1 < \theta _2$

> **Solution**:
>
> 1. Concave.
>
>    If $f$ is a function from $\,   \Omega \subseteq \mathbb {R}^ d \to \mathbb {R} \,$, then it is concave if the Hessian of $f$ is negative semi-definite. In the special case of two dimensions, this can be checked by testing whether both $\text{tr}\nabla^2 f\leq 0$ and $\text{det}\nabla^2 f \geq 0$ are true.s
>    $$
>    \nabla f_1(\theta _1, \theta _2) =\begin{pmatrix}  -\theta _1 - \theta _2\\ -\theta _1 - 5 \theta _2 \end{pmatrix}\\
>     H f_1(\theta _1, \theta _2) =\begin{pmatrix}  -1 &  -1\\ -1 &  -5 \end{pmatrix}.
>    $$
>    Since $\operatorname {tr}\nabla ^2 f_1 = -6 < 0$ and $ \mathrm{det}\nabla ^2 f_1 = 4 > 0$, we have $\nabla ^2 f $ is negative semi-definite for all $\theta$, and in turn, $f_1$ is concave.
>
> 2. Concave.
>    $$
>    \begin{aligned}
>    \nabla f_2(\theta _1, \theta _2) &= \begin{pmatrix}  -4 \theta _1^3 + 3(\theta _2 - \theta _1)^2\\ -4 \theta _2^3 - 3(\theta _2 - \theta _1)^2 \end{pmatrix}\\
>     H f_2(\theta _1, \theta _2) &=\begin{pmatrix}  -12 \theta _1^2 - 6(\theta _2 - \theta _1) &  6(\theta _2 - \theta _1)\\ 6(\theta _2 - \theta _1) &  -12 \theta _2^2 - 6(\theta _2 - \theta _1) \end{pmatrix}.
>    \end{aligned}
>    $$
>    We again check
>    $$
>    \begin{aligned}
>    \operatorname {tr}\nabla ^2 f_2(\theta _1, \theta _2) &= -12 \theta _1^2 - 12 (\theta _2 - \theta _1) - 12 \theta _2^2 < 0, \quad \text {if } \theta _1 < \theta _2\\
>    \mathrm{det}\nabla ^2 f_2(\theta _1, \theta _2) &= (12 \theta _1^2 + 6(\theta _2 - \theta _1))(12 \theta _2^2 + 6(\theta _2 - \theta _1)) - 36 (\theta _2 - \theta _1)^2\\
>    &= 144 \theta _1^2 \theta _2^2 + 72 (\theta _1^2 + \theta _2^2)(\theta _2 - \theta _1) > 0, \quad \text {if } \theta _1 < \theta _2.
>    \end{aligned}
>    $$
>    Combined, $f_2$ is concave on $\{\theta_1 < \theta_2\}$.

# 4. Maximum Likelihood Estimators

Compute the likelihood function and the maximum likelihood estimator for $\theta$ for

1. $f_\theta (x) = \sqrt{\theta }x^{\sqrt{\theta }-1} \mathbf{1}(0 < x < 1), \quad \theta >0$
2. $f_\theta (x)= \theta \tau x^{\tau -1} \exp \{ -\theta x^\tau \}  \mathbf{1}(x\geq 0), \quad \theta >0$

> **Solution:**
>
> 1. The likelihood function is
>    $$
>    L= \theta ^{n/2} \prod _ i{X_ i^{\sqrt{\theta }-1}} \mathbf{1}\{ 0 \leq X_ i \leq 1\} .
>    $$
>    The log-likelihood function is
>    $$
>    l= \frac{n}{2} \ln \theta + (\sqrt{\theta } -1) \sum _{i}{\ln X_ i}.
>    $$
>    Take the derivative with respect to $\theta$ and set it to $0$:
>    $$
>    \frac{\partial l}{\partial \theta }= \frac{n}{2\theta } + \frac{1}{2\theta ^{1/2}} \sum _ i{\ln X_ i}=0.
>    $$
>    Then we get
>    $$
>    \hat{\theta }=\frac{n^2}{(\sum {\ln X_ i})^2}.
>    $$
>
> 2. The likelihood function is
>    $$
>    L= \theta ^ n \tau ^ n \prod _ i{X_ i^{\tau -1}} \exp \{ -\theta \sum _ i{X_ i^\tau }\}  \mathbf{1} \{ X_ i\geq 0\}
>    $$
>    The log-likelihood function is
>    $$
>    l= n \ln \theta + n \ln \tau + (\tau -1) \sum _ i{\ln X_ i} - \theta \sum _ i{X_ i^\tau }.
>    $$
>    Take the derivative with respect to $\theta$ and set it to 0
>    $$
>    \frac{\partial l}{\partial \theta }= \frac{n}{\theta } - \sum _ i{X_ i^\tau }=0,
>    $$
>    We get
>    $$
>    \hat{\theta }=\frac{n}{\sum _ i{X_ i^\tau }}.
>    $$

# 5. Constrained Maximum Likelihood Estimator

Let $X_1 ,... ,X_n$ be $n$ i.i.d. random variables with probability density function
$$
f_\theta (x)= \theta x^{-\theta -1}, \quad \theta >0, \quad x \geq 1.
$$

1. What is the likelihood function for $\theta$?

2. What is the maximum likelihood estimator for $\theta$?

3. Suppose we have two numbers $0< a < b$. We are interested in the value of $\theta$ that maximizes the likelihood in the set $[a,b]$.

   Let $\hat{\theta}$ denote the maximum likelihood estimator you found in part (b) above, and let $\hat{\theta}_{const}$ denote the maximum likelihood estimator within the interval $[a,b]$, where $0 < a < b$. Choose the correct answer:

   a. If $b \leq \hat{\theta}$, then $\hat{\theta}_{const}=a$.

   b. If $b \leq \hat{\theta}$, then $\hat{\theta}_{const}=b$.

   c. If $b \leq \hat{\theta}$, then $\hat{\theta}_{const}=\hat{\theta}$.

   d. If $a < \hat{\theta} < b$, then $\hat{\theta}_{const}=a$.

   e. If $a < \hat{\theta} < b$, then $\hat{\theta}_{const}=b $.

   f. If $a < \hat{\theta} < b$, then $\hat{\theta}_{const}=\hat{\theta}$.

   g. If $a \geq \hat{\theta}$, then $\hat{\theta}_{const}=a$.

   h. If $a \geq \hat{\theta}$, then $\hat{\theta}_{const}=$b.

   i. If $a \geq \hat{\theta}$, then $\hat{\theta}_{const}=\hat{\theta}$.

> **Solution:**
>
> 1. The likelihood is
>    $$
>     L_ n  = \prod _{i=1}^{n}{\theta x_ i^{-\theta -1}} \mathbf{1}\{ {X_ i} \geq 1\}   =\theta ^ n \prod _{i=1}^{n}{x_ i^{-\theta -1}} \mathbf{1}\{ \min _ i{X_ i} \geq 1\}  
>    $$
>    Since we assume our statistical model to be well-specified, $\min _ i{X_ i} \geq 1$ will always be satisfied, and so we can drop the corresponding indicator function. Hence, $L_ n\, =\, \theta ^ n \prod _{i=1}^{n}{x_ i^{-\theta -1}}$ is correct under the well-specified assumption.
>
> 2. Take the derivative of the likelihood with respect to $\theta$.
>    $$
>    \frac{\partial L_ n}{\partial \theta } = \frac{n}{\theta }-\sum _{i=1}^{n} \ln X_ i = 0
>    $$
>    Solving the equation for $\theta$, we get
>    $$
>    \hat{\theta }=\frac{n}{\sum _{i=1}^{n}\ln X_ i}
>    $$
>
> 3. b,f,g.
>
>    Take the second derivative of the likelihood function with respect to $\theta$.
>    $$
>    \frac{\partial ^2 L_ n}{\partial \theta ^2} = -\frac{n}{\theta ^2} <0
>    $$
>    Since the second derivative is strictly less than $0$, the function is strictly concave with respect to $\theta$. Therefore, depending on the value of $\frac{n}{\sum _{i=1}^{n}\ln X_ i}$, which is the maximum, the largest value that likelihood function can take in the set $[a,b]$ changes.

