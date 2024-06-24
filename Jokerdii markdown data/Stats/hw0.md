# Probability and Linear Algebra Review

There are 8 topics.

## 1. Discrete Random Variables

### Normalization constant for the Poisson distribution

The probability mass function (pmf) of a **Poisson distribution** with parameter $λ$ is given by
$$
\text {Poi}(\lambda ) = \frac{e^{-\lambda}\lambda ^ k}{k!}, \quad k=0,1,2,\ldots .
$$
Note that a probability distribution must satisfy
$$
e^{-\lambda} \sum^{\infty}_{k=0} \frac{\lambda ^ k}{k!} = 1
$$
where 
$$
\sum _{k = 0}^{\infty } \frac{\lambda ^ k}{k!} = \exp (\lambda )
$$

### Moments of Bernoulli variables

The $n$th **moment** of a random variable $X$ is defined to be the expectation $E[X^n]$ of the $n$th power of $X$.

> Let $X$ be a Bernoulli random variable with parameter 0.7. Compute the **expectation values** of $X^k$, denoted by $E[X^k]$, for the following three values of $k$: $k=1,4, $ and $3203$.
>
> **Answer**: 
>
> $E[X] = 0.7\\ E[X^4] = 0.7 \\ E[X^{3203}] = 0.7$
>
> **Solution**: 
>
> The expectation of discrete random variable is 
> $$
> \mathbb E[X] = \sum _{j \in \operatorname {range}(X)} j \,  \mathbf{P}(X = j)
> $$
> The higher moments are
> $$
> \mathbb E[X^ n] = \sum _{j \in \operatorname {range}(X)} j^ n \,  \mathbf{P}(X = j)
> $$
> For a Bernoulli random variable with parameter $p = 0.7$
> $$
> \mathbb E[X] = 0 \times (1 - p) + 1 \times p = p =0.7\\
> \mathbb E[X^4] = 0 \times (1 - p) + 1^4 \times p = p =0.7\\
> \mathbb E[X^{3203}] = 0 \times (1 - p) + 1^{3203} \times p = p =0.7
> $$

### Variance of Bernoulli variables

$$
\textsf{Var}[X] = \mathbb E[X^2] - \mathbb E[X]^2 = p - p^2 = p(1-p)
$$

> When $p \in \{0,1\}$, $\textsf{Var}[X]$ is minimized; When $p=1/2$, $Var[X]$ is maximized.

### Sum of Bernoulli variables

Given $n$ i.i.d. realizations $X_1,…,X_n∼Ber(p)$, from probability theory that $∑^n_{i=1}X_i$ follows a **Binomial** distribution with parameter $n$ and $p$.

### Discrete uniform random variables

A **uniform random variable** is a random variable that takes values with equal probability.

## 2. Gaussian Random Variables

### Moments of Gaussian random variables

The **probability density function (pdf)** of a standard normal distribution 
$$
\phi (z)=\frac{1}{\sqrt{2\pi }} e^{-\frac{z^2}{2}}
$$
The **cumulative distribution function (cdf)** of a standard normal distribution
$$
\Phi (x) = \mathbf{P}(Z \leq x), \quad x \in \mathbb {R}
$$
where $Z \sim \mathcal{N}(0,1)$ is a standard normal variable. 

> **Question 1**: Let $X$ be a **Gaussian random variable** with mean $μ$ and variance $σ^2$. Compute the following moments:
>
> **Answer 1** : 
>
> $\mathbb{E}[X^2] = \sigma^2 + \mu^2\\\mathbb{E}[X^3] = 3 \times \sigma^2 \times \mu + \mu^3\\ \mathbb{E}[X^4] = 3 \times \sigma^4 + 6 \times \sigma^2 \times \mu^2 + \mu^4\\ \textsf {Var}[X^2] = 2 \times \sigma^4 + 4 \times \sigma^2 \times \mu^2$
>
> **Solution 1**: 
>
> We can write a general Gaussian variable $\,   X \sim \mathcal{N}(\mu , \sigma ^2)  \,$ as $\,   X = \sigma Z + \mu  \,$, where $\,   Z \sim \mathcal{N}(0,1)  \,$ is a standard normal variable. Hence, the calculation can be made by factoring out the corresponding polynomials and calculating (or looking up the moments of $Z$).
>
> $\mathbb E[Z] = 0\\\mathbb E[Z^2] = 1\\\mathbb E[Z^3] = 0\\ \mathbb E[Z^4] = 3$
>
> Compute $\mathbb{E}[X^3]$ for example, 
> $$
> \begin{aligned}
> \mathbb E[X^3] &= \int _{-\infty }^{\infty } \left(\sigma z+\mu \right)^3 \phi (z) dz\\
> &=\int _{-\infty }^{\infty }\sigma ^3 z^3 \phi (z) dz +3\sigma ^2 \mu z^2 \phi (z) dz +3\sigma \mu ^2 z \phi (z) dz + \mu ^3 \phi (z) dz\\
> &=\sigma ^3 \mathbb E[Z^3]+3\sigma ^2 \mu \mathbb E[Z^2]+3\sigma \mu ^2 \mathbb E[Z]+ \mu ^3\\
> &=3\sigma ^2 \mu +\mu ^3
> \end{aligned}
> $$
> Compute $Var(X^2)$ using formula
> $$
> \,  \textsf{Var}(X^2)=\mathbb E[X^4]-\left(\mathbb E[X^2]\right)^2 \,
> $$
> **Question 2**: Write $P(X>0)$ in terms of the **cumulative distribution function (cdf)** $Φ$ of the standard Gaussian distribution, evaluated at a function of $μ$ and $σ$.
>
> **Answer 2**: $P(X > 0) = 1 - \mathbb{\Phi}(-\frac{\mu}{\sigma})$.
>
> **Solution 2**: 
> $$
> \begin{aligned}
> \mathbf{P}(X > 0) &=\mathbf{P}( \sigma Z + \mu > 0 ) \\ 
> &= \mathbf{P}(\sigma Z > - \mu )\\
> &= \mathbf{P}( Z > - \frac{\mu }{\sigma } ) \\
> &= 1 - \Phi \left( -\frac{\mu }{\sigma } \right)
> \end{aligned}
> $$

