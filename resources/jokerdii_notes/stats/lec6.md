# Lecture 6. Introduction to Hypothesis Testing, and Type 1 and Type 2 Errors

There are 11 topics and 6 exercises.

## 1. Intro to Hypothesis Testing

* Let $X$ (resp. $Y$) denote the boarding time of a random JetBlue (resp. United) flight. 

* We assume that $X \sim \mathcal{N}(\mu_1, \sigma^2_1)$ and $Y \sim \mathcal{N}(\mu_2, \sigma^2_2)$

* Let $n$ and $m$ denote the JetBlue and United sample sizes respectively. 
* We have $X_1, ..., X_n$ independent copies of $X$ and $Y_1, ..., Y_m$ independent copies of $Y$.
* We further assume that the two samples are independent.

We want to answer the question: "Is $\mu_1 = \mu_2$? " or "Is $\mu_1 > \mu_2$? "

By making **modeling assumptions**, we have reduced the number of ways the hypothesis $\mu_1 = \mu_2$ may be rejected. We do not allow that $\mu_1 < \mu_2$.

We have two samples: this is a **two-sample test**.

## 2. Statistical Model of a Two Sample Experiment

An associated statistical model is $\left(E,\{ P_\theta \} _{\theta \in \Theta }\right)$ where

* $E$ is the smallest sample space of the pair $(X,Y)$, 
* $P_\theta$ is the family of joint distribution of $(X,Y)$ with parameter $\theta$. Because $X $ and $Y$ are independent, their joint distribution is the product of their respective distributions.

In the first scenario, the observed outcome of a statistical experiment consists of two samples:
$$
X_1,X_2,\ldots X_ n\stackrel{\text {i.i.d.}}{\sim }X\sim \textsf{Ber}(p_1)\\
Y_1,Y_2,\ldots Y_ m\stackrel{\text {i.i.d.}}{\sim }Y\sim \textsf{Ber}(p_2).
$$
where in addition, $X,Y$ and the two samples $X_1, ..., X_n$ and $Y_1, ..., Y_m$ are independent.

Identify the sample space $E$ and the parameter space $\Theta$: (Use $]x,y[$ to denote an open interval.)

* Sample space $E$: $\{0,1\}\times \{0,1\} = \{(0,0), (0,1),(1,0), (1,1)\}$.

  Since $X\sim \textsf{Ber}(p_1)$ and $X\sim \textsf{Ber}(p_2)$, the pair $(X,Y)$ takes value in the sample space $E=\{ 0,1\} \times \{ 0,1\} =\{ (0,0),(0,1),(1,0),(1,1)\}$.

* Parameter space $\Theta$: $]0,1[\;  \times \; ]0,1[\;  \subset \mathbb {R}^2$.

  Since $X,Y$ are independent, the joint distribution of $(X,Y)$ is the product $\textsf{Ber}(p_1)\times \textsf{Ber}(p_2)$. Hence, the family $\{ P_\theta \} _{\theta \in \Theta }$ of joint distributions is parametrized by $\theta = (p_1, p_2)$ and the parameter space is 
  $$
  \Theta =\{ (p_1,p_2): p_1\in ]0,1[, p_2\in ]0,1[\} = ]0,1[\times ]0,1[\subset \mathbb {R}^2.
  $$

---

In the second scenario, we aim to test whether boarding times by the Window-Middle-Aisle boarding method is shorter than boarding times by the rear-to-front method. We collect a sample of boarding times of each method and model these boarding times as the following two sets of normal variables:
$$
X_1,X_2,\ldots X_ n \text { are } i.i.d. \text { copies of } X\sim \mathcal{N}(\mu _1,\sigma _1^2)\qquad \text {boarding times of rear-to-front}\\
Y_1,Y_2,\ldots Y_ m \text { are } i.i.d. \text { copies of } Y\sim \mathcal{N}(\mu _2,\sigma _2^2)\qquad \text {boarding times of window-middle-aisle}
$$
where $X$ and $Y$ are also independent.

For simplicity, **assume the two standard deviations $\sigma^2_1$ and $\sigma^2_2$ are some known, fixed quantities $\sigma^*_1$ and $\sigma^*_2$** .

Identify the sample space $E$ and the parameter space $\Theta$: (Use $]x,y[$ to denote an open interval.)

* Parameter space $\Theta$: $(\mu_1, \mu_2)$

  Since $X$ and $Y$ are independent, the joint distribution of $(X,Y)$ is the product $\mathcal{N}\left(\mu _1,(\sigma _1)^2\right) \times \mathcal{N}\left(\mu _2,(\sigma _2)^2\right)$. Since $\sigma_1$ and $\sigma_2$ are fixed and known, the only parameter determining the joint distribution is $\mu_1$ and $\mu_2$. Hence, a choice of the parameter $\theta$ is the 2D vector $(\mu_1 \quad \mu_2)$.

* Sample space $E$: 

  Since the family of joint distribution would be parametrized by $(\mu_1 \quad \mu_2)$, we have the parameter space 
  $$
  \Theta =\{ (\mu _1,\mu _2): \mu _1\in \mathbb {R}, \mu _2\in \mathbb {R}\} =\mathbb {R}^2.
  $$
  Because $\mu_1$ and $\mu_2$ model average boarding times, we can further restrict to 
  $$
  \Theta =\{ (\mu _1,\mu _2): \mu _1\in [0,\infty ), \mu _2\in [0,\infty )\} =[0,\infty )\times [0,\infty )\} .
  $$

