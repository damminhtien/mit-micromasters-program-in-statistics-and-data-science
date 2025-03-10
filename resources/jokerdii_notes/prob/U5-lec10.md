# Lecture 10. Conditioning on a random variable; Independence; Bayes' rule

* Conditioning $X$ on $Y$

  * Definition: $f_{X|Y}(x|y) = {f_{X,Y}(x,y)\over f_Y(y)}$ if $f_Y(y) > 0$.

  * Multiplication rule: $f_{X,Y}(x,y) = f_Y(y) \cdot f_{X|Y}(x|y) = f_X(x) \cdot  f_{Y|X}(y|x)$.

  * Total probability theorem and Total expectation theorem

    | Discrete                                                   | Continuous                                                   |
    | ---------------------------------------------------------- | ------------------------------------------------------------ |
    | $p_X(x) = \sum_y p_Y(y) p_{X\vert Y}(x\vert y)$            | $f_X(x) =\int^\infty_{-\infty}f_Y(y)f_{X\vert Y}(x\vert y)dy$ |
    | $\mathbf{E}[X\vert Y=y] = \sum_x x p_{X\vert Y}(x\vert y)$ | $\mathbf{E}[X\vert Y=y] = \int^\infty_{-\infty} xf_{X\vert Y}(x\vert y) dx$ |
    | $\mathbf{E}[X] = \sum_y p_Y(y) \mathbf{E}[X\vert Y=y]$     | $\mathbf{E}[X] = \int^\infty_{-\infty}f_Y(y) \mathbf{E}[X\vert Y=y] dy$ |

* Independence

  * $f_{X,Y}(x,y) = f_X(x)f_Y(y), \quad \text{for all }x \text{ and } y$.

  * $f_{X,Y}(x,y) = f_{X|Y}(x|y)f_Y(y), \quad \text{for all }x \text{ and } y$.

  * $f_{X|Y}(x|y) =f_X(x), \quad \text{for all }x \text{ and } y$.

  * If $X,Y$ are independent: 

    $\mathbf{E}[XY] = \mathbf{E}[X]\mathbf{E}[Y]$

    $\mathsf{Var}(X + Y)=\mathsf{Var}(X) + \mathsf{Var}(Y)$

    $\mathbf{E}[g(X)h(Y)] = \mathbf{E}[g(X)]\cdot \mathbf{E}[h(Y)]$

  * Independent standard normals

    $f_{X,Y}(x,y) = f_X(x)f_Y(y) \\= {1\over \sqrt{2\pi}}\exp \{-{x^2 \over 2}\} \cdot {1\over \sqrt{2\pi} }\exp \{-{y^2 \over 2}\}\\={1\over 2n} \exp \{-{1\over 2}(x^2 + y^2)\}$

  * Independent normals

    $f_{X,Y}(x,y) = f_X(x)f_Y(y)\\={1\over 2\pi \sigma_x \sigma_y}\exp\{-{(x-\mu_x)^2\over 2\sigma_x^2}-{(y-\mu_y)^2\over s\sigma_y^2}\}$

* A comprehensive example

  Break a stick of length $l$ twice: first break at $X$, $X \sim \mathsf{Unif}[0,l]$; second break at $Y$, $Y \sim \mathsf{Unif}[0,X]$.

  * Given PDFs $f_X(x) = 1/l,\quad f_Y(y) = 1/x, \quad 0\leq y \leq x \leq l$.
  * The joint PDF is $f_{X,Y}(x,y) =f_X(x)f_{Y|X}(y|x) = {1\over lx}$.
  * The marginal PDF is $f_Y(y) = \int f_{X,Y}(x,y)dx = \int^l_y {1\over lx} dx = {1\over l} \log({l\over y })$.
  * The expectation of $Y$ is $\mathbf{E}[Y] = \int^l_0 y {1\over e}\log ({l\over y})dy.$
  * Or using total expectation theorem: $\mathbf{E}[Y] = \int^l_0 {1\over e} \mathbf{E}[Y|X=x]dx = \int^l_0 {1\over e} {x \over 2} dx = {1\over 2}\mathbf{E}[X] = {1\over 2} \cdot {l \over 2} = {l \over 4}$.

