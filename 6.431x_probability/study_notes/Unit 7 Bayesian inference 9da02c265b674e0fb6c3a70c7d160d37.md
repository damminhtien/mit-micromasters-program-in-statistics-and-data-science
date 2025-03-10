# Unit 7: Bayesian inference

# Motivation

In this unit, we focus on Bayesian inference, including both hypothesis testing and estimation problems.

1.  We apply the Bayes rule to find the posterior distribution of an unknown random variable given one or multiple observations of related random variables.
2. We discuss the most common methods for coming up with a point estimate of the unknown random variable (Maximum a Posteriori probability estimate, Least Mean Squares estimate, and Linear Least Mean Squares estimate).
3. We consider the question of performance analysis, namely, the calculation of the probability of error in hypothesis testing problems or the calculation of the mean squared error in estimation problems.
4. To illustrate the methodology, we pay special attention to a few canonical problems such as linear normal models and the problem of estimating the unknown bias of a coin.

Unit overview slide: [[clean]](https://courses.edx.org/assets/courseware/v1/1532963cd2cf4d73af6c401de4b17581/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U7-overview-slide.pdf)

# Lecture 14: Introduction to Bayesian inference

[Course | edX](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__14_Introduction_to_Bayesian_inference)

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/7cc7ffe1100786c2660ac3371b05252b/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L14-clean.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/d1146be0ccdf4f519873c048343938e9/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L14-annotated.pdf)

More information is given in [Sections 8.1 and 8.2 of the text](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/61).

You are also encouraged to review the different variants of the Bayes rule, in the last part of Lecture 10 and in [Section 3.6 of the text](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/27).

Source attributions:

S&P 500 chart from [http://finance.yahoo.com/](http://finance.yahoo.com/) (fair use)

Genomics graphic from unknown source (fair use)

Systems biology graphic from [http://commons.wikimedia.org/wiki/File:Signal_transduction_v1.png](http://commons.wikimedia.org/wiki/File:Signal_transduction_v1.png) (CC license)

Electoral vote distribution graphic copyright Stanford University, 2012 (fair use)

### **Motivation of Lecture 14**

- The big picture
    - motivation, applications
    - problem types (hypothesis testing, estimation, etc)
- The general framework
    - Bayes’ rule → posterior (4 versions)
    - Point estimates (MAP, LMS)
    - Performance measures (prob. of error; mean squared error)

### The big picture of Inference

![Untitled](Unit%207%20Bayesian%20inference%209da02c265b674e0fb6c3a70c7d160d37/Untitled.png)

## 14.1. Model building versus inferring unobserved variables

$X=aS+W$

- Model building:
    - know “signal” S, observe X
    - infer a
- Variable estimation:
    - know a, observe X
    - infer S

![Untitled](Unit%207%20Bayesian%20inference%209da02c265b674e0fb6c3a70c7d160d37/Untitled%201.png)

| **Hypothesis testing** | **Estimation** |
| --- | --- |
| + unknown takes one of few possible values
+ aim at small probability of incorrect decision | + numerical unknown(s)
+ aim at an estimate that “close” to true but unknown value |

# [Lecture 15: Linear models with normal noise](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__15_Linear_models_with_normal_noise)

In this lecture we focus on an important special case of inference problems in which the random variables of interest are normal and are related through linear relations. We show that the posterior distribution is also normal and examine how we can calculate the posterior mean and variance. We illustrate the methodology through a progression of increasingly complex examples, including the problem of estimating a trajectory on the basis of multiple noisy measurements.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/73780eb6023b23df88ff18475255f11b/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L15-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/61e5005a7c3429b4d4814bfe7c855020/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L15-annotated.pdf)

Some of the material in this lecture is covered in Example 8.3 on page 415 and page 421, and on pages 480-482 of the textbook.

For a written summary of the trajectory estimation problem, see [this document](https://courses.edx.org/assets/courseware/v1/21ddfd5247c2500011c50b549bdf705b/asset-v1:MITx+6.431x+1T2024+type@asset+block/estimation-tracking-post-6.041x.pdf).

### Recognizing normal PDFs

$f_X(x)=c.e^{-(\alpha x^2+\beta x +\gamma)} \quad \alpha>0$ Normal wth mean $-\beta/2\alpha$ and variance $1/2\alpha$

# [Lecture 16: Least mean squares (LMS) estimation](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__16_Least_mean_squares__LMS__estimation)

In this lecture we focus on the conditional expectation estimator. We show that it minimizes both the conditional and the unconditional mean squared estimation error. We develop some its mathematical properties and also illustrate the calculation of the mean squared error.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/6c0ff8ab30b0fd1c4299e1675b919d4f/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L16-clean.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/203ab23c0eb72c70442fea689df9c97f/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L16-annotated.pdf)

More information is given on pp. 225-226 of the text as well in [Section 8.3](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/65).

# [Lecture 17 (Optional Ungraded): Linear least mean squares (LLMS) estimation](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@_Optional_Ungraded__Lec__17_Linear_least_mean_squares__LLMS__estimation)

In this section we consider the **estimator that minimizes the mean squared error** within the restricted class of estimators that depend linearly on the observations. 

We develop and interpret a **simple formula for this estimator for the special case of a single observation**.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/b0851a276fada05f0f9fb3f8af0ca5ae/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L17-clean.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/cd199a805ba40132f4454dc6ebb398f4/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L17-annotated.pdf)

