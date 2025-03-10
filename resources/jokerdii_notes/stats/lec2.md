# 2. Probability Redux

There are 8 topics and 14 exercises.

## 1. Two important probability tools

Averages of random variables: Laws of Large Numbers and Central Limit Theorem

Let $X, X_1, X_2, ..., X_n$ be i.i.d. random variables, with $\mu = \mathbb{E}[X]$ and $\sigma^2 = \rm{Var}[X]$.

* Laws (weak and strong) of large numbers (LLN):
  $$
  \overline X_ n:=\frac{1}{n}\sum _{i=1}^ n X_ i \xrightarrow [n\to \infty ]{\mathbf{P},\text{ a.s.}} \mu
  $$
  where the convergence is in probability (as denoted by $\mathbf{P}$ on the convergence arrow) and almost surely (as denoted by a.s. on the arrow) for the weak and strong laws respectively.

* Central limit theorem (CLT):
  $$
  \begin{aligned}
  \sqrt{n}\, \frac{\overline X_ n-\mu }{\sigma }&\xrightarrow [n\to \infty ]{(d)}\mathcal{N}(0,1)\quad  \text{or equivalently }\\
  \sqrt{n}\, \left(\overline X_ n-\mu \right)&\xrightarrow [n\to \infty ]{(d)}\mathcal{N}(0,{\sigma ^2})
  \end{aligned}
  $$
  where the convergence is in distribution, as denoted by ($d$) on top of the convergence arrow.

  or equivalently
  $$
  \frac{S_ n-n\mu }{\sqrt{n}\sigma }\xrightarrow [n\to \infty ]{(d)}\mathcal{N}(0,1)
  $$
  where $S_ n=\sum _{i=1}^{n} X_ i$ is the sum (not the average) of $X_i$.

> #### Exercise 1 
>
> Let $X_1, X_2,...,X_n$ be i.i.d. **standard normal random variables**. For a finite $n$, what is the distribution, mean, and variance?
> $$
> \overline{X}_ n=\frac{X_1+X_2+\cdots +X_ n}{n}
> $$
>
> **Solution**:
> 
> The sum of i.i.d. Gaussian random variables is also Gaussian, so $X_1+\cdots +X_ n \sim N(0,n)$. Multiplying by $1/n$, we get $\overline{X}_ n \sim N(0,1/n)$, as scaling a random variable with a constant $c$ scales its variance by $c^2$.
> 
> Therefore, $\overline{X}_ n$ is a Gaussian random variable with mean $0$ and variance $1/n$.

> #### Exercise 2
>
> Let $X_1, X_2,...,X_n$ be a sequence of i.i.d. random variables with $\mathbb{E}[X] = \mu$, and $\rm{Var}(X) = \sigma^2$. Assuming that $n$ is very large, according to the CLT, what is the best approximate characterization of the distribution of $\overline{X}_ n$?
>
> **Solution**:
>
> Given CLT $\sqrt{n}\, \frac{\bar X_ n-\mu }{\sigma } \xrightarrow [n\to \infty ]{(d)}\mathcal{N}(0,1)$, we can use **approximate normality** and get
>
>  $$
> \overline{X}_ n \approx N(\mu ,\sigma ^2/n)
>  $$

In practice, for $X_i \sim Ber(p_i), p_i = p \quad \forall_i$: 

* The LLN's tell us that $\bar{R}_n \xrightarrow[n \rightarrow \infty]{\mathbf{P},~a.s.}  p$.

* When the size $n$ of the experiment becomes large, $\bar{R}_n$ is a **consistent** estimator of $p$.

* The CLT refines this by quantifying *how good* this estimate is: for $n$ large enough the distribution of $\hat{p}$ is almost:
  $$
  \mathbf{P}(|\bar{R}_n - p| \geq \epsilon) \simeq \mathbf{P}(|\mathcal{N}(0, \frac{p(1-p)}{n})| > \epsilon), \quad n \geq 30
  $$

  $$
  \mathbf{P}(|\bar{R}_n - p| \geq 0.084) \simeq 5\%
  $$

  This means that 5% of the time the interval is bad. 

## 2. Hoeffding's Inequality

Used when $n$ is not large enough to apply CLT.

