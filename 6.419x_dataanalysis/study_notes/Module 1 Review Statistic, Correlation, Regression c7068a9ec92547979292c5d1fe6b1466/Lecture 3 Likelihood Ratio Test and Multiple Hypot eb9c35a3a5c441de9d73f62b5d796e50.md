# Lecture 3: Likelihood Ratio Test and Multiple Hypothesis Testing

# **1. Likelihood ratio test**

The likelihood ratio test can be applied to a general setting with

- Hypotheses: $H_0$: $\theta \in \Theta _0$,  $H_ A: \theta \in \Theta _ A$, where $\Theta _0$ and $\Theta _ A$ are disjoint subsets ($\Theta _0 \cap \Theta _ A =\emptyset$) of a parameter space $\Theta =\Theta _0\cup \Theta _ A$.
- Parametric model with parameter $\theta$: The probability (or likelihood) of observing the data $x$ is $p(x;\theta )$.with the parameter \theta.

The likelihood ratio test statistic $\Lambda (x)$ is defined as (negative twice) the logarithm of the likelihood ratio $L(x)$:

$$
\displaystyle \displaystyle \Lambda (x)\displaystyle =\displaystyle -2\log (L(x)) \qquad \text {where } L(x)\, =\, \frac{\max _{\theta \in {\color{blue}{\Theta _0}} }p(x;\theta )}{\max _{\theta \in {\color{blue}{\Theta }} }p(x;\theta )}
$$

(Equivalently, in the language of maximum likelihood estimators, 

$$
\displaystyle \displaystyle L(x)\displaystyle =\displaystyle \frac{ p\left(x;\hat{\theta }_{\text {MLE}}^{\text {constrained}}\right)}{p\left(x;\hat{\theta }_{\text {MLE}}\right)}
$$

where  $\hat{\theta }_{\text {MLE}}$ is the maximum likelihood estimator of $\theta$ and $\hat{\theta }_{\text {MLE}}^{\text {constrained}}$ is the constrained maximum likelihood estimator of $\theta$ within $\Theta _0$.)

Use the definition of likelihood ratio L(x) and the likehood ratio test statistic $\Lambda (x)$ above.

We expect the null hypothesis to **not** be true if

If the likelihood ratio L(x) is small, then there is a parameter \theta in \Theta _ A such that p(x;\theta ) is big, i.e. that makes seeing the data much more likely. Hence, we should reject H_0 in this case.

# **2. The Distribution of Likelihood Ratio test statistics**

**Wilk's Theorem** states that when the sample size is large, the distribution of \Lambda under H_{0} approaches a \chi ^2distribution:

|  | \displaystyle \displaystyle \Lambda \overset {n\to \infty }{\longrightarrow } \chi _ d^2 \qquad \text {where } d = \text {dim}(\Theta ) - \text {dim}(\Theta _0) |  |  |
| --- | --- | --- | --- |

where d is the degree of freedom of the \chi ^2 distribution.

**Power of Likelihood Ratio Test**

The **Neyman–Pearson lemma** states that among all tests that test for the simple hypotheses H_0: \theta =\theta _0\, ;\, H_ A:\theta =\theta _ A at significance level \alpha, the likelihood ratio test is the most powerful. That is, among all tests testing the same simple hypotheses and at the same significance level, the likelihood ratio test gives the largest probability of rejecting the null when indeed the alternate is true.

The likelihood ratio (LR) test statistic \(\Lambda(x)\) is used to test hypotheses about the parameter \(\theta\). The LR-test statistic is given by:

\[ \Lambda(x) = -2 \log \left( \frac{\text{likelihood under } H_0}{\text{likelihood under } H_A} \right) \]

### Asymptotic Distribution of the LR-test Statistic

When the sample size is large, the distribution of the LR-test statistic \(\Lambda(x)\) approaches a \(\chi^2\) (chi-squared) distribution. This result is a consequence of Wilks' theorem, which states that the LR-test statistic is asymptotically chi-squared under the null hypothesis.

### Degrees of Freedom

The degrees of freedom \(d\) for the chi-squared distribution in the context of the LR-test statistic depends on the number of parameters being tested. Specifically, it is equal to the difference in the number of parameters between the null hypothesis and the alternative hypothesis. For the hypotheses:

\[ H_0: \theta = \theta_0 \]
\[ H_A: \theta \neq \theta_0 \]

we are testing a single parameter \(\theta\). Hence, the degrees of freedom \(d\) is 1.

### Summary

1. The approximate distribution of the LR-test statistic \(\Lambda(x)\) when the sample size is large is a **\(\chi^2\)-distribution**.
2. The degrees of freedom \(d\) of this distribution is **1**.

### Answer

1. The approximate distribution of the LR-test statistic \(\Lambda(x)\) when the sample size is large:
    - \(\chi^2\)-distribution
2. The degrees of freedom \(d\) of the distribution:
    - \(d = 1\)

# **3. Likelihood Ratio Test on the Mammography Study**

In the following problems, we apply the likelihood ratio test to the mammography study to answer the question whether the treatment changes the death rate. The corresponding hypotheses in terms of the breast cancer death rates, \pi _ T in the treatment group and \pi _ C in the control group, are

|  | \displaystyle \displaystyle H_0 | \displaystyle : | \displaystyle \pi _ T=\pi _ C |  |  |
| --- | --- | --- | --- | --- | --- |
|  | \displaystyle H_ A | \displaystyle : | \displaystyle \pi _ T\neq \pi _ C. |  |  |