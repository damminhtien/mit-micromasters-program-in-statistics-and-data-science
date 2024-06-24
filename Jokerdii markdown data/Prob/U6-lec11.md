# Lecture 11. Derived Distribution

* Given the distribution of $X$, find the distribution of $Y = g(X)$.

  | Discrete                                                     | Continuous                                                   |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | $Y = g(X),\quad p_Y(y) = \mathbf{P}(g(X) = y) = \sum\limits_{x:g(X)=y} p_X(x)$ |                                                              |
  | $Y=aX+b, \quad p_Y(y) = p_X({y-b \over a})$                  | $Y=aX+b, \quad f_Y(y) = {1 \over \vert a \vert}f_X({y-b \over a})$ |

  * a linear function of a normal r.v. is normal

    $X \sim \mathcal{N}(\mu, \sigma^2),\quad f_X(x) = {1\over \sqrt{2\pi} \sigma} e^{-(x-\mu)^2/2\sigma^2}, \quad f_Y(y)= {1\over \vert a \vert} {1 \over \sqrt{2\pi} \sigma} e^{-({y-b \over a} - \mu)^2 /2 \sigma^2} = {1\over \sqrt{2\pi }\sigma \vert a \vert } e^{-(y-b-a\mu)^2/2 \sigma^2 a^2}$

    Therefore, if $X \sim \mathcal{N}(\mu, \sigma^2),$ then $aX+b \sim \mathcal{N}(a\mu + b, a^2 \sigma^2)$.

  * general approach, using CDFs

    1. Find the CDF of $Y$: $F_Y(y) = \mathbf{P}(Y \leq y) = \mathbf{P}(g(x) \leq y)$
    2. Differentiate: $f_Y(y) = {dF_Y\over dy} (y)$

  * general formula when $g$ is monotonic (strictly increasing or decreasing)

    $Y=g(x), \quad f_Y(y) = f_X(h(y))\vert {dh \over dy}(y) \vert$,   where $h(y)$ is the inverse function of $g(x)$.

  * Non-monotonic example $Y = X^2$

    * Discrete case: $p_Y(y) = p_X(\sqrt{y}) + p_X(-\sqrt{y})$

    * Continuous cases:

      $F_Y(y) = \mathbf{P}(Y \leq y) = \mathbf{P}(X^2 \leq y) = \mathbf{P}(\vert x \vert \leq \sqrt{y}) = \mathbf{P}(-\sqrt{y} \leq x \leq \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$

      $f_Y(y) = f_X(\sqrt{y}) {1\over 2 \sqrt{y}} - f_X(-\sqrt{y}){-1\over 2 \sqrt{y}}$

* Given the (joint) distribution of $X$ and $Y$, find the distribution of $Z = g(X,Y)$

  Let $Z = Y/X; X,Y$ independent, uniform on $[0,1]$.
  $$
  F_Z(z) = \mathbf{P}(Y/X \leq z) = \begin{cases}0 & z < 0\\ {1\over 2} z, & 0 \leq z \leq1 \\ 1 - {1\over 2z},\quad &z > 1 \end{cases} 
  $$
  ![lec11-multiple-rv](../assets/images/lec11-multiple-rv.png)

There are 3 selected exercises and 4 solved problems.

---

## Exercise 1 PDF of a general function

The random variable $X$ has a PDF of the form
$$
f_ X(x)=\begin{cases}  \displaystyle {\frac{1}{x^2},}&  \text{for }x\geq 1,\\ 0,& \text{otherwise.} \end{cases}
$$
Let $Y = X^2$. For $y \geq 1$, the PDF of $Y$ takes the form $f_Y(y) = {a \over y^b}.$ Find the values of $a$ and $b$.

**Solution**: 

For any $y \geq 1$, we have
$$
F_ Y(y)=\mathbf{P}(Y\leq y)=\mathbf{P}(X^2\leq y)=\mathbf{P}(X\leq \sqrt{y})=F_ X(\sqrt{y}).
$$
By differentiating and using the chain rule, we have
$$
f_ Y(y)=\frac{1}{2\sqrt{y}}f_ X(\sqrt{y})=\frac{1}{2y^{1.5}}.
$$

## Exercise 2 Using the formula for the monotonic case

The random variable $X$ is **exponential** with parameter $\lambda = 1$. The random variable $Y$ is defined by $Y = g(X) = 1/(1+X)$. For $y \in (0,1]$, find the PDF of $Y$: $f_Y(y)$.

**Solution**:

The exponential PDF of $X$ with parameter $\lambda =  1$ is
$$
f_X(x) = e^{-x}
$$
First find the inverse function,
$$
h(y) = {1-y \over y} = {1\over y} - 1
$$
Then find
$$
{dh\over dy}(y) = - {1\over y^2}
$$
Therefore,
$$
f_Y(y) = f_X(h(y)) \vert {dh \over dy} (y) \vert = e^{- (1/y) + 1} \cdot {1\over y^2}
$$

## Exercise 3 Nonmonotonic functions

Suppose that $X$ is a continuous random variable and that $Y = X^4$. Then, for $y \geq 0$, what is the PDF of $y$: $f_Y(y)$?

**Solution**: 

We have, for $y \geq 0$,
$$
F_ Y(y)=\mathbf{P}(Y\leq y)=\mathbf{P}(X^4\leq y)=\mathbf{P}(-y^{1/4}\leq X \leq y^{1/4}) =F_ X(y^{1/4})- F_ X(-y^{1/4}).
$$
By differentiating, and using also the chain rule, we obtain
$$
f_ Y(y)=f_ X(y^{1/4}) \cdot \frac{1}{4}\cdot y^{-3/4} +f_ X(-y^{1/4}) \cdot \frac{1}{4}\cdot y^{-3/4}.
$$

## Problem 1 The PDF of the absolute value of $X$

Let $X$ be a random variable with PDF $f_X$. Find the PDF of the random variable $Y = |X|$.

1. When $f_ X(x) \  = \    \begin{cases} 1/3, &  \text{if }-2 < x \leq 1, \\ 0, &  \text{otherwise}; \end{cases} $
2. For general $f_X(x)$.

**Solution**:

1. $f_X(x)$ for $-1 \leq x \leq 0$ gets added to $f_X(x)$ for $0 \leq x \leq 1$, so
   $$
   f_Y(y) = \begin{cases}2/3, &\text{if }0\leq y\leq 1,\\ 1/3, &\text{if }1 < y \leq 2,\\ 0, &\text{otherwise}. \end{cases}
   $$

2. When $y \geq 0$,
   $$
   \mathbf{P}(Y \leq y) =\mathbf{P}(|X| \leq y)   = \mathbf{P}(-y\leq X \leq y)=\int^y_{-y}f_X(x)dx = F_X(y) - F_X(-y).
   $$
   Taking derivatives of both sides, we have
   $$
   f_Y(y) = f_X(x) + f_X(-y), \quad y \geq 0.
   $$
   Therefore, the PDF of $Y$ is
   $$
   f_Y(y) = \begin{cases} f_X(x) + f_X(-y), \quad & \text{if }y \geq 0\\ 0, \quad & \text{if }y < 0 \end{cases}
   $$


## Problem 2 Derived distribution

Let $X$ have the normal distribution with mean $0$ and variance $1$, i.e.,
$$
f_ X(x) \  = \  \frac{1}{\sqrt{2\pi }} e^{-x^2/2}.
$$
Also, let $Y = g(X)$ where
$$
g(t) \  = \    \begin{cases} -t, &  \text{for } t \leq 0; \\ \sqrt{t}, &  \text{for }t > 0, \end{cases} 
$$
Find the PDF of $Y$.

**Answer**: $f_Y(y) = {1\over \sqrt{2\pi}} \left( 2y e^{-y^4/2} + e^{-y^2/2}\right)$

**Solution**:

Because of the definition of $g$, the random variable $Y$ takes on only non-negative values. Thus $f_Y(y)=0$ for any negative $y$. 

For $y>0$,
$$
\begin{aligned}
F_Y(y) &= \mathbf{P}(Y \leq y)\\
&= \mathbf{P}(X \in [-y, 0]) + \mathbf{P}(X \in (0,y^2])\\
&= \mathbf{P}(-y \leq X \leq y^2)\\
&= F_X(y^2) - F_x(-y).
\end{aligned}
$$
Taking the derivative of $F_Y(y)$ (and using the chain rule),
$$
\begin{aligned}
f_Y(y) & = 2yf_X(y^2) + f_X(-y)\\
&= {1\over \sqrt{2\pi}} \left( 2y e^{-y^4/2} + e^{-y^2/2}\right).
\end{aligned}
$$

## Problem 3 Ambulance travel time

An ambulance travels back and forth, at a constant speed , along a road of length . We may model the location of the ambulance at any moment in time to be uniformly distributed over the interval . Also at any moment in time, an accident (not involving the ambulance itself) occurs at a point uniformly distributed on the road; that is, the accident's distance from one of the fixed ends of the road is also uniformly distributed over the interval . Assume the location of the accident and the location of the ambulance are independent.

Supposing the ambulance is capable of **immediate** U-turns, compute the CDF and PDF of the ambulance's travel time to the location of the accident.

**Solution**:

We want to compute the CDF of the ambulance's travel time $T, \mathbf{P}(T \leq t) = \mathbf{P}(|X - Y| \leq vt)$, where $X$ and $Y$ are the locations of the ambulance and accident (uniform over $[0,l]$). Since $X$ and $Y$ are independent, we know:
$$
f_{X,Y}(x,y) = \begin{cases} {1\over l^2}, \quad &\text{if }0\leq x,y \leq l\\0, \quad &\text{otherwise} \end{cases}
$$

$$
\begin{aligned}
\mathbf{P}(T \leq t) &= \mathbf{P}(|X - Y| \leq vt) = \mathbf{P}(-vt \leq Y-X \leq vt)\\
&= \mathbf{P}(X - vt \leq Y \leq X + vt)
\end{aligned}
$$

We can see that $ \mathbf{P}(X - vt \leq Y \leq X + vt)$ corresponds to the integral of the joint density of $X$ and $Y$ over the shaded region in the figure below.

![u6-lec11-prob3](../assets/images/u6-lec11-prob3.png)

Because the joint density is uniform over the entire region, for $0 \leq t \leq {l \over  v}$,
$$
F_T(t) = (1/l^2) \times {1\over 2}\times (1-vt)^2 \times 2 = {2vt \over l} - {(vt)^2\over l^2}
$$
Therefore, we have
$$
F_T(t) = (1/l^2) \times (\text{Shaded area}) = \begin{cases}0, \quad &\text{if }t < 0\\ {2vt \over l} - {(vt)^2\over l^2}, &\text{if }0 \leq t \leq {l \over v}\\ 1, \quad &\text{if }t \geq {l \over v} \end{cases}
$$
By differentiating the CDF, we find the density of $T$:
$$
f_T(t) = \begin{cases}{2v\over l} - {2v^2 t \over l^2}, &\text{if } 0\leq t\leq {l\over v}\\ 0, \quad &\text{otherwise} \end{cases}
$$

## Problem 4 The PDF of the maximum

Let $X$ and $Y$ be independent random variables, each uniformly distributed on the interval $[0,1s]$.

1. Let $Z = \max\{X,Y\}$. Find the PDF of $Z$ for $0 < z < 1$.
2. Let $Z = \max \{ 2X,Y\}$. Find the PDF of $Z$, for $0 < z < 1$ and for $1 < z < 2$ respectively.

**Solution:**

1. The CDF of a random variable $U$ distributed uniformly on the interval $[0,1]$ is given by
   $$
   F_ U(u) = \begin{cases}  0, &  \text{if } u<0, \\ u, &  \text{if } 0\leq u\leq 1, \\ 1, &  \text{if } u>1.\end{cases}
   $$
   Let $Z = \max\{X,Y\}$. For $Z \in (0,1)$,
   $$
   \begin{aligned}
   {F}_ Z{(z)} &= \mathbf{P}(Z \leq z)\\
   &= \mathbf{P}(X \leq z \text { and } Y \leq z)\\
   &= {{F}}_ X(z) {{F}}_ Y(z)\\
   &= z^2
   \end{aligned}
   $$
   Hence, 
   $$
   f_ Z(z) = 2z
   $$

2. Let $Z = \max \{ 2X, Y\}$, the CDF is
   $$
   {F}_ Z{(z)} = \mathbf{P}(Z \leq z) = \mathbf{P}(2X \leq z \text { and } Y\leq z)={{F}}_{X}(z/2) {F}_ Y(z).
   $$
   Hence, for $0 < z < 1$, the CDF is
   $$
   {{F}}_ Z(z) = (z/2)\cdot z = z^2/2
   $$
   and the corresponding PDF is
   $$
   f_ Z(z) = z
   $$
   For $1 < z <2$, the CDF is
   $$
   {{F}}_ Z(z) = (z/2)\cdot 1 = z/2
   $$
   and the corresponding PDF is
   $$
   f_ Z(z) = 1/2
   $$

