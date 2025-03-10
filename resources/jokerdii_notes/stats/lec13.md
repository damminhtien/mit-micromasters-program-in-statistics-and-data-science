# Lecture 13. Chi Squared Distribution, T-Test

There are 9 topics and 6 exercises.

## 1. Hypothesis Testing (Review)

#### Review:

We have seen the basic notions of hypothesis testing:

* Hypotheses $H_0 / H_1$​,
* Type 1/ Type 2 error, level and power,
* Test statistics and rejection region,
* p-value.

Our tests were based on CLT (and sometimes Slutsky)...

* What if data is Gaussian, $\sigma^2$​​​​ is unknown and Slutsky does not apply? **T-test**.
* Can we use asymptotic normality of MLE? **Wald's test**.
* Tests about multivariate parameter $\theta=(\theta_1, ..., \theta_d)$​​​​ (e.g.: $\theta_1 = \theta_2$​​​)? **Testing implicit hypotheses**.
* More complex tests: "Does my data follow a Gaussian distribution"? **Goodness of fit**.

**Problem Set-up:**

The National Assessment of Educational Progress tested a simple random sample of $n$ thirteen year old students in both 2004 and 2008 and recorded each student's score. The standard deviation in 2004 was 39. In 2008, the standard deviation was 38.

Your goal as a statistician is to assess whether or not there were statistically significant changes in the average test scores of students from 2004 to 2008. To do so, you make the following modeling assumptions regarding the test scores:

- $X_1, ..., X_n$ represent the scores in 2004.
- $X_1, ..., X_n$​ are iid Gaussians with standard deviation $39$.
- $\mathbb{E}[X_1] = \mu_1$, which is an unknown parameter.
- $Y_1, ..., Y_n$ represent the scores in 2008.
- $Y_1, ..., Y_n$ are iid Gaussians with standard deviation $38$.
- $\mathbb{E}[Y_1] = \mu_2$, which is an unknown parameter.
- $X_1,..., X_n$ are independent of $Y_1, ..., Y_n$.

You define your hypothesis test in terms of the null $H_0: \mu_1 = \mu_2$ (Signifiying that there were not significant changes in test scores) and $H_1: \mu_1 \neq \mu_2$​. We can conclude that

* The test given above is a **two-sided, two-sample test.**

* Assuming that the null hypothesis holds, the distribution of the statistic $\sqrt{n} \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}}$​​​ is **standard Gaussian.**
  $$
  \sqrt{n} \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
  $$
  Since by **linearity of expectation**,
  $$
  \mathbb {E}\left[ \sqrt{n} \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \right] = \sqrt{\frac{n}{38^2 + 39^2}} ( \mathbb {E}[\overline{X}_ n] - \mathbb {E}[\overline{Y}_ n] ) = 0.
  $$
  By **independence**, the variance is additive
  $$
  \text {Var}\left( \sqrt{n} \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \right) = \frac{1}{n(38^2 + 39^2)} \left( \sum _{i = 1}^ n \text {Var}(X_ i) + \sum _{i = 1}^ n \text {Var}(Y_ i) \right) = 1.
  $$

* Suppose now that the variance $\sigma_X^2$​ of $X_1, ..., X_n$​ and the variance $\sigma_Y^2$​ of $Y_1, ..., Y_n$​ are unknown. Let $\widehat{\sigma _ X}^2$​ denote the sample variance of $X_1, ..., X_n$​, and let $\widehat{\sigma _ Y}^2$​ denote the sample variance of $Y_1, ..., Y_n$​​. Assuming the null hypothesis holds, the statistic converges to standard Gaussian by **Slutsky's theorem**.

  Since $\widehat{\sigma _ X}$​ and $\widehat{\sigma _ Y}$​ are random variables, the distribution of the above cannot be standard Gaussian for any fixed $n$. However, we know that
  $$
  \widehat{\sigma _ X} \xrightarrow {n \to \infty } \sigma _ X, \quad \widehat{\sigma _ Y} \xrightarrow {n \to \infty } \sigma _ Y
  $$
  Therefore, **Slutsky's theorem** applies because
  $$
  \sqrt{n} \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{\sigma _ X^2 + \sigma _ Y^2}} \sim \mathcal{N}(0,1)
  $$
  Therefore we conclude that
  $$
  \sqrt{n} \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{\widehat{\sigma _ X}^2 + \widehat{\sigma _ Y}^2}} \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
  $$

