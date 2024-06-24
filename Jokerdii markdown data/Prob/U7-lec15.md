# Lecture 15. Linear models with normal noise

* Recognizing normal PDFs

  Recall the normal random variable and its PDF:
  $$
  X \sim \mathcal{N}(\mu, \sigma^2) \qquad f_X(x) = {1\over \sigma \sqrt{2\pi} } \exp\left( {-(x - \mu)^2 \over 2\sigma^2}\right)
  $$
  For $f_X(x) = c \cdot \exp \left( \alpha x^2 + \beta x + \gamma\right),\ a>0$, we recognize it a normal PDF, with mean $\mu = -\beta/2\alpha$ and variance $\sigma^2 = 1/2\alpha$ by 
  $$
  \alpha x^2 + \beta x + \gamma = \alpha(x^2 + {\beta \over \alpha} x + {\gamma \over \alpha}) = \alpha ((x+ {\beta \over 4\alpha^2})^2 - {\beta^2 \over 4 \alpha^2} + {\gamma\over \alpha})
  $$
  Thus, the PDF can be written as
  $$
  f_X(x) = c\cdot \exp \left(-\alpha (x + {\beta \over 2 \alpha})^2 \right) \exp \left( -\alpha\left( -{\beta \over 4\alpha^2 }+ {\gamma \over \alpha} \right)\right)
  $$
  To find the mean of the PDF $f_X(x) = c \cdot \exp \left( \alpha x^2 + \beta x + \gamma\right)$, we know the mean happens to the peak of the distribution, so we can maximize the PDF, which equals to minimizing the quadratic function $\alpha x^2 + \beta x + \gamma$.

  To minimize $\alpha x^2 + \beta x + \gamma$, we take the derivative with respect to $x$ and set it to zero.
  $$
  {\partial \over\partial x }\alpha x^2 + \beta x + \gamma = 2\alpha x + \beta  = 0\\
  x = - {\beta \over 2\alpha}
  $$

* Estimating a normal random variable in the presence of additive normal noise

  $X = \Theta + W, \quad \Theta, W: \mathcal{N}(0,1), \quad $ independent
  $$
  f_{X|\Theta}(x|\theta): \mathcal{N}(\theta, 1)\\
  f_{\Theta|X}(\theta |x) = {1 \over f_X(x) }c \ \exp\left( -{1\over 2} \theta^2 \right) \ c \ \exp\left( -{1\over 2} (x- \theta)^2 \right) = c(x) \exp\left( - \text{quadratic}(\theta) \right)
  $$
  To find the conditional expectation, we maximize the distribution, which equals to minimizing the quadratic function with $x$ fixed.
  $$
  \min_\Theta \left[ {1\over 2} \theta^2 + {1\over 2} (x-\theta)^2 \right]\\
  \theta + (\theta -x ) =0\\
  \hat{\theta}_{MAP}=\hat{\theta}_{LMS} = \mathbf{E}[\Theta | X=x] = {x \over 2}\\
  \hat{\theta}_{MAP}=\hat{\theta}_{LMS} = \mathbf{E}[\Theta | X] = {X \over 2}
  $$
  Properties: 

  * Posterior is normal
  * LMS and MAP estimators coincide
  * These estimators are linear, of the form $\widehat{\Theta} = aX+b$

