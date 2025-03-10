# Lecture 12. Sums of independent r.v.'s; Covariance and correlation

* The PMF/PDF of $X + Y$ ($X$ and $Y$ independent)

  | Discrete                                | Continuous                                                   |
  | --------------------------------------- | ------------------------------------------------------------ |
  | $p_Z(z) = \sum\limits_x p_X(x)p_Y(z-x)$ | $f_Z(z) = \int^\infty_{-\infty} f_X(x) f_Y(z-x)dx$           |
  |                                         | $f_{Z|X}(z|x) = f_Y(z-x);\\ f_{x + b}(x) = f_X(x-b);\\f_{X,Z}(x,z) = f_X(x)f_Y(z-x)$ |

  * the sum of independent normals

    Given $X \sim \mathcal{N}(\mu_x \sigma_x^2), Y \sim \mathcal{N(\mu_y, \sigma_y^2)}$ are independent, $Z = X + Y$.

    $f_X(x)= {1\over \sqrt{2 \pi} \sigma_x} e^{-(x - \mu_x)^2/2 \sigma_x^2}; \quad f_Y(y)= {1\over \sqrt{2 \pi} \sigma_y} e^{-(y - \mu_y)^2/2 \sigma_y^2}$
    $$
    \begin{aligned}
    f_Z(z) &= \int^\infty_{-\infty} f_X(x) f_Y(z-x) dx\\
    &=\int^\infty_{-\infty}{1\over \sqrt{2\pi} \sigma_x}\exp\left(  - {(x-\mu_x)^2\over 2\sigma_x^2}\right) {1\over \sqrt{2\pi} \sigma_y} \exp \left( - {(z-x-\mu_y)^2\over 2 \sigma^2_y } \right) dx \\
    &= {1\over \sqrt{2\pi} (\sigma_x^2 + \sigma_y^2) } \exp \left( - {(z-\mu_x - \mu_y)^2 \over2(\sigma_x^2 + \sigma_y^2) }\right) \quad  \sim \mathcal{N}(\mu_x + \mu_y, \sigma_x^2 + \sigma^2_y)
    \end{aligned}
    $$

* A linear function of two independent continuous random variables
  $$
  f_{aX}(y) = {1\over |a|}f_X({y \over a})
  $$
  Example: What is the PDF of $2X-Y$? (For independent $X,Y$)
  $$
  \begin{aligned}
  f_{2X-Y}(z) &= \int^\infty_{-\infty} f_{2X}(x) f_{-Y}(z-x)dx\\
  \text{Each part:} &\\
  f_{2X}(x) &= {1\over 2}f_X({x\over 2})\\
  f_{-Y}(y) &= f_Y(-y)\\  
  f_{-Y}(z-x) &= f_Y(x-z)\\
  \text{Therefore:} \\
  \implies f_{2X-Y}(z) &= \int^\infty_{-\infty} {1\over 2} f_X(x/2) f_Y(x-z)dx
  \end{aligned}
  $$
  
* Covariance

  * definition

    $\mathsf{cov}(X,Y) = \mathbf{E}\left[(X-\mathbf{E}[X]) \cdot (Y - \mathbf{E}(Y))\right]$

  * independence

    $\mathsf{cov}(X,Y) = \mathbf{E}\left[(X-\mathbf{E}[X]) \cdot (Y - \mathbf{E}(Y))\right] = \mathbf{E}[(X-\mathbf{E}(X))] \cdot \mathbf{E}[(Y-\mathbf{E}(Y))]$

    Independence $\implies \mathsf{cov}(X,Y) = 0$, converse is not true.

  * mathematical properties

    $\mathsf{cov}(X,X) = \mathbf{E}[(X - \mathbf{E}[X])^2] = \mathsf{Var}(X) = \mathbf{E}[X^2] - (\mathbf{E}[X])^2$

    $\mathsf{cov}(aX + b, Y) = a \cdot \mathsf{cov}(X,Y)$
  
    $\mathsf{cov}(X,Y+Z) = \mathsf{cov}(X,Y) + \mathsf{cov}(X,Z)$
  
    $\mathsf{cov}(X, Y) = \mathbf{E}[XY] - \mathbf{E}[X]\mathbf{E}[Y]$
  
  * variance of a sum of random variables
  
    $\mathsf{Var}(X_1 + X_2) = \mathsf{Var}(X_1) + \mathsf{Var}(X_2) + 2 \mathsf{cov}(X_1, X_2)$
  
    $\mathsf{Var}(X_1 + ... + X_n) = \sum\limits^n_{i=1}\mathsf{Var}(X_i) + \sum\limits_{\{(i,j): i \neq j\}} \mathsf{cov}(X_i ,X_j)$
  