* Four variants of the Bayes rule

  | Type                           | Formula                                                      |
  | ------------------------------ | ------------------------------------------------------------ |
  | $X$ discrete, $Y$ discrete     | $p_{X\vert Y}(x \vert y) = {p_X(x) p_{Y \vert X}(y \vert x) \over p_Y(y)} \\ p_Y(y) = \sum_{x'}p_X(x') p_{Y\vert X}(y \vert x')\\p_{Y\vert X}(y \vert x) = { p_Y(y) p_{X\vert Y} (x \vert y)\over p_X(x)}\\ p_X(x) = \sum_{y'} f_Y(y') p_{X \vert Y} (x \vert y')$ |
  | $X$ discrete, $Y$ continuous   | $p_{X\vert Y}(x \vert y) = {p_X(x) f_{Y \vert X}(y \vert x) \over f_Y(y) }\\ f_Y(y) = \sum_{x'}p_X(x') f_{Y\vert X}(y \vert x')\\f_{Y\vert X}(y \vert x) = { f_Y(y) p_{X\vert Y} (x \vert y)\over p_X(x)}\\ p_X(x) = \int f_Y(y') p_{X \vert Y} (x \vert y') dy'$ |
  | $X$ continuous, $Y$ discrete   | $f_{X\vert Y}(x \vert y) = {f_X(x) p_{Y \vert X}(y \vert x) \over p_Y(y) }\\ p_Y(y) = \int f_X(x') p_{Y\vert X}(y \vert x')dx'\\p_{Y\vert X}(y \vert x) = { p_Y(y) f_{X\vert Y} (x \vert y)\over f_X(x)}\\ f_X(x) = \sum_{y'} p_Y(y') f_{X \vert Y} (x \vert y')$ |
  | $X$ continuous, $Y$ continuous | $f_{X\vert Y}(x \vert y) = {f_X(x) f_{Y \vert X}(y \vert x) \over f_Y(y) }\\ f_Y(y) = \int f_X(x') p_{Y\vert X}(y \vert x')dx'\\f_{Y\vert X}(y \vert x) = { f_Y(y) f_{X\vert Y} (x \vert y)\over f_X(x)}\\ f_X(x) = \int f_Y(y') f_{X \vert Y} (x \vert y') dy'$ |

There are 3 selected exercises and 3 solved problems.

---

## Exercise 1 Conditional PDFs

The random variables $X$ and $Y$ are jointly continuous, with a joint PDF of the form
$$
f_{X,Y}(x,y)=\begin{cases}  cxy,&  \mbox{if } 0\leq x\leq y\leq 1,\\ 0,&  \mbox{otherwise,}\end{cases}
$$
where $c$ is a normalizing constant.

For $x\in [0,0.5]$, the conditional PDF $f_{X|Y}(x\, |\, 0.5)$ is of the form $ax^b$. Find $a$ and $b$.

**Answer**: $a = 8, b = 1.$

**Solution**: 

By Bayes' Theorem,
$$
f_{X|Y}(x\, |\, 0.5)=\frac{f_{X,Y}(x,0.5)}{f_ Y(0.5)}.
$$
Having fixed $y = 0.5$, the conditional PDF is to be viewed as a function of $x$. For those values of $x$ that are possible (i.e. $x \in [0,0.5]$), the conditional PDF will be proportional to the joint PDF, hence of the form $ax$, for some constant $a$. This implies that $b =1$. To find the normalizing constant, we use normalization equation.
$$
1=\int _0^{0.5} f_{X|Y}(x\, |\, 0.5)\,  dx=\int _0^{0.5} ax\,  dx = a \cdot \frac{x^2}{2}\Big|_0^{0.5} =\frac{a}{8},
$$
which yields $a = 8$.

## Exercise 2 Expected value rule and total expectation theorem

Let $X, Y$, and $Z$ be jointly continuous random variables. Assume that all conditional PDFs and expectations are well defined. E.g., when conditioning on $X=x$, assume that is such that $f_X(x) > 0$. For each one of the following formulas, state whether it is true for all choices of the function $g$ or false (i.e., not true for all choices of $g$).

1) $\mathbf{E}(g(Y)| X=x) = \int g(y) f_{Y|X}(y|x) dy$

