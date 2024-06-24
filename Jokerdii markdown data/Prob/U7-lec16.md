# Lecture 16. Least mean squares (LMS) estimation

* Minimize mean squared error (MSE), $\mathbb{E}\left[(\Theta - \hat{\theta})^2 \right]: \quad \hat{\theta} = \mathbb{E}[\Theta]$.
  * Optimal mean squared error: $\mathbb{E}[(\Theta - \mathbb{E}[\Theta])^2] = \mathsf{Var}(\Theta)$.
  
* Minimize (conditional) mean squared error, $\mathbb{E}\left[(\Theta - \hat{\theta})^2 | X = x\right]: \quad \hat{\theta} = \mathbb{E}[\Theta | X=x]$.

* LMS estimation of $\Theta$ based on $X$​.

  * Unknown $\Theta$​​; prior $p_{\Theta}(\theta)$​.

    * Interested in a point estimate $\hat{\theta}$​.

  * Observation $X$; model $p_{X|\Theta}(x|\theta)$.

    * LMS estimate: $\hat{\theta} = \mathbb{E}[\Theta|X=x]$​.
    * LMS estimator: $\hat{\Theta} = \mathbb{E}[\Theta | X]$​.

  * $\mathbb{E}[\Theta]$​ minimizes $\mathbb{E}[({\Theta} - \hat{\theta})^2]$:

    $\mathbb{E}[(\Theta - \mathbb{E}[\Theta])^2] \leq \mathbb{E}[(\Theta - c)^2]$​, for all $c$.

  * $\mathbb{E}[\Theta| X=x]$​​​ minimizes $\mathbb{E}[({\Theta} - \hat{\theta})^2| X=x]$:

    $\mathbb{E}[(\Theta - \mathbb{E}[\Theta|X=x])^2|X=x] \leq \mathbb{E}[(\Theta - g(x))^2|X=x]$​​​, for all $x$​​​.

    $\mathbb{E}[(\Theta - \mathbb{E}[\Theta|X])^2|X] \leq \mathbb{E}[(\Theta - g(X))^2|X]$​​​

    $\mathbb{E}[(\Theta - \mathbb{E}[\Theta|X])^2] \leq \mathbb{E}[(\Theta - g(X))^2]$​​

    $\widehat{\Theta}_{LMS} = \mathbb{E}[\Theta|X]$​​ minimizes $\mathbb{E}[(\Theta - g(X))^2]$​​, over all estimators $\widehat{\Theta} = g(X)$​.

  * Expected performance

    * MSE = $\mathbb{E}[(\Theta - \mathbb{E}[\Theta | X=x])^2|X=x]= \text{var}(\Theta|X=x)$​​.
    * MSE = $\mathbb{E}[(\Theta - \mathbb{E}[\Theta|X])^2] = \mathbb{E}[\text{var}(\Theta | X)]$​​.

* Some challenges in LMS estimation

  * Full correct model, $f_{X|\Theta}(x | \theta)$​, may not be available.
  * Can be hard to compute / implement / analyze.

* Properties of the estimation error in LMS estimation

  * Estimator: $\widehat{\Theta} = \mathbb{E}[\Theta | X]$​; Error: $\tilde{\Theta} = \widehat{\Theta}-\Theta$​​.
  * $\mathbb{E}[\tilde{\Theta}|X=x] =\mathbb{E}[\widehat{\Theta} - \Theta|X=x] = \hat{\Theta} - \mathbb{E}[\Theta|X=x] = 0$​​.
  * $\text{cov}(\tilde{\Theta}, \widehat{\Theta})=\mathbb{E}[\tilde{\Theta}\widehat{\Theta}] - \mathbb{E}[\tilde{\Theta}]\mathbb{E}[\hat{\Theta}] = 0$​.
  * $\text{var}(\Theta)=\text{var}(\widehat{\Theta}) + \text{var}(\tilde{\Theta})$​.

There are 2 selected exercises and 3 solved problems.

---

## Exercise 1 LMS estimation error

Let $\Theta$​​ be the bias of a coin, i.e., the probability of Heads at each toss. We assume that $\Theta$​​ is uniformly distributed on $[0,1]$​​. Let $K$​​ be the number of Heads in $9$​​ independent tosses. We have seen that the LMS estimate of $K$​​ is $\mathbb{E}[K|\Theta = \theta] = n\theta$​​.

