# Lecture 9. Conditioning on an event; Multiple r.v.'s

* Conditioning a r.v. on an event

  * Conditional PDF

    | Discrete                                                     | Continuous                                                   |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | $p_X(x) = \mathbf{P}(X=x)$                                   | $f_X(x) \cdot \delta \approx \mathbf{P}(x \leq X \leq x+ \delta)$ |
    | $p_{X\vert A}(x) = \mathbf{P}(X=x\vert A)$                   | $f_{X\vert A}(x) \cdot \delta \approx \mathbf{P}(x \leq X \leq x+ \delta \vert A)$ |
    | $\mathbf{P}(X\in B) = \sum_{x \in B}p_X(x)$                  | $\mathbf{P}(X\in B) = \int_{B}f_X(x)dx$                      |
    | $\mathbf{P}(X\in B \vert A) = \sum_{x \in B}p_{X\vert A}(x)$ | $\mathbf{P}(X\in B\vert A) = \int_{B}f_{X\vert A}(x)dx$      |
    | $\sum_xp_{X\vert A}(x) = 1$                                  | $\int f_{X \vert A}(x)dx = 1$                                |
    |                                                              | $\mathbf{P}(x \leq X \leq x+\delta\vert X \in A) \approx f_{X \vert X \in A}(x) \cdot \delta\\={\mathbf{P}(x \leq X \leq x+\delta , x \in A)\over \mathbf{P}(A)}={\mathbf{P}(x \leq X \leq x+\delta)\over \mathbf{P}(A)} \approx {f_x(x) \over \mathbf{P}(A)}$ |
    |                                                              | $f_{X\vert X\in A(x)}  = \begin{cases} 0, & \text{if } x \notin A\\ {f_x(x) \over \mathbf{P}(A)}, & \text{if } x \in A \end{cases}$ |

  * Conditional expectation and the expected value rule

    | Discrete                                               | Continuous                                             |
    | ------------------------------------------------------ | ------------------------------------------------------ |
    | $\mathbf{E}[X] = \sum_x xp_X(x)$                       | $\mathbf{E}[X] = \int xf_X(x) dx$                      |
    | $\mathbf{E}[X\vert A] = \sum_x xp_{X\vert A}(x)$       | $\mathbf{E}[X\vert A] = \int xf_{X\vert A}(x) dx$      |
    | $\mathbf{E}[g(X)] = \sum_x g(x)p_X(x)$                 | $\mathbf{E}[g(X)] = \int g(x)f_X(x)dx$                 |
    | $\mathbf{E}[g(X)\vert A] = \sum_x g(x)p_{X\vert A}(x)$ | $\mathbf{E}[g(X)\vert A] = \int g(x)f_{X\vert A}(x)dx$ |

  * Exponential PDF: Memorylessness - probabilistically identical.

    * Bulb lifetime $T$: $\mathsf{Exp}(\lambda)$. So $\mathbf{P}(T > x)= e^{-\lambda x},$ for $x \geq 0$.

      We are told that $T > t$, and $X$ is a random variable of remaining lifetime, $T - t$.

      Then we have $\mathbf{P}(X > x \vert T > t) = e^{-\lambda x},$ for $x \geq 0$.

    * Equivalently,
      $$
      \mathbf{P}(t \leq T \leq t + \delta \vert T > t) = \mathbf{P}(0 \leq T \leq \delta) = \lambda \delta
      $$

    * Proof:
      $$
      \begin{aligned}
      \mathbf{P}(X > x \vert T > t) &= {\mathbf{P} (T-t > x, T > t)\over \mathbf{P}(T > t)} \\
      &= {\mathbf{P} (T > t+x, T > t)\over \mathbf{P}(T > t)} \\
      &= {\mathbf{P} (T > t+x) \over \mathbf{P}(T > t)} \\
      &= {e^{-\lambda(t+x)}\over e^{-\lambda t} }\\
      &= e^{-\lambda x}
      \end{aligned}
      $$

  * Total probability and expectation theorems

    | Discrete                                                     | Continuous                                                   |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | $\mathbf{P}(B) = \mathbf{P}(A_1)\mathbf{P}(B \vert A_1) + ... + \mathbf{P}(A_n)\mathbf{P}(B \vert A_n)\\ p_X(x) = \mathbf{P}(A_1)p_{X \vert A_1}(x) + ... + \mathbf{P}(A_n)p_{X \vert A_n}(x) $ | $f_X(x) = \mathbf{P}(A_1)f_{X \vert A_1}(x) + ... +  \mathbf{P}(A_n)f_{X \vert A_n}(x) $ |
    |                                                              | $\mathbf{E}[X] = \mathbf{P}(A_1)\mathbf{E}[X \vert A_1] + ... + \mathbf{P}(A_n)\mathbf{E}[X \vert A_n]$ |

    **Example**: Bill goes to the supermarket shortly, with probability $1/3$, at a time uniformly distributed between $0$ and $2$ hours now; or with probability $2/3$, later in the day at a time uniformly distributed between 6 and 8 hours from now.

    * Given $\mathbf{P}(A_1) = 1/3,\quad f_{X\vert A_1} \sim \mathsf{Unif}[0,2], \quad \mathbf{P}(A_2) = 2/3,\quad f_{X\vert A_2} \sim \mathsf{Unif}[6,8]$

    * $f_X(x) = \mathbf{P}(A_1)f_{X \vert A_1}(x) +  \mathbf{P}(A_2)f_{X \vert A_2}(x)  = 1/3 \times 1/2 + 2/3 \times 1/2 = 1/2$. So the PDF looks like this

      ![U5-lec9-total-prob-ex](../assets/images/U5-lec9-total-prob-ex.png)

    * $\mathbf{E}[X] = \mathbf{P}(A_1)\mathbf{E}[X \vert A_1] + \mathbf{P}(A_2)\mathbf{E}[X \vert A_2] = 1/3 \cdot 1 + 2/3 \cdot 7$.

  * Mixed distributions

