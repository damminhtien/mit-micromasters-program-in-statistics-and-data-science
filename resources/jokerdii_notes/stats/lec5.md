# Lecture 5. Confidence Intervals and the Delta Method

There are 5 topics and 6 exercises.

## 1. Confidence Intervals Concept Check

Let $X_1, ... X_n \stackrel{iid}{\sim} P_\theta$, where $\theta$ is an unknown parameter. You construct a C.I. $\mathcal{I}=\left[ L(X_1, ..., X_n), U(X_1, ..., X_n)\right]$ for $\theta$. The C.I. $\mathcal{I}$ is a **random object** (not deterministic). As defined, a C.I. $\mathcal{I} = [L,U]$ for an unknown parameter $\theta$ is a **random interval** such that the expressions for its endpoints $L, U$ do not depend on $\theta$.

$L$ and $U$ are functions of the random sample that do not depend on $\theta$. In practice, one uses data (e.g. realizations $x_1, ..., x_n$ of the i.i.d. observations $X_1, ..., X_n$) to compute the realization $\mathcal{I}_\text{real}$ of the C.I. $\mathcal{I}$:
$$
\mathcal{I}_{\text {real}} := [L(x_1, \ldots , x_ n), U(x_1, \ldots , x_ n)].
$$
Note that it is important to distinguish the **random variable** $\mathcal{I}$ (C.I.) from its **realization** $\mathcal{I}_\text{real}$, which can be formed only after collecting data.

> ####  Exercise 27
>
> Let $I, J$ be some $95\%$ and $98\%$ asymptotic C.I.s (respectively) for $p$. Which one is correct? 
>
> a. We always have $I \subset J$ ; Any realization of $\mathcal{I}$ is a subinterval of any realization of $\mathcal{J}$.
>
> b. We always have $J \subset I$; Any realization of $\mathcal{J}$ is a subinterval of any realization of $\mathcal{I}$.
>
> c. None of the above.
>
> Find a $98\%$ asymptotic C.I. for $p$.
>
> **Answer**: C
>
> **Solution**: 
>
> The $98\%$ C.I. is not necessarily bigger than $95\%$ one. And those two C.I.s can be calculated by two different techniques. Moreover, with the same confidence level, the centered data have the narrowest C.I., any deviation from the center will strictly give wider C.I.
>
> Find a $98\%$ asymptotic C.I. for $p$.
> $$
> 1-\alpha = 0.98 \text{ C.I.}, \quad \overline{R}_n \pm {q_{\alpha/2} \over 2 \sqrt{n}}, \quad q_{1\%}
> $$
> The C.I. becomes larger when the confidence level increases.

> #### Exercise 28
>
> In a new experiment consisting of $150$ couples, $75$ couples are observed to turn their heads to the left and the remaining 75 couples turned their heads to the right when kissing. Let $p$ denote the (unknown) parameter which specifies the probability that a couple turns their head to the right. Which of the following is true?
>
> a. $[0,0.5]$ is a $50\%$ asymptotic C.I. for $p$.
>
> b. $[0.5,0]$ is a $50\%$ asymptotic C.I. for $p$.
>
> **Answer**: ab
>
> **Solution**:  Take option **a** for example:
>
> Let $R_1, R_2, \ldots , R_{150} \stackrel{iid}{\sim } \text {Ber}(p)$ denote the sampled response (without loss of generality, assume that $R_i=1$ encodes that the $i$-th couple turns their heads to the right, and $R_i=0$ encodes that the couple turns their heads to the left.) Let $P=\text{Ber}(p)$ denote the common distribution of $R_1, ...,R_{150}$.
>
> Consider the sample mean $\overline{R}_n$. By CLT,
> $$
> \sqrt{n} \left( \frac{\overline{R}_ n - p}{\sqrt{p(1-p)}} \right) \xrightarrow [(d)]{} N(0,1).
> $$
> Consider the interval $[0,0.5]$. Since $\overline{R}_n=0.5$, this interval is a realization of the (random) C.I. $\mathcal{I}=(0,\overline{R}_n)$. We compute that
> $$
> P( \mathcal{I} \ni p ) = P( p \leq \overline{R}_ n ) = P( \overline{R}_ n - p \geq 0 ) = P\left(\frac{\overline{R}_ n - p}{\sqrt{p(1-p)}} \geq 0 \right).
> $$
> This probability goes to $0.5$ as $n→∞$. Therefore, the realization $[0,0.5]$ of the random interval $[0,R_n]$ is an asymptotic C.I. of level $0.5$.
>
> **Remark**: Difference between **asymptotic and non-asymptotic C.I.**:
>
> *Non-asymptotic* C.I.s are those where the probability is exact; i.e. $P(I∋θ)≥1−α$, rather than $\lim_{n→∞}P(I∋θ)≥1−α$, where C.I.s are called *asymptotic* C.Is. In other words, for *non-asymptotic* C.I.s we're not using any techniques involving convergence of random variables (like Slutsky's theorem or the CLT).