* Assuming true variances are known: $\sigma_X^2 = 39^2, \ \sigma_Y^2 = 38^2$​. Accordingly, you design the test,
  $$
  \psi = \mathbf{1}\left( \sqrt{n}\bigg| \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \bigg| \geq q_{\eta /2} \right)
  $$
  where $q_{\eta}$​ represents the $1- \eta$​ quantile of a standard Gaussian. 

  The level of this test is $\eta$​, which can be either **non-asymptotic** or **asymptotic**.

  The level is given by
  $$
  P( |Z| > q_{\eta /2} ) = \eta
  $$
  where $Z \sim \mathcal{N}(0,1)$.

## 2. Parametric Hypothesis Testing - Clinical Trials

#### Notation and modeling

* Let $\Delta_d > 0$ denote the expected decrease of LDL level (in mg/dL) for a patient that has used the drug.
* Let $\Delta_c \geq 0$ denote the expected decrease of LDL level (in mg/dL) for a patient that has used the placebo.
* We want to know if $\Delta_d > \Delta_c$.
* We observe two independent samples:
  * $X_1, ..., X_n \stackrel{iid}{\sim} \mathcal{N}(\Delta_d ,\sigma_d^2)$​ from the test group and
  * $Y_1, ..., Y_m \stackrel{iid}{\sim}\mathcal{N}(\Delta_c, \sigma_c^2)$ from the control group.

Consequence of Gaussian Samples

* $\overline{X}_ n=\frac{X_1 + X_2 + \dots + X_ n}{n}$ is a Gaussian random variable
* $\overline{Y}_ m=\frac{Y_1 + Y_2 + \dots + Y_ m}{m}$ is a Gaussian random variable
* $\overline{X}_ n-\overline{Y}_ m=\frac{X_1 + X_2 + \dots + X_ n}{n} - \frac{Y_1 + Y_2 + \dots + Y_ m}{m}$ is a Gaussian random variable
* $X_ i + Y_ j$​ is​ a Gaussian random variable for any $i=1, ..., n$​ and $j=1,...,m$.
* The variance of $\overline{X}_ n - \overline{Y}_ m$ is $\frac{\sigma _ d^2}{n} + \frac{\sigma _ c^2}{m}$.

#### Hypothesis Testing

* Hypotheses:
  $$
  H_0: \Delta_c = \Delta_d \ \  vs. \ \ H_1: \Delta_d > \Delta_c
  $$

* Since the data is Gaussian by assumption we don't need the CLT.

* We have
  $$
  \overline{X}_n \sim \mathcal{N}(\Delta_d, {\sigma_d^2\over n})\ \ \text{and} \ \ \overline{Y}_m \sim \mathcal{N}(\Delta_c, {\sigma_c^2\over m})
  $$

* Therefore,
  $$
  {\overline{X}_n - \overline{Y}_n - (\Delta_d - \Delta_c) \over \sqrt{{\sigma_d^2 \over n} + {\sigma^2_c \over m}}} \sim \mathcal{N}(0,1)
  $$
  But there is an issue that we do not know $\sigma^2_d$​ and $\sigma_c^2$​.

## 3. Parametric Hypothesis Testing - Asymptotic Test with Level Alpha

#### Asymptotic test

* Assume that $m=cn$​ and $n \rightarrow \infty$​.