* Jointly continuous r.v.'s and joint PDFs

  * Definition: two random variables are jointly continuous if they can be described by a joint PDF $f_{X,Y}(x,y)$.

    | Discrete                                                     | Continuous                                                   |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | $p_{X,Y}(x,y) = \mathbf{P}(X=x, Y=y) \geq 0$                 | $f_{X,Y}(x,y) \geq 0$                                        |
    | $\mathbf{P}((X,Y) \in B) = \sum\limits_{(x,y)}\sum\limits_{\in B} p_{X,Y}(x,y)$ | $\mathbf{P}((X,Y) \in B) = \int\limits_{(x,y)}\int\limits_{\in B} f_{X,Y}(x,y)dxdy$ |
    | $\sum\limits_x\sum\limits_y p_{X,Y}(x,y)=1$                  | $\int^\infty_{-\infty}\int^\infty_{-\infty} f_{X,Y}(x,y)dxdy = 1$ |

  * From the joints to the marginals

    | Discrete                                                     | Continuous                                |
    | ------------------------------------------------------------ | ----------------------------------------- |
    | $p_{X}(x) = \sum\limits_y p_{X,Y}(x,y)$                      | $f_{X}(x) = \int f_{X,Y}(x,y)dy$          |
    | $p_{Y}(y) = \sum\limits_x p_{X,Y}(x,y)$                      | $f_{Y}(y) = \int f_{X,Y}(x,y)dx$          |
    | $\sum\limits_x\sum\limits_y\sum\limits_z p_{X,Y,Z}(x,y,z) = 1$ | $\int\int\int f_{X,Y,Z}(x,y,z)dxdydz = 1$ |
    | $p_X(x) = \sum\limits_y\sum\limits_z p_{X,Y,Z}(x,y,z)$       | $f_X(x) = \int\int f_{Y,Z}(y,z)dydz$      |
    | $p_{X,Y}(x,y) = \sum\limits_z p_{X,Y,Z}(x,y,z)$              | $f_{X,Y}(x,y) = \int f_{X,Y,Z}(x,y,z)dz$  |

  * Uniform joint PDF example

  * The expected value rule

    | Discrete                                                     | Continuous                                              |
    | ------------------------------------------------------------ | ------------------------------------------------------- |
    | $\mathbf{E}[g(X,Y)] = \sum\limits_x \sum\limits_yg(x,y)p_{X,Y}(x,y)$ | $\mathbf{E}[g(X,Y)] = \int \int g(x,y)f_{X,Y}(x,y)dxdy$ |

  * The linearity of expectations

    $\mathbf{E}[aX+b] = a\mathbf{E}[X] + b$

    $\mathbf{E}[X+Y] = \mathbf{E}[X] + \mathbf{E}[Y]$

    $\mathbf{E}[X_1+...+X_n] = \mathbf{E}[X_1] + ...+\mathbf{E}[X_n]$

  * The joint CDF

    $F_{X,Y}(x,y) = \mathbf{P}(X \leq x, Y \leq y) = \int^y_{-\infty} \left[\int^x_{-\infty} f_{X,Y}(s,t)ds\right] dt$

    $f_{X,Y}(x,y) = {\partial^2F_{X,Y} \over \partial x\partial y}(x,y)$

