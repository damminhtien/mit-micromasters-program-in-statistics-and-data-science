# Unit 5: Nonparametric Hypothesis testing

# [Lecture 15: Goodness of Fit Test for Discrete Distributions](https://learning.edx.org/course/course-v1:MITx+18.6501x+1T2024/block-v1:MITx+18.6501x+1T2024+type@sequential+block@u05s01_hypotesting)

## **15.1. Motivation**

At the end of this lecture, you will be able to do the following:

- Understand the difference between parameter estimation, parametric hypothesis testing, and goodness of fit testing.
- Know when and how to apply a **goodness of fit** test for discrete distributions.
- Understand the **categorical distribution** , compute probabilities associated with it, and know how to compute **likelihoods** for a categorical distribution.
- Use the **maximum likelihood estimator** for the categorical distribution.

## **15.2. Introduction to Goodness of Fit Tests**

### Exercise 1: Determine fittest tests

Suppose you observe i.i.d. samples $X_1, \ldots , X_ n \sim P$ from some unknown distribution $\mathbf{P}$. Let $\mathcal{F}$ denote a parametric family of probability distributions (for example, $\mathcal{F}$ could be the family of normal distributions $\{ \mathcal{N}(\mu , \sigma ^2) \} _{\mu \in \mathbb {R}, \sigma ^2 > 0})$*.*

In the topic of goodness of fit testing, our goal is to answer the question "Does $\mathbf{P}$ belong to the family $\mathcal{F}$, or is $\mathbf{P}$ any distribution outside of $\mathcal{F}$?”
Parametric hypothesis testing is a particular case of goodness of fit testing (why?). However, in the context of parametric hypothesis testing, we assume that the data distribution $\mathbf{P}$ comes from some parametric statistical model $\{ \mathbf{P}_\theta \} _{\theta \in \Theta }$, and we ask if the distribution $\mathbf{P}$ belongs to a sub-model $\{ \mathbf{P}_\theta \} _{\theta \in \Theta_0}$ or its complement $\{ \mathbf{P}_\theta \} _{\theta \in \Theta_1}$. In parametric hypothesis testing, we allow only a small set of alternatives  $\{ \mathbf{P}_\theta \} _{\theta \in \Theta _1}$, where as in the goodness of fit testing, we allow the alternative to be anything.
Categorize the following problems as examples of parameter estimation (as studied in Unit 2), parametric hypothesis testing (as studied in the previous two lectures), or goodness of fit testing (as introduced in the above video). (Choose all categories that apply.)
**Problem 1: Estimate the bias of an unfair coin.**
**Problem 2: Decide if a 6-sided die is fair or not.**
**Problem 3: Decide if the heights of pine trees in Canada have a Gaussian distribution.** Assume that the statistical model for this data is $\{ \mathbb {R}, \Pi \}$ where $\Pi$ denotes the set of all probability distributions with sample space $\mathbb {R}$. (In particular, this model is non-parametric.)

**Solution:**

The terminology around parameter estimation, parametric hypothesis testing, and goodness of fit testing involves distinguishing between inferring parameters within a specified statistical model, testing hypotheses within a parametric framework, and assessing if an observed data distribution fits a hypothesized model, respectively. Let's analyze each problem based on these concepts:

**Problem 1: Estimate the bias of an unfair coin.**

- **a) Parameter estimation** - This is a classic example of parameter estimation where the goal is to determine the probability $p$ of heads (or tails) for a coin, which is not assumed to be a fair  $p = 0.5$. The parameter $p$ characterizes the distribution of outcomes (heads or tails) from the coin tosses.
- **b) Parametric hypothesis testing** - This does not apply directly here unless a specific hypothesis about the bias $p$ (like $p = 0.5$ or $p = 0.75$) is being tested against an alternative.
- **c) Goodness of fit testing** - This is not a case of goodness of fit testing since it does not involve assessing the adequacy of the binomial model against any unspecified alternative. The focus is on estimating within the assumed model.

**Problem 2: Decide if a 6-sided die is fair or not.**

- **1) Parameter estimation** - While estimating the probabilities of each face could be seen as parameter estimation, the problem as phrased aims more at hypothesis testing (fair vs. unfair).
- **2) Parametric hypothesis testing** - This problem is more accurately an example of parametric hypothesis testing where the hypothesis might be $H_0: \text{Each face has equal probability } \frac{1}{6}$ versus $H_1: \text{Not all faces have probability } \frac{1}{6}$.
- **3) Goodness of fit testing** - This problem also fits into goodness of fit testing since deciding whether a die is fair involves checking if the observed frequencies of die rolls fit the uniform distribution over six outcomes.

**Problem 3: Decide if the heights of pine trees in Canada have a Gaussian distribution.**

- **1) Parameter estimation** - This does not involve parameter estimation since the problem is not about inferring specific parameters within a parametric model but rather about assessing the distributional form of the data.
- **2) Parametric hypothesis testing** - This is not parametric hypothesis testing, as the model is not confined to a parameterized family; instead, it is non-parametric.
- **3) Goodness of fit testing** - This problem is clearly an example of goodness of fit testing. The task is to determine whether the empirical distribution of tree heights conforms to a Gaussian distribution, which is a case of testing the fit of observed data to a specific theoretical model without assuming that the data must follow a parametric model.

## **15.3. The Probability Simplex in $K$ Dimensions**

The probability simplex in $\mathbb {R}^ K$, denoted by $\Delta _ K$, is the set of all vectors $\mathbf{p} = \left[p_1, \dots , p_ K\right]^ T$ (note that we are using subscripts for vector indices for simplicity) such that

$$
\displaystyle \displaystyle \mathbf{p}\cdot \mathbf{1}\, =\, \mathbf{p}^ T \mathbf{1} = 1, ~ ~ p_ i \ge 0 \text { for all } i= 1,\ldots , K
$$

where $\mathbf{1}$ denotes the vector $\, \mathbf{1}=\begin{pmatrix} 1& 1& \ldots & 1\end{pmatrix}^ T$. Equivalently, in more familiar notation,

$$
\displaystyle \displaystyle \, \Delta _ K\, =\, \left\{ \mathbf{p}=(p_1,\ldots ,p_ K) \in [0,1]^ K \, :\, \displaystyle \sum _{i=1}^{K} p_ i \, =\, 1\right\} .
$$

## 15.4. **Goodness of Fit Test - Discrete Distributions**

### **Multinomial Distribution**

The **Multinomial Distribution** with $K$ modalities (or equivalently $K$ possible outcomes in a trial) is a generalization of the binomial distribution. It models the probability of counts of the $K$ possible outcomes of the experiment in $n$' i.i.d. trials of the experiment.

It is parameterized by the parameters $n$’, $n$$p_1,\dots ,p_ K$ where

- $n$' is the number of i.i.d trials of the experiment;
- $p_i$ is the probability of observing outcome $i$ in any trial, and hence the $p_ i$'s satisfy $p_ i \ge 0$for all $i = 1,\dots , K$, and $\displaystyle \sum _{i=1}^ K p_ i = 1$.

Let $\mathbf{p} \triangleq [p_1~ ~ p_2~ ~ \cdots ~ ~ p_ K]^ T$ and note that $\mathbf{p} \in \Delta _ K$.

The multinomial distribution can be represented by a random vector $\mathbf N\in \mathbb {Z}^ K$ to represent the number of instances $N^{(i)}$ of the outcome  $i = 1, \dots , K$. Note that $\sum _{i=1}^ K N^{(i)} = n$'. The **multinomial PMF** for all $\mathbf n$ such that $\sum _{i=1}^ K n^{(i)} = n', n^{(i)} \ge 0, i = 1, \dots , K$, and $n^{(i)} \in \mathbb {Z}, i = 1, \dots , K$ is given by

$$
\displaystyle p_{\mathbf N}\left(N^{(1)} = n^{(1)}, \dots , N^{(K)} = n^{(k)}\right) = \frac{n'!}{n^{(1)}! n^{(2)}! \cdots n^{(K)}!} \prod _{i=1}^ K p_ i^{n^{(i)}}.
$$

### **Categorial (Generalized Bernoulli) Distribution and its Likelihood**

The multinomial distribution, when specialized to $n$'$=1$ for any $K$ gives the **categorical distribution** . When $K = 2$ and the two outcomes are 0 and 1 the categorical distribution is the Bernoulli distribution, and for any  $K \ge 2$ the categorical distribution is also known as the **generalized Bernoulli distribution** .

The categorical distribution, therefore, models the probability of counts of the $K$ possible outcomes of a discrete experiment in a single trial. Since the total count is equal to 1 (only one trial), we can use a random variable $X$ to represent the outcome of the trial. This means the sample space of a **categorical random variable** $X$ is

$$
\displaystyle E = \{ a_1, \ldots , a_ K \} .
$$

The vector $\mathbf{p}$ is the parameter of a categorical random variable. The PMF of a categorical distribution can be given as

$$
P(X=a_ j) = \prod _{i=1}^ K p_ i^{\mathbf{1}(a_ i=a_ j)} = p_ j, ~ ~ j=1,\dots ,K.
$$

Let $\mathbf{P}_\mathbf {p}$ denote the distribution of a categorical random variable with sample space $E= \{ a_1, \ldots , a_ K \}$ and parameter vector $\mathbf{p}$. The **categorical statistical model** can thus be written as the tuple $\left( \{ a_1, \ldots , a_ K \} , \{ \mathbf{P}_{\mathbf{p}} \} _{\mathbf{p} \in \Delta _ K}\right)$.

In goodness of fit testing for a discrete distribution, we observe $n$ i.i.d. samples $X_1, \dots , X_ n$ of a categorical random variable $X$ and it is our aim to find statistical evidence of whether a certain distribution $\mathbf{p}^0 \in \Delta _ K$ could have generated $X_1, \dots , X_ n$.

The **categorical likelihood** of observing a sequence of $n$ i.i.d. outcomes $X_1, X_2, \dots , X_ n \sim X$ can be written using the number of occurrences $N_ i, i=1,\dots ,K$, of the $K$ outcomes as

$$
\displaystyle L_ n(X_1,\dots ,X_ n,p_1,\dots ,p_ K) = p_1^{N_1}p_2^{N_2} \cdots p_ K^{N_ K}.
$$

The categorical likelihood of the random variable X, when written as a random function, is

$$
\displaystyle L(X,p_1,\dots ,p_ K) = \prod _{i=1}^ K p_ i^{\mathbf{1}(X = a_ i)}.
$$

### Exercise 2: The Goodness of Fit Hypothesis Test for Discrete Distributions

Let  $X_1, \dots , X_ n$ be i.i.d. samples from a discrete distribution $\mathbf{P}_\mathbf {p}$ for some unknown $\mathbf{p} \in \Delta _ K$. Let $\mathbf{p}^0 \in \Delta _ K$ define a fixed pmf.

Which of the following represent valid goodness of fit tests to know whether there is statistical evidence that $X_1,\dots ,X_ n$ could have been generated by the pmf $\mathbf{p}^0$ as opposed to any other pmf? (Choose all that apply.)

a) $H_0: \mathbf{p} = \mathbf{p}^0, H_1: \mathbf{p} \ne \mathbf{p}^0$