* Correlation

  * definition: correlation is the dimensionless version of covariance; measure of the degree of "association" between $X$ and $Y$.

  * $\rho(X,Y) = \mathbf{E}\left[{(X-\mathbf{E}(X)) \over \sigma_X} \cdot {(Y-\mathbf{E}(Y)) \over \sigma_Y}\right] = {\mathsf{cov}(X,Y) \over\sigma_X \sigma_Y }, \quad -1 \leq \rho \leq 1$

  * Independent $\implies \rho = 0,$ "uncorrelated" (converse is not true).

  * $\vert \rho \vert = 1 \iff (X - \mathbf{E}[X]) = c(Y - \mathbf{E}[Y]) $ (linearly related)

  * $\mathsf{cov}(aX + b, Y) = a \cdot \mathsf{cov}(X,Y) \implies \rho(aX + b,Y) = {a \cdot \mathsf{cov}(X,Y) \over \vert a \vert \sigma_x \sigma_y} = \mathsf{sign}(a) \cdot \rho(X,Y)$

  * Example:

    A real-estate investment company invests \$ 10M in each of $10$ states. At each state $i$, the return on its investment is a random variable $X_i$, with mean $1$ and standard deviation $1.3$ (in millions). Find the variance of the sum of variables.

    $\mathsf{Var}(X_1 + ... + X_{10}) = \sum\limits^{10}_{i=1}\mathsf{Var}(X_i) + \sum\limits_{\{(i,j): i \neq j\}} \mathsf{cov}(X_i ,X_j)$

    If the $X_i$ are uncorrelated, then:

    $\mathsf{Var}(X_1 + ... + X_{10}) = 10 \cdot (1.3)^2 = 16.9$

    $\sigma(X_1 + ... + X_{10}) = 4.1$

    If for $i \neq j$, suppose $\rho(X_i, X_j) = 0.9$

    $\mathsf{Var}(X_1 + ... + X_{10}) = 10 \cdot (1.3)^2  +90 \cdot 1.52 = 154$

    $\sigma(X_1 + ... + X_{10}) = 12.4$.

There are 5 selected exercises and 4 solved problems.

---

## Exercise 1 Discrete convolution

The random variables $X$ and $Y$ are independent and have the PMFs shown in this diagram.

![U6-lec12-ex1](../assets/images/U6-lec12-ex1.png)

What is the probability that $X + Y = 6$?

**Solution**:

We flip the PMF of $Y$ to obtain a PMF on the set $\{-4,-3,-2\}$ . We shift it to the right by $6$ and place it underneath the PMF of $X$. By multiplying the probabilities that are on top of each other in the resulting diagram, we obtain
$$
p_{X+Y}(6)=\frac{1}{6}\cdot \frac{3}{6}+\frac{3}{6}\cdot \frac{2}{6}=\frac{9}{36}=1/4.
$$

## Exercise 2 Continuous convolution

When calculating the convolution of two PDFs, one must be careful to use the appropriate limits of integration. Suppose that $X$ and $Y$ are nonnegative random variables. In particular, $f_X(x)$ is equal to some positive function $$h_X(x)$$ for $x \geq 0$ and is zero for $x < 0$. Similarly, $f_Y(y)$ is equal to some positive function $h_Y(y)$ for $y \geq 0$ , and is zero for $y <0$ . Then, the convolution integral $\int^\infty_{-\infty} f_X(x) f_Y(z-x)$ is of the form
$$
\int _ a^ b h_ X(x) h_ Y(z-x)\, dx,
$$
for suitable choices of $a$ and $b$ determined by $z$. Fix some $z \geq 0$. Find $a$ and $b$.