* The case of multiple observations

  $X_1= \Theta + W_1, ..., X_n = \Theta + W_n$. $\Theta \sim \mathcal{N}(x_0, \sigma^2_0), W_i \sim \mathcal{N}(0, \sigma_i^2)$. $\Theta, W_1, ..., W_n$ independent.

  Given $\Theta = \theta: \quad x_i = \theta + W_i \sim \mathcal{N}(\theta, \sigma_i^2)$. 
  $$
  f_{X_i | \Theta}(x_i | \theta) = c_i \exp\left( {-(x_i - \theta)^2\over 2\sigma_i^2}  \right)
  $$
  Given $\Theta = \theta: \quad W_i$ independent $\implies X_i$ independent
  $$
  \begin{aligned}
  f_{\Theta |X} (\theta|x) &= {1\over f_X(x)} \  c_0  \ \exp\left( -{(\theta -x_0)^2\over 2\sigma_0^2} \right) \prod\limits^n_{i=1} \ c_i \ \exp\left(-{(x_i-\theta)^2\over 2 \sigma_i^2}\right)\\
  &= c \ \exp (- \text{quad}(\theta))\\
  \text{where    quad}(\theta) &= {(\theta-x_0)^2\over 2\sigma_0^2} + {(\theta-x_1)^2\over 2\sigma_1^2} + ... + {(\theta-x_n)^2\over 2\sigma_n^2}
  \end{aligned}
  $$
  To find the conditional expectation,
  $$
  \begin{aligned}
  &{\partial \over \partial \theta} \text{quad}(\theta) = 0\\
  \implies& \sum^n_{i=0} {(\theta - x_i)\over \sigma_i^2} = 0\\
  \implies& \theta \sum^n_{i=0} {1 \over \sigma_i^2} = \sum^n_{i=0} { x_i \over \sigma_i^2}\\
  \implies& \hat{\theta}_{MAP}= \hat{\theta}_{LMS} = \mathbf{E}[\Theta|X=x] = {\sum\limits^n_{i=0}{x_i\over\sigma^2_i } \over \sum\limits^n_{i=0} {1\over \sigma_i^2} }
  \end{aligned}
  $$
  Properties

  * Posterior is normal
  * LMS and MAP estimates coincide
  * These estimates are linear, of the form $\hat{\theta} = a_0 + a_1 x_1 + ... + a_n x_n$.

  Interpretations

  * Estimates $\hat{\theta}$ weighted average of $x_0$ (prior mean) and $x_i$ (observations)
  * Weights determined by variances

* Mean squared error

  $\mathbf{E}\left[(\Theta - \widehat{\Theta})^2|X=x \right] = \mathbf{E}\left[(\Theta - \widehat{\theta})^2|X=x \right] = \mathsf{Var}(\Theta|X=x) = 1/\sum\limits^n_{i=0}{1\over\sigma_i^2 }\\\mathbf{E}\left[(\Theta - \widehat{\Theta})^2\right] = \int \mathbf{E}\left[(\Theta - \widehat{\Theta})^2|X=x \right]f_X(x)\ dx$

  Thus
  $$
  \mathbf{E}\left[(\Theta - \widehat{\Theta})^2|X=x \right]  = \mathbf{E}\left[(\Theta - \widehat{\Theta})^2\right]=1/\sum\limits^n_{i=0}{1\over\sigma_i^2 }
  $$

  * Example 1

    Recall $f_X(x) = c \cdot \exp \left( \alpha x^2 + \beta x + \gamma\right),\ a>0$, is a normal PDF, with mean $\mu = -\beta/2\alpha$ and variance $\sigma^2 = 1/2\alpha$. Consider $f_{\Theta |X} (\theta|x) = c \ \exp (- \text{quad}(\theta))$ , where $\text{quad}(\theta) = {(\theta-x_0)^2\over 2\sigma_0^2} + {(\theta-x_1)^2\over 2\sigma_1^2} + ... + {(\theta-x_n)^2\over 2\sigma_n^2}$. We have
    $$
    \alpha =  {1 \over 2\sigma_0^2} + {1\over 2\sigma_1^2} + ... + {1\over 2\sigma_n^2}
    $$
    Properties:

    * Some $\sigma_i^2$ small $\implies $ MSE small
    * All $\sigma_i^2$ large $\implies $ MSE large

  * Example 2

    $\sigma^2_0=\sigma^2_1=...=\sigma^2_n=\sigma^2$

    $\mathbf{E}\left[(\Theta - \widehat{\Theta})^2|X=x \right] = \mathbf{E}\left[(\Theta - \widehat{\theta})^2|X=x \right] = \mathsf{Var}(\Theta|X=x) = 1/\sum\limits^n_{i=0}{1\over\sigma_i^2 } = {1\over (n+1){1\over \sigma^2}} = {\sigma^2 \over n+1}$

    This implies that as $n$ increases we improve the performance.

