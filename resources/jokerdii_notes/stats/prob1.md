Problem set for Lec3-4.

# 1. Biased and unbiased estimation for variance of Bernoulli variables

Let $\,  X_1,\ldots ,X_ n \,$ be i.i.d. Bernoulli random variables, with unknown parameter $\,  p\in (0,1) \,$. The aim is to estimate the common variance of the $X_i$. Let $\overline{X}_n$ be the sample average of $X_i$. Recall the $\,  \textsf{Var}(X_ i) \,$ for Bernoulli random variables is 
$$
\,  \textsf{Var}(X_ i) \, = p(1-p)
$$
We are interested in finding an estimator for $\,  \textsf{Var}(X_ i) \,$ and propose to use 
$$
\hat V = \overline{X}_ n (1 - \overline{X}_ n).
$$
$\hat{V}$ is **consistent** because of the Law of Large Numbers (LLN) and Continuous Mapping Theorem (CMT).

Compute the bias of $\hat{V}$ and an unbiased estimator $\hat{V}'$.

> The bias of $\hat{V}$ is $\,   \mathbb E[\hat V] - \textsf{Var}(X_ i) $.
>
> First compute $\mathbb E[\hat V] $:
> $$
> \begin{aligned}
> \mathbb E[\overline{X}_ n(1-\overline{X}_ n)] &= \mathbb E[\overline{X}_ n] - \mathbb E[\overline{X}_ n^2],\\
> \mathbb E[\overline{X}_ n] &= \mathbb E\left[ \frac{1}{n} \sum _{i=1}^{n} X_ i \right] = \frac{1}{n} \sum _{i = 1}^{n} \mathbb E\left[ X_ i \right] = {}p\\
> 
> \mathbb E[\overline{X}_ n^2] &=\textsf{Var}(X_ n) + \mathbb E[X_ n]^2\\
> &= \frac{1}{n^2} \sum _{i = 1}^{n} \textsf{Var}(X_ i) + p^2\\
> &= \frac{1}{n} p(1-p) + p^2\\
> \end{aligned}
> $$
>
> $$
> \implies \mathbb E[\hat V] =p - p^2 - \frac{1}{n}p(1-p) = \frac{n-1}{n}p(1-p)
> $$
>
> and therefore the bias is 
> $$
> \,   \mathbb E[\hat V] - \textsf{Var}(X_ i) =-\frac{1}{n}p(1-p)
> $$
> We can obtain an unbiased estimator if we compensate the multiplicative bias in $\hat{V}$, so
> $$
> \hat V' = \frac{n}{n-1} \overline{X}_ n (1 - \overline{X}_ n).
> $$

# 2. Estimation of an exponential parameter

Let $X_1,\ldots ,X_ n$ be i.i.d. $\mathsf{Exp}(\lambda)$ random variables ,where $\lambda $ is unknown. 

1. What is the **distribution** of $\min _{1\le i \le n} (X_ i)$? Write down the pdf $f_{\min}(x)$.
2. Use Q1 to give an **unbiased** estimator $\hat{θ}$ for $1/λ$.
3. What is the **variance** and **quadratic risk** of unbiased estimator $\hat{\theta}$ in the previous part?
4. Compute $\mathbf{P}\left( \frac{1}{\lambda } \geq \frac{ n \min _ i X_ i}{\ln (5)} \right)$. This computation allows us to compute a confidence interval. The interpretation is as follows: Let $\alpha$ be a value such that $1-\alpha = \mathbf{P}\left( \frac{1}{\lambda } \leq \frac{ n \min _ i (X_ i)}{\ln (5)} \right).$ Based on this setup, what is the corresponding, non-asymptotic, one-sided confidence interval at level $1-\alpha$ for $1/\lambda$ ?

