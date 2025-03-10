# Lecture 8. Continuous Random Variables and Probability Density Functions

* Probability density functions

  * Definition: A random variable is continuous if it can be described by a PDF.
  * Properties

  | Discrete                                                     | Continuous                                                   |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | $\mathbf{P}(a \leq X \leq b) = \sum_{x: a\leq x \leq b} p_X(x)$ | $\mathbf{P}(a \leq X \leq b) = \int^b_a f_X(x) dx$           |
  | $p_X(x) \geq 0$                                              | $f_X(x) \geq 0$                                              |
  | $\sum_xp_X(x)=1$                                             | $\int^\infty_{-\infty} f_X(x)dx = 1$                         |
  |                                                              | $\mathbf{P}(a \leq X \leq a + \delta) \approx f_X(a) \cdot \delta\\\mathbf{P}(X=a) = 0$ |

  * Examples

* Expectation and its properties

  * The expected value rule

    | Discrete                                | Continuous                                             |
    | --------------------------------------- | ------------------------------------------------------ |
    | $\mathbf{E}[X] = \sum_x x p_X(x)$       | $\mathbf{E}[X] = \int^\infty_{-\infty} x f_X(x) dx$    |
    | $\mathbf{E}[g(X)] = \sum_x g(X) p_X(x)$ | $\mathbf{E}[g(X)] = \int_{-\infty}^\infty g(X) p_X(x)$ |

  * Properties 

    * If $X \geq 0$, then $\mathbf{E}[X] >0$.
    * If $a \leq X \leq b$, then $a \leq \mathbf{E}[X] \leq b$.

    * Linearity: $\mathbf{E}[aX+b] = a\mathbf{E}[X]+b$.

* Variance and its properties

  * Definition: $\mathsf{Var}(X) = \mathbf{E}[(X-\mu)^2]$
  * Standard deviation: $\sigma_{X} = \sqrt{\mathsf{Var}(X)}$
  * Properties: $\mathsf{Var}(aX+b) = a^2 \mathsf{Var}(X)$
  * A useful formula: $\mathsf{Var}(X) = \mathbf{E}[X^2] - (\mathbf{E}[X])^2$

* Uniform random variables

  | Discrete                                    | Continuous                                                   |
  | ------------------------------------------- | ------------------------------------------------------------ |
  | $p_X(x) = {1 \over b-a+1}$                  | $f_X(x) = {1 \over b-a}$                                     |
  | $\mathbf{E}[X] = {a+b \over 2}$             | $\mathbf{E}[X] = {a+b \over 2}\\\mathbf{E}[X^2] = {1\over b-a}\left({b^3\over 3} - {a^3 \over 3}\right)$ |
  | $\mathsf{Var}(X) = {1\over 12}(b-a)(b-a+2)$ | $\mathsf{Var}(X)={1\over 12}(b-a)^2$                         |

* Exponential random variables $\lambda > 0$

  ![U5-lec8-exponential](../assets/images/U5-lec8-exponential.png)

  | Geometric (discrete)          | Exponential (continuous)                                     |
  | ----------------------------- | ------------------------------------------------------------ |
  | $p_X(x) = (1-p)^{k-1}p$       | $f_X(x) = \begin{cases}\lambda e^{-\lambda x}, & x\geq 0\\0, &x < 0 \end{cases}$ |
  | $\mathbf{E}[X] = {1 \over p}$ | $\mathbf{E}[X] = {1 \over \lambda}$                          |
  |                               | $\mathsf{Var}(X)= {1\over \lambda^2} $                       |
  |                               | $\mathbf{P}(X\geq a) = \int^\infty_a\lambda e^{-\lambda x} dx = \lambda \cdot (-{1\over \lambda}) e^{-\lambda x}\vert ^\infty_a = e^{-\lambda a}\\ \mathbf{P}(X\leq a) = 1 - e^{-\lambda a}$ |

