Problem set for Lec5.

# 1. Confidence Intervals for Curved Gaussian Family

Let $X_1, ..., X_n$ be i.i.d. random variables with distribution $\mathcal{N}(\theta, \theta),$ for some unknown parameter $\theta > 0$.

1. Expectation and variance of $\overline{X}_n$.

2. Find an interval $\mathcal{I}_{\theta } = [ A_\theta , B_\theta ]$ (that depends on $\theta$) centered about $\overline{X}_n$ such that
   $$
   \mathbf{P}(\mathcal{I}_{\theta} \ni \theta) = 0.9 \quad \text{ for all n (i.e., not for large } n).
   $$
   (Use the estimate $q_{0.05} \approx 1.6448$ for best results.)

3. Find a C.I. $ \mathcal{I}_{\text {plug-in}} = [ A_{\text {plug-in}}, B_{\text {plug-in}}]$ with **asymptotic** C.I. $90\%$ by plugging in $\overline{X}_n$ for all occurrences of $\theta$ in $\mathcal{I}_\theta$.

   (Use the estimate $q_{0.05} \approx 1.6448$ for best results.)

4. Find a C.I. $\mathcal{I}_{\text {solve}} = [ A_{\text {solve}}, B_{\text {solve}}]$ for $\theta$ with **non-asymptotic** level $90\%$ solving the bounds in $\mathcal{I}_\theta$ for $\theta$.

> 1) 
>
> Since the sample average $\overline{X}_n$ follows a normal distribution for any integer $n \geq 1$,
>
> The expectation and variance are
> $$
> \mathbb E[\overline{X}_ n] = \theta , \quad \textsf{Var}(\overline{X}_ n) = \frac{1}{n^2} \sum _{i=1}^{n} \textsf{Var}(X_ i) = \frac{\theta }{n}.
> $$
> Hence,
> $$
> \sqrt{\frac{n}{\theta }} (\overline{X}_ n - \theta ) \sim \mathcal{N}(0,1).
> $$
> 2) 
>
> We look up the quantile value for a symmetric $90\%$ C.I. for a Gaussian random variable $Z \sim \mathcal{N}(0,1)$
> $$
> \mathbf{P}(\vert Z\vert \leq 1.6448) \approx 0.9
> $$
> we obtain
> $$
> \mathbf{P}\left(\left|\sqrt{\frac{n}{\theta }} (\overline{X}_ n - \theta ) \right| \leq 1.6448\right) = 0.9,
> $$
> Hence, 
> $$
> \mathcal{I}_1 = \left[ \overline{X}_ n - \frac{1.6448 \sqrt{\theta }}{\sqrt{n}}, \overline{X}_ n + \frac{1.6448 \sqrt{\theta }}{\sqrt{n}} \right].
> $$
> 3) 
>
> By LLN we have
> $$
> \overline{X}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \theta .
> $$
> Then CLT and Slutsky together imply that
> $$
> \sqrt{\frac{n}{\bar{X_ n}}} (\overline{X}_ n - \theta ) \xrightarrow [n \to \infty ]{d} \mathcal{N}(0,1).
> $$
> Hence, we obtain an asymptotic C.I. with level $90\%$ by replacing $\theta$ by $\overline{X}_n$ in the expression for $\mathcal{I}_1$ and we can set
> $$
> \mathcal{I}_2 = \left[ \overline{X}_ n - \frac{1.6448 \sqrt{\overline{X}_ n}}{\sqrt{n}}, \overline{X}_ n + \frac{1.6448 \sqrt{\overline{X}_ n}}{\sqrt{n}} \right].
> $$
> 4) From Q2 we have
> $$
> \mathbf{P}\left( \left| \sqrt{\frac{n}{\theta }} (\overline{X}_ n - \theta ) \right| \leq 1.65 \right) = 90\% .
> $$
> with $t = 1.6448$, the constraint on $\theta$ is equivalent to 
> $$
> \begin{aligned}
> &\left| \sqrt{\frac{n}{\theta }} (\overline{X}_ n - \theta ) \right| \leq t\\
> \iff & \frac{n}{\theta }(\overline{X}_ n - \theta )^2 \leq t^2\\
> \iff & \theta ^2 - 2 \theta \overline{X}_ n + \overline{X}_ n^2 \leq {t^2 \theta \over n}\\
> \iff & \theta ^2 - \left(2 \overline{X}_ n + \frac{t^2}{n}\right) \theta + \overline{X}_ n^2 \leq 0\\
> \iff & \theta \in \left[ \overline{X}_ n + \frac{t^2}{2n} - \sqrt{\Delta }, \, \overline{X}_ n + \frac{t^2}{2n} + \sqrt{\Delta } \right], \quad \text {where }\, \Delta = \frac{t^4}{4n^2} + \frac{t^2 \overline{X}_ n}{n}
> \end{aligned}
> $$
> By the quadratic formula. Substituting $t = 1.65$ gives
> $$
> \mathcal{I}_{\text {solve}} = \left[ \overline{X}_ n + \frac{1.6448^2}{2n} - \sqrt{\frac{1.6448^4}{4n^2} + \frac{1.6448^2 \overline{X}_ n}{n}}, \overline{X}_ n + \frac{1.6448^2}{2n} + \sqrt{\frac{1.6448^4}{4n^2} + \frac{1.6448^2 \overline{X}_ n}{n}} \right].
> $$

