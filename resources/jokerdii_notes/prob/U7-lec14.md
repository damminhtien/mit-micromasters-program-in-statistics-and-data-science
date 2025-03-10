# Lecture 14. Introduction to Bayesian Inference

* The big picture

  ![U7-lec14-bayes-framework](../assets/images/U7-lec14-bayes-framework.png) 

  * Problem types 
    * Hypothesis testing: unknown takes one of few possible values, aim at small probability of incorrect decision.
    * Estimation: numerical unknown(s), aim at an estimate that is "close" to the true but unknown value.

* The general framework

  * Bayes' rule $\rightarrow$ Posterior

    Unknown $\Theta$: treated as a random variable

    Prior distribution $p_\Theta$ or $f_\Theta$

    Observation $X$: observation model $p_{X|\Theta}$ or $f_{X|\Theta}$.

    Use appropriate version of the Bayes rule to find $p_{X|\Theta}(\cdot | X=x)$ or $f_{X|\Theta}(\cdot |X=x)$.

    ![U7-lec14-bayes-workflow](../assets/images/U7-lec14-bayes-workflow.png)

  * Point estimates (MAP, LMS)

    estimate: $\hat{\theta} = g(x)$;

    estimator: $\hat{\Theta} = g(X)$.

    * Maximum a posteriori probability (MAP):
      $$
      p_{\Theta|X}(\theta^*|x) = \max_\theta p_{\Theta|X}(\theta|x)\\
      f_{\Theta|X}(\theta^*|x) = \max_\theta f_{\Theta|X}(\theta|x)
      $$

    * Least Mean Squares (LMS):

      Conditional expectation: $\mathbf{E}[\Theta|X=x]$.

  * Types of Bayes rule

    | Types                               | Formula                                                      |
    | ----------------------------------- | ------------------------------------------------------------ |
    | Discrete $\Theta$, discrete $X$     | $p_{\Theta \vert X}(\theta \vert x) = {p_{\Theta}(\theta) p_{X\vert \Theta}(x \vert \theta) \over p_X(x)}\\ p_X(x) = \sum_{\theta'}p_{\Theta}(\theta')p_{X \vert \Theta} (x \vert \theta')$ |
    | Discrete $\Theta$, continuous $X$   | $p_{\Theta \vert X}(\theta \vert x) = {p_{\Theta}(\theta) f_{X\vert \Theta}(x \vert \theta) \over f_X(x)}\\ f_X(x) = \sum_{\theta'}p_{\Theta}(\theta')f_{X \vert \Theta} (x \vert \theta')$ |
    | Continuous $\Theta$, continuous $X$ | $f_{\Theta \vert X}(\theta \vert x) = {f_{\Theta}(\theta) f_{X\vert \Theta}(x \vert \theta) \over f_X(x)}\\ f_X(x) = \int f_{\Theta}(\theta')f_{X \vert \Theta} (x \vert \theta') \ d\theta' $ |
    | Continuous $\Theta$, discrete $X$   | $f_{\Theta \vert X}(\theta \vert x) = {f_{\Theta}(\theta) p_{X\vert \Theta}(x \vert \theta) \over p_X(x)}\\ p_X(x) = \int f_{\Theta}(\theta')p_{X \vert \Theta} (x \vert \theta') \ d\theta' $ |

  * Performance measures (prob. of error; mean squared error)

    * Conditional probability of error:  (smallest under the MAP rule)
      $$
      \mathbf{P}(\hat{\theta}\neq \Theta| X=x) 
      $$

    * Overall probability of error:
      $$
      \begin{aligned}
      \mathbf{P}(\hat{\Theta} \neq \Theta) &= \sum_x\mathbf{P}(\widehat{\Theta} \neq \Theta|X=x)p_X(x)\\
      &= \sum_\theta \mathbf{P}(\widehat{\Theta} \neq \Theta| \Theta = \theta) p_\Theta(\theta)\\
      \text{or}\\
      \mathbf{P}(\hat{\Theta} \neq \Theta) &= \int \mathbf{P}(\widehat{\Theta} \neq \Theta|X=x)f_X(x)dx\\
      &= \sum_\theta \mathbf{P}(\widehat{\Theta} \neq \Theta| \Theta = \theta) p_\Theta(\theta)\\
      \end{aligned}
      $$

  * Example: Inferring the unknown bias of a coin and the Beta distribution

    Coin with bias $\Theta$; prior $f_\Theta(\cdot)$; fix $n$; $K=$ Number of heads

    Assume prior $f_\Theta(\cdot)$ is uniform in $[0,1]$. The posterior probability is
    $$
    f_{\Theta\vert k}(\theta \vert k) = { 1 \cdot {n \choose k} \theta^k (1-\theta)^{n-k}\over p_K(k) } = {1\over d(n,k)} \theta^k (1-\theta)^{n-k}, \quad \theta \in [0,1]
    $$
    which follows Beta distribution, with parameter $(k+1, n-k+1)$.

    If prior is Beta
    $$
    f_\Theta(\theta) = {1\over c} \theta^\alpha (1-\theta)^\beta, \quad \alpha, \beta \geq 0
    $$
    The posterior probability is
    $$
    f_{\Theta \vert K}(\theta \vert k) = {{1\over c} \theta^\alpha (1-\theta)^\beta {n \choose k} \theta^k (1-\theta)^{n-k}\over p_K(k)} = d\ \theta ^{\alpha + k} (1-\theta) ^{\beta + n - k}
    $$
    The MAP estimate:
    $$
    \max_\theta \left[k \log \theta + (n-k) \log(1- \theta) \right]\\
    k/\theta - (n-k)/(1-\theta) = 0\\
    \widehat{\theta}_{MAP} = k/n
    $$
    The LMS is
    $$
    \begin{aligned}
    \mathbf{E}[\Theta | K=k] &= \int^1_0 \theta \ f_{\Theta|K}(\theta | k) \ d\ \theta \\
    &= {1\over d(n,k)} \int^1_0 \theta^{k+1} (1-\theta)^{n-k} \ d\ \theta \\
    &= {1\over {k!(n-k)!\over (n+1)! } }\cdot {(k+1)!(n-k)! \over (n+2)! } \\
    &= {k+1 \over n+2} \approx {k \over n} \quad \text{when n is large}
    \end{aligned}
    $$
    Note that for Beta random variable
    $$
    \int^1_0 \theta^\alpha (1-\theta)^\beta \ d\theta = {\alpha! \beta! \over (\alpha + \beta + 1)!}
    $$


There are 1 selected example and 2 solved problems.

---

## Exercise 1 Continuous unknown and observation

Let $\Theta$ and $X$ be jointly continuous nonnegative random variables. A particular value $x$ of $X$ is observed and it turns out that $f_{\Theta |X}(\theta \, |\, x)=2e^{-2\theta }$, for $\theta \geq 0$.

Recall that for an exponential random variable $Y$ with parameter $\lambda$, we have ${\bf E}[Y]=1/\lambda$ and $\textsf{Var}(Y)=1/\lambda ^2$.

1. What is the LMS estimate (conditional expectation) of $\Theta$?
2. What is the conditional mean squared error ${\bf E}\big [(\Theta -\widehat\Theta _{{\rm LMS}})^2\, |\, X=x]$?
3. What is the MAP estimate of $\Theta$?
4. What is the conditional mean squared error ${\bf E}\big [(\Theta -\widehat\Theta _{{\rm MAP}})^2\, |\, X=x]$?

**Solution:**

1. The posterior PDF is exponential with parameter 2. The LMS estimate is the mean of this distribution
   $$
   \mathbf{E}[\lambda|x] = 1/\lambda = 1/2
   $$

2. The conditional variance - the variance of an exponential random variable with parameter 2 is
   $$
   {\bf E}\big [(\Theta -\widehat\Theta _{{\rm LMS}})^2\, |\, X=x] = 1/\lambda^2 = 1/4
   $$

3. The posterior PDF, which is exponential, is largest at zero. The MAP estimate of $\Theta$ is 0.

4. Since $\widehat{\Theta}=0$, the conditional mean squared error is the second moment of the exponential distribution (that is, of the form ${\bf E}[Y^2]$, where $Y$ is exponential with parameter 2). Using the formula 
   $$
   {\bf E}[Y^2]=\textsf{Var}(Y)+\big ({\bf E}[Y]\big )^2
   $$
   we obtain
   $$
   {\bf E}[Y^2]=\frac{1}{4}+\Big(\frac{1}{2}\Big)^2=\frac{1}{2}.
   $$
   Note that the LMS estimator results in a smaller mean squared error.

## Problem 1 Defective Coin

A defective coin minting machine produces coins whose probability of Heads is a random variable $Q$ with PDF
$$
f_{Q}(q) = \begin{cases}5q^4, &  \text{if } q \in [0,1],\\ 0, &  \text{otherwise}. \end{cases}
$$
A coin produced by this machine is tossed repeatedly, with successive tosses assumed to be independent. Let $A$ be the event that the first toss of this coin results in Heads, and let $B$ be the event that the second toss of this coin results in Heads.

1. Find $\mathbf{P}(A)$.
2. Find the conditional PDF of $Q$ given event $A$. 
3. Find the $\mathbf{P}(B|A)$.

**Solution:**

1. To calculate $\mathbf{P}(A)$, we use the continuous version of the total probability theorem
   $$
   \mathbf{P}(A) = \int _0^1 \mathbf{P}(A\mid Q = q)f_ Q(q)\  dq = \int _0^1 q\cdot (5q^4)\  dq = \left[\frac{5}{6}q^6\right]_0^1 = \frac{5}{6}.
   {"mode":"full","isActive":false}
   $$

2. Using Bayes' rule
   $$
   \begin{aligned}
   f_{Q\mid A}(q) &= \frac{\mathbf{P}(A\mid Q = q)f_ Q(q)}{\mathbf{P}(A)}\\
   &=  \begin{cases} \frac{q\cdot (5q^4)}{5/6}, &  \text{if }0\leq q \leq 1,\\ 0, &  \text{otherwise,} \end{cases}\\
   &= \begin{cases} \displaystyle 6q^5, &  \text{if } 0\leq q \leq 1,\\ 0, &  \text{otherwise.} \end{cases} 
   \end{aligned}
   $$

3. Again we use the continuous version of the total probability theorem
   $$
   \begin{aligned}
    \mathbf{P}(B\mid A) & =\int _0^1\mathbf{P}(B\mid A, Q=q)f_{Q\mid A}(q)\  dq\\
    &= \int _0^1\mathbf{P}(B\mid Q=q)f_{Q\mid A}(q)\  dq\\
    &= \int _0^1 q(6q^5)\  dq\\
    &= 6/7.
   \end{aligned}
   $$
   The second equality holds because for a given value $q$ of $Q$, the events $A$ and $B$ are (conditionally) independent.

## Problem 2 Hypothesis test between two coins

Alice has two coins. The probability of Heads for the first coin is $1/4$, and the probability of Heads for the second is $3/4$. Other than this difference, the coins are indistinguishable. Alice chooses one of the coins at random and sends it to Bob. The random selection used by Alice to pick the coin to send to Bob is such that the first coin has a probability $p$ of being selected. Assume that $0 < p < 1$. Bob tries to guess which of the two coins he received by tossing it $3$ times in a row and observing the outcome. Assume that for any particular coin, all tosses of that coin are independent.

1. Given that Bob observed $k$ Heads out of the $3$ tosses (where $k = 0,1,2,3$), what is the conditional probability that he received the first coin?
2. We define an error to have occurred if Bob decides that he received one coin from Alice, but he actually received the other coin. He decides that he received the first coin when the number of Heads, $k$, that he observes on the $3$ tosses satisfies a certain condition. When one of the following conditions is used, Bob will minimize the probability of error. Choose the correct threshold condition.
3. For this part, assume that $p = 3/4$. What is the probability that Bob will guess the coin correctly? 
4. If $p$ is small, then Bob will always decide in favor of the second coin, ignoring the results of the three tosses. The range of such $p$'s is $[0,t)$. Find $t$.

**Solution:**

1. Let $Y$ be the number of Heads Bob observed in the three tosses. Let $C$ denote the coin that Bob received, so that $C=1$ if Bob received the first coin, and $C =2$ if Bob received the second coin. Then $\mathbf{P}(C=1)=p$ and $\mathbf{P}(C=2)=1-p$. Given the value of $C,Y$ is a binomial random variable.

   We can find the conditional probability that Bob received the first coin given that he observed $k$ Heads using Bayes' rule.
   $$
   \begin{aligned}
   \mathbf{P}(C=1\mid Y=k) &= \frac{\mathbf{P}(Y=k\mid C=1)\mathbf{P}(C=1)}{\mathbf{P}(Y=k)}\\
   &= \frac{\mathbf{P}(Y=k\mid C=1)\mathbf{P}(C=1)}{\mathbf{P}(Y=k\mid C=1)\mathbf{P}(C=1)+\mathbf{P}(Y=k\mid C=2)\mathbf{P}(C=2)}\\
   &= \frac{\binom {3}{k}(1/4)^ k(3/4)^{3-k}\cdot p}{\binom {3}{k}(1/4)^ k(3/4)^{3-k}\cdot p+ \binom {3}{k}(1/4)^{3-k}(3/4)^{k}\cdot (1-p)}\\
   &= \frac{3^{3-k}\cdot p}{3^{3-k}\cdot p + 3^ k \cdot (1-p)}.
   \end{aligned}
   $$

2. Given that Bob observes $k$ Heads, he is to decide whether the first or second coin was used. To minimize the probability of error, he should use the MAP rule, which in this case is to decide on the first coin when $\mathbf{P}(C=1|Y=k)\geq \mathbf{P}(C=2|Y=k)$. From symmetry, the second item, namely $\mathbf{P}(C=2|Y=k)$ is equal to $\frac{3^ k\cdot (1-p)}{3^{3-k}\cdot p + 3^ k \cdot (1-p)}$. We then have the following equivalent versions of this decision rule:
   $$
   \begin{aligned}
   \mathbf{P}(C=1|Y=k) &\geq \mathbf{P}(C=2|Y=k)\\
   \frac{3^{3-k}\cdot p}{3^{3-k}\cdot p + 3^ k \cdot (1-p)} & \geq \frac{3^ k\cdot (1-p)}{3^{3-k}\cdot p + 3^ k \cdot (1-p)}\\
   3^{3-k}\cdot p & \geq 3^ k \cdot (1-p)\\
   3^{2k-3} &\leq \frac{p}{1-p}\\
   2k-3 & \leq \log _3 \frac{p}{1-p}\\
   k & \leq \frac{3}{2}+\frac{1}{2}\log _3 \frac{p}{1-p}.
   \end{aligned}
   $$

3. If $p=3/4$ the threshold in the rule above is equal to $2$. Therefore, Bob will decide that he received the first coin when he observes $0,1,$ or $2$ Heads, and will decide that he received the second coin when he observes $3$ Heads.

   We find the probability of a correct decision using the total probability theorem:
   $$
   \begin{aligned}
   \mathbf{P}(\text{Correct}) &= \mathbf{P}(\text{Correct}|C=1)\cdot p + \mathbf{P}(\text{Correct}|C=2)\cdot (1-p)\\
   &= \mathbf{P}(Y<3|C=1)\cdot p + \mathbf{P}(Y=3|C=2)\cdot (1-p)\\
   &= (1-\mathbf{P}(Y=3|C=1))\cdot p + \mathbf{P}(Y=3|C=2)\cdot (1-p)\\
   &=  (1-(1/4)^3)(3/4) + (3/4)^3(1/4)\\
   &=\frac{216}{256}=\frac{27}{32}.
   \end{aligned}
   $$

4. Bob will never decide that he received the first coin if the threshold in the decision rule is negative, i.e., when
   $$
   \begin{aligned}
   \frac{3}{2}+\frac{1}{2}\log _3 \frac{p}{1-p} &< 0\\
   \log _3 \frac{p}{1-p} &< -3\\
   \frac{p}{1-p} &< {1\over 27}\\
   p &< \frac{1}{28}.
   \end{aligned}
   $$
   If $p < 1/28$, the prior probability of receiving the first coin is so low that no amount of evidence from $3$ tosses of the coin will make Bob decide he received the first coin.