## 3. Heuristics for Two Sample Tests

**Simple heuristic:** 

If $\bar{X}_n > \bar{Y}_m$, then $\mu_1 > \mu_2$.

This could go wrong if I randomly pick only full flights in my sample $X_1, ..., X_n$ and empty flights in my sample $Y_1,...,Y_m$.

**Better heuristic:**

If $\bar{X}_n - \text{Buffer}_n > \bar{Y}_m + \text{Buffer}_m$, then $\mu_1 > \mu_2$.

To make this intuition more precise, we need to take the **size of the random fluctuations** of $\bar{X}_n$ and $\bar{Y}_m$ into account (including variance, sample size, confidence, fluctuations of $\bar{X}_n$ and $\bar{Y}_m$ about their respective means $\mu_{\text{drug}}$ and $\mu_{\text{control}}$, those are what "Buffer" depends on).

## 4. Heuristics for One Sample Tests

Waiting time in the ER:

* Is it true that the new hospital has a longer waiting time than 30min, which is the average waiting time in the Emergency Room (ER).
* We collect only one sample $X_1,...,X_n$ (waiting time in minutes for $n$ random patients) with unknown expected value $\mathbb{E}[X_1] = \mu$.
* We want to know if $\mu > 30$

Heuristic:

If $\bar{X}_n + \text{Buffer}_n < 30$, then conclude that $\mu \leq 30$. 

If $\bar{X}_n - \text{Buffer}_n > 30$, then conclude that $\mu \geq 30$.

> #### Exercise 33
>
> Which of the following are **true statements** regarding **hypothesis testing** as exemplified above and **parameter estimation** as discussed in previous lectures?
>
> a. In the above hypothesis testing set-up and in the models in the previous lectures on parameter estimation, we make the assumption that our data is iid from some unknown distribution.
>
> b. When carrying out parameter estimation, we are interested in coming up with an estimator $\hat{\mu}$ that we want to be close to the true parameter $\mu$.
>
> c. When performing hypothesis testing (as above), we are **not** necessarily interested in finding an estimator for $\mu$. Rather, our goal is to decide whether or not the true parameter lies in a certain region.
>
> d. When performing hypothesis testing, our main goal is to come up with a good approximation of the true parameter.
>
> **Answer**: abc
>
> **Solution**: 
>
> a. In the parameter estimation unit, for all statistical models we assumed that our sample consisted of iid random variables.
>
> b. The main goal of parameter estimation is to come up with some approximation for the unknown true parameter using the sample $X_1, ..., X_n$.
>
> cd. The goal of hypothesis testing is to decide if the true parameter has some particular property (e.g. whether it lies in a particular region or not).

## 5. Two Sample vs. One Sample Tests

A **one-sample test** is a hypothesis test where an unknown parameter $\mu$ is to be compared to a known reference value.

A **two-sample test** is a hypothesis test where two unknown parameters are compared to each other.

## 6. Examples

#### 1. Does at most a third of Americans get at least some news from YouTube?

According to a survey conducted in 2017 on 4,971 randomly sampled Americans, $32\%$ report to get at least some of their news on Youtube. Can we conclude that at most a third of all Americans get at least some of their news on Youtube?

* $n =  4,971, X_1, ..., X_n \stackrel{iid}{\sim}\mathsf{Ber}(p):$

* $\bar{X}_n = 0.32$

* If it was true that $p = .33$. 

* The mean is  $\mathbf{E}[\bar{X}_n] = 0.33$, the variance is $ \mathsf{Var}(\bar{X}_n) = {0.33 (1- 0.33)\over 4,971 }$

* By CLT,
  $$
  \sqrt{n} {\bar{X}_n - 0.33 \over \sqrt{0.33 (1- 0.33)}} \approx \mathcal{N}(0,1)
  $$

* $\sqrt{n} {\bar{X}_n - 0.33 \over \sqrt{0.33 (1- 0.33)}} \approx -1.50$

* Remark: 
  * Once the $\bar{X}_n$ is normalized, the fluctuations are from standard Gaussian. That is, the $\bar{X}_n$ not being equal to $0.33$ might be due to the fluctuations of the standard Gaussian.
  * What statistics is about is to take a problem that might be on its own scale, map it into a scale which is in terms of percentage of a Gaussian, then we are willing to tolerate $99\%$ of probability, or $1\%$ of error, which means a confidence level of $99\%$. Then we need to map it back onto the original scale.

