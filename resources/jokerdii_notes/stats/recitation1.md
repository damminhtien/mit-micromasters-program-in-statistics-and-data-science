# Recitation 1: Mode of Convergence

## Example 1

Given $U \sim \mathsf{Unif}[0,1], X_n = U + U^n$, Claim: $X_n \xrightarrow[]{a.s.} U$.

**Proof**: 

We divide the sample space into two disjoint parts:

* $U < 1, X_n \xrightarrow[n \rightarrow \infty]{}U$
* $U = 1, X_n = 2$

$\mathbf{P}(X_n \xrightarrow[n \rightarrow \infty]{}U) = \mathbf{P}(X_n \rightarrow U | U < 1) \mathbf{P}(U < 1) + \mathbf{P}(X_n \rightarrow U|U=1) \mathbf{P}(U=1) = 1 + 0 = 1$

Since $U$ is a continuous random variable, $\mathbf{P}(U=1) = 0$.

## Example 2

Given $X_1, ...,X_n \stackrel{iid}{\sim} \mathsf{Unif[0,1]}, X_{(1)} = \min X_i$, Claim: $X_{(1)} \xrightarrow[]{P} 0$.

**Proof**:
Fix $\epsilon > 0$,
$$
\begin{aligned}
\mathbf{P}(|X_{(1)}-0| > \epsilon) &= \mathbf{P}(X_{(1)} > \epsilon)\\
&= \mathbf{P}(X_i > \epsilon, \forall i)\\
&= (\mathbf{P}(X_1 > \epsilon))^n\\
&= (\int^1_{\epsilon} 1 \, \mathsf{dx})^n\\
&= (1- \epsilon)^n \xrightarrow[n \rightarrow \infty]{} 0 \quad \text{ Since } 0<\epsilon < 1
\end{aligned}
$$

## Example 3

Given $X_1, ...,X_n \stackrel{iid}{\sim} \mathsf{Unif[0,1]}, X_{(1)} = \max X_i$, Claim: $n(1-X_{(n)}) \xrightarrow[]{(d)} \mathsf{Exp}(1)$.

**Proof**:
$$
\mathbf{P}(X_{(n)} < x) = \mathbf{P}(X_i < x, \forall i) = (x)^n \quad \text{by independence}
$$
Recall that $(1- {x \over n})^2 \rightarrow e^{-x}$, so we plug it in the equation above and get
$$
\mathbf{P}(X_{(n)} < 1-{x \over n}) = (1- { x \over n})^n\\
\mathbf{P}(x < n(1-X_{(n)})) = ( 1- {x \over n})^n\\
$$
Now we write it as CDF
$$
F_{n(1-X_{(n)})}(x) = 1 - \mathbf{P}(x < n(1- X_{(n)}) ) = 1 - (1- { x \over n})^n \xrightarrow[]{n \rightarrow \infty} 1 - e^{-x}
$$
which is the CDF of $\rm{Exp}(1)$.

## Example 4

Given $U \sim \rm{Unif}[0,1],$
$$
\begin{aligned}
X_1 &= U+ \mathbf{1}(U \in [0,1])\\
X_2 &= U+ \mathbf{1}(U \in [0,1/2])\\
X_3 &= U+ \mathbf{1}(U \in [1/2,1])\\
X_4 &= U+ \mathbf{1}(U \in [0,1/3])\\
X_5 &= U+ \mathbf{1}(U \in [1/3,2/3])\\
X_6 &= U+ \mathbf{1}(U \in [2/3,1])\\
\end{aligned}
$$
**Claim 1**: $X_n \xrightarrow[]{P} U$. **Proof**:

Fix $0 < \epsilon < 1$,
$$
\mathbf{P}(|X_n - U|> \epsilon) = \mathbf{P}(U \in \{ a_n, b_n\}) = b_n - a_n \xrightarrow[n \rightarrow \infty]{} 0
$$
Since when $U \in \{a_n ,b_n\}$, the value $X_i -U= \mathbf{1}(U \in [a_n, b_n])$ tends to be larger. When $n$ is large, the interval tends to be small.

**Claim 2**: $X_n \xrightarrow[]{a.s.} U$. **Disproof**:
$$
\mathbf{P}(X_n \rightarrow U) \neq 1
$$
Since $X_n$ does not converge to any number, i.e. $X_n$ has no limit.

## Summary

* Law of Large Numbers (LLN): 

  $X_1, ..., X_n, i.i.d, \,\, E[X_i] = \mu \implies \overline{X} = {1 \over n} \sum^n_{i=1 }X_i$

* **Central Limit Theorem (CLT)** is a typical example of convergence in distribution.

  $X_1, ..., X_n, i.i.d, \,\, \mathbb{E}[X] = \mu, \mathsf{Var}[X] = \sigma^2 < \infty \implies \sqrt{n}(\overline{X_n} - \mu) \xrightarrow[]{(d)} \mathcal{N}(0, \sigma^2)$