# 2. Delta method and asymptotic variances

#### Review of arguments: the Law of Large Numbers, the Central Limit Theorem, and the Delta Method.

Let $X_1, X_2, ...$ , be random variables. The **(weak) Law of Large Numbers** says that under suitable assumptions, with
$$
\overline{X}_ n = \frac{1}{n} \sum _{i=1}^{n} X_ i,
$$
We have
$$
\overline{X}_ n \xrightarrow {\mathbf{P}} \mathbb E[X_1].
$$
The **Central Limit Theorem** states that under some assumptions, there is a $V$ such that
$$
\sqrt{n} (\overline{X}_ n - \mathbb E[X_1]) \xrightarrow {\mathrm{(D)}} \mathcal{N}(0,V).
$$
The **Delta Method** gives us a way to control the asymptotic variance of a transformation of a random variable. Let $\theta \in \R$ be a parameter and $Z_n \in \R$ be a sequence of random variables that satisfies.
$$
\sqrt{n}(Z_ n - \theta ) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0,V)
$$
for some $V>0$.

Given a function $g \,  \colon \Omega \subseteq \mathbb {R}\to \mathbb {R}$,
$$
\sqrt{n}(g(Z_ n) - g(\theta )) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0,W).
$$
for some $X > 0$.

1. What are the assumptions we need for the **weak Law of Large Numbers**?

* $\mathbb E[|X_ i|] < \infty$ for all $i$
* $X_1, X_2, ...$ independent
* $X_1, X_2, ...$ identically distributed

2. What are the assumptions we need for the **Central Limit Theorem**?

* $\mathbb E[|X_ i|] < \infty$ for all $i$
* $\textsf{Var}(X_ i) < \infty$ for all $i$

* $X_1, X_2, ...$ independent
* $X_1, X_2, ...$ identically distributed

3. Pick the following assumptions and conditions that apply to the **Delta Method** as stated in class:

* $g$ is continuously differentiable at $\theta$

* $W = g'(\theta)^2 V$

#### Problem statement

Compute the **asymptotic variance** of some estimators. Recall that the asymptotic variance of an estimator $\hat{\theta}$ for a parameter $θ$ is defined as $V(\hat{θ})$, if
$$
\sqrt{n}(\widehat{\theta } - \theta ) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, V(\widehat{\theta })).
$$