> #### Exercise 34 Review CLT
>
> Recall the CLT states that if 
>
> * $X_1 ,..., X_n$ are i.i.d.;
> * $\mathbb {E}[X_1] = \mu < \infty ,$ and $\text {Var}(X_1) = \sigma ^2 < \infty$
>
> Then a shift and a rescaling of the sample mean $\overline{X}_ n = \displaystyle \frac{1}{n} \sum _{i = 1}^ n X_ i$ converges to a standard Gaussian $\mathcal{N}(0,1)$ in distribution as $n \rightarrow \infty$:
> $$
> \sqrt{n}\left( \frac{\overline{X}_ n - \mu }{\sigma } \right) \xrightarrow [n \to \infty ]{(d)} \mathcal{N}(0,1).
> $$
> Suppose $\mu = 0$ and $\sigma^2 = 1$. Given this assumption, which of the following limits is strictly between 0 and 1?
>
> a. $\lim _{n \to \infty } P(\overline{X}_ n \in (-1, 1))$
>
> b. $\lim _{n \to \infty } P\left(\overline{X}_ n \in \left(-\frac{1}{\sqrt{n}}, \frac{1}{\sqrt{n}} \right)\right)$
>
> c. $\lim _{n \to \infty } P\left(\overline{X}_ n \in \left(-\frac{1}{n}, \frac{1}{n} \right)\right)$
>
> **Answer**: b
>
> **Solution**:
>
> Let $Z \sim \mathcal{N}(0,1)$ and let $a_n, b_n$ denote sequences depending on $n$. By the CLT,
> $$
> \begin{aligned}
> \lim _{n \to \infty } P(\overline{X}_ n \in (a_ n,b_ n)) &= \lim _{n \to \infty } P(\sqrt{n}\,  \overline{X}_ n \in (\sqrt{n} a_ n, \sqrt{n} b_ n))\\
> &= P(Z \in (\lim _{n \to \infty } \sqrt{n} a_ n, \lim _{n \to \infty } \sqrt{n} b_ n))
> \end{aligned}
> $$
>
> * For option 'a', $\lim _{n \to \infty } P(\overline{X}_ n \in (-1, 1))  = 1$. 
>
>   By setting $a_n = -1$ and $b_n = 1$, we see that
>   $$
>   \lim _{n \to \infty } \sqrt{n} a_ n = - \infty , \quad \lim _{n \to \infty } \sqrt{n} b_ n = \infty .
>   $$
>   Hence, by the above calculation,
>   $$
>   \lim _{n \to \infty } P(\overline{X}_ n \in (a_ n,b_ n)) = P(Z \in (-\infty , \infty )) = 1.
>   $$
>
> * $\lim _{n \to \infty } P\left(\overline{X}_ n \in \left(-\frac{1}{\sqrt{n}}, \frac{1}{\sqrt{n}} \right)\right)$ lies strictly between $0$ and $1$, as we will show below. Setting $a_n = -{1\over \sqrt{n}}$ and $b_n = {1\over \sqrt{n}}$, we see that
>   $$
>   \sqrt{n}a_n = -1, \quad \sqrt{n} b_n = 1.
>   $$
>   Hence, by the above calculation,
>   $$
>   \lim _{n \to \infty } P(\overline{X}_ n \in (a_ n,b_ n)) = P(Z \in (-1,1))
>   $$
>   Since Gaussian variables have a positive probability of being inside $(-1,1)$ and also a positive probability of being outside $(-1,1)$, we can also conclude without doing any computation that $0 < \mathbf{P}(Z \in (-1,1)) < 1$.
>
>   **Remark**: Alternatively we can compute, using computational tools or a table that
>   $$
>   P(Z \in (-1,1)) = \int _{-1}^1 \frac{1}{\sqrt{2 \pi }} e^{-x^2/2} \,  dx \approx 0.6827.
>   $$
>
> * $\lim _{n \to \infty } P\left(\overline{X}_ n \in \left(-\frac{1}{n}, \frac{1}{n} \right)\right)=0$.
>
>   Setting $a_n = -{1\over n },$ and $b_n = {1\over n}$, we see that 
>   $$
>   \lim _{n \to \infty } \sqrt{n} a_ n = \lim _{n \to \infty } -\frac{1}{\sqrt{n}} = 0, \quad \lim _{n \to \infty } \sqrt{n} b_ n = \lim _{n \to \infty } \frac{1}{\sqrt{n}} = 0
>   $$
>   Hence, by the above calculation,
>   $$
>   \lim _{n \to \infty } P(\overline{X}_ n \in (a_ n,b_ n)) = P(Z \in (0, 0)) = 0.
>   $$
>
> **Remark:** This exercise emphasizes the heuristic interpretation of the CLT which states that the sample mean $\bar{X}_n$ lives inside an interval of radius  "$Constant \times {1\over \sqrt{n}}$" around its expectation. This heuristic will be useful for designing hypothesis tests.

#### 2. Testing fairness of a coin

A coin is tossed $30$ times and Heads are obtained $13$ times. Can we conclude that the coin is significantly unfair?

* $n =30, X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Ber}(p);$

* $\bar{X}_n = 13/30 \approx 0.43$

* If it was true that $p = 0.5$. By CLT,
  $$
  \sqrt{n}{\bar{X}_n - 0.5 \over\sqrt{0.5(1-0.5)} } \approx \mathcal{N}(0,1)
  $$

