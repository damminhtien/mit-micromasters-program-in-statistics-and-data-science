# Unit 2: Foundation of inference

Unit 2 materials - Lecture 3: [[slide]](https://courses.edx.org/asset-v1:MITx+18.6501x+1T2022+type@asset+block@lectureslides_Chap2annotlast_attrib.pdf)

# Confidence Intervals

Building the confidence interval of asymptotical level $1-\alpha=0.95 (\alpha=5\%)$ ****by solving for $p$ 

Recall that $R_1,...,R_n \sim Ber(p)$ for some unknown parameter $p$, and we estimate $p$ using the estimator 

$$
\hat{p}=\bar{R_n}=\frac{1}{n}\sum_{i=1}^n R_i
$$

As in the method using a conservative bound, our starting point is the result of the CTL:

$$
\lim _{n\to \infty } \mathbf{P}\left(\left|\sqrt{n}\frac{\overline{R}_ n-p}{\sqrt{p(1-p)}}\right|< q_{\alpha /2}\right) =1-\alpha 
$$

In this second method, we solve for values of $p$ that satisfy the inequality  
$\left| \sqrt(n) \frac{\bar{R_n}-p}{\sqrt{p(1-p)}} \right| < q_{\alpha/2}$

$$
\displaystyle \Longrightarrow \displaystyle p^2\left(1+ \frac{q_{\alpha /2}^2}{n}\right)-p\left(2\overline{R}_ n+\frac{q_{\alpha /2}^2}{n}\right)+\left(\overline{R}_ n\right)^2<0.
$$

The quadratic formula gives the roots $\displaystyle \frac{-B\pm \sqrt{B^2-4AC}}{2A}$

# Models of Convergence

Three types model of convergence

1. Convergence almost surely
2. Convergence in probability
3. Convergence in distribution