1. Argue that the proposed estimators $\widehat{\lambda }$ and $\widetilde\lambda$ below are both consistent and asymptotically normal. Then, give their asymptotic variances $V(\widehat{\lambda })$ and $V(\tilde{\lambda})$, and decide if one of them is always bigger than the other.

   Let $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim }\textsf{Poiss}(\lambda )$, for some $\lambda > 0$. Let $\hat{\lambda} = \overline{X}_n$ and $\tilde{\lambda} = -\ln(\overline{Y}_n)$, where $Y_i = \mathbf{1}\{X_i = 0\}, i = 1,...,n$.

   > **Answer**: 
   >
   > $V(\widehat{\lambda}) = \lambda\\ V(\tilde{\lambda}) = \exp(\lambda) - 1$
   >
   > **Solution**: 
   >
   > For $\widehat{\lambda}$, By the LLN,
   > $$
   > \overline{X}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[X_1] = \lambda .
   > $$
   > By the CLT,
   > $$
   > \sqrt{n} (\overline{X}_ n - \lambda ) \sim \mathcal{N}(0,\textsf{Var}(X_1)) = \mathcal{N}(0,\lambda ),
   > $$
   > Hence,
   > $$
   > V(\widehat\lambda ) = \lambda .
   > $$
   > For $\tilde{\lambda}$, first observe that by the LLN,
   > $$
   > \overline{Y}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[Y_1] = \mathbf{P}(X_1 = 0) = \exp (-\lambda ),
   > $$
   > so with $g(t) = -\log (t)$,
   > $$
   > \tilde\lambda = g(\overline{Y}_ n) \xrightarrow [n \to \infty ]{\mathbf{P}} g(\exp (-\lambda )) = \lambda .
   > $$
   > The CLT yields
   > $$
   > \sqrt{n} (\overline{Y}_ n - \mathbb E[Y_1]) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, \textsf{Var}(Y_1)) = \mathcal{N}(0, \exp (-\lambda ) (1 - \exp (-\lambda )),
   > $$
   > where we used the formula $\textsf{Var}(Z) = p(1-p) $ if $Z \sim \textsf{Be}(p)$. In order to apply the Delta Method for the above $g(t)$, we compute
   > $$
   > g'(t) = -\frac{1}{t}, \quad g'(\exp (-\lambda )) = -\exp (\lambda ),
   > $$
   > which results in
   > $$
   > \sqrt{n}(\tilde\lambda - \lambda ) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, \exp (\lambda ) - 1).
   > $$
   > Moreover, by the series expansion for the exponential,
   > $$
   > \exp (\lambda ) - 1 = \sum _{k = 1}^{\infty } \frac{\lambda ^ k}{k!} > \lambda , \quad \text {for all } \lambda > 0,
   > $$
   > so $V(\widehat{\lambda}) < V(\tilde{\lambda})$ for all $\lambda$.

2. As above, argue that both proposed estimators $\widehat{\lambda}$ and $\tilde{\lambda}$ are consistent and asymptotically normal. Then, give their asymptotic variances $V(\widehat{\lambda})$ and $V(\tilde{\lambda})$, and decide if one of them is always bigger than the other.

   Let $X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim }\textsf{Exp}(\lambda )$, for some $\lambda > 0$. Let $\widehat\lambda = \frac{1}{\overline{X}_ n}$ and $\tilde\lambda = -\ln (\overline{Y}_ n)$, where $Y_ i=\mathbf{1}\{ X_ i>1\} , i=1,\ldots ,n$.

   > **Answer**: 
   >
   > $V(\widehat{\lambda}) = \lambda^2\\ V(\tilde{\lambda}) = \exp(\lambda) - 1$
   >
   > **Solution**: 
   >
   > For $\widehat{\lambda}$, by the LLN,
   > $$
   > \overline{X}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[X_1] = \frac{1}{\lambda }.
   > $$
   > With $g(t) = 1/t$, we have that
   > $$
   > \widehat\lambda \xrightarrow [n \to \infty ]{\mathbf{P}} \frac{1}{\mathbb E[X_1]} = \lambda .
   > $$
   > By the CLT,
   > $$
   > \sqrt{n} (\overline{X}_ n - \frac{1}{\lambda }) \sim \mathcal{N}(0,\textsf{Var}(X_1)) = \mathcal{N}\left(0,\frac{1}{\lambda ^2}\right).
   > $$
   > The fact that
   > $$
   > g'(t) = -\frac{1}{t^2}
   > $$
   > together with the Delta Method then yields
   > $$
   > V(\widehat\lambda ) = \lambda ^2.
   > $$
   > For $\tilde{λ}$, first observe that it is the average of Bernoulli variables, and by the LLN,
   > $$
   > \overline{Y}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[Y_1] = \mathbf{P}(X_1 > 1) = \exp (-\lambda ),
   > $$
   > so with $\tilde g(t) = -\log (t)$
   > $$
   > \tilde\lambda = \tilde g(\overline{Y}_ n) \xrightarrow [n \to \infty ]{\mathbf{P}} g(\exp (-\lambda )) = \lambda .
   > $$
   > The CLT yields
   > $$
   > \sqrt{n} (\overline{Y}_ n - \mathbb E[Y_1]) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, \textsf{Var}(Y_1)) = \mathcal{N}(0, \exp (-\lambda ) (1 - \exp (-\lambda )).
   > $$
   > In order to apply the Delta Method for the above $\tilde g(t)$, we compute
   > $$
   > \tilde g'(t) = -\frac{1}{t}, \quad \tilde g'(\exp (-\lambda )) = -\exp (\lambda ),
   > $$
   > which results in 
   > $$
   > \sqrt{n}(\tilde\lambda - \lambda ) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, \exp (\lambda ) - 1).
   > $$
   > In order to compare these two asymptotic variances, first observe that similar to previous part,
   > $$
   > \exp (\lambda ) - 1 \geq \lambda , \quad \text {for all } \lambda > 0,
   > $$
   > and since $ \lambda ^2 < \lambda$ for $\lambda \in (0, 1)$, we have
   > $$
   > \exp (\lambda ) - 1 \geq \lambda ^2, \quad \text {for } \lambda \in (0,1).
   > $$
   > Moreover,
   > $$
   > \exp (1) - 1 = e -1 > 1 = 1^2,
   > $$
   > and
   > $$
   > \frac{d}{d \lambda } (\exp (\lambda ) - 1) = \exp (\lambda ), \quad \frac{d}{d \lambda } \lambda ^2 = 2 \lambda ,
   > $$
   > so that
   > $$
   > \frac{d}{d \lambda } (\exp (\lambda ) - 1) = \exp (\lambda ) \geq 1 + \lambda + \frac{\lambda ^2}{2} > 2 \lambda = \frac{d}{d \lambda } \lambda ^2, \quad \text {for all } \lambda > 0,
   > $$
   > which can be checked by the quadratic formula. This means that for $\lambda \geq 1$,
   > $$
   > \exp (\lambda ) - 1 = e + \int _{1}^{\lambda } \exp (t) \, dt -1 > 1 + \int _{1}^{\lambda } 2 t \, dt = \lambda ^2.
   > $$
   > so $V(\widehat{\lambda}) < V(\tilde{\lambda})$ for all $\lambda$.