b) $H_0: \left\| \mathbf{p} \right\| _2 = \left\| \mathbf{p}^0 \right\| _2, H_1: \left\| \mathbf{p} \right\| _2 \ne \left\| \mathbf{p}^0 \right\| _2$

**Solution:**

The first choice is a valid goodness of test while the second choice is not. Our aim in a goodness of fit test is to know whether there is statistical evidence that the data was generated by only our candidate distribution (against all other possible distributions). The first choice clearly achieves this aim.

The second choice is not a valid goodness of fit test. The failure to reject the null hypothesis does not necessarily imply that there is statistical evidence to say $\mathbf{p}^0$ is the only distribution that could have generated the observed data (with some probability). There are many vectors $\mathbf{p}$ that satisfy $\left\| \mathbf{p} \right\| _2 = \left\| \mathbf{p}^0 \right\| _2$ so the failure to reject means that we have statistical evidence that many possible candidate distributions could have generated the data.

## **15.5. Maximum Likelihood Estimator for the Categorical Distribution**

### Exercise: Likelihood for a Categorical Distribution

Suppose that $K = 3$, and let $E =\{ 1, 2, 3\}$. Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}_{\mathbf{p}}$ for some unknown $\mathbf{p} \in \Delta _3$. Let $f_{\mathbf{p}}$ denote the pmf of $\mathbf{P}_{\mathbf{p}}$ and recall that the likelihood is defined to be $L_ n(X_1, \ldots , X_ n, \mathbf{p}) = \prod _{i = 1}^ n f_{\mathbf{p}}(X_ i).$

Here we let the sample size be $n = 12$, and you observe the sample $\mathbf{x} = x_1, \ldots , x_{12}$ given by $\mathbf{x} = 1, 3, 1, 2, 2, 2, 1, 1, 3, 1, 1, 2,.$

The likelihood for this data set can be expressed as $L_{12}( \mathbf{x}, \mathbf{p}) = p_1^ A p_2^ B p_3^ C$.

Find in the values of A, B, and C.

**Solution:**

Since $K = 3$ and $E = \{ 1, 2, 3\}$, $f_{\mathbf{p}}(i) = p_ i, \quad i = 1,2,3.$

Next, $L_ n( X_1, \ldots , X_ n, \mathbf{p}) = \prod _{i = 1}^ n f_{\mathbf{p}}(X_ i) = p_1^{N_1} p_2^{N_2} p_3^{N_3}$

where $N_ i = \text {number of times} \, \, i \, \, \text {appears in } (X_1, \ldots , X_ n) , \quad i = 1,2, 3.$

In the data set above, 1 appears 6 times, 2 appears 4 times, and 3 appears 2 times. Thus, $A = N_1 = 6, B = N_2 = 4, C = N_3 = 2$.

### Exercise: Maximum Likelihood Estimator for Categorical Distribution

As above, under the statistical model $( \{ 1,2,3 \} , \{ \mathbf{P}_{\mathbf{p}} \} _{\mathbf{p} \in \Delta _3})$, we have $L_{12}(\mathbf{x}, \mathbf{p}) = p_1^ A p_2^ B p_3^ C$

where $\mathbf{x} = 1, 3, 1, 2, 2, 2, 1, 1, 3, 1, 1, 2.$

In the previous problem, you found the specific values for A, B, and C.

Recall that the MLE is given by $\widehat{\mathbf{p}}^{MLE}_ n = \text {argmax}_{\mathbf{p} \in \Delta _3} \log L_ n(X_1, \ldots , X_ n, \mathbf{p}).$

By the theory of Lagrange multipliers, one can show that the maximum occurs at the point $\mathbf{p}$ such that there exists $\lambda \neq 0$ so that $\nabla \log L_ n (X_1, \ldots , X_ n, \mathbf{p}) = \lambda \begin{bmatrix}  1 \\ 1 \\ 1 \end{bmatrix}.$(The gradient above is taken with respect to the parameter $\mathbf{p}$.)

Using this result and the previous problem, what is the estimate $\widehat{\mathbf{p}}^{MLE}_{12}$ for $\mathbf{p}$ given the data set $\mathbf{x}$?

**Solution:**

In the previous problem, we saw that A = 6, B = 4, and C = 2. Thus $\log L_ n(\mathbf{x}, \mathbf{p}) = 6 \log p_1 + 4 \log p_2 + 2 \log p_3.$

Hence, $\nabla \log L_ n(\mathbf{x}, \mathbf{p}) = \begin{bmatrix} \frac{6}{p_1} \\ \frac{4}{p_2} \\ \frac{2}{p_3} \end{bmatrix}.$

Applying the Lagrange multipliers, we have $\begin{bmatrix} \frac{6}{p_1} \\ \frac{4}{p_2} \\ \frac{2}{p_3} \end{bmatrix} = \lambda \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}.$

Therefore, $p_1 = \frac{6}{\lambda }, \, \, p_2 = \frac{4}{\lambda }, \, \, p_3 = \frac{2}{\lambda }.$

By the constraint $p_1 + p_2 + p_3 = 1$, we see that $\lambda = 6 + 4 + 2 = 12.$

Therefore, $\widehat{\mathbf{p}}^{MLE}_{12} = \begin{bmatrix} \frac{1}{2} \\ \frac{1}{3} \\ \frac{1}{6} \end{bmatrix}.$

### Exercise: Degrees of Freedom of a Known Test

Let us consider a statistical model with parameter $\theta \in \mathbb {R}^ d$. Let $\theta ^*$ be the parameter that generates the $n$ i.i.d. samples $\mathbf X_1,\dots , \mathbf X_ n$. Let $I(\theta )$ be the Fisher information and assume that the MLE $\hat{\theta }_ n^{\text {MLE}}$ is asymptotically normal. Assume that $I(\theta ^0)$ is a diagonal matrix with positive entries $1/t_1, \dots , 1/t_ d$. We wish to perform a test for the hypotheses $H_0: \theta ^* = \theta ^0$ and $H_1: \theta ^* \ne \theta ^0$.

Let the test statistic $T_ n$ be 

$$
\displaystyle T_ n = n\sum _{i=1}^ d \frac{\left(\theta _ i^0 - \hat{\theta }_{i}\right)^2 }{t_ i},
$$

where $\left[\hat{\theta }_{1} ~ ~ \hat{\theta }_{2}~ ~ \cdots ~ ~ \hat{\theta }_{d}\right]^ T = \hat{\theta }_ n^{\text {MLE}}$.

1) What distribution does the test statistic $T_ n$ converge to under $H_0$ as $n \to \infty$?

2) What is the number of degrees of freedom of the asymptotic distribution of $T_ n$?

**Solution:**

The test statistic $T_n$ can be seen to be equivalent to $\displaystyle n\left(\hat{\theta }_ n^{\text {MLE}} - \theta ^0\right)^ T I(\theta ^0) \left(\hat{\theta }_ n^{\text {MLE}} - \theta ^0\right)$

which is the test statistic for Wald's test. Therefore, $\displaystyle T_ n \xrightarrow [n\to \infty ]{(d)} \chi _ d^2.$

## **15.6. The Goodness of Fit Test for Discrete Distributions: Chi-Squared Test**

### Exercise: Hypothesis Testing for a Non-Uniform Distribution

Aliens from Planets X, Y, and Z gather on a remote planet every year to decide intergalactic policy. The organizing committee wants to check that the numbers of visitors from each planet is representative of that planet's population. Note that 

$\displaystyle \text {Population of Planet X: 1 million}$

$\displaystyle \text {Population of Planet Y: 4 million}$

$\displaystyle \text {Population of Planet Z: 5 million}.$

Let $E = \{ X, Y, Z\}$ denote the sample space. There are a total of 100 visitors chosen for this year's meeting from the overall population of 10 million. Let $\xi _1, \ldots , \xi _{100}$ denote random variables corresponding to alien $1,2,\ldots , 100,$ respectively, so that 

$\xi _ i = \begin{cases}  X \quad \text {if alien i comes from Planet X}\\ Y \quad \text {if alien i comes from Planet Y} \\ Z \quad \text {if alien i comes from Planet Z} \end{cases}$

The organizing committee models the outcome of the selection process as a statistical experiment with a categorical distributional model: $(\{ X, Y, Z\} , \{ \mathbf{P}_{\mathbf{p}} \} _{\mathbf{p} \in \Delta _3 })$ and write $\xi _1, \ldots , \xi _{100} \stackrel{iid}{\sim } \mathbf{P}_{\mathbf{p}^*} where \mathbf{p}^*$ is the true parameter. The null hypothesis and alternative hypothesis are, respectively,

$\displaystyle H_0\displaystyle : \mathbf{p}^* = \begin{bmatrix} \frac{1}{10} \\ \frac{4}{10} \\ \frac{5}{10} \end{bmatrix}.$ $\displaystyle H_1: \displaystyle : \mathbf{p}^* \neq \begin{bmatrix} \frac{1}{10} \\ \frac{4}{10} \\ \frac{5}{10} \end{bmatrix}.$