True. 

2) $\mathbf{E}(g(y)| X=x) = \int g(y) f_{Y|X}(y|x) dy$

False. $g(y)$ is a number (not a random variable). The LHS is a function of $y$, whereas on the RHS $y$ is a dummy variable that gets integrated away.

3) ${\bf E}\big [g(Y)\big ] =\displaystyle {\int } {\bf E}\big [g(Y)\, |\, Z=z\big ]\,  f_ Z(z)\,  dz$

True.

4) ${\bf E}\big [g(Y)\, |\, X=x, Z=z\big ]=\displaystyle {\int } g(y) f_{Y|X,Z}(y\, |\, x,z)\,  dy$

True.

5) ${\bf E}\big [g(Y)\, |\, X=x\big ] =\displaystyle {\int } {\bf E}\big [g(Y)\, |\, X=x,Z=z\big ]\,  f_{Z|X}(z\, |\, x)\,  dz$

True.

6) ${\bf E}\big [g(X,Y)\, |\, Y=y\big ]= {\bf E}\big [g(X,y)\, |\, Y=y\big ]$

True.

7) ${\bf E}\big [g(X,Y)\, |\, Y=y\big ]= {\bf E}\big [g(X,y)\big ]$

False. Given that $Y=y$, we need to somehow take into account the conditional distribution of $X$, whereas the RHS is determined by the unconditional PDF of $X$.

8) ${\bf E}\big [g(X,Z)\, |\, Y=y\big ]= \displaystyle {\int } g(x,z) f_{X,Z|Y}(x,z\, |\, y)\,  dy$

False. The LHS is a function of $y$, whereas the RHS (after $y$ is integrated out) is a function of $x$ and $z$. The correct form (expected value rule, in a conditional model) is
$$
{\bf E}\big [g(X,Z)\, |\, Y=y\big ]= \int \int g(x,z) f_{X,Z|Y}(x,z\, |\, y)\,  dx\,  dz.
$$


## Exercise 3 Independence and CDFs

1. Suppose that $X$ and $Y$ are independent. Is it true that their joint CDF satisfies $F_{X,Y}(x,y)=F_ X(x)F_ Y(y),$ for all $x$ and $y$.
2. Suppose that $F_{X,Y}(x,y)=F_ X(x)F_ Y(y),$ for all $x$ and $y$. Is it true that $X$ and $Y$ are independent? (Hint: $f_{X,Y}(x,y)=(\partial ^2/\partial x\partial y)F_{X,Y}(x,y)$).

1) True.
$$
\begin{aligned}
F_{X,Y}(x,y) &= \mathbf{P}(X\leq x, Y\leq y)\\
&= \int _{-\infty }^ y \int _{-\infty }^ x f_{X,Y}(x,y)\,  dx\,  dy\\
&=\int _{-\infty }^ x f_ X(x)\,  dx \int _{-\infty }^ y f_ Y(y)\, dy\\
&=F_ X(x)F_ Y(y).
\end{aligned}
$$
2) True.
$$
\begin{aligned}
f_{X,Y}(x,y) &= \frac{\partial ^2}{\partial x\partial y}F_{X,Y}(x,y)\\
&= \frac{\partial ^2}{\partial x\partial y}F_{X}(x) F_ Y(y)\\
&= \frac{\partial }{\partial x} F_ X(x) \frac{\partial }{\partial y} F_ Y(y)\\
&= f_ X(x) f_ Y(y)
\end{aligned}
$$
and therefore we have independence.