Let $n$ be a positive integer and $X_1,X_2,\ldots ,X_ n\stackrel{iid}{\sim }X$ such that $\mu = \mathbb{E}[X]$ and $\mathbf{P}(X \notin [a,b])=0$ ($a<b$ are given numbers). Then,
$$
\mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq \epsilon \right) \leq 2 \exp \left(-\frac{2n\epsilon ^2}{(b-a)^2}\right)\qquad \forall \epsilon >0.
$$
Unlike for the central limit theorem, here the **sample size** $n$ **does not need to be large**.

In practice, for $X_i \sim \rm{Ber}(p_i), p_i = p \quad \forall_i$: 

* Hoeffding's inequality tells us that
  $$
  \mathbf{P}(|\bar{R}_n - p| \geq 0.084) \leq 2 \exp\{\frac{-2.124(0.084)^2}{(1-0)^2}\} \leq 0.35
  $$
  This means that 35% of the time the interval is bad. So Hoeffding's inequality is more conservative.

* CLT is mostly used since people want to make more precise statements.

## 3. Probability review: Markov and Chebyshev inequalities

**Markov inequality**: 

For a random variable $X≥0$ with mean $μ>0$, and any number $t>0$:
$$
\mathbf{P}(X\geq t)\leq \frac{\mu }{t}.
$$
Note that the Markov inequality is restricted to **non-negative** random variables.

**Chebyshev inequality**: 

For a random variable $X$ with (finite) mean $μ$ and variance $σ^2$, and for any number $t>0$,
$$
\mathbf{P}\left(\left|X-\mu \right|\geq t\right)\leq \frac{\sigma ^2}{t^2}.
$$

> #### Exercise 3
>
> Let $X_1,X_2,\ldots ,X_ n\stackrel{iid}{\sim }\textsf{Unif}(0,b)$ be $n$ i.i.d. uniform random variables on the interval $[0,b]$ for some positive $b$. Suppose $n$ is small (i.e. $n < 30$) so that the CLT is not justified.
>
> Find an upper bound on the probability that the sample mean is “far away" from the expectation (the true mean) of $X$. More specifically, find the respective upper bounds given by the Chebyshev and Hoeffding inequalities on the following probability:
> $$
> \mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq c\frac{\sigma }{\sqrt{n}} \right)\qquad \text {where }\, \sigma ^2=\textsf{Var}{X_ i}
> $$
> for $c = 2$ and $c = 6$.
>
> **Answer**: 
>
> Using Chebyshev inequality: $\mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq {{2}}  \frac{\sigma }{\sqrt{n}} \right)\leq 1/4$
>
> Using Hoeffding inequality: $\mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq {{2}}  \frac{\sigma }{\sqrt{n}} \right)\leq 2 \times e^{-2/3}$ 
>
> **Solution**: 
>
> Chebyshev inequality gives 
> $$
> \mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq t \right) \leq \frac{\sigma^2/n}{t^2}
> $$
> The variance is 
> $$
> \rm{Var}(\bar{X}_n) = \frac{\sigma^2}{n}
> $$
> Substitute $t = c\frac{\sigma^2}{\sqrt{n}}$, we get
> $$
> \mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq c\frac{\sigma }{\sqrt{n}} \right)\leq \frac{1}{c^2}.
> $$
> Hoeffding inequality gives
> $$
> \mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq c \frac{\sigma }{\sqrt{n}} \right)  \leq 2 \exp \left(-2c^2 \frac{\sigma ^2}{b^2}\right)
> $$
> The variance for $X_i \sim \rm{Unif}(0,b)$ is 
> $$
> \sigma^2 = \frac{b^2}{12}
> $$
> Substitute $\epsilon =c\frac{\sigma }{\sqrt{n}}$ in Hoeffding's inequality
> $$
> \mathbf{P}\left(\left|\overline{X}_ n-\mathbb E[X]\right|\geq c \frac{\sigma }{\sqrt{n}} \right)  \leq 2 \exp \left(-2c^2 \frac{\sigma ^2}{b^2}\right) \leq 2 \exp \left(-2c^2 \frac{1}{12}\right)=2 \exp \left(-\frac{c^2}{6}\right)
> $$
> Plug in $c = 2$ and $c = 6$ to get the following numerical upper bounds
>
> |           | c=2                | c=6                   |
> | --------- | ------------------ | --------------------- |
> | Chebyshev | $1/4 = 0.25$       | $1/36 = 0.0278$       |
> | Hoeffding | $2e^{-4/6} =1.027$ | $2e^{-36/6} =0.00496$ |
>
> **Remark**:
>
> When $c$ is small, Chebyshev may give a better bound. But as $c$ increases, the bound given by Hoeffding decays exponentially in $c^2$ while the bound given by Chebysheve decays only by $1 \over c^ 2$.

