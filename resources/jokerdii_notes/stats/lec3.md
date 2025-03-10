# Lecture 3. Parametric Statistical Models

There are 6 topics and 7 exercises.

## 1. The goals of statistics

Trinity of statistical inference: 

* Estimation
* Confidence intervals
* Hypothesis testing

The rationale behind statistical modeling

* Let $X_1, ..., X_n$ be $n$ independent copies of $X$. The goal of statistics is to learn the **distribution** of $X$. 
* If $X \in \{0,1\}$, it is **Bernoulli** and we only have to learn the parameter $p$.
* If $X \in \{0,1,2,3,4,5,6,7\}$, each with different probabilities $\mathbf{P}(X = x)$. We have to learn 8 parameters. More parameters requires more observations.
* Or we could assume that $X - 1 \sim \mathsf{Poiss}(\lambda)$. That's only $1$ parameter $\lambda$ to learn. 

## 2. Statistical model

Let the observed outcome of a statistical experiment be a sample $X_1, ..., X_n$ of $n$ **i.i.d** random variables in some measurable space $E$ (usually $E \subset \R$) and denote by $\mathbb{P}$ their common distribution. A statistical model associated to that statistical experiment is a pair
$$
{\left(E, \{ P_\theta \} _{\theta \in \Theta }\right)}
$$
where:

* $E$ is **sample space** for $X$, i.e. a set that contains all possible outcomes of $X$,
* $(\mathbb{P_\theta})_{\theta \in \Theta}$ is a family of **probability distributions** on $E$;
* $\Theta$ is a **parameter set**, i.e. a set consisting of some possible values of $\theta$.

## 3. Types of statistical models

* We usually assume that the statistical model is **well-specified**, i.e.,  $\exist ~\theta$ such that $\mathbb{P} = \mathbb{P}_\theta$.
* This $\theta$ is called the **true parameter**, and is unknown: The aim of the statistical experiment is to check $\theta$'s properties when they have special meaning, e.g. $\theta > 2, \theta \neq 1/2...$
* The model is **parametric** when we assume that $\Theta \subset \R^d$ for some $d \geq 1$.
* The model is **nonparametric** when we have $\Theta$ be **infinite dimensional**.
* The model is **semiparametric** if $\Theta = \Theta_1 \times \Theta_2$, where $\Theta_1$ is finite dimensional and $\Theta_2$ is infinite dimensional. In these models, we only care to estimate the finite dimensional parameter and the infinite dimensional one is called **nuisance parameter**. 

> #### Exercise 15
>
> Find the smallest sample space for each of the following random variables
>
> 1. $X_1 \sim \mathsf{Poiss}(\lambda)$, a **Poisson** random variable with parameter $\lambda$
> 2. $X_2\sim \mathcal{N}(0,1)$, a **standard Gaussian (or normal)** random variable with mean 0 and variance 1.
> 3. $X_3\sim \exp (\lambda )$, and **exponential** random variable with parameter $\lambda > 0$.
> 4. $X_4 \sim \mathcal{I}(Y > 0)$ where $Y$ is standard Gaussian and $\mathcal{I}$ is the **indicator function**.
>
> A. $\{0,1\}$
>
> B. $\{x \in \Z:x \geq 0\}$
>
> C. $[0,\infty)$
>
> D. $(-\infty, \infty)$
>
> **Answer**: 1-B, 2-D, 3-C, 4-A

#### Examples of parametric models

1. For $n$ Bernoulli trials:
   $$
   (\{0,1\}, (\mathsf{Ber}(p))_{p \in (0,1)})
   $$

2. If $X_1, ..., X_n \stackrel{iid}{\sim} \mathsf{Poiss} (\lambda)$ for some unknown $\lambda > 0$:
   $$
   (\N, (\mathsf{Poiss}(\lambda))_{\lambda > 0})
   $$
   