* The case of multiple parameters: trajectory estimation

  * Random variables $\Theta_0, \Theta_1, \Theta_2$
  
    Independent; priors $f_{\Theta_j}$
  
  * Measurements at times $t_1, ..., t_n$
  
    The observation model is $Y_i = X_i + W_i$, where $X_i = \Theta_0 + \Theta_1t_i + \Theta_2 t_i^2$.
  
    The noise model: $f_{W_i}$; Independent $W_i$; independent from $\Theta_j$
  
  * Assume $\Theta_j \sim \mathcal{N}(0,\sigma^2),W_i \sim \mathcal{N}(0,\sigma^2)$; independent
  
    Given $\Theta = \theta = (\theta_0, \theta_1, \theta_2), X_i$ is $\mathcal{N}(\theta_0 + \theta_1 t_i + \theta_2 t_i^2, \sigma^2)$
  
    The conditional PDF of $Y$ given $\Theta$ is
    $$
    f_{Y_i|\Theta}(y|\theta) = c \cdot \exp \left({-(x_i - \theta_0 - \theta_1 t_i - \theta_2t_i^2)^2\over 2\sigma^2}\right)\\
    f_{Y|\Theta}(y|\theta) = c \cdot \prod_{i=1}^n \exp \left({-(x_i - \theta_0 - \theta_1 t_i - \theta_2t_i^2)^2\over 2\sigma^2}\right)
    $$
    The joint PDF of $\Theta$ and $Y$ is
    $$
    f_{\Theta,Y}(\theta, y) = \prod^2_{j=0} f_{\Theta_j}(\theta_j) \cdot \prod^n_{i=1}f_{Y_i|\Theta}(y|\theta)
    $$
    The posterior PDF is
    $$
    \begin{aligned}
    f_{\Theta|Y}(\theta|y) &= {1\over f_Y(x)} f_{\Theta,Y}(\theta,y)\\
    &= {1\over f_Y(x)} \prod^2_{j=0}f_{\theta_j}(\theta_j) \prod^n_{i=1} f_{Y_i|\Theta} (y_i|\theta)\\
    &= c(y) \cdot \exp \left( -{1\over 2} \left( {\theta_1^2 \over \sigma_0^2} + {\theta_2^2 \over \sigma_1^2} + {\theta_2^2 \over \sigma_2^2} \right) - {1\over 2\sigma^2} \sum^n_{i=1}(y_i - \theta_0 - \theta_1 t_i - \theta_2 t_i^2)^2 \right)
    \end{aligned}
    $$
    where $c(y)$ is a normalizing constant.
  
    Note that the numerical value of $f_Y(y)$ is not required, if we are interested in just the MAP estimator, or the general shape of the posterior distribution.
  
  * MAP estimate: maximize over $(\theta_0, \theta_1, \theta_2)$: (minimize quadratic function)
    $$
    {\partial \over \partial \theta_j} (\text{quad}(\theta)) = 0\\
    \text{where   quad}(\theta) = \theta_0^2/\sigma_0^2 + \theta_1^2/\sigma_1^2+ \theta_2^2/\sigma_2^2 + {1\over \sigma^2} \sum^n_{i=1}(y_i - \theta_0 - \theta_1 t_i - \theta_2 t_i^2)^2
    $$
  