## 4. Gaussian distribution

The **Gaussian distribution**:

* $X \sim \mathcal{N}(\mu, \sigma^2)$
* $\mathbb{E}[X] = \mu$
* $\rm{var}(X) = \sigma^2 > 0$

The **Gaussian density function (PDF)**:

$$
f_{\mu,\sigma^2}(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp (-\frac{(x-\mu)^2}{2 \sigma^2})
$$

* Tails decay very fast (like $\exp(- \frac{x^2}{2 \sigma^2})$): almost in finite interval

* No closed form for their **cumulative distribution function (CDF)**. (often use computers)
  $$
  \mathbf{P}(X \leq x) = F_{\mu,\sigma^2}(x) = \frac{1}{\sigma \sqrt{2 \pi}} \int^x_{-\infty} \exp(-\frac{(t-\mu)^2}{2\sigma^2}) \rm{dt}
  $$

> #### Exercise 4
>
> Let $X\sim \mathcal{N}\left(\mu ,\sigma ^2\right)$, i.e. the PDF of $X$ is 
> $$
> f_ X(x)=\frac{1}{\sigma \sqrt{2\pi }} \exp \left(-\frac{(x-\mu )^2}{2 \sigma ^2}\right).
> $$
> Let $Y = 2X$. Write down the PDF of the random variable $Y$. 
>
> **Answer**: 
>
> $f_ Y(y)=\frac{1}{2\sigma \sqrt{2\pi }} \exp \left(-\frac{(y-2\mu )^2}{2 \left(4\sigma ^2\right)}\right).$
>
> **Solution**: 
>
> Since $Y=2X \sim \mathcal{N}\left(2\mu , 4\sigma ^2\right)$, we have
> $$
> f_ Y(y)=\frac{1}{2\sigma \sqrt{2\pi }} \exp \left(-\frac{(y-2\mu )^2}{2 \left(4\sigma ^2\right)}\right).
> $$
> Alternative method:
>
> In general, for any continuous random variables $X$ and any continuous monotonous (i.e. always increasing or always decreasing) function $g$, such that $Y=g(X)$, the pdf of $Y$ is given by:
> $$
> f_Y(y)=\frac{f_ X(x)}{|g'(x)|}\qquad \text {where } x=g^{-1}(y).
> $$
> In this problem, $X\sim \mathcal{N}\left(\mu ,\sigma ^2\right), Y = g(X) = 2X$, and $g'(x) = 2$. Therefore, 
> $$
> \begin{aligned}
> f_ Y(y) &=\frac{f_ X\left(\frac{y}{2}\right)}{\left|g'\left(\frac{y}{2}\right)\right|}\\
> &=\frac{1}{g'(y/2) \sigma \sqrt{2\pi }} \exp \left(-\frac{(y/2-\mu )^2}{2 \sigma ^2}\right)\\
> &=\frac{1}{2 \sigma \sqrt{2\pi }} \exp \left(-\frac{\left((y-2\mu )/2\right)^2}{2\sigma ^2}\right)\\
> &=\frac{1}{2 \sigma \sqrt{2\pi }} \exp \left(-\frac{\left((y-2\mu )\right)^2}{2(4)\sigma ^2}\right)
> \end{aligned}
> $$
> and we recover the same answer as above.

> #### Exercise 5
>
> Let $X∼N(5,1)$ and $f_X(x)$ be its pdf. Sketch the cumulative distribution function (cdf) $Φ(x)=∫^x_{−∞}f_X(t)dt$ of $X$ by doing the following:
>
> ![gaussian-cdf](../assets/images/gaussian-cdf.png)

## 5. Properties of the Gaussian distribution

Gaussian family is invariant under affine transformation

* $X \sim \mathcal{N}(\mu, \sigma^2)$, then for any $a, b \in \R$,
  $$
  a \cdot X + b \sim \mathcal{N}(a\mu+b, a^2 \sigma^2)
  $$

* **Standardization** (a.k.a. Normalization / Z-score): If $X \sim \mathcal{N}(\mu,\sigma^2)$, then
  $$
  Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0,1)
  $$
  Useful to compute probabilities from CDF of $Z \sim \mathcal{N}(0,1)$:
  $$
  \mathbf{P}(u \leq X \leq v) = \mathbf{P}(\frac{u - \mu}{\sigma} \leq Z \leq \frac{v-\mu}{\sigma})
  $$

* **Symmetry**: If $X \sim \mathcal{N}(0, \sigma^2)$ then $-X \sim \mathcal{N}(0, \sigma^2): $ If $x > 0$
  $$
  \mathbf{P}(|X| > x) = \mathbf{P}(X > x) + \mathbf{P}(-X > x) = 2 \mathbf{P}(X > x)
  $$
  Note that here $x>0$.

> #### Exercise 6
>
> Let $X_1, X_2, \ldots ,X_ n\,$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2$. Denote the sample mean by $\overline{X}_ n= \frac{\sum _{i=1}^ n X_ i}{n}$.
>
> Assume that $n$ is large enough that the CLT holds. Find a random variable $Z$ with approximate distribution $\mathcal{N}(0,1)$.
>
> **Answer**: 
>
> $Z \sim \mathcal{N}(0,1)$ for $Z =\sqrt{n}\frac{\overline{X}_ n-\mu }{\sigma }.$
>
> **Solution**: 
>
> Compute the mean and variance of $\overline{X}_n$
> $$
> \mathbb E\left[\overline{X}_ n\right] =\mathbb E[X_ i]=\mu\\
>  \textsf{Var}\left(\overline{X}_ n\right) =\frac{\sum _{i=1}^ n \textsf{Var}[X_ i]}{n^2}\, =\, \frac{n\sigma ^2}{n^2}\, =\, \frac{\sigma ^2}{n}.
> $$
> Thus, standardize by defining
> $$
> Z = \frac{\overline{X}_ n-\mathbb E\left[\overline{X}_ n\right]}{\sqrt{\textsf{Var}\left(\overline{X}_ n\right)}}=\frac{\overline{X}_ n-\mu }{\sqrt{\sigma ^2/n}}=\sqrt{n}\frac{\overline{X}_ n-\mu }{\sigma }.
> $$
> By the CLT, $Z \sim \mathcal{N}(0,1)$.

> #### Exercise 7
>
> Let $X\sim \mathcal{N}(2,2),$ i.e. $X$ is a Gaussian variable with mean $\mu = 2$ and variance $\sigma^2 = 2$. Let $x > 0$.
>
> Write $\mathbf{P}(X \geq -x)$ in terms of the CDF $\Phi$ of the standard Gaussian variable with a positive argument $\Phi (g(x))$, where $g(x)$ is a function of $x$ which takes only **positive** values for $x>0$.
>
> **Answer**: $\mathbf{P}\left(X\geq -x\right)=\Phi \left(\frac{{{x+2}} }{\sqrt{2}}\right).$
>
> Standardizing $X \sim \mathcal{N}(2,2)$, we have $\frac{X-2}{\sqrt{2}}\sim \mathcal{N}(0,1)$. 
>
> **Solution**: 
> $$
> \begin{aligned}
> \mathbf{P}\left(X\geq -x\right) &=\mathbf{P}\left(\frac{X-2}{\sqrt{2}}\geq \frac{-x-2}{\sqrt{2}}\right)\\
> &=\mathbf{P}\left(\frac{X-2}{\sqrt{2}}{\color{blue}{\leq }}  \frac{{{x+2}} }{\sqrt{2}}\right) \quad \text{ by symmetry}\\
> &=\Phi \left(\frac{{{x+2}} }{\sqrt{2}}\right).
> \end{aligned}
> $$
> The expression $\Phi \left(\frac{{{-x-2}} }{\sqrt{2}}\right)$ gives the same value, but the argument is negative and so is not an accepted answer.

## 6. Gaussian Probability Tables and Quantiles

**Quantiles**: Let $\alpha$ in $(0,1)$, The quantile of order $1-\alpha$ of a random variable $X$ is the number $q_{\alpha}$ such that
$$
\mathbf{P}(X \leq q_{\alpha}) = 1-\alpha
$$
Let $F$ denote the CDF of $X$:

* $F(q_{\alpha}) = 1-\alpha$
* If $F$ is invertible, then $q_{\alpha} = F^{-1}(1-\alpha)$
* $\mathbf{P}(X > q_{\alpha}) = \alpha$
* If $X = Z \sim \mathcal{N}(0,1): \mathbf{P}(|X| > q_{\alpha/2}) = \alpha$

Some important quantiles of the $Z \sim \mathcal{N}(0,1)$ are:

| $\alpha$     | $2.5\%$ | $5\%$  | $10\%$ |
| ------------ | ------- | ------ | ------ |
| $q_{\alpha}$ | $1.96$  | $1.65$ | $1.28$ |

We get that $\mathbf{P}(|Z| > 1.96) = 5\%$.

> #### Exercise 8
>
> Graphed below is the pdf of the normal distribution with generic/unknown (but fixed) variance $σ^2$. If the total area of the two shaded regions is $0.03$, then what is $x$?
>
> ![gaussian_quantile](../assets/images/ex_gaussian_quantile.svg)
>
> **Answer**: $x = q_{\alpha} = q_{0.015}$.
>
> **Solution**: The total area of the two shaded regions equals $P(|X|≥x)=0.03$. By symmetry, the probability in the positive tail is $P(X≥x)=0.015$; hence $x=q_α$ with $α=0.015$.

> #### Exercise 9
>
> Which of the following is the correct ordering of the numbers $q_{0.05},2q_{0.5},q_{0.02}$, which are quantiles of a standard Gaussian variable?
>
> **Answer**: $2q_{0.5} < q_{0.05} < q_{0.02}$
>
> **Solution**: In general, the quantiles of any continuous random variable satisfies $q_{a}>q_{b}$ if $a < b$, since the definition of quantile $q_{\alpha}$ is $\mathbf{P}\left(X{{\geq }}  q_{\alpha }\right)=\alpha$. Note that $q_{0.5} = 0$.

> #### Exercise 10 
>
> The score distribution of the final exam in a data science course follows a normal distribution with mean 70 and standard deviation 10. According to this distribution, what score do you need to get in order to be at the 90th percentile of the class, that is, in order that 90% of all students in the class have a score less than or equal to your score?
>
> **Answer**: $82.82$
>
> **Solution**: 
>
> Given the final exam grade $X$ follows a normal distribution with $μ=70$ and $σ=10$, we can define a variable $Z=(X−70)/10$ that follows the standard normal distribution $N(0,1)$.
>
> $\mathbf{P}\left(Z\leq \frac{t-70}{10}\right) = 0.9 \quad \text {if and only if } \quad \frac{t-70}{10}=q_{0.1}=\Phi ^{-1}(0.9).$
>
> where $q_{0.1}=\Phi ^{-1}$ is the inverse of the cdf of the standard normal distribution. Since $\Phi^{-1}(0.9) = 1.282$ (by using `qnorm(0.9)` in R), we have
>
> $t = 1.282*10+70\, =\, 82.82.$

## 7. Modes of Convergence

### **Three types of convergence**: 

Suppose $(T_n)_{n \geq 1}$ is a sequence of random variables, $T$ is a random variables ($T$ may be deterministic). 

* Almost surely (a.s) convergence: [**Convergence almost surely (a.s)** is also known as **convergence with probability  (w.p.1)** and **strong convergence**.]
  $$
  T_n \xrightarrow[n \rightarrow \infty]{a.s.} T \quad \text{iff} \quad \mathbf{P}[\{w:T_n(w) \xrightarrow [n \rightarrow \infty]{}T(w) \}] = 1 \quad (\text{i.e. } \lim_{n \rightarrow \infty} T_n = T)
  $$

* Convergence in probability:
  $$
  T_n \xrightarrow[x\rightarrow \infty]{\mathbf{P}} T \quad \text{iff} \quad \mathbf{P}[|T_n - T| \geq \epsilon] \xrightarrow[n \rightarrow \infty]{} 0, \quad \forall \epsilon > 0 \quad (\text{i.e. } \lim_{n \rightarrow \infty} \mathbf{P}(|T_n - T| \geq \epsilon) =0)
  $$

* Convergence in distribution: [**Convergence in distribution** is also known as **convergence in law** and **weak convergence**.]
  $$
  T_n \xrightarrow[n \rightarrow \infty]{(d)} T \quad \text{iff} \quad \mathbb{E}[(f(T_n)] \xrightarrow[n \rightarrow \infty]{} \mathbb{E}[f(T)]
  $$
  for all continuous and bounded function $f$.

Properties:

* The following three types of convergence are from strong to weak

  * If $(T_n)_{n \geq 1}$ converges a.s., then it also converges in probability, and the two limits are equal a.s.
  * If $(T_n)_{n \geq 1}$ converges in probability, then it also converges in distribution.

* Convergence in distribution implies convergence of probabilities if the limit has a density (e.g. Gaussian)
  $$
  T_n \xrightarrow [n \rightarrow \infty]{(d)} T \implies \mathbf{P}(a \leq T_n \leq b) \xrightarrow[n \rightarrow \infty]{} \mathbf{P}(a \leq T \leq b)
  $$

### **Equivalent definition of convergence in distribution for real r.v.s**

**Convergence in distribution** is also known as **convergence in law** and **weak convergence**.

1. For all continuous and bounded function $f$
   $$
   T_ n\xrightarrow [n\longrightarrow \infty ]{(d)}T\hspace{3mm}\text{ iff }\hspace{3mm}\mathbb E[f(T_ n)]\xrightarrow [n\rightarrow \infty ]{}\mathbb E[f(T)]
   $$

2. For all $x∈R$ at which the CDF of $T$ is continuous,
   $$
   T_ n\xrightarrow [n\longrightarrow \infty ]{(d)}T \hspace{3mm}\text{ iff }\hspace{3mm} \mathbf{P}[T_ n\leq x]\xrightarrow [n\to \infty ]{}\mathbf{P}[T\leq x] \quad (\text{i.e. } F_{T_n}(x) \xrightarrow[n \rightarrow \infty]{} F_{T}(x))
   $$

> #### Exercise 11
>
> Let $\{X_1, X_2, ..., X_n\}$ be a sequence of r.v. such that $X_n \sim \rm{Ber}({1 \over n})$. What is the limit of the sequence $\mathbb{E}[\cos(X_n)]$ as $n$ tends to infinity?
>
> **Answer**:  1
>
> **Solution**: 
>
> $\mathbf{P}(\{X_n =1\})={1\over n} \xrightarrow[n \rightarrow \infty]{} 0 $, thus, $\{X_n\}$ converges in probability. The limit of $\{X_n\}$ (that is $X_n \xrightarrow[n \rightarrow \infty]{\mathbf{P}}X$) is $X = 0$.
>
> Since $\cos(x)$ is bounded and continuous, $\mathbb{E}[\cos(X_n)] \xrightarrow[n \rightarrow \infty]{}\mathbb{E}[\cos(0)] = 1$.

> #### Exercise 12
>
> Let $(T_n)_{n \geq 1} = T_1, T_2 ...$ be a sequence of r.v.s such that
> $$
> T_ n \sim \textsf{Unif}\left(5-\frac{1}{2n},5+\frac{1}{2n}\right).
> $$
> a) Given an arbitrary fixed number $0 < \delta < 1$, find the smallest number $N$ (in terms of $\delta$) such that $\mathbf{P}\left(\{ \left|T_ n-5\right|>\delta \} \right)=0$ whenever $n > N$. 
>
> b) What is the limit value of $\left(T_ n\right)_{n\geq 1}$?
>
> c) Let $F_n(t)$ be the cdf of $T_n$ and $F(t)$ be the cdf of the constant limit. For which values of $t$ does $\lim _{n\to \infty } F_ n(t)=F(t)$?
>
> **Answer**: 
>
> a) $N = {1 \over 2\delta}$ ;  b) $ \left(T_ n\right)_{n\geq 1}\stackrel{\mathbf{P}}{\longrightarrow } 5$ ; c) $t \neq 5$
>
> **Solution**:  
>
> a) $\frac{1}{2n}<\delta \implies N = {1 \over 2\delta}$
>
> b) By the definition of convergence in probability $T_ n \xrightarrow [n\to \infty ]{\mathbf{P}} 5.$
>
> c) The cdf of $F_n$ of $T_n$ is a piecewise linear function with value $0$ for all $t \leq 5 - {1 \over 2n}$, 1 for all $t\geq 5+\frac{1}{2n}$, and a line connecting the points $\left(t,F_ n(t)\right)= \left(5-\frac{1}{2n}, 0\right)$ and $\left(t,F_ n(t)\right)= \left(5+\frac{1}{2n}, 1\right)$ in the interval $5-\frac{1}{2n}\leq t\leq 5+\frac{1}{2n}$. In particular, $F_ n(5)=\frac{1}{2}$ for all $n$. On the other hand, the cdf $F$ of the constant 5 is $F(t)=0$ when $t < 5$, and $F(t)=1$ when $t \geq 5$. Therefore, $F_ n(t) \xrightarrow [n\to \infty ]{} F(t)$ for all $t \neq 5$.