### Covariance of Gaussians

A collection of random variables $X_1,…,X_n$ are **independent and identically distributed (i.i.d.)** if all of them follow the same distribution, and each $X_i$ does not contain information about the other realizations.

The **covariance** of two random variables $X$ and $Y$, denoted by $\textsf{Cov}(X,Y)$, is defined as
$$
\textsf{Cov}(X,Y) = \mathbb E\left[\left(X-\mathbb E[X]\right)\left(Y-\mathbb E[Y]\right)\right]
$$

> Compute the following variances and covariances.
>
> **Answer**: 
>
> $\,  \textsf{Var}(X+Y)= \, 2\\ \textsf{Var}(XY) = 1\\ \textsf{Cov}(X,XY) = 0\\ \textsf{Cov}(X, X+Y)  = 1$
>
> **Solution**:
>
> By the definition of a standard Gaussian random variable
> $$
> \mathbb E[X] = \mathbb E[Y] = 0 \quad \mathbb E[X^2] = \mathbb E[Y^2] = 1
> $$
> By the rule of **independence**
> $$
> \begin{aligned}
> &\textsf{Var}(X + Y) =  \textsf{Var}(X) + \textsf{Var}(Y) = 1 + 1 = 2,\\
> &\textsf{Var}(XY) =  \mathbb E[(XY)^2] - \left(\mathbb E[XY]\right)^2=  \mathbb E[X^2] \mathbb E[Y^2] - \mathbb E[X]^2\mathbb E[Y]^2 = 1 \times 1 - 0 = 1,\\
> &\textsf{Cov}(X,XY) = \mathbb E[X(XY)] - \mathbb E[X] \mathbb E[XY] = \mathbb E[X^2] \mathbb E[Y] - \mathbb E[X]^2 \mathbb E[Y] = 1 \times 0 - 0 \times 0 = 0
> \end{aligned}
> $$
> By the rule of **independence** and **linearity of expectation**
> $$
> \begin{aligned}
> \textsf{Cov}(X, X+Y) &=\mathbb E[X(X+Y)] - \mathbb E[X] \mathbb E[X+Y] \\
> &=  \mathbb E[X^2] + \mathbb E[XY] - \mathbb E[X] (\mathbb E[X] + \mathbb E[Y])\\
> &= \mathbb E[X^2] + \mathbb E[X] \mathbb E[Y] - \mathbb E[X]^2 - \mathbb E[X] \mathbb E[Y]\\
> &=1
> \end{aligned}
> $$

### Variance, covariance and independence

For any two random variables:
$$
\textsf{Var}(X+Y)=\textsf{Var}(X)+\textsf{Var}(Y)+2{\rm Cov}(X,Y)
$$
In particular, if $X$ and $Y$ are dependent, then ${\rm Cov}(X,Y)\neq 0$. But the reverse is not necessarily true.  In other word, if the covariance, $\textsf{Cov}(X,Y)$ between two random variables $X,Y$ is $0$, then $X$ and $Y$ are not necessarily independent.

For example, let $X \sim \rm{Unif}[-1, 1]$ and let $Y = X^2$ Then, 
$$
{\rm Cov}(X,Y)=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]=\mathbb E[X^3]-\mathbb E[X]\mathbb E[X^2]=0,
$$
using the fact that $X$ is **centered and symmetric around 0**, and its **odd moments vanish**. Even though they are uncorrelated, they are (highly) dependent, $Y$ is obtained from $X$.

##  3. Uniform random variables

### Expectation, variance and probabilities