* Linear normal models

  * $\Theta_j$ and $X_i$ are linear functions of independent normal random variables

  * $f_{\Theta|X} (\theta|x) = c(x) \ \exp (-\text{quad}(\theta_1, ..., \theta_m))$

  * MAP estimate: maximize over $(\theta_1, ..., \theta_m)$ (minimize quadratic function)

    $\widehat{\Theta}_{MAP,j}:$ Linear function of $X = (X_1, ..,X_n)$.

  * Facts

    * $\widehat{\Theta}_{MAP,j} = \mathbf{E}[\Theta_j|X]$
    * marginal posterior PDF of $\Theta_j: f_{\Theta_j|X}(\theta_j|x)$, is normal
    * MAP estimate based on the joint posterior PDF: same as MAP estimate based on the marginal posterior PDF
    * $\mathbf{E}\left[ (\Theta_{i, MAP} - \Theta_i)^2|X=x \right]$: same for all $x$.

There are 4 selected exercises and 2 solved problems.

---

## Exercise 1 Multiple observations, more general model

Suppose that $X_1=\Theta +W_1$ and $X_2=2\Theta +W_2$, where $\Theta ,W_1,W_2$ are independent **standard normal** random variables. If the values that we observe happen to be $X_1 = -1$ and $X_2 = 1$, then what is the MAP estimate of $\Theta$ ?

**Solution:**

The numerator term of the posterior is equal to a constant times
$$
e^{-\theta ^2/2} e^{-(x_1-\theta )^2/2}e^{-(x_2-2\theta )^2/2}.
$$
To find the MAP estimate, we set $x_1$ and $x_2$ to the given values, and set the derivative of the exponent (with respect to $\theta$) to zero. We obtain
$$
\theta +(\theta +1) +2(2\theta -1)=0,
$$
which yields $6 \theta - 1 = 0$ or $\theta =1/6$.

## Exercise 2 The mean-squared error

Recall the mean squared error is
$$
\frac{1}{\displaystyle {\sum _{i=0}^{n} \frac{1}{\sigma _ i^2}}}
$$
Considering two scenarios: 

In the first scenario, $\Theta \sim N(0,1)$ and we observe $X = \Theta + W$, where $W\sim N(0,1)$ is independent of $\Theta$.

In the second scenario, the prior information on $\Theta$ is extremely inaccurate: $\Theta \sim N(0,\sigma _0^2)$, where $\sigma_0^2$ is so large that it can be treated as infinite. But in this second scenario we obtain two observations of the form $X_i = \Theta + W_i$, where the $W_i$ are standard normals, independent of each other and of $\Theta$.

What is the MSE in both scenarios?

**Solution:**

They are the same in both scenarios.

For the second scenario, we set $\sigma _0^2=\infty$. In the first scenario, we obtain
$$
\frac{1}{\frac{1}{1}+\frac{1}{1}}=\frac{1}{2},
$$
and in the second scenario, we obtain the same mean squared error:
$$
\frac{1}{\frac{1}{\infty } + \frac{1}{1}+\frac{1}{1}}=\frac{1}{2}.
$$
**Remark:** the prior information on $\Theta$ in the first scenario is, in a loose sense, exactly as informative as having no useful prior information but one more observation, as in the second scenario.

## Exercise 3 The effect of a stronger signal

For the model $X=\Theta +W$, and under the usual independence and normality assumptions for $\Theta$ and $W$, the mean squared error of the LMS estimator is
$$
\frac{1}{(1/\sigma _0^2)+(1/\sigma _1^2)},
$$
where $\sigma_0^2$ and $\sigma_1^2$ are the variances of $\Theta$ and $W$, respectively.

Suppose now that we change the observation model to $Y = 3\Theta + W$. In some sense the "signal" $\Theta$ has a stronger presence, relative to the noise term $W$, and we should expect to obtain a smaller mean squared error. Suppose $\sigma _0^2=\sigma _1^2=1$. The mean squared error of the original model $X=\Theta +W$ is then $1/2$. In constrast, what is the mean squared error of the new model $Y=3\Theta +W$ ?

**Solution:**