3. If $X_1, ..., X_n \stackrel{iid}{\sim} \mathcal{N}(\mu, \sigma^2)$, for some unknown $\mu \in \R$ and $\sigma^2 > 0$:
   $$
   (\R, (\mathcal{N}(\mu, \sigma^2))_{(\mu,\sigma^2) \in \R \times (0,\infty)})
   $$

4. If $X_1, .., X_n \stackrel{iid}{\sim} \mathcal{N}_d(\mu, I_d)$, for some unknown $\mu \in \R^d$:
   $$
   (\R^d, \mathcal{N}_d(\mu, I_d)_{(\mu \in \R^d)}
   $$

#### Examples of nonparametric models

1. If $X_1, ..., X_n \in \R$ are i.i.d with unknown unimodal pdf $f$:
   $$
   \begin{aligned}
   E &= \R \\ 
   \Theta &= \{\text{unimodal pdf } f\}\\
   \mathbb{P}_\theta &= \mathbb{P}_f = \text{distribution with pdf }f
   \end{aligned}
   $$

2. If $X_1, ..., X_n \in [0,1]$ are i.i.d with unknown invertible cdf $f$:
   $$
   E = [0,1]
   $$

> #### Exercise 16
>
> Let $\mathcal{U}([0,a])$ denote the uniform distribution on the interval $[0,a]$. Let $X_1,…,X_n\stackrel{iid}{∼}\mathcal{U}([0,a])$ for some unknown $a>0$. Which one of the following is *not* a statistical model associated with this statistical experiment?
>
> A. $\left([0,a],\left(\mathcal U([0,a])\right)_{a > 0}\right)$
>
> B. $\left(\mathbb {R}_{+},\left(\mathcal U([0,a])\right)_{a > 0}\right)$
>
> **Answer**: A.
>
> **Solution**: $\left([0,a],\left(\mathcal U([0,a])\right)_{a > 0}\right)$ is not a statistical model because the sample space depends on an unknown parameter $a$. $\left(\mathbb {R}_{+},\left(\mathcal U([0,a])\right)_{a > 0}\right)$ is a statistical model because for any value of $a$, the random variables $X_1,…,X_n$ will have sample space contained in the interval $[0,∞)=R_+$.

> #### Exercise 17
>
> Which of the following statistical models are parametric?
>
> A. $E=\{x \in \Z: x \geq 0\}; \{P_\theta\}_{\theta \in \Theta}$ is the set of all probability distributions with the sample space $\{x \in \Z:x \geq 0\}$.
>
> B. $E = \{0,1\}l \{P_\theta\}_{\theta \in [0,1]} = \{\mathsf{Ber}(\theta)\}_{\theta \in [0,1]}$
>
> C. $E = (-\infty, \infty); \{P_{\sigma^2}\}_{\sigma^2 \in (0,\infty)}$ is the set of all centered (mean 0) Gaussian distributions $\mathcal{N}(0, \sigma^2)$ where $\sigma^2 > 0$.
>
> D. $E = \{1,2,3,4\}; \{P_{(p_1, p_2,p_3,p_4)}\}_{(p_1, p_2,p_3,p_4) \in S}$ is defined in terms of 
>
> * $S$: the set of all $(p_1, p_2, p_3, p_4) \in \R^4$ such that $0 \leq p_i \leq 1$ for all $i=1, ..., 4$ and $\sum^4_{i=1} p_i = 1$
> * $P_{(p_1, p_2,p_3,p_4)}:$ the distribution defined by setting the probability of outcome $i $ to be $p_i$.
>
> E. $E \, =\,  (-\infty , \infty ); \{ P_{(\mu , \sigma ^2)}\} _{(\mu , \sigma ^2) \in \mathbb {R} \times (0, \infty )}$ is the set of all Gaussian distribution $\mathcal{N}(\mu, \sigma^2)$ where $\mu \in \R$ and $\sigma^2 > 0$.
>
> F. $E = (0,\infty); \{ P_\theta \} _{\theta \in [0, \infty )} = \{ \mathcal{U}([0, \theta ])\} _{\theta \in (0, \infty )}$ is the set of all uniform distributions on the interval $[0,\theta]$ with $\theta > 0$
>
> G. $E=[0,1]; \{ P_\theta \} _{\theta \in \Theta }$ is the set of all probability distributions given by a probability density function $f:\R \rightarrow \R$ with $f$ continuous and $\int _{0}^1 f(x) \,  dx = 1$.
>
> **Answer**: BCDEF
>
> **Solution**: 
>
> A specifying the distribution requires us to know the probability of the outcome $i$ for all $i∈\Z$ such that $i≥0$. An infinite amount of information (or unknowns) is required, so this statistical model is non-parametric.
>
> BCF all require just a single unknown to specify the distribution. These models are parametric.
>
> D requires three unknowns to specify the distribution (once $p_1,p_2$, and $p_3$ are specified, $p_4$ is uniquely determined). This model is parametric.
>
> E requires only the specification of the mean and variance, so it is also parametric.
>
> G: the space of continuous density functions cannot be specified by a finite amount of information; we need to know the values of the function on an infinite subset of $[0,1]$ to be able to uniquely determine it. Hence, this statistical model is also non-parametric.

#### Statistical Model for a Censored Exponential

Let $X$ denote an **exponential** random variable with unknown parameter $λ>0$. Let $Y=\mathcal{I}(X>5)$, the indicator that $X$ is larger than $5$. 

We think of $Y$ as a **censored** version of the Exponential random variable $X$: we cannot directly observe $X$, but we are able to gather some information about it (in this case, whether or not $X$ is larger than 5.)

Observe that $Y$ is a **Bernoulli** random variable. Thus, the statistical model for $Y$ can be written $(\{ 0,1\} , \{ \text {Ber}(f(\lambda ))\} _{\lambda > 0})$ for some function $f$ for $\lambda$.  

- What is $f(\lambda)$?  $f(\lambda) = e^{-5\lambda}$.

We need to compute the probability that $X > 5$. Recall that the density of $\mathsf{Exp}(\lambda)$ is given by $\lambda e^{-\lambda x}$. we need to compute
$$
P(X > 5) = \int _{5}^\infty \lambda e^{- \lambda x} \,  dx = e^{-5 \lambda }.
$$
We conclude that if $X \sim \text {Exp}(\lambda )$, then $Y \sim \text {Ber}(e^{-5 \lambda })$. Hence, $f(\lambda ) = e^{-5 \lambda }$.

## 5. Further examples

#### Linear regression model

$(X_1, Y_1),...,(X_n,Y_n) \in \R^d \times \R$ are i.i.d. from the linear regression model $Y_i = \beta^T X_i + \epsilon_i$, $\epsilon_i \stackrel{iid}{\sim} \mathcal{N}(0,1)$ for an unknown $\beta \in \R^d$ and $X_i \sim \mathcal{N}_d(0,I_d)$ independent of $\epsilon_i$
$$
E = \R^d \times \R, \qquad \Theta = \R^d
$$
We know $X_i \sim \mathcal{N}_d(0,I_d)$. Conditioning on $X$, the probability distribution of $Y$ is $Y_i \sim \mathcal{N}_d(x^T \beta,1)$. 

The random ordered pair $(X,Y) \subset \R^d \times \R$ is distributed as $P_\beta$ if

* $X_i \sim \mathcal{N}_d(0,I_d)$
* $Y \sim \beta ^ T X + \varepsilon$, where $\epsilon_i \stackrel{iid}{\sim} \mathcal{N}(0,1)$ and $\epsilon$ is independent of $X$.

The set $\Theta$ in the ordered pair $(E, \{  P_\beta \} _{\beta \in \Theta } )$ denotes the parameter space for this model.

> #### Exercise 18
>
> Suppose that $\beta = 1 \in \R^d$, which denotes the $d$-dimensional vector with all entries equal to 1. What is the mean and variance of $Y_1$?
>
> **Answer**: $0; 1 + d$
>
> **Solution**: 
>
> We have $Y_1$:
> $$
> Y_1 = \beta ^ T X_1 + \varepsilon _1 = \mathbf{1}^ T X_1 + \varepsilon _1 = \varepsilon _1 + \sum _{j = 1}^ d X_{1,j}.
> $$
> where $X_{i,j}$ denotes the $j$th coordinate of $X_ i \sim \mathcal{N}(0, I_ d)$. By linearity of expectation,
> $$
> \mathbb {E}[Y_1] = \mathbb {E}[\varepsilon _1] + \sum _{j = 1}^ d \mathbb {E}[X_{1,j}] = 0
> $$
> Next we compute the variance. Since $X_{1,1}, \ldots , X_{1,d}, \varepsilon _ i$ are mutually independent, the variance is additive:
> $$
> \text {Var}[Y_1] = \text {Var}[\varepsilon _1] + \sum _{j = 1}^ d \text {Var}[X_{1,j}] = 1 + d
> $$
> because $X_{1,1}, \ldots , X_{1,d}, \varepsilon _1 \stackrel{iid}{\sim } N(0,1)$.

#### Cox proportional Hazard model

$(X_1, Y_1),...,(X_n,Y_n) \in \R^d \times \R:$ the conditional distribution of $Y$ given $X = x$ has CDF $F$ of the form:
$$
F(t) = 1 - \exp \left(-\int^t_0 h(u) e^{(\beta^Tx)}du\right)
$$
where $h$ is an unknown non-negative **nuisance** function and $\beta \in \R^d$ is the parameter of interest.

## 6. Identifiability

#### Injectivity

The notation $f: S \rightarrow T$ denotes that $f$ is a function, also called a **map**, defined on all of a set $S$ and whose outputs lie in a set $T$. A function $f: S \rightarrow T$ is **injective** if for all $x,y \in S, f(x) = f(y)$ implies that $x = y$.

Alternatively: a function is injective if we can **uniquely** recover some input $x$ based on an output $f(x)$.

Intuitively, injectivity means if we have two parameters to start from, we are going to end up with two distributions that are different.

> #### Exercise 19
>
> Which of the following functions are injective? 
>
> A. $f_1: \R \rightarrow \R,$ given by $f_1(x)=x$.
>
> B. $f_2:\R \rightarrow \R$, given by $f_2(x) = x^2$
>
> C. $f_3:\R \rightarrow \R$, given by $f_3(x) = \sin(x)$.
>
> D. $f_4: [0,1] \rightarrow \{\text{probability distribution on } \{0,1\} \}, $ given by $f_4(p)=\mathsf{Ber}(p)$
>
> **Answer**: AD

#### Identifiability

The parameter $\theta$ is called **identifiable** iff the map $\theta \in \Theta \rightarrow \mathbb{P}_\theta$ is **injective**, i.e.,
$$
\theta \neq \theta' \implies \mathbb{P}_\theta \neq \mathbb{P}_{\theta'}
$$
Or equivalently,
$$
\mathbb{P}_\theta = \mathbb{P}_{\theta'} \implies \theta = \theta'
$$
Intuitively, if we the parameter $\theta$ is identifiable, event with an infinite number of data, we can go from $\mathbb{P}_\theta$ to $\theta$. If parameter $\theta$ is not identifiable, we could have multiple $\theta$ that give the same $\mathbb{P}$, and there is no way to decide which one is. In other words, identifiability means that, given the true distribution $P_θ$, we can uniquely recover the true parameter $θ$.

The formal mathematical way of convincing someone that the model is NOT identifiable, is to take two sets of parameters and obtain the same distribution.

**Example**: 

If $X_i = \mathcal{I}_{Y_i\geq 0}$ (indicator function), $Y_1, ..., Y_n \stackrel{iid}{\sim} \mathcal{N}(\mu, \sigma^2),$ for some unknown $\mu \in \R$ and $\sigma^2 > 0$, are unobserved: $\mu$ and $\sigma^2$ are NOT identifiable from the common distribution of the $X_i$'s.

Since $X_i \sim \mathsf{Ber}({P}(Y \geq 0))$, the probability is
$$
{P}(Y \geq 0) = {P}({Y-\mu \over \sigma} \geq - {\mu \over \sigma}) = 1 - \Phi(-{\mu \over \sigma})
$$
Thus, parameter $\theta = {\mu \over \sigma} = - \Phi^{-1}(1-p)$ is identifiable but not $\mu$ and $\sigma^2$.

Intuitively, only one parameter that determines the Bernoulli is a single $p$, we cannot split it into two numbers.

To prove that $\mu$ and $\sigma^2$ are not identifiable: create two sets of parameters ($\mu, \sigma^2$): $(1,4)$ and $(2,16)$, both have ${\mu \over \sigma} = {1\over 2}$, so these two parameters are not identifiable.

**Example**: 

The followings are all identifiable.

* One observes $n$ i.i.d. Poisson random variables with unknown parameter $λ$.

  since $\,   \mathbb E[X_ i] = \lambda  \,$.

* One observes $n$ i.i.d. exponential random variables with parameter $λ$, which is unknown but a priori known to be no larger than $10$.

  since $\,   \mathbb E[X_ i] = \lambda ^{-1}  \,$.

* One observes $n$ i.i.d. uniform random variables in the interval $[0,θ]$, where $θ$ is unknown.

  since $\,   \mathbb E[X_ i] = \theta /2  \,$.

* One observes $n$ i.i.d. Gaussian random variables with unknown parameters $μ,σ^2$.

  since $\,   \mathbb E[X_ i] = \mu  \,,   \textsf{Var}(X_ i) = \sigma ^2  \,$.

* The US Census Bureau is interested in finding out the average commute time of Bostonians. To that end, it randomly selects $n$ individuals, with replacement, among the people who work and live in the Boston area, and asks to each if their commute time is at least 20 minutes. The commute time of a random person is assumed to follow an exponential distribution with parameter $λ$.

  since what we collect can be seen as Bernoulli random variables $Y_i$ with hitting probability $p=\exp(−20λ)$, hence $λ$ can be reconstructed by $\lambda = - \frac{\log \mathbb E[Y_ i]}{20}.$

> #### Exercise 20
>
> Which of the following families of distributions has an identifiable parameter?
>
> A. $\{\mathsf{Ber}(p)\}_{p \in [0,1]}$
>
> B. $\{\mathsf{Ber}(p^2)\}_{p \in [-1,1]}$
>
> C. $\{\mathsf{Ber}(\sin(p))\}_{p \in [0,{\pi \over 2}]}$
>
> D. $\{\mathsf{Ber}(\sin(p))\}_{p \in [0,\pi]}$
>
> **Answer**: AC

> #### Exercise 21
>
> Let $X_ i = \mathcal{I}(Y_ i \geq a/2)$ where $Y_1, \ldots , Y_ n\stackrel{iid}{\sim }\mathcal U([0,a])$ for some unknown parameter $a$. We observe the independent samples $X_1, ..., X_n$ but not the $Y_i$'s themselves. Is the parameter $a$ identifiable from the common distribution of the $X_i$'s?
>
> **Answer**: No
>
> **Solution**: 
>
> $X$ is a Bernoulli random variable with parameter $p := P\left(\mathcal{I}\left(Y_ i \geq \frac{a}{2}\right) = 1\right) = P\left(Y_ i \geq \frac{a}{2}\right)$.
>
> For any choice of $a$, we have by the distribution of $Y_i$ that $p = P(Y_ i \geq a/2) = 1/2$. Hence, for any choice of $a$, the random variable $X$ is distributed as $\text {Ber}(1/2)$. The parameter $a$ is not identifiable.