3. As above, argue that both proposed estimators $\widehat{p},\, \widetilde{p},$ are consistent and asymptotically normal. Then, give their asymptotic variances $V(\widehat{\lambda})$ and $V(\tilde{\lambda})$, and decide if one of them is always bigger than the other.

   Let $ X_1,\ldots ,X_ n\stackrel{i.i.d.}{\sim }\textsf{Geom}(p) $, for some $p \in (0,1)$. That means that
   $$
   \mathbf{P}(X_1=k)=p(1-p)^{k-1}, \quad \text {for } k = 1, 2, \dots .
   $$
   Let
   $$
   \hat{p} = {1\over \overline{X_n}}
   $$
   and $\tilde{p}$ be the number of ones in the sample divided by $n$.

   > **Answer**: 
   >
   > $V(\widehat{p}) = p^2 (1-p)\\ V(\tilde{p}) = p(1-p)$
   >
   > **Solution**: 
   >
   > By the LLN,
   > $$
   > \overline{X}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[X_1] = \frac{1}{p}.
   > $$
   > Setting
   > $$
   > g(t) = \frac{1}{t},
   > $$
   > we obtain consistency of $ \widehat{p} = g(\overline{X}_ n)$, i.e.,
   > $$
   > \widehat{p} = g(\overline{X}_ n) \xrightarrow [n \to \infty ]{\mathbf{P}} g(\mathbb E[X_1]) = p.
   > $$
   > By the CLT,
   > $$
   > \sqrt{n} (\overline{X}_ n - \frac{1}{p}) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0,\textsf{Var}(X_1)) = \mathcal{N}\left(0,\frac{1-p}{p^2}\right),
   > $$
   > and hence by the Delta Method, together with
   > $$
   > g'\left( \frac{1}{p} \right)^2 = \left( -p^2 \right)^2 = p^4,
   > $$
   > we end up with
   > $$
   > \sqrt{n} (\widehat{p} - p) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, p^2(1-p)),
   > $$
   > So
   > $$
   > V(\widehat{p}) = p^2(1-p).
   > $$
   > For $\tilde{p}$, note that we can write it as
   > $$
   > \tilde p = \overline{Y}_ n, \quad \text {where } Y_ i = \mathbf{1} \{ X_ i = 1\} ,
   > $$
   > so it is again an average over Bernoulli variables. The LLN gives
   > $$
   > \overline{Y}_ n \xrightarrow [n \to \infty ]{\mathbf{P}} \mathbb E[Y_1] = \mathbf{P}(X_1 = 1) = p,
   > $$
   > while the CLT yields
   > $$
   > \sqrt{n} (\overline{Y}_ n - p) \xrightarrow [n \to \infty ]{\mathrm{(D)}} \mathcal{N}(0, \textsf{Var}(Y_1)) = \mathcal{N}(0, p(1-p)).
   > $$
   > Since $p^2 < p$ for $p \in (0,1)$,
   > $$
   > V(\widehat{p}) < V(\tilde p).
   > $$