* Our data gives $\sqrt{n}{\bar{X}_n - 0.5 \over\sqrt{0.5(1-0.5)} } \approx -0.77$

* The number $-0.77$ is a plausible realization of a random variable $Z \sim \mathcal{N}(0.1).$

* Conclusion: **It is not unlikely that the coin is fair**.

> #### Exercise 35
>
> We use the statistical set-up from the previous problem. Consider a statistical experiment where you flip the coin $200$ times. In one run of this experiment, you observe $80$ **heads**. We will use this data and the estimator $\sqrt{n}\frac{\left( \overline{X}_ n - 0.5\right)}{\sqrt{0.5(1 - 0.5)}}$ to provide an answer to the hypothesis testing question of interest: "Does $p = 0.5$ or does $p \neq 0.5$?".
>
> 1. Let $D_1$ denote the value of the realization of the statistic $\sqrt{n}\frac{\left( \overline{X}_ n - 0.5\right)}{\sqrt{0.5(1 - 0.5)}}$ on the given data set. (Here $n=200$, the number of flips.) What is $D_1$?
>
> 2. Let $Z \sim \mathcal{N}(0,1)$. What is $\mathbf{P}(Z < D_1)$?
>
> 3. Since $n=200$ is fairly large, we may assume that if $p=0.5$ that $\sqrt{n}\frac{\left( \overline{X}_ n - 0.5\right)}{\sqrt{0.5(1 - 0.5)}} \sim \mathcal{N}(0,1).$
>
>    Suppose that $p=0.5$ and you ran the experiment above (consisting of $200$ coin flips) a total of $1000$ times (i.e. a total $200 \times 1000$ coin flips). What is the expected number of experiments such that the estimator $\sqrt{n}\frac{\left( \overline{X}_ n - 0.5\right)}{\sqrt{0.5(1 - 0.5)}}$ is small than the value $D_1$ attained in the first experiment?
>
> **Answer**:
>
> $1) -2.82842$ ; 2) $0.00234$ ; 3) $2$
>
> **Solution**: 
>
> 1) First, 
>$$
> D_1 = \sqrt{200}\left( \frac{\frac{80}{200} - 0.5 }{\sqrt{0.25}} \right) \approx -2.82842.
> $$
> 2) Using a table or computational software, we can also compute that if $Z \sim \mathcal{N}(0,1)$,
> $$
> P(Z < D_1) = \int _{-\infty }^{-2.82842} \frac{1}{\sqrt{2 \pi }} e^{-x^2/2} \,  dx \approx .00234
> $$
> ![lec6-ex35-gaussian](../assets/images/lec6-ex35-gaussian.svg)
> 
> 3) Hence, for a single experiment, if $p=0.5$, then there is (approximately) a $0.23\%$ chance of seeing an observation smaller than $D_1 \approx -2.82842$. Thus if we run $1000$ experiments, we would expect to see
>$$
> 1000*(.00234) \approx 2.33907
> $$
> Experiments where $\sqrt{n}\frac{\left( \overline{X}_ n - 0.5\right)}{\sqrt{0.5(1 - 0.5)}}$ is smaller than $D_1 \approx -2.82842$.
> 
> **Remark 1**:
>
> We can conclude that it is unlikely that $p=0.5$. Indeed, if $p=0.5$, observing the value $D_1 \approx -2.82842$ would be a very rare event, intuitively speaking. 
>
> **Remark 2**:
>
> In general, we will transform our data into a given statistic whose distribution we know well that does **not** depend on the true parameter (e.g., as in this problem, the standard Gaussian). Such a distribution is known as **pivotal**. Then we can reduce our hypothesis testing question to a problem of deciding whether or not a given observation is likely (or not) for this pivotal distribution.

## 7. Statistical Formulation of Hypothesis Testing

Statistical formulation:

* Consider a sample $X_1, ..., X_n$ of i.i.d. random variables and a statistical model $(E, (\mathbb{P}_\theta)_{\theta \in \Theta})$.
* Let $\Theta_0$ and $\Theta_1$ be disjoint subsets of $\Theta$.
* Conside the two hypotheses: $\begin{cases}H_0: &\theta \in \Theta_0 \\ H_1: & \theta \in \Theta_1 \end{cases}$
* $H_0$ is the *null hypothesis*, $H_1$ is the *alternative hypothesis*.
* If we believe that the true $\theta$ is either in $\Theta_0$ or in $\Theta_1$, we may want to *test $H_0$ against $H_1$*.
* We want to decide whether to *reject* $H_0$ (look for evidence against $H_0$ in the data.)

If $\Theta_1$ lies on only one side of $\Theta_0$, this is called a **one sided test**. If $\Theta_1$ lies on both sides of $\Theta_0$, this is called a **two sided test**.

**Remark**: 

Suppose the question is "whether this hospital has longer waiting time than average?" We state the hypothesis as $H_0: \mu \leq 30; H_1 : \mu > 30$, where $H_1$ is what we are looking for evidence in the data to show. Intuitively, if it is "innocnet" at the end, we did not find enough evidence to prove that it is "guilty". And the burden is on the trial to bring evidence. But if you walk away free, it does not mean that it is "innocnet". It is just that we were not able to bring enough evidence.