**Answer**: $a = 0, b = z$. 

**Solution**:

The integrand is equal to $h_X(x)h_Y(z-x)$ only for those choices of $x$ for which the arguments of the functions $h_X$ and $h_Y$ are nonnegative; that is, when $x \geq 0$ and $z -x \geq 0$, which yields $0 \leq x \leq z$. Thus, we should only integrate from $0$ to $z$.

## Exercise 3 Covariance calculation

Suppose that $X,Y,$ and $Z$ are independent random variables with unit variance. Furthermore, $\mathbf{E}[X] = 0$ and $\mathbf{E}(Y) = \mathbf{E}(Z)=  2$. Then, what is $\mathsf{cov}(XY, XZ)$?

**Solution**: 

Because of independence and the zero-mean assumption, it follows that $\mathbf{E}[XY] = \mathbf{E}[X] \cdot \mathbf{E}[Y] = 0$ and similarly $\mathbf{E}[XZ] =0$. Thus,
$$
\textsf{Cov}(XY,XZ)={\bf E}[XYXZ]={\bf E}[X^2 YZ]={\bf E}[X^2]\cdot {\bf E}[Y] \cdot {\bf E}[Z]= \textsf{Var}(X)\cdot {\bf E}[Y] \cdot {\bf E}[Z]=4.
$$

## Exercise 4 Covariance properties

1. Find the value of $a$ in the relation $\mathsf{Cov}(2X,-3Y+2) =a \cdot \mathsf{Cov}(X,Y)$

2. Suppose that $X,Y$, and $Z$ are independent, with a common variance of $5$. Then, find $\mathsf{Cov}(2X+Y,3X - 4Z)$

**Solution**:

1)  We have $\textsf{Cov}(aX+b,Y)=a \cdot \textsf{Cov}(X,Y)$. By symmetry, we also have $\textsf{Cov}(X,aY+b)=a \cdot \textsf{Cov}(X,Y)$. By using this relations,
$$
\textsf{Cov}(2X,-3Y+2)=2\cdot \textsf{Cov}(X,-3Y+2)=2\cdot (-3)\cdot \textsf{Cov}(X,Y)=-6\, \textsf{Cov}(X,Y).
$$
2) Using linearity,
$$
\begin{aligned}
 \textsf{Cov}(2X+Y,3X-4Z)&=\textsf{Cov}(2X+Y,3X)+\textsf{Cov}(2X+Y,-4Z)\\
 &=\textsf{Cov}(2X,3X)+\textsf{Cov}(Y,3X)+\textsf{Cov}(2X,-4Z)+\textsf{Cov}(Y,-4Z)\\
 &=6\, \textsf{Var}(X)+0+0+0=30,
\end{aligned}
$$
where the zeros are obtained because independent random variables have zero covariance.

## Exercise 5 Correlation properties

Let $Z,V,W$ be independent random variables with mean $0$ and variance $1$, and let $X= Z + V$ and $Y = Z +W$. We have found that $\rho(X,Y) = 1/2$.

1. $\rho (X,-Y)=\,?\\\rho (-X,-Y)=\,?$

2. Suppose that $X$ and $Y$ are measured in dollars. Let $X' $ and $Y'$ be the same random variables, but measured in cents, so that $X' = 100X$ and $Y' = 100Y$. Then,

   $\rho (X',Y')=\,?$

3. Suppose now thta $\tilde{X} = 3Z + 3V + 3$ and $\tilde{Y} = -2Z -2W$. Then

   $\rho (\tilde{X},\tilde{Y})=\,?$

4. Suppose now that the variance of $Z$ is replaced by a very large number. Then

   $\rho (X,Y)\,$ is close to $?$