> 1) The cdf of $X_i$ is 
> $$
> F_ X(x)=\int _{0}^ x \lambda e^{-\lambda t} dt= 1-e^{-\lambda x}
> $$
> The cdf of $\min_i(X_i)$:
> $$
> \begin{aligned}
> \mathbf{P}\left(\min _ i (X_ i)\leq t\right)\, &=\, 1-\mathbf{P}\left(\min _ i (X_ i)\geq t\right)\\
> &=1-\left(\mathbf{P}\left(X_1\geq t\right)\right)\left(\mathbf{P}\left(X_2\geq t\right)\right)\ldots \left(\mathbf{P}\left(X_ n\geq t\right)\right)\\
> &= 1-\left(1-F_ X(t)\right)^ n \\
> &=\, 1-e^{-n\lambda x}.
> \end{aligned}
> $$
> Differentiate w.r.t. $x$ to get the pdf of $\min_i(X_i)$
> $$
> f_{\min}(x)=(n\lambda ) e^{-(n\lambda ) x}
> $$
> That is, $\min_i(X_i)$ follows an exponential distribution with parameter $n\lambda$. 
>
> As a sanity check,
> $$
> \mathbb E\left[ \min _ i (X_ i) \right]\, =\, 1/(n\lambda )<\mathbb E\left[X_ i\right]=1/\lambda \quad \text{for } n > 1
> $$
> 2) Since $\mathbb E\left[ \min _ i (X_ i) \right]\, =\, 1/(n\lambda )$, we have $\mathbb E\left[ n\min _ i (X_ i) \right]\, =\, 1/(\lambda )$. Therefore, $n \min_i(X_i)$ is an unbiased estimator of $1/\lambda$. The unbiased estimator $\hat{\theta} = n \min_i(X_i)$.
>
> 3) $ \textsf{Var}\left(n \min _ i(X_ i)\right) = n^2\textsf{Var}\left(\min _ i(X_ i)\right)\, =\, \frac{n^2}{n^2\lambda ^2}=\frac{1}{\lambda ^2}$
>
> $\text {Quadratic risk}\left(n \min _ i(X_ i)\right) = \left[\text {bias}\left(n \min _ i(X_ i)\right) \right]^2+\textsf{Var}\left(n \min _ i(X_ i)\right)=0+\, \frac{1}{\lambda ^2}\, =\, \frac{1}{\lambda ^2}$
>
> Note that the variance and quadratic risk of this estimator stay constant as $n \rightarrow \infty$
>
> 4) $ \mathbf{P}\left( \frac{1}{\lambda } \geq \frac{ n \min _ i X_ i}{\ln (5)} \right) = 4/5$
> $$
> \frac{1}{\lambda } \geq \frac{ n \min _ i X_ i}{\ln (5)} \Longleftrightarrow\min _ i X_ i\leq \frac{\ln (5)}{n\lambda }
> $$
> Hence,
> $$
> \begin{aligned}
> \mathbf{P}\left( \frac{1}{\lambda } \geq \frac{ n \min _ i X_ i}{\ln (5)} \right) &= \mathbf{P}\left(\min _ i X_ i\leq \frac{\ln (5)}{n\lambda }\right)\\
> &=1-e^{-n\lambda \left(\frac{\ln (5)}{n\lambda }\right)}\, =\, \frac{4}{5} =0.8
> \end{aligned}
> $$
> Note that when the event $\frac{1}{\lambda } \leq \frac{n \min _ i X_ i }{ \ln (5) }$ occurs, ${1\over \lambda}$ lies in the interval $\left[0,\frac{n \min _ i X_ i }{ \ln (5) }\right]$. Thus, the corresponding confidence interval at level $20\%$ is $\left[0,\frac{n \min _ i X_ i }{ \ln (5) }\right]$.

# 3. A confidence interval for Poisson variables

Let $X_1, ..., X_n$ be i.i.d. **Poisson** random variables with parameter $\lambda > 0$ and denote by $\overline{X}_n$ their empirical average,
$$
\overline{X}_ n=\frac{1}{n}\sum _{i=1}^ n X_ i.
$$

1. Find two sequences $(a_n)_{n \geq 1}$ and $(b_n)_{n \geq 1}$ such that $a_n(\overline{X}_n - b_n)$ converges in distribution to a standard Gaussian random variable $Z \sim \mathcal{N}(0,1)$.

2. Express $\,   \mathbf{P}(|Z| \leq t)  \,$ in terms of $\,   \Phi (r) = \mathbf{P}(Z \leq r)  \,$ for $t >0$.

3. Find an interval $\mathcal{I}_\lambda$ that depends on $\lambda$ and that is centered around $\overline{X}_n$ such that 
   $$
   \mathbf{P}[\mathcal{I}_{\lambda }\ni \lambda ]\to .95, \quad n \to \infty .
   $$
   (*Hint*: The $97.5\%$-quantile of the standard Gaussian distribution is $1.96$.)

