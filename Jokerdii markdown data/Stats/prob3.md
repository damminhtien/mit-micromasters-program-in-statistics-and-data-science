Problem set for Lec6-7.

# 1. True or False

Suppose the following: According to a fixed statistical model $\{\mathbf{P}_\theta\}_{\theta \in \Theta}$, a pair of hypotheses $H_0: \theta \in \Theta_0$ and $H_1 : \theta \in \Theta_1$, and a $0.05$-level test $\psi_{0.05}$ of the form
$$
\psi _{\alpha } = \mathbf{1}(T_ n > c_\alpha ), \quad T_ n = T_ n(X_1,\ldots ,X_ n), \quad c_\alpha \in \mathbb {R},
$$
We observe the sample $x_1, ..., x_n$ and compute the p-value to be $0.01$. Here $T_n$ is a test statistic, and $c_\alpha$ is a threshold constant.

For each of the following groups of statements, select the one that is necessarily true. If there is none, select "None of the above."

Which of the following is necessarily true?

a. Any test $\psi_\alpha$ that rejects $H_0$ for this observation will have a Type 1 error of at most $0.05$.

b. Any test $\psi_\alpha$ that rejects $H_0$ for this observation will have a Type 2 error of at most $0.05$.

c. Any test $\psi_\alpha$ that does not reject $H_0$ for this observation will have a Type 1 error of at most $0.01$.

d. Any test $\psi_\alpha$ that does not reject $H_0$ for this observation will have a Type 2 error of at most $0.01$.

e. None of the above.

> **Answer**: $c.$
>
> **Solution**:
>
> Note that $\psi _{0.05}(x_1,\ldots ,x_ n)=1$ since the p-value $0.01$ of this sample is lower than $0.05$, the level of the test. Thus, $T_ n(x_1,\ldots ,x_ n) > c_{0.05}$. In fact, $T_ n(x_1,\ldots ,x_ n) = c_{0.01}$ by the definition of p-value. If another test of the form $\psi _\alpha = \mathbf{1}(T_ n > C_\alpha )$ does not reject $H_0$ at the given sample $x_1, ...,x_n$, then its threshold must satisfy
> $$
> c_\alpha > T_ n(x_1,\ldots ,x_ n) = c_{0.01}.
> $$
> Since $\psi_\alpha$ has a higher threshold than $\psi_{0.01}$, we always have
> $$
> \{ T_ n > c_\alpha \}  \subset \{ T_ n > c_{0.01}\}  \quad \text {and}\quad \mathbf{P}_{\theta }\{ T_ n > c_\alpha \}  \le \mathbf{P}_{\theta }\{ T_ n > c_{0.01}\}  \quad \forall \theta \in \Theta _0 .
> $$
> Thus, its level must be $\alpha < 0.01$.
>
> On the other hand, any test of this form that reject $H_0$ for this sample will have a type 1 error rate of at least $0.01$.
>
> This problem does not provide any information about the Type 2 errors.

# 2. Hypothesis Test Using a Single Observation

Let $X$ be a single (i.e. $n =1$) Gaussian random variable with unknown mean $\mu$ and variance $1$. Consider the following hypotheses:
$$
H_0: \mu =0 \quad \text {vs} \quad H_1: \mu \neq 0.
$$

1. Define a test $\psi_\alpha:\R \rightarrow\{0,1\}$ with level $\alpha$ that is of the form
   $$
   \psi _\alpha = \mathbf{1}\{  f_\alpha (X) > 0 \} ,
   $$
   For some function $\,   f_\alpha : \mathbb {R}\to \mathbb {R} \,$.

   We want our test $\psi$ above to satisfy the following:

   * Symmetric in the value of $X$ about $0$, so $f(X)=f(-X)$.
   * Its “acceptance region" is an interval. (The **acceptance region** of a test is the region in which the null hypothesis is **not rejected**, i.e. the complement of its rejection region.)

   What's the function $f_\alpha(X)$ in terms of $\alpha$?

2. Assume you observe $X = 1.32$, and what is the value of your test $\psi_\alpha$ with level $\alpha = 0.05$?  

3. As above, what is the p-value of your test (keeping in mind the symmetry and interval requirements)? 

4. As above, what is the conclusion of the test?

> **Answer**:
>
> $1.\quad f_\alpha(X)=|X| - q_{\alpha/2};\\ 2. \quad \psi(X)=0; \\3. \quad \text{p-value} = 2 (1-\Phi(1.32))$
>
> **Solution**:
>
> 1. Since our test should be symmetric about zero and its “acceptance region" an interval, it must be of the form
>    $$
>    \psi = \mathbf{1}\{  |X| - q_{\alpha /2} > 0 \} .
>    $$
>
> 2. First, determine $q_{\alpha}$ for our test $\psi_\alpha$ when $\alpha = 0.05$:
>    $$
>    \begin{aligned}
>    \mathbf{P}_{\mu = 0}(|X| > q) &= 0.05\\
>    \implies 2(1-\Phi(q)) &= 0.05\\
>    \implies \Phi(q) &= 0.975\\
>    \implies q = q_{0.025} &\approx 1.96
>    \end{aligned}
>    $$
>    Hence, the test $\Phi_{0.05}(X) = \mathbf{1}\{f_{0.05}(X) > 0\}$ where
>    $$
>    f_{0.05}(X) = |X| - 1.96.
>    $$
>    Since $|1.32| < 1.96, \psi_{0.05} (1.32) = 0$.
>
> 3. The p-value is defined as
>    $$
>    \inf \{ \alpha : \psi _\alpha (X) = 1\} ,
>    $$
>    where
>    $$
>    \psi _\alpha (X) = \mathbf{1}\{ |X| > q(\alpha )\} .
>    $$
>    In other words, the p-value is the smallest value so that we could still reject $H_0$ given the observation, when picking our hypothesis test from a family of hypothesis tests indexed by $\alpha$. In this case, by the requirement of $\psi_\alpha$ having confidence level $\alpha$,
>    $$
>    \mathbf{P}_{\mu = 0}(\psi _\alpha (X) > q(\alpha )) = 2(1-\Phi (q)) = \alpha\\
>    \implies \Phi(q) = 1 - {\alpha \over 2}
>    $$
>    and hence
>    $$
>    q(\alpha) = q_{\alpha/2}
>    $$
>    The $1 - \alpha/2$ quantile of a Normal variable. Now, by the form of the test $\psi_\alpha$, we see that we get the infimum of $\alpha$ if $|X| = q_{\alpha/2}$, i.e., if
>    $$
>    \alpha = 2(1 - \Phi (|X|)) = 2 - 2 \Phi (1.32) \approx 0.19.
>    $$
>
> 4. We do not reject $H_0$ because there is not enough evidence for doing so. That does not necessarily mean that we think $H_0$ true, so we should not "accept" it.

# 3. Simple Testing

Let $X_1, ..., X_n$ be i.i.d. $\mathcal{N}(\theta,1)$. Consider testing
$$
H_0: \theta = 0 \quad \text { v.s. } \quad H_1: \theta = 1.
$$

1. What should a Type 1 error and a Type 2 error be in this test?
2. Suppose that the rejection region of a test $\psi$ has the form $R = \{ \overline{X}_ n : \overline{X}_ n > c\}$. Find the smallest $c$ such that $\psi$ has level $\alpha$.
3. Suppose that the test $\psi$ has level $\alpha = 0.05$. What is the power of $\psi$? What does the power of $\psi$ approach as $n \rightarrow \infty$?

> **Answer**:
>
> 1. Type 1 error is rejecting $H_0$ when $\theta = 0$. Type 2 error is not rejecting $H_0$ when $\theta = 1$.
>
> 2. $c \geq {q_\alpha \over \sqrt n}$
>
> 3. Power of $\psi:$ $1 - \Phi(q_{0.05} - \sqrt n)$
>
>    $\lim\limits_{n \rightarrow \infty}$Power$= 1$.
>
> **Solution**:
>
> 1. /
>
> 2. Since $X_i$ are Gaussian, for $\theta = 0$,
>    $$
>    \sqrt{n}\overline{X}_ n\sim \mathcal{N}(0,1).
>    $$
>    Given the rejection region $R = \{ \overline{X}_ n : \overline{X}_ n > c\}$, the corresponding test $\psi _{n,\alpha }=\mathbf{1}\left(\overline{X}_ n\in R \right)$ has level $\alpha$ for any $c$ such that
>    $$
>    \mathbf{P}_0\left(\overline{X}_ n > c\right)\, =\, \mathbf{P}_0\left(\sqrt{n}\overline{X}_ n > \sqrt{n}c\right)
>    $$
>    Hence, the smallest such $c$ is $c=\frac{q_{\alpha }}{\sqrt{n}}$.
>
> 3. Since $H_1$ consists of a single point, the type 2 error of $\psi$ is
>    $$
>    \begin{aligned}
>    \mathbf{P}_{\theta =1}(\psi =0)\, =\, \mathbf{P}_{\theta =1}\left(\overline{X}_ n\leq \frac{q_{0.05}}{\sqrt{n}}\right) &= \mathbf{P}_{\theta =1}\left(\sqrt{n}\left(\overline{X}_ n-1\right)\, \leq \,  q_{0.05}-\sqrt{n}\right)\\
>    &=\Phi \left(q_{0.05}-\sqrt{n}\right).
>    \end{aligned}
>    $$
>    Hence, the power is $1 - \Phi(q_{0.05} - \sqrt n)$. As $n \rightarrow \infty$, this goes to $1$.

# 4. Relating Hypothesis Tests and Confidence Intervals

Consider an i.i.d. sample $\,   X_1, \dots , X_ n \sim \textsf{Poiss}(\lambda ) \,$ for $\lambda > 0$.

1. Starting from the CLT, find a C.I. $I=[A,B]$ with asymptotic level $1- \alpha$ that is centered about $\overline{X}_n$ using the **plug-in** method.

2. Continuing the problem above, now consider the following hypothesis with a fixed number $\lambda_0 > 0$:
   $$
   H_0 : \lambda = \lambda _0 \quad \text {vs} \quad H_1 : \lambda \neq \lambda _0.
   $$
   Define a test for the above hypotheses with asymptotic level $\alpha$, and rewrite it in the form
   $$
   \psi = \mathbf{1}\{ \lambda _0 \notin J\} ,
   $$
   Find C.I. $J = [C,D]$ obtained through the plug-in method.

> **Answer**: 
>
> $1. \quad I = \left[ \overline{X}_ n - \frac{q \sqrt{\overline{X}_ n}}{\sqrt{n}}, \overline{X}_ n + \frac{q \sqrt{\overline{X}_ n}}{\sqrt{n}} \right];\\2. \quad J = \left[ \overline{X}_ n - \frac{q_{\alpha /2} \sqrt{\overline{X}_ n}}{\sqrt{n}}, \overline{X}_ n + \frac{q_{\alpha /2} \sqrt{\overline{X}_ n}}{\sqrt{n}} \right]$
>
> **Solution**:
>
> 1. By the CLT, 
>    $$
>    \sqrt{n} \frac{\overline{X}_ n - \lambda }{\sqrt{\lambda }} \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0,1).
>    $$
>    Since 
>    $$
>    \overline{X}_ n \xrightarrow [n \to \infty ]{\mathrm{\mathbf{P}}} \lambda ,
>    $$
>    By **Slutsky's Theorem**, we get 
>    $$
>    \sqrt{n} \frac{\overline{X}_ n - \lambda }{\sqrt{\overline{X}_ n}} \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0,1).
>    $$
>    That means for $q > 0$ that with
>    $$
>    I = \left[ \overline{X}_ n - \frac{q \sqrt{\overline{X}_ n}}{\sqrt{n}}, \overline{X}_ n + \frac{q \sqrt{\overline{X}_ n}}{\sqrt{n}} \right],
>    $$
>    we have
>    $$
>    \mathbf{P}_\lambda \left( \lambda \in I \right) \xrightarrow [n \to \infty ]{} 1 - 2 \Phi (-q).
>    $$
>    If we want this quantity to be $1 - \alpha$ to guarantee level $1-\alpha$ of the interval, that leads to
>    $$
>    \Phi (q) = 1 - \frac{\alpha }{2} \iff q = q_{\alpha /2} = \Phi ^{-1}(1 - \frac{\alpha }{2}).
>    $$
>
> 2. By setting
>    $$
>    J = I = \left[ \overline{X}_ n - \frac{q_{\alpha /2} \sqrt{\overline{X}_ n}}{\sqrt{n}}, \overline{X}_ n + \frac{q_{\alpha /2} \sqrt{\overline{X}_ n}}{\sqrt{n}} \right]
>    $$
>    From (1), the fact that $I$ is a C.I. with asymptotic level $\alpha$ means that
>    $$
>    \mathbf{P}_\lambda (\lambda \in I) \xrightarrow [n \to \infty ]{} 1 - \alpha \quad \lambda > 0,
>    $$
>    so
>    $$
>    \mathbf{P}_\lambda (\lambda \notin I) \xrightarrow [n \to \infty ]{} \alpha \quad \lambda > 0.
>    $$
>    In particular, if we set
>    $$
>    \psi = \mathbf{1}\{ \lambda _0 \notin I\} ,
>    $$
>    This means that 
>    $$
>    \mathbf{P}_{\lambda _0}(\psi = 1) = \mathbf{P}_{\lambda _0}(\lambda _0 \notin I) \xrightarrow [n \to \infty ]{} \alpha ,
>    $$
>    yielding a hypothesis test with asymptotic level $\alpha$.

# 5. P-Values Formulas

In each of the following questions, you are given an i.i.d. sample and two hypotheses. For any $\alpha \in (0,1)$ , use the Central Limit Theorem to define a test with asymptotic level $\alpha$, then give a formula for the asymptotic p-value of your test.

1. $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim } \textsf{Poiss}(\lambda )$ For some unknown $\lambda > 0$;
   $$
   H_0: \lambda = \lambda _0 \quad \text { v.s. }\quad H_1: \lambda \neq \lambda _0\qquad \text {where }\,  \lambda _0 > 0.
   $$
   What is the asymptotic p-value?

2. $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim } \textsf{Poiss}(\lambda )$ For some unknown $\lambda>0$;
   $$
   H_0: \lambda {\color{blue}{\geq }}  \lambda _0 \quad \text { v.s. } \quad H_1: \lambda {\color{blue}{<}} \lambda _0 \qquad \text {where }\,  \lambda _0 > 0.
   $$
   What is the asymptotic p-value?

3. $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim } {{\textsf{Exp}(\lambda )}}$ for some unknown $\lambda > 0$;
   $$
   H_0: \lambda =\lambda _0 \quad \text { v.s. } \quad H_1: \lambda \neq \lambda _0 \qquad \text {where }\,  \lambda _0 > 0.
   $$
   What is the asymptotic p-value?

> **Answer**:
>
> 1. $2\left(1-\Phi \left( \sqrt{n}\left|\frac{\overline{X}_ n-\lambda _0}{{{\sqrt{\lambda_ 0}}} }\right| \right)\right)$
> 2. $\Phi \left(  \sqrt{n}\left(\frac{\overline{X}_ n-\lambda _0}{{{\sqrt{\lambda_ 0}}} }\right)  \right)$
> 3. $2\left(1-\Phi \left(\sqrt{n}\left|\frac{1/\overline{X}_ n-\lambda _0}{\lambda _0}\right|\right)\right)$
>
> **Solution**:
>
> 1. Since $X_ i\sim \textsf{Poiss}(\lambda )$, $\mathbb E[X_ i]=\lambda$ and $\sigma =\sqrt{\lambda }$. Hence, under $H_0: \lambda =\lambda _0$, the CLT gives
>    $$
>    T_{n,\lambda _0}(\overline{X}_ n) = \sqrt{n}\left(\frac{\overline{X}_ n-\lambda _0}{\sqrt{\lambda _0}}\right) \xrightarrow [n\to \infty ]{(d)} \mathcal{N}\left(0,1\right).
>    $$
>    A test $\psi$ with asymptotic level $\alpha$ is therefore
>    $$
>    \psi _{n,\lambda _0,\alpha } = \mathbf{1}\left( \left| T_{n,\lambda _0}(\overline{X}_ n) \right| > q_{\alpha /2} \right).
>    $$
>    The **asymptotic p-value is the smallest level $\alpha$ such that the test $\psi _{n,\lambda _0,\alpha }$ rejects the null hypothesis for a given sample** (here, for a given realization of $\overline{X}_n$), hence:
>    $$
>    \begin{aligned}
>    \text{p-value} &= \mathbf{P}\left(\left|  Z \right| > \left|  T_{n,\lambda _0}(\overline{X}_ n) \right|\right) \quad \text {where}\quad Z \sim \mathcal{N}(0,1)\\
>    &=2\left(1-\Phi \left( \left| T_{n,\lambda _0}(\overline{X}_ n) \right| \right)\right).
>    \end{aligned}
>    $$
>    **Alternatively**, define the test $\psi$ and the p-value using
>    $$
>    T_{n,\lambda _0}(\overline{X}_ n) = \sqrt{n}\left(\frac{\overline{X}_ n-\lambda _0}{{{\sqrt{\overline{X}_ n}}} }\right).
>    $$
>    By Slutsky's theorem and the CLT, $T_{n,\lambda _0}(\overline{X}_ n) \xrightarrow [n\to \infty ]{(d)} \mathcal{N}(0,1)$.
>
> 2. As in the previous problem, since $X_ i\sim \textsf{Poiss}(\lambda )$, $\mathbb E[X_ i]=\lambda$ and $\sigma = \sqrt \lambda$. Hence, assuming $\lambda = \lambda_o$, which is at the boundary of $\Theta_0$ and $\Theta_1$, the CLT gives again
>    $$
>    T_{n,\lambda _0}(\overline{X}_ n) = \sqrt{n}\left(\frac{\overline{X}_ n-\lambda _0}{\sqrt{\lambda _0}}\right) \xrightarrow [n\to \infty ]{(d)} \mathcal{N}(0,1).
>    $$
>    A candidate test $\psi$ with asymptotic level $\alpha$ is therefore
>    $$
>    \psi _{n,\lambda _0,\alpha } = \mathbf{1}\left(T_{n,\lambda _0}(\overline{X}_ n) {{<}}  -q_{\alpha }\right).
>    $$
>    This is because 
>    $$
>    \mathbf{P}_{\lambda }\left(T_{n,\lambda _0}(\overline{X}_ n) {{<}}  -q_{\alpha }\right) \le \mathbf{P}_{\lambda }\left(T_{n,\lambda _0}(\overline{X}_ n) {{<}}  -q_{\alpha }\right) \quad \text {for} \quad \lambda \ge \lambda _0
>    $$
>    Recall that the **(asymptotic) level $\alpha$ is an upper bound of the type 1 error.** The maximum of the type 1 error is achieved at the boundary of $\Theta_0$ and $\Theta_1$ for a one-sided tests, where the parameter space is 1-dimensional.
>
>    The asymptotic p-value is 
>    $$
>    \begin{aligned}
>    \text{p-value} &= \mathbf{P}\left(  Z  <   T_{n,\lambda _0}(\overline{X}_ n) \right) \quad \text {where}\quad Z \sim \mathcal{N}(0,1)\\
>    &=\Phi \left(  T_{n,\lambda _0}(\overline{X}_ n)  \right).
>    \end{aligned}
>    $$
>    **Alternatively**, again define the test $\psi$ and the p-value using
>    $$
>    T_{n,\lambda _0}(\overline{X}_ n) = \sqrt{n}\left(\frac{\overline{X}_ n-\lambda _0}{{{\sqrt{\overline{X}_ n}}} }\right).
>    $$
>    By Slutsky's theorem and the CLT, $T_{n,\lambda _0}(\overline{X}_ n)\xrightarrow [n\to \infty ]{(d)} \mathcal{N}(0,1).$
>
> 3. Since $X_ i\sim \textsf{Exp}(\lambda )$, $\mathbb E[X_ i]=\sigma =\frac{1}{\lambda }$. Hence, assuming $H_0: \lambda =\lambda _0$, the central limit theorem and the delta method gives
>    $$
>    \begin{aligned}
>    T_{n,\lambda _0}\left(\overline{X}_ n\right)\, =\, \sqrt{n}\left(\frac{g\left(\overline{X}_ n\right)-g\left(1/\lambda _0\right)}{\lvert g'(1/\lambda _0)\rvert (1/\lambda _0)}\right)&\xrightarrow [n\to \infty ]{(d)}\mathcal{N}\left(0,1\right)\qquad \text {where }\, g(x):=1/x.\\
>    \iff\sqrt{n}\left(\frac{1/\overline{X}_ n-\lambda _0}{\lambda _0}\right)&\xrightarrow [n\to \infty ]{(d)}\mathcal{N}\left(0,1\right)\qquad \text {since }\, g'(1/\lambda )=-\lambda ^2.
>    \end{aligned}
>    $$
>    As in (1), a test $\psi$ with asymptotic level $\alpha$ is therefore
>    $$
>    \psi _{n,\lambda _0,\alpha } = \mathbf{1}\left(\lvert T_{n,\lambda _0}\left(\overline{X}_ n\right)\rvert {\color{blue}{>}} \, q_{\alpha /2}\right).
>    $$
>    With asymptotic p-value
>    $$
>    \begin{aligned}
>    \text{p-value }&=\mathbf{P}\left( \lvert Z\rvert > \lvert T_{n,\lambda _0}\left(\overline{X}_ n\right)\rvert \right)\qquad \text {where } Z\sim \mathcal{N}(0,1)\\
>    &=2\left(1-\Phi \left(\lvert T_{n,\lambda _0}\left(\overline{X}_ n\right)\rvert \right)\right).
>    \end{aligned}
>    $$
>    **Alternatively**, define the test $\psi$ and the p-value using
>    $$
>    T_{n,\lambda _0}\left(\overline{X}_ n\right)=\sqrt{n}\left(\frac{1/\overline{X}_ n-\lambda _0}{{{1/\overline{X}_ n}} }\right).
>    $$
>    Where we plug-in the estimator $1/\overline{X}_n$ for $\lambda_0$.

# 6. A Two-Sample Test on Standardized Test Scores

The National Assessment of Educational Progress tested a simple random sample of 1000 thirteen year old students in both 2004 and 2008 and recorded each student's score. The average and standard deviation in 2004 were 257 and 39, respectively. In 2008, the average and standard deviation were 260 and 38, respectively.

Your goal as a statistician is to assess whether or not there were statistically significant changes in the average test scores of students from 2004 to 2008. To do so, you make the following modeling assumptions regarding the test scores:

* $X_1, \ldots , X_{1000}$ Represent the scores in 2004.
* $X_1, \ldots , X_{1000}$ Are iid Gaussians with standard deviation $39$.
* $\mathbb {E}[X_1] = \mu _1$, which is an unknown parameter.
* $Y_1, \ldots , Y_{1000}$ represent the scores in 2008.
* $Y_1, \ldots , Y_{1000}$ are iid Gaussians with standard deviation $38$.
* $\mathbb {E}[Y_1] = \mu _2$, which is an unknown parameter.
* $X_1, \ldots , X_ n$ Are independent of $Y_1, \ldots , Y_ n$.

You define your hypothesis test in terms of the null $H_0: \mu _1 = \mu _2$ (signifying that there were not significant changes in test scores) and $H_1: \mu _1 \neq \mu _2$. You design the test
$$
\psi = \mathbf{1}\left( \sqrt{n}\bigg| \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \bigg| \geq q_{\eta /2} \right).
$$
where $q_\eta$ represents the $1-\eta$ quantile of a standard Gaussian.

Under $H_0: \mu _1 = \mu _2$, the test statistic is distributed as a standard Gaussian:
$$
\sqrt{n} \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \sim N(0,1)
$$

1. What is the largest possible value of $\eta$ so that $\psi$ has level $10\%$?
2. If $\psi$ is designed to have level $10\%$, would you reject or fail to reject the null hypothesis given these data?
3. What is the p-value for this data set?

> **Answer**:
>
> 1. $\eta = 0.1$
> 2. Reject
> 3. $0.0815$
>
> **Solution**:
>
> 1. $q_\eta$ Is the number such that
>    $$
>    \eta = P(Z \geq q_\eta )
>    $$
>    where $Z \sim N(0,1)$. Observe that under the null hypothesis,
>    $$
>    \sqrt{n}\bigg| \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \bigg| \sim N(0,1).
>    $$
>    By symmetry,
>    $$
>    P(|Z| \geq q_{\eta /2}) = 2 P(Z \geq q_{\eta /2}).
>    $$
>    Thus our goal is to choose the smallest $\eta$ such that $P(|Z| \geq q_{\eta /2}) \leq 0.1 \%$. We get
>    $$
>    2 P(Z \geq q_{\eta /2}) = 0.1 \Rightarrow \eta = 0.1.
>    $$
>
> 2. To determine if we should reject or accept the null based on the 2008 data, we need to compute $q_{0.1/2} = q_{0.05}$. Using computational software or a table, we find that $q_{0.05} \approx 1.64$. Now we evaluate our test statistic on the 2008 data:
>    $$
>    \sqrt{n}\bigg| \frac{\overline{X}_ n - \overline{Y}_ n}{\sqrt{38^2 + 39^2}} \bigg| = \sqrt{1000}\bigg| \frac{260-257}{\sqrt{38^2 + 39^2}} \bigg| \approx 1.7422
>    $$
>    Hence, $\psi = 1$, and we would reject the hypothesis that there were no changes in test scores between 2004 and 2008.
>
> 3. To compute the p-value for this data set, we let $Z \sim N(0,1)$ and compute using a table.
>    $$
>    P(|Z| > 1.7422) = 2 P(Z > 1.7422) \approx 0.0815
>    $$

# 7. Select a Test

Select a test with asymptotic level $\alpha$, in terms of the function $T_{n,p}\left(\overline{X}_ n\right),\,$ for each of the following pairs of hypotheses: 

* $H_0 : p = 0.5 \quad \text {vs} \quad H_1 : p \neq 0.5 :$

  $\mathbf{1}\left(\left|  T_{n,0.5}\left(\overline{X}_ n\right) \right| {{>}} q_{{{\alpha /2}} }\right)$

* $H_0 : p \leq 0.5 \quad \text {vs} \quad H_1 : p > 0.5 :$

  $\mathbf{1}\left(T_{n,0.5}\left(\overline{X}_ n\right){{>}} q_{{{\alpha }} }\right)$

* $H_0 : p \geq 0.5 \quad \text {vs} \quad H_1 : p < 0.5 :$

  $\mathbf{1}\left(T_{n,0.5}\left(\overline{X}_ n\right){{<}} {{-}} q_{{{\alpha }} }\right)$

# 8. A Union-Intersection Test

Let $\,   X_1, \dots , X_ n  \,$ be i.i.d. Bernoulli random variables with unknown parameter $p \in (0,1)$. Suppose we want to test
$$
H_0: p \in [0.48, 0.51] \quad \text {vs} \quad H_1: p \notin [0.48, 0.51]
$$
We want to construct an asymptotic test $\psi$ for these hypotheses using $\overline{X}_n$. For this problem, we specifically consider the family of tests $\psi_{c_1, c_2}$ where we reject the null hypothesis if either $\,  \overline{X}_ n < c_1 \leq 0.48 \,$ or $\,  \overline{X}_ n > c_2 \geq 0.51 \,$ for some $c_1$ and $c_2$ that may depend on $n$, i.e.,
$$
\psi _{c_1,c_2}=\mathbf{1}\left((\overline{X}_ n < c_1)\, \cup \, (\overline{X}_ n > c_2 ) \right)\qquad \text {where } c_1<0.48<0.51<c_2.
$$
Throughout this problem, we will discuss **possible choices for constants $c_1$ and $c_2$ , and their impact to both the asymptotic and non-asymptotic level of the test**.

1. What is the expression of the (smallest asymptotic) level $\alpha$ of this test?

2. Use the central limit theorem and the approximation $\sqrt{p(1-p)} \approx \frac{1}{2}$ for $p \in [0.48, 0.51]$ to approximate $\mathbf{P}_ p(\overline{X}_ n < c_1)$ and $\mathbf{P}_ p(\overline{X}_ n > c_2)$ for large $n$. Express your answers as a formula in terms of $c_1, c_2, n$ and $p$. For what value of $p \in [0.48, 0.51]$ is the expression for $\mathbf{P}_ p\left(\overline{X}_ n < c_1\right)\,$ and $\mathbf{P}_ p(\overline{X}_ n > c_2)$ maximized?

3. Next, we combine the results from (1) and (2). Apply the inequality
   $$
   \max _{x} \left(f(x) + g(x)\right) \leq \max _ x f(x) + \max _ x g(x)\,
   $$
   To the expression for the (asymptotic) level $\alpha$ obtained in part (1) and use the results from part (b) to give an upper bound on $\alpha$. Express your answer as a formula in terms of $c_1, c_2,$ and $n$.

4. Suppose that we wish to have a level $\alpha = 0.05$. What $c_1$ and $c_2$ will achieve $\alpha = 0.05$? Choose $c_1$ and $c_2$ by setting the expressions you obtained above for $\max _{p\in [0.48,0.51]} \mathbf{P}_ p\left(\overline{X}_ n<c_1\right)$ and $\max _{p\in [0.48,0.51]} \mathbf{P}_ p\left(\overline{X}_ n>c_2\right)$ to both be $0.025$.

5. We will now show that the values we just derived for $c_1$ and $c_2$ are in fact too conservative. 

   For $p > 0.48$ (note the strict inequality), find $\lim _{n\to \infty } \mathbf{P}_ p(\overline{X}_ n < c_1)$.

   For $p < 0. 51$ (note the strict inequality), find $\lim _{n\to \infty }\mathbf{P}_ p(\overline{X}_ n > c_2)$. 

6. Next, we analyze the asymptotic test given different possible values of $p$, in order to choose suitable and sufficiently-tight $c_1$ and $c_2$. Looking more closely at part (d), we may note that the asymptotic behavior of the expressions for the errors are different depending on whether $p=0.48$, $0.48 <p  < 0.51$, or $p=0.51$.

   Based on your answers and work from the previous part, evaluate the asymptotic Type 1 error
   $$
   \mathbf{P}(\overline{X}_ n < c_1) + \mathbf{P}(\overline{X}_ n > c_2).
   $$
   on each of the three cases for the value of $p$ in terms of $c_1$, $c_2$, and $n$, and determine in each case which component(s) of the Type 1 error will converge to zero.

   This would allow you to come up with a new set of conditions for $c_1$ and $c_2$ in terms of $n$, given the desired level of $5\%$. 

> **Answer**:
>
> 1. $\alpha \, =\, \max _{p \in [0.48, 0.51]} (\mathbf{P}_ p(\overline{X}_ n < c_1) + \mathbf{P}_ p(\overline{X}_ n > c_2)) .$
> 2. $\mathbf{P}_ p(\overline{X}_ n < c_1) \approx \Phi \left(2(c_1 - p)\sqrt{n}\right).\\ \mathbf{P}_ p(\overline{X}_ n < c_1)  \text{ is max at p = } 0.48.\\\mathbf{P}_ p(\overline{X}_ n > c_2) \approx 1 - \Phi (2(c_2 - p)\sqrt{n}).\\\mathbf{P}_ p(\overline{X}_ n > c_2) \text{ is max at p = } 0.51.$
> 3. $\alpha \leq \Phi ( 2(c_1 - 0.48)\sqrt{n})+ 1 - \Phi ( 2(c_2 - 0.51)\sqrt{n}) $
> 4. $c_1 = -\frac{0.98}{\sqrt{n}}+0.48\\c_2 = \frac{0.98}{\sqrt{n}}+0.51$
>
> **Solution**:
>
> 1. The type 1 error is 
>    $$
>    \mathbf{P}_ p\left((\overline{X}_ n < c_1)\,  \cup \, (\overline{X}_ n > c_2)\right)
>    $$
>    Since $c_1 < 0.48 < 0.51 < c_2$, we have
>    $$
>    \mathbf{P}_ p\left((\overline{X}_ n < c_1)\,  \cup \, (\overline{X}_ n > c_2)\right) = \mathbf{P}_ p\left(\overline{X}_ n < c_1\right)+ \mathbf{P}_ p\left(\overline{X}_ n > c_2)\right).
>    $$
>    Maximizing this over $p \in [0.48, 0.51]$, we get that the **maximum Type 1 error of this test, i.e., the smallest level**, is
>    $$
>    \alpha \, =\, \max _{p \in [0.48, 0.51]} (\mathbf{P}_ p(\overline{X}_ n < c_1) + \mathbf{P}_ p(\overline{X}_ n > c_2)) 
>    $$
>
> 2. Consider a specific $p\in [0.48, 0.51]$, then
>    $$
>    \mathbf{P}_ p(\overline{X}_ n < c_1) = \mathbf{P}_ p\left(\frac{\overline{X}_ n - p}{\sqrt{p(1-p)}}\sqrt{n} < \frac{c_1 - p}{\sqrt{p(1-p)}}\sqrt{n}\right).
>    $$
>    By the CLT and noting that the variance of $X_1$ is $\sqrt{p(1-p)}$, we see
>    $$
>    {\overline{X}_n -p  \over \sqrt{p(1-p)} }\sqrt n \xrightarrow [n\rightarrow \infty]{(d)} \mathcal{N}(0,1)
>    $$
>    So 
>    $$
>    \mathbf{P}_ p(\overline{X}_ n < c_1) = \Phi \left(\frac{c_1 - p}{\sqrt{p(1-p)}}\sqrt{n})\right) \approx \Phi \left(2(c_1 - p)\sqrt{n}\right).
>    $$
>    As $\Phi(x)$ is an increasing function, $\Phi(2(c_1-p)\sqrt n)$ is maximized at the minimum possible $p$ in the range, which is $p=0.48$. Hence, $\max _{p \in [0.48, 0.51]} \mathbf{P}_ p(\overline{X}_ n < c_1) = \Phi (2(c_1 - 0.48)\sqrt{n})$.
>
>    Similarly, for a specific $p\in [0.48, 0.51]$,
>    $$
>    \mathbf{P}_ p\left(\overline{X}_ n > c_2\right) = \mathbf{P}_ p\left(\frac{\overline{X}_ n - p}{\sqrt{p(1-p)}}\sqrt{n} > \frac{c_2 - p}{\sqrt{p(1-p)}}\sqrt{n}\right)
>    $$
>    Applying the CLT and the approximation $\sqrt{p(1-p)} \approx \frac{1}{2}$ gives 
>    $$
>    \mathbf{P}_ p(\overline{X}_ n > c_2) \approx 1 - \Phi (2(c_2 - p)\sqrt{n}).
>    $$
>    As $\Phi(x)$ is an increasing function, $1 - \Phi ( 2(c_2 - p)\sqrt{n})$ is maximized at the maximum possible $p$ in the range, which is $p=0.51$. Hence,
>    $$
>    \max _{p \in [0.48, 0.51]} \mathbf{P}_ p(\overline{X}_ n > c_2) = 1 - \Phi ( 2(c_2 - 0.51)\sqrt{n})
>    $$
>
> 3. Recall that **the (smallest) asymptotic level $\alpha$ of a test is equal to the maximum Type 1 error rate.** We have
>    $$
>    \begin{aligned}
>    \max _{p \in [0.48, 0.51]} (\mathbf{P}_ p(\overline{X}_ n < c_1) + \mathbf{P}(\overline{X}_ n > c_2)) &\leq \max _{p \in [0.48, 0.51]} \mathbf{P}(\overline{X}_ n < c_1) + \max _{p \in [0.48, 0.51]} \mathbf{P}(\overline{X}_ n > c_2)\\
>    &\approx \Phi ( 2(c_1 - 0.48)\sqrt{n})+ 1 - \Phi ( 2(c_2 - 0.51)\sqrt{n})
>    \end{aligned}
>    $$
>    **(This bound is not tight because the the maxima for the two summands are not obtained at the same $p$.)**
>
> 4. To have a test of level $0.05$ and equal left and right tails, solve the equations
>    $$
>    \Phi (2*(c_1-0.48)*\sqrt{n}) = 0.025\\
>    2*(c_1-0.48)*\sqrt{n} = -1.96\\
>    c_1 = -\frac{0.98}{\sqrt{n}}+0.48
>    $$
>
>    $$
>    \Phi (2*(c_2-0.51)*\sqrt{n}) = 0.975\\
>    2*(c_2-0.51)*\sqrt{n} = 1.96\\
>    c_2 = \frac{0.98}{\sqrt{n}}+0.51
>    $$
>
> 5. From (2), 
>    $$
>    \mathbf{P}(\overline{X}_ n < c_1) = \Phi (\frac{c_1 - p}{\sqrt{p(1-p)}}\sqrt{n})) \approx \Phi (2(c_1 - p)\sqrt{n}).
>    $$
>    If $p > 0.48$, then
>    $$
>    \Phi (2(c_1 - p)\sqrt{n}) < \Phi (2(0.48 - p)\sqrt{n}).
>    $$
>    This argument in $\Phi$ on the right is a negative constant times $\sqrt n$, so the argument tends to negative infinity as $n \rightarrow \infty $ and thus,
>    $$
>    \Phi (2(c_1 - p)\sqrt{n}) \rightarrow 0.
>    $$
>    For the other side, $c_2$, we obtained in (2) that
>    $$
>    \mathbf{P}(\overline{X}_ n > c_2) \approx 1 - \Phi (2(c_2 - p)\sqrt{n}).
>    $$
>    If $ p < 0.51$, then
>    $$
>    1 - \Phi (2(c_2 - p)\sqrt{n}) < 1 - \Phi (2(c_2 - 0.51)\sqrt{n}).
>    $$
>    Taking $n \rightarrow \infty$, as $c_2 > 0.51$,
>    $$
>    2(c_2 - 0.51)\sqrt{n} \rightarrow +\infty ;
>    $$
>    So
>    $$
>    1 - \Phi (2(c_2 - 0.51)\sqrt{n}) \rightarrow 0
>    $$
>    And thus,
>    $$
>    1 - \Phi (2(c_2 - p)\sqrt{n}) \rightarrow 0.
>    $$
>
> 6. For this solution, we write $c_1(n)$ and $c_2(n)$ for $c_1$ and $c_2$ respectively as they are in practice functions of $n$.
>
>    From the previous part, $\mathbf{P}(\overline{X}_ n < c_1(n))$ for any $c_1(n) < 0.48$ will definitely converge to $0$ for $0.48 < p < 0.51$ and for $p = 0.51$, but not for $p=0.48$. When $p = 0.48$, we could write
>    $$
>    \mathbf{P}(\overline{X}_ n < c_1(n)) = \Phi (2(c_1(n) - 0.48)\sqrt{n}).
>    $$
>    Similarly, $\mathbf{P}(\overline{X}_ n > c_2(n))$ for any $c_2(n) > 0.51$ will converge to $0$ for $p=0.48$ and $0.48 < p < 0.51$, while for $p=0.51$,
>    $$
>    \mathbf{P}(\overline{X}_ n > c_2(n)) = 1 - \Phi (2(c_2(n) - 0.51)\sqrt{n}).
>    $$
>    Summarizing the above observations, we get
>    $$
>    \lim _{n\to \infty } (\mathbf{P}_(\overline{X}_ n < c_1(n)) + \mathbf{P}_(\overline{X}_ n > c_2(n))) = \begin{cases}  \lim _{n\to \infty } \Phi (2(c_1(n) - 0.48)\sqrt{n}), \quad &p=0.48\\ 0, \quad &0.48 < p < 0.51\\ \lim _{n\to \infty } 1 - \Phi (2(c_2(n) - 0.51)\sqrt{n}), \quad &p=0.51 \end{cases}
>    $$
>    Hence our constraints (from the first and third cases above) are
>    $$
>    \lim _{n\to \infty } \Phi (2(c_1(n) - 0.48)\sqrt{n}) \leq 0.05, \quad \lim _{n\to \infty } \Phi (2(c_2(n) - 0.51)\sqrt{n}) \geq 0.95.
>    $$
>    Taking the simplest (or broadest) case, we could set equality everywhere, which gives
>    $$
>    \Phi \left(2(c_1(n) - 0.48)\sqrt{n}\right) = 0.05,\quad \Phi \left((2(c_2(n) - 0.51)\sqrt{n}\right) = 0.95.
>    $$
>    Finally, taking $\Phi ^{-1}$ of both sides then rearranging gives our answer:
>    $$
>    c_1(n) = \frac{-q_{0.05}}{2\sqrt{n}} + 0.48,\quad c_2(n) = \frac{q_{0.05}}{2\sqrt{n}} + 0.51
>    $$





