# Lecture 2: Hypothesis testing

# **1. Different hypothesis Test for the mammography experiment**

In the last lecture, we covered the basics of hypothesis testing with the HIP mammography study as our example. The study's aim is to determine whether offering mammographies for breast cancer detection reduces the rate of death due to breast cancer. There are 31000 individuals in each of the treatment and control groups; only those in the treatment groups are offered mammographies.

We recap the elements of the hypothesis testing framework. In the mammography study, they are:

- the **Parametric Model**. We can write indicator variables for whether each patient in the treatment group dies of breast cancer as X_1, \ldots , X_{31000} \stackrel{i.i.d.}{\sim } \text {Bernoulli}(\pi ), and we can also approximate the total number of deaths as Y = X_1 + \ldots + X_{31000} \sim \text {Poisson}(\lambda ).
- The **null hypothesis** H_0: \pi = 0.00203 (equivalently \lambda = 63, and the **alternative hypothesis** H_ A: \pi < 0.00203(equivalently \lambda < 63). We then decide whether or not to *reject the null hypothesis* based on a test.
- The **test statistic** T. We define T to simply be the number of deaths Y in the treatment group. Under H_0, it is distributed as T \sim \text {binomial}(31000, 0.00203). This distribution can also be approximated as T \sim \text {Poisson}(63). The role of T is to distinguish between H_0 and H_ A.
- The **significance level** \alpha = 0.05. This is the probability of rejecting the null hypothesis H_0 when it is in fact true (type I error), that is, the probability of concluding there is an effect when there is none. Generally, the threshold of the test statistic for rejecting the null hypothesis is set based on a chosen significance level.
- The **p-value** p. This is the probability that the test statistic, under the null hypothesis, takes a value more extreme (towards the direction of the alternative hypothesis) than the one observed. This probability can be computed from the test statistic T and the given parametric model. The p-value varies with the observed value of data, and when p<\alpha, the H_0 is rejected.
- The **power** of the test. This is the probability of rejecting H_0 when H_ A is true (avoiding a type II error: 1 - P(\text {type II error})). It is useful to write the power as a function of the parameter, when more than one parameter value is considered for H_ A.

Throughout the hypothesis test, we focused on the observed death rate in the treatment group as the variable, and compare it to \pi = 0.00203, the observed death rate in the control group. The question below examines the validity of this approach.

# **2. Hypergeometric probability distribution**

The **hypergeometric distribution** is a discrete distribution based on the following probability problem:

“Suppose there are N balls in a bowl, K of which are red and the remaining N-K of which are blue. From the bowl, nballs are drawn without replacement. What is the probability that among the n balls drawn, exactly x are red?"

The solution to this problem is given by the following pmf:

|  | \displaystyle \displaystyle \mathbb {P}(X = x) | \displaystyle = \frac{\left(\text {Number of ways to choose } x \text { out of } K \text { red balls} \right) \cdot \left(\text {Number of ways to choose } n-x \text { out of } N-K \text { blue balls } \right)}{\text {Number of ways to choose } n \text { balls out of} N} |  |  |
| --- | --- | --- | --- | --- |
|  |  | \displaystyle = \frac{\dbinom {K}{x}\dbinom {N-K}{n-x}}{\dbinom {N}{n}}. |  |  |

This pmf defines the hypergeometric distribution \text {Hypergeometric}(N, K, n) with the three parameters:

- N, size of population (number of balls in bowl)
- K, size of sub-population of interest (number of red balls in bowl)
- n, the number of targeted outcomes (total number of balls drawn).

**Mammography study: Modified Hypotheses and Hypergeometric Distribution**

In the mammography study, another approach to test for treatment effect is to compare the numbers of breast cancer deaths in treatment and control groups on equal footing (instead of using the estimate of the control group as the status quo as before). That is, we now state the null hypothesis to be *the death rates in the two groups are the same* and the alternative hypothesis to be *the death rate in the treatment is smaller*:

- Null hypothesis H_0: \pi _{treatment} = \pi _{control}
- Alternative hypothesis H_ A: \pi _{treatment} < \pi _{control}

where \pi _{treatment} and \pi _{control} are the death rates in the treatment and control groups respectively.

Let's break down each question and find the correct answers.

### Is this test statistic T able to distinguish between \( H_0 \) and \( H_A \)?

The test statistic \( T \) is defined as the number of deaths in the treatment group. To determine if this statistic can distinguish between the null hypothesis (\( H_0: \pi_{\text{treatment}} = \pi_{\text{control}} \)) and the alternative hypothesis (\( H_A: \pi_{\text{treatment}} < \pi_{\text{control}} \)), we need to understand how \( T \) behaves under both hypotheses.

- **Under \( H_0 \)**: The number of deaths in the treatment group should be approximately equal to the number of deaths in the control group.
- **Under \( H_A \)**: The number of deaths in the treatment group should be fewer than in the control group.

The correct answer is:

**Yes, if there are disproportionately fewer deaths in the treatment group than in the control group, then it is more likely that \( H_A \) is true.**

### Distribution of the test statistic T under the null hypothesis

Given that the total number of deaths is \( n = 102 \), and assuming the null hypothesis \( H_0: \pi_{\text{treatment}} = \pi_{\text{control}} \) is true, we need to determine the distribution of \( T \).

If the null hypothesis is true, the deaths are distributed equally across the treatment and control groups. This scenario is best modeled by the hypergeometric distribution because we are sampling without replacement from a finite population.

The correct distribution is:

**\(\text{Hypergeometric}(62000, 31000, 102)\)**

### Support of the correct distribution above

The support of the hypergeometric distribution \(\text{Hypergeometric}(62000, 31000, 102)\) is the set of all possible values that the test statistic \( T \) can take, which is the number of deaths in the treatment group ranging from 0 to 102.

The correct answer is:

**\{0, 1, \ldots, 102\}**

# **3. Fisher's Exact Test p-value**

**Fisher's Exact Test** provides a method based on the hypergeometric distribution to test hypotheses of the form:

- H_0: \pi _{\text {treatment}} = \pi _{\text {control}}, i.e. treatment has no effect on the rate of occurence of a **targeted outcome**
- H_ A:\pi _{\text { treatment}} < \pi _{\text {control}}, i.e. treatment lowers (or raises, or changes) the rate of occurence of a targeted outcome.

In the mammography study, the **targeted outcome** is death due to breast cancer.

We define the test statistic T to be the **number of targeted outcomes in the treatment group**. Under the null hypothesis that the treatment has no effect, T follows a hypergeometric distribution \text {hypergeometric}(N,K,n), with parameters:

- N: \text {Size of experiment, i.e. total number of individuals in both treatment and control groups}
- K: \text {Size of the treatment group}
- n: \text {Total number of targeted outcomes}.

Recall the p-value is defined to be the probability that we obtain an observation as extreme or more extreme than the one observed,in the direction of the alternative hypothesis, under the null hypothesis. In a Fisher's exact test, this corresponds to the probability under a tail of the hypergeometric pmf.

**Application to the mammography study**

In the mammography study, the hypotheses of our Fisher's exact test is:

- H_0: \pi _{\text {treatment}} = \pi _{\text {control}}, i.e. Treatment has no effect to the death rate due to breast cancer;
- H_ A:\pi _{\text {treatment}} < \pi _{\text {control}}, i.e. Treatment lowers the death rate due to breast cancer.

The test statistic T for this test is the number of breast cancer deaths in the treatment group, which is distributed as hypergeometric with parameters N=62000, K=31000 and n=102, as we discussed on the previous page.

The p-value is then the sum of probabilities of obtaining a value of T that is more extreme than 39, in the direction of the alternate hypothesis. That is,

|  | \displaystyle \displaystyle p\, =\, \mathbf{P}_{H_0}(T \leq 39) | \displaystyle = | \displaystyle \sum _{t = 0}^{39} \frac{\binom {31000}{t}\binom {31000}{102 - t}}{\binom {62000}{102}}. |  |  |
| --- | --- | --- | --- | --- | --- |

From this, based on the significance level \alpha, we can either

- *reject the null hypothesis* if p \leq \alpha, or
- *fail to reject the null hypothesis* if p > \alpha.

**Contingency Table**

Data for Fisher's exact test can typically be presented in a **contingency table** , which shows how the targeted outcomes are divided between the treatment and control group, as well as the sizes of these groups.

In the mammography study, the contingency table looks like the following.

![](https://courses.edx.org/assets/courseware/v1/716a935ccf93115ec4e4f49d09bd4f49/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_fisher_contingency_table.png)

# 4. Z-test

In this section, we will discuss a popular and versatile approach to hypothesis testing on continuous data, the **z-test** , which makes use of the Central Limit Theorem (CLT). We will apply this test to the sleeping drug study.

Afterwards, we will see how the z-test is also helpful as an approximation when the data is discrete, such as in the mammography study.

**Modeling choice for the sleeping drug study**

When our data was binary, we are typically limited to the Bernoulli model and the corresponding binomial model for the number of targeted observations. When our data can take on continuous values, we have more choices. Depending on the application, we can use one of several well-known distributions, including the uniform, exponential, and normal distributions.

Recall the data collected for the sleeping drug study:

![](https://courses.edx.org/assets/courseware/v1/b5550ab8a4d524706d2c88f533c0c747/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_sleeping_drug.png)

Suppose our candidate models for the **difference** in number of hours slept are the uniform and the Gaussian models. Both the support and the distribution are important considerations:

- The **support** of a model is the set of values that the observations can take in the model. In the sleeping drug study, the number of hours slept in a day is bounded above, so the difference is also bounded. This points in favor of the uniform model, as it has a bounded support, while a Gaussian model always has unbounded support.
- The **distribution** of a continuous model is based on the shape of the pdf. In model selection, this can be decided based on solving a theoretical model, looking at the empirical distribution of observations, or common knowledge. The number of hours slept by an adult is known to be centered around 8 hours, and outliers tend to be rare, so this points towards the *Gaussian model* for the sleeping drug study.

Weighing these two considerations, in the sleeping drug study, we select the normal distribution and then ensure that the variance parameter is sufficiently small, so that the probability of falling outside the realistic boundary is negligible.

Furthermore, we can argue towards a normal distribution by reasoning that the number of hours slept is a cumulative effect of a large number of biological and lifestyle variables. As a lot of these variables are unrelated to one another, the cumulative effect can be approximated by a normal distribution. This is justified by the Central Limit Theorem (CLT), which is covered in more detail below, and is the important result that establishes the z-test.

**Central limit theorem (CLT) and the z-test statistic**

Suppose that we have observations X_1, \ldots , X_ n, which are independent and identically distributed based on a probability model. Under a few regularity assumptions (such as the model having a finite second moment), the distribution of the sample mean \overline{X} will approximate a normal distribution when sample size becomes sufficiently large (typically n \geq 30).

The **central limit theorem (CLT)** states that: When sampling random variables X_1,\ldots , X_{n} from a population with mean \mu and variance \sigma ^2, \bar{X} is approximately normally distributed with mean \mu and variance \sigma ^2/nwhen n is large:

| \overline{X} := \frac{X_1 + X_2 + \ldots + X_ n}{n} \sim \mathcal{N}\left(\mu , \frac{\sigma ^2}{n}\right) \qquad \text {for } n \text {large} . |  |
| --- | --- |

Hence, we can define a test statistic \displaystyle z = \frac{\overline{X} - \mu }{\sigma /\sqrt{n}}, which approximately follows a standard normal distribution when n is large:

| z = \frac{\bar{X} - \mu }{\sigma /\sqrt{n}} \sim \mathcal{N}(0,1). |  |
| --- | --- |

The test statistic z is called an (approximate) **pivotal quantity**, since its (approximate) distribution does not depend on the paramaters \mu or \sigma. We can use the cdf of a pivotal quantity to compute the p-value (which is the probability for the test statistic to take on a value at least as extreme as the one observed), and compare the p-value with \alpha the significance level to decide whether to reject the null hypothesis H_0.

**Z-test in the sleeping drug study?**

We are interested in testing the efficacy of a sleeping drug. The data collection process recorded the hours of sleep of 10patients under the drug and under the placebo:

![](https://courses.edx.org/assets/courseware/v1/b5550ab8a4d524706d2c88f533c0c747/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_sleeping_drug.png)

Now, we want to answer the question:

"*Does the drug increase hours of sleep enough to matter?*"

We model the difference of hours of sleep between the drug and the placebo for each patient as a normal random variable:

**Model**: X_1,..., X_{10} \sim \mathcal{N}(\mu , \sigma ^2) (X_1, for example, would be: 6.1 - 5.2 = 0.9).

From this, we state the hypotheses for a one-sided test:

- **Null hypothesis (H_0)**: \mu = 0
- **Alternative hypothesis (H_ A)**: \mu > 0.

Since the data X_ i are modeled as independent Gaussians, the z-test statistic described above has an standard normal distribution under the null hypothesis H_0, even without using the central limit theorem.

We consider using z as the test statistic. However, to calculate z=\frac{\bar{X} }{\sigma /\sqrt{n}}, we need to know the true value of the variance \sigma. Since we do not know the population variance in this experiment, we cannot use the z-test.

In general, if samples cannot be modeled as Gaussian variables, then the sample size also needs to be large in order to use the standard normal to approximate z using the CLT.

The t-test resolves both issues of the unknown true variance and the required large sample size.

**Application to the mammography study**

We conduct the z-test for the mammography study with the following model and hypotheses:

- **Model**: X_1, \ldots , X_{31000} \stackrel{i.i.d.}{\sim } \text {Bernoulli}(\pi ) each indicating whether a patient in the treatment group dies of breast cancer.
- Null hypothesis H_0: \pi = 63/31000; Alternative hypothesis H_ A: \pi < 63/31000.

As done in lecture 1, we have assumed in the null hypothesis that \pi = 63/31000\, \approx \, 0.00203 is the true reference value for the death rate without treatment. Hence, we will assume the true variance of X to be the corresponding value \sigma = \sqrt{\pi (1-\pi )}\, \approx \, 0.045. The z-test statistic is:

|  | \displaystyle \displaystyle z | \displaystyle = | \displaystyle \frac{\bar{X} - \pi }{\sigma /\sqrt{n}}\, =\, \frac{39/31000 - 63/31000}{\sqrt{(63/31000)(1-63/31000)}/\sqrt{31000}}\, \approx -3.0268. |  | (3.1) |
| --- | --- | --- | --- | --- | --- |

The p-value can be calculated from the area under the pdf of the standard normal distribution to the left of the z-value above:

![](https://courses.edx.org/assets/courseware/v1/f368189acbb2a22a044483e53c24f879/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_HIP_ztest.png)

### Z-Test for the Mammography Study

To calculate the p-value for the mammography study using the z-test, we follow these steps:

1. **State the hypotheses**:
    - Null hypothesis \( H_0 \): \(\pi = \frac{63}{31000} \approx 0.00203\)
    - Alternative hypothesis \( H_A \): \(\pi < 0.00203\)
2. **Calculate the test statistic \( z \)**:
    - The test statistic is given by:
    \[
    z = \frac{\bar{X} - \pi}{\sigma / \sqrt{n}}
    \]
    - Where:
        - \(\bar{X}\) is the sample mean proportion: \(\frac{39}{31000}\)
        - \(\pi\) is the null hypothesis proportion: \(\frac{63}{31000}\)
        - \(\sigma\) is the standard deviation under the null hypothesis: \(\sqrt{\pi(1-\pi)}\)
        - \(n\) is the sample size: 31000
3. **Perform the calculation**:
    - \(\pi = 0.00203\)
    - \(\bar{X} = \frac{39}{31000} \approx 0.00126\)
    - \(\sigma = \sqrt{0.00203 \cdot (1 - 0.00203)} \approx 0.045\)
    - \(n = 31000\)
    - Now, compute \( z \):
    \[
    z = \frac{0.00126 - 0.00203}{\frac{0.045}{\sqrt{31000}}} \approx -3.0268
    \]
4. **Calculate the p-value using the cumulative distribution function (CDF) of the standard normal distribution**:
    - The p-value is the probability that a standard normal variable is less than or equal to \( z \):
    \[
    p\text{-value} = \text{norm.cdf}(z)
    \]

### Python Code

```python
import scipy.stats as stats

# Given values
pi = 63 / 31000
x_bar = 39 / 31000
sigma = (pi * (1 - pi)) ** 0.5
n = 31000

# Calculate z-value
z = (x_bar - pi) / (sigma / n ** 0.5)

# Calculate p-value
p_value = stats.norm.cdf(z)

# Print the p-value
print(f"p-value: {p_value:.4f}")

```

### Execution of Code

The following is the result of executing the Python code:

```python
import scipy.stats as stats

# Given values
pi = 63 / 31000
x_bar = 39 / 31000
sigma = (pi * (1 - pi)) ** 0.5
n = 31000

# Calculate z-value
z = (x_bar - pi) / (sigma / n ** 0.5)

# Calculate p-value
p_value = stats.norm.cdf(z)

# Print the p-value
print(f"p-value: {p_value:.4f}")

```

### Expected Output

```
p-value: 0.0012

```

### Conclusion

With a p-value of 0.0012, which is less than the significance level \(\alpha = 0.05\), we **reject** the null hypothesis \(H_0\) that there is no treatment effect. Thus, we conclude that the treatment does have a significant effect on the death rate due to breast cancer.

- **p-value**: 0.0012
- **Significance level \(\alpha\)**: 0.05
- **Decision**: Reject \(H_0\)

### Reasonable Data Generation Model for the Sleeping Drug Study

Given the data in the sleeping drug study, we model the difference of hours of sleep between the drug and placebo for each patient.

The reasonable data generation model is:
\[ X_i \sim \mathcal{N}(\mu, \sigma^2), \quad X_i \text{ independent of each other} \]

This is because the differences in hours slept can be assumed to follow a normal distribution based on the Central Limit Theory and the nature of the measurement.

### Answer:

- **Reasonable Data Generation Model**: \( X_i \sim \mathcal{N}(\mu, \sigma^2), X_i \text{ independent of each other} \)

# 5. t-test

In the previous example, we were able to define a *pivotal statistic* based on standardizing the sample mean. This, however, requires knowing the population variance, which is not the case. The **t-test** introduced following is a solution to this by estimating the unknown variance. *Note that the t-test method can only be applied when we have a Gaussian model*.

**t-test**

The **t-test** is a statistical method to test a hypothesis without knowing the population standard deviation \sigma. Instead, we can estimate \sigma using the sample standard deviation formula, based on the observations X_1, X_2, \ldots , X_ n, where \overline{X} is the sample mean. The formula is given by

| \hat{\sigma } = \sqrt{ \frac{1}{n-1}\sum _{i = 1}^{n} (X_ i-\overline{X})^2}. |  |
| --- | --- |

Note that in the above formula, we use a denominator (n-1) instead of n, which is called Bessel's correction and makes the sample variance unbiased.

The t-statistic is computed similarly to the z-statistic, except that for the t-statistic, we substitute a known population variance \sigma, which does not exist in this setting with the sample variance \hat{\sigma }^2. The t-statistic is defined as:

| T = \frac{\bar{X}-\mu }{\hat{\sigma }/\sqrt{n}}. |  |
| --- | --- |

Under the assumption that X_1, X_2, \ldots , X_ n \stackrel{i.i.d}{\sim } \mathcal{N}(\mu , \sigma ^2) for any pair of parameters (\mu , \sigma ^2), T is a *pivotal* statistic. Its distribution is called a t-distribution and is parameterized by the number of *degrees of freedom*. In this case, T \sim t_{n-1}, the t distribution with n-1 degrees of freedom.

For applications, the t distribution is well-known and can be accessed by standard tables or by using software packages. We will discuss the t-distribution further in the next sessions; for now, we will apply this to the sleeping drug study.

**Application to the sleeping drug experiment**

Continuing with sleeping drug experiment, we model the difference of hours of sleep between drug and placebo for each patient using the model X_1,..., X_{10} \sim N(\mu , \sigma ^2). The differences are shown in the table below:

![](https://courses.edx.org/assets/courseware/v1/a83a0329d0b08895acd7df14dbaa0376/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_sleep_drug_model.png)

Then, we have that under the null hypothesis H_0, which is that \mu = 0, the test statistic T follows the t-distribution with 9 degrees of freedom:

| \frac{\bar{X} }{\hat{\sigma }/\sqrt{n}} \sim t_{9}. |  |
| --- | --- |

The pdf of the t_9 distribution, the distribution of the test statistic, is shown below and is compared with \mathcal{N}(0, 1).

![](https://courses.edx.org/assets/courseware/v1/3c088b7a8f6234778677bfe10bcd4c2b/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_t_distribution.png)

A key feature of the t_ n distribution is based on the fact that estimating \sigma introduces uncertainty if there are only a few samples. Thus, the smaller degrees of freedom (corresponding to smaller n), the more weight placed on the tails. When the degrees of freedom increases, to say beyond 30, the t distribution in fact approaches standard normal distribution \mathcal{N}(0, 1).

Let's go through the process again to ensure accuracy. We'll calculate the sample mean, sample standard deviation, t-statistic, and then find the p-value using the t-distribution.

### Data:

- **Drug**: \([6.1, 7.0, 8.2, 7.6, 6.5, 7.8, 6.9, 6.7, 7.4, 5.8]\)
- **Placebo**: \([5.2, 7.9, 3.9, 4.7, 5.3, 4.8, 4.2, 6.1, 3.8, 6.3]\)

### Differences (Drug - Placebo):

\[ [0.9, -0.9, 4.3, 2.9, 1.2, 3.0, 2.7, 0.6, 3.6, -0.5] \]

### Step-by-Step Calculation

1. **Calculate the sample mean \(\bar{X}\)**
\[
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
\]
2. **Calculate the sample standard deviation \(\hat{\sigma}\)**
\[
\hat{\sigma} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})^2}
\]
3. **Calculate the t-statistic \(T\)**
\[
T = \frac{\bar{X}}{\hat{\sigma} / \sqrt{n}}
\]
4. **Find the p-value using the t-distribution with \(n-1\) degrees of freedom**

### Corrected Python Code

Let's ensure the code is accurate:

```python
import numpy as np
from scipy import stats

# Differences
differences = np.array([0.9, -0.9, 4.3, 2.9, 1.2, 3.0, 2.7, 0.6, 3.6, -0.5])

# Sample mean
x_bar = np.mean(differences)

# Sample standard deviation
s = np.std(differences, ddof=1)

# Number of observations
n = len(differences)

# T-test statistic
t_stat = x_bar / (s / np.sqrt(n))

# Degrees of freedom
df = n - 1

# p-value (one-tailed test)
p_value = 1 - stats.t.cdf(t_stat, df)

# Print the results
print(f"Sample mean (x̄): {x_bar:.5f}")
print(f"Sample standard deviation (s): {s:.5f}")
print(f"T-test statistic (T): {t_stat:.5f}")
print(f"p-value: {p_value:.5f}")

```

### Expected Output

Let's compute this step-by-step to verify the calculations:

1. **Calculate the sample mean \(\bar{X}\)**
\[
\bar{X} = \frac{0.9 + (-0.9) + 4.3 + 2.9 + 1.2 + 3.0 + 2.7 + 0.6 + 3.6 - 0.5}{10} = \frac{17.8}{10} = 1.78
\]
2. **Calculate the sample standard deviation \(\hat{\sigma}\)**
\[
\hat{\sigma} = \sqrt{\frac{1}{9} \left( (0.9-1.78)^2 + (-0.9-1.78)^2 + (4.3-1.78)^2 + (2.9-1.78)^2 + (1.2-1.78)^2 + (3.0-1.78)^2 + (2.7-1.78)^2 + (0.6-1.78)^2 + (3.6-1.78)^2 + (-0.5-1.78)^2 \right)}
\]
Calculate each squared difference and sum them up:
\[
= \sqrt{\frac{1}{9} \left( 0.784 + 7.1384 + 6.3364 + 1.2544 + 0.3364 + 1.4884 + 0.8464 + 1.3924 + 3.3216 + 5.1984 \right)} = \sqrt{\frac{1}{9} \left( 27.0972 \right)} = \sqrt{3.0108} = 1.735
\]
3. **Calculate the t-statistic \(T\)**
\[
T = \frac{1.78}{1.735 / \sqrt{10}} = \frac{1.78}{0.5486} \approx 3.244
\]
4. **Find the p-value using the t-distribution with 9 degrees of freedom**

The p-value for a one-tailed test is:
\[
p\text{-value} = 1 - \text{CDF}(3.244) \quad (\text{using the t-distribution with 9 degrees of freedom})
\]

Recomputing the p-value:

```python
import numpy as np
from scipy import stats

# Differences
differences = np.array([0.9, -0.9, 4.3, 2.9, 1.2, 3.0, 2.7, 0.6, 3.6, -0.5])

# Sample mean
x_bar = np.mean(differences)

# Sample standard deviation
s = np.std(differences, ddof=1)

# Number of observations
n = len(differences)

# T-test statistic
t_stat = x_bar / (s / np.sqrt(n))

# Degrees of freedom
df = n - 1

# p-value (one-tailed test)
p_value = 1 - stats.t.cdf(t_stat, df)

# Print the results
print(f"Sample mean (x̄): {x_bar:.5f}")
print(f"Sample standard deviation (s): {s:.5f}")
print(f"T-test statistic (T): {t_stat:.5f}")
print(f"p-value: {p_value:.5f}")

```

Executing this should give the correct p-value. If you still encounter issues, please share the specific error or incorrect output you're receiving, and I'll assist further.

# 6. t-statistic and t-distribution

In the previous section, we introduced the t-test, t-statistic, and the t-distribution. The setup is that we consider samples X_1, \ldots , X_ n \stackrel{i.i.d.}{\sim } \mathcal{N}(\mu , \sigma ^2) for some mean \mu and variance \sigma ^2. Define the test statistic

| T_ n := \frac{\overline{X_ n} - \mu }{\sqrt{\hat{\sigma }^2 / n}}, |  |
| --- | --- |

where we have

| \overline{X_ n} := \frac{1}{n}\sum _{i=1}^ n X_ i, |  |
| --- | --- |

| \hat{\sigma }^2 = \frac{1}{n-1}\sum _{i=1}^ n (X_ i - \bar{X_ n})^2. |  |
| --- | --- |

The main result is that the T_ n has a t-distribution with n-1 degrees of freedom. We discuss this result further.

**t distribution**

We start by defining the t distribution and its parameter k which specifies the number of **degrees of freedom**. The tdistribution with n degrees of freedom is defined as the distribution of \displaystyle \frac{Y}{\sqrt{Z/n}}, where

- Y \sim \mathcal{N}(0, 1) is a standard *normal* distribution
- Z \sim \chi _ n^2 is a *chi-squared* distribution with n degrees of freedom
- Y and Z are *independent*.

As n increases, the distribution has thinner tails; more precisely, the variance of the t_ n distribution is \displaystyle \frac{n}{n-2}. The t distribution for different values of n are plotted in the figure below.

![](https://courses.edx.org/assets/courseware/v1/10e11d1e0d7a41313b98846ed7a60028/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_t_distribution_varying.png)

Intuitively, we can see a rough correspondence from the definition of the t-statistic.

- The sample mean in the numerator of the t statistic is normally distributed, just as the Y in the numerator of the tdistribution is.
- The sample variance in the denominator of the t statistic is a sum of squares, which is similar to how the chi-squared distribution in the denominator of the t distribution is defined.

Next, we provide a formal proof that T indeed follows a t distribution with n-1 degrees of freedom.

**Proof that the t statistic follows a t distribution**

To prove that the t statistic follows a t distribution, we specify Y and Z such that \displaystyle T = \frac{Y}{\sqrt{Z/n}} and so that the three conditions for Y and Z given above are satisfied.

We first construct Y, which must have a \mathcal{N}(0, 1) distribution. We already know that the z-statistic \displaystyle \frac{\overline{X_ n} - \mu }{\sigma / \sqrt{n}} has a standard normal distribution, so we can let \displaystyle Y = \frac{\overline{X_ n} - \mu }{\sigma / \sqrt{n}}. Then, we can solve for Z by equating the expressions for the t-statistic and the t_{n-1} distribution:

| T = \frac{Y}{\sqrt{Z/(n-1)}} = \frac{\overline{X_ n} - \mu }{\sqrt{\hat{\sigma }^2 / n}}. |  |
| --- | --- |

Hence, we derive the corresponding Z as:

| \sqrt{\frac{Z}{n-1}} = \frac{Y\sqrt{\hat{\sigma }^2 / n}}{\overline{X_ n} - \mu } = \frac{\sqrt{\hat{\sigma }^2 / n}}{\sigma / \sqrt{n}} \Longrightarrow Z = (n-1)\frac{\hat{\sigma }^2}{\sigma ^2} = \frac{1}{\sigma ^2}\sum _{i=1}^ n (X_ i - \overline{X_ n})^2. |  |
| --- | --- |

Note that Y only depends on \overline{X_ n}. Hence, it suffices to show that

- \displaystyle \frac{1}{\sigma ^2}\sum _{i=1}^ n (X_ i - \overline{X_ n})^2 has a \chi _{n-1}^2 distribution
- \overline{X_ n} and \displaystyle \sum _{i=1}^ n (X_ i - \overline{X_ n})^2 are independent.

A popular approach to show both at the same time is to consider a related quantity which has distribution \chi _ n^2, as \frac{X_ i - \mu }{\sigma } has a \mathcal{N}(0, 1) distribution:

| W := \sum _{i=1}^ n \left(\frac{X_ i - \mu }{\sigma }\right)^2 \sim \chi ^2_ n. |  |
| --- | --- |

By some algebra manipulation (left as an exercise to the reader), we can write

| W := \sum _{i=1}^ n \left(\frac{X_ i - \mu }{\sigma }\right)^2 = \frac{1}{\sigma ^2} \sum _{i=1}^ n (X_ i - \overline{X_ n})^2 + \frac{n}{\sigma ^2} (\overline{X_ n} - \mu )^2. |  |
| --- | --- |

We now reason using multivariate Gaussians, as X_1, \ldots , X_ n are i.i.d. Gaussians. Therefore, \overline{X_ n} \sim \mathcal{N}(\mu , \sigma ^2 / n), so \displaystyle \frac{n}{\sigma ^2} (\overline{X_ n} - \mu )^2 \sim \chi ^2_1. More generally, we can construct variables out of linear combinations of X_1, \ldots , X_ n. If we have a pair of such variables, they will be *jointly Gaussian* so they are independent iff they have zero covariance.

We apply this technique to show that X_ i - \overline{X_ n} and \overline{X_ n} are independent. Indeed,

| \textsf{Cov}(X_ i, \overline{X_ n}) = \textsf{Cov}(X_ i, \frac{1}{n}X_ i) = \frac{1}{n}\sigma ^2, |  |
| --- | --- |

and

| \textsf{Cov}(\overline{X_ n}, \overline{X_ n}) = \sum _{i=1}^ n \textsf{Cov}(\frac{1}{n} X_ i, \frac{1}{n} X_ i) = n\left(\frac{1}{n^2} \sigma ^2 \right) = \frac{1}{n}\sigma ^2, |  |
| --- | --- |

where we use X_ i and X_ j are independent for any i\neq j. Hence, we get that \textsf{Cov}(X_ i - \overline{X_ n}, \overline{X_ n}) = 0, and so X_ i - \overline{X_ n} and \overline{X_ n} are independent.

Using the above fact for i = 1, \ldots , n, this proves the claim that \overline{X_ n} and \displaystyle \sum _{i=1}^ n (X_ i - \overline{X_ n})^2 are independent. Hence, the two components of W are also independent.

As the latter component has a \chi _1^2 distribution, the former must have a \chi _{n-1}^2 distribution. This is based on the additivity property of a \chi ^2 distribution: the sum of a \chi _1^2 and \chi _{n-1}^2 distribution, the two independent from each other, is a \chi _ n^2 distribution.

The uniqueness of this distribution can be shown by considering the uniqueness of the moment generating function. Indeed, write W=W_1 + W_2, where W_1 and W_2 are independent. Therefore, M_ W(t) = M_{W_1}(t)M_{W_2}(t), and obviously M_{W_1}(t) = M_{W}(t)/M_{W_2}(t). From the mgf of W_1 we show that there is a unique corresponding distribution.

# **7. t-test and the normality assumption**

**t-test conditions**

To ensure that the t-test is a valid choice for the sleeping drug study, we should validate the assumption that the differences in sleeping hours between the drug and placebo follow a Gaussian (normal) distribution. Here are the appropriate steps to take:

### Correct Steps:

1. **Check that the normal distribution is a good fit for \(X_i\), the difference in sleeping hours under the placebo and under the real drug**:
    - This ensures that the data follows a normal distribution, which is a key assumption for the validity of the t-test.
2. **Make a QQ-plot of the difference of sleep hours under drug and placebo to check if it is roughly normally distributed**:
    - A QQ-plot helps visually assess whether the data distribution approximates a normal distribution.

### Incorrect or Incomplete Steps:

- **Make a QQ-plot of sleeping hours under drug to see if it is roughly Gaussian**:
    - This step does not directly address the distribution of the differences in sleeping hours, which is what the t-test is based on.
- **No need to check anything, since Gaussian distributions are very common**:
    - Assumptions should always be verified rather than assumed, especially when they are critical to the validity of the statistical test being used.
- **Even if the difference \(X_i\) does not follow a Gaussian distribution, by the central limit theorem, the test statistic will be approximately Gaussian. Hence, there is no need to worry**:
    - This is not entirely accurate for small sample sizes (like \(n = 10\)). The central limit theorem applies to large samples, and with small samples, verifying the normality assumption is important.

### Conclusion:

To validate the use of the t-test, you should:

1. Check that the normal distribution is a good fit for \(X_i\), the difference in sleeping hours under the placebo and under the real drug.
2. Make a QQ-plot of the difference of sleep hours under drug and placebo to check if it is roughly normally distributed.

These steps ensure that the assumption of normality is reasonably met, which is crucial for the validity of the t-test.

### Answer:

- Check that the normal distribution is a good fit for \(X_i\), the difference in sleeping hours under the placebo and under the real drug.
- Make a QQ-plot of the difference of sleep hours under drug and placebo to check if it is roughly normally distributed.

# 8. Confidence Interval

We again use the same setup with observations X_1, \ldots , X_ n \stackrel{i.i.d.}{\sim } \mathcal{N}(\mu , \sigma ^2). The model parameter \mu is not known, but \sigma ^2 is known (or we are able to assume a value for \sigma ^2).

Suppose that we are interested to infer the population mean \mu based on the observations and our model, but we are more interested in a **range** of *realistic values*. Such a range is called a **confidence interval**.

**Confidence Interval**

A confidence interval is an interval that is a **function of the observations**. It is closely related to the question of estimating the mean, as:

- it is **centered around the sample mean**
- its width is **proportional to the standard error**.

The confidence interval is also parameterized by the significance level \alpha. The interval is defined so that with probability 1-\alpha, the interval will contain the true mean \mu. This “probability" means that if we sample the dataset numerous times and calculate intervals for each time, the *probability* that \mu is in the proposed range (resulting intervals) is **1-\alpha** .

It could be defined as:

I(X) = \{ \theta | H_0: \mu = \theta can not be rejected at significance level \alpha, given the data X\}.

Figure below shows the probability of **z-test statistic** can take between -\Phi ^{-1}_{(1-\alpha /2)} and {\Phi ^{-1}_{(1-\alpha /2)}}, where \Phi is the Cumulative Distribution Function of the standard normal distribution, \alpha is the significant level.

The cumulative distribution function (cdf) is the probability that variable X takes a value less than or equal to x.

F_{X}(x)= P (X\leq x)

The figure shows the cumulative distribution function for a standard normal distribution:

![](https://courses.edx.org/assets/courseware/v1/1e3d06f991da458b69e54315e896f470/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_cdf.png)

The shade area in following figure represents \Phi _{(1-\alpha /2)}, where \alpha = 0.05:

![](https://courses.edx.org/assets/courseware/v1/6c61ab1b1b24d6ab7f605faf6a593e2c/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_cdf_cut.png)

Hide

![](https://courses.edx.org/assets/courseware/v1/40fa7afd0a09d4ac58d241485fade030/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_confidence_interval.png)

which means that:

|  | \displaystyle \displaystyle P ({-\Phi ^{-1}_{(1-\alpha /2)}} \leq {\frac{\bar{X} - \mu }{\sigma /\sqrt{n}}} \leq {\Phi ^{-1}_{(1-\alpha /2)}})= 1 - \alpha |  |  |
| --- | --- | --- | --- |

when we isolate \mu, the formula is equals to:

|  | \displaystyle \displaystyle P (\bar{X} -\frac{\sigma }{\sqrt{n}}\Phi ^{-1}_{(1-\alpha /2)} \leq \mu \leq \bar{X} +\frac{\sigma }{\sqrt{n}}\Phi ^{-1}_{(1-\alpha /2)}) = 1 - \alpha |  |  |
| --- | --- | --- | --- |

Hence, the confidence interval for true parameter \mu with probability 1 - \alpha:

|  | \displaystyle \displaystyle \bar{X} \pm \frac{\sigma }{\sqrt{n}}\Phi ^{-1}_{(1-\alpha /2)} |  |  |
| --- | --- | --- | --- |

The figure shows the confidence interval for 100 times simulation (sampling the dataset for 100 times). The probability where \mu falls into interval section is 1-\alpha. As you can see from the figure, \mu (red vertical line) is in the range of intervals (black horizontal line) in most of cases.

![](https://courses.edx.org/assets/courseware/v1/f723bddcd1a27699e771dde1a8ca36f6/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_confidence_interval_stimulation.png)

Note that in the video, the professor gives the confidence interval for estimating the mean of normalized r.v. \bar{X}_ i=\frac{X_ i}{\sigma /\sqrt{n}}.

# 9. Summary

In this lecture, we have discussed three different test statistics: Fisher Exact Test, Z - Test and T-Test. The table below provides a summary of properties of these three tests for reference.

![](https://courses.edx.org/assets/courseware/v1/09df8e73156cf8c53b21b8cc94a3fb15/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_hypothesis_test_summary-corrected-2.png)

We note that, the T-test only works when the sample is drawn from a normal distribution.

When conducting hypothesis testing, it is important to consider your claim and experiment data to pick the test approach most fitted to your objective.