4. Which of the following is a confidence interval $\mathcal{J}$ that fulfills
   $$
   \mathbf{P}[\mathcal{J}\ni \lambda ]\to .95, \quad n \to \infty .
   $$

> 1) To apply **CLT**, we need to know the mean and variance.
> $$
> \mathbb E[X_ i] = \lambda , \quad \textsf{Var}(X_ i) = \lambda .
> $$
> To make $a_n(\overline{X}_n - b_n)$ converge in distribution to a standard Gaussian random variable, we have
> $$
> \sqrt{\frac{n}{\lambda }} \left(\frac{1}{n} \sum _{i=1}^{n} X_ i - \lambda \right) \xrightarrow {(d)} Z \sim \mathcal{N}(0,1).
> $$
> Therefore,
> $$
> a_ n = \sqrt{\frac{n}{\lambda }}, \quad b_ n = \lambda .
> $$
> 2) We should first observe that by substitution in the **Gaussian integral** and **symmetry**.
> $$
> \begin{aligned}
> \mathbf{P}(Z \geq -t) &=\frac{1}{\sqrt{2 \pi }} \int _{-t}^{\infty } \exp \left(-\frac{x^2}{2}\right) \, dx\\
> &=\frac{1}{\sqrt{2 \pi }} \int _{-\infty }^{t} \exp \left(-\frac{(-x)^2}{2}\right) \, dx\\
> &= \frac{1}{\sqrt{2 \pi }} \int _{-\infty }^{t} \exp \left(-\frac{x^2}{2}\right) \, dx =\mathbf{P}(Z \leq t).
> \end{aligned}
> $$
>  Then, apply this to write 
> $$
> \begin{aligned}
> \mathbf{P}(|Z| \leq t) &=\mathbf{P}(-t \leq Z \leq t)\\
>  &= \mathbf{P}(Z \leq t) - \mathbf{P}(Z \leq -t)\\
>  &=\mathbf{P}(Z \leq t) - (1 - \mathbf{P}(Z \geq -t))\\
>  &=\mathbf{P}(Z \leq t) - 1 + \mathbf{P}(Z \leq t)\\
>  &=2 \Phi (t) - 1.
> \end{aligned}
> $$
> 3) By setting
> $$
> q = \Phi ^{-1}(0.975) = 1.96,
> $$
> we see that
> $$
> \mathbf{P}\left(\sqrt{\frac{n}{\lambda }} (\overline{X}_ n - \lambda ) \in [-q, q] \right) \to \mathbf{P}(Z \in [-q, q]) = 2 \Phi (q) - 1 = 2 \times 0.975 - 1 = 0.95.
> $$
> Hence we have
> $$
> \mathcal{I}_{\lambda } := \left[ \overline{X}_ n - 1.96 \sqrt{\frac{\lambda }{n}}, \overline{X}_ n + 1.96 \sqrt{\frac{\lambda }{n}} \right],
> $$
> where $\mathcal{I}_\lambda$ is centered about $\overline{X}_n$ and $\mathbf{P}( \lambda \in \mathcal{I}_{\lambda } ) \to 0.95$ as desired.
>
> 4)  $\overline{X}_n$ is a **consistent** estimator of $\lambda$ by the **LLN**, so $\,   \sqrt{\frac{n}{\overline{X}_ n}}(\overline{X}_ n - \lambda ) \to Z \sim \mathcal{N}(0,1) \,$ by **Slutsky's** Theorem. Hence, we can obtain an interval that does not depend on $\lambda$ as
> $$
> \,   \mathcal{J}= [\overline{X}_ n - 1.96 \sqrt{\overline{X}_ n/n},\,  \overline{X}_ n + 1.96 \sqrt{\overline{X}_ n/n}]  \,
> $$

# 5. A confidence interval for uniform distributions

Let $\,  X_1,\ldots ,X_ n \,$ be i.i.d. uniform random variables in $[0,\theta]$, for some $\theta >0$. Denote by
$$
M_ n=\max _{i=1,\ldots ,n} X_ i.
$$