Since $Y'$ is just $Y$ scaled by a factor of $1/3$, $Y'$ carries the same information as $Y$, so that ${\bf E}[\Theta \mid Y]={\bf E}[\Theta \mid Y']$. Thus, the alternative observation model $Y'=\Theta +(W/3)$ will lead to the same estimates and will have the same mean squared error as the unscaled model $Y=3\Theta +W$. In the equivalent $Y'$ model, we have a noise variance of $1/9$ and therefore the mean squared error is
$$
\frac{1}{\frac{1}{1}+\frac{1}{1/9}}=\frac{1}{10}.
$$

## Exercise 4 Multiple observations and unknowns

Let $\Theta_1, \Theta_2, W_1$ and $W_2$ be independent standard normal random variables. We obtain two observations,
$$
X_1=\Theta _1+W_1,\qquad X_2=\Theta _1+\Theta _2+W_2.
$$
Find the MAP estimate $\hat\theta =(\hat\theta _1,\hat\theta _2)$ of $(\Theta _1,\Theta _2)$ if we observe that $X_1=1,X_2=3$. 

**Solution:**

We focus on the exponential term in the numerator of the expression given by Bayes' rule. The prior contributes a term of the form
$$
e^{-\frac{1}{2}(\theta _1^2+\theta _2^2)}.
$$
Conditioned on $(\Theta _1,\Theta _2)=(\theta _1,\theta _2)$, the measurements are independent. In the conditional universe, $X_1$ is normal with mean $\theta_1,X_2$ is normal with mean $\theta_1 + \theta_2$, and both variances are $1$. Thus, the term $f_{X_1,X_2|\Theta _1,\Theta _2}$ makes a contribution of the form
$$
e^{-\frac{1}{2}(x_1-\theta _1)^2}\cdot e^{-\frac{1}{2}(x_2-\theta _1-\theta _2)^2}.
$$
We substitute $x_1 = 1$ and $x_2=3$, and in order to find the MAP estimate, we minimize the expression
$$
\frac{1}{2}\left(\theta _1^2+\theta _2^2+(\theta _1-1)^2+(\theta _1+\theta _2-3)^2\right).
$$
Setting the derivatives (withe respect to $\theta_1$ and $\theta_2$) to zero, we obtain:
$$
\hat\theta _1+(\hat\theta _1-1)+(\hat\theta _1+\hat\theta _2-3)=0, \qquad \hat\theta _2+(\hat\theta _1+\hat\theta _2-3)=0,
$$
or
$$
3\hat\theta _1+\hat\theta _2=4,\qquad \hat\theta _1+2\hat\theta _2=3.
$$
Either by inspection, or by substitution, we obtain the solution $\hat\theta _1=1, \hat\theta _2=1$.

## Problem 1 Trajectory estimation

The vertical coordinate ("height") of an object in free fall is described by an equation of the form
$$
x(t) = \theta _0 + \theta _1 t + \theta _2 t^2,
$$
where $\theta_0, \theta_1,$ and $\theta_2$ are some parameters and $t$ stands for time. At certain times $t_1, ..., t_n$, we make noisy observations $Y_1, ..., Y_n$, respectively, of the height of the object. Based on these observations, we would like to estimate the object's vertical trajectory.

We consider the special case where there is only one unknown parameter. We assume that $\theta_0$ (the height of the object at time zero) is a known constant. We also assume that $\theta_2$ (which is related to the acceleration of the object) is known. We view $\theta_1$ as the realized value of a continuous random variable $\Theta_1$. The observed height at time $t_i$ is $Y_ i = \theta _0 + \Theta _1 t_ i +\theta _2 t_ i^2 + W_ i,\,  i = 1, \ldots , n$, where $W_i$ models the observation noise. We assume that $\Theta _1\sim N(0,1)$, $W_1,\dots ,W_ n \sim N(0,\sigma ^2)$, and that all these random variables are independent.

In this case, finding the MAP estimate of $\Theta_1$ involves the minimization of
$$
\theta _1^2+ \frac{1}{\sigma ^2}\sum _{i=1}^ n(y_ i-\theta _0-\theta _1 t_ i -\theta _2 t_ i^2)^2
$$
with respect to $\theta_1$.

1. Carry out this minimization and find the formula for the MAP estimate, $\hat{\theta}_1$.
2. The formula for $\hat{\theta}_1$ can be used to define the MAP estimator $\hat{\Theta}_1$ (a random variable), as a function of $t_1, ..., t_n$ and the random variables $Y_1, .., Y_n$. Does the MAP estimator $\hat{\Theta}_1$ has a normal distribution?
3. Let $\sigma=1$ and consider the special case of only two observations ($n=2$). Write down a formula for the mean squared error $\mathbb {E}[(\hat{\Theta }_1-\Theta _1)^2]$, as a function of $t_1$ and $t_2$.
4. Consider the "experimental design" problem of choosing when to make measurements. Under the assumptions of the previous part, and under the constraints $0\leq t_1,t_2 \leq 10$, find the values of $t_1$ and $t_2$ that minimize the mean squared error associated with the MAP estimator.

**Solution:**

1. Setting the partial derivative with respect to $\theta_1$ equal to zero, we obtain
   $$
   \theta _1 -\frac{1}{\sigma ^2} \sum _{i=1}^ n t_ i (y_ i-\theta _0-\theta _1 t_ i -\theta _2 t_ i^2)=0,
   $$
   yielding the MAP estimate
   $$
   \hat\theta _1= \frac{\sum _{i=1}^ n t_ i (y_ i-\theta _0-\theta _2 t_ i^2)}{\sigma ^2 + \sum _{i=1}^ n t_ i^2}.
   $$

2. We have
   $$
   \hat\Theta _1= \frac{\sum _{i=1}^ n t_ i (Y_ i-\theta _0-\theta _2 t_ i^2)}{\sigma ^2 + \sum _{i=1}^ n t_ i^2}.
   $$
   Recall that the observation model is $Y_ i = \theta _0 + \Theta _1t_ i + \theta _2t_ i^2 + W_ i$, and so we can rewrite the estimator as
   $$
   \hat\Theta _1 = \frac{\sum _{i=1}^ n t_ i(\Theta _1t_ i + W_ i)}{\sigma ^2 + \sum _{i=1}^ n t_ i^2} = \frac{\Theta _1\sum _{i=1}^ n t_ i^2 + \sum _{i=1}^ n t_ i W_ i}{\sigma ^2 + \sum _{i=1}^ n t_ i^2}.
   $$
   We see that $\hat{\Theta}_1$ is a linear function of $\Theta_1$ and $W_1, ..., W_n$, which are all normal and independent. Since a linear function of independent normal random variables is normal, it follow that $\hat{\Theta}_1$ is normal.

3. For the special case $\sigma=1$ and $n=2$, that the estimation error is
   $$
   \tilde\Theta _1 \triangleq \hat\Theta _1 - \Theta _1 = \frac{t_1W_1 + t_2W_2- \Theta _1 }{1 + t_1^2 + t_2^2}.
   $$
   Since $\Theta _1,W_1,W_2$ are all zero-mean, independent normal random variables, $\tilde{\Theta}_1$ is also a zero-mean normal random variable. Hence, the mean squared error is
   $$
   \begin{aligned}
   \mathbb {E}[(\hat\Theta _1-\Theta _1)^2] = \mathbb {E}[\tilde\Theta _1^2] = {\rm var}(\tilde\Theta _1)
   &=\frac{{\rm var}(\Theta _1)+t_1^2{\rm var}(W_1)+t_2^2{\rm var}(W_2)}{\left(1+t_1^2+t_2^2\right)^2}\\
   &= \frac{1+t_1^2+t_2^2}{\left(1+t_1^2+t_2^2\right)^2}\\
   &= \frac{1}{1+t_1^2+t_2^2}.
   \end{aligned}
   $$

4. In order to minimize the mean squared error found in the previous part, we should choose the observation times to be as large as possible. Under the constraints $0\leq t_1,t_2\leq 10$, we should choose $t_1 = t_2 = 10$. The intuition is that (since and are known constants), we are effectively making observations of the form
   $$
   Z_ i = \Theta _1 t_ i + W_ i.
   $$
   Or equivalently, we are making observations of the form
   $$
   Z_ i' = \frac{Z_ i}{t_ i}=\Theta _1 + \frac{W_ i}{t_ i}.
   $$
   When the noise term is smallest, more precisely, when its variance is smallest, these observations become more informative. This corresponds to choosing as large as possible.

## Problem 2 Hypothesis test between two normals

Conditioned on the result of an unbiased coin flip, the random variables $T_1,T_2,\ldots ,T_ n$ are independent and identically distributed, each drawn from a common normal distribution with mean zero. If the result of the coin flip is Heads, this normal distribution has variance $1$; otherwise, it has variance $4$. Based on the observed values $t_1,t_2,\ldots ,t_ n$, we use the MAP rule to decide whether the normal distribution from which they were drawn has variance $1$ or variance $4s$. In what condition does the MAP rule decide that the underlying normal distribution has variance $1$?

**Solution:**

Let $\Theta=0$ denote that the observations $t_1, t_2, ..., t_n$ were generated from a normal distribution with variance $1$, and let $\Theta=1$ denote that they were generated from a normal distribution with variance $4$. For simplicity, let us use the notation $\mathcal{N}(t_1, ...,t_n;0,\sigma^2)$ to denote the joint PDF of $n$ i.i.d. normal random variables with mean $0$ and variance $\sigma^2$, evaluated at $t_1, ..., t_n$.

Therefore, given the observations $t_1, ..., t_n$, the posterior probability that the samples are generated from a normal distribution with variance $1$ is
$$
\mathbf{P}(\Theta =0 \mid T_1=t_1, \ldots , T_ n=t_ n) = \frac{(1/2)\cdot N(t_1, \ldots , t_ n;0,1)}{(1/2)\cdot N(t_1, \ldots , t_ n;0,1) + (1/2)\cdot N(t_1, \ldots , t_ n;0,4)}.
$$
Similarly, the probability that the samples are generated from a normal distribution with variance $4$ is given by
$$
\mathbf{P}(\Theta =1 \mid T_1=t_1, \ldots , T_ n=t_ n) = \frac{(1/2)\cdot N(t_1, \ldots , t_ n;0,4)}{(1/2)\cdot N(t_1, \ldots , t_ n;0,1) + (1/2)\cdot N(t_1, \ldots , t_ n;0,4)}.
$$
The MAP rule favors $\Theta=0$ if the following inequality holds
$$
\mathbf{P}(\Theta = 0 \mid T_1=t_1, \ldots , T_ n=t_ n) > \mathbf{P}(\Theta = 1\mid T_1=t_1, \ldots , T_ n=t_ n)
$$
We notice that the denominators in the expressions for $\mathbf{P}(\Theta =0\mid \ldots )$ and $\mathbf{P}(\Theta =1\mid \ldots )$ are the same, so it suffices to compare the numerators. Therefore, the MAP rule favors $\Theta=0$ if the following inequality holds
$$
N(t_1, \ldots , t_ n;0,1) > N(t_1, \ldots , t_ n;0,4)\\
\prod _{i=1}^{n} \frac{1}{\sqrt{2 \pi \cdot 1}} e^{-\frac{t_ i^2}{2\cdot 1}} > \prod _{i=1}^{n} \frac{1}{\sqrt{2 \pi \cdot 4}} e^{-\frac{t_ i^2}{2\cdot 4}}.
$$
With a little bit of algebra, we obtain
$$
\left| \frac{3}{8} \sum _{i=1}^{n} t_ i^2 \right|
 < n \cdot \ln(2)
$$
