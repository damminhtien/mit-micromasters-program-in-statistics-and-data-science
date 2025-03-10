# Lecture 2: Probability redux

Let $X, X_1,X_2,...,X_n$ be i.i.d. random variables, with $\mu=\mathbb{E}[X]$ and $\sigma^2=Var[X]$

## Laws (weak and strong) of large numbers (LLN)

$$
\bar{X_n} := \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow[n \to \inf]{\bm{P}, a.s.} \mu 
$$

where the convergence is in probability (as denoted by  $\bm{P}$ on the convergence arrow) and almost surely (as denoted by $a.s.$ on the arrow) for the weak and strong laws respectively.

## Central limit theorem (CLT)

$$
\sqrt{n} \frac{\bar{X_n}-\mu}{\sigma} \xrightarrow{(d)} \mathcal{N}(0,1)
$$

where the convergence is in distribution, as denoted by $(d)$ on top of the convergence arrow.

## Hoeffding’s inequality

Given $n (n>0)$ i.i.d. random variables $X_1,X_2,...,X_n \sim X$ that are almost surely bounded - meaning $\bm{P}(X\notin[a,b])=0.$

$$
\bm{P}(|\bar{X_n}-\mathbb{E}[X]|\geq\epsilon) \leq 2\exp(-\frac{2n\epsilon^2}{(b-a)^2})
$$

for all $\epsilon>0$. Unlike for the central limit theorem, here the **sample size $n$ does not need to be large.** 

## (Optional) Markov and Chebyshev inequalities

### Markov inequality

For a random variable $X\geq0$ with mean $\mu\geq0$, and any number $t>0$:

$$
\bm{P}(X\geq t)\leq \frac{\mu}{t}
$$

Note that the Markov inequality is restricted to non-negative random variables.

### Chebyshev inequality

For a random variable $X$ with (finite) mean $\mu$ and variance $\sigma^2$, and for any number $t>0$,

$$
\bm{P}(|X-\mu|\geq t)\leq \frac{\sigma^2}{t^2}
$$

Note that Markov inequality is applied to $(X-\mu)^2$, we obtain Chebyshev’s inequality. Markov inequality is also used in the proof of Hoeffding’s inequality.