1. Compute the following probabilities: 

   $\,   \mathbf{P}(M_ n \geq \theta ) $ 

   For all $0 \leq t\leq \theta: \,   \mathbf{P}(M_ n \leq \theta - t) $

2. Compute the cdf $F_n(t)$ of $n(1-M_n/\theta)$ for fixed $t \in [0,n]$ and any positive integer $n$. Then compute the limit of the cdf. $\lim_{n \rightarrow \infty} F_n(t)$.

3. Find an interval $\mathcal{I}$ of the form $\,  \mathcal I=[M_ n,M_ n+c] \,$, that does not depend on $\theta$ and such that
   $$
   \mathbf{P}[\mathcal I\ni \theta ]\to .95, \text { as } n \to \infty .
   $$
   The strategy now is to use a plug-in estimator for $\theta$ to replace it in the expression for $c$. Q1-2 suggest that we use $c$ of the form $\left(\frac{t}{n}\right) M_ n$, where $t$ ought to equal a certain value in order for $\mathbf{P}[\mathcal I\ni \theta ]\to .95$. What is the appropriate numerical value of $t$? Why can we use a plugin-estimator for the asymptotic confidence interval?

4. Compute the bias of $M_n$ as an estimator of $\theta$: $\mathbb E[M_ n] - \theta$.