More information is given in [Section 8.4](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/66) of the textbook.

## 17.1. LLMS formulation

Linear regression without a constant term and the method of least squares are applied here to minimize prediction error by choosing the best linear estimator.
In statistics, the method of least squares is a standard approach to approximate the solution of overdetermined systems by minimizing the sum of the squares of the residuals. In this context, without a constant term, the best linear unbiased estimator (BLUE) of the coefficient is derived by setting the derivative of the MSE to zero, which simplifies to a ratio of the covariance of $X$ and $\Theta$ to the variance of $X$.

### Exercise 1: LMS and LLMS

Suppose that the random variables $\Theta$ and $X$ are not independent, but ${\mathbb E}[\Theta \mid X=x]=3$ for all $x$. Then the LLMS estimator of $\Theta$ based on $X$ is of the form $aX+b$, with

$a=0, b=3$

### Exercise 2: LLMS without a constant term

Suppose that instead of estimators of the form $aX+e$, we consider estimators of the form  $\widehat\Theta =aX$ and ask for the value of a that minimizes the mean squared error. Mimic the derivation you have just seen and find the optimal value of $a$. Your answer should be an algebraic expression involving some of the constants $b, c, d$, where $b={\mathbb E}[\Theta ^2], c={\mathbb E}[\Theta X], d={\mathbb E}[X^2]$.

**1. Define the Mean Squared Error (MSE)**

The mean squared error of the estimator $\widehat{\Theta}$  given the true value $\Theta$ is:
$\textsf{MSE} = \mathbb{E}[(\widehat{\Theta} - \Theta)^2]$ 

Substituting $\widehat{\Theta} = aX$: 
$\textsf{MSE} = \mathbb{E}[(aX - \Theta)^2]$

**2. Expand the MSE expression**

Expanding the square gives:
$\textsf{MSE} = \mathbb{E}[a^2X^2 - 2aX\Theta + \Theta^2]$

Using linearity of expectation:
$\textsf{MSE} = a^2\mathbb{E}[X^2] - 2a\mathbb{E}[X\Theta] + \mathbb{E}[\Theta^2]$

Plugging in the constants $b, c, d$ where $b = \mathbb{E}[\Theta^2], c = \mathbb{E}[\Theta X]$, and $d = \mathbb{E}[X^2]$:
$\textsf{MSE} = a^2d - 2ac + b$