## Problem 1 The Bayes rule with continuous random variables

Let $X$ and $Y$ be independent continuous random variables with PDFs $f_X$ and $f_Y$ , respectively, and let $Z = X + Y$.

Show that $f_{Z|X}(z|x) = f_Y(z - x)$ . *Hint:* Write an expression for the conditional CDF of given , and differentiate.

**Solution**:

We first find CDF,
$$
\begin{aligned}
\mathbb{P}(Z \leq z| X=x) &= \mathbb{P}(X+Y \leq z | X=x)\\ 
&= \mathbb{P}(X + Y\leq z | X=x)\\
&= \mathbb{P}(X + Y\leq z)\\
&= \mathbb{P}(Y \leq z - x)\\
&= F_Y(z-x)\\
\end{aligned}
$$
Then differentiate it, we get
$$
f_{Z|X}(z|x) = f_Y(z - x)
$$
**Remark**: Combining it with Bayes' Theorem, we can easily solve many problems.
$$
f_{X|Z}(x|z) = {f_X(x) f_{Z|X}(z|x)\over f_Z(x)}\\
f_{Z|X}(z|x) = f_Y(z - x)
$$


## Problem 2 Sophia's vacation

Sophia is vacationing in Monte Carlo. On any given night, she takes $X$ dollars to the casino and returns with $Y$ dollars. The random variable $X$ has the PDF shown in the figure. Conditional on $X = x$, the continuous random variable $Y$ is uniformly distributed between zero and $3x$.

![lec10-prob2](../assets/images/lec10-prob2.jpg)

1. Determine the joint PDF $f_{X,Y}(x,y).$

   a. If $0 < x < 40$ and $0 < y < 3x$

   b. If $y < 0$ or $y > 3x$

2. On any particular night, Sophia makes a profit $Z = Y-X$ dollars. Find the probability that Sophia makes a positive profit, that is, find $\mathbf{P}(Z > 0)$.

3. Find the PDF of $Z$: $f_Z(z)$. Express your answers in terms of $z$.

   a. If $-40 < z < 0$

   b. If $0 < z < 80$

   c. If $z < -40$ or $z > 80$

4. What is $\mathbf{E}[Z]$?

**Solution**: 

1) First reveal $f_X(x)$ by observing the figure
$$
1 = \int^\infty_{-\infty} f_X(x) dx = \int^{40}_0 ax dx = 800a
$$
Hence,
$$
f_X(x) = {x \over 800}
$$
Given
$$
f_{Y|X} (y | x) =  {1\over 3x} \quad \text{for }0 < y < 3x
$$
By using $f_{Y|X}(y\mid x)=\frac{1}{3x}$. We obtain the following expression for the joint density
$$
f_{X,Y}(x,y)=\left\{ \begin{array}{ll}\displaystyle \frac{1}{2400},&  \text { if } 0<x<40\text { and }0<y<3x\\ 0,& \text {otherwise.}\end{array}\right.
$$
2) The first approach is to consider the region where Sophia makes positive profit. Notice that, this region consists of pairs $(x,y)$ , where $y > x$. Intersecting this region with the region where the joint density is non-negative, we need to consider
$$
\{(x,y): 0 < x < 40, x < y < 3x\}
$$
Thus, the joint CDF is
$$
\mathbf{P}(Y > X)=\int _0^{40} \int _ x^{3x}f_{X,Y}(x,y)\; dy\; dx=\int _0^{40}\int _ x^{3x}\frac{1}{2400}\; dy\; dx=\int _0^{40} \frac{x}{1200}=\frac{2}{3}.
$$
We could have also arrived at this answer by realizing that for each possible value of $X$, there is a probability that $Y>X$, and therefore by the total probability theorem,
$$
\begin{aligned}
\mathbf{P}(Y>X) &=\int _0^{40}\mathbf{P}(Y>X\mid X=x)f_ X(x)\; dx\\
&=\int _0^{40}\frac{2}{3}f_ X(x)\; dx\\
&= {2\over 3}
\end{aligned}
$$
where the last equality follows because a PDF always integrates to $1$, over the region where it is nonzero.

3) Given $X = x$, $Y$ is uniformly distributed on $[0,3x]$, hence $Z = Y-x$ is uniform over $[-x, 2x]$. Thus,
$$
f_{Z|X}(z\mid x)=\frac{1}{3x}, \quad \text { for }-x\leq z\leq 2x.
$$
Therefore,
$$
f_{X,Z}(x,z)=f_ X(x)f_{Z|X}(z\mid x)=\frac{x}{800}\frac{1}{3x}=\frac{1}{2400},\text { for }0<x<40\text { and }-x\leq z \leq 2x.
$$
Now, we will integrate over $x$ to compute the marginal density $f_Z(z)$. Note that, $x \geq -z$ and $x \geq {z \over 2}$ must be satisfied at the same time (in order for $f_{X,Z}$ to be non-zero).

If $-40 < z < 0$, the range of integration is $-z < x < 40$. Hence,
$$
f_{Z}(z)=\int _{-z}^{40}\frac{1}{2400}\; dx=\frac{40+z}{2400}.
$$
If $0 < z < 80$, the range of integration is $z/2 \leq x \leq 40$. Hence,
$$
f_ Z(z)=\int _{z/2}^{40}\frac{1}{2400}\; dx=\frac{80-z}{4800}.
$$
Therefore, the pdf of $Z$ is
$$
f_ Z(z)=\left\{ \begin{array}{ll}\displaystyle \frac{40+z}{2400},& -40<z<0\\ \displaystyle \frac{80-z}{4800},& 0<z<80\\ 0, & \text {otherwise.}\end{array}\right.
$$
4) First, calculate $\mathbf{E}[Y|X=x]$, for any $x \in [0,40]$:
$$
\begin{aligned}
\mathbf{E}[Y|X=x] &= \int^{3x}_0 y f_{Y|X}(y|x) dy\\
&= \int^{3x}_0 {y \over 3x} dy\\
&= \left[ {1\over 6} \cdot {y^2 \over x} \right]^{3x}_0\\
&= {1\over 6x} (9x^2 - 0)\\
&= {3\over 2} x
\end{aligned}
$$
Thus, using the total expectation theorem,
$$
\begin{aligned}
{\bf E}[Y] &=\int _0^{40}{\bf E}[Y|X=x]f_ X(x)\; dx\\
&=\frac{3}{2}\int _0^{40}xf_ X(x)\; dx\\
&=\frac{3}{2}{\bf E}[X].
\end{aligned}
$$
Since, $Z = Y - X$, we have, using linearity of expectation, $\mathbf{E}[Z] = \mathbf{E}[Y] - \mathbf{E}[X] = {1\over 2} \mathbf{E}[X].$

Now, 
$$
{\bf E}[X]=\int _0^{40}xf_ X(x)\; dx=\int _0^{40}\frac{x^2}{800}\; dx=\frac{80}{3}.
$$
Hence, ${\bf E}[Z]=40/3$.

## Problem 3 A joint PDF on a triangular region

This figure below describes the joint PDF of the random variables $X$ and $Y$. These random variables take values in $[0,2]$and $[0,1]$, respectively. At $x=1$, the value of the joint PDF is $1/2$.

![lec10-prob3-1](../assets/images/lec10-prob3.png)

1. Are $X$ and $Y$ independent?