> #### Exercise 29
>
> If $[0.34, 0.57]$ is a realization of a (non-asymptotic, for some fixed $n$) 95% C.I. for an unknown parameter $p$, then which of the following is true? 
>
> The probability that the unknown parameter $p$ is in this interval is 
>
> a. $\geq 0.95$
>
> b. None of the above, because $p$ and $[0.34, 0.57]$ are both deterministic.
>
> **Answer**: b
>
> **Solution**: 
>
> Given some unknown but fixed parameter $\theta \in \mathbb {R}$ for a parametric model and random variables $X_1, \ldots , X_ n$ distributed i.i.d. $P_\theta$ recall that the non-asymptotic $95\%$ C.I. of $p$ is an interval $\mathcal{I} = \mathcal{I}(X_1,\ldots ,X_ n)$ such that $\Pr (\mathcal{I} \ni \theta ) \geq 0.95$. It is important to note that there is **randomness** here, given by the randomness of $\mathcal{I}$. That is,
> $$
> \lim_{n \rightarrow \infty} \mathbb{P}\left( p \in \left[ \overline{R}_n \pm {q_{\alpha/2}\over 2\sqrt{n}}\right]\right) \geq 1-\alpha
> $$
> However, a **realization** of a random variable is *deterministic*. The interval $[0.34, 0.57]$ either contains the parameter $p$, or it doesn't. In other words, the expression $\Pr ([0.34,0.57] \ni p)$ is equal to $1$ or $0$. 

## 2. Modeling Inter-arrival Times of a Subway System

### Statistical Problem

The times (in minutes) between arrivals of the $T$ at Kendall are: $T_1,..., T_n$. Assume that these times are 1) mutually independent, 2) exponentially random variables with common parameter. Based on the observed arrival times, we want to estimate the value of $\lambda$.

* Mutual independence of $T_1,..., T_n$: plausible but not completely justified (often the case with independence).

* $T_1,..., T_n$ are exponential r.v. Exponential distribution is a very common distribution for inter-arrival times, mainly because it has **lack of memory** (*memorylessness*). 
  The memorylessness states that
  $$
  \mathbb{P}\left[ T_1 > t+s | T_1 > t \right] = \mathbb{P}\left[ T_1 > s\right], \quad \forall s,t \geq 0
  $$
  $T_i > 0$ almost surely.

  **Proof**:

  Assume $T \sim \mathsf{Exp}(\lambda)$, we want to know $\mathbb{P}[T>t+s | T>t]$:
  $$
  \begin{aligned} 
  \mathbb{P}[T>t+s | T>t]&= {\mathbb{P}(T > t+s,T>t) \over \mathbb{P}(T>t)}\\
  &={\mathbb{P}(T > t+s) \over \mathbb{P}(T>t)} \\
  &={\exp(-\lambda(t+s) )\over \exp(-\lambda t)}\\
  &=\exp(-\lambda s)\\
  &= \mathbb{P}[T>s]
  \end{aligned}
  $$

* The exponential distribution of $T_1,..., T_n$ have the same parameter: in average all the same inter-arrival time. True only for limited period.