1. Find the **conditional mean squared error** ${\bf E}\big [\big (K-{\bf E}[K\mid \Theta =\theta ]\big )^2\mid \Theta =\theta \big ]$.
2. Find the **overall mean squared error** of this estimation procedure.

**Solution:**

1. **This is the variance of the conditional distribution of $K$​.** Since the conditional distribution is binomial with parameters $n=9$​ and $\theta = 1/3$​, the conditional variance is $9(1/3)(2/3)=2$​.

2. **This is the averages of the conditional variance, averaged over all possible values of the observation $\Theta$​​,** which has a uniform distribution.
   $$
   \begin{aligned}
   \int _0^1 f_{\Theta }(\theta ) \textsf{Var}(K\mid \Theta =\theta )\,  d\theta &=\int _0^1 9\theta (1-\theta )\,  d\theta\\
   &= \left(9\frac{1}{2}\theta ^2-9\frac{\theta ^3}{3}\right)\Big|_0^1\\
   &= 4.5-3\\
   &= 1.5
   \end{aligned}
   $$

## Exercise 2 Mean squared error

We assume that the random variables $\Theta$ and $X$ are described by the joint PDF which is uniform on the triangular set defined by the constraints $0 \leq x \leq 1, 0 \leq \theta \leq x$.

1. Find an expression for the conditional mean squared error of the LMS estimator given that $X=x$, valid for $x \in [0,1]$. 
2. Find the (unconditional) mean squared error of the LMS estimator.

**Solution:**

1. Since the conditional PDF of $\Theta$ is uniform on the range $[0,x]$. Hence, the conditional variance is $x^2/12$.