* Using **Slutsky's lemma**, we also have
  $$
  {\overline{X}_n - \overline{Y}_n - (\Delta_d - \Delta_c) \over \sqrt{{\widehat{\sigma_d}^2 \over n} + {\widehat{\sigma_c}^2 \over m}}} \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}(0,1)
  $$
  where 
  $$
  \hat{\sigma}_d^2 = {1\over n}\sum^n_{i=1} (X_i - \bar{X}_n^2)^2 \ \ \text{and} \ \ \hat{\sigma}_d^2 = {1\over n}\sum^n_{i=1} (Y_i - \bar{Y}_m^2)^2
  $$
  Scaling by ${1\over n-1}$​ leads to an unbiased estimator for the covariance between two random variables, thus
  $$
  \hat{\sigma}_d^2 = {1\over n-1}\sum^n_{i=1} (X_i - \bar{X}_n^2)^2 \ \ \text{and} \ \ \hat{\sigma}_d^2 = {1\over n-1}\sum^n_{i=1} (Y_i - \bar{Y}_m^2)^2
  $$
  Since by **Continuous Mapping Theorem (CMT)**,
  $$
  {\sqrt{{\widehat{\sigma_d}^2 \over n} + {\widehat{\sigma_c}^2 \over m}}\over \sqrt{{{\sigma_d}^2 \over n} + {{\sigma_c}^2 \over m}}} \xrightarrow[n \rightarrow \infty]{\mathbf{P}}1
  $$
  Thus, by **Slutsky's theorem**,
  $$
  {\overline{X}_n - \overline{Y}_n - (\Delta_d - \Delta_c) \over \sqrt{{\widehat{\sigma_d}^2 \over n} + {\widehat{\sigma_c}^2 \over m}}} \times {\sqrt{{\widehat{\sigma_d}^2 \over n} + {\widehat{\sigma_c}^2 \over m}}\over \sqrt{{{\sigma_d}^2 \over n} + {{\sigma_c}^2 \over m}}} = {\overline{X}_n - \overline{Y}_n - (\Delta_d - \Delta_c) \over \sqrt{{{\sigma_d}^2 \over n} + {{\sigma_c}^2 \over m}}} \xrightarrow[n\rightarrow \infty]{(d)} \mathcal{N}(0,1)
  $$
  
* We get the following test at asymptotic level $\alpha$.
  $$
  R_\psi = \Bigg\{ {\overline{X}_n \cdot \overline{Y}_m \over \sqrt{{\widehat{\sigma_d}^2 \over n} + {\widehat{\sigma_c}^2 \over m}}} > q_\alpha \Bigg\}
  $$

* This is a **one-sided, two-sample** test.

Example:

* $n=70, m=50, \bar{X}_n = 156.4, \bar{X}_m=132.7, \hat{\sigma}_d^2 = 5198.4, \hat{\sigma}_c^2 = 3867.0$,
  $$
  {156.4 - 132.7 \over \sqrt{{5198.4 \over 70} + {3867.0 \over 50}}} = 1.57
  $$
  Since $q_{5\%}=1.645$, we fail to reject the $H_0$.

* We can also compute the p-value = $\mathbf{P}(\mathcal{N}(0,1) > 1.57) = 0.0582$.

## 4. Hypothesis Testing in the Regime of Small Sample Sizes

* What if $n=20, m=12$​​? We cannot realistically apply Slutsky's lemma.

  * Because the calculation presented on the given slides was an asymptotic analysis (*i.e.*, we assumed $n \rightarrow \infty$​). Slutsky's theorem only gives a good approximation when the sample size is very large.

* We needed it to find the (asymptotic) distribution of quantities of the form
  $$
  {\bar{X}_n - \mu \over \sqrt{\hat{\sigma}^2}}
  $$
  when $X_1, ..., X_n \stackrel{iid}{\sim}\mathcal{N}(\mu, \sigma^2)$​​.

* It turns out that this distribution does not depend on $\mu$ or $\sigma$​ so we can compute its **quantiles**.