> Let $X$ be a uniform random variable in the interval $[2, 8.5]$. Find the following quantities 
>
> **Answer**:
>
> $\mathbb{E}[X] = 21/4\\ \rm{Var}[X] = 169/48\\ P(X > 4) = 9/13\\ P(\rm{log}(X) \leq 1)$ 
>
> **Solution**:
>
> We can write $X = 6.5 Z +2$, where $Z$ follows a uniform distribution on $[0,1]$. By properties of the uniform distribution, we then conclude
> $$
> \mathbb E[X] = 2 + 6.5 \mathbb E[Z] = 2 + 6.5 \times \frac{1}{2} = \frac{21}{4},\\
> \textsf{Var}[X] = 6.5^2 \times \textsf{Var}[Z] = \frac{169}{4} \times \frac{1}{12} = \frac{169}{48},\\
> \mathbf{P}(X \geq 4) = \mathbf{P}(Z \geq \frac{4}{13}) = 1 - \frac{4}{13} = \frac{9}{13},\\
> \mathbf{P}(\log (X) \leq 1) = \mathbf{P}(X \leq e) = \mathbf{P}(Z \leq \frac{2(\mathbf e- 2)}{13}) \approx 0.110549.
> $$

### Two independent copies

> Let $U, V$ be i.i.d, random variables uniformly distributed in $[0,1]$. Compute the following quantities
>
> **Answer**: 
>
> $\mathbb{E}[|U - V|] = 1/3\\ P(U = V) = 0\\ P(U \leq V) = 1/2$
>
> **Solution**: 
>
> For the first quantity, we write the joint expectation as an **iterated expectation and conditional expectation**,
> $$
> \mathbb E[|U - V|] = \mathbb E[\mathbb E[|U - V| | V]].
> $$
> By independence, we can compute the inner expectation as
> $$
> \begin{aligned}
> \mathbb E[|U - V| | V = v] &= \int _0^1 | u - v | \,  du\\
>  &= \int _0^ v (v-u) \,  du + \int _ v^1 (u-v) \,  du\\
>  &= \left[ vu - \frac{1}{2}u^2 \,  \right]_0^ v + \left[ \frac{1}{2}u^2 - vu \,  \right]_ v^1 \\
>  &=v^2 - v + \frac{1}{2}
>  \end{aligned}
> $$
> so
> $$
> \mathbb E[\, |U - V|\, ] = \mathbb E\left[V^2 - V + \frac{1}{2}\right] = \frac{1}{3} - \frac{1}{2} + \frac{1}{2} = \frac{1}{3}.
> $$
> For the probability $ \mathbf{P}(U = V)$, just write this as double expectation as well as notice that
> $$
> \mathbf{P}(U = V) = \mathbb E[ \mathbb E[ \mathbf{1}(U = V) | V] ] = \mathbb E[0] = 0,
> $$
> because the probability of a uniform random variable being equal to any fixed number between $0$ and $1$ is zero.
>
> For $P(U≤V)$, write it again as a double expectation, 
> $$
> \mathbf{P}(U \leq V) = \mathbb E[ \mathbb E[\mathbf{1}(U \leq V) | V] ] = \mathbb E[ \mathbf{P}(U \leq V) | V ] = \mathbb E[V] = \frac{1}{2}.
> $$
> Alternatively, by symmetry of the two variables, $P(U≤V)=P(V≤U)$ and either one of the two is true.

### Maximum and sum of independent copies