# 3. Application of Delta Method on Gamma Variables

The Gamma distribution $\text {Gamma}(\alpha ,\beta )$ with parameter $\alpha > 0$, and $\beta > 0$ is defined by the density
$$
f_{\alpha ,\beta }(x)=\frac{\beta ^\alpha }{\Gamma (\alpha ) } x^{\alpha -1} e^{-\beta x}, \quad \text {for all} x\geq 0.
$$
The $\Gamma$ function is defined by
$$
\Gamma (s)=\int _{0}^\infty x^{s-1} e^{-x} dx.
$$
As usual, the constant $\frac{\beta ^\alpha }{\Gamma (\alpha ) }$ is a normalization constant that gives $\int _{0}^{\infty } f_{\alpha ,\beta }(x)dx=1.$

In this problem, let $X_1,\ldots ,X_ n$ be i.i.d. Gamma variables with
$$
\beta =\frac{1}{\alpha }\quad \text {for some } \alpha >0.
$$
That is, $X_1,\ldots ,X_ n\sim \text {Gamma}\left(\alpha ,\frac{1}{\alpha }\right)$ random variables for some $\alpha > 0$. The pdf for $X_i$ is therefore
$$
f_\alpha (x)=\frac{1}{\Gamma (\alpha ) \alpha ^\alpha } x^{\alpha -1} e^{-x/\alpha }, \quad \text {for all } x\geq 0.
$$

1. What is the limit, in probability, of the sample average $\overline{X}_n$ of the sample in terms of $\alpha$? $\overline{X}_ n\xrightarrow [n \to \infty ]{\mathbf{P}}\quad ? $
2. Use the result from the previous problem to give a consistent estimator $\hat{\alpha}$ of $\alpha$ in terms of $\overline{X}_n$.
3. For the Delta method to apply, at what value of $x$ does $g$ need to be continuously differentiable? 
4. Find C.I. for $\alpha$ with asymptotic level $90\%$ using both the "solving" and the "plug-in" methods. Use $n=25$ and $\overline{X}_n = 4.5$. Use $q_{0.05} \approx 1.6448$.