> #### Exercise 13
>
> Let $(Y_n)_{n \geq 1}$ be a sequence of i.i.d. random variables with $Y_ n \sim \textsf{Unif}\left(0,1\right).$ Let $M_ n=\max (Y_1, Y_2,\ldots , Y_ n).$
>
> a) For any fixed number $0 < \delta < 1$, find $\mathbf{P}\left(\left|M_ n-1\right|>\delta \right)$.
>
> b) Does the sequence $(M_n)_{n \geq 1}$ converge in probability to a constant? If yes, enter the value of the constant limit.
>
> c) Find the CDF $F_{M_ n}(x)$ for $0 \leq x \leq 1$.
>
> **Answer**: 
>
> a) $\mathbf{P}\left(\left|M_ n-1\right|>\delta \right) = (1- \delta)^n$.
>
> b) $\left(M_ n\right)_{n\geq 1}\stackrel{\mathbf{P}}{\longrightarrow } 1$
>
> c) $F_{M_ n}(x) = \mathbf{P}(M_n \leq x) = x^n$
>
> **Solution**: 
>
> Since $M_n \leq 1$, 
> $$
> \begin{aligned}
> \mathbf{P}\left(\left| M_ n-1\right| \geq \delta \right) &=\mathbf{P}\left(1- M_ n \geq \delta \right)\\
> &=\mathbf{P}\left(M_ n\leq 1- \delta \right) \\
> &=\mathbf{P}\left(Y_1\leq 1- \delta \right)\mathbf{P}\left(Y_2\leq 1- \delta \right)\cdots \mathbf{P}\left(Y_ n\leq 1- \delta \right)\qquad \text {since }\, Y_ i \text { independent}\\
> &=\left(1- \delta \right)^ n\, \xrightarrow [n\to \infty ]{} 0\qquad \text {since }\, 0< (1-\delta )<1 .
> \end{aligned}
> $$
> Hence the sequence $(M_n)_{n \geq 1}$ converges in probability to the deterministic limit $M = 1$. This implies that is also converges in distribution to the same limit.
>
> The CDF is computed in the same way:
> $$
> F_{M_ n}(x)\, =\, \mathbf{P}(M_ n \leq x)\, =\,  \mathbf{P}(Y_1 \leq x) \cdots \mathbf{P}(Y_ n \leq x) \, = \, x^ n \qquad \text {for }0\leq x\leq 1.
> $$
> We already know that $ \left(M_ n\right)_{n\geq 1}$ converges in distribution to $M$; here we check directly through definition. As $n \rightarrow \infty$, $F_{M_n}(x)$ approaches the step function shown below. 
>
> ![u1s2_stepfunction](../assets/images/u1s2_stepfunction.svg)