> 1) Since all $X_ n \leq \theta$ almost surely, $M_ n \leq \theta $ almost surely, so
> $$
> \,   \mathbf{P}(M_ n \geq \theta )  = 0
> $$
> Let $0 \leq t\leq \theta$. Since having an upper bound on the maximum of $n$ variables $M_n$ is the same as having an upper bound on all of the variables, and the $X_i$ are independent, we can write
> $$
> \begin{aligned}
> \mathbf{P}(M_ n \leq \theta - t) &= \mathbf{P}(X_ i \leq \theta - t \text { for all } i = 1,\dots ,n)\\
> &=\prod^n_{i=1} \mathbf{P}(X_i \leq \theta-t) \quad \text{by independence}\\
> &= \left(\mathbf{P}(X_1 \leq \theta-t)\right)^n \quad \text{all }X_i \text{ have the same distribution}\\
> &=\left( {\theta - t \over \theta} \right)^n \quad \text{cdf of Uniform distribution}\\
> &=\left( {\theta - t \over \theta} \right)^n \xrightarrow[n \rightarrow \infty]{} 0
> \end{aligned}
> $$
> Hence,
> $$
> M_ n \xrightarrow {\mathbf{P}} \theta .
> $$
> 2) Let $t > 0$ and first we can write 
> $$
> n \left( 1 - \frac{M_ n}{\theta } \right) \leq t \iff M_ n \geq \theta - \theta \frac{t}{n}.
> $$
> For $n$ large enough, $t/n \leq 1$. Together with the fact that the cdf of $M_n$ does not have atoms, we can compute the cdf and its limit:
> $$
> \begin{aligned}
> \mathbf{P}\left( n \left( 1 - \frac{M_ n}{\theta } \right) \leq t \right) &=  \mathbf{P}\left( M_ n \geq \theta - \theta \frac{t}{n} \right)\\
> &=1 - \mathbf{P}\left( M_ n \leq \theta - \theta \frac{t}{n} \right)\\
> &=1 - \left( 1 - \frac{t}{n} \right)^ n \quad \text{by Q1}\\
> &\xrightarrow [n \to \infty ]{} 1- \exp(-t).
> \end{aligned}
> $$
> To obtain the limit, we used the limit formula for the **exponential**,
> $$
> \left( 1 + \frac{a}{n} \right)^ n \xrightarrow [n \to \infty ]{} \exp (a), \quad \text {for } a \in \mathbb {R}.
> $$
> Therefore, $n(1-M_ n/\theta )$ converges to an **exponential** random variable with parameter $\lambda = 1$.
> $$
> n(1-M_ n/\theta ) \xrightarrow [n \to \infty ]{\text {(D)}} \mathrm{Exp}(1),
> $$
> 3) Since we want $0.95 = 1 - \exp(-t)$, we have $t = \log(20).$
>
> From Q2 for any $t > 0$ we have that
> $$
> \mathbf{P}\left(\theta \geq M_ n + \theta \frac{t}{n}\right) \xrightarrow [n \to \infty ]{} \exp (-t)
> $$
> From Q1 we know that
> $$
> M_ n \xrightarrow {\mathbf{P}} \theta
> $$
> which is a constant. By **Slutsky's** Theorem, we can substitute $M_n$ for $\theta$ above to obtain
> $$
> \mathbf{P}\left(\theta \geq M_ n + M_ n \frac{t}{n}\right) \xrightarrow [n \to \infty ]{} \exp (-t).
> $$
> Plug in $t = \log(20)$ and we obtain
> $$
> \mathcal{I}= \left[ M_ n, M_ n + M_ n \frac{\log (20)}{n} \right]
> $$
> With this, we obtain
> $$
> \begin{aligned}
> \mathbf{P}(\mathcal{I}\ni \theta ) &= 1 - \underbrace{\mathbf{P}(\theta \leq M_ n)}_{= 0} - \mathbf{P}\left(\theta \geq M_ n + M_ n \frac{\log (20)}{n}\right)\\
> &\to 1 - \exp (-\log (20)) = 0.95.
> \end{aligned}
> $$
> 4) From Q1 we know that for $r \in [0,\theta]$,
> $$
> \mathbf{P}\left( M_ n \leq r \right) = \left( 1 - \frac{\theta - r}{\theta } \right)^ n = \left( \frac{r}{\theta } \right)^ n,
> $$
> and that the support of $M_n$ is $[0,\theta]$. Hence, the density $f_n$ of $M_n$ is 
> $$
> f_ n(r) = \left\{  \begin{aligned}  0, \quad &  r < 0 \text { or } r > \theta \\ \frac{1}{\theta } n \left( \frac{r}{\theta } \right)^{n-1}, \quad &  0 \leq r \leq \theta \\ \end{aligned} \right.
> $$
> Therefore, we can compute its expectation,
> $$
> \begin{aligned}
> \mathbb E[M_ n] &=  \int _{0}^{\theta } \frac{nr}{\theta } \left( \frac{r}{\theta } \right)^{n-1} \,  d r\\
> &= \frac{n}{(n+1)\theta ^ n} \left. r^{n+1} \right|_{0}^{\theta } = \frac{n}{n+1} \theta .
> \end{aligned}
> $$
> That means that the bias of $M_n$ is 
> $$
> \mathbb E[M_ n] - \theta = - \frac{1}{n+1} \theta .
> $$
> If we wanted, we could therefore obtain an unbiased estimator $\,   \tilde M_ n  \,$ by setting
> $$
> \tilde M_ n = \frac{n+1}{n} M_ n.
> $$

# 6. Modes of convergence

For $n \geq 2$, let $X_n$ be a random variable such that ${\mathbf{P}\left(X_ n=\frac{1}{n}\right)=1-\frac{1}{n^2}}$ and ${\mathbf{P}\left(X_ n=n\right)=\frac{1}{n^2}}$. 

1. Does $X_n$ converge in probability? $X_ n \xrightarrow [n\longrightarrow \infty ]{\mathbf{P}} ?$

2. Compute $ \lim _{n\to \infty }\mathbb E\left[X_ n\right]$ and $\lim _{n\to \infty } \textsf{Var}\left(X_ n\right)$.

> 1) $X_ n \xrightarrow [n\longrightarrow \infty ]{\mathbf{P}} 0$ in probability: It is enough to check that for every $\epsilon > 0, \mathbf{P}(|X_ n| \leq \varepsilon ) \to 1$ as $n \rightarrow \infty$, which is true since
> $$
> \begin{aligned}
> \mathbf{P}(|X_ n| \leq \varepsilon ) &= \mathbf{P}(X_ n = 1/n) \quad\text {if } n > \frac{1}{\varepsilon }\\
> &=1 - \frac{1}{n^2} \to 1 \quad \quad \text{as }n \rightarrow \infty
> \end{aligned}
> $$
> 2) The mean and its limit is
> $$
> \mathbb E\left[X_ n\right] =\frac{1}{n} \left( 1 - \frac{1}{n^2} \right) + \frac{n}{n^2} \xrightarrow {n\to \infty } 0.
> $$
> The variance and its limit is 
> $$
> \textsf{Var}\left(X_ n\right)\, =\,  \mathbb E\left[|X_ n|^2\right] = \left(\frac{1}{n}\right)^2 \left( 1 - \frac{1}{n^2} \right) + \frac{n^2}{n^2} \xrightarrow {n\to \infty } 1.
> $$
> **Remark:** Convergence in probability does not necessarily imply convergence in variance.