* Cumulative distribution functions

  * Definition: $F_X(x) = \mathbf{P}(X\leq x) $

  | Discrete                         | Continuous                          |
  | -------------------------------- | ----------------------------------- |
  | $F_X(x) = \sum_{k \leq x}p_X(k)$ | $F_X(x) = \int^x_{-\infty}f_X(t)dt$ |

  * Properties
    * Non-decreasing: If $y \geq x \implies F_X(y) \geq F_X(x)$.
    * $F_X(x) \xrightarrow[x\rightarrow \infty]{}1$.
    * $F_X(x) \xrightarrow[x\rightarrow -\infty]{}0$.

* Normal (Gaussian) random variables 

  * Standard normal $\mathcal{N}(0,1): f_X(x) = {1\over \sqrt{2 \pi}} \exp(-x^2/2)$.

    $\mathbf{E}[X] = 0,\quad \mathsf{Var}(X)=1$.

  * General normal $\mathcal{N}(\mu, \sigma^2):f_X(x) = {1\over \sigma\sqrt{2\pi}} \exp\left(-(x-\mu)^2\over 2\sigma^2\right)$.

    $\mathbf{E}[X] = \mu,\quad \mathsf{Var}(X)=\sigma^2$.

  * Linearity properties: Let $Y = aX+b, \quad X \sim \mathcal{N}(\mu, \sigma^2)$.

    $\mathbf{E}[X] = a\mu+b,\quad \mathsf{Var}(X)=a^2\sigma^2$

  * Using tables to calculate probabilities since no closed form available for CDF

    Standardizing a random variable $Y = {X-\mu \over \sigma}$.

    $Y \sim \mathcal{N}(0,1), \quad \Phi(y) = F_Y(y) = \mathbf{P}(Y \leq y)$.


There are 0 selected exercise and 2 solved problems.

---

## Problem 1 Mean and variance of the exponential

Let $\lambda$ be a positive number. The continuous random variable $X$ is called exponential with parameter $\lambda$ when its probability density function is
$$
f_{X}(x) =  \begin{cases} \lambda e^{-\lambda x}, &  \text{if } x \geq 0, \\ 0, &  \text{otherwise}.  \end{cases}
$$
(a) Find the cumulative distribution function (CDF) of $X$.

(b) Find the mean of $X$.

(c) Find the variance of $X$.

(d) Suppose $X_1， X_2,$ and $X_3$ are independent exponential random variables, each with parameter $\lambda$ . Find the PDF of $Z = \max\{X_1, X_2, X_3\}$.

(e) Find the PDF of $W =  \min\{X_1, X_2\}$.

**Solution**:

(a)

For $x  >0$,
$$
F_X(x) = \int^x_{-\infty}f_X(x)dt = \int^x_{0}\lambda e^{-\lambda t} dt = \left[ -e^{-\lambda t}\right]^x_0 = 1 - e^{-\lambda x}
$$
For $x < 0$, we have $F_X(x) = \int^x_{-\infty}f_X(t)dt = 0$. 

Thus we conclude
$$
F_X(x) =  \begin{cases}0, & \text{if }x < 0 \\ 1-e^{-\lambda x} &\text{if }x \geq 0 \end{cases}
$$
(b)

The key step in the following computation uses integration by parts, whereby
$$
\int^{\infty}_0 u dv = \left. uv \right\vert ^\infty_0 - \int^\infty_0 vdu
$$
is applied with $u = x$ and $v = -e^{-\lambda x}$:
$$
\mathbf{E}[x] = \int^\infty_{-\infty} x f_X(x)dx = \int^\infty_0x \lambda e^{-\lambda x}dx = \left[-x e^{-\lambda x}\right]^\infty_0 + \int^\infty_0 e^{-\lambda x} dx = {1\over \lambda}
$$
(c)

Integrating by parts with $u = x^2$ and $v = -e^{-\lambda x}$ in the second line below gives
$$
\begin{aligned}
\mathbf{E}[X^2] &= \int^\infty_{-\infty} x^2 f_X(x) dx = \int^\infty_0 x^2 \lambda e^{-\lambda x}dx\\
&= [-x^2 e^{-\lambda x}]^\infty_0 + 2 \int^\infty_0 x e^{-\lambda x} dx = {2\over \lambda} \mathbf{E}[X] = {2\over \lambda^2} 
\end{aligned}
$$
Combining with the previous computation, we obtain
$$
\mathsf{Var}(X) = \mathbf{E}[X^2] - (\mathbf{E}[X])^2 = {2\over \lambda^2} - \left( 1 \over \lambda \right)^2 = {1\over \lambda^2}
$$
(d) 