5. Alternatively, suppose that the variance of $Z$ is close to zero. Then,

   $\rho (X,Y)\,$ is close to $?$

**Answer**:

1) $\rho (X,-Y)=\,-1/2\\\rho (-X,-Y)=\,1/2$

2) $\rho (X',Y')=\,1/2$

3) $\rho (\tilde{X},\tilde{Y})=\,-1/2$

4) $\rho (X,Y)\,$ is close to $1$

5) $\rho (X,Y)\,$ is close to $0$

**Solution**:

We saw that a linear transformation $x\mapsto ax+b$ of a random variable does not change the value of the correlation coefficient, except for a possible sign change if the coefficient $a$ is negative. 

For the last two parts, if $Z$ has a very large variance, then teh terms $V$ and $W$ become insignificant, and $\rho(X,Y) \approx \rho(Z,Z) = 1$. And if $Z$ has very small variance, then $X$ and $Y$ are approximately independent, so that $\rho(-X,-Y) \approx 0$.

## Problem 1 The difference of two independent exponential random variables

Romeo and Juliet have a date at a given time, and each, independently, will be late by an amount of time that is exponentially distributed with parameter $\lambda$. What is the PDF of the difference between their times of arrival?

**Solution**:

Let $X,Y$ be exponential random variables with parameter $\lambda$. We are interested in the PDF of difference $Z$ between $X$ and $Y$: $Z = X - Y$, denoted as $f_Z(z)$.

Recall that if $W = X + Y$, we have
$$
f_W(w)=\int^\infty_{-\infty} f_X(x)f_Y(w-x)dx
$$
We can rewrite the $Z$ as $Z = X + (-Y)$, so the PDF is
$$
f_Z(z)=\int^\infty_{-\infty} f_X(x)f_{-Y}(z-x)dx
$$
Since
$$
f_{-Y}(z -x) = f_Y(x-z)
$$
We have
$$
f_Z(z)=\int^\infty_{-\infty} f_X(x)f_{Y}(x-z)dx
$$
Recall the PDF of an exponential random variable $X$ is
$$
f_X(x) = \begin{cases}0, &x<0\\ \lambda e^{-\lambda x}, &x \geq0 \end{cases}
$$
When $z < 0$,
$$
\begin{aligned}
f_Z(z) &=\int^\infty_{0} f_X(x)f_{Y}(x-z)dx\\
&=\int^\infty_{0} \lambda e^{-\lambda x} \lambda e^{-\lambda(x-z)}dx\\
&=\lambda e^{\lambda z} \int^\infty_0 \lambda e^{-2\lambda x}dx\\
&= \lambda e^{\lambda z}\left(\right. -{1\over 2} e^{2 \lambda x} \left|^\infty_0 \right)\\
&= {\lambda \over 2}e^{\lambda z}
\end{aligned}
$$
When $z\geq 0$, since $Z = X - Y$ and $-Z = Y-X$, and $X,Y $ are i.i.d., $Z$ and $-Z$ have the same distribution $Z \stackrel{d}{=}-Z$. This means the distribution of $Z$ must be symmetric around $0$. Thus, 
$$
f_Z(z)= f_Z(-z) ={\lambda \over 2}e^{-\lambda z}
$$
Therefore,
$$
f_Z(z) = \begin{cases}{\lambda \over 2}e^{\lambda z}, &z < 0 \\{\lambda \over 2}e^{-\lambda z}, &z \geq 0 \end{cases}
$$

## Problem 2 The sum of discrete and continuous r.v.'s

Let $X$ be a discrete random variable with PMF $p_X$ and let $Y$ be a continuous random variable, independent from $X$, with PDF $f_Y$. Derive a formula for the PDF of the random variable $X+Y$.

**Solution**:

Let $Z = X+Y$. Using the 2 step CDF method,
$$
\begin{aligned}
F_Z(z) &= \mathbf{P}(Z \leq z)\\
&= \mathbf{P}(X + Y \leq z)
\end{aligned}
$$
Using the Total Probability Theorem, we have
$$
\begin{aligned}
F_Z(z) &= \sum_x p_X(x)\mathbf{P}(x + Y \leq z)\\
&= \sum_x p_X(x) \mathbf{P}(Y \leq z -x)\\
&= \sum_x p_X(x) \mathbf{P}(Y \leq z -x)\\
&= \sum_x p_X(x) F_Y(z-x)
\end{aligned}
$$
Differentiating both sides with respect to $z$, we obtain
$$
f_Z(z) = {d\over dz} F_Z(z) = \sum_x p_X(x) f_Y(z-x)
$$

## Problem 3 Convolution calculations

1. Let the discrete random variable $X$ be uniform on $\{0,1,2\}$ and let the discrete random variable $Y$ be uniform on ${3,4}$. Assume that $X$ and $Y$ are independent. Find the PMF of $X+Y$ using **convolution**. The form of the PMF is
   $$
   p_{X+Y}(z) = \left\{  \begin{array}{ll} a, & z = 3, \\ b, & z = 4, \\ c, & z = 5, \\ d, & z = 6, \\ 0, &  \text{otherwise.} \end{array} \right.
   $$

2. Let the random variable $X$ be uniform on $[0,2]$ and the random variable $Y$ be uniform on $[3,4]$ . (Note that in this case, $X$ and $Y$ are continuous random variables.) Assume that $X$ and $Y$ are independent. Let $Z = X+Y$. Find the PDF of $Z$ using convolution. Find $a,b,c,d,e$ in the graph of the PDF

   ![images_chap4_convolution1](../assets/images/images_chap4_convolution1.jpg)

**Solution:**

1. $Z = X+Y \in \{3,4,5,6\}$, by computing the probability of each $Z$, we have the PMF
   $$
   p_{X+Y}(z) = \left\{  \begin{array}{ll} 1/6, &  z\in \{ 3,6\}  \\ 1/3, &  z\in \{ 4,5\} \\ 0, &  \text{otherwise.} \end{array} \right.
   $$

2. The answer is easiest to find graphically, by sliding a rectangle of width 1 along a rectangle of width 2, and is:
   $$
   f_{X+Y}(z) = \left\{  \begin{array}{lcl} \frac{z-3}{2}, & &  3 \leq z < 4, \\ \frac{1}{2}, & &  4 \leq z < 5, \\ \frac{6-z}{2}, & &  5 \leq z \leq 6, \\ 0, & &  \text{otherwise.} \end{array}\right.
   $$
    A more formal approach involves the convolution formula, but requires careful thought in order to identify the appropriate limits of integration. In particular, if $3 \leq z \leq 6 $, we have
   $$
   \begin{aligned}
   f_{X+Y}(z) &= \int _{-\infty }^{\infty } f_ X(x) f_ Y(z-x) \,  dx\\
   &= \int _{\max (0,z-4)}^{\min (2,z-3)} \frac{1}{2} \,  dx\\
   &=  (\min (2,z-3) - \max (0,z-4))/2
   \end{aligned}
   $$
   which actually agrees with the answer obtained through the graphical method.

## Problem 4 Covariance of the multinomial

Consider $n$ independent rolls of a $k$-sided fair die with $k \geq 2$: the sides of the die are labelled $1,2,...,k$ and each side has probability $1/k$. Let the random variable $X_i$ denote the number of rolls that result in side $i$. Thus, the random vector $(X_1, ...,X_k)$ has a multinomial distribution.

1. Are $X_1$ and $X_2$ correlated?

2. Find the covariance, $\mathsf{Cov}(X_1, X_2)$, of $X_1$ and $X_2$. 

3. Suppose now that the die is biased, with a probability $p_i \neq 0$ that the result of any given die roll is $i$, for $i=1,2,...,k.$ We still consider $n$ independent rolls of this biased die and define $X_i$ to be the number of rolls that result in side $i$.

   Find $\mathsf{Cov}(X_1, X_2)$ for this cases of a biased die.

**Solution:**

1. Negatively correlated. There is a fixed number $n$ of rolls of the die. A large number of rolls that result in $1$ leaves fewer remaining rolls that could result in $2$.

2. Let $A_t$ (resp. $B_t$) be a Bernoulli random variable that is equal to $1$ if and only if the $t$th roll resulted in a $1$ (resp. 2). Note that $X_1=\sum _{t=1}^ n A_ t$ and $X_2=\sum _{t=1}^ n B_ t$, and so
   $$
   {\bf E}[X_1]={\bf E}[X_2] = {\bf E}\left[\sum _{t=1}^ n A_ t\right] = n{\bf E}[A_1] = \frac{n}{k}.
   $$
   Since a single roll of the die cannot result in both a $1$ and a $2$, at least one of $A_t$ and $B_t$ must equal $0$. Thus, $\mathbf{E}[A_tB_t]=0$. Furthermore, since different rolls are independent, $A_t$ and $B_s$ are independent when $t \neq s$. Therefore,
   $$
   {\bf E}[A_ t B_ s] = {\bf E}[A_ t]{\bf E}[B_ s] = \frac{1}{k} \cdot \frac{1}{k} = \frac{1}{k^2} \qquad \text{for} \quad t\neq s,
   $$
   and so
   $$
   \begin{aligned}
   \displaystyle  {\bf E}[X_1 X_2] &={\bf E}\left[(A_1+\cdots +A_ n)(B_1+\cdots +B_ n)\right]\\
   &= {\bf E}\left[\sum _{t=s} A_ tB_ t + \sum _{t\neq s}A_ tB_ s\right]\\
   &= n\cdot 0 + n(n-1)\cdot {\bf E}[A_1B_2]\\
   &= n(n-1)\cdot \frac{1}{k^2}.
   \end{aligned}
   $$
   Thus,
   $$
   \begin{aligned}
    {\rm cov}(X_1,X_2) &= {\bf E}[X_1 X_2]-{\bf E}[X_1]{\bf E}[X_2]\\
    &= n(n-1)\cdot \frac{1}{k^2} - \frac{n}{k}\cdot \frac{n}{k}\\
    &=  -\frac{n}{k^2}.
   \end{aligned}
   $$
   The covariance of $X_1$ and $X_2$ is negative as expected.

3. We follow the same reasoning as in (2). Let $A_t$ (resp. $B_t$) be a Bernoulli random variable that is equal to $1$ if an only if the $t$th roll resulted in a $1$ (resp. $2$). As in (2), a single roll of the die result in both a $1$ and a $2$, so $\mathbf{E}[A_tB_t]=0$. Different rolls of the die are independent, and so ${\bf E}[A_ t B_ s] = {\bf E}[A_ t]{\bf E}[B_ s] = p_1\cdot p_2$, for $t \neq s $. Thus,
   $$
   \begin{aligned}
   {\bf E}[X_1 X_2] &= {\bf E}\left[(A_1+\cdots +A_ n)(B_1+\cdots +B_ n)\right]\\
   &= {\bf E}\left[\sum _{t=s} A_ tB_ t + \sum _{t\neq s}A_ tB_ s\right]\\
   &= n\cdot 0 + n(n-1)\cdot {\bf E}[A_1B_2]\\
   &= n(n-1)p_1 p_2.
   \end{aligned}
   $$
   Note that $X_1=\sum _{t=1}^ n A_ t$ and $X_2=\sum _{t=1}^ n B_ t$, and so ${\bf E}[X_1]={\bf E}\left[\sum _{t=1}^ n A_ t\right] = n{\bf E}[A_1] = np_1$. Similarly, ${\bf E}[X_2]=np_2$.

   Therefore,
   $$
   \begin{aligned}
   {\rm cov}(X_1,X_2) &= {\bf E}[X_1 X_2]-{\bf E}[X_1]E[X_2]\\
   &= n(n-1)p_1p_2 - (np_1)(np_2)\\
   &= -np_1p_2.
   \end{aligned}
   $$
   The covariance of $X_1$ and $X_2$ is again negative.