Regardless of the data, our conclusion will never be to *accept* the null. On observing the data, we will either **reject** the null in favor of the alternative OR we will **fail to reject** the null. In the latter case, we are not claiming that the null is true, rather we are stating that the data does not provide us with enough evidence to refute the null hypothesis.

## 8. Statistical Tests

#### Asymmetry in the hypothesis

* $H_0$ and $H_1$ do not play a symmetric role: the data is only used to try to disprove $H_0$
* In particular lack of evidence, does not mean that $H_0$ is true (" innocent until proven guilty")
* A *(statistical) test* is a **statistic** $\psi \in \{0,1\}$, which does not depend explicitly on the value of true unknown parameter, such that:
  * If $\psi=0$, $H_0$ is not rejected.
  * If $\psi = 1$, $H_1$ is rejected.
* Coin example: $H_0: p = 1/2$ vs. $H_1: p \neq 1/2$.
* $\psi = \mathbf{1} \{ \sqrt{n} {|\bar{X}_n - 0.5|\over \sqrt{0.5(1-0.5)} } > C \}$, for some $C > 0$.

## 9. Type 1/2 Error and Power of a Statistical Test

* Rejection region of a test $\psi$:
  $$
  R_{\psi} = \{ x \in E^n : \psi(x)=1\}.
  $$
  Rejection region of test $\psi_n$:
  $$
  R_{\psi _ n} := \{ (x_1, \ldots , x_ n) \in E^ n: \,  \psi _ n(x_1, \ldots , x_ n) =1 \}
  $$
  where $E$ is the sample space of the i.i.d. variables $X_i$, which is $\R_{\geq0}$ in this example since $X_i$ are uniform random variables.

* Type 1 error of a test $\psi$ (rejecting $H_0$ when it is actually true):
  $$
  \begin{aligned}
  \alpha_{\psi}: \Theta_0 &\rightarrow \R\\
  \theta &\mapsto \mathbb{P_\theta}[\psi = 1].
  \end{aligned}
  $$
  Type 1 error of test $\psi_n$ (rejecting $H_0$ when it is actually true):
  $$
  \begin{aligned}
  \alpha_{\psi_n}: \Theta_0 &\rightarrow \R\\
  \theta &\mapsto \mathbb{P_\theta}[\psi_n = 1].
  \end{aligned}
  $$
  Where $\mathbf{P}_\theta(\psi_n=1)$ is the probability of the event $\psi_n=1$ under the probability distribution $\mathbf{P}_\theta$ when $\theta \in \Theta_0$, i.e. the probability of rejecting $H_0$ when $H_0$ is true. 

* Type 2 error of a test $\psi$ (not rejecting $H_0$ although $H_1$ is actually true):
  $$
  \begin{aligned}
  \beta_\psi:\Theta_1 &\rightarrow \R\\
  \theta &\mapsto \mathbb{P_\theta}[\psi = 0].
  \end{aligned}
  $$
  Type 2 error of test $\psi_n$ (not rejecting $H_0$ although $H_1$ is actually true):
  $$
  \begin{aligned}
  \beta_{\psi_n}:\Theta_1 &\rightarrow \R\\
  \theta &\mapsto \mathbb{P_\theta}[\psi_n = 0].
  \end{aligned}
  $$
  Where $\mathbf{P}_\theta(\psi_n=0)$ is the probability of the event $\psi_n=0$ under the probability distribution $\mathbf{P}_\theta$ when $\theta \in \Theta_1$, i.e. the probability of not rejecting $H_0$ when $H_1$ is true. 

* Power of a test $\psi$:
  $$
  \pi_\psi = \inf_{\theta \in \Theta_1} (1-\beta_\psi(\theta))
  $$

> #### Exercise 36 Type 1 error
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } N(\mu , 1)$ where $\mu$ is an unknown parameter. You are interested in answering the question of interest: "Does $\mu = 0$?".
>
> To do so, you construct
>
> * the **null hypothesis** $H_0: \mu = 0$;
> * the **alternative hypothesis** $H_1: \mu \neq 0$.
>
> Motivated by the CLT, you decide to use a test of the form
> $$
> \psi _ C = \mathbf{1}(\sqrt{n} \,  | \overline{X}_ n | > C ).
> $$
> Recall that the **type 1 error** (also known as **type 1 error rate** ) of a test $\psi$ is the **function**:
> $$
> \begin{aligned}
> \alpha _{\psi }: \Theta _0 &\rightarrow [0,1]\\
> \theta &\mapsto \mathbf{P}_\theta(\psi = 1)
> \end{aligned}
> $$
> If you choose the threshold $C = q_{0.05}$, what is the type 1 error $\alpha_\psi$?
>
> (In this case, since $H_0$ only consists of one point, the function $\alpha_\psi$ is defined only at one point, and we loosely use the terminology "type 1 error" to mean the value of $\alpha_\psi$ at that point.)
>
> **Solution**:
>
> If we assume the null hypothesis $H_0: \mu = 0$, and since the variance is known to be $1$, the CLT gives
> $$
> \sqrt{n}\,  \overline{X}_ n \sim \mathcal{N}(0,1)\qquad \text {for large } \, n.
> $$
> The probability of a type 1 error is
> $$
> \alpha _\psi (0)\, =\, \mathbf{P}_{0}(\psi _ C = 1)
> $$
> as depicted in the figure below
>
> ![lec6-ex36-type1error](../assets/images/lec6-ex36-type1error.svg)
>
> If $H_0$ is true, i.e. $\mu = 0$, then $\sqrt{n}\overline{X}_n$ is asymptotically normal. Hence, the total area of the two shaded regions is $\mathbf{P}_{0}(\psi _ C = 1)\, =\, \mathbf{P}_0\left(\sqrt{n} \,  | \overline{X}_ n | > q_{0.05} \right)$, the probability that $H_0$ is rejected even through it is true.