> #### Exercise 30
>
> Let $X\sim \exp(1)$, what is $\mathbf{P}(X > 3)$? What is $\mathbf{P}\left( X > t + 3| X > t \right)$ if $t > 0$?
>
> **Answer**: Both $\exp(-3)$
>
> **Solution**: 
>
> The density of $\exp(1)$ is $\exp(-x)$, thus,
> $$
> \mathbf{P}(X > 3) = \left.\int _{3}^{\infty } \exp(-x) \,  dx = - \exp(-x) \right|_3^\infty = \exp(-3).
> $$
> By memoryless property,
> $$
> \mathbf{P}\left( X > t + 3| X > t \right) = \mathbf{P}(X > 3) = \exp(-3)
> $$

### Estimating the Parameter for an Exponential Model

The pdf of $T_1$ is
$$
f_{\lambda}(t)=\lambda e^{-\lambda t} \quad t >0
$$
The mean of $T_1$ is 
$$
\begin{aligned}
  \mathbb {E}[T_1] &= \int _{0}^\infty t \lambda e^{-\lambda t} \,  dt\\
  &= - t e^{-\lambda t} \bigg|_{0}^\infty + \int _{0}^\infty e^{-\lambda t} \,  dt\\
  &= 0 - \frac{1}{\lambda } e^{-\lambda t} \bigg|_{0}^\infty\\
  &= \frac{1}{\lambda }.
  \end{aligned}
$$
Hence, a natural estimate of ${1\over \lambda}$ is
$$
\bar{T}_n = {1\over n}\sum^n_{i=1}T_i
$$
A natural estimator of $\lambda$ is 
$$
\hat{\lambda} = {1 \over \bar{T}_n}
$$
This is a **consistent** estimator, because of 

* By the **LLN**:
  $$
  \bar{T}_n = {1\over n} \sum_{i=1}^n T_i \xrightarrow[n \rightarrow \infty]{a.s./\mathbf{P}} \mathbb{E}[T_i]={1\over \lambda}
  $$
  Hence,
  $$
  \hat{\lambda} \xrightarrow[n\rightarrow \infty]{a.s./\mathbf{P}} \lambda
  $$

* By the **CLT**,
  $$
  \sqrt{n}\left( \bar{T}_n - {1\over \lambda}\right) \xrightarrow[n\rightarrow \infty]{} \mathcal{N}(0, \lambda^{-2})
  $$
  Note that the **asymptotic variance** of what $\sqrt{n}\left( \bar{T}_n - {1\over \lambda}\right)$ converges to is calculated by
  $$
  \begin{aligned}
  \mathsf{Var}\sqrt{n}\left( \bar{T}_n - {1\over \lambda}\right) &= n\mathsf{Var}\left( \bar{T}_n - {1\over \lambda}\right)\\&= n\mathsf{Var}\left( \bar{T}_n\right)\\&= n\mathsf{Var}\left({1\over n}\sum_{i=1}^n T_i\right) \\&=n {1\over n^2} \left(\mathsf{Var}(T_1) +...+\mathsf{Var}(T_n) \right) \\&=\mathsf{Var}(X_i)\\&=  {1\over \lambda^2}
  \end{aligned}
  $$

* By the **continuous mapping theorem (CMT)**
  $$
  {1\over \overline{T_n}}\xrightarrow [n \to \infty ]{a.s/\mathbf{P}} {1\over \mathbb{E}[T_i]} = \lambda
  $$