Let $X_n$ and $Y_n$ be two sequences of random variables. For each of the following statement, say whether it is true or false. When your answer is "false", try to think of a counter example.

1. If $\,  X_ n\xrightarrow [n\to \infty ]{\text{a.s.}} X \,$ and $\,  Y_ n\xrightarrow [n\to \infty ]{\text{a.s.}} Y \,$, then $\,  X_ n+Y_ n\xrightarrow [n\to \infty ]{\text{a.s.}} X+Y \,$
2. If $\,  X_ n\xrightarrow [n\to \infty ]{\mathbf{P}} X \,$ and $\,  Y_ n\xrightarrow [n\to \infty ]{\mathbf{P}} Y \,$, then $\,  X_ n+Y_ n\xrightarrow [n\to \infty ]{\mathbf{P}} X+Y \,$
3. If $\,  X_ n\xrightarrow [n\to \infty ]{(d)} X \,$ and $\,  Y_ n\xrightarrow [n\to \infty ]{(d)} Y \,$, then $\,  X_ n+Y_ n\xrightarrow [n\to \infty ]{(d)} X+Y \,$

> 1) True
>
> 2) True
>
> To show the convergence of $X_n + Y_n$ in probability, let $\epsilon, \delta > 0$. By definition of this mode of convergence, we can choose $n_1$ and $n_2$ such that 
> $$
> \mathbf{P}\left(| X_ n - X | > \frac{\varepsilon }{2} \right) <  \frac{\delta }{2} \quad \text {if } n \geq n_1 \\\mathbf{P}\left(| Y_ n - Y | > \frac{\varepsilon }{2} \right) < \frac{\delta }{2} \quad \text {if } n \geq n_2
> $$
> Hence, by triangle inequality and sub-additivity of $\mathbf{P}$, if $n \geq \max\{n_1, n_2\}$, we have
> $$
> \mathbf{P}\left( |X_ n + Y_ n - (X + Y)| > \varepsilon \right) \leq \mathbf{P}\left( |X_ n - X| > \frac{\varepsilon }{2} \right) + \mathbf{P}\left( |Y_ n - Y| > \frac{\varepsilon }{2} \right) < \frac{\delta }{2} + \frac{\delta }{2} = \delta ,
> $$
> which shows the desired convergence.
>
> 3) False
>
> The intuition is that random variables can be **coupled** in strange ways to make this statement false. 
>
> E.g. let $Z$ and $Z_1, Z_2, ...$ be a sequence of i.i.d. standard Gaussian RVs $\mathcal{N}(0,1)$. Using $(Z_n)$, we now define a pair of sequences $(X_n)$ and $(Y_n)$: let $X_n = Z_n$ and $Y_n = -Z_n$, let $X=Y=Z$. It is clear that $X_n \rightarrow Z$ in probability;and by symmetry of the Gaussian, $Y_n \rightarrow Z$ in probability as well. However, $X_n + Y_n = 0$, so the sequence $(X_n + Y_n)$ converges to the constant $0$ in probability.

# 7. Examples of convergence

**Rescaled Poisson RVs:**

For $m \leq 1$, let $X_n$ be a Poisson random variable with parameter $1/n$. Compute  $\mathbf{P}(X_n = 0)$. What can you conclude?