> #### Exercise 37 A Non-Asymptotic Test for the Support of a Uniform Variable
>
> Let $X_1, ...,X_n \stackrel{iid}{\sim}\mathsf{Unif}(0, \theta)$ for an unknown parameter $\theta$. Let $\left(\mathbb {R}_{\geq 0}, \{ \text {Unif}[0, \theta ]\} _{\theta > 0}\right)$ denote the associated statistical model. (Here, $\R_{\geq 0}$ denotes the nonnegative real numbers. )
>
> You want to answer the question of interest: "Is $\theta\leq 1/2$?". To do so you formulate a hypothesis test with
> $$
> H_0: \theta \leq 1/2\\H_1: \theta > 1/2
> $$
> And also design the test
> $$
> \psi _ n = \mathbf{1}(\displaystyle \max _{1 \leq i \leq n} X_ i > 1/2)
> $$
> If $\psi_n = 1$ we will reject the null hypothesis. Note the dependence of $\psi_n$ on the sample size.
>
> 1. We use $\Theta_0$ to denote the region of $\Theta$ defined by the null hypothesis. In this example, $\Theta_0$ can be written as an interval $(A,B]$. What are the numbers $A$ and $B$? Similarly, we use $\Theta_1$ to denote the region of $\Theta$ defined by the alternative hypothesis. $\Theta_1$ can be written as an interval $(C,\infty)$. What is the number $C$?
>
> 2. Consider the complement $C_n$ of the rejection region: this is all the points in $(\R_\geq 0)^n$ that do not lie in $R_{\psi_n}$. Note that the dimension of $C_n$ is determined by the sample size $n$. What is the length of $C_1, C_2, C_3$?
>
> 3. Recall that the type 1 error (or error rate) of the test $\psi_n$ is the function
>    $$
>    \begin{aligned}
>    \alpha _{\psi }: \Theta _0 &\rightarrow [0,1]\\
>    \theta &\mapsto \mathbf{P}_\theta(\psi = 1)
>    \end{aligned}
>    $$
>    Where $\mathbf{P}_{\theta} = \mathsf{Unif}[0,\theta],$ and $\mathbf{P}_\theta (\psi_n = 1)$ is the probability of the event $\{\psi_n=1\}$ under the probability distribution $\mathbf{P}_\theta$ when $\theta \in \Theta_0$. i.e. the probability of rejecting $H_0$ when $H_0$ is true.
>
>    What is $\alpha_{\psi_n}(\theta)$?
>
> **Answer**: 
>
> $1.\quad A = 0, B = 1/2, C=1/2.\\2.\quad C_1 = 1/2, C_2 = 1/4, C_3 = 1/8.\\3.\quad 0.$
>
> **Solution**: 
>
> 1) The parameter space is $\Theta = \{\theta: \theta > 0\}$. Since the null hypothesis is $H_0:\theta \leq 1/2$, then $\Theta_0 = (0,1/2]$. Similarly, $\Theta_1 = (1/2, \infty)$.
>
> 2) The complement $C_n$ of the rejection region is the set of all $(x_1, \ldots , x_ n) \in \mathbb {R}_{\geq 0}^ n$ such that $\max _{1 \leq i \leq n} x_ i \leq 1/2$. (Equivalently, it is the set of all $(X_1, ..., X_n)$) such that $\psi _ n = \mathbf{1}(\displaystyle \max _{1 \leq i \leq n} x_ i > 1/2) = 0$. The region defined by the constraint $x_i \leq 1/2$ for all $1 \leq i \leq n$ is the set $[0,1/2]^n$.
>
> In one dimension, this is the interval $[0,1/2]$ which has length $1/2$. In two dimensions, this is the square $[0,1/2]\times [0,1/2]$, which has area $(1/2)^2 = 1/4$. Finally in three dimensions, $C_3$ is a cube $[0,1/2] \times [0,1/2] \times [0,1/2]$, which has volume $(1/2)^3 = 1/8$.
>
> 3)  By definition,
>$$
> \alpha _{\psi _ n}(\theta ) = P_\theta (\max _{1 \leq i \leq n} X_ i > 1/2)
>$$
> Where $P_\theta = \text {Unif}[0, \theta ]$ and we restrict $\theta \in \Theta_0 = \{\theta: \theta \leq 1/2\}$. Observe that if $\theta \leq 1/2$, then there is a $0\%$ chance of generating an observation which is larger than $1/2$. Hence, the type 1 error $\alpha_{\psi_n}(\theta)$ is 0 for all $\theta \in \Theta_0$.
>
> **Remark:** In general, the type 1 error will be a function of $\theta$ , but in this special case it is constant.