**Remark**: Note that if $H_0$ holds, then the visiting delegation is representative of the populations of the three planets in the sense that the percentage of visitors from Planet X (respectively, Planet Y and Z) is not far from the percentage of aliens that live on Planet X (respectively, Planet Y and Z).

Suppose there are 20 visitors from Planet X, 30 visitors from Planet Y, and 50 visitors from Planet Z. Let $\widehat{\mathbf{p} }$ denote the MLE for  $\mathbf{p}^*$ for this data set.

What is the asymptotic p-value of the $\chi ^2$ test 

$$
\psi _{100} = \mathbf{1}\left( 100 \left( \frac{(\widehat{p}_1 - \frac{1}{10} )^2}{1/10 } + \frac{(\widehat{p }_2 - \frac{4}{10} )^2}{4/10 } + \frac{(\widehat{p}_3 - \frac{5}{10} )^2}{5/10} \right) > C \right) ?
$$

Use [this tool](https://shiny.rit.albany.edu/stat/chisq/) to find the tail probabilities of a \chi ^2 distribution (you may also use any software you are familiar with).

**Solution:**

Since the sample space has 3 elements, X, Y, and Z, we know that $T_ n \xrightarrow [n \to \infty ]{(d)} \chi _2^2.$

Recall that the asymptotic p-value is the smallest asymptotic level so that the test  $\psi _ n$ rejects on the given data set.

The maximum likelihood estimator is given by $\widehat{\mathbf{p}} = \begin{bmatrix}  \frac{2}{10} \\ \frac{3}{10} \\ \frac{5}{10} \end{bmatrix}.$

Thus the test statistic takes the value

$$
\displaystyle T_{100} = 100 \left( \frac{(\frac{2}{10} - \frac{1}{10} )^2}{1/10 } + \frac{(\frac{3}{10} - \frac{4}{10} )^2}{4/10 } + \frac{(\frac{5}{10} - \frac{5}{10} )^2}{5/10} \right) \approx 12.5.
$$

Let $X \sim \chi _2^2$. To compute the asymptotic p-value, we set the threshold $C$ to be equal to the observed value of $T_{100}$ and compute $P( X \geq T_{100}) = P( X \geq 12.5) \approx 0.00193$ using the online tool.

## 15.7. The Chi-Squared Test for Two Modalities

### Exercise:

Consider the  $\chi ^2$ test statistic for $K=2$:

$$
T_ n = n \sum _{j = 1}^2 \frac{(\widehat{p}_ j - p_ j^0 )^2}{p_ j^0 }.
$$

We can use this statistic in a chi-squared test with 1 degree of freedom to determine, with an asymptotic level $\alpha$, whether the observed iid samples follow the distribution $\text {Ber}(p_2^0)$ under the null hypothesis $H_0$, with the sample space being the two values $a_1 = 0$ and $a_2 = 1$. The chi-squared test with asymptotic level $\alpha$ is $\mathbf{1}\left\{  T_ n > q_\alpha \right\} ,$ where $q_\alpha$ is the $(1-\alpha )$-quantile of the chi-squared distribution with 1 degree of freedom.

Is the following statement true or false? "This test is identical (asymptotically) to Wald's test of the Bernoulli statistical model with parameter $p$, null hypothesis $H_0: p=p_2^0$ and alternative hypothesis $H_1: p\ne p_2^0$, where $p_2^0$, as defined above, is the probability of  $a_2 = 1$ under the null hypothesis."

**Solution:**

The answer is true. Wald's test in the above statement is:

$$
\displaystyle \mathbf{1}\left\{ n \frac{\left(\widehat{p}_2 - p_2^0 \right)^2}{p_2^0\left(1 - p_2^0\right)} > q_\alpha \right\} ,
$$

where $q_\alpha$ is the $(1-\alpha )$-quantile of the chi-squared distribution with 1 degree of freedom.

The chi-squared test statistic can be re-written as:

$$
\displaystyle T_ n =\displaystyle n \sum _{j = 1}^2 \frac{(\widehat{p}_ j - p_ j^0 )^2}{p_ j^0 }=\displaystyle n \frac{(\widehat{p}_1 - p_1^0 )^2}{p_1^0 } + n\frac{(\widehat{p}_2 - p_2^0 )^2}{p_2^0 }=\displaystyle n \frac{((1-\widehat{p}_2) - (1-p_2^0) )^2}{1-p_2^0 } + n\frac{(\widehat{p}_2 - p_2^0 )^2}{p_2^0 }=\displaystyle n \frac{\left(\widehat{p}_2 - p_2^0 \right)^2 (p_2^0 + 1 - p_2^0)}{p_2^0\left(1 - p_2^0\right)}=\displaystyle n \frac{\left(\widehat{p}_2 - p_2^0 \right)^2}{p_2^0\left(1 - p_2^0\right)},
$$

which is the same as the test statistic for Wald's test.

### Exercise: **Chi-Squared Test for a Family of Discrete Distributions**

In the problems on this page, you will apply the $\chi ^2$ goodness of fit test to determine whether or not a sample has a binomial distribution.

So far, we have used the $\chi ^2$ test to determine if our data had a categorical distribution with specific parameters (e.g. uniform on an N element set).

For the problems on this page, we extend the discussion on $\chi ^2$ tests **beyond** what was discussed in lecture to the following more general statistical set-up.

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X\sim \mathbf{P}$ denote i.i.d. discrete random variables supported on $\{ 0, \ldots , K\}$. We will decide between the following null and alternative hypotheses:

$\displaystyle H_0: \displaystyle \mathbf{P}\in \{ \text {Bin}(K, \theta ) \} _{\theta \in (0,1)}$

$\displaystyle H_1:\displaystyle \mathbf{P}\notin \{ \text {Bin}(K, \theta ) \} _{\theta \in (0,1)},$

where the null hypothesis can be rephrased as: 

$$
\displaystyle \displaystyle H_0: \displaystyle \text {there exists } \, \theta \in (0,1)\, \text {such that for all }\, j = 0, \ldots , K, \, \text {we have } P(X = j) = \binom {K}{j} \theta ^{j} (1 - \theta )^{K -j}.
$$

**Exercise: Review: Log-likelihood for a Binomial Distribution**

Let  $(\{ 0, \ldots , K\} , \{ \text {Bin}(K, \theta ) \} _{\theta \in (0,1)})$ denote a binomial statistical model. Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Bin}(K, \theta ^*)$ for some unknown parameter $\theta ^* \in (0,1)$.

The log-likelihood of this statistical model can be written $C + A \log B + (n K - A ) \log (1 - B)$

where $C$ is independent of $\theta, A$ depends on  $\sum _{i = 1}^ n X_ i,$ and $B$ depends on $\theta$.

Find $A, B$?

**Solution:**

The PMF of $\text {Bin}(K, \theta )$ is $j \mapsto \binom {K}{j} \theta ^ j (1 - \theta )^{K - j}$ for $j \in \{ 0, \ldots , K\}$.

Therefore, the likelihood is given by

$\displaystyle L_ n(X_1, \ldots , X_ n, \theta )\displaystyle = \prod _{i = 1}^ n \left(\binom {K}{X_ i} \theta ^{X_ i} (1 - \theta )^{K - X_ i} \right)\displaystyle = \left( \prod _{i = 1}^ n \binom {K}{X_ i} \right) \theta ^{\sum _{i = 1}^ n X_ i} (1 - \theta )^{nK - \sum _{i = 1}^ n X_ i }.$

Taking the logarithm, we have $\log L_ n(X_1, \ldots , X_ n, \theta ) = \log \left( \prod _{i = 1}^ n \binom {K}{X_ i} \right) + \left( \sum _{i = 1}^ n X_ i \right) \log \theta + \left( nK - \sum _{i = 1}^ n X_ i \right) \log (1 - \theta ).$

Therefore, $A = \sum _{i = 1}^ n X_ i$ and $B = \theta$.

**Review: MLE for a Binomial Distribution**

As above, let $(\{ 0, \ldots , K\} , \{ \text {Bin}(K, \theta ) \} _{\theta \in (0,1)})$ denote a binomial statistical model. Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Bin}(K, \theta ^*)$ for some unknown parameter $\theta ^* \in (0,1)$.

Which of the following denotes the MLE for $\theta ^*$?

**Solution:**

Recall from the previous problem that $\log L_ n(X_1, \ldots , X_ n, \theta ) = C + \left( \sum _{i = 1}^ n X_ i \right) \log \theta + \left( nK - \sum _{i = 1}^ n X_ i \right) \log (1 - \theta )$ where $C$ does not depend on $\theta$.

To compute the MLE, we need to maximize the above with respect to the parameter $\theta$. We set the derivative to be 0: $\frac{\sum _{i = 1}^ n X_ i}{\theta } - \frac{nK - \sum _{i = 1}^ n X_ i}{1 - \theta } =0.$

The above holds when $p = \frac{1}{nK} \sum _{i = 1}^ n X_ i.$

Therefore, the right-hand side is the MLE for this statistical model.

**Review $\chi ^2$-Test for a Family of Distributions** 

Now, we return to the following more general statistical set-up.

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}$ denote i.i.d. discrete random variables supported on $\{ 0, \ldots , K\}$. We will decide between the following null and alternative hypotheses.

$\displaystyle H_0:\displaystyle \mathbf{P}\in \{ \text {Bin}(K, \theta ) \} _{\theta \in (0,1)}.$

$\displaystyle H_1:\displaystyle \mathbf{P}\notin \{ \text {Bin}(K, \theta ) \} _{\theta \in (0,1)}.$

Let $f_\theta$ denote the pmf of the distribution $\text {Bin}(K, \theta )$, and let $\widehat{\theta }$ denote the MLE of the parameter $\theta$ from the previous problem.