> #### Exercise 31 Consistency and Biasedness
>
> Let $X_1, X_2, \ldots , X_ n \stackrel{iid}{\sim } \exp (\lambda )$. Let $\overline{X}_ n := \frac{1}{n} \sum _{i = 1}^ n X_ i$ denote the sample mean of the data set.
>
> 1.  $\overline{X}_n \xrightarrow[x \rightarrow \infty]{a.s./\mathbf{P}} ?$
> 2. ${1\over\overline{X}_n} \xrightarrow[x \rightarrow \infty]{a.s./\mathbf{P}} ?$
> 3. What is the bias of ${1 \over \overline{X}_n}$ as an estimator of $\lambda$?
> 4. Which are the properties of ${1\over \overline{X}_n}$ as an estimator of $\lambda$?
>
> **Solution**:
>
> 1. $\overline{X}_n \xrightarrow[x \rightarrow \infty]{a.s./\mathbf{P}} \mathbb{E}[X_i] \text{ or } \overline{X}_n \xrightarrow[x \rightarrow \infty]{a.s./\mathbf{P}} {1 \over \lambda}$
>
> By the (strong/weak) LLN,
> $$
> \overline{X}_n = \frac{\sum _{i = 1}^ n X_ i}{n}\xrightarrow [n \to \infty ]{a.s/\mathbf{P}}\mathbb E[X_ i]\, =\, \frac{1}{\lambda }.
> $$
>
> 2. ${1\over\overline{X}_n} \xrightarrow[x \rightarrow \infty]{a.s./\mathbf{P}}  \lambda \text{ or } {1\over\overline{X}_n} \xrightarrow[x \rightarrow \infty]{a.s./\mathbf{P}} \frac{1}{\mathbb E[X_ i]}$
>
> By the continuous mapping theorem (CMT),
> $$
> {1\over \overline{T_n}}\xrightarrow [n \to \infty ]{a.s/\mathbf{P}} {1\over \mathbb{E}[T_i]} = \lambda
> $$
> Thus, ${1\over \overline{T_n}}$ is a **consistent** estimator of $\lambda$.
>
> 3. $\mathbb E\left[\frac{1}{\overline{X}_ n}\right]-\lambda \text{ or } \mathbb E\left[\frac{1}{\overline{X}_ n}\right]-\frac{1}{\mathbb E[X_ i]} \text{ or } \mathbb E\left[\frac{1}{\overline{X}_ n}\right]-\frac{1}{\mathbb E[\overline{X}_ n]}$
>
> The bias of ${1 \over \overline{X}_n}$ as an estimator of $ \lambda =\frac{1}{\mathbb E[X_ i]}=\frac{1}{\mathbb E\left[\overline{X}_ n\right]}$ is 
> $$
> \text {Bias}=\mathbb E\left[\frac{1}{\overline{X}_ n}\right]-\frac{1}{\mathbb E\left[\overline{X}_ n\right]}.
> $$
>
> 4. Consistent by not unbiased.
>
> Note that
> $$
>  \mathbb E\left[\frac{1}{\overline{X}_ n}\right]\neq \frac{1}{\mathbb E\left[\overline{X}_ n\right]}\, =\, \lambda .
> $$
> Since the function ${1\over x}$ is convex (by the shape of its graph or by $\left(1\over x\right)'' = {2 \over x^3} > 0$), Jensen's inequality gives $\mathbb E\left[\frac{1}{\overline{X}_ n}\right]> \frac{1}{\mathbb E\left[\overline{X}_ n\right]}$ and hence the bias is greater than zero.

## 3. The One-Dimensional Delta Method

Let $(Z_n)_{n \geq 1}$ sequence of r.v. that satisfies
$$
\sqrt{n}(Z_n - \theta) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,\sigma^2)
$$
for some $\theta \in \R$ and $\sigma^2 > 0$ (the sequence $(Z_n)_{n \geq 1}$ is **asymptotically normal around** $\theta$)

Let $g: \R \rightarrow \R$ be continuously differentiable at the point $\theta$. Then

* $(g(Z_n))_{n \geq 1}$ is also **asymptotically normal around** $g(\theta)$.