## 5. The Chi-Squared Distribution and its Properties

* The definition of $\chi^2$​ distribution:

  For a positive integer $d$, the $\chi^2$ distribution with $d$ degrees of freedom is the law of the random variable $Z_1^2 + Z_2^2 + ... + Z_d^2$, where $Z_1, ..., Z_d \stackrel{iid}{\sim}\mathcal{N}(0,1)$​.

  

  Example:

  * If $Z \sim \mathcal{N}(0, I_d)$​, then $||Z||_2^2 \sim \chi_d^2$​.

    The PDF of $X \sim X_k^2 = \Gamma ({k \over 2}, {1\over 2})$​​ is
    $$
    {1\over 2^{k/2} \Gamma({k \over 2})} x^{k/2-1} e^{-x/2}, \ \ x > 0
    $$

  * $\chi_2^2 = \text{Exp}(1/2)$​.

  We should see the expectation and variance increase with the increase of the degree of freedom.

* Properties of $\chi^2$ distribution:

  For a positive integer $d$​​​, the $\chi^2$​​​ Distribution with $d$​​​ Degrees of freedom is the law of the random variable $Z_1^2 + ... + Z_d^2$​​, where $Z_1, ..., Z_d \stackrel{iid}{\sim} \mathcal{N}(0,1)$.

  If $V\sim \chi_k^2$​, then

  * $\mathbb{E}[V]=\mathbb{E}[Z^2_1] + ... + \mathbb{E}[Z_d^2] = d$.

  * $\text{Var}[V] = \text{Var}[Z_1^2]+ ... + \text{Var}[Z_d^2] = 2d$

    Since $\text{Var}[Z_1^2] = \mathbb{E}[Z_1^4] -1 = 3-1 =2$.

> #### Exercise 75
>
> 1. What is the smallest possible sample space of $\chi_d^2$?
>
> 2. If $X \sim \chi_d^2$, what is $\mathbb{E}[X]$?
>
> 3. Let $\mathbf{Z} \sim \mathcal{N}(0, I_{d \times d})$ denote a random vector whose components are standard Gaussians: $Z^{(1)}, \ldots , Z^{(d)} \sim \mathcal{N}(0,1)$. Which one of the following random variables has a $\chi$-squared distribution with $d$ degrees of freedom.
>
>    a. $\max (Z^{(1)}, \ldots , Z^{(d)})$
>
>    b. $|Z^{(1)}| + |Z^{(2)}| + \cdots |Z^{(d)}|$
>
>    c. $\left\|  \mathbf{Z} \right\| _2$
>
>    d. $\left\|  \mathbf{Z} \right\| _2^2$
>
> **Solution:**
>
> 1. The smallest possible sample space of $Z^2$​ is $\R_{\geq 0}$​, since the smallest sample space of a Gaussian random variable $Z$​ is $\R$​.
>
> 2. By linearity of expectation,
>    $$
>    \mathbb {E}[X] = \mathbb {E}[Z_1^2 + Z_2^2 + \cdots + Z_ d^2] = d \cdot 1 = d,
>    $$
>    Because $Z_1, \ldots , Z_ d \stackrel{iid}{\sim } \mathcal{N}(0,1)$.
>
> 3. The $\ell_2$ norm $||\cdot||_2$ measures the Euclidean distance from the origin. Hence, if $\mathbf{Z} \sim \mathcal{N}(0, I_{d \times d})$, then
>    $$
>    \left\|  \mathbf{Z} \right\| _2^2 = \left(Z^{(1)}\right)^2 + \left(Z^{(2)}\right)^2 + \cdots + \left(Z^{(d)}\right)^2 \sim \chi _ d^2.
>    $$