Further, let $N_ j$ denote the number of times that $j\, (j\in \{ 0,1,\ldots , K\})$ appears in the data set $\, X_1, \ldots , X_ n\,$ (so that $\, \displaystyle \sum _{j=0}^{K} N_ j =n.\, \,$) The ${\color{blue}{\chi ^2}}$ **test statistic for this hypothesis test** is defined to be $T_ n := n\sum _{j =0}^ K \frac{\left( \frac{N_ j}{n} - {\color{blue}{f_{\widehat{\theta }}(j)}}  \right)^2}{{\color{blue}{f_{\widehat{\theta }}(j)}}  }.$

This statistic is different from before. Previously, under the null hypothesis,  $\mathbf{P}(X=j)=p_ j\,$for some fixed $p_ j$. Here, instead, we use $f_{\widehat{\theta }}(j)$, to estimate $\mathbf{P}(X=j)\,$. This statistic still converges in distribution to a $\chi ^2$ distribution, but the number of degrees of freedom is smaller.

**Degrees of Freedom for \chi ^2 Test for a Family of Distribution**

More generally, to test if a distribution \mathbf{P} is described by some member of a family of discrete distributions \{ \mathbf{P}_{\theta } \} _{\theta \in \Theta \subset \mathbb {R}^ d} where \Theta \subset \mathbb {R}^ d is d-dimensional, with support \{ 0,1,2, \ldots , K\} and pmf f_\theta, i.e. to test the hypotheses:

|  | \displaystyle H_0: | \displaystyle \mathbf{P}\in \{ \mathbf{P}_\theta \} _{\theta \in \Theta } |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle H_1: | \displaystyle \mathbf{P}\notin \{ \mathbf{P}_\theta \} _{\theta \in \Theta }, |  |  |

then if indeed \mathbf{P}\in \{ \mathbf{P}_{\theta } \} _{\theta \in \Theta \subset \mathbb {R}^ d} (*i.e.*, the null hypothesis H_0 holds), and if in addition some technical assumptions hold, then we have that

| T_ n:= n\sum _{j =0}^ K \frac{\left( \frac{N_ j}{n} - f_{\widehat{\theta }}(j) \right)^2}{ f_{\widehat{\theta }}(j) } \xrightarrow [n \to \infty ]{(d)} \chi ^2_{(K+1) - d - 1}. |  |
| --- | --- |

Note that K+1 is the support size of \mathbf{P}_\theta (for all \theta.)

In our example testing for a binomial distribution, the parameter \theta is one-dimensional, i.e. d=1. Therefore, under the null hypothesis H_0, it holds that

| T_ n \xrightarrow [n \to \infty ]{(d)} \chi ^2_{(K+1) - 1 - 1} = \chi ^2_{K-1}. |  |
| --- | --- |

### Chi-squared Test for a Binomial Distribution on a Sample Data Set I

1/1 point (graded)

Consider the same statistical set-up as above. In particular, we have the test statistic

| T_ n := n \sum _{j =0}^ K \frac{\left( \frac{N_ j}{n} - f_{\widehat{\theta }}(j) \right)^2}{ f_{\widehat{\theta }}(j) }. |  |
| --- | --- |

where \widehat{\theta } is the MLE for the binomial statistical model (\{ 0,1, \ldots , K\} , \{ \text {Bin}(K, \theta ) \} _{\theta \in (0,1)}).

We define our test to be

| \psi _ n = \mathbf{1}( T_ n > \tau ), |  |
| --- | --- |

where \tau is a threshold that you will specify. For the remainder of this page, we will assume that K = 3 (the sample space is \{ 0,1,2,3\}).

What value of \tau should be chosen so that \psi _ n is a test of asymptotic level 5 \%? Give a numerical value with at least 3 decimals.

