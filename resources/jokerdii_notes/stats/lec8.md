# Lecture 8. Distance Measures Between Distribution

In previous examples, we intuitively use $\hat{p}=\bar{X}_n$, since by LLN, $p = \mathbb{E}[X]$. But what if $\theta \neq \mathbb{E}[X]$?

* Maximum likelihood estimation: a generic approach with every good properties
* Method of moments: a (fairly) generic and easy approach
* M-estimators: a flexible approach, close to machine learning.

There are 9 topics and 6 exercises.

## 1. Total Variation Distance

Let $(E, (\mathbf{P}_\theta)_{\theta \in \Theta})$ be a statistical model associated with a sample of i.i.d. r.v. $X_1, ..., X_n$. Assume that there exists $\theta^* \in \Theta$ such that $X_1 \sim \mathbf{P}_{\theta^*} : \theta^*$ is the **true** parameter.

**Statistical's goal**: 

Given $X_1, ..., X_n$, find an estimator $\hat{\theta} = \hat{\theta}(X_1, ..., X_n)$ such that $\mathbf{P}_{\hat{\theta}}$ is close to $\mathbf{P}_{\theta^*}$ for the true parameter $\theta^*$.

This means: $\left\vert\mathbf{P}_{\hat{\theta}}(A) - \mathbf{P}_{\theta^*}(A) \right\vert$ is small for all $A \subset E$.

**Definition of** **Total Variation Distance**:

The total variation distance between two probability measures $\mathbf{P}_{\theta }$ and $\mathbf{P}_{\theta'}$ is defined by
$$
\text {TV}(\mathbf{P}_{\theta }, \mathbf{P}_{\theta '})={\max _{A \subset E}}\, \big |\mathbf{P}_{\theta }(A)-\mathbf{P}_{\theta '}(A)\big |\,
$$
**Interpretation**:

By analyzing the data, we are able to produce an estimator $\hat{\theta}$ such that the distributions $\mathbf{P}_{\theta }$ and $\mathbf{P}_{\theta'}$ are close in total variation distance, More precisely,  
$$
\text {TV}(\mathbf{P}_{\hat{\theta }}, \mathbf{P}_{\theta ^*}) \leq \epsilon ,
$$
where $\epsilon$ is a very small positive number.

We conclude that

* Let $A$ be an event, then $|\mathbf{P}_{\theta ^*}(A) - \mathbf{P}_{\hat{\theta }}(A)| \leq \epsilon$.
* Let $X \sim \mathbf{P}_{\theta ^*}$, let $Y \sim \mathbf{P}_{\hat{\theta }}$, and suppose $a, b \in \R$ where $a \leq b$. Then $|\mathbf{P}_{\theta ^*}(a \leq X \leq b ) - \mathbf{P}_{\hat{\theta }}(a \leq Y \leq b)| \leq \epsilon$.

## 2. Total Variance Distance Between Discrete Measures

Assume that $E$ is discrete (i.e., finite or countable). This includes Bernoulli, Binomial, Poisson...

Therefore $X$ has a PMF: $\mathbf{P}_\theta(X = x) = p_\theta(x)$ for all $x \in E$,
$$
p_\theta(x) \geq 0, \quad \sum_{x \in E} p_\theta(x)=1.
$$
The total variation distance between $\mathbf{P}_\theta$ and $\mathbf{P}_{\theta'}$ is a simple function of the PMF's $p_\theta$ and $p_{\theta'}$:
$$
\text {TV}(\mathbf{P}_\theta, \mathbf{P}_{\theta'}) = {1\over 2} \sum_{x \in E}\left\vert p_{\theta}(x) -  p_{\theta'}(x) \right\vert.
$$

**Prove there exists $A$ such that**
$$
|\mathbf{P}_\theta(A) - \mathbf{P}_{\theta'}(A)| = {1\over 2} \sum\limits_{x \in E} |p_\theta(x) - p_{\theta'}(x)|
$$
Let $A = \{x \in E, \quad p_\theta(x) \geq p_{\theta'}(x)\}$, 
$$
\sum_{x:\,\, p_\theta(x) \geq p_{\theta'}(x)} |p_\theta(x) - p_{\theta'}(x)| = |\mathbf{P}_\theta(A) - \mathbf{P}_{\theta'}(A)|
$$
Let $A = \{x \in E, \quad p_\theta(x) < p_{\theta'}(x)\}$,
$$
\sum_{x:\,\, p_\theta(x) < p_{\theta'}(x)} |p_\theta(x) - p_{\theta'}(x)| = \mathbf{P}_\theta(A^c) - \mathbf{P}_{\theta'}(A^c) = \mathbf{P}_{\theta'}(A) - \mathbf{P}_{\theta}(A) = | \mathbf{P}_{\theta}(A) - \mathbf{P}_{\theta'}(A)|
$$
Combined together and we get
$$
\sum_{x \in E} |p_\theta(x) - p_{\theta'}(x)| = 2|\mathbf{P}_\theta(A) - \mathbf{P}_{\theta'}(A)|\\
{1\over 2}\sum_{x \in E} |p_\theta(x) - p_{\theta'}(x)| = |\mathbf{P}_\theta(A) - \mathbf{P}_{\theta'}(A)|\\
$$

> #### Exercise 44
>
> 1. Let $X \sim \mathbf{P} = \mathsf{Ber}(1/2)$ and $Y \sim \mathbf{Q} = \mathsf{Ber}(1/2)$. What is $\, \text {TV}(\mathbf{P},\mathbf{Q})\,$, the total variation distance between the distributions of the Bernoulli random variables $X$ and $Y$?
> 2. Let $X \sim \mathbf{P} = \mathsf{Ber}(1/2)$ and $Y \sim \mathbf{Q} = \mathsf{Ber}(1/3)$. What is $\, \text {TV}(\mathbf{P},\mathbf{Q})\,$, the total variation distance between the distributions of the Bernoulli random variables $X$ and $Y$?
>
> **Answer**: 
>
> $1. \quad 0;\\2. \quad 0.16667.$
>
> **Solution**:
>
> 1. Intuitively, since $X$ and $Y$ have the same distribution, we expect the (total variation) distance between their distributions to be $0$. Observe that for any event, $\mathbf{P}(A) = \mathbf{Q}(A)$ since $\mathbf{P}$ and $\mathbf{Q}$ are both $\mathsf{Ber}(1/2)$.
>    $$
>    \text {TV}(\mathbf{P}, \mathbf{Q}) = \max _{A \subset E} |\mathbf{P}(A) - \mathbf{Q}(A)| = 0.
>    $$
>    Note that the distance between two distributions only depends on the distributions themselves and *not* their relation to each other (the joint distribution). This is why assuming $X$ and $Y$ are independent (or not) does not affect the total variation distance.
>
> 2. The sample space of $X$ and $Y$ is $\{0,1\}$. Let $f$ be the PMF of $X$ and let $g$ be the PMF of $Y$. Note that $f(1) = f(0) = 1/2$ and  $g(1)=1/3, g(0)=2/3$. Hence, we can apply the given formula:
>    $$
>    \begin{aligned}
>    \text {TV}(\mathbf{P}, \mathbf{Q})&= \frac{1}{2} \sum _{x \in E} |f(x) - g(x)|\\
>    &=\frac{1}{2} (|f(0) - g(0)| + |f(1) - g(1)|)\\
>    &=\frac{1}{2} ( 1/6 + 1/6 ) = 1/6 \approx 0.16667.
>    \end{aligned}
>    $$
>    **Remark**: In general, we have the formula
>    $$
>    \text {TV}(\text {Ber}(p), \text {Ber}(q)) = |p - q|.
>    $$

## 3. Total Variance Distance for Continuous Distributions

Assume that $E$ is continuous. This includes Gaussian, Exponential, ....

Assume that $X$ has a density $\mathbb{P}_\theta(X \in A) = \int_A f_\theta(x)dx$ for all $A \subset E$.
$$
f_\theta(x) \geq 0, \quad \int_E f_\theta(x) dx = 1.
$$
The total variation distance between $\mathbb{P}_\theta$ and $\mathbb{P}_{\theta'}$ is a simple function of the densities $f_\theta$ and $f_{\theta'}$
$$
\text {TV}(\mathbb{P}_\theta, \mathbb{P}_{\theta'}) = {1\over 2} \int_{x \in E} |f_\theta(x) - f_{\theta'}(x)|dx
$$
**Graphical interpretation to total variation**

Let $X \sim \mathbf{P}$ and $Y \sim \mathbf{P}$ be Gaussian random variables with mean $0$. Let $f$ denote the probability density function of $X$ and $g$ denote the density of $Y$. The graphical interpretation of $2\text {TV}(\mathbf{P}, \mathbf{Q})$ is

![images_u3s1_areabetweencurves](../assets/images/images_u3s1_areabetweencurves.svg)

## 4. Properties of Total Variation Distance

* Symmetric: $\text{TV}(\mathbf{P}_\theta, \mathbf{P}_{\theta'})=\text{TV}(\mathbf{P}_{\theta'},\mathbf{P}_\theta)$
* Positive: $0 \leq \text{TV}(\mathbf{P}_\theta, \mathbf{P}_{\theta'}) \leq 1$
* Definite: If $\text{TV}(\mathbf{P}_\theta, \mathbf{P}_{\theta'}) = 0$ then $\mathbf{P}_\theta= \mathbf{P}_{\theta'}$ 

* Triangle inequality: $\text{TV}(\mathbf{P}_\theta, \mathbf{P}_{\theta'}) \leq \text{TV}(\mathbf{P}_{\theta}, \mathbf{P}_{\theta''}) + \text{TV}(\mathbf{P}_{\theta''}, \mathbf{P}_{\theta'})$

These imply that the **total variation is a distance between probability distributions**.

**Upper bound on TV:**

The smallest number $M$ such that $\text {TV}(\mathbf{P},\mathbf{Q})\le M$ for any probability measures $\mathbf{P,Q}$ is $1$.

Using the definition of total variation distance $\text {TV}(\mathbf{P},\mathbf{Q}) = {\max _{A \subset E}}| \mathbf{P}(A) - \mathbf{Q}(A)|,$ we can say that if the maximum is obtained using a set $A_1$ such that $\mathbf{P}(A_1) \ge \mathbf{Q}(A_1)$, then
$$
\text {TV}(\mathbf{P},\mathbf{Q}) = |\mathbf{P}(A_1) - \mathbf{Q}(A_1)| \le \mathbf{P}(A_1) \le 1.
$$

> #### Exercise 45
>
> Compute
>
> 1. $\text{TV}(\mathsf{Ber}(0.5), \mathsf{Ber}(0.1)) $
> 2. $\text{TV}(\mathsf{Exp}(1), \mathsf{Unif}(0,1)) $
> 3. $\text{TV}(X, X+a)$ For any $a\in (0,1)$, where $X \sim \mathsf{Ber}(0.5)$.
> 4. $\, \text {TV}(2\sqrt{n} (\bar X_ n-1/2),Z)\,$ , where $\, X_ i \stackrel{i.i.d}{\sim } \textsf{Ber}(0.5)$ and $Z \sim \mathcal{N}(0,1)$.
>
> **Answer**: 
>
> 1. $0.4$
> 2. $1/e$
> 3. $1$
>
> **Solution**:
>
> 1. $$
>    \begin{aligned} \text{TV}(\mathsf{Ber}(0.5), \mathsf{Ber}(0.1)) &= {1\over 2}\left[|p_{0.5}(0) - p_{0.1}(0)| + |p_{0.5}(1) - p_{0.1}(1)| \right] \\&= {1\over 2}[|0.5-0.9| + |0.5-0.1|]\\ &= 0.4 \end{aligned}
>    $$
>
> 2. Let $f$ and $g$ represent the density functions of $\mathsf{Exp}(1)$ and $\mathsf{Unif}[0,1]$, respectively. So $f(x) = e^{-x} \mathbf{1}_{( x \geq 0)}$ and $g(x) = \mathbf{1}_{(0 < x \leq 1)}$,
>    $$
>    \begin{aligned} 
>    \text{TV}(\mathsf{Exp}(1), \mathsf{Unif}(0,1)) &= {1\over 2} \int |e^{-x} \mathbf{1}_{( x \geq 0)} - \mathbf{1}_{(0 < x \leq 1)}| dx\\
>    &= {1\over 2} \int_0^1 |e^{-x}  - 1| dx + {1\over 2} \int_1^\infty |e^{-x}| dx\\
>    &= {1\over 2} \int_0^1 1- e^{-x} dx + {1\over 2} \int_1^\infty |e^{-x}| dx\\
>    &= {1\over 2} - {1\over 2} \int_0^1 e^{-x} dx + {1\over 2} \int_1^\infty e^{-x} dx\\
>    &= {1\over 2} + {1\over 2} \left. e^{-x}\right|^1_0 - {1\over 2} e^{-x}|^\infty_1\\
>    &= {1\over 2} + {1\over 2e} - {1\over 2} - (0-{1\over 2e})\\
>    &={1\over e}
>    \end{aligned}
>    $$
>    **Remark:** Even though the two distributions have different sample spaces, we can take the union of the two as the sample space for both, and integrate over it.
>
> 3. $$
>    \text{TV}(X, X+a) = |\mathbb{P}(X \in \{0,1\})  - \mathbb{P}(X + a \in \{0,1\})| = |1 - 0 | = 1
>    $$
>
> 4. By CLT, we know
>    $$
>    \sqrt n {\overline{X}_n - {1/2} \over \sqrt{1/2(1-1/2)}} = 2 \sqrt n (\overline{X} - 1/2) \xrightarrow[n \rightarrow \infty]{(d)} \mathcal{N}(0,1)
>    $$
>    However, when $\, X_ i \stackrel{i.i.d}{\sim } \textsf{Ber}(0.5)$, we have $S_n \triangleq \left\{ a_ i = 2 \sqrt{n} \left(\frac{i}{n} - \frac{1}{2}\right) \mid i = 0, 1, \dots , n\right\}$ , a set of $n+1$ point where the PMF of $2\sqrt{n} (\bar X_ n-1/2)$ is non-zero. So that $\mathbf{P}(Z \in S_n) = 0$ since a continuous random variable's probability to take values in a finite set is $0$ , and $\mathbf{P}(2\sqrt{n} (\bar X_ n-1/2) \in Sn) = 1$. 
>
>    Therefore, $|\mathbf{P}(A) - \mathbf{Q}(A)| = 1$ and $\text {TV}(2\sqrt{n} (\bar X_ n-1/2),Z)=1$.

## 5. Kullback-Leibler (KL) Divergence

There are many distances between probability measures to replace total variation. One is KL Divergence.

**Definition of Kullback-Leibler (KL) Divergence:**

Let consider $\mathbf{P}$ and $\mathbf{Q}$ be both **discrete** or **continuous** probability distributions with PMFs or PDFs $p$ and $q$ respectively. Let's also assume $\mathbf{P}$ and $\mathbf{Q}$  have a common sample space $E$ . Then the *KL divergence* (also known as *relative entropy* ) between $\mathbf{P}$ and $\mathbf{Q}$ is defined by
$$
KL(\mathbf{P},\mathbf{Q} ) = \begin{cases} \sum\limits _{x \in E} p(x) \ln \left( \frac{p(x)}{q(x)} \right), &\text{if E is discrete} \\{{\int }} _{x \in E} p(x) \ln \left( \frac{p(x)}{q(x)} \right) dx, & \text{if E is continuous} \end{cases}
$$
where the sum is only over the support of $\mathbf{P}$.  Note that $\mathbf{P}$ can be written as $\mathbb{P}_\theta$, $\mathbf{Q}$ can be written as $\mathbb{P}_{\theta'}$ 

> **Why do we sum only over the support of $\mathbf{P}$?**
>
> At any point $x \in E$ outside the support of $\mathbf{P}$ but where $q(x) \neq 0$:
> $$
> \begin{aligned}
> \lim _{p/q\to 0^+}q\left(\frac{p}{q}\right) \ln \left(\frac{p}{q}\right) &= q \lim _{p/q\to 0^+}\left(\frac{p}{q}\right) \ln \left(\frac{p}{q}\right)\\
> &= q \cdot (0) \quad  \text{(by L'hopital's rule)}
> \end{aligned}
> $$

> #### Exercise 46
>
> Let $X \sim \mathbf{P}_ X = \text {Ber}(1/2)$ and let $Y \sim \mathbf{P}_ Y = \text {Ber}(1/2)$. What is $\text {KL}(\mathbf{P}_ X, \mathbf{P}_ Y)$?
>
> **Answer**: $1$
>
> **Solution**:
>
> Let $p$ be the PMF of the distribution $\mathsf{Ber}(1/2)$. Note that the sample space is the discrete set $E = \{0,1\}$. Then
> $$
> \begin{aligned}
> \text {KL}(\mathbf{P}_ X, \mathbf{P}_ Y) &= p(1) \ln (p(1)/p(1)) + p(0) \ln (p(0)/p(0))\\
> &= (1/2) \ln (1) + (1/2) \ln (1) = 0.
> \end{aligned}
> $$
> Note that the result is consistent with the second property.

**Properties:**

* **In general:** $\text {KL}(\mathbf{P}, \mathbf{Q}) \neq \text {KL}(\mathbf{Q}, \mathbf{P}) $ [ **Asymmetric** ]
* **Non-negative**: $\text {KL}(\mathbf{P}, \mathbf{Q}) \geq 0$
* **Definite**: $\text {KL}(\mathbf{P}, \mathbf{Q}) = 0$ only if $\mathbf{P}$ and $\mathbf{Q}$ are the same distribution, i.e., $\mathbf{P}=\mathbf{Q}$.
* **In general:** $\text {KL}(\mathbf{P}, \mathbf{Q}) \nleq \text {KL}(\mathbf{P}, \mathbf{R}) + \text {KL}(\mathbf{R}, \mathbf{Q}) $

Not a distance.

This is called a divergence.

Asymmetry is the key to our ability to estimate it.

$\theta^*$ Is the unique minimizer of $\theta \mapsto \text{KL}(\mathbb{P}_{\theta^*}, \mathbb{P}_\theta)$.

> **Why does the KL divergence take only non-negative values?**
>
> Here is the proof of the positive semi-definiteness of the KL-divergence. For simplicity, we only prove the case when the two distributions are given by pdfs.
>
> $\text {KL}(\mathbf{P}_{X}, \mathbf{P}_{Y})\geq 0$ for all distributions $\mathbf{P}_ Y$ and $\mathbf{P}_ X$ (positive semi-definiteness).
>
> **Proof.** The main idea is to use **Jensen's inequality**.
>
> Let $p_X, p_Y$ (with suitable condition) be the PDFs defining the distribution $\mathbf{P}_X$ and $\mathbf{P}_Y$ respectively. Define another random variable $Z = {p _Y(X)\over  p_X(X)}$, which is a function of the random variable $X$. Observe that the function $-\ln$ is convex, then Jensen's inequality gives
> $$
> \begin{aligned}
> \text {KL}\left(\mathbf{P}_{X}, \mathbf{P}_{Y}\right)\, &=\, \mathbb E_ X\left[-\ln (Z)\right]  \geq -\ln \left(\mathbb E_ X[Z]\right)\qquad (\text {Jensen's Inequality})\\
> &= -\ln \left(\mathbb E_ X\left[\frac{p_{Y}(X)}{p_{X}(X)}\right]\right)\\
> &\geq -\ln(1) = 0
> \end{aligned}
> $$

## 6. Estimating KL Divergence

$$
\begin{aligned}
\text{KL}(\mathbb{P}_{\theta^*},\mathbb{P}_{\theta}) &= \mathbb{E}_{\theta^*}\left[ \log\left( {p_{\theta^*}(X) \over p_\theta(X)}\right) \right]\\
&= \mathbb{E}_{\theta^*}[\log p_{\theta^*}(X)] - \mathbb{E}_{\theta^*}[\log p_\theta(X)]
\end{aligned}
$$

So the function $\theta \mapsto \text{KL} (\mathbb{P}_{\theta^*},\mathbb{P}_{\theta})$ is of the form: (since the first term dose not depend on $\theta$.)
$$
\text{"constant"} - \mathbb{E}_{\theta^*}[\log p_\theta(X)]
$$
Can be estimated: $\mathbb{E}_{\theta^*}[h(X)] \rightarrow {1\over n} \sum^n_{i=1}h(X_i)$ (by LLN)
$$
\widehat{\text{KL}}(\mathbb{P}_{\theta^*},\mathbb{P}_{\theta}) = \text{"constant"} - {1\over n} \sum^n_{i=1} \log p_\theta(X_i)
$$
Therefore, as shown above, while we cannot find $\theta$ that minimizes $\text {KL}(P_{\theta ^*}, P_\theta )$, we can find $\theta$ that minimizes $\widehat{\text{KL}}(\mathbb{P}_{\theta^*},\mathbb{P}_{\theta}) $.

**Remark:**

Note that in general, it is **easier to build an estimator for the KL divergence than it is to build an estimator for the total variation distance**. The total variation distance is not an expectation with respect to either of the probability measures. Therefore there is no natural way to estimate it without requiring an estimate of the true parameter $\theta^*$. The KL divergence, by contrast, is an expectation of some function with respect to one of the probability measures. This means that it can be estimated naturally by replacing the expectation with a sample average. Note that this application of the law of large numbers does not require knowledge of the true parameter value, only a random sample generated from the true distribution.

## 7. Parameter Estimation via KL Divergence - Maximum Likelihood

$$
\widehat{\text{KL}}(\mathbb{P}_{\theta^*},\mathbb{P}_{\theta}) = \text{"constant"} - {1\over n} \sum^n_{i=1} \log p_\theta(X_i)\\
\begin{aligned}
\min_{\theta \in \Theta} \widehat{\text{KL}}(\mathbb{P}_{\theta^*},\mathbb{P}_{\theta}) &\iff \min_{\theta \in \Theta} - {1\over n} \sum^n_{i=1} \log p_\theta(X_i)\\
& \iff\max_{\theta \in \Theta} \log\left[ \prod_{i = 1}^n p_\theta (X_i)\right]\\
&\iff \max_{\theta \in \Theta} \prod^n_{i=1} p_\theta(X_i)
\end{aligned}
$$

This is the **maximum likelihood principle**.

The quantity 
$$
\hat{\theta }_ n := \text {maximizer of} \,  \,  \prod _{i = 1}^ n p_\theta (X_ i)
$$
is referred to as the **maximum likelihood estimator**. Note that this is the same as the estimator
$$
\hat{\theta }_ n := \text {minimizer of } \,  \,  - \displaystyle \frac{1}{n} \sum _{i = 1}^ n \ln (p_\theta (X_ i))
$$
Under certain technical conditions, the maximum likelihood estimator is guaranteed to **(weakly) converge** to the true parameter $\theta^*$.

> #### Exercise 47
>
> Consider the optimization problem in which we minimize the KL divergence between $P_{\theta ^*}$, the true distribution, and $P_{\theta}$. Formally, we want to solve
> $$
> \min _{\theta \in \mathbb {R}} \text {KL}(P_{\theta ^*}, P_{\theta }).
> $$
> We are not so much interested in the minimum value attained by the objective function $\text {KL}(P_{\theta ^*}, P_{\theta })$, but rather the value of $\theta$ where the minimum is attained. We refer to such a $\theta$ as a **minimizer**.
>
> Let's suppose that there is a unique minimizer for the above optimization problem - i.e., if $m$ is the minimum value of $\text {KL}(P_{\theta ^*}, P_{\theta })$, there is only one point $\theta_{\min}$ such that
> $$
> m = \text {KL}(P_{\theta ^*}, P_{\theta _{\min } }).
> $$
> For which $\theta$ is the minimum value of $\text {KL}(P_{\theta ^*}, P_{\theta })$ attained? (Equivalently, what is $\theta_\min$?)
>
> **Answer**: $\theta^*$
>
> **Solution**:
>
> The RHS is achieved if we set $\theta = \theta^*$: $\text {KL}(P_{\theta ^*}, P_{\theta ^*}) = 0$. Since the minimizer is unique by assumption, we conclude that the minimum value is attained at $\theta = \theta^*$.
>
> **Remark:** The assumption that there is a unique minimizer holds if we are given that the parameter $\theta$ is identified. Here is why: since KL divergence is definite, $\text {KL}(P_{\theta ^*}, P_\theta ) = 0$ if and only if $P_{\theta ^*}$ and $P_{\theta}$ are the same distribution. And if $\theta$ is identified, this implies that $\theta = \theta^*$.

## 8. Likelihood of a Discrete Distribution

Let $(E, (\mathbb{P}_{\theta \in \Theta}))$ be a statistical model associated with a sample of i.i.d. r.v. $X_1, ..., X_n$. Assume that $E$ is discrete (i.e. finite or countable).

**Definition**

The *likelihood* of the model is the map $L_n$ (or just $L$) defined as:
$$
\begin{aligned}
L_n : E^n \times \Theta &\rightarrow \R\\
(x_1,..., x_n, \theta) &\mapsto \mathbb{P}_\theta [X_1 = x_1, ..., X_n = x_n]
\end{aligned}
$$
**Example 1: Likelihood for the Bernoulli model**

If $X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Ber}(p)$ for some $p\in(0,1)$:

* $E = \{0,1\}$

* $\Theta = (0,1)$

* $\forall(x_1, ...,x_2) \in \{0,1\}^n, \quad \forall p \in (0,1)$,
  $$
  \begin{aligned}
  L(x_1,...,x_n,p) &= \prod^n_{i=1}\mathbb{P}_p[X_i = x_i]\\
  &= \prod^n_{i=1} p^{x_i} (1-p)^{1-x_i}\\
  &= p^{\sum\limits^n_{i=1}x_i} (1-p)^{n - \sum\limits^n_{i=1}x_i}
  \end{aligned}
  $$

* Alternatively, if we use the expression $f(x) = xp + (1 - x)(1 - p)$ for the PMF of $\text {Ber}(p)$, then
  $$
  L(x_1, \ldots , x_ n, p) = \prod _{i = 1}^ n \left( x_ i p + (1 - x_ i) (1 - p) \right)
  $$
  is, by definition, the likelihood. 

**Example 2: Likelihood of a Poisson Statistical Model**

If $X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Poiss}(\lambda)$ for some $\lambda > 0$:

* $E = \N$

* $\Theta = (0, \infty)$

* $\forall (x_1, ..., x_n) \in \N^n, \forall \lambda > 0$,
  $$
  L_ n(x_1, \ldots , x_ n, \lambda ) = \prod _{i = 1}^ n e^{-\lambda } \frac{\lambda ^{x_ i}}{{x_ i}!} = e^{-n \lambda } \frac{\lambda ^{\sum _{i = 1}^ n x_ i}}{x_1 ! \cdots x_ n !}.
  $$

> #### Exercise 48
>
> Let $X_1, \ldots , X_ n \stackrel{iid}{\sim } \text {Poiss}(\lambda ^*)$ for some unknown $\lambda^* \in (0,\infty)$. You construct the associated statistical model $(E, \{ \text {Poiss}(\lambda )\} _{\lambda \in \Theta })$ where $E$ and $\Theta$ are defined as in the answers to the previous question.
>
> 1. Suppose you observe two samples $X_1 = 1, X_2 = 2.$ What is  $L_2(1, 2, \lambda )$? Express your answer in terms of $\lambda$.
> 2. Next, you observe a third sample $X_3 = 3$ that follows $X_1 = 1$ and $X_2 = 2$. What is $L_3(1,2,3,\lambda)$?
> 3. Suppose your data arrives in a different order: $X_1 = 2, X_2 = 3,X_3=1$. What is $L_3(2,3,1,\lambda)$?
>
> **Answer**:
>
> 1. $L_2(1,2,\lambda ) = e^{-2 \lambda } \frac{\lambda ^{3}}{2}.$
> 2. $L_3(1,2,3,\lambda )  = e^{-3 \lambda } \frac{\lambda ^6}{12}.$
> 3. $L_3(2,3,1, \lambda ) = e^{-3 \lambda } \frac{\lambda ^6}{12}.$
>
> **Solution:**
>
> 1. Plug in $n=2,x_1=1,x_2=2$:
>    $$
>    L_2(1,2,\lambda ) = e^{-2 \lambda } \frac{\lambda ^{1 + 2}}{2! 1!} = e^{-2 \lambda } \frac{\lambda ^{3}}{2}.
>    $$
>
> 2. We can simply evaluate the density of a Poisson at the observation:
>    $$
>    P(X_3 = 3) = e^{-\lambda } \frac{\lambda ^3}{3!}, \quad X \sim \text {Poiss}(\lambda )
>    $$
>    and multiply this by the previous response:
>    $$
>    L_3(1,2,3,\lambda ) = e^{-\lambda } \frac{\lambda ^3}{3!} L_2(1,2,\lambda ) = e^{-3 \lambda } \frac{\lambda ^6}{12}.
>    $$
>    **Remark 1:** Observe that we can compute the likelihood sequentially as the data arrives, updating it in the previous fashion after each new observation.
>
> 3. Similarly,
>    $$
>    L_3(2,3,1, \lambda ) = e^{-3 \lambda } \frac{\lambda ^6}{12}.
>    $$
>    **Remark 2**: Observe that the likelihood of observations $X_1 = x_1, \ldots , X_ n =x_ n$ is independent of the *order* in which these observations arrive.

> #### Exercise 49
>
> Consider a discrete statistical model $M_1 = (\mathbb {Z}, \{ \mathbf{P}_\theta \} _{\theta \in \mathbb {R}})$, Let $p_\theta$ denote the PMF of $\mathbf{P}_\theta$. Assume that $p_\theta$ vary continuously with the parameter $\theta$ for each fixed $x \in E$. Let $x_1, ..., x_n$ be fixed natural numbers. Let $(L_1)_ n$ denote the likelihood of the discrete model $M_1$. Keeping $x_1, ..., x_n$ fixed, let's think of $(L_1)_ n(x_1, \ldots , x_ n, \theta )$ as a function of $\theta$.
>
> True of False: The map $\theta \mapsto (L_1)_ n(x_1, \ldots , x_ n, \theta )$ is a continuous function of $\theta$.
>
> **Answer**: True.
>
> **Solution**:
>
> Observe that 
> $$
> (L_1)_ n(x_1, \ldots , x_ n, \theta ) = \prod _{i = 1}^ n p_\theta (x_ i)
> $$
> We are given that $p_\theta$ is a continuous function of the parameter $\theta \in \R$. Since products of continuous functions are continuous, this implies the map is a continuous function of the parameter $\theta \in \R$.

**Likelihood Properties**:

* Symmetric: we can take the product $\prod _{i = 1}^ n p_\theta (x_ i)$ in any order, and the result will still be the same.

* Can be updated sequentially as new samples are observed.

* The likelihood of a discrete statistical model can be continuous. Considering the likelihood of a Bernoulli:
  $$
  L(x_1, \ldots , x_ n, p) = \prod _{i = 1}^ n p^{x_ i}(1 - p)^{1 - x_ i} = p^{\sum _{i = 1}^ n x_ i} (1 -p)^{n - \sum _{i = 1}^ n x_ i}.
  $$
  we can clearly see that the above varies continuously as a function of the *parameter*. This is also true for a host of other discrete models (for example, the Poisson model).

## 9. Likelihood of a Continuous Distribution

Let $(E, (\mathbb{P}_{\theta \in \Theta}))$ be a statistical model associated with a sample of i.i.d. r.v. $X_1, ...,X_n$. Assume that all the $\mathbb{P}_\theta$ have density $f_\theta$.

**Definition:**

The likelihood of the model is the map $L$ defined as:
$$
\begin{aligned}
L : E^n \times \Theta &\rightarrow \R\\
(x_1,..., x_n, \theta) &\mapsto \prod^n_{i=1} f_\theta(x_i)
\end{aligned}
$$
**Example 3: Likelihood of a Gaussian Model**

If $X_1, ..., X_n \stackrel{iid}{\sim} \mathcal{N}(\mu, \sigma^2)$, for some $\mu \in \R,\sigma^2 > 0$,

* $E = \R$
* $\Theta = \R \times (0,\infty)$

* The PDF is
  $$
  f_{\mu, \sigma^2} (x) = {1\over \sigma \sqrt{2\pi}} \exp \left(-{1\over 2\sigma^2} (x-\mu)^2 \right)\\
  $$

* $\forall (x_1, ..,x_n) \in \R^n, \quad \forall(\mu,\sigma^2) \in \R \times (0,\infty)$, the likelihood is
  $$
  L(x_1, ...,x_n; \mu, \sigma^2)=\prod^n_{i=1} f_{\mu, \sigma^2} (x_i) = {1\over (\sigma \sqrt{2\pi})^{n}} \exp\left( -{1\over 2\sigma^2} \sum^n_{i=1} (x_i - \mu)^2 \right)
  $$

**Example 4: Likelihood of an Exponential Distribution**

Let $(E, (\mathbb{P}_\theta)_{\theta \in \Theta})$ be a statistical model associated with $X_1, ...,X_n \sim \mathsf{Exp}(\lambda), \lambda > 0$.

* $E \in (0,\infty)$

* $\Theta \in (0,\infty)$

* The PDF is
  $$
  f_\lambda(x) = \lambda e^{-\lambda x}, x> 0
  $$

* The likelihood is
  $$
  \prod^n_{i=1} f_\lambda(x_i) = \lambda^n e^{-\lambda \sum\limits^n_{i=1}x_i} \prod^n_{i=1} \mathbf{1}_{x_i > 0}
  $$
  Equivalently,
  $$
  \prod^n_{i=1} f_\lambda(x_i) = \lambda^n e^{-\lambda \sum\limits^n_{i=1}x_i} \mathbf{1}_{\min\limits_i x_i > 0}
  $$

* In general, the likelihood is usually written as
  $$
  \prod^n_{i=1} f_\lambda(x_i) = \lambda^n e^{-\lambda \sum\limits^n_{i=1}x_i}
  $$
  Note that it does not matter if this indicator does not depend on the parameter.

**Example 5: Likelihood of a Uniform Distribution**

Let $(E,(\mathbb{P}_\theta)_{\theta \in \Theta})$ be a statistical model associated with $X_1,. ..,X_n \stackrel{iid}{\sim}\mathsf{Unif}[0,b]$ for some $b > 0$.

* $E \in [0,\infty)$

* $\Theta \in [0,\infty)$

* The PDF is 
  $$
  f_b(x) = {1\over b} \mathbf{1}_{(0\leq x\leq b)}
  $$

* The likelihood is 
  $$
  \begin{aligned}
  \prod^n_{i=1}f_b(x) &= {1\over b^n} \prod^n_{i=1} \mathbf{1}_{(0\leq X_i \leq b)}\\
  &= {1\over b^n} \mathbf{1}_{(\min\limits_i X_i \geq 0)} \mathbf{1}_{(\max\limits_i X_i \leq b)}
  \end{aligned}
  $$

* In general, the likelihood is usually written as
  $$
  \prod^n_{i=1}f_b(x) 
  = {1\over b^n}  \mathbf{1}_{(\max\limits_i X_i \leq b)}
  $$