> #### Exercise 76
>
> You are playing darts on a dart-board that is represented by the entire plane, $\R^2$. You get a 'bullseye' if the dart lands inside of the unit disc $D^1 := \{  (x, y): x^2 + y^2 \leq 1 \}$. You dart throws are modeled by a Gaussian random vector $\mathbf{Z}$, where $Z^{(1)}, Z^{(2)} \stackrel{iid}{\sim } \mathcal{N}(0,1)$.
>
> Let $f_d$​ represent the density of the $\chi_d^2$​ distribution. What is the probability of getting a bullseye?
>
> **Answer:** $\int _0^1 f_2(x) \,  dx$​
>
> **Solution:** 
>
> A bullseye is given by the event $\left(Z^{(1)}\right)^2 + \left(Z^{(2)}\right)^2 \leq 1$. Since $\left(Z^{(1)}\right)^2 + \left(Z^{(2)}\right)^2 \sim \chi _2^2$, it follows that
> $$
> P(\text {bullseye}) = \int _{0}^1 f_2(x) \,  dx.
> $$

> #### Exercise 77
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathcal{N}(0, \sigma ^2)$​ and let
> $$
> V_ n = \frac{1}{n} \sum _{i = 1}^ n X_ i^2
> $$
> denote the sample second moment. For an appropriate deterministic constant $a$​, that depends on $n$​ and $\sigma^2$​, and an integer $k$, we have that $a \cdot V_n \sim \chi_k^2$. 
>
> 1. What is $a$​​?
> 2. How many degrees of freedom does the above $\chi$-squared random variable have? 
>
> **Answer:**
>
> 1. $a = n/\sigma^2$​
> 2. $k=n$​
>
> **Solution:**
>
> Observe that
> $$
> \frac{n}{\sigma ^2} V_ n = \sum _{i = 1}^ n \frac{X_ i^2}{\sigma ^2}= \sum _{i = 1}^ n \left(\frac{X_ i}{\sigma }\right)^2,
> $$
> and $X_ i/\sigma \sim \mathcal{N}(0,1)$ because $X_ i \sim \mathcal{N}(0, \sigma ^2)$. Hence, $\frac{n}{\sigma ^2} V_ n$ is a $\chi_n^2$ random variable.

## 6. Sample Variance and Sample Mean of IID Gaussians: Cochran's Theorem

The sample variance:

* **Cochran's theorem** states that for $X_1, ..., X_n \stackrel{iid}{\sim}\mathcal{N}(\mu,\sigma^2)$, $S_n$​ is the sample variance defined as 
  $$
  S_n = {1\over n}\sum^n_{i=1}(X_i - \bar{X}_n)^2 = {1\over n} \sum^n_{i=1}X_i^2 - (\bar{X}_n)^2
  $$

* For $X_1, ..., X_n \stackrel{iid}{\sim}\mathcal{N}(\mu,\sigma^2)$​, if $S_n$​ is the sample variance, then it satisfies

  * $\bar{X}_n \perp S_n$​​ for all $n$​​, i.e., $\overline{X}_n$​ is independent of  $S_n$,​

  * ${n S_n\over \sigma^2} \sim \chi_{n-1}^2$​​.

  * We often prefer the unbiased estimator of $\sigma^2$.

    $\tilde{S}_n = {1\over n-1}\sum^n_{i=1} (X_i - \bar{X}_n)^2 = {n \over n-1} S_n$​.

    $\mathbb{E}[\tilde{S}_n] = {n \over n-1}\mathbb{E}[{\sigma^2 \over n} \chi^2_{n-1}] = {n \sigma^2 \over n-1} (n-1) = \sigma^2$​​​​​.

* For unbiased sample variance $\tilde{S}_n$​ of $X_1, ..., X_n$, which is
  $$
    \widetilde{S}_ n = \frac{1}{n-1} \sum _{i=1}^ n \left(X_ i - \overline{X}_ n\right)^2
  $$
  $\frac{(n-1)\widetilde{S}_ n}{\sigma ^2}$​​​ is a $\chi_{n-1}^2$​​​ random variable, thereby the distribution of $\frac{\widetilde{S}_ n}{\sigma ^2}$​​​ is the distribution of a $\chi _{n-1}^2$​​​​ random variable scaled by ${1\over n -1}$.