> The pmf of the Poisson random variable is given by
> $$
> \mathbf{P}(X=x, \lambda) = {\lambda^x \exp(-\lambda) \over x!}
> $$
> we compute
> $$
> \mathbf{P}(X_n = 0) = \left({1 \over n}\right)^0 {1 \over 0!}\exp\left( - {1 \over n}\right) = \exp\left(-{1\over n}\right)
> $$
> As $n \rightarrow \infty$, $\exp\left(-{1\over n}\right)$ tends to $1$, therefore $X_n \rightarrow 0$ in probability. 
>
> Moreover, the same calculation tells us the probability $\mathbf{P}(nX_n = 0)$, therefore we also obtain $nX_n \rightarrow 0$ in probability.
>
> However, $\mathbb{E}\left[(xX_n)^2\right]$ does not go to zero.
> $$
> \mathbb E[(n X_ n)^2] = n^2 \mathbb E[X_ n^2]  = n^2 \left(\mathsf{Var}(X_n) + (\mathbb{E}(X_n))^2\right)\\
> = n^2 \left( \frac{1}{n}+ \frac{1}{n^2} \right) = n +1 \to \infty .
> $$
> We can conclude that $X_n \rightarrow 0$ and $nX_n \rightarrow 0$ in probability, but $\mathbb{E}\left[(xX_n)^2\right]$ does not converge.
>
> **Remark**: $nX_n$ does NOT "**converge in $L^2$- norm**". 
>
> A sequence of random variable $(Y_n)_{n \geq 1}$ converges in $L^2$-norm to a random variable $Y$, denoted by $\, Y_ n\xrightarrow [n\to \infty ]{L^2}Y,\,$ if $\,  \lim _{n\to \infty } \, \mathbb E\left[\mid Y_ n-Y\mid ^2\right]=0.\, \,$ Moreover, if $\, Y_ n\xrightarrow [n\to \infty ]{L^2} Y,\,$ then $\,  \lim _{n\to \infty } \, \mathbb E\left[\mid Y_ n\mid ^2\right]= \mathbb E[Y^2].\, \,$ Hence, in this example, since $\, \mathbb E[(n X_ n)^2]\, \xrightarrow [n\to \infty ]{} \infty ,\,$ $nX_n$ does not converge in $L^2$-norm.

**Limit of rescaled Binomials:**

Let $X_n$ be a binomial random variable with parameters $n$ and $p=\lambda/n$, where $\lambda$ is a fixed positive number. 

Let $k \in \N$ be fixed. As $n \rightarrow \infty$, the pmf $\mathbf{P}(X_n=k)$ converges to a number that only depends on $\lambda$ and $k$. What is the limit: $\,  \lim _{n \to \infty } \mathbf{P}(X_ n = k) \,$ ? 

> This pmf of the Binomial random variable $X_n$ is given by
> $$
> \mathbf{P}(X_ n = k) = {n \choose k} \left( \frac{\lambda }{n} \right)^{k} \left( 1 - \frac{\lambda }{n} \right)^{n-k}, \quad 0 \leq k \leq n, k \in \N
> $$
> Write the binomial coefficient as
> $$
> {n \choose k} = \frac{1}{k!} \frac{n!}{(n-k)!},
> $$
> We have
> $$
> \mathbf{P}(X_ n = k) = \frac{\lambda ^ k}{k!} \underbrace{\left( 1 - \frac{\lambda }{n} \right)^ n}_{=:A_ n} \underbrace{\left( 1 - \frac{\lambda }{n} \right)^{-k}}_{=:B_ n} \underbrace{\frac{n!}{n^ k (n-k)!}}_{=:C_ n}.
> $$
> Term $A_n$ can be handled by the exponential formula
> $$
> \left(1 + \frac{a}{n}\right)^ n \xrightarrow [n \to \infty ]{} \exp (a), \quad \text {for } a \in \mathbb {R}.
> $$
> Hence,
> $$
> A_ n \to \exp (-\lambda ), \quad \text {as } n \to \infty .
> $$
> Since $k$ is fixed and $\lambda/n \rightarrow 0$, we have $B_n \rightarrow 1$. Finally, write
> $$
> \begin{aligned}
> C_ n &= \frac{n!}{n^ k (n-k)!} = 1 \times \left( \frac{n-1}{n} \right) \times \dots \times \left( \frac{n - k + 1}{n} \right)\\
> &= 1 \times \left( 1 - \frac{1}{n} \right) \times \dots \times \left( 1 - \frac{k-1}{n} \right) \to 1, \quad \text {as } n \to \infty .
> \end{aligned}
> $$
> Combined, we get that
> $$
> \mathbf{P}(X_ n = k) \to \frac{\lambda ^ k}{k!} \exp (-\lambda ).
> $$
> Since that entails the convergence of the cumulative mass function,  $\,   \mathbf{P}(X_ n \leq m)  \,$ , for any $m \in \Z$ as well, we have just shown that $X_n$ converges in distribution to a Poisson distribution with parameter $\lambda$