**Exercise Remark**: In general, for a sequence $\left(T_ n\right)_{n\geq 1},\,$ if $\, \mathbb E[T_ n]\xrightarrow [n\to \infty ]{}\mu \,$ and $\, \textsf{Var}(T_ n)\xrightarrow [n\to \infty ]{} 0,\,$then $\, T_ n\xrightarrow [n\to \infty ]{\mathbf{P}}\mu .\, \,$ Both this problem and the previous one satisfy these conditions.

## 8. Operations on Sequences and Convergence

### Addition, Multiplication, Division for Convergence a.s. and in probability 

Assume
$$
{T_ n\xrightarrow [n\to \infty ]{\text{a.s.}/\mathbf{P}}T} \qquad \text {and}\qquad {U_ n\xrightarrow [n\to \infty ]{\text{a.s.}/\mathbf{P}}U}
$$
Then,

* ${T_ n+U_ n\xrightarrow [n\to \infty ]{\text{a.s.}/\mathbf{P}}T+U}$

* ${T_ nU_ n\xrightarrow [n\to \infty ]{\text{a.s.}/\mathbf{P}}TU}$

* If in addition, $U \neq 0$ a.s., then ${\frac{T_ n}{U_ n}\xrightarrow [n\to \infty ]{\text{a.s.}/\mathbf{P}}\frac{T}{U}}$