2. This is given by the integral of the conditional variance, weighted by the PDF of $X$. 

   The PDF of $X$ is found using the formula for going from the joint to the marginal, and is $f_X(x)=2x$, for $x \in [0,1]$. (We know the area of the triangle is $1/2$ and it's uniformly distribution, so the PDF if $f_X(x) = 2x.$)

   Thus, the mean squared error is
   $$
   \int _0^1 \frac{x^2}{12} \cdot 2x\,  dx =\frac{1}{6}\int _0^1 x^3\,  dx =\frac{1}{24}.
   $$

## Problem 1 Determining the type of a lightbulb

The lifetime of a type-A bulb is exponentially distributed with parameter $\lambda$. The lifetime of a type-B bulb is exponentially distributed with parameter $\mu$, where $\mu > \lambda > 0$. You have a box full of lightbulbs of the same type, and you would like to know whether they are of type A or B. Assume an a priori probability of $1/4$ That the box contains type-B lightbulbs.

1. Assume that $\mu \geq 3\lambda$. You observe the value $t_1$ of the lifetime, $T_1$, of a lightbulb. A MAP decision rule decides that the lightbulb is of type A if and only if $t_1 \geq \alpha$. Find $\alpha$.
2. Assume again that $\mu \geq 3\lambda$. What is the probability of error of the MAP decision rule?
3. Assume that $\lambda =3$ and $\mu = 4$. Find the LMS estimate of $T_2$, the lifetime of another lightbulb from the same box, based on observing $T_1=2$. Assume that conditioned on the bulb type, bulb lifetimes are independent. 

**Solution:**

1. Let $A$ and $B$ be the events that the box contains lightbulbs of type A and type B, respectively. A MAP rule decides in favor of type A if and only if
   $$
   \mathbf{P}(A\mid T_1=t_1) \geq \mathbf{P}(B\mid T_1=t_1)\\
   \frac{f_{T_1\mid A}(t_1)\mathbf{P}(A)}{f_{T_1}(t_1)} \geq \displaystyle \frac{f_{T_1\mid B}(t_1)\mathbf{P}(B)}{f_{T_1}(t_1)}
   $$
   Equivalently, we decide that the bulb is of type A if and only if 
   $$
   \begin{aligned}
   f_{T_1\mid A}(t_1)\mathbf{P}(A) &\geq f_{T_1\mid B}(t_1)\mathbf{P}(B)\\
   \lambda e^{-\lambda t_1}\frac{3}{4} &\geq \mu e^{-\mu t_1}\frac{1}{4}\\
   \frac{\lambda }{\mu }e^{(\mu -\lambda )t_1} &\geq {1\over 3}\\
   (\mu -\lambda )t_1 &\geq \ln \left(\frac{\mu }{3\lambda }\right).
   \end{aligned}
   $$
   Thus, since $\mu - \lambda > 0$, a MAP rule decides in favor of type A if and only if $t_1 \geq \ln \left(\frac{\mu }{3\lambda }\right)\cdot \frac{1}{\mu -\lambda }$. Hence, we deduce that
   $$
   \alpha = \frac{1}{\mu -\lambda }\ln \left(\frac{\mu }{3\lambda }\right).
   $$

2. Let events $A$ and $B$ be defined as in part (1). Let $\hat{A}$ be the event that the MAP rule decides in favor of type A, and let $\hat{B}$ be the event that the MAP rule decides in favor of type B. An error occurs whenever the decision is different from the actual type of the bulb. Thus,
   $$
   \begin{aligned}
   \mathbf{P}(\text{error}) &= \mathbf{P}(\hat{A}\cap B)+\mathbf{P}(A\cap \hat{B})\\
   &= \mathbf{P}(\hat{A}\mid B)\cdot \mathbf{P}(B) + \mathbf{P}(\hat{B}\mid A)\cdot \mathbf{P}(A)\\
   &= \mathbf{P}(T_1\geq \alpha \mid B)\cdot \frac{1}{4}+\mathbf{P}(T_1<\alpha \mid A)\cdot \frac{3}{4}\\
   &= e^{-\mu \alpha }\cdot \frac{1}{4}+(1-e^{-\lambda \alpha })\cdot \frac{3}{4}.
   \end{aligned}
   $$

3. The LMS estimate of $T_2$ based on observing $T_1= t_1$ is
   $$
   \begin{aligned}
   {\bf E}[T_2\mid T_1=t_1] &= {\bf E}[T_2\mid T_1=t_1,A]\cdot \mathbf{P}(A\mid T_1=t_1) + {\bf E}[T_2\mid T_1=t_1,B]\cdot \mathbf{P}(B\mid T_1=t_1)\\
   &= {\bf E}[T_2\mid A]\cdot \mathbf{P}(A\mid T_1=t_1) + {\bf E}[T_2\mid B]\cdot \mathbf{P}(B\mid T_1=t_1)\\
   &= \frac{1}{\lambda }\cdot \left(\frac{f_{T_1\mid A}(t_1)\cdot \mathbf{P}(A)}{f_{T_1}(t_1)}\right) + \frac{1}{\mu }\cdot \left(\frac{f_{T_1\mid B}(t_1)\cdot \mathbf{P}(B)}{f_{T_1}(t_1)}\right)\\
   &= \frac{\frac{1}{\lambda }\frac{3}{4}\lambda e^{-\lambda t_1}+\frac{1}{\mu }\frac{1}{4}\mu e^{-\mu t_1}}{\frac{3}{4}\lambda e^{-\lambda t_1}+\frac{1}{4}\mu e^{-\mu t_1}}.
   \end{aligned}
   $$
   Inserting the values $\lambda=3, \mu = 4$, and $t_1=2$, we obtain ${\bf E}[T_2\mid T_1=2]=0.328$.

## Problem 2 Estimating the parameter of a geometric r.v.

We have $k$ coins. The probability of Heads is the same for each coin and is the realized value $q$ of a random variable $Q$ that is uniformly distributed on $[0,1]$. We assume that conditioned on $Q=q$, all coin tosses are independent. Let $T_i$ be the number of tosses of the $i^{th}$ coin until that coin results in Heads for the first time, for $o=1,2,...,k$. ($T_i$ includes the toss that results in the first Heads.)

Hint: For any non-negative integers $k$ and $m$,
$$
\int _0^1 q^ k(1-q)^ m dq = \frac{k! m!}{(k+m+1)!}.
$$

1. Find the PMF of $T_1$, denoted by $p_{T_1}(t)$, for $t=1,2,...$.
2. Find the least mean squares (LMS) estimate of $Q$ based on the observed value, $t$, of $T_1$, denoted by ${\bf E}[Q \mid T_1 = t]$.
3. We flip each of the $k$ coins until they result in Heads for the first time. Compute the maximum a posteriori (MAP) estimate $\hat{q}$ of $Q$ given the number of tosses needed, $T_1=t_1, \ldots , T_ k=t_ k$, for each coin. Choose the correct expression for $\hat{q}$.

**Solution:**

1. The conditional probability of $T_1$ given $q$ is 
   $$
   p_{T_1 \mid Q}(t\mid q)=(1-q)^{t-1}q
   $$
   Using the total probability theorem, we have
   $$
   p_{T_1}(t)=\int ^1_0 p_{T_1\mid Q}(t\mid q)f_ Q(q)\, dq=\int ^1_0 (1-q)^{t-1} q\, dq=\frac{1}{(t+1)t}, \,  \text{ for }t=1,2,\ldots.
   $$

2. The LMS estimate is
   $$
   \begin{aligned}
   {\bf E}[Q\mid T_1=t] &=  \int ^1_0 f_{Q\mid T_1}(q\mid t)q\, dq\\
   &= \int ^1_0 \frac{p_{T_1\mid Q}(t\mid q)f_ Q(q)}{p_{T_1}(t)}q\, dq\\
   &= \int ^1_0 t(t+1)q(1-q)^{t-1}q\, dq\\
   &= \int ^1_0 t(t+1)q^2(1-q)^{t-1}dq\\
   &= t(t+1)\frac{2(t-1)!}{(t+2)!}\\
   &= {2\over t+2}
   \end{aligned}
   $$

3. We compute the posterior distribution of $Q$ given that $T_1=t_1, \ldots , T_ k=t_ k$.
   $$
   \begin{aligned}
   f_{Q|T_1, \ldots , T_ k}(q\mid t_1, \ldots , t_ k) &= \frac{f_ Q(q)\prod ^ k_{i=1} p_{T_ i|Q}(t_ i\mid q)}{\int ^1_0 f_ Q(q)\prod ^ k_{i=1} p_{T_ i|Q}(t_ i\mid q)dq}\\
   & =\frac{q^ k(1-q)^{\sum ^ k_{i=1} t_ i -k}}{c}
   \end{aligned}
   $$
   where $c$ is a normalizing constant that does not depend on $q$.

   To maximize the above expression, we set its derivative with respect to $q$ to zero and obtain
   $$
   kq^{k-1}(1-q)^{\sum ^ k_{i=1} t_ i -k}-\left(\sum ^ k_{i=1} t_ i -k\right)q^{k}(1-q)^{\sum ^ k_{i=1} t_ i -k-1}=0,\\
   \implies k(1-q)-\left(\sum ^ k_{i=1} t_ i -k\right)q=0,
   $$
   which yields the MAP estimate
   $$
   \hat q=\frac{k}{\sum ^ k_{i=1}t_ i}.
   $$

## Problem 3 Inference example

Continuous random variables $X$ and $Y$ have a joint PDF given by
$$
f_{X,Y}(x,y) = \begin{cases} 2/3, &  \text{if } (x,y) \text{ belongs to the closed shaded region,} \\ 0, &  \text{otherwise.} \end{cases}
$$
![images_8_3_lms_2_02](/Users/dizhen/Git/Notebooks/probability-and-statistics-notes/docs/assets/images/images_8_3_lms_2_02.png)

We want to estimate $Y$ based on $X$.

1. Find the LMS estimator $g(X)$ of $Y$.
2. Calculate the conditional mean squared error ${\bf E}\left[\left(Y-g(X)\right)^2\mid X=x\right]$.
3. Calculate the mean squared error ${\bf E}\left[\left(Y-g(X)\right)^2\right]$. Is it the same as ${\bf E}\left[\textsf{Var}(Y\mid X)\right]$?
4. Find $L(X)$, the linear LMS estimator of $Y$ based on $X$.
5. How do you expect the mean squared error of $L(X)$ to compare to that of $g(X)$?
6. What problem do you expect to encounter, if any, if you try to find the MAP estimator for $Y$ based on observations of $X$.

**Solution:**

1. We can observe the expectation of $Y$ given $X$ from the graph above, so the LMS estimator is
   $$
   g(X) = \mathbf{E}[Y|X] = \begin{cases}{1\over 2}X, & 0\leq X \leq 1 \\ X - {1\over 2}, & 1 \leq X \leq 2\\ \text{undefined}, & \text{otherwise} \end{cases}
   $$

2. With a fixed $x$ we can observe the conditional PDF of $Y$ from the graph above. If $x\in[0,1]$, the conditional PDF of $Y$ is uniform over the interval $[0,x]$, and
   $$
   {\bf E}\left[\left(Y-g(X)\right)^2\mid X=x\right] = {x^2 \over 12}.
   $$
   Similarly, if $x\in [1,2]$, the conditional PDF of $Y$ is uniform over the interval $[1-x,x]$, and
   $$
   {\bf E}\left[\left(Y-g(X)\right)^2\mid X=x\right] = {1 \over 12}.
   $$

3. The expectations ${\bf E}\left[\left(Y-g(X)\right)^2\right]$ and ${\bf E}\left[\textsf{Var}(Y\mid X)\right]$ are equal because by the Law of Iterated Expectations,
   $$
   {\bf E}\left[\left(Y-g(X)\right)^2\right] = {\bf E}\left[{\bf E}\left[ \left(Y-g(X)\right)^2|X\right]\right] = {\bf E}\left[\textsf{Var}(Y\mid X)\right]
   $$
   Recall from (2) that
   $$
   \textsf{Var}(Y|X=x) = \begin{cases}{x^2 \over 12} & 0 \leq x \leq 1 \\ {1\over 12 }& 1 \leq x \leq 2 \end{cases}
   $$
   It follows that
   $$
   \mathbf{E}[\textsf{Var}(Y|X)] = \int_x \textsf{Var}(Y|X=x) f_X(x) dx = \int^1_0 {x^2 \over 12} \cdot {2\over 3}x \ dx+ \int^2_1 {1\over 12}\cdot {2\over 3} dx ={5\over 72}
   $$
   Note that
   $$
   f_X(x) = \begin{cases}2x/3, & 0\leq x < 1\\ 2/3, & 1\leq x \leq 2 \end{cases}
   $$

4. The linear LMS estimator is
   $$
   L(X)  =\mathbf{E}[Y] + {\text{cov}(X,Y) \over \text{var}(X)} [X-\mathbf{E}[X]].
   $$
   In order to calculate $\text{var}(X)$ we first calculate $\mathbf{E}[X^2]$ and $\mathbf{E}[X]^2$.
   $$
   \begin{aligned}
   \mathbf{E}[X^2] &= \int^1_0 x^3 {2\over 3} dx + \int^2_1 x^2 {2\over 3} dx\\
   &= {31 \over 18}\\
   \mathbf{E}[X] &= \int^1_0 x^2 {2\over 3}dx + \int^2_1 x{2\over 3} dx\\
   &= {11\over 9}
   \end{aligned}
   $$
   Thus, $\textsf{Var}(X) = \mathbf{E}[X^2] - \mathbf{E}[X]^2 = {37\over 162}$. Also,
   $$
   \mathbf{E}[Y] = \int^1_0 \int^x_0 {2\over 3}\ y\ dy\ dx + \int^2_1 \int^x_{x-1} {2\over 3}y \ dy \ dx = {1\over 9} + {2\over 3} = {7 \over 9}
   $$
   To determine $\textsf{Cov}(X,Y)$ we need to evaluate $\mathbf{E}[XY]$:
   $$
   \begin{aligned}
   \mathbf{E}[XY] &= \int_x \int_y xyf_{X,Y}(x,y) \ dy \ dx\\
   &= \int^1_0 \int^x_0 yx {2\over 3}\ dy \ dx+ \int^2_1\int^x_{x-1} yx {2\over 3}\ dy\ dx\\
   & ={41 \over 36}
   \end{aligned}
   $$
   and so $\textsf{Cov}(X,Y) = \mathbf{E}[XY] - \mathbf{E}[X]\mathbf{E}[Y] = {61 \over 324}$. Therefore,
   $$
   L(X) = {7 \over 9} + {61 \over 74}(X- {11 \over 9})
   $$

5. The LMS estimator is the one that minimizes mean squared error (among all estimators of $Y$ based on $X$). The linear LMS estimator, therefore, cannot perform better than the LMS estimator, i.e., we expect $\mathbf{E}[(Y-L(X))^2] \geq \mathbf{E}[(Y-g(X))^2]$. In fact,
   $$
   \begin{aligned}
   \mathbf{E}[(Y-L(X))^2] &= \sigma_Y^2(1 - \rho)\\
   &= \sigma_Y^2\left(1 - {\textsf{Cov}(X,Y)^2 \over \sigma_X^2 \sigma_Y^2}\right)\\
   &= {37\over 162} \left(1 - \left({61\over 74}\right)^2 \right)\\
   &= 0.073\\
   & \geq {5 \over 72}
   \end{aligned}
   $$

6. For a single observation $x$ of $X$, the MAP estimate is not unique since all possible values of $Y$ for this $x$ are equally likely. Therefore, the MAP estimator does not give meaningful results.

   