There are 3 selected exercises and 3 solved problems.

---

## Exercise 1 A conditional PDF

Suppose that $X$ has a PDF of the form
$$
f_ X(x)=\begin{cases} 1/x^2,&  \text{if } x\geq 1,\\ 0,& \text{otherwise.}\end{cases}
$$
For any $x > 2$, what is the conditional PDF of $X$, given the event $X > 2$ ?

**Answer**: $2/x^2$

**Solution**: 

The conditional PDF will be a scaled version of the unconditional, of the form $\frac{f_ X(x)}{\mathbf{P}(X>2)}.$ Since
$$
\mathbf{P}(X>2)=\int _2^{\infty }\frac{1}{x^2}\,  dx =-\frac{1}{x}\Big|_2^{\infty }=1/2,
$$
Hence, 
$$
f_X(x \vert X>2) = \frac{f_ X(x)}{\mathbf{P}(X>2)} = 2/x^2
$$

## Exercise 2 Memorylessness of the exponential

Let $X$ be an exponential random variable with  parameter $\lambda$

1. What is the probability that $X > 5$
2. What is the probability that $X > 5$ given that $X > 2$?
3. Given that $X > 2$ and for a small $\delta > 0$, what is the probability that $4\leq X \leq 4 + 2 \delta$?

**Answer**:

1. $e^{-5\lambda }$.
2. $e^{-3\lambda }$.
3. $2\lambda \delta e^{-2\lambda }$.

**Solution**: 

1. $\mathbf{P}(X>5)=e^{-5\lambda }$ according to the formula $\mathbf{P}(X>a)=e^{-\lambda a}$.

2. According to memorylessness property, given that $X>2$, the remaining time $X−2$ is again exponential with the same parameter, we have
   $$
   \mathbf{P}(X>5\, |\, X>2)=\mathbf{P}(X-2>3\, |\, X>2)=\mathbf{P}(X>3)=e^{-3\lambda }
   $$

3. By memorylessness, this is the same as the unconditional probability that an exponential takes values in the interval $[2,2+2\delta ]$, which is approximately the length $2\delta$ of the small interval times the **density (pdf)** evaluated at $2$, yielding $2\lambda \delta e^{-2\lambda }$.
   $$
   \mathbf{P}(4\leq X \leq 4 + 2 \delta \vert X > 2) = \mathbf{P}(2\leq X \leq 2 + 2 \delta)  = f_X(2) \cdot 2\delta=2\lambda \delta e^{-2\lambda }
   $$

## Exercise 3 From joint PDFs to probabilities

1. The probability of the event that $0\leq Y \leq X\leq 1$ is of the form $ \int _ a^ b \left(\int _ c^ d f_{X,Y}(x,y)\, dx\right)\, dy.$ Find the values of $a,b,c,d$.
2. The probability of the event that $0\leq Y \leq X\leq 1$ is of the form $ \int _ a^ b \left(\int _ c^ d f_{X,Y}(x,y)\, dy\right)\, dx.$ Find the values of $a,b,c,d$.

**Answer**: 

$1. a=0, b=1, c=y, d=1\\2. a=0, b=1, c=0, d=x$

## Problem 1 Mixed distribution example

The taxi stand and the bus stop near Al's home are in the same location. Al goes there at a given time and if a taxi is waiting (this happens with probability $2/3$) he boards it. Otherwise, he waits for a taxi or a bus to come, whichever comes first. The next taxi will arrive in a time that is uniformly distributed between $0$ and $10$ minutes, while the next bus will arrive in exactly $54$ minutes. Find the CDF and the expected value of Al's waiting time.

**Answer**:

![U5-prob1-mixed](../assets/images/U5-prob1-mixed.png)

**Solution**: 
$$
\begin{aligned}
\mathbf{E}[X] &= \mathbb{P}(B_1) \mathbf{E}(X | B_1) + \mathbb{P}(B_2) \mathbf{E}(X | B_2) + \mathbb{P}(B_3) \mathbf{E}(X | B_3)\\
&= {2 \over 3} \cdot 0 + {1\over 3} \cdot {1 \over 2} \cdot {5\over 2} + {1\over 3} \cdot {1\over 2} \cdot 5\\
&= {5 \over 12} + {5 \over 6}\\
&= {15 \over 12}
\end{aligned}
$$
For $0 \leq x < 5$, 
$$
\begin{aligned}
\mathbb{P}(X \leq x) &= \mathbb{P}(B_1)\mathbb{P}(X \leq x| B_1) + \mathbb{P}(B_2)\mathbb{P}(X \leq x | B_2) + \mathbb{P}(B_3) \mathbb{P}(X \leq x | B_3)\\
&= {2 \over 3} \cdot 1 +{1\over 3} \cdot {1\over 2} \cdot {1\over 5} \cdot x + {1\over 3}\cdot {1\over 2} \cdot 0\\
&= {2\over 3} + {1\over 30} x
\end{aligned}
$$
Therefore,
$$
\begin{aligned}
F_X(x) &= \mathbb{P}(X \leq x) \\
&= 0 &\quad \text{ if }x < 0 \\
&= {2\over 3} + {1\over 30} x &\quad \text{ if }0 \leq x < 5 \\
&= 1 &\quad \text{ if }x \geq 5 \\
\end{aligned}
$$