Note that these rules **do not** apply to convergence in distribution ($d$).

### Slutsky's theorem

For convergence in distribution, the Slutsky's Theorem will be our main tool.

Let $(T_n),(U_n)$ be two sequences of r.v., such that:

* $ T_ n\xrightarrow [n\to \infty ]{(d)}T$
* $ U_ n\xrightarrow [n\to \infty ]{\mathbf{P}}u$

where $T$ is a r.v. and $u$ is a given real number (deterministic limit $\mathbf{P}(U = u) = 1$). Then, 

* $ {T_ n+U_ n\xrightarrow [n\to \infty ]{(d)}T+u}$
* ${T_ nU_ n\xrightarrow [n\to \infty ]{(d)}Tu}$
* If in addition, $u\neq 0$, then ${\frac{T_ n}{U_ n}\xrightarrow [n\to \infty ]{(d)}\frac{T}{u}}$.

### Continuous Mapping Theorem

If $f$ is a **continuous** function:
$$
T_ n\xrightarrow [n\to \infty ]{\text{a.s.}/\mathbf{P}/(d)}T\hspace{3mm}\Rightarrow \hspace{3mm} f(T_ n)\xrightarrow [n\to \infty ]{{\text{a.s.}/\mathbf{P}/(d)}}f(T).
$$
**Example**: 