> #### Exercise 78
>
> Verify that Cochran's theorem holds when $n=2$. Let $X_1, X_2 \stackrel{iid}{\sim } \mathcal{N}(\mu , \sigma ^2)$.
>
> The expression $S_2$​​​ can be written in the form $A^2$​​ where $A$​​ is a polynomial in $X_1$​ and $X_2$​.
>
> 1. What is $A^2$​​?​
>
> 2. The expression $A$​​​​​ is a random variable, and is distributed as $\mathcal{N}(\mu^*, (\sigma^*)^2)$​​​​​ for some $\mu^*$​​​​ and $\sigma^*$​​​​ that can be expressed in terms of the original parameters $\mu$ and $\sigma$.
>
>    What is $\mu^*$​ and $(\sigma^*)^2$?
>
> **Solution:**
>
> 1. Observe that
>    $$
>    S_ n = \frac{X_1^2 + X_2^2}{2} - \left( \frac{X_1 + X_2}{2} \right)^2 = \frac{X_1^2}{4} + \frac{X_2^2}{4} - \frac{1}{2} X_1 X_2 = \left( \frac{X_1 - X_2}{2} \right)^2.
>    $$
>
> 2. We can take $A =\pm \frac{X_1 - X_2}{2}$. Then,
>    $$
>    \mathbb {E}[A] = \frac{1}{2}\mathbb {E}[X_1 - X_2] = \frac{1}{2}(\mu - \mu ) = 0,
>    $$
>    and
>    $$
>    \text {Var}(A) = \text {Var}\left(\frac{X_1 - X_2}{2}\right) = \frac{1}{4} (\text {Var}(X_1) + \text {Var}(X_2)) = \frac{\sigma ^2}{2}.
>    $$

## 7. Student's T Distribution

Definition of student's t distribution:

For a positive integer $d$, the Student's T distribution with $d$ degrees of freedom (denoted by $t_d$) is the law of the random variable ${Z \over \sqrt{V/d}}$, where $Z \sim \mathcal{N}(0,1), V \sim \chi_d^2$ and $Z \perp V$ ($Z$ is independent of $V$).

> #### Exercise 79
>
> 1. Consider the distribution $\chi_n^2$​​​​. Let $f_n:\R \rightarrow \R$​​​​ denote the PDF of $\chi_n^2$​​​​, and let $A_n$​​​​ denote the maximizer of $f_n$​​​. (i.e., the peak of the PDF of the distribution $\chi_n^2$​​​ is located at $A_n$​​​). What is $\lim _{n \to \infty } A_ n$​​​​?
> 2. Consider the Student's T Distribution, which is defined to be the distribution of $T_ n := \frac{Z}{\sqrt{V/n}}$, where $Z \sim \mathcal{N}(0,1),V \sim \chi_n^2$, and $Z$ and $V$ are independent. Let $g_n$ denote the PDF of $T_n$, and let $B_n$ denote the maximizer of $g_n$ (i.e., the peak of the PDF of the distribution $T_n$ Is located at $B_n$). What is $\lim _{n \to \infty } B_ n$?
>
> **Answer:**
>
> 1. $\lim _{n \to \infty } A_ n = \infty$​.
> 2. $\lim _{n \to \infty } B_ n= 0$​​
>
> **Solution:**
>
> 1. The graph of the PDF of $\chi _ n^2$​ in the slides shows that the peak of the distribution moves to the right as $n \rightarrow \infty$. Hence
>    $$
>    \lim _{n \to \infty } A_ n = \infty
>    $$
>    This is intuitive since 
>    $$
>    \mathbb {E}[X] = n, \ \ \text{if} \ X \sim \chi _ n^2
>    $$
>
> 2. As $n \rightarrow \infty$​, the random variable $V/n$​ converges to $1$​ In probability. Hence, as $n \rightarrow \infty$.
>    $$
>    T_ n \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0,1).
>    $$
>    which implies 
>    $$
>    \lim _{n \to \infty } B_ n= 0
>    $$