* More precisely,
  $$
  \sqrt{n}(g(Z_n) - g(\theta)) \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}(0, (g'(\theta))^2 \sigma^2)
  $$

* Proof: Apply **Taylor theorem**
  $$
  \begin{aligned}
  g(Z_n) - g(\theta) &= (Z_n - \theta)g'(\theta) + {(Z_n-\theta)^2\over2 } g''(w), \quad \text{where }w \in [Z_n, \theta]\\
  &\simeq (Z_n - \theta) g'(\theta), \quad \text{since } (Z_n-\theta)^2 \approx {1\over n}\\
  \sqrt{n}(g(Z_n) - g(\theta))  &\simeq \sqrt{n}(Z_n - \theta) g'(\theta) \xrightarrow[n \rightarrow \infty]{} \mathcal{N}(0, g'(\theta)^2 \sigma^2), \quad \text{since }g'(\theta) \text{ is a deterministic number}
  \end{aligned}
  $$

> #### Exercise 32
>
> Let $(Z_ n)_{n \geq 1}$ be a sequence of random variables such that
> $$
> \sqrt{n}(Z_ n - \theta ) \xrightarrow [n \to \infty ]{(d)}Z
> $$
> for some $\theta \in \R$ and some random variable $Z$.
>
> Let $g(x) = 5x$ and define another sequence by $Y_n = g(Z_n)$.
>
> The sequence $\sqrt{n}(Y_ n - g(\theta ))$ converges. 
>
> 1. In terms of $Z$, what random variable $Y$ does it converge to?
>
> $$
> \sqrt{n}(Y_ n - g(\theta )) \xrightarrow [n \to \infty ]{(d)} \quad Y.
> $$
>
> 2. What theorem did we invoke to compute What theorem did we invoke to compute $Y$?
> 3. If $\mathsf{Var}(Z) = \sigma^2$, what is $\mathsf{Var}(Y)$? 
>
> **Answer**: 
>
> 1. $Y = 5Z$
> 2. Slutsky theorem or continuous mapping theorem
> 3. $\mathsf{Var}(Y) = 25 \sigma^2$.
>
> **Solution**: 
>
> 1. $$
>    \sqrt{n}( Y_ n - g(\theta ) ) \, =\,  \sqrt{n}(g(Z_ n) - g(\theta ) ) = \sqrt{n}(5Z_ n - 5\theta )=5 \left(\sqrt{n} (Z_ n-\theta )\right)\xrightarrow [n \to \infty ]{(d)} 5Z
>    $$
>
> 2. By the **continuous mapping theorem** because $\sqrt{n}(Z_ n - \theta ) \xrightarrow [n \to \infty ]{(d)}Z$ is a linear and hence continuous function of $Z_n$,
>    $$
>    5 \left(\sqrt{n} (Z_ n-\theta )\right)\xrightarrow [n \to \infty ]{(d)} 5Z
>    $$
>    Alternatively, since we were given that $\sqrt{n}(Z_ n - \theta ) \xrightarrow [n \to \infty ]{(d)}Z$, and $5$ converges trivially in probability to itself $5 \rightarrow 5$, we can also use **Slutsky theorem** to conclude.
>
> 3. The **asymptotic variance** of $(Y_ n)_{n \geq 1}$ is
>    $$
>    \textsf{Var}(Y)=25\textsf{Var}(Z)=25 \sigma ^2
>    $$

### Applying the Delta Method

We have
$$
\sqrt{n}(T_n - {1\over \lambda}) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,{1\over \lambda^2})
$$
Suppose $g(\theta) = {1\over \theta}$, then $g'(\theta) = -{1\over \theta^2}$. We first calculate $(g'(\theta))^2$:
$$
(g'(\theta))^2 = (g'({1\over \lambda}))^2 = \lambda^4
$$
Therefore, we obtain
$$
\sqrt{n}\left(\hat{\lambda} - \lambda\right) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,\lambda^2)
$$
Note: For the Delta method to apply, $g′$ exists and is continuous at $\mathbb{E}[X]=g^{−1}(θ)$. Since $θ$ and $μ=\mathbb{E}[X]$ are unknown, for the Delta method to apply, we need to make sure **$g$ is continuously differentiable at all possible values of $\mathbb{E}[X]$ given that $θ>0$.**

Hence, for $\alpha \in (0,1)$ and when $n$ is large enough,
$$
|\hat{\lambda}  - \lambda| \leq \lambda \cdot {q_{\alpha/2} \over \sqrt{n}}
$$
with probability approximately $1-\alpha$.

However, $\left[\hat{\lambda} - {q_{\alpha/2}\lambda\over \sqrt{n}}, \hat{\lambda} + {q_{\alpha/2}\lambda\over \sqrt{n}}\right]$ CAN'T be used as an asymptotic C.I. for $\lambda$, since the expression for the left and right endpoint depends on the true parameter $\lambda$. By definition, a C.I. must be computed only using the data and other known quantities, but not the true parameter, which is unknown.

**Three Solutions:**