> 1) $\overline{X}_ n\xrightarrow [n \to \infty ]{\mathbf{P}} \alpha^2$
>
> By LLN,
> $$
> \overline{X}_ n\xrightarrow [n \to \infty ]{\mathbf{P}}\mathbb E[X_ i].
> $$
> In general, for $\text{Gamma}(\alpha, \beta)$，
> $$
> \mathbb{E}[X] = {\alpha \over \beta}, \quad \mathsf{Var}(X) = {\alpha \over \beta^2}
> $$
> Hence, for $X_ i\sim \text {Gamma}\left(\alpha ,\frac{1}{\alpha }\right)$, we have
> $$
> \mathbb{E}[X_i] = \frac{\alpha }{1/\alpha }\, =\, \alpha ^2.
> $$
> 2) 
>
> By the continuous mapping theorem, 
> $$
> \hat{\alpha }=\sqrt{\overline{X}_ n}\xrightarrow [\mathbf{P}]{n\to \infty } \sqrt{\alpha ^2}=\alpha, \quad \text{since }\alpha > 0
> $$
> Hence,
> $$
> \hat{\alpha} = \sqrt{\overline{X}_n}
> $$
> 3) 
>
> The Delta method gives
> $$
> \sqrt{n}\left(\hat{\alpha }-\alpha \right)=\sqrt{n}\left(\sqrt{\overline{X}_ n}-\alpha \right)\xrightarrow [d.]{n\to \infty } \mathcal{N}\left(0,\left(g'(\mathbb E[X_ i])\right)^2 \textsf{Var}(X_ i)\right)=\mathcal{N}\left(0,\left(g'(\alpha ^2)\right)^2 \textsf{Var}(X)\right)\qquad  \text{where }\, g(x)=\sqrt{x}
> $$
> If $g$ is continuously differentiable at $\alpha^2$. 
>
> Since $g'(x) = {1\over 2 \sqrt{x}}$ exists and is continuous for all $x > 0$, $g'$ is continuously differentiable at any $\alpha^2$ value. Hence, the Delta method does apply.
>
> To compute the asymptotic variance $\left(g'(\alpha ^2)\right)^2 \textsf{Var}(X_ i)$, we need $g'(\alpha ^2)$ and $\textsf{Var}(X_ i)$, which are as follows
> $$
> g'(\alpha ^2) = {1\over 2 \sqrt{\alpha^2}} = {1\over 2 \alpha}\\
> \textsf{Var}(X) = {\alpha \over \beta^2} = \alpha^3 \quad \text{since }\beta = 1 / \alpha
> $$
> Combined together, the asymptotic variance is
> $$
> \left(g'(\alpha ^2)\right)^2 \textsf{Var}(X_ i) = {1\over 4 \alpha^2}(\alpha^3) = {\alpha \over 4}
> $$
> 4) 
>
> From previous questions we know that
> $$
> \begin{aligned}
> \sqrt{n}\left(\hat{\alpha }-\alpha \right) &\xrightarrow[d.]{n\rightarrow \infty} \mathcal{N}\left(0,\tau ^2\right) \qquad \text {where }\, \tau ^2=\frac{\alpha }{4}\\
> \implies \frac{\sqrt{n}}{\tau }\left(\hat{\alpha }-\alpha \right) &\xrightarrow[d.]{n\rightarrow \infty} \quad \mathcal{N}(0,1) \quad \text{where }\tau^2 = {\alpha \over 4}
> \end{aligned}
> $$
> For large $n$, approximately
> $$
> \mathbf{P}\left(\hat{\alpha }-q_{0.05}\frac{\tau }{\sqrt{n}}<\alpha <\hat{\alpha }+q_{0.05}\frac{\tau }{\sqrt{n}}\right)= 0.9.
> $$
> Plugging in the asymptotic variance $\tau =\sqrt{\alpha }/2$ gives
> $$
> \mathbf{P}\left(\hat{\alpha }-q_{0.05}\frac{\sqrt{\alpha }}{2\sqrt{n}}<\alpha <\hat{\alpha }+q_{0.05}\frac{\sqrt{\alpha }}{2\sqrt{n}}\right)= 0.9.
> $$
> We now go through the three methods of solving for the C.I.:
>
> * Conservative bound: Since $\sqrt{α}$ is not bounded, the conservative bound method does not give a C.I.
>
> * Solving for $α$: 
>   $$
>   \begin{aligned}
>   &\vert \hat{\alpha} - \alpha \vert < q_{0.05} {\tau \over \sqrt{n}} = q_{0.05}{\sqrt{\alpha} \over 2 \sqrt{n}}\\
>   \iff& (\hat{\alpha} - \alpha)^2 < q_{0.05}^2 {\alpha \over 4n}\\
>   \iff& \alpha ^2-\left(2\hat{\alpha }+\frac{q_{0.05}^2}{4n}\right) \alpha +\hat{\alpha }^2 = 0
>   \end{aligned}
>   $$
>   where $\hat{\alpha}^2 = \overline{X}_n = 4.5$, and $q_{0.05} = 1.6448$. Using the quadratic formula or software, we get the C.I.
>   $$
>   \mathcal{I}_{\text {solve}}=[1.89,2.37]
>   $$
>
> * Plug-in: Since $\hat{\alpha }^2=\overline{X}_ n=4.5$, the plug-in C.I. is 
>   $$
>   \begin{aligned}
>   \mathcal{I}_{\text {plug-in}} &= \left[\hat{\alpha }-q_{0.05}\frac{\sqrt{\hat{\alpha }}}{2\sqrt{n}}, \hat{\alpha }+q_{0.05}\frac{\sqrt{\hat{\alpha }}}{2\sqrt{n}}\right]\\
>   &=[1.88, 2.36]
>   \end{aligned}
>   $$
>
> 