**3. Differentiate MSE with respect to $a$ and set to 0**

Differentiating the MSE with respect to $a$ and setting it equal to zero to find the critical points:
$\frac{d}{da}(\text{MSE}) = 2ad - 2c = 0 \rightarrow a = \frac{c}{d}$ 

**4. Verify the minimization**

To ensure that this value of $a$ indeed minimizes the MSE, check the second derivative:
$\frac{d^2}{da^2}(\text{MSE}) = 2d$.

Since $d = \mathbb{E}[X^2] > 0$ (assuming $X$ is not a degenerate random variable), the second derivative is positive, confirming that $a = \frac{c}{d}$ minimizes the MSE.

### Exercise 3: LLMS drill

Suppose that $\Theta$ and $W$ are independent, both with variance 1, and that  $X=\Theta +W$. Furthermore, ${\mathbb E}[\Theta ]=1$ and ${\mathbb E}[W]=2$. The LLMS estimator $\widehat\Theta =aX+b$ has
$a=?, b=?$
Hint: Remember the formula $\textsf{Cov}(X+Y,Z)=\textsf{Cov}(X,Z)+\textsf{Cov}(Y,Z)$.

Given:

- $\mathbb{E}[\Theta] = 1$
- $\mathbb{E}[W] = 2$
- $\textsf{Var}(\Theta) = 1$
- $\textsf{Var}(W) = 1$

Since $\Theta$ and $W$ are independent:

- $\mathbb{E}[X] = \mathbb{E}[\Theta + W] = \mathbb{E}[\Theta] + \mathbb{E}[W] = 1 + 2 = 3$
- $\textsf{Var}(X) = \textsf{Var}(\Theta) + \textsf{Var}(W) = 1 + 1 = 2$
- $\textsf{Cov}(\Theta, X) = \textsf{Cov}(\Theta, \Theta + W) = \textsf{Cov}(\Theta, \Theta) + \textsf{Cov}(\Theta, W) = \textsf{Var}(\Theta) = 1$ (since $\Theta$ and $W$ are independent, their covariance is 0)

The LLMS estimator $\widehat{\Theta} = aX + b$ aims to minimize the mean squared error between $\widehat{\Theta}$ and $\Theta$. The optimal coefficients $a$ and $b$ can be found using:

- $a = \frac{\textsf{Cov}(X, \Theta)}{\textsf{Var}(X)}$
- $b = \mathbb{E}[\Theta] - a\mathbb{E}[X]$

Substitute the values:

- $a = \frac{\textsf{Cov}(X, \Theta)}{\textsf{Var}(X)} = \frac{1}{2}$
- $b = \mathbb{E}[\Theta] - a\mathbb{E}[X] = 1 - \frac{1}{2} \times 3 = -\frac{1}{2}$

### Exercise 4: Possible values of the estimates

Suppose that the random variable $\Theta$ takes values in the interval [0,1].

a) Is it true that the LMS estimator is guaranteed to take values only in the interval [0,1]?

Yes

b) Is it true that the LLMS estimator is guaranteed to take values only in the interval [0,1]?

No

**Solution**

a) The conditional expectation ${\mathbb E}[\Theta \mid X=x]$ is a weighted average of the values of $\Theta$, weighted according to the posterior PDF. A weighted average of values in [0,1] must lie in [0,1].

b) On the other hand, there is no such guarantee for the LLMS estimator. You can see this from the picture in the last example. Or you may consider the example where $X=\Theta +W$, where $W$ can take any real value. Then, the term $aX$ can take any real value, and can therefore fall outside the range [0,1].

### Exercise 5: Comparison for the coin problem

Recall that the MAP estimator for the problem of estimating the bias of a coin is $X/n$, which is different from the LLMS estimator $(X+1)/(n+2)$. How do they compare in terms of mean squared error (MSE)?

**Solution**