## 8. The Student's T Test (T Test)

* One sample, two-sided:

  Let $X_1, ..., X_n \stackrel{i.i.d}{\sim} \mathcal{N}(\mu,\sigma^2)$​​​ where​​ both $\mu$​​​ and $\sigma^2$​​​ are unknown.

  We want to test:
  $$
  H_0: \mu = 0, \ \ vs. \ \ H_1: \mu \neq 0
  $$
  Test statistic:
  $$
  T_n = {\overline{X}_n \over \sqrt{\tilde{S}_n/n}} = {\sqrt{n}{\overline{X_n} - \mu \over \sigma}  \over \sqrt{\tilde{S_n}/\sigma^2}} = {\sqrt{n}{\overline{X_n} \over \sigma}  \over \sqrt{\tilde{S_n}/\sigma^2}} \sim \mathcal{N}(0,1)
  $$
  Since $\overline{X}_n \sim \mathcal{N}(\mu, {\sigma^2 \over n})$​,
  $$
  { \overline{X}_n - \mu \over \sqrt{\widehat{\sigma^2}/n}} = {\sqrt{n}{\overline{X_n} - \mu \over \sigma}  \over \sqrt{\tilde{S_n}/\sigma^2}} \sim \mathcal{N}(0,1)
  $$
   $\sqrt{n} \overline{X}_n / \sigma \sim \mathcal{N}(0,1)$​​ (Under )  and $\tilde{S}_n/\sigma^2 \sim {\chi^2_{n-1}\over n-1}$​​​ are independent by **Cochran's Theorem**, we have
  $$
  T_n \sim t_{n-1}
  $$
  Student's test with (non-asymptotic) level $\alpha \in (0,1)$:
  $$
  \psi_\alpha = \mathbb{1} \{|T_n| > q_{\alpha/2}\}
  $$
  where $q_{\alpha/2}$ is the $(1-\alpha/2)$-quantile of $t_{n-1}$.

* One sample, one-sided:

  We want to test:
  $$
  H_0: \mu \leq \mu_0, \ \ vs. \ \ H_1: \mu > \mu_0
  $$
  Test statistic:
  $$
  T_n = {\overline{X}_n - \mu_0 \over \sqrt{\tilde{S}_n}} \sim t_{n-1}, \ \ \text{under } H_0
  $$
  Student's test with (non asymptotic) level $\alpha \in (0,1)$:
  $$
  \psi_\alpha = \mathbb{1}\{T_n > q_\alpha\}
  $$
  where $q_\alpha$​​ is the $(1-\alpha)$​​-quantile of $t_{n-1}$​​.

**Remark:**

For any fixed $n$, we may find the quantiles of the student's T distribution in tables. Since the distribution does not depend on the value of the true parameter, the test statistic $T_n$​ is indeed **pivotal**. Therefore, the test is **non-asymptotic**.

Assuming the data is Gaussian, the student's T test is useful in situations where the sample size is not very large, since the level may be precisely quantified even for small $n$.