> Let $X,Y$ be independent random variables uniformly distributed in $[0,1]$. In the graph below, sketch
>
> 1. The probability density $f_{X + Y} (z)$ of $X + Y$;
> 2. The probability density $f_{\max(X,Y)}(z)$ of $\max(X,Y)$;
>
> **Answer**: 
>
> $f_{X + Y} (z) = \left\{  \begin{aligned}  0, & \qquad z < 0\\ z, & \qquad 0 < z < 1\\ 2 - z, & \qquad 1 < z < 2\\ 0, & \qquad z > 2. \end{aligned} \right.\\f_{\max(X,Y)}(z) = \left\{  \begin{aligned}  0, \quad & z < 0\\ 2z, \quad & 0 \leq z \leq 1\\ 0, \quad & z > 1. \end{aligned} \right. $
>
> **Solution**: 
>
> The density of a uniform random variable is 
> $$
> f(x) = \mathbf{1}[0,1] = \left\{  \begin{aligned}  1, \quad & \text {if } x \in [0,1]\\ 0, \quad & \text {otherwise} \end{aligned} \right.
> $$
> The density of $X + Y$ is given by the **convolution** of the density of a uniform random variable. Therefore, the density $g$ of $X+ Y$ is
> $$
> \begin{aligned}
> g(z) &= \int _{\mathbb {R}} f(x) f(z - x) \,  dx\\
> &= \int _{\mathbb {R}} \mathbf{1}(x \in [0,1]) \mathbf{1}(z - x \in [0, 1]) \,  dx\\
> &= \int _0^1 \mathbf{1} (z - 1 \leq x \leq z) \,  dx\\
> &= \mathbf{1}(z \leq 2) \int _{\max \{ 0, z-1\} }^{\min \{ 1, z\} } \,  dx\\
> &= \left\{  \begin{aligned}  0, & \qquad z < 0\\ z, & \qquad 0 < z < 1\\ 2 - z, & \qquad 1 < z < 2\\ 0, & \qquad z > 2. \end{aligned} \right.
> \end{aligned}
> $$
> For the density of $\max\{X,Y\}$, first note that it is supported in $[0,1]$. Now, first compute the **cdf** on that interval:
> $$
> \mathbf{P}(\max \{ X,Y\}  \leq y) = \mathbf{P}(X \leq y) \mathbf{P}(Y \leq y) \quad \text {(by independence)} = z^2
> $$
> Hence the density $h$ of $\max\{X,Y\}$ is given by taking the derivative of the cdf and get
> $$
> h(z) = \left\{  \begin{aligned}  0, \quad & z < 0\\ 2z, \quad & 0 \leq z \leq 1\\ 0, \quad & z > 1. \end{aligned} \right.
> $$

### Maximum of uniform random variables

> Let $U_1, ..., U_n$ be i.i.d. random variables uniformly distributed in $[0,1]$ and let $\,  \displaystyle M_ n= \max _{1\leq i\leq n} U_ i \,$. Find the cdf of $M_n$, which we denote by $G(t)$, for $t \in [0,1]$. And compute $ \lim _{n \to \infty } F_ n(t)$ where $F_ n(t)$ denote the cdf of $n(1-M_n)$, for $t > 0$.
>
> **Answer**: 
>
> For $t \in [0,1]$, $G(t) = t^n$;  For $t > 0$, $ \lim _{n \to \infty } F_ n(t) = 1-\exp(-t)$.
>
> **Solution**: 
>
> The cdf of $M_n$ is 
> $$
> \mathbf{P}(M_ n \leq t) = \mathbf{P}\left(\max _{i = 1, \dots , n} U_ i \leq t\right) = \mathbf{P}\left(\cap _{i=1}^ n \{ U_ i \leq t\} \right) \quad \text{(by independence) }= \prod _{i=1}^ n \mathbf{P}(U_ i \leq t) = t^ n,
> $$
> The cdf of $n(1-M_n)$ is 
> $$
> \begin{aligned}
> \mathbf{P}\left(n(1-M_ n) \leq t\right) &= \mathbf{P}\left(1 - M_ n \leq \frac{t}{n}\right) = \mathbf{P}\left(M_ n \geq 1 - \frac{t}{n}\right)\\
> &=1 - \mathbf{P}\left(M_ n < 1 - \frac{t}{n}\right) = 1 - \left( 1 - \frac{t}{n} \right)^ n \xrightarrow {n \to \infty } 1 - \mathbf e^{-t}.
> \end{aligned}
> $$

## 4. Exponential random variables

### Sums and products

Recall that:

If $X \sim \mathrm{Exp}(\lambda )$ with $\lambda>0$, then
$$
\mathbb E[X] = \lambda , \quad \mathbb E[X^2] = \frac{2}{\lambda ^2}, \quad \textsf{Var}(X) = \frac{1}{\lambda ^2}.
$$
If $ Y \sim \mathrm{Poi}(\mu )$, again with $\mu > 0$, then
$$
\mathbb E[Y] = \mu , \quad \mathbb E[Y^2] = \mu + \mu ^2, \quad \textsf{Var}(Y) = \mu .
$$

> Let $X$ be an exponential random variable with parameter $λ>0$ and $Y$ be a Poisson random variable with parameter $μ>0$. Assume that $X$ and $Y$ are independent. Compute the following quantities:
>
> By linearity of expectation,
> $$
> \mathbb E[X^2 + Y^2] = \mathbb E[X^2] + \mathbb E[Y^2] = \frac{2}{\lambda ^2} + \mu + \mu ^2 
> $$
> By multiplicativity of expectation for independent variables,
> $$
> \mathbb E[X^2 Y] =\mathbb E[X^2] \mathbb E[Y] = \frac{2 \mu }{\lambda ^2}
> $$
> By additivity of variance for independent variables and scaling property of variance,
> $$
> \textsf{Var}(2X + 3Y) = \textsf{Var}(2 X) + \textsf{Var}(3 Y) =2^2 \textsf{Var}(X) + 3^2 \textsf{Var}(Y) = \frac{4}{\lambda ^2} + 9 \mu
> $$

### Estimators

Recall that the cdf of exponential distribution with parameter $\lambda$ on $(0, \infty)$ is 
$$
F(x) = 1 - \exp (-\lambda x).
$$

> Let $X_1,…,X_n$ be i.i.d exponential random variables with parameter $λ$ and let $Z_i=1(X_i≤1),i=1,…,n$.  What is the limit in probability, as $n$ goes to infinity, of $\frac{1}{n}\sum _{i=1}^ n Z_ i$.
>
> **Answer**: $\frac{1}{n} \sum _{i=1}^{n} Z_ i \xrightarrow [n \to \infty ]{\mathrm{\mathbf{P}}} \, 1-\exp(-\lambda)$
>
> **Solution**: 
>
> Since $X_i$ are i.i.d. by the Law of Large Numbers 
> $$
> \frac{1}{n} \sum _{i=1}^{n} Z_ i \xrightarrow [n \to \infty ]{\mathrm{\mathbf{P}}} \mathbb E[Z_ i],
> $$
> And the following formula follows the cdf of an Exponential distribution:
> $$
> \mathbb E[Z_ i] = \mathbf{P}(X_ i \leq 1) = 1 - \exp (-\lambda \times 1) = 1 - \exp (-\lambda )
> $$

### Properties of the exponential distribution

> Let $X$ be an exponential random variable with parameter $\lambda = 2$ that models the lifetime (in years) of a lightbulb. Compute the probability that the lightbulb lasts for at least 2 years. Given the lightbulb has lasted 2 years, find the probability that it lasts for $k$ more years for any positive integer $k$.
>
> **Answer**: 
>
> $\mathbf{P}(X \geq 2) = \exp(-4)\\\mathbf{P}(X \geq k + 2 | X \geq 2) = \exp(-2k)$
>
> **Solution**: 
>
> For $\lambda = 2$, using the cdf of exponential distribution
> $$
> \mathbf{P}(X \geq 2) = 1- \mathbf{P}(X \leq 2) = 1- F(X=2) =  1 - (1- \exp(-2 \times 2)) = e^{-4}
> $$
> Note that $ \{ X \geq k+2\}  \subseteq \{ X \geq 2\}$, so
> $$
> \mathbf{P}(X \geq k + 2 | X \geq 2) = \frac{\mathbf{P}(\{ X \geq k + 2\}  \cap \{ X \geq 2\} )}{\mathbf{P}(X \geq 2)} = \frac{\mathbf{P}(X \geq k + 2)}{\mathbf{P}(X \geq 2)} =\frac{e^{-2(k + 2)}}{e^{-4}} = e^{-2k}
> $$

This is an example of the exponential distribution being **memoryless** : The probability of the lightbulb lasting $k$ more years given that it already lasted 2 years is exactly the same as the probability of it lasting $k$ years in the first place.

## 5. Probability tables

### Gaussian probabilities

For $Z \sim \mathcal{N}(0, 1), x > 0$ we have
$$
\mathbf{P}(Z \leq -x) = \mathbf{P}(Z \geq x) = 1 - \mathbf{P}(Z \leq x),
$$
and 
$$
\mathbf{P}(Z \geq x) = 1 - \mathbf{P}(Z \leq x).
$$
To obtain probabilities for any normal distribution with any given $\mu$ and $\sigma$, we can represent $X = \sigma Z +\mu$ where $Z \sim \mathcal{N}(0,1)$.

> Let $X \sim N(1, 2.25)$, compute the probabilities below (also look up the normal probability table)
>
> **Answer**: 
>
> $\mathbf{P}(X > 1) = 0.5\\ \mathbf{P}(|X - 2| \leq 1) = 0.4082 \\ \mathbf{P}(X^2 > 4) = 0.2752427 \\ \mathbf{P}(X^2 - 2X - 1 > 0) = 0.3457786$
>
> **Solution**: 
> $$
> \begin{aligned}
> \mathbf{P}(X > 1) &= \mathbf{P}(1.5Z + 1 > 1) = \mathbf{P}(1.5Z > 0)\\
> &= \mathbf{P}(Z \geq 0) = 1 - \mathbf{P}(Z \leq 0) = 1 - 0.5000 = 0.5000\\
> \mathbf{P}(| X - 2 | \leq 1) &= \mathbf{P}(-1 \leq (X - 2) \leq 1) = \mathbf{P}(-1 \leq (1.5Z + 1 -2) \leq 1)\\
> &=\mathbf{P}(0 \leq 1.5Z \leq 2)\\
> & \simeq\mathbf{P}(0 \leq Z \leq 1.33)\\
> &=\mathbf{P}(Z \leq 1.33) - \mathbf{P}(Z \leq 0) \simeq 0.9082 - 0.5000 = 0.4082\\
> \mathbf{P}(X^2 > 4) &=\mathbf{P}(| X | > 2) = \mathbf{P}(| 1.5Z + 1 | > 2)\\
> &= \mathbf{P}(1.5Z + 1 \leq -2) + \mathbf{P}(1.5 Z + 1 \geq 2)\\
> &=\mathbf{P}(Z \leq -2) + \mathbf{P}\left(Z \geq \frac{2}{3}\right)\\
> &=1 - \mathbf{P}(Z \leq 2) + 1 - \mathbf{P}\left(Z \leq \frac{2}{3}\right)\\
> &\simeq 2 - 0.9772 - 0.7486 = 0.2742\\
> \mathbf{P}( X^2 - 2X - 1 > 0 ) &= \mathbf{P}((X-1)^2 - 2 > 0) = \mathbf{P}(|X-1| > \sqrt{2})\\
> &=\mathbf{P}(|1.5Z| > \sqrt{2})\\
> &=\mathbf{P}(Z > \frac{\sqrt{2}}{1.5}) + \mathbf{P}(Z < -\frac{\sqrt{2}}{1.5})\\
> &=2 - 2\mathbf{P}(Z < \frac{\sqrt{2}}{1.5})\\
> & \simeq 2 - 2(0.8264)\\
> &= 0.3472.
> \end{aligned}
> $$

### Approximation of Binomial variables

> Using the normal probability table, evaluate approximately $P(X>400)$, where $X$ is a binomial random variable with parameters $1000$ and $0.3$.
>
> **Answer**: $\mathbf{P}(X > 400) \simeq 0.0002$
>
> **Solution**: 
>
> A binomial distribution with parameters $(n,p)$ has expectation $np$ and variance $np(1−p)$. Hence, by the Central Limit Theorem, we have
> $$
> \frac{1}{\sqrt{n p (1-p)}} (X - np) \xrightarrow {\text{(D)}} Z \sim \mathcal{N}(0,1).
> $$
> The probability in question can therefore be approximated by
> $$
> \begin{aligned}
> \mathbf{P}(X > 400) &=  \mathbf{P}\left(\frac{1}{\sqrt{1000 \times 0.3 \times 0.7}} (X - 300) > \frac{100}{\sqrt{1000 \times 0.3 \times 0.7}}\right)\\
> &\simeq 1 - \mathbf{P}(Z \leq \frac{100}{\sqrt{1000 \times 0.3 \times 0.7}})\\
> & \simeq 1 - \mathbf{P}(Z \leq 6.90)\\
> &\leq 1 - 0.9998 = 0.0002.
> \end{aligned}
> $$

## 6. Matrices and Vectors

### Matrix Multiplication

The size of the output is the number of rows of the left matrix, and the number of columns of the right matrix. 

### Vector Inner product

The product $\mathbf{u}^ T \mathbf{v}$ evaluates the **inner product** (also called the **dot product** ) of $\mathbf{u}$ and $\mathbf{v}$. The inner product of $\mathbf{u}$ and $\mathbf{v}$ is sometimes written as $⟨\mathbf{u},\mathbf{v}⟩$. The inner product is always a scalar. 

In general, if $\mathbf{u}= (u_1, u_2, \ldots , u_ n)^ T$ and $\mathbf{v}= (v_1, v_2, \ldots , v_ n)^ T$, then $\mathbf{u}^ T \mathbf{v}= \sum _{i=1}^{n} u_ i v_ i$.
$$
\begin{pmatrix}  u_1 &  \cdots &  u_ n \end{pmatrix} \begin{pmatrix}  v_1 \\ \vdots \\ v_ n \end{pmatrix} = (\cdot )
$$

### Vector Outer product

The product $\mathbf{u}\mathbf{v}^T$ evaluates the **outer product** of $\mathbf{u}$ and $\mathbf{v}$, which is a 2×2 matrix in this case. 

In general, if $\mathbf{u}= \begin{pmatrix}  u_1 \\ \vdots \\ u_ m \end{pmatrix}$ and $\mathbf{v}= \begin{pmatrix}  v_1 \\ \vdots \\ v_ n \end{pmatrix}$, $\mathbf{u}\mathbf{v}^ T$ is an $m \times n$ matrix whose $(i,j)$ entry is $(\mathbf{u}\mathbf{v}^ T)_{i,j} = u_ i v_ j$.

## 7. Linear Independence, Subspaces and Dimension

Vectors $\mathbf{v}_1, \ldots , \mathbf{v}_ n$ are said to be **linearly dependent** if there exist scalars $c_1, \ldots , c_ n$ such that 

(1) not all $c_i$'s are zero and 

(2) $\mathbf{c}_1\mathbf{v}_1+⋯+\mathbf{c}_n\mathbf{v}_n=0$.

Otherwise, they are said to be **linearly independent** : the only scalars $c_1, \ldots , c_ n$ that satisfy $c_1 \mathbf{v}_1 + \cdots + c_ n \mathbf{v}_ n = 0$ are $c_1 = \cdots = c_ n = 0$.

The collection of non-zero vectors $\mathbf{v}_1, \ldots , \mathbf{v}_ n \in \mathbb {R}^ m$ determines a **subspace** of $\R^m$, which is the set of all linear combinations $c_1 \mathbf{v}_1 + \cdots + c_ n \mathbf{v}_ n$ over different choices of $c_1,\ldots ,c_ n \in \mathbb {R}$. The **dimension** of this subspace is the size of the **largest possible, linearly independent** sub-collection of the (non-zero) vectors $\mathbf{v}_1, \ldots , \mathbf{v}_ n$.

### The rank of a matrix

In general, the rank of any $m×n$ matrix can be at most $\min(m,n)$, since rank = column rank = row rank. In general, a matrix $\mathbf{A}$ is said to have **full rank** if $\mathrm{rank}(\mathbf{A}) = \min (m,n)$.

> The rank of matrix $\begin{pmatrix}  0 &  0 \\ 0 &  0 \end{pmatrix}$ is 0.
>
> By definition, the rank is equal to the number of **nonzero** linearly independent vectors.
>
> The rank of matrix $\begin{pmatrix}  1 &  1 &  0 \\ 0 &  -3 &  2 \\ 0 &  0 &  1 \end{pmatrix}$ is 3.
>
> All three rows are independent. An easy way to check is to notice that this matrix is **upper triangular** , with nonzero entries along the diagonal.

**Every rank-1 matrix can be written as an outer product. Conversely, every outer product $\mathbf{u} \mathbf{v} ^T$ is a rank-1 matrix.**

In general, the sum of two matrices can have a varying range of ranks, and they can be greater **or** less than the ranks of matrices that are being summed up. On the other hand, it is a general fact that if $\mathbf{A}$ and $\mathbf{B}$ are arbitrary (possibly rectangular) matrices, $\mathrm{rank}(\mathbf{A}\mathbf{B}) \leq \min (\mathrm{rank}(\mathbf{A}), \mathrm{rank}(\mathbf{B}))$. It is possible to use **determinants** to reason about rank. Other times, one may resort to using **Gaussian Elimination** – the rank of any upper triangular matrix is **at least** the number of non-zero entries along the diagonal.

> Given $\mathbf{A}= \begin{pmatrix} -1 &  1 \\ -3 &  3\end{pmatrix}, \mathbf{B}= \begin{pmatrix} 1 &  -1 \\ -1 &  1\end{pmatrix}, \mathbf{C}= \begin{pmatrix}  0 &  0 \\ 0 &  1\end{pmatrix}, \mathbf{D}= \begin{pmatrix} 1 &  1 \\ 1 &  1\end{pmatrix}$, which are rank 1. We can write them as $\mathbf{A}= \mathbf{u}\mathbf{v}^ T, \mathbf{B}= \mathbf{v}\mathbf{v}^ T, \mathbf{C}= \mathbf{w}\mathbf{w}^ T,$ and $\mathbf{D}= \mathbf{x}\mathbf{x}^ T$, where
> $$
> \mathbf{u}= \begin{pmatrix} 1 \\ 3 \end{pmatrix}, \mathbf{v}= \begin{pmatrix} -1 \\ 1 \end{pmatrix}, \mathbf{w}= \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \mathbf{x}= \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
> $$
> which combination of these matrices has rank 2 ? which combination of these matrices has rank 1? 
>
> **Answer**: 
>
> Considering the sums of matrices,
>
> $\mathbf{A}+\mathbf{A}= 2\mathbf{A}$, which has rank 1.
>
> $\mathbf{A}+\mathbf{B}= \mathbf{u}\mathbf{v}^ T + \mathbf{v}\mathbf{v}^ T = (\mathbf{u}+ \mathbf{v})\mathbf{v}^ T$ which has rank 1
>
> $\mathbf{A}+\mathbf{C}= \begin{pmatrix} -1 &  1 \\ -3 &  4\end{pmatrix}$ which has two linearly independent rows, hence its rank is 3.
>
> Considering the products of matrices,
>
> $\mathbf{A}\mathbf{B}= \mathbf{u}\mathbf{v}^ T \mathbf{v}\mathbf{v}^ T = \mathbf{u}\langle \mathbf{v}, \mathbf{v}\rangle \mathbf{v}^ T = \langle \mathbf{v},\mathbf{v}\rangle \mathbf{u}\mathbf{v}^ T$. Note that the inner product $\mathbf{v}^ T \mathbf{v}= \langle \mathbf{v}, \mathbf{v}\rangle$ is a scalar. So this outer product of two vectors has rank 1.
>
> $\mathbf{A}\mathbf{C}= \mathbf{u}\mathbf{v}^ T \mathbf{w}\mathbf{w}^ T = \langle \mathbf{v}, \mathbf{w}\rangle \mathbf{u}\mathbf{w}^ T$ , which has rank 1.
>
> $\mathbf{B}\mathbf{D}= \mathbf{v}\mathbf{v}^ T \mathbf{x}\mathbf{x}^ T = \langle \mathbf{v}, \mathbf{x}\rangle \mathbf{v}\mathbf{x}^ T$ which has rank 1. Notice that $\mathbf{v}$ is orthogonal to $\mathbf{x}$, so $\mathbf{B}\mathbf{D}= 0 \mathbf{v}\mathbf{x}^ T$ is the zero matrix. Its rank is zero.

### Invertibility of a matrix

An $n×n$ matrix $\mathbf{A}$ is invertible if and only if $\mathbf{A}$ has full rank, i.e. $\mathrm{rank}(\mathbf{A}) = n$.

## 8. Eigenvalues, Eigenvectors and Determinants (Optional)

### Eigenvalues and Eigenvectors of a matrix

Solve $\mathbf{A} \mathbf{v} = \lambda \mathbf{v}$, where $\lambda$ is a diagonal matrix. 

> Let $\mathbf{A}= \begin{pmatrix}  3 &  0 \\ \frac{1}{2} &  2 \end{pmatrix}$, $\mathbf{v}= \begin{pmatrix}  2 \\ 1 \end{pmatrix}$, $\mathbf{w}= \begin{pmatrix}  0 \\ 1 \end{pmatrix}$. 
>
> **Answer**: 
>
> $\mathbf{A}\mathbf{v}= \lambda _1 \mathbf{v}$, where $\lambda_1 = 3$.
>
> $\mathbf{A}\mathbf{w}= \lambda _2 \mathbf{w}$, where $\lambda_2 = 2.$
>
> **Solution**:
> $$
> \mathbf{A}\mathbf{v}= \begin{pmatrix}  3 &  0 \\ \frac{1}{2} &  2 \end{pmatrix} \begin{pmatrix}  2 \\ 1 \end{pmatrix} = \begin{pmatrix}  6 \\ 3 \end{pmatrix} \implies \lambda _1 = 3\\
> \mathbf{A}\mathbf{w}= \begin{pmatrix}  3 &  0 \\ \frac{1}{2} &  2 \end{pmatrix} \begin{pmatrix}  0 \\ 1 \end{pmatrix} = \begin{pmatrix}  0 \\ 2 \end{pmatrix} \implies \lambda _2 = 2
> $$

### Geometric Interpretation of Eigenvalues and Eigenvectors

> Let $\mathbf{A}= \begin{pmatrix}  3 &  0 \\ \frac{1}{2} &  2 \end{pmatrix}$, $\mathbf{v}= \begin{pmatrix}  2 \\ 1 \end{pmatrix}$, $\mathbf{w}= \begin{pmatrix}  0 \\ 1 \end{pmatrix}$.  Suppose $\mathbf x= \mathbf{v}+ 2\mathbf{w}= \begin{pmatrix}  2 \\ 3 \end{pmatrix}$. Then $\mathbf{A}\mathbf x= s \mathbf{v}+ t \mathbf{w}$, where:
>
> **Answer**: 
>
> $s = 3$ and $t =4 $,
>
> **Solution**:
>
> We have
> $$
> \begin{aligned}
> \mathbf{A}\mathbf x &= \mathbf{A}(\mathbf{v}+ 2\mathbf{w})\\
> &= \mathbf{A}\mathbf{v}+ 2\mathbf{A}\mathbf{w}\\
> &= (3\mathbf{v}) + 2(2\mathbf{w})\\
> &= 3\mathbf{v}+ 4\mathbf{w}.
> \end{aligned}
> $$
> From this, we get $s = 3, t = 4$.
>
> In particular, $s$ describes the amount that $\mathbf{A}$ stretches $\mathbf{x}$ in the direction of $\mathbf{v}$, and $t \over 2$ (note the “2" in front of $\mathbf{w}$ in $\mathbf{x}$) describes the amount that $\mathbf{A}$ stretches $\mathbf{x}$ in the direction of $\mathbf{w}$. 

### Determinant and Eigenvalues 

The **determinant** of a matrix indicates whether it is singular. For 2×2 matrices, it has the formula
$$
\mathrm{det}\left( \begin{array}{cc} a &  b \\ c &  d \end{array} \right) = ad-bc
$$
For general n×n matrices, the **product of the eigenvalues is always equal to the determinant**.

### Trace and Eigenvalues

The **trace** of a matrix is the sum of the diagonal entries.

For general n×n matrices, the **sum of the eigenvalues is always equal to the trace of the matrix**.

### Nullspace

> If a (nonzero) vector is in the nullspace of a square matrix $\mathbf{A}$, it is an eigenvector of $\mathbf{A}$.
>
> If $0$ is an eigenvalue for a given square matrix $\mathbf{A}$,
>
> * $\mathrm{det}(\mathbf{A})= 0$
> * $\text {NS}(\mathbf{A})\neq \mathbf{0}$
>
> **Solution**: 
>
> If a vector $\mathbf{v}$ is in the nullspace of $\mathbf{A}$, then $\mathbf{Av}=0=(0)\mathbf{v}$. So it is an eigenvector of $\mathbf{A}$ associated to the eigenvalue 0.
>
> If 0 is an eigenvalue for a matrix $\mathbf{A}$, then by definition, there exists a nonzero solution to $\mathbf{Av}=0$; that is, $\rm{NS}(\mathbf{A})≠0$, and this only happens if and only if $\rm{det}(\mathbf{A})=0$.

# Additional Readings

![distributions](../assets/images/distribution-summary.jpeg)

From : https://medium.com/@ciortanmadalina/overview-of-data-distributions-87d95a5cbf0a