(Use [this table](https://people.richland.edu/james/lecture/m170/tbl-chi.html) or software to find the quantiles of a chi-squared distribution.)

\tau =\quad

correct

5.991

**Solution:**

Since [mathjaxinline]K = 3[/mathjaxinline] and [mathjaxinline]d = 1[/mathjaxinline], we know that the limiting distribution of [mathjaxinline]T_ n[/mathjaxinline] is [mathjaxinline]\chi _2^2[/mathjaxinline]. Thus, the asymptotic level is the value [mathjaxinline]\tau[/mathjaxinline] such that

| [mathjax]\lim _{n \to \infty } P( T_ n > \tau ) = P( Z > \tau ) = 0.05[/mathjax] |  |
| --- | --- |

where [mathjaxinline]Z \sim \chi _{2}^2[/mathjaxinline]. Hence, [mathjaxinline]\tau[/mathjaxinline] should be chosen to be [mathjaxinline]5.991[/mathjaxinline] (from the given table).

**SaveSave your answerShow answer**

**Submit**

You have used 1 of 2 attemptsSome problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

Answers are displayed within the problem

Review

### Chi-squared Test for a Binomial Distribution on a Sample Data Set II

3/3 points (graded)

Consider the same statistical set-up as above. Suppose we observe a data set consisting of 1000 observations as described in the following (format: i, number of observations of i):

|  | \displaystyle i ~ | \displaystyle ~ N_ i |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle 0 ~ | \displaystyle ~ 339 |  |  |
|  | \displaystyle 1 ~ | \displaystyle ~ 455 |  |  |
|  | \displaystyle 2 ~ | \displaystyle ~ 180 |  |  |
|  | \displaystyle 3 ~ | \displaystyle ~ 26 |  |  |

What is the value of the test statistic T_ n for this data set? Give a numerical value with at least 4 decimals. (You are encouraged to use computational software.)

T_ n=\quad

correct

0.8829

What is the p-value of this data set with respect to the test \psi _{1000}? Give a numerical value with at least 4 decimals.

Use [this tool](https://shiny.rit.albany.edu/stat/chisq/) to find the tail probabilities of a \chi ^2 distribution (you may also use any other software). If you are using this tool, note that you need to set "Choose Type of Control" to "Adjust X-axis quantile (Chi square) value" to find the tail probability associated with an x-axis value for a chi-squared distribution with degrees of freedom set in the "Degrees of Freedom" box.

p-value:

correct

0.6431

If \psi _ n is designed to have level 5\%, would you **reject** or **fail to reject** on the given data set?

correct

**Solution:**

Observe that the MLE is given by

| [mathjax]\widehat{\theta } = \frac{1}{3 \cdot 1000} (455 + 2 \cdot 180 + 3 \cdot 26 ) \approx 0.29767.[/mathjax] |  |
| --- | --- |

Thus for this data set,

|  | [mathjaxinline]\displaystyle T_ n = 1000[/mathjaxinline] | [mathjaxinline]\displaystyle \cdot \bigg( \frac{\left(\frac{339}{1000} - \binom {3}{0} (0.2977^0) (0.7023)^{3 - 0} \right)^2}{\binom {3}{0} (0.2977^0) (0.7023)^{3 - 0} } + \frac{\left(\frac{455}{1000} - \binom {3}{1} (0.2977^1) (0.7023)^{3 - 1} \right)^2}{\binom {3}{1} (0.2977^1) (0.7023)^{3 - 1} } +[/mathjaxinline] |  |  |
| --- | --- | --- | --- | --- |
|  |  | [mathjaxinline]\displaystyle \frac{\left(\frac{180}{1000} - \binom {3}{2} (0.2977^2) (0.7023)^{3 - 2} \right)^2}{\binom {3}{2} (0.2977^2) (0.7023)^{3 - 2} } + \frac{\left(\frac{26}{1000} - \binom {3}{3} (0.2977^3) (0.7023)^{3 - 3} \right)^2}{\binom {3}{3} (0.2977^3) (0.7023)^{3 - 3} } \bigg)[/mathjaxinline] |  |  |
|  |  | [mathjaxinline]\displaystyle \approx 0.8829[/mathjaxinline] |  |  |

The asymptotic p-value for this data set is given by

| [mathjax]\lim _{n \to \infty } P(T_ n > 0.8829) = P(Z > 0.8829).[/mathjax] |  |
| --- | --- |

where [mathjaxinline]Z \sim \chi _2^2[/mathjaxinline]. Consulting the suggested link, we see that [mathjaxinline]P(Z > 0.8829) \approx 0.6431[/mathjaxinline].

According to the golden rule of p-values, since [mathjaxinline]0.6431 > 0.05[/mathjaxinline], we should

**fail to reject**

the null hypothesis that [mathjaxinline]X_1, \ldots , X_{1000}[/mathjaxinline] are distributed as [mathjaxinline]\text {Bin}(3, \theta )[/mathjaxinline] for some value of the parameter [mathjaxinline]\theta[/mathjaxinline].

# [Lecture 16: The Kolmogorov-Smirnov test](https://learning.edx.org/course/course-v1:MITx+18.6501x+1T2024/block-v1:MITx+18.6501x+1T2024+type@sequential+block@u05s02_hypotesting)

## **16.1. Motivation**

### **Goodness of Fit Tests Continued: Kolmogorov-Smirnov test**

At the end of this lecture, you will be able to do the following:

- Compute the **empirical cumulative distribution function** for a given sample.
- Perform the **Kolmogorov-Smirnov** test to determine if a data set has a particular type of distribution.

## **16.2. Empirical Cumulative Distribution**

Let X be a random variable with distribution $\mathbf{P}$. Recall the CDF of $\mathbf{P}$, is given by the function

$$
⁍
$$

$$
\displaystyle t\displaystyle \mapsto \mathbf{P}(X \leq t).
$$

Let  $X_1, \ldots , X_ n \stackrel{iid}{\sim } X$. The **empirical cumulative distribution function**, also called the **empirical CDF**, is the random function

$$
\displaystyle F_ n: \mathbb {R}\displaystyle \to [0,1]
$$

$$
\displaystyle t\displaystyle \mapsto \frac{1}{n} \sum _{i = 1}^ n \mathbf{1}(X_ i \leq t).
$$

The empirical CDF depends on n and the observed data $X_ i, i = 1,\dots , n$.

### Exercise: Example of Empirical CDF

Let $X_1, \ldots , X_5$ be i.i.d. random variables. You obtain the sample $X_1=5, \, X_2=1.5, \, X_3=-3,\, X_4=0.0,\, X_5=7$.

Let $F(t)$ be the empirical CDF of this sample. Find

Find $F(-4)$.

Find $F(-3)$.

Find $F(10)$.

Find the largest interval of $t$ for which $\displaystyle F(t)=3/5$. Answer by entering $A$ and $B$ in the equation below $F(t)=3/5\, for A\leq t< B$.

**Solution**

Given the sample $\, X_1=5, \, X_2=1.5, \, X_3=-3,\, X_4=0.0,\, X_5=7$ the empirical cdf is

$$
\displaystyle F(t)\displaystyle =\displaystyle \frac{1}{5} \sum _{i = 1}^5 \mathbf{1}(X_ i \leq t)
\displaystyle =\displaystyle \begin{cases} 0 & \text {if }t<-3\\ 1/5& \text {if }-3\leq t< 0\\ 2/5& \text {if }0\leq t<1.5\\ 3/5& \text {if }1.5\leq t<5\\ 4/5& \text {if }5\leq t<7\\ 1& \text {if }7\leq t\\ \end{cases}.
$$

Hence $F(-4)=0,\, F(-3)=1/5,\, F(10)=1$ and $F(t)=3/5\,$, for$\, 1.5\leq t <5$.

**Remark:** The empirical CDF is right-continuous, just like the CDF.

## **16.3. Pointwise and Uniform Convergence of Functions**

A sequence of functions $g_n(x)$ **converges pointwise** to a function $g(x)$ if for each $x, \displaystyle \lim _{n\to \infty } g_ n(x)=g(x)$.

**Example:** In the region $x>1,\, g_ n(x)=\frac{1}{x^ n}$ converges **pointwise** to $g(x)=0$. For any fixed $x>1$, $\displaystyle \frac{1}{x^ n}\xrightarrow [n\to \infty ]{}0$.

A sequence of functions $g_ n(x)$ **converges uniformly** to a function $g(x)$ if $\displaystyle \lim _{n\to \infty } \sup _{x\in \mathbb {R}} |g_ n(x)-g(x)|=0.\, \,$That is, for every $M>0$, there exists an $n_ M$ such that $\sup _ x |g_ n(x) - g(x)| < M, \forall n \ge n_ M$.

**Example:** In the region $x>{\color{blue}{2}} ,\, g_ n(x)=\frac{1}{x^n}$ converges **uniformly** to $g(x)=0$, since  $\displaystyle \sup _{x>2} g_ n(x)=\sup _{x>2} \frac{1}{x^ n}= \frac{1}{2^ n}\xrightarrow [n\to \infty ]{} 0$.

**Example of pointwise but not uniform convergence:**

The sequence of functions $g_ n(x)=\frac{1}{x^ n}$ does **not** converge uniformly to $g(x) = 0$ in the region $x>1$, since  $\displaystyle \sup _{x>1} g_ n(x)=\sup _{x>1} \frac{1}{x^ n}= 1$, which does not converge to 0 as $n\to \infty$.

### **Fundamental Theorem of Statistics**

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X$ be i.i.d. random variables with cdf $F(t)$ and empirical cdf $F_ n(t)$.

The **Glivenko-Cantelli theorem**, also known as the **Fundamental Theorem of Statistics**, states that

$$
\sup _{t \in \mathbb {R}} |F_ n(t) - F(t)| \xrightarrow [n \to \infty ]{a.s.} 0.
$$

This is a stronger result than the one in the problem above in that the convergence happens **uniformly** over $t$. This means for all large enough n and for any $\delta > 0$, the difference $|F_ n(t) - F(t)|$ is bounded above by $\delta$ for all $t$. 

Almost sure convergence means that for all $\delta > 0$ and $\epsilon > 0$, there exists $N = N(\delta ,\epsilon )$ such that the event $\sup _{t} |F_ n(t) - F(t)| < \delta$ occurs with probability at least $1-\epsilon$ for all $n > N$. In other words, with probability approaching 1, the function $F_ n$ is a close  $L_\infty$  (the sup-norm) approximation of $F$.

### Exercise: Consistency of the Empirical CDF

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X$ be i.i.d. random variables with CDF $F(t)$.

Recall the empirical cdf is the random function

|  | \displaystyle F_ n: \mathbb {R} | \displaystyle \to [0,1] |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle t | \displaystyle \mapsto \frac{1}{n} \sum _{i = 1}^ n \mathbf{1}(X_ i \leq t). |  |  |

Then following convergence holds almost surely:

| F_ n(0) =\frac{1}{n} \sum _{i = 1}^ n \mathbf{1}(X_ i \leq 0) \xrightarrow [n\to \infty ]{a.s.} L |  |
| --- | --- |

for some value L. What is L? What result is invoked to obtain the value of L?

**Solution:**

Observe that for all i,\, \mathbf{1}(X_ i \leq 0)\, is a Bernoulli random variable with mean P(X_ i \leq 0) = F(0) . By the law of large numbers,

| F_ n(0) = \frac{1}{n} \sum _{i = 1}^ n \mathbf{1}(X_ i \leq 0) \xrightarrow [n\to \infty ]{a.s.} \mathbb E[\mathbf{1}(X_1 \leq 0)] = F(0). |  |
| --- | --- |

Therefore, L = F(0).

**Remark**

: It holds in general that for any t \in \mathbb {R},

| F_ n(t) = \frac{1}{n} \sum _{i = 1}^ n \mathbf{1}(X_ i \leq t) \xrightarrow [n\to \infty ]{a.s.} \mathbb E[\mathbf{1}(X_1 \leq t)]\, =\,  F(t) |  |
| --- | --- |

## 16.3. **Asymptotic Normality of the Empirical CDF**

### **Donsker's Theorem**

A stronger result than the one in the previous problem holds.

Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } X$ for some distribution $\mathbf{P}$ with cdf F. Let $F_ n$ denote the empirical cdf of $X_1, \ldots , X_ n$.

**Donsker's theorem** states that if the true cdf F is continuous, then

$$
\sqrt{n} \sup _{t \in \mathbb {R}} |F_ n(t) - F(t)| \xrightarrow [n \to \infty ]{(d)} \sup _{0 \leq x \leq 1} |\mathbb {B}(x)|,
$$

where $\mathbb {B}$ is a random curve called a **Brownian bridge**.

The definition of $\mathbb {B}$ is outside the scope of this course. What we need to know about it is the fact that $\sup _{0 \leq x \leq 1} |\mathbb {B}(x)|$ is a **pivotal** distribution, i.e. it does not depend on the unknown distribution of the data, and hence we can look up its quantiles in tables or by using software. This will be important as we develop goodness of fit tests for continuous distributions.

### Exercise: Pointwise Asymptotic Normality of the Empirical CDF

Let X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P} for some distribution \, \mathbf{P}\,, and let F denote its cdf. Let F_ n denote the empirical cdf. Then it holds for every t \in \mathbb {R} that

| \sqrt{n} (F_ n(t) - F(t)) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0, \sigma ^2) |  |
| --- | --- |

for any fixed t and for some asymptotic variance \sigma ^2.

What theorem implies the above convergence statement?

correct

Which of the following is \sigma ^2? Note that \sigma ^2 is dependent on t.

correct

What is the asymptotic variance \sigma ^2 of F_ n(0) in terms of the values of the cdf F? (Enter **F(x)** for F(x) for any numerical value x.)

\, \sigma ^2 = \,

correct

F(0)*(1 - F(0))

F(0)*(1-F(0))

**Solution:**

Recall that the empirical CDF is given by

| F_ n(t) = \frac{1}{n} \sum _{i = 1}^ n \mathbf{1}(X_ i \leq t). |  |
| --- | --- |

Moreover, \mathbb {E}[\mathbf{1}(X_ i \leq t)] = P(X_1 \leq t) = F(t), by definition. Therefore,

| \sqrt{n}(F_ n(t) - F(t)) = \sqrt{n} \left( \frac{1}{n} \sum _{i = 1}^ n \left( \mathbf{1}(X_ i \leq t) - \mathbb {E}[\mathbf{1}(X_ i \leq t)] \right) \right). |  |
| --- | --- |

The random variables \mathbf{1}(X_ i \leq t) are iid Bernoulli with mean P(X_ i \leq t) = F(t), so the **central limit theorem** applies:

| \sqrt{n}(F_ n(t) - F(t)) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0, F(t)(1 - F(t)) ). |  |
| --- | --- |

In summary, the correct answers are

- **Central limit theorem**, for the first question,
- F(t)(1 - F(t)) for the second question, and
- F(0)(1 - F(0)) for the third question when t=0.

## 16.4.  **Goodness of Fit Test of Continuous Distributions: Kolmogorov-Smirnov Test**

### Exercise: **Concept Check: Goodness of Fit Testing**

Let X_1, \ldots , X_ n be i.i.d. random variables with unknown cdf F. We will use the tools of goodness of fit testing to test if X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathcal{N}(0,1). Let \Phi denote the cdf of a standard normal.

Accordingly, you set the null and alternative hypotheses to be, respectively,

|  | \displaystyle H_0 | \displaystyle : F = \Phi |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle H_1 | \displaystyle : F \neq \Phi . |  |  |

If the null hypothesis holds and n is very large, you expect the empirical cdf F_ n(t) and standard normal cdf \Phi (t) to be...

correct

**Solution:**

We know by the Glivenko-Cantelli theorem that

| \sup _{t \in \mathbb {R}} |F_ n(t) - F(t)| \xrightarrow [n \to \infty ]{a.s.} 0. |  |
| --- | --- |

In particular, for fixed t,

| \lim _{n \to \infty } F_ n(t) = F(t). |  |
| --- | --- |

If the null hypothesis holds, then F(t) = \Phi (t), and we have

| \sup _{t \in \mathbb {R}} |F_ n(t) - \Phi (t)| \xrightarrow [n \to \infty ]{a.s.} 0. |  |
| --- | --- |

Therefore, if n is sufficiently large, this uniform convergence guarantees that the empirical cdf F_ n(t) and standard normal cdf \Phi (t) are ‘close' as functions of t. Thus, the correct response for this problem is ‘Similar.'