> #### Exercise 80
>
> Consider the statistic
> $$
> T_{n} := \sqrt{n} \left( \frac{\overline{X}_ n - \mu }{\sqrt{\frac{1}{n- 1} \sum _{i = 1}^ n (X_ i - \overline{X}_ n)^2} } \right),
> $$
> where $\overline{X}_n$ is the sample mean of i.i.d Gaussian observations with mean $\mu$ and variance $\sigma^2$.
>
> 1. For all $n \geq 2$​​, is the distribution of $T_n$​​ a standard Gaussian $\mathcal{N}(0,1)$​​?
>
> 2. As $n \rightarrow \infty$, what does
>    $$
>    \frac{1}{n- 1} \sum _{i = 1}^ n (X_ i - \overline{X}_ n)^2
>    $$
>    converge to?
>
> 3. As $n \rightarrow \infty$​​​, what does the statistic $T_n$​​​ converges in distribution to?
>
> **Solution:**
>
> 1. No. The definition of the student's T distribution with $n-1$​​ degrees of freedom is that it is given by the distribution of $\frac{Z}{\sqrt{V/(n-1)}}$​​ where $Z \sim \mathcal{N}(0,1), V\sim \chi_{n-1}^2$​​ and $Z$​​ and $V$​ are​ independent. Since we are dividing by $V$​, a $\chi^2$​ random variable, then $T_n$​ will not have the same distribution as $\mathcal{N}(0,1)$ for all $n \geq 2$.
>
> 2. By the **LLN** and **Slutsky's lemma**,
>    $$
>    \frac{1}{n- 1} \sum _{i = 1}^ n (X_ i - \overline{X}_ n)^2 = \frac{n}{n-1} \left[\left(\frac{1}{n}\sum _{i = 1}^ n X_ i^2\right) - (\overline{X}_ n)^2\right] \to \sigma ^2
>    $$
>    in probability.
>
> 3. By the **CLT**, 
>    $$
>    \sqrt{n} \left( \frac{\overline{X}_ n - \mu }{\sigma } \right) \to \mathcal{N}(0,1).
>    $$
>    Hence, by the **LLN** and **Slutsky's lemma**,
>    $$
>    \sqrt{n} \left( \frac{\overline{X}_ n - \mu }{\sqrt{\frac{1}{n- 1} \sum _{i = 1}^ n (X_ i - \overline{X}_ n)^2} } \right) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0,1).
>    $$

## 9. Back to Clinical Trials: Two Sample T-Test and the Welch-Satterthwaite Formula

Two Sample T-Test:

* Back to our cholesterol example. What happens for small sample size?

* We want to know the distribution of 
  $$
  {\overline{X}_n - \overline{Y}_n - (\Delta_d - \Delta_c) \over \sqrt{{\widehat{\sigma_d}^2 \over n} + {\widehat{\sigma_c}^2 \over m}}}
  $$

* We have approximately
  $$
  {\overline{X}_n - \overline{Y}_n - (\Delta_d - \Delta_c) \over \sqrt{{\widehat{\sigma_d}^2 \over n} + {\widehat{\sigma_c}^2 \over m}}} \sim t_N
  $$
  where
  $$
  N = { \left(\widehat{\sigma_d^2}/n + \widehat{\sigma_c^2}/m\right)^2\over {\widehat{\sigma_d^4} \over n^2(n-1)} + {\widehat{\sigma_c^4}\over m^2(m-1) }} \geq \min(n,m)
  $$
  (Welch-Satterthwaite Formula)

Non-asymptotic test:

* Example $n=70, m=50, \bar{X}_n = 156.4, \bar{Y}_m = 132.7,\hat{\sigma}_d^2 = 5198.4, \hat{\sigma}_c^2 = 3867.0$.
  $$
  \frac{156.4 - 132.7}{\sqrt{\frac{5198.4 }{70} + \frac{3867}{50}}} \approx 1.9248.
  $$

* Using the shorthand formula $N = \min (n,m) = 50$, we get $q_{5\%} = 1.68$ and
  $$
  \text{p-value } = \mathbf{P}(t_{50} > 1.9248) = 0.0614
  $$

* Using the W-S formula
  $$
  N =  { ({5198.4 \over 70}+ {3867.0\over 50 })^2 \over {5198.4^2\over 70^2(70-1) } + {3867.0^2\over50^2(50-1) }} = 113.78 \approx 113
  $$

* We get
  $$
  \text{p-value }= \mathbf{P}(t_{113} > 1.9248) = 0.0596
  $$