By LLN, $\bar{R}_n \xrightarrow[n \rightarrow \infty]{\mathbf{P},\,\,\, a.s.} p$. Therefore,
$$
f(\bar{R}_n) \xrightarrow[n \rightarrow \infty]{\mathbf{P}, \,\,a.s.} f(p) \quad \text{for any continuous }f
$$
(Only need $f$ to be continuous around $p: f(x) = 1/x$ works if $p > 0$)

We also have by CLT: $\sqrt{n }\frac{\bar{R}_n - p}{\sqrt{p(1-p)}} \xrightarrow[n \rightarrow \infty]{(d)} Z, Z \sim \mathcal{N}(0,1)$. So
$$
f(\sqrt{n} (\bar{R}_n - p))\xrightarrow[n \rightarrow \infty]{(d)} f(Y) \quad Y \sim \mathcal{N}(0,p(1-p))
$$
Note that not the limit of $\sqrt{n}[f(\bar{R}_n) - f(p)]$, which is what we usually need. To know $\sqrt{n}[f(\bar{R}_n) - f(p)]$ we resort to **Delta ($\Delta$) method**.

> #### Exercise 14
>
> Given the following:
>
> * $Z_1,Z_2,\ldots , Z_ n, \ldots$  is a sequence of random variables that converge in distribution to another random variable $Z$;
> * $Y_1,Y_2,\ldots , Y_ n, \ldots$  is a sequence of random variables each of which takes value in the interval $(0,1)$, and which converges in probability to a constant $c$ in $(0,1)$;
> * $f(x) = \sqrt{x(1-x)}$
>
> Does $Z_ n \frac{f(Y_ n)}{f(c)}$ converge in distribution? If yes, enter the limit.
>
> **Answer**: $Z_ n \frac{f(Y_ n)}{f(c)}\stackrel{\text {d}}{\longrightarrow } \quad Z$
>
> **Solution**: 
>
> Since $f$ is continuous in $(0,1), f(Y_n) $ converges in probability to $f(c)$ by the continuous mapping theorem. Since $f(c)$ is a constant, we have $\frac{f(Y_ n)}{f(c)}$ converges in probability to $1$. Finally, since $Z_n$ converges in distribution to $Z$ and $\frac{f(Y_ n)}{f(c)}$ converges in probability to a constant, by Slutsky's Theorem, $Z_n \frac{f(Y_ n)}{f(c)}$ converges in distribution to $Z$.