1. The conservative bound: we have no a priori way to bound $\lambda$, since $\lambda$ is unbounded.

   We try to find the following defined C.I. using "conservative method",
   $$
   \mathcal{I}_{cons} := \left[ \widehat{\lambda }_ n - \max _{\lambda \in (0, \infty )} \frac{q_{\alpha /2} \lambda }{\sqrt{n}} , \widehat{\lambda }_ n + \max _{\lambda \in (0, \infty )} \frac{q_{\alpha /2} \lambda }{\sqrt{n}} \right].
   $$
   Since we observe that
   $$
   \max _{\lambda \in (0, \infty ) } \frac{q_{\alpha /2} \lambda }{\sqrt{n}} = \infty
   $$
   The C.I. is actually 
   $$
   \mathcal{I}_{cons} = (-\infty , \infty ).
   $$
   It is not useful for statistical purposes because such a confidence interval gives no information about the location of the true parameter.

2. We can solve for $\lambda$:
   $$
   \begin{aligned}
   |\hat{\lambda} - \lambda| \leq {q_{\alpha/2}\lambda \over \sqrt{n}} &\iff \lambda\left(1 - {q_{\alpha/2} \over \sqrt{n}}\right)\leq \hat{\lambda} \leq \lambda \left(1 + {q_{\alpha/2} \over \sqrt{n}}\right)\\
   &\iff {\hat{\lambda}\over1+{q_{\alpha/2} \over \sqrt{n}}} \leq \lambda \leq {\hat{\lambda}\over1-{q_{\alpha/2} \over \sqrt{n}}}
   \end{aligned}
   $$
   It yields
   $$
   \mathcal{I}_{\text{solve}} = \left[\hat{\lambda}\left( 1+{q_{\alpha/2} \over \sqrt{n}}\right)^{-1},\hat{\lambda}\left( 1-{q_{\alpha/2} \over \sqrt{n}}\right)^{-1}\right]
   $$

3. Plug-in yields
   $$
   \mathcal{I}_{\text{plug-in}} = \left[\hat{\lambda}\left( 1-{q_{\alpha/2} \over \sqrt{n}}\right),\hat{\lambda}\left( 1+{q_{\alpha/2} \over \sqrt{n}}\right)\right]
   $$

## 4. Delta Method for Non-invertible $g$

Let $(Z_ n)_{n \geq 1}$ denote an asymptotically normal sequence with known asymptotic variance $1$:
$$
\sqrt{n}(Z_ n - \mu ) \xrightarrow [n \to \infty ]{(d)} N(0,1).
$$
Let
$$
\begin{aligned}
g:\mathbb {R} &\to \mathbb {R}\\
x &\mapsto \sqrt{2}\sin (x).
\end{aligned}
$$
Notice that $g$ is no invertible, but the Delta method still applies. 

By applying the **Delta method**, we conclude that

* The sequence $(g(Z_ n))_{n \geq 1}$ is **asymptotically normal**.
  * Since the Delta method states that continuously differentiable function applied to an asymptotically normal sequence of random variables is again asymptotically normal.
  * Note that the Delta method only concerns asymptotic normality, and does not conclude for finite $n$ that the random variable $g(Z_n)$ is normal (or Gaussian).
* The **asymptotic variance** of the sequence $(g(Z_ n))_{n \geq 1}$ is ${2\cos ^2(\mu )}$. 
  * First find $g'(x) = \sqrt{2}\cos (x),$ then by the Delta method, the asymptotic variance of $g(Z_ n)$ is $g'(\mu )^2 \textsf{Var}(Z)= 2\cos ^2(\mu )$.
  * Note that the asymptotic variance of $g(Z_n)$ depends on the unknown parameter $μ$, even though the asymptotic variance of $Z_n$ is known to be $1$.

Let $Z_n = \overline{X}_n$ where $X_1, ..., X_n$ are i.i.d. with mean $\mu$ and known variance $1$. Then the CLT gives
$$
\sqrt{n}(\overline{X}_ n - \mu ) \xrightarrow [n \to \infty ]{(d)} N(0,1).
$$
You estimates $θ=g(μ)$ by the consistent estimator $\hat{\theta} = g(\overline{X}_n)$. Use the “**plug-in**" method to construct a **C.I.** for $θ=g(μ)$ at **asymptotic** level $1−α$. 