## 10. Level of statistical test

"Level" is a very important notion. When building a test, we say “build a test at level $\alpha$.” 

* A test $\psi$ has level $\alpha$ if
  $$
  \alpha_{\psi}(\theta) \leq \alpha, \quad \forall\theta \in \Theta_0.
  $$

* A test $\psi$ has asymptotic level $\alpha$ if
  $$
  \alpha_\psi(\theta) \leq \alpha, \quad \forall \theta \in \Theta_0.
  $$
  Where $\alpha _{\psi }=\mathbf{P}_\theta (\psi =1)$ is the type 1 error. We will use the word "level" to mean the "smallest" such level, i.e. the least upper bound of the type 1 error, defined as follows
  $$
  \alpha = \text {sup}_{\theta \in \Theta _0} \alpha _{\psi }(\theta )
  $$
  Here, $\text {sup}_{\theta \in \Theta _0} $ stands for the supremum over all values of $\theta$ within $\Theta_0$. If $\Theta_0$ is a closed (*resp*. closed half-interval), and if $\alpha_\psi(\theta)$ is continuous (*resp*. continuous and decreasing as it approaches infinity), then its supremum equals the maximum.

* In general, a test has the form
  $$
  \psi = \mathbf{1} \{ T_n > c\},
  $$
  For some statistic $T_n$ and threshold $c\in \R$.

* $T_n$ is called the test statistic. The rejection region is $\R_\psi= \{T_n>c\}$.