The LLMS estimator coincides with the LMS estimator and therefore achieves the smallest possible mean squared error.

### Exercise 6: LLMS with multiple observations

Suppose that $\Theta, X_1, X_2$ have zero means. Furthermore,

$\textsf{Var}(X_1)=\textsf{Var}(X_2)=\textsf{Var}(\Theta )=4,$ and $\textsf{Cov}(\Theta ,X_1)=\textsf{Cov}(\Theta ,X_2)=\textsf{Cov}(X_1,X_2)=1.$

The LLMS estimator of $\Theta$ based on $X_1$ and $X_2$ is of the form $\widehat\Theta = a_1X_1 + a_2X_2 + b$. Find the coefficients $a_1, a_2, b$. *Hint:* To find b, recall the argument we used for the case of a single observation.

Given:

- $\mathbb{E}[\Theta]=\mathbb{E}[X_1]=\mathbb{E}[X_2]=0$
- $\textsf{Var}(X_1) = \textsf{Var}(X_2) = \textsf{Var}(\Theta) = 4$
- $\textsf{Cov}(\Theta, X_1) = \textsf{Cov}(\Theta, X_2) = \textsf{Cov}(X_1, X_2) = 1$

We form the covariance matrix $\Sigma$ for $X_1$ and $X_2$:

$$
\Sigma = \begin{bmatrix}
\textsf{Var}(X_1) & \textsf{Cov}(X_1, X_2) \\
\textsf{Cov}(X_2, X_1) & \textsf{Var}(X_2)
\end{bmatrix} = \begin{bmatrix}
4 & 1 \\
1 & 4
\end{bmatrix}
$$

The cross-covariance vector between $\Theta$ and the observations $(X_1, X_2)$ is:

$$
\textsf{Cov}(\Theta, X) = \begin{bmatrix}
\textsf{Cov}(\Theta, X_1) \\
\textsf{Cov}(\Theta, X_2)
\end{bmatrix} = \begin{bmatrix}
1 \\
1
\end{bmatrix} 
$$

We use the LLMS estimator formula:

$$
\begin{bmatrix}
a_1 \\
a_2
\end{bmatrix} = \Sigma^{-1} \times \textsf{Cov}(\Theta, X)
$$

First, calculate $\Sigma^{-1}$:

$$
\Sigma^{-1} = \frac{1}{\textsf{det}(\Sigma)} \begin{bmatrix}
4 & -1 \\
-1 & 4
\end{bmatrix} = \frac{1}{15} \begin{bmatrix}
4 & -1 \\
-1 & 4
\end{bmatrix} 
$$

Then multiply by the covariance vector:

$$
\begin{bmatrix}
a_1 \\
a_2
\end{bmatrix} = \frac{1}{15} \begin{bmatrix}
4 & -1 \\
-1 & 4
\end{bmatrix} \begin{bmatrix}
1 \\
1
\end{bmatrix} = \frac{1}{15} \begin{bmatrix}
3 \\
3
\end{bmatrix} = \begin{bmatrix}
0.2 \\
0.2
\end{bmatrix}
$$

The estimator $\widehat{\Theta}$ also has a zero mean:

$$
\mathbb{E}[\widehat{\Theta}] = a_1\mathbb{E}[X_1] + a_2\mathbb{E}[X_2] + b = 0
$$

Thus, $b = 0$ since $\mathbb{E}[X_1]=\mathbb{E}[X_2]=0$.

### Exercise 7: Choice of representations

We wish to estimate an unknown quantity $\Theta$. Our measuring equipment produces an observation of the form $X=\Theta ^3+W$, where $W$ is a noise term which is small relative to the range of $\Theta$. Which type of linear estimator is preferable in such a situation?

**Solution:**

If the noise $W$ were completely absent, we would estimate $\Theta$ by letting  $\widehat\Theta =X^{1/3}$. In the presence of small noise, our estimator should again have a similar form, which argues in favor of the third option.