## 16.5. **Kolmogorov-Smirnov Test: Computational Issues**

Let X_1, \ldots , X_ n be i.i.d. random variables with unknown cdf F. Our goal is to test the hypotheses:

|  | \displaystyle H_0 | \displaystyle : | \displaystyle F = F^0 |  |  |
| --- | --- | --- | --- | --- | --- |
|  | \displaystyle H_1 | \displaystyle : | \displaystyle F \neq F^0. |  |  |

The **Kolmogorov-Smirnov test statistic** is defined as

| {\color{blue}{T_ n = \sup _{t \in \mathbb {R}} \sqrt{n} \bigg| F_ n(t) - F^0(t) \bigg|}} |  |
| --- | --- |

and the **Kolmogorov-Smirnov test** is

|  | \displaystyle \displaystyle \mathbf{1}(T_ n>q_\alpha )\qquad \text {where } q_\alpha =q_\alpha (\sup _{t \in [0,1]}\left| \mathbb {B}(t) \right|). |  |  |
| --- | --- | --- | --- |

Here, q_\alpha =q_\alpha (\sup _{t \in [0,1]}\left| \mathbb {B}(t) \right|)\, is the \, (1-\alpha )-quantile of the supremum \sup _{t \in [0,1]}\left| \mathbb {B}(t) \right| of the Brownian bridge as in Donsker's Theorem.

Even though the K-S test statistics T_ n is defined as a supremum over the entire real line, it can be computed explicitly as follows:

|  | \displaystyle \displaystyle T_ n | \displaystyle = | \displaystyle \sqrt{n}\sup _{t \in \mathbb {R}} \bigg| F_ n(t) - F^0(t) \bigg| |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | \displaystyle = | \displaystyle \sqrt{n}\max _{i=1,\ldots ,n}\left\{ \max \left(\left| \frac{i-1}{n}-F^0(X_{(i)}) \right|,\left| \frac{i}{n}-F^0(X_{(i)}) \right| \right) \right\} |  |  |

where X_{(i)} is the **order statistic** , and represents the i^{\text (th)} smallest value of the sample. For example, X_{(1)} is the smallest and X_{(n)} is the greatest of a sample of size n.