2. Find $f_X(x)$. Express your answers in terms of $x$.

   a. If $0 < x < 1$,

   b. If $1 < x < 2$,

   c. If $x < 0$ or $x \geq 2$,

3. Find $f_{Y|X}(y | 0.5)$

   a. If $0 < y < 1/2$,

   b. If $y < 0$ or $y > 1/2$,

4. Find $f_{X\mid Y}(x\mid 0.5)$

   a. If $1/2<x<1$,

   b. If $1 < x < 3/2$,

   c. If $x < 1/2$ or $x > 3/2$,

5. Let $R = XY$ and let $A$ be the event that $\{ X < 0.5\}$. Find $\mathbf{E}[R|A]$

**Solution**: 

1) 

Since $X$ gives information about $Y$, that is, given $X < 0.5$, we can infer that $Y < 0.5$. In other words, 
$$
f_{Y|X}(y| 0.5) \neq f_Y(y)
$$
 Therefore, they are not independent.

2) 

Using the formula $f_X(x)=\int f_{X,Y}(x,y) dy$, we have
$$
\begin{aligned}
f_ X(x)&=  \begin{cases} \int _0^ x\frac12\,  dy, &  \text{if } 0 < x \leq 1, \\ \int _0^{2-x}\frac32\,  dy ,&  \text{if } 1 < x < 2, \\ 0,&  \text{otherwise}, \end{cases}\\
&=   \begin{cases} x/2, &  \text{if } 0 < x \leq 1, \\ -3x/2+3,&  \text{if } 1 < x < 2, \\ 0,&  \text{otherwise.}\end{cases}
\end{aligned}
$$
A plot of the PDF is shown below:

![lec10-prob3-2](../assets/images/lec10-prob3-2.png)

3) 

Given that $X = 0.5$,  $f_{X,Y}(x,y)  =1/2$ is fixed, thus, $Y$ is uniformly distributed.
$$
f_{Y|X}(y|x) = { f_{X,Y}(x,y) \over f_X(x) } = {1/2 \over 1/4} = 2
$$
Thus, $Y$ is uniform distributed with PDF of a constant $2$ between $0$ and $1/2$.

Therefore, the conditional PDF is
$$
f_{Y|X}(y \mid 0.5)= \begin{cases} 2, &  \text{if } 0 \leq y \leq 1/2, \\ 0, &  \text{otherwise.} \end{cases}
$$
A plot of the conditional PDF is shown below:

![lec10-prob3-3](../assets/images/lec10-prob3-3.png)

4)

The PDF of $Y$ is
$$
\begin{aligned}
f_ Y(y)&= \int_Xf_{X,Y}(x,y)dx=\int_y^1\frac{1}{2}dx+\int_1^{2-y}\frac{3}{2}dx=\frac{1-y}{2}+\frac{3(1-y)}{2}=2(1-y)
\end{aligned}
$$
Given that $Y = 0.5$, the conditional distribution of $X$ is piecewise constant
$$
f_{X|Y}(x|0.5) = { f_{X,Y}(x,0.5) \over f_Y(0.5) } = \begin{cases}{1/2}&\text{if } 1/2 < x \leq 1\\{{3/2}} &\text{if } 1 < x < 3/2\\ 0 &\text{o.w.} \end{cases}
$$
A plot of the conditional PDF is shown below:

![lec10-prob3-4](../assets/images/lec10-prob3-4.png)

5)

Under event $A$, the pair $(X,Y)$ takes values in a triangular region with sides of length $1/2$ , and area $1/8$. The conditional point PDF is uniform, so that $f_{X,Y|A}(x,y)=8$ on that set. The conditional expectation is
$$
\begin{aligned}
\mathbf{E}[R|A] &=\mathbf{E}[XY|A]\\
&=\int\int xy f_{X,Y|A}(x,y) dxdy\\
&=\int^{0.5}_0\int^{0.5}_y 8xy dxdy\\
&= 1/16
\end{aligned}
$$