> #### Exercise 38 Type 2 error
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Unif}[0, \theta ]$ for an unknown parameter $\theta$ and we designed the statistical test
> $$
> \psi _ n = \mathbf{1}(\displaystyle \max _{1 \leq i \leq n} X_ i > 1/2)
> $$
> To decide between the null and alternative hypotheses
> $$
> H_0: \theta \leq 1/2\\H_1: \theta > 1/2
> $$
>
> 1. Evaluate $\displaystyle \mathbf{P}_{\theta }(\psi _ n = 0)=\mathbf{P}_{\theta } \left(\max _{1 \leq i \leq n} X_ i \leq 1/2\right)$ at $\theta = 1/2$, the boundary between $\Theta_0$ and $\Theta_1$. In other words, what is $\mathbf{P}_{\theta =1/2} \left(\max _{1 \leq i \leq n} X_ i \leq 1/2\right)$?
>
> 2. In this example, $\Theta_1 = (1/2, \infty)$, and $\mathbf{P}_\theta = \mathsf{Unif}[0,\theta]$. What is $\beta_{\psi_n}(\theta), \lim\limits_{\theta \rightarrow 1/2} \beta_{\psi_n}(\theta),$ and $\lim\limits_{\theta \rightarrow \infty} \beta_{\psi_n}(\theta)$?
>
> 3. What is the power $\pi_{\psi_n}$?
>
> 4. Do the following
>
>    * Place a vertical line at the boundary of $\Theta_0$ and $\Theta_1$.
>    * Sketch the graph of $\mathbf{P}_\theta(\psi_n=1)$ as a function of $\theta$ in black.
>    * Sketch the graph of the type 1 error $\alpha _{\psi _ n}(\theta )$ in yellow.
>    * Sketch the graph of the type 2 error $\beta _{\psi _ n}(\theta )$ in blue.
>
> 5. What is the smallest level $\alpha$ of the test $\psi_n$ ?
>
> 6. How should the threshold of the test be changed to increase the smallest level $\alpha$? In other words, consider tests of the form
>    $$
>    \psi _{n,{{C}} } = \mathbf{1}(\displaystyle \max _{1 \leq i \leq n} X_ i >{{C}}  )
>    $$
>    where $C$ is the threshold. In the original test above, $C=1/2$. What should the value of $C$ be so that the level of $\psi_{n,C}$ is greater than the level of the $\psi_{n,1/2}$?
>
> 7. Determine the smallest threshold $C$ such that the test $\psi_{n,C}$ has level $\alpha$.
>
> **Answer**: 
>
> $1.\quad 1.\\2. \quad \left({1/2\over \theta}\right)^2,\quad 1,\quad 0. \\ 3. \quad 0.\\ 4.$
>
> ![lec6-ex38](../assets/images/lec6-ex38.png)
>
> $5. \quad 0.\\6. \quad C < 1/2.\\7.\quad C=\frac{1}{2}\sqrt[n]{1-\alpha }$
>
> **Solution**:
>
> 1. 
>
> $$
> \begin{aligned}
>  \beta _{\psi _ n}(1/2) &= \mathbf{P}_{1/2}(\displaystyle \max _{1 \leq i \leq n} X_ i < 1/2)\\
>  &= \mathbf{P}_{1/2}(X_1 < 1/2) \ldots \mathbf{P}_{1/2}(X_ n < 1/2)\\
>  &=1 \times 1 ... \times 1 = 1 
> \end{aligned}
> $$
> Where we applied independence of the $X_i's$ in the second line.
>
> 2) For any $\theta \in \Theta_1 = [1/2, \infty),$
> $$
> \begin{aligned}
> \beta _{\psi _ n}(\theta ) \, =\,  \mathbf{P}_{\theta }(\psi _ n=0) & = \mathbf{P}_{\theta }\left(\displaystyle \max _{1 \leq i \leq n} X_ i < 1/2\right)\,\\
> &=\mathbf{P}_{\theta }(X_1 < 1/2) \ldots \mathbf{P}_{\theta }(X_ n < 1/2) = \left(\frac{1/2}{\theta }\right)^ n.
> \end{aligned}
> $$
> As $\theta \rightarrow 1/2,$
> $$
> \beta _{\psi _ n}(\theta )\to \left(\frac{1/2}{1/2}\right)^ n=1.
> $$
> As $\theta \rightarrow \infty$,
> $$
> \beta _{\psi _ n}(\theta )= \left(\frac{1/2}{\theta }\right)^ n\to 0.
> $$
> **Remark**: This test is rather extreme example in that it minimizes type-1 error while maximizing the type-2 error. In general, we want to design tests so that the type-1 and type-2 error are both controlled. These types of trade-offs are crucial to consider in the context of hypothesis testing.
>
> 3)  We computed above that $\beta _{\psi _ n}(1/2) = P_{0.5}[\psi _ n = 0] = 1$. Thus $1- \beta _{\psi _ n}(1/2) = 0$.
>
> Moreover,
> $$
> \pi _{\psi _ n} = \inf _{\theta \in [1/2, \infty )} (1 - P_\theta (\psi _ n = 0)) = \inf _{\theta \in [1/2, \infty )} P_\theta (\psi _ n = 1) \geq 0.
> $$
> Thus, $\pi_{\psi_n} = 0.$
>
> **Remark**: The power of a test is the **largest lower bound** on the probability that if $H_1$ is true, that indeed $H_0$ is rejected in favor of $H_1$. In this example, as $\theta \in \Theta_1$ approaches the boundary $1/2$, the probability of rejecting $H_0$ decreases and approaches $0$. As $\theta \in \Theta_1$ approaches infinity, $P_\theta (\psi _ n = 1) $ increases.
>
> 5)  Since the type 1 error $\alpha _{\psi _ n}(\theta )$ is constantly zero over $\Theta_0$, the smallest level of this test $\psi$ is $\alpha = 0$.
>
> 6) To increase the smallest level $\alpha$ from $0$, note that $\mathbf{P}_\theta \left(\max\limits_{1 \leq i \leq n} X_ i >C\right)=0$ if and only if $\theta \leq C$. This means the constant zero region of graph of $\mathbf{P}_\theta \left(\psi _ C\right)=0$ shifts to the right as $C$ increases from $1/2$, and to the left as $C$ decreases from $1/2$. Since the maximum of type 1 error occurs at the boundary $\theta = 1/2$, this means $C< 1/2$ is required for the level to be positive.
>
> **Remark:** The reason behind increasing the level in this example is to increase the power of the test from $0$. In general, one of the first requirements of a test is to have a small-enough level so that the probability of concluding a false positive, (i.e. rejecting the null while the null is true) is controlled.
>
> 7) Following similar computation as in a previous problem where $C = 1/2$, we have $\mathbf{P}_{\theta }(\psi _{n,C}=1)\, =\, 1-\left(\frac{C}{\theta }\right)^ n$.  
>
> Note that
> $$
> P(\max_i X_i > C) = 1 - P(\max_i X_i < C) = 1 - (P_\theta(X_i < C))^n
> $$
> And the level $\alpha$ is
> $$
> \alpha _{\psi }=\mathbf{P}_\theta (\psi =1)
> $$
> The smallest level is 
> $$
> \begin{aligned}
> \alpha &= \max _{\theta \in \Theta _0} p_{\theta }(\psi _{n,C}=1)\\
> &= p_{1/2}(\psi _{n,C}=1)\, =\, 1-\left(\frac{C}{1/2}\right)^ n
> \end{aligned}
> $$
> A test with threshold $C=\frac{1}{2}\sqrt[n]{1-\alpha }$ or smaller will have level $\alpha$.
>
> **Remark**: Notice the threshold $C$ depends on $n,\alpha$, as well as the value of $\theta$ at the boundary of $\Theta_0$ and $\Theta_1$.

## 11. One-sided vs two-sided tests

We can refine the terminology when $\theta \in \Theta \subset \R$ and $H_0$ is of the form
$$
H_0:\theta = \theta_0 \iff \Theta_0 = \{\theta_0\}
$$

* If $H_1: \theta \neq \theta_0$: two-sided test
* If $H_1:\theta > \theta_0$ or $H_1:\theta <\theta_0$: one-sided test

One or two sided tests will have different rejection regions.