From the problem we know that
$$
\sqrt{n}\left(g(\overline{X}_ n)-g(\mu )\right) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}\left(0,\tau ^2\right) \qquad \text {where }\, \tau ^2=\left(g'(\mu )\right)^2 \textsf{Var}(X)= \left(g'(\mu )\right)^2.
$$
This implies 
$$
\frac{\sqrt{n}}{\tau }\left(g(\overline{X}_ n)-g(\mu )\right) \xrightarrow[n \rightarrow \infty]{(d)}  \mathcal{N}(0,1)\qquad \text {where }\, \tau ^2=\left(g'(\mu )\right)^2 .
$$
We follow the usual procedure for C.I.:
$$
\mathbf{P}\left(\frac{\sqrt{n}}{\tau }\left|g(\overline{X}_ n)-g(\mu )\right|<q_{\alpha /2}\right)=1-\alpha .
$$
Manipulate the event with the probability above:
$$
\begin{aligned}
\frac{\sqrt{n}}{\tau }\left|g(\overline{X}_ n)-g(\mu )\right|<q_{\alpha /2} &\Longleftrightarrow -q_{\alpha /2}\frac{\tau }{\sqrt{n}}<g(\overline{X}_ n)-g(\mu )<q_{\alpha /2}\frac{\tau }{\sqrt{n}}\\
&\Longleftrightarrow g(\overline{X}_ n)-q_{\alpha /2}\frac{\tau }{\sqrt{n}}<g(\mu )<g(\overline{X}_ n)+q_{\alpha /2}\frac{\tau }{\sqrt{n}}
\end{aligned}
$$
Therefore, 
$$
g(\mu ) \in \left[ g(\overline{X}_ n)-q_{\alpha /2}\frac{\mid g'(\mu )\mid }{\sqrt{n}}, g(\overline{X}_ n)+q_{\alpha /2}\frac{\mid g'(\mu )\mid }{\sqrt{n}} \right]\qquad \left(\tau =\sqrt{\left(g'(\mu )\right)^2 }=\mid g'(\mu )\mid \right).
$$
Notice that any interval in terms of unknown parameter is not a C.I. To remedy this, we apply the **Plug-in** method: substitute $g'(\mu)$ with $g'(\overline{X}_n)$ via **Slutsky's theorem** and the **Continuous Mapping theorem**.

This gives
$$
g(\mu ) \in \left( g(\overline{X}_ n)-q_{\alpha /2}\frac{\mid g'(\overline{X}_ n)\mid }{\sqrt{n}}, g(\overline{X}_ n)+q_{\alpha /2}\frac{\mid g'(\overline{X}_ n)\mid }{\sqrt{n}} \right).
$$
Which is the second choice. Equivalently, by plugging in $g(x) = \sqrt{2} \sin (x)$ and $g'(x) = \sqrt{2} \cos (x)$, we obtain
$$
g(\mu) \in \left[\sqrt{2}\sin \left(\overline{X}_ n\right)- q_{\alpha /2}\frac{\sqrt{2}\lvert \cos \left(\overline{X}_ n\right)\rvert }{\sqrt{n}},\sqrt{2}\sin \left(\overline{X}_ n\right)+ q_{\alpha /2}\frac{\sqrt{2}\lvert \cos \left(\overline{X}_ n\right)\rvert }{\sqrt{n}}\right]
$$
Notice that the C.I. does not involve $g^{-1}$, the Delta method works even when $g$ is non-invertible.

## 5. Frequentist Interpretation of a Confidence Interval

Take $\mathcal{I}_{\text{plug-in}} = [0.12, 0.20]$ for example, the meaning of " $\mathcal{I}_{\text{plug-in}}$ is a C.I. of asymptotic level $95\%$" is:

If we were to **repeat** the experiment then the parameter would be in the resulting C.I. about $1-\alpha$ of time.

It does NOT mean that
$$
\lim_{n \rightarrow \infty} \mathbb{P}(\lambda \in [0.12, 0.20])\geq 0.95
$$