## Problem 2 Circular Uniform PDF

Ben throws a dart at a circular target of radius $r$. We assume that he always hits the target and that all points of impact $(x,y)$ are equally likely. Compute the joint PDF $f_{X,Y}(x,y)$ of the random variables $X$ and $Y$ , and compute the conditional PDF $f_{X|Y}(x|y)$ .

**Solution**: 

The random variable $X$ is x-coordinate, $Y$ is y-coordinate. The joint PDF of $X, Y$ is
$$
f_{X,Y}(x,y) = \begin{cases}{1\over \pi r^2}, & x^2 + y^2 \leq r^2\\ 0, & \text{o.w.} \end{cases}
$$
The marginal PDF of $Y$ is 
$$
\begin{aligned}
f_Y(y) &= \int^\infty_{-\infty} f_{X,Y}(x,y)dx\\ 
&= \int^{\sqrt{r^2 - y^2}}_{-\sqrt{r^2 - y^2}} {1\over \pi r^2} dx\\ 
&= \begin{cases}{2 \sqrt{r^2 - y^2} \over \pi r^2}, & -r \leq y \leq r \\ 0, & \text{o.w.}\end{cases}
\end{aligned}
$$
The conditional PDF is 
$$
\begin{aligned}
f_Y(y) &= \begin{cases}{{1 \over \pi r^2} \over {2\sqrt{r^2 - y^2} \over \pi r^2}}, &x^2 + y^2 \leq r^2 \\ 0, & \text{o.w.} \\ \end{cases}\\
&= \begin{cases}{1  \over {2\sqrt{r^2 - y^2} }}, &-r \leq y \leq r, \quad-\sqrt{r^2 -y^2} \leq x \leq \sqrt{r^2 - y^2} \\ 0, & \text{o.w.} \\ \end{cases}\\

\end{aligned}
$$
Notice that ${1  \over {2\sqrt{r^2 - y^2} }}$ is uniform and does not depend on $x$. It is interesting that the original distribution ${1\over \pi r^2}$ is uniform, the marginal distribution of $Y$ is not uniform, which depends on $y$, but when we calculate the conditional distribution, we got a uniform distribution back again which does not depend on $x$.

## Problem 3 The absent minded professor

An absent-minded professor schedules two student appointments for the same time. The appointment durations are **independent** and **exponentially** distributed with mean $30$ minutes. The first student arrives on time, but the second student arrives 5 minutes late. What is the expected value of the time between the **arrival** of the first student and the **departure** of the second student?

**Solution**:

Recall the exponential distribution: $T \sim \mathsf{Exp}(\lambda)$.

The mean is $\mathbf{E}[T] = {1\over \lambda}$.

The CDF is $\mathbf{P}(T \leq t) = 1 - e^{-\lambda t}, \quad t \geq 0$.

Given $T_1, T_2 \sim \mathsf{Exp}({1\over 30})$ and are independent.

Consider two scenarios:

If $T_1 \leq 5$, 
$$
\begin{aligned}
\mathbf{E}[X|T_1 \leq 5] &= 5+ \mathbf{E}[T_2] = 35\\
\mathbb{P}(T_1 \leq 5) &= 1 - e^{-5/30}
\end{aligned}
$$
If $T_2 > 5$,
$$
\begin{aligned}
\mathbf{E}(X|T_1 > 5) &= 5 + 30 + 30 = 65\\
\mathbb{P}(T_1 > 5) &= e^{-5/30}
\end{aligned}
$$
Applying total expectation theorem,
$$
\begin{aligned}
\mathbf{E}[X] &= \mathbb{P}(T_1 \leq 5)\mathbf{E}[X | T_1 \leq 5] + \mathbb{P}(T_2 > 5)\mathbf{E}[X | T_2 > 5]\\
&= 35 (1-e^{-5/30}) + 65 e^{-5/30}\\
&= 60.394
\end{aligned}
$$








