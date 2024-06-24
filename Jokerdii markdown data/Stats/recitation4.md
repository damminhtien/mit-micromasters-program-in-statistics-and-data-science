# Recitation 4. Distances between probability distribution

**Review:**

Let $P,Q,R$ be probability distributions over $E$, with PDF or PMF $p,q,r$.

Let event $A$ be $A \subset E,$ then $\mathbf{P}(A) = \int_Ap(x)dx$ or $\mathbf{P}(A) = \sum\limits_{x \in A}p(x)dx$, $(\mathbf{P}_\theta)_{\theta \in \Theta}$.

The distance is $d(\mathbf{P}_\theta, \mathbf{P}_{\theta'})$.

* Total Variation Distance (TV)
  $$
  \begin{aligned}
  \text{TV}(P,Q) &= \sup_{A \subset E} |\mathbf{P}(A) - \mathbf{Q}(A)|\\
  &= {1\over 2} \int_E |p(x) - q(x)| dx\\
  [&={1\over 2} \sum_{x \in E} |p(x) - q(x)|]
  \end{aligned}
  $$

* Kullback-Leibler Divergence (KL)
  $$
  \begin{aligned}
  \text{KL}(P,Q) &= \text{KL} (P || Q)\\
  &= \begin{cases} \int_E p(x) \log {p(x) \over q(x) } dx \qquad\text{or} \qquad  [\sum_{x \in E} p(x) \log {p(x) \over q(x)}] \\ +\infty \qquad \exist x: q(x) = 0, p(x) \neq 0 \end{cases}
  \end{aligned}
  $$

Properties:

|                                                              | TV       | KL       |
| ------------------------------------------------------------ | -------- | -------- |
| Non-negative: $d(P,Q)\geq 0$                                 | $\surd$  | $\surd$  |
| Definite: $d(P,Q) = 0 \implies P=Q$                          | $\surd$  | $\surd$  |
| Symmetric: $d(P,Q) = d(Q,P)$                                 | $\surd$  | $\times$ |
| Triangle inequality: $d(P,Q) \leq d(P,R) + d(R,Q)$           | $\surd$  | $\times$ |
| Amenable to estimation (replace $\mathbb{E}(\cdot)$ by ${1\over 2} \sum\limits^n_{i=1} [\cdot]$) | $\times$ | $\surd$  |

**Problem statement:**

1. Show that the Poisson distribution with parameter $1/n$ converges in total variation distance to the Dirac distribution at zero (i.e., the distribution of the random variable that is always equal to zero).
2. For $p,q \in (0,1)$ and $n \geq 1$, compute the Kullback-Leibler divergence between $\mathsf{B}(n,p)$ and $\mathsf{B}(n,q)$.
3. Compute the Kullback-Leibler divergence between two Gaussian distributions that have the same variance.

>  **Solution:**
>
> 1. Given $P_n = \mathsf{Poiss}({1\over n}), Q = \delta_o$, show $\text{TV}(P_n,Q) \xrightarrow[n\rightarrow \infty]{}0$.
>
>    Recall the PMF of $\mathsf{Poiss}(\lambda)$ is 
>    $$
>    p_\lambda(k) = {\lambda^k \over k!} e^{-\lambda}, k = 0,1,2,...;
>    $$
>    The PMF of Dirac distribution is 
>    $$
>     q(k) =\begin{cases} 1, & k=0\\ 0, &\text{o.w.} \end{cases}
>    $$
>    The TV is
>    $$
>    \begin{aligned}
>    \text{TV}(P_n, Q) &= {1\over 2} \sum^\infty_{k=0} |p_{1/2}(k) - q(k)| \\
>    &= {1\over 2} \sum^\infty_{k=0} |{ ({1\over n})^k \over k!} e^{-1/n} - \delta_o(k)|\\
>    &={1\over 2} |{({1\over n})^0 \over 0!} e^{-1/n}-1| - {1\over 2} \sum^\infty_{k\geq 1} |{ ({1\over n})^k \over k!} e^{-1/n} - \delta_o(k)|\\
>    &= {1\over 2} | e^{-1/n}-1| - {1\over 2} \sum^\infty_{k\geq 1} |{ ({1\over n})^k \over k!} e^{-1/n} - \delta_o(k)|\\
>    &= {1\over 2} | e^{-1/n}-1| - {1\over 2} \mathbf{P}_n(\{1,2,...\}) \\
>    &= {1\over 2} | e^{-1/n}-1| - {1\over 2} (1 -\mathbf{P}_n({\{0}\})) \\
>    &= {1\over 2} | e^{-1/n}-1| - {1\over 2} (1 - {(1/n)^0 \over 0!} e^{-1/n}) \\
>    & \xrightarrow[n \rightarrow \infty]{} {1\over 2}|1-1|  - {1\over 2} (1-1)\\
>    & \xrightarrow[n \rightarrow \infty]{} 0
>    \end{aligned}
>    $$
>
> 2. Given $\mathbf{P} = \mathsf{Bin}(n,p)$ and $\mathbf{Q} = \mathsf{Bin}(n,q), \quad p,q \in (0,1)$.
>
>    Recall the PDF of Binomial distribution is
>    $$
>    f(p,k) = {n \choose k} l^k(1-p)^{n-k}
>    $$
>    The KL is
>    $$
>    \begin{aligned}
>    \text{KL}(P||Q) &= \sum^n_{k=0} f(p,k) \cdot \log { f(p,k)\over f(q,k) }\\ 
>    &= \sum^n_{k=0} f(p,k) \cdot \log \left[ {{n\choose k}p^k (1-p)^{n-k} \over {n\choose k}q^k (1-q)^{n-k} } \right]\\
>    &=\sum^n_{k=0} f(p,k) \cdot \left[ \log(({p\over q})^k) + \log(({1-p \over 1-q })^{n-k})\right]\\
>    &= \sum^n_{k=0} f(p,k)\cdot \left[ k\log({p\over q}) + (n-k)\log({1-p \over 1-q })\right]\\
>    &\left(\text{Since } \sum^n_{k=0}k f(p,k) = \mathbb{E}[k] = np, \quad \text{where } k \sim \mathsf{Ber}(n,p)\right)\\
>    &= \log({p\over q}) \cdot np + \log ({1-p \over1-q }) \cdot (n - np)\\
>    &= 
>    \end{aligned}
>    $$
>    Note that when $q \rightarrow 0$, KL$(P,Q)\rightarrow \infty$.
>
> 3. Given $\mathbf{P} = \mathcal{N}(a,1), Q = \mathcal{N}(b,1), a,b \in \R; $
>
>    Recall the PDF of normal distribution is
>    $$
>    f_{a,\sigma^2} (x) = {1\over \sqrt{2\pi \sigma^2}} e^{-{1\over 2\sigma^2}(x-a)^2}
>    $$
>    The KL is
>    $$
>    \begin{aligned}
>    \text{KL} (P||Q) &= \int_\R f_{a,1}(x) \log \left[ {f_{a,1}(x) \over f_{b,1}(x) } \right]dx\\
>    &= \int_\R f_{a,1}(x) \log \left[ {1\over \sqrt{2\pi}} e^{-{1\over 2}(x-a)^2} \over {1\over \sqrt{2\pi }} e^{-{1\over 2}(x-b)^2}  \right]dx\\
>    &= \int_\R f_{a,1}(x) \log \left[  e^{-{1\over 2}(x-a)^2} \over  e^{-{1\over 2}(x-b)^2}  \right]dx\\
>    &= \int_\R f_{a,1}(x) \log e^{-{1\over 2} (x-a)^2 + {1\over 2} (x-b)^2} dx\\
>    &= \int_\R f_{a,1}(x) \left( -{1\over 2} (x-a)^2 + {1\over 2} (x-b)^2  \right)dx\\
>    &=\int_\R f_{a,1}(x) \left( x(a-b) -{1\over 2} a^2 + {1\over 2}^2 \right)dx\\
>    &= (a-b) \int_\R x f_{a,1}(x)dx + \left(-{1\over 2} a^2 + {1\over 2}b^2\right) \int_\R f_{a,1}(x)dx\\
>    & \left(\text{Since } \mathbb{E}[X] = \int_\R x f_{a,1}(x)dx = a, \text{ and }  \int_\R f_{a,1}(x)dx = 1\right)\\
>    &=  (a-b) a  + \left(-{1\over 2} a^2 + {1\over 2}b^2\right) 1\\
>    &= {1\over 2} (a^2 - 2ab + b^2)\\
>    &= {1\over 2}(a-b)^2
>    \end{aligned}
>    $$
>    