The maximum of a set is upper bounded by $z$ when each element of the set if upper bounded by $z$. Thus for any positive $z$,
$$
\begin{aligned}
\mathbf{P}(Z \leq z) &= \mathbf{P}(\max\{ X_1, X_2, X_3\} \leq z)\\
&= \mathbf{P}(X_1 \leq z, X_2 \leq z, X_3 \leq z)\\
&=  \mathbf{P}(X_1 \leq z)\mathbf{P}( X_2 \leq z) \mathbf{P}(X_3 \leq z)\\
&=(1-e^{-\lambda z})^3
\end{aligned}
$$
where the third equality uses the independence of $X_1, X_2,$ and $X_3$. Thus,
$$
F_Z(z) = \begin{cases}0, &\text{if }z <0\\ (1-e^{-\lambda z})^3, & \text{if } z \geq 0\end{cases}
$$
Differentiating the CDF gives the desired PDF:
$$
f_Z(z) = \begin{cases}0, &\text{if }z \leq 0\\ 3\lambda e^{-\lambda z}(1 - e^{-\lambda z})^2, &\text{if }z \geq 0 \end{cases}
$$
(e)

The minimum of a set is lower bounded by $w$ when each element of the set is lower bounded by $w$. Thus for any positive $w$,
$$
\begin{aligned}
\mathbf{P}(W \geq w) &= \mathbf{P}(\min\{ X_1, X_2\} \geq w) \\
&= \mathbf{P}(X_1 \geq w, X_2 \geq w) \\
&= \mathbf{P}(X_1 \geq w)\mathbf{P}( X_2 \geq w)\\
&= (e^{-\lambda w})^2\\
&= e^{-2 \lambda w}
\end{aligned}
$$
Where the third equality uses the independence of $X_1$ and $X_2$, Thus,
$$
F_W(w) = \begin{cases}0, &\text{if } w < 0  \\ 1 - e^{-2\lambda w},&\text{if } w \geq 0\end{cases}
$$
We can recognize this as the CDF of an exponential random variable with parameter $2\lambda$. The PDF is
$$
f_W(w) = \begin{cases}0, &\text{if } w < 0 \\ 2 \lambda e^{-2\lambda w}, &\text{if }w \geq 0\end{cases}
$$

## Problem 2 Buffon's needle

A surface is ruled with parallel lines, which are at distance $d$ from each other. Suppose that we throw a needle of length $l$ on the surface at random. What is the probability that the needle will intersect one of the lines?

**Solution**: 

Suppose $X$ represents the distance between the middle of the needle and the line, $\Theta$ represents the angle between the needle and the intersected line. They are independent.

Since $X \sim \mathsf{Unif}(0, {d\over 2})$, the PDF of $X$ is
$$
f_X(x) = {2\over d}, \quad 0 \leq x \leq {d\over 2}
$$
Since $\Theta \sim \mathsf{Unif}(0, {\pi \over 2})$, the PDF of $\Theta$ is
$$
f_\Theta(\theta) = {2\over \pi}, \quad 0 \leq \theta \leq {\pi \over 2}
$$
The needle intersects the line if 
$$
X \leq {l \over 2} \sin \theta
$$
To obtain the probability of $X \leq {l \over 2} \sin \theta$, i.e. the CDF of $X$, we first calculate the joint probability of $X$ and $\Theta$,
$$
f_{X,\Theta}(x,\theta) = {4 \over \pi d}, \quad 0 \leq x\leq d/2, \quad 0\leq \theta \leq \pi/2
$$
Therefore, we get the probability of intersection.
$$
\begin{aligned}
\mathbb{P}(X \leq {l \over 2}\sin\theta)&=\int^{n/2}_0\int^{{l\over 2} \sin \theta}_0 {4\over \pi d} ~dx d\theta\\
&= \int^{n/2}_0 {4 \over \pi d} \cdot {l \over 2} \sin \theta~ d\theta\\
&={2l \over \pi d} (-\cos\theta)|^{n/2}_0\\
&= {2l \over \pi d}
\end{aligned}
$$