![](https://courses.edx.org/assets/courseware/v1/3ff6eea185fddcb024048b2512ecb854/asset-v1:MITx+18.6501x+1T2024+type@asset+block/images_u4s6_KSstat.svg)

An example of the empirical cdf \, F_ n(x_{(1)},x_{(2)},x_{(3)},x_{(4)})\, for a specific data set x_{(1)},x_{(2)},x_{(3)},x_{(4)} of sample size 4, and the cdf F_ X(x) under the null hypothesis.We see that because F^0(t) is increasing, and F_ n(t) is piecewise constant, \bigg| F_ n(t) - F^0(t) \bigg| can only possibly achieve its maximum at t=x_{(i)}.

### Concept Check: Kolmogorov-Smirnov Test Statistic

As above, let X_1, \ldots , X_ n be iid random variables with unknown cdf F. To decide between the null hypothesis, H_0: F = \Phi, and the alternative hypothesis, H_1: F \neq \Phi, stated in the previous problem, we consider the Kolmogorov-Smirnov test statistic for this hypothesis

$$
T_ n = \sup _{t \in \mathbb {R}} \sqrt{n} \bigg| F_ n(t) - \Phi (t) \bigg|.
$$

Which of the following are true statements regarding the test statistic T_ n? (Choose all that apply.)

- [ ]  Under H_0, T_ n converges in distribution to a Brownian motion.
- [ ]  T_ n converges to a pivotal distribution under H_0.
- [ ]  If H_0 holds, then T_ n converges to a distribution whose quantiles we can either look up in tables or estimate very well using simulations.
- [ ]  If H_0 holds, then T_ n converges to a distribution whose quantiles we can either look up in tables or estimate very well using simulations.

**Solution:**

We examine the choices in order.

- The first choice is incorrect. If H_0 holds, then T_ n converges to the **supremum** of a Brownian bridge. A Brownian motion is a **random curve** while its supremum over the interval [0,1] is a **random variable**. Since T_ n is also a random variable, it cannot converge to a random curve.
- The second choice is correct. Independent of the distribution of X_1, \ldots , X_ n, we have that $\sqrt{n}\sup _{t \in \mathbb {R}} |F_ n(t) - F(t)| \xrightarrow [n \to \infty ]{(d)} \sup _{x \in [0,1]} |\mathbb {B}(x)|.$
    
    That is, the limiting distribution is **independent** of the distribution of the X_1, \ldots , X_ n (as long as F is continuous). By definition, T_ n is a pivotal statistic under H_0.
    
- The third choice is correct. In general, pivotal distributions can be understood by consulting a table of quantiles. Using computational tools, Brownian motions (and their suprema) can be simulated, so this is another approach to computing the quantiles.
- The fourth choice is incorrect. If the sample size is n, then the formula on the slide "Kolmogorov-Smirnov test (3)" provides a formula that involves computing 2n maxima. This is certainly doable if n = 1000.

### Practice: Compute the Kolmogorov-Smirnov Test Statistic

1/1 point (graded)

Let X_1, \ldots , X_ n be iid samples with cdf F, and let F^0 denote the cdf of \textsf{Unif}(0,1). Recall that

| F^0(t) = t \cdot \, \mathbf{1}(t \in [0,1]) + 1 \cdot \mathbf{1}(t > 1) . |  |
| --- | --- |

We want to use goodness of fit testing to determine whether or not X_1, \ldots , X_ n \stackrel{iid}{\sim } \textsf{Unif}(0,1). To do so, we will test between the hypotheses

|  | \displaystyle H_0 | \displaystyle : F(t) = F^0 |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle H_1 | \displaystyle : F(t) \neq F^0. |  |  |

To make computation of the test statistic easier, let us first reorder the samples from smallest to largest, so that

| X_{(1)} \leq X_{(2)} \leq \ldots \leq X_{(n)} |  |
| --- | --- |

is the reordered sample. In this set-up, the Kolmogorov-Smirnov test statistic is given by the formula

| T_ n = \sqrt{n} \max _{i = 1, \ldots , n} \left\{  \max \left(\bigg| \frac{i -1}{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|, \bigg| \frac{i }{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|\right) \right\} . |  |
| --- | --- |

You observe the data set \mathbf{x} consisting of 5 samples:

| \mathbf{x}= 0.8, 0.7, 0.4, 0.7, 0.2 |  |
| --- | --- |

Using the formula above, what is the value of T_{5} for this data set? (You are encouraged to use computational tools.)

correct

0.6708

**Solution:**

First we reorder the given data set to get

| 0.2, 0.4, 0.7, 0.7, 0.8. |  |
| --- | --- |

Now X_{(i)} is defined to be the i-th element in the list above. Our goal is to compute

| T_ n = \sqrt{n} \max _{i = 1, \ldots , n} \left\{  \max \left(\bigg| \frac{i -1}{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|, \bigg| \frac{i }{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|\right) \right\} . |  |
| --- | --- |

for n = 5 and plugging in the above reordered data set. We first need to compute the maximum of the following list of numbers:

|  |  | \displaystyle \max (|0 - 0.2|,|0.2 - 0.2|) = 0.2 |  |  |
| --- | --- | --- | --- | --- |
|  |  | \displaystyle \max (|0.2 - 0.4|,|0.4 - 0.4|) = 0.2 |  |  |
|  |  | \displaystyle \max (|0.4 - 0.7|, |0.6 - 0.7|) = 0.3 |  |  |
|  |  | \displaystyle \max (|0.6 - 0.7|,|0.8 - 0.7|) = 0.1 |  |  |
|  |  | \displaystyle \max (|0.8 - 0.8|,|1 - 0.8|) ) = 0.2 |  |  |

which comes out to be 0.3. Therefore, T_5 = \sqrt{5} \cdot 0.3 \approx 0.6708.

## 16.5. **Kolmogorov-Smirnov Test Statistic Pivotal Under Null**

**Kolmogorov-Smirnov Test Statistic as a Pivotal Distribution Under Null Hypothesis**

Let \, X_1, \ldots , X_ n\, be iid samples with unknown cdf F_ X. For simplicity, restrict to the cases when F_ X is invertible.

Recall the goal of the Kolmogorov-Smirnov Test goodness of fit test is to decide between the hypotheses

|  | \displaystyle H_0 | \displaystyle : F_ X = F^0 |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle H_1 | \displaystyle : F_ X\neq F^0. |  |  |

Recall also the Kolmogorov-Smirnov test statistic:

|  | \displaystyle \displaystyle T_ n\, =\, \sqrt{n} \sup _{t \in \mathbb {R}} \left| F_ n(t) - F^0(t) \right| |  |  |
| --- | --- | --- | --- |

Assuming H_0 is true, then T_ n becomes

|  | \displaystyle \displaystyle T_ n\, =\, \sqrt{n} \sup _{t \in \mathbb {R}} \left| F_ n(t) - F_ X(t) \right| |  |  |
| --- | --- | --- | --- |

We will see that under the null hypothesis, the distribution of T_ n does not depend on the distribution of the data X_ i, i.e. T_ n is pivotal, and this is true for any n,\, not only for large n.

The trick is to make a change of variables. Let \tilde{t}=F_ X(t),\, then \, t=F_ X^{-1}(\tilde{t}).\, We have

|  | \displaystyle \displaystyle T_ n | \displaystyle = | \displaystyle \sqrt{n} \sup _{t \in \mathbb {R}} \left| F_ n(t) - F_ X(t) \right| |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | \displaystyle = | \displaystyle \sqrt{n} \sup _{t \in \mathbb {R}} \left| \left(\frac{1}{n}\sum _{i=1}^ n \mathbf{1}(X_ i\leq t)\right) - F_ X(t) \right|\qquad (\text {definition of empirical cdf}) |  |  |
|  |  | \displaystyle = | \displaystyle \sqrt{n} \sup _{t \in \mathbb {R}} \left| \left(\frac{1}{n}\sum _{i=1}^ n \mathbf{1}\left(F_ X(X_ i)\leq F_ X(t)\right)\right) - F_ X(t) \right|\qquad (\text {apply } F_ X\, \text {to both sides of inequality }) |  |  |
|  |  | \displaystyle = | \displaystyle \sqrt{n} \sup _{\tilde{t} \in (0,1)} \left| \left(\frac{1}{n}\sum _{i=1}^ n \mathbf{1}\left(Y_ i \leq \tilde{t}\right)\right)- \tilde{t}\, \right|\qquad \text {where } Y_ i\sim \textsf{Unif}(0,1). |  |  |

## 16.6. **Quantiles of the Pivotal Distribution and P-values**

### Kolmogorov-Smirnov Test for a Uniform Distribution

2/2 points (graded)

We use the statistical set-up from a previous problem. Recall that X_1, \ldots , X_ n are i.i.d. samples with cdf F, and F^0 denotes the cdf of \textsf{Unif}([0,1]). We have the null and alternative hypotheses

|  | \displaystyle H_0 | \displaystyle : F(t) = F^0 |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle H_1 | \displaystyle : F(t) \neq F^0. |  |  |

In the last problem, we computed the value of the test-statistic

| T_ n = \sqrt{n} \max _{i = 1, \ldots , n} \left\{  \max \left(\bigg| \frac{i -1}{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|, \bigg| \frac{i }{n} - X_{(i)} \mathbf{1}\left( X_{(i)} \in [0,1]\right) \bigg|\right) \right\} . |  |
| --- | --- |

for the data set

| \mathbf{x}= 0.8, 0.7, 0.4, 0.7, 0.2. |  |
| --- | --- |

You will use the Kolmogorov-Smirnov test

| \psi _5 = \mathbf{1}( T_5 > C ). |  |
| --- | --- |

What value of C should be chosen so that \psi _5 has (non-asymptotic) level 5 \%?

**Note:** Refer to the table in the slide “K-S table". If you are using this table, also note that the quantiles are presented for the statistic \sup _ t |F_ n(t) - F(t)| and you need to account for the factor \sqrt{n} while entering the quantile value for your answer. That is, the number x in the n-th row of the column labeled by the level \alpha table in the slide “K-S table" is such that

| P_ n^{KS}\left(\frac{T_ n}{\sqrt{n}} > x \right) = \alpha . |  |
| --- | --- |

correct

1.2595

For the Kolmogorov-Smirnov test of level 5\%, would you **reject** or **fail to reject** the null hypothesis on the above data set?

correct

**Solution:**

Let Y_1, \ldots , Y_ n be iid random variables with continuous cdf F. Consider the distribution of the statistic

| T_ n = \sqrt{n} \sup _{t \in \mathbb {R}} |F_ n(t) - F(t)|. |  |
| --- | --- |

This statistic is **pivotal**, *i.e.*, for any fixed n, the distribution of T_ n does **not** depend on the distribution of Y_ i. Let P_ n^{KS} denote the distribution of T_ n.

The number x in the n-th row of the column labeled by the level \alpha table in the slide “K-S table" is such that

| P_ n^{KS}\left(\frac{T_ n}{\sqrt{n}} > x \right) = \alpha . |  |
| --- | --- |

In our example, n = 5, and we want our test \psi _5 to have level 5 \%. The number in the 5'th row and column labeled by 0.05 is 0.56328. Therefore, we need to set C = \sqrt{5} \cdot 0.56328 \approx 1.2595.

In the previous question, we computed T_5 \approx 0.6708. Therefore, the test \psi _5 will

**fail to reject**

the null hypothesis that X_1, \ldots , X_5 \stackrel{iid}{\sim } U([0,1]) on the given data set.

## 16.7. **Goodness of Fit Tests Using Other Distances between Distributions**

Goodness of fit tests are statistical procedures used to determine how well a sample of observed data fits a specified theoretical distribution. While the Kolmogorov-Smirnov (KS) test uses the maximum absolute deviation between the empirical and theoretical cumulative distribution functions (CDFs), other tests use different metrics to measure the distance or difference between distributions. Here are some commonly used goodness of fit tests that use other distance measures:

### 1. **Chi-Squared Test**

- **Distance Measure**: This test compares the observed frequency counts in various categories to the expected frequency counts under the assumed distribution. The distance measure is the sum of squared differences between observed and expected frequencies, divided by the expected frequencies:
\[
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
\]
where \(O_i\) is the observed frequency for category \(i\) and \(E_i\) is the expected frequency under the null hypothesis.

### 2. **Anderson-Darling Test**

- **Distance Measure**: This test places more weight on the tails of the distribution than the KS test. It integrates the square of a weighted difference between the empirical and theoretical CDFs:
\[
A^2 = n \int_{-\infty}^{\infty} \frac{(F_n(x) - F(x))^2}{F(x)(1-F(x))} \, dF(x)
\]
where \(F_n(x)\) is the empirical CDF and \(F(x)\) is the theoretical CDF. The weighting function \(1/[F(x)(1-F(x))]\) amplifies discrepancies in the distribution's tails.

### 3. **Cramér-von Mises Criterion**

- **Distance Measure**: This criterion measures the squared differences between the empirical and theoretical CDFs, integrated over the entire range of the data:
\[
\omega^2 = n \int_{-\infty}^{\infty} (F_n(x) - F(x))^2 \, dF(x)
\]

### 4. **Lilliefors Test**

- **Distance Measure**: This is a variation of the KS test designed for situations where the parameters of the theoretical distribution are estimated from the data. It uses the KS statistic but adjusts for the estimation of parameters.

### 5. **Shapiro-Wilk Test**

- **Distance Measure**: Primarily used for testing normality, this test measures how much a dataset deviates from a normally distributed set of data. It's based on the correlation between the data and the corresponding normal scores.

### 6. **Energy Distance-Based Tests**

- **Distance Measure**: These tests are based on the concept of energy statistics, which involve computing distances between all pairs of points in the combined sample from two distributions. They are used in two-sample testing scenarios to compare two distributions but can be adapted for goodness of fit by treating the theoretical distribution as one of the samples.

### Applications

Each test has specific strengths and is particularly useful depending on the nature of the data and the importance of different parts of the distribution:

- The **Chi-Squared test** is easy to use and interpret but can be sensitive to the number of observations per category.
- The **Anderson-Darling and Cramér-von Mises tests** are more sensitive to deviations in the tails of the distribution than the KS test.
- The **Lilliefors Test** is useful when parameters are not known and must be estimated.
- **Shapiro-Wilk** is highly effective for small sample sizes when testing for normality.

These goodness of fit tests provide a range of tools for statisticians to test hypotheses about the underlying distributions of data, allowing for tailored approaches depending on specific data characteristics and hypothesis testing requirements.

# [Lecture 17: The Kolmogorov-Lilliefors test and Quantile-Quantile Plots](https://learning.edx.org/course/course-v1:MITx+18.6501x+1T2024/block-v1:MITx+18.6501x+1T2024+type@sequential+block@u05s03_hypotesting)

## 17.1. **Kolmogorov-Lilliefors Test**

### Motivation: Goodness of Fit Testing for a Gaussian Distribution

Let X_1, \ldots , X_ n be iid random variables with continuous cdf F. Let \{ \mathcal{N}(\mu , \sigma ^2) \} _{\mu \in \mathbb {R}, \sigma ^2 > 0} denote the family of all **Gaussian** distributions. We want to test whether or not F \in \{ \mathcal{N}(\mu , \sigma ^2) \} _{\mu \in \mathbb {R}, \sigma ^2 > 0}.

Let \Phi _{\mu , \sigma ^2} denote the cdf of \mathcal{N}(\mu , \sigma ^2). We formulate the null and alternative hypotheses

|  | \displaystyle H_0 | \displaystyle : F = \Phi _{\mu , \sigma ^2} \, \text {for some} \, \mu \in \mathbb {R}, \sigma ^2 > 0 |  |  |
| --- | --- | --- | --- | --- |
|  | \displaystyle H_1 | \displaystyle : F \neq \Phi _{\mu , \sigma ^2} \, \text {for any} \, \mu \in \mathbb {R}, \sigma ^2 > 0. |  |  |

Motivated by the Kolmogorov-Smirnov test, you define a test-statistic using the sample mean \hat{\mu } and sample variance \hat{\sigma ^2}:

| \widetilde{T}_ n = \sup _{t \in \mathbb {R}} \sqrt{n} |F_ n(t) - \Phi _{\hat{\mu }, \hat{\sigma ^2}}|. |  |
| --- | --- |

Assume that the **null hypothesis** is **true**. Is it true that

| \widetilde{T}_ n \xrightarrow [n \to \infty ]{(d)} \sup _{x \in [0,1]} |\mathbb {B}(x)| |  |
| --- | --- |

where \mathbb {B}(x) is a **Brownian bridge**? (Refer to the slides.)

correct

incorrect

**Solution:**

This claim is **false**. It is true that for any fixed \mu , \sigma ^2 that

| T_ n = \sup _{t \in \mathbb {R}}\sqrt{n} |F_ n(t) - \Phi _{\mu , \sigma ^2}| \xrightarrow [n \to \infty ]{(d)} \sup _{x \in [0,1]} |\mathbb {B}(x)|. |  |
| --- | --- |

This result follows by **Donsker's theorem** as the Gaussian cdf is continuous over the real line.

But if we plug in

**estimators**

for \mu and \sigma ^2 (and not their true values), then this convergence result no longer holds.

**Remark**

: However, it is true that under the null hypothesis

| H_0: F = \Phi _{\mu , \sigma ^2} \,  \text {for some} \,  \mu \in \mathbb {R}, \sigma ^2 > 0 |  |
| --- | --- |

that the statistic

| \widetilde{T}_ n =\sup _{t \in \mathbb {R}} \sqrt{n} |F_ n(t) - \Phi _{\hat{\mu }, \hat{\sigma ^2}}| |  |
| --- | --- |

is **pivotal**. Moreover, the statistic \widetilde{T}_ n converges in distribution as n \to \infty. The quantiles of \widetilde{T}_ n can be found in tables, and the test based on \widetilde{T}_ n is known as the **Kolmogorov-Lilliefors test** , which we discuss next.

### Concept Check: Kolmogorov-Smirnov vs. Kolmogorov-Lilliefors Test

0/1 point (graded)

Let X_1, \ldots , X_ n \stackrel{iid}{\sim } \mathcal{N}(\mu , \sigma ^2), let

| F_ n(t) = \frac{1}{n} \sum _{i =1}^ n \mathbf{1}(X_ i \leq t) |  |
| --- | --- |

denote their empirical distribution, and let \Phi _{\mu , \sigma ^2} denote the cdf of the distribution \mathcal{N}(\mu , \sigma ^2).

Recall that in the Kolmogorov-Smirnov test, we considered the test statistic

| T_ n = \sqrt{n}\sup _{t \in \mathbb {R}} |F_ n(t) - \Phi _{\mu , \sigma ^2}| |  |
| --- | --- |

In the Kolmogorov-Lilliefors test, we consider the test statistic

| \widetilde{T}_ n = \sqrt{n}\sup _{t \in \mathbb {R}} |F_ n(t) - \Phi _{\widehat{\mu }, \widehat{\sigma }^2}| |  |
| --- | --- |

It is true or false that T_ n and \widetilde{T}_ n have the same distribution for for all n \in \mathbb {N}? (Refer to the slides.)

correct

incorrect

**Solution:**

In T_ n, we plug in the actual values of parameters \mu and \sigma ^2. However, in \widetilde{T}_ n, we plug in estimators \widehat{\mu } and \widehat{\sigma }^2 for the true parameters. Therefore, T_ n and \widetilde{T}_ n will have different distributions for all n.

**Remark**

: Since the Kolmogorov-Lilliefors test uses a test statistic with a different distribution, when performing this goodness of fit test, we will have to consult a different table than what we used for the Kolmogorov-Smirnov test. We will compare the quantiles of the Kolmogorov-Smirnov test statistic and those of the Kolmogorov-Lilliefors test statistic in a problem below.

## 17.2. **Quantile-Quantile (QQ) Plots**

### Concept Check: QQ Plots

A quantile-quantile (QQ) plot is an informal but useful method for goodness of fit testing. Suppose we have an i.i.d. sample X_1, X_2, \ldots , X_ n with unknown cdf F^*. We are interested in determining whether or not F^* is the cdf F of some known distribution. For example, we may set F = \Phi _{0,1} to determine whether or not the sample comes from a standard Gaussian \, \mathcal{N}(0,1).

The **quantile-quantile (QQ) plot** is constructed in the following way from a data set:

1. Reorder the samples to be in increasing order. Denote the reordered sample by X_{(1)}, X_{(2)}, \ldots , X_{(n)}.
2. Plot the points
    
    
    | \bigg(F^{-1}\left(\frac{1}{n}\right), X_{(1)}\bigg), \,  \,  \bigg(F^{-1}\left(\frac{2}{n}\right), X_{(2)}\bigg), \,  \,  \ldots , \,  \,  \bigg(F^{-1}\left(\frac{i}{n}\right), X_{(i)}\bigg), \,  \,  \ldots , \,  \,  \bigg(F^{-1}\left(\frac{n-1}{n}\right), X_{(n-1)}\bigg). |  |
    | --- | --- |

Note that above we omit plotting the n'th point because F^{-1}(n/n) = F^{-1}(1) = \infty. (In cases where F^{-1}(1) is defined, we do not need to omit that point.)

Which of the following are true about quantile-quantile (QQ) plots? (Choose all that apply.)

- [ ]  A QQ plot provides a visual method for determining whether or not a data set has a certain distribution.
- [ ]  A QQ plot is a rigorous, formal method of goodness of fit testing. For example, it makes sense to talk about the type 1 error of a goodness of fit test.
- [ ]  If n is very large and the points on the QQ plot lie very far from the line y = x, then it is reasonable to conclude that F and F^* are close as cdfs.
- [ ]  Looking at the graphs of the empirical cdf F_ n(t) and the cdf F, it can be difficult to tell if the two functions are close. The QQ plot transforms the cdf F and the empirical cdf F_ n(t) so that it is easier to compare the two visually.

**Solution:**

We examine the choices in order.

- The first choice is correct. If the empirical cdf F_ n(t) and cdf F are close, then we expect F^{-1}(i/n) \approx X_{(i)}. Hence, the data points
    
    
    | \bigg(F^{-1}(1/n), X_{(1)}\bigg), \,  \,  \bigg(F^{-1}(2/n), X_{(2)}\bigg), \,  \,  \ldots , \,  \,  \bigg(F^{-1}(i/n), X_{(i)}\bigg), \,  \,  \ldots , \,  \,  \bigg(F^{-1}((n-1)/n), X_{(n-1)}\bigg). |  |
    | --- | --- |
    
    should lie near the line y = x. Plotting these points, we can visually compare the distribution of our data to the distribution that has cdf F.
    
- The second choice is incorrect. In contrast to the methods we have studied before for hypothesis testing, a QQ plot is **not** a formal testing procedure. Rather, it conveniently visualizes the data so that we can get a sense of whether the distribution of our data matches some known distribution (for example, \, \mathcal{N}(0,1)).
- The third choice is incorrect. Rather, if n is very large and the points in the QQ plot are very far from the line y = x, this implies that the cdf of X_1, \ldots , X_ n and the cdf F are **not** close. More precisely, this would imply that F is **not** well-approximated by F_ n(t). On the other hand, if n is very large, then F_ n(t) \approx F^* by the Glivenko-Cantelli theorem. Therefore, if the QQ plot lies near the line y = x, we see that F(i/n) \approx F_ n(i/n) for all 1 \leq i \leq n. In this situation it would be more reasonable to infer that X_1, \ldots , X_ n have cdf F.
- The fourth choice is correct. Indeed, it can be difficult to compare the empirical cdf F_ n(t) with another cdf F near the tail values. Taking the QQ plot compares the inverse cdf F^{-1} with a notion of the inverse of the empirical cdf (However, note that, strictly speaking, the empirical cdf is not invertible). This is much easier to visualize, because then we just have to check if the points in the QQ plot lie near the line y = x to see if the distribution of our data is similar to the distribution with cdf F.

# Homework 8

## 3. QQ plots

Consider an i.i.d. sample $X_1, X_2, \ldots , X_ n \stackrel{iid}{\sim } \mathbf{P}$ that has been reordered as $X_{(1)} \leq X_{(2)} \leq \ldots \leq X_{(n)}$ where n is very large. In the problems below, we have chosen a different distribution for $\mathbf{P}$ and compared the empirical quantiles to the standard Gaussian quantiles using a QQ plot. Recall that

- the **Laplace distribution** $\text {Lap}(\lambda )$ with parameter $\lambda > 0$ is the continuous probability distribution with density $f_\lambda = \frac{\lambda }{2} e^{-\lambda |x|}$, and
- the **Cauchy distribution** is the continuous probability distribution with density $g(x) = \frac{1}{\pi } \frac{1}{1 + x^2}$.

(These were also introduced in Lecture 12. )

For each plot below, match the QQ plot with the correct distribution for $\mathbf{P}$. *Hint:* Each possible distribution will be an answer choice exactly once, so you should use the process of elimination.

*Hint:* You may use computational tools to graph the pdf of the possible distributions of $\mathbf{P}$.

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Number of samples
n_samples = 1000

# Generate samples
data_normal = np.random.normal(0, 1, n_samples)
data_cauchy = np.random.standard_cauchy(n_samples)
data_shifted_exponential = np.random.exponential(1/2.5, n_samples) + 1  # shift c=1 for illustration
data_uniform = np.random.uniform(-np.sqrt(3), np.sqrt(3), n_samples)
data_laplace = np.random.laplace(0, 1/np.sqrt(2), n_samples)

# Function to create QQ plots
def create_qq_plot(data, theoretical_dist, title):
    # Calculate quantiles
    data_quantiles = np.quantile(data, q=np.linspace(0, 1, n_samples))
    theoretical_quantiles = theoretical_dist.ppf(np.linspace(0, 1, n_samples))
    
    # Create QQ plot
    plt.figure(figsize=(8, 8))
    plt.scatter(theoretical_quantiles, data_quantiles, s=5)
    plt.plot(theoretical_quantiles, theoretical_quantiles, color='r', ls='--')  # y=x reference line
    plt.title(title)
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')
    plt.grid(True)
    plt.show()

# Create QQ plots for each distribution
create_qq_plot(data_normal, stats.norm, 'QQ Plot: Standard Normal vs. Standard Normal')
create_qq_plot(data_cauchy, stats.norm, 'QQ Plot: Cauchy vs. Standard Normal')
create_qq_plot(data_shifted_exponential, stats.norm, 'QQ Plot: Shifted Exponential vs. Standard Normal')
create_qq_plot(data_uniform, stats.norm, 'QQ Plot: Uniform vs. Standard Normal')
create_qq_plot(data_laplace, stats.norm, 'QQ Plot: Laplace vs. Standard Normal')
```

![Untitled](Unit%205%20Nonparametric%20Hypothesis%20testing%203675da3f5dbc4d3b8be1eb7bf0b4d08a/Untitled.png)

![Untitled](Unit%205%20Nonparametric%20Hypothesis%20testing%203675da3f5dbc4d3b8be1eb7bf0b4d08a/Untitled%201.png)

![Untitled](Unit%205%20Nonparametric%20Hypothesis%20testing%203675da3f5dbc4d3b8be1eb7bf0b4d08a/Untitled%202.png)

![Untitled](Unit%205%20Nonparametric%20Hypothesis%20testing%203675da3f5dbc4d3b8be1eb7bf0b4d08a/Untitled%203.png)

![Untitled](Unit%205%20Nonparametric%20Hypothesis%20testing%203675da3f5dbc4d3b8be1eb7bf0b4d08a/Untitled%204.png)