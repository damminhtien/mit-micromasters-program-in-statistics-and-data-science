# Recitation 13. Wald's Test versus Likelihood Ratio Test

Suppose we have a dataset $X_1, ..., X_n$ that is i.i.d. $f_\theta (x) = \theta x^{-\theta - 1} \mathbf{1}_{x > 1}$.

1. Calculate the MLE and Fisher Information for $\theta$.
2. Give the **likelihood ratio test** with level $\alpha = 0.05$ to test if $\theta= 2$.
3. Give **Wald's test** with level $\alpha = 0.05$ to test if $\theta=2$.
4. Assume $n=100$ and $\hat{\theta} = 2.45$. Compute the asymptotic $p$-values of both tests.

> **Review:**
>
> Recall that the **Wald's test** is based on the **asymptotic normal approximation** to the MLE. We have
> $$
> \sqrt{n} \left(\hat{\theta}_{MLE} - \theta\right) \xrightarrow[]{(d)} \mathcal{N}(0, I^{-1}(\theta))\\
> \sqrt{n} \sqrt{I(\theta)} \left(\hat{\theta}_{MLE} - \theta\right) \xrightarrow[]{(d)} \mathcal{N}(0, 1)\\
> {n} {I(\theta)} \left(\hat{\theta}_{MLE} - \theta\right)^2 \xrightarrow[]{(d)} \chi_1^2\\
> {n} {I(\hat{\theta}_{MLE})} \left(\hat{\theta}_{MLE} - \theta\right)^2 \xrightarrow[]{(d)} \chi_1^2
> $$
> The **likelihood ratio test** looks at how much more likely is the alternative hypothesis when compared to the null hypothesis. If
> $$
> \frac{\sup_{\Theta \in \Theta_1} L(X_1, \ldots , X_ n; \Theta )}{L(X_1, \ldots , X_ n; \Theta _0 )} > C
> $$
> We reject the null hypothesis in favor of the alternatives.
>
> Note that
> $$
> \begin{aligned}
> &\frac{\sup_{\Theta \in \Theta_1} L(X_1, \ldots , X_ n; \Theta )}{L(X_1, \ldots , X_ n; \Theta _0 )} > C\\
> \implies & \frac{ L(X_1, \ldots , X_ n; \hat{\Theta}_{MLE} )}{L(X_1, \ldots , X_ n; \Theta _0 )} > C\\
> \implies & 2(\ell(X_1, ..., X_n; \hat{\Theta}_{MLE}) - \ell (X_1, ..., X_n ; \Theta_0)) >  \log C \quad \text{(take the log and multiply by 2)}
> \end{aligned}
> $$
> **Wilk's theorem** states that
> $$
> 2(\ell(X_1, ..., X_n; \hat{\Theta}_{MLE}) - \ell (X_1, ..., X_n ; \Theta_0)) \xrightarrow[]{(d)} \chi_1^2
> $$
> **Solution:**
>
> 1. Find the **MLE**:
>
>    The likelihood is 
>    $$
>    \begin{aligned}
>    L(x_1, ..., x_n; \Theta) &= \prod_{i=1}^n f(x_i ; \Theta)\\
>    &= \prod^n_{i=1} \Theta x_i^{-\Theta-1}\\
>    &= \Theta^n (\prod^n_{i=1}x_i)^{-\Theta-1}\\
>    \end{aligned}
>    $$
>    The log likelihood is
>    $$
>    \begin{aligned}
>    \ell(X_1, ..., X_n ; \Theta) &= \log \left(\Theta^n \left(\prod^n_{i=1}X_i\right)^{-\Theta-1}\right)\\
>    &= n \log \Theta + (-\Theta-1) \sum^n_{i=1} \log X_1\\
>    \end{aligned}
>    $$
>    Take the first derivative and set it to zero
>    $$
>    {d \ell \over d\Theta } = {n \over \Theta} - \sum^n_{i=1} \log X_i = 0\\ 
>    \implies \hat{\Theta} = {n \over \sum^n_{i=1} \log X_i}
>    $$
>    Take the second derivative
>    $$
>    {d ^2 \ell\over d \Theta^2} = - {n \over \Theta^2} < 0
>    $$
>    This tells us that the log likelihood is concave and $\hat{\Theta}$ is a maximizer.
>    $$
>    \hat{\Theta}_{MLE} = {n \over \sum^n_{i=1} \log X_i}
>    $$
>    Find the **Fisher information**:
>    $$
>    I(\Theta) = \mathbb{E}\left[- {d ^2 \ell (X; \Theta)\over d \Theta^2}\right] = \mathbb{E}\left[- \left(- {1\over \Theta^2}\right)\right] = {1\over \Theta^2}
>    $$
>    
> 2. **Likelihood ratio test:**
>
>    Under the null hypothesis,
>    $$
>    2(\ell(X_1, ..., X_n; \hat{\Theta}_{MLE}) - \ell (X_1, ..., X_n ; \Theta_0)) \xrightarrow[]{(d)} \chi_1^2
>    $$
>    The test statistic $T_n$ is
>    $$
>    T_n = 2(\ell(X_1, ..., X_n; \hat{\Theta}_{MLE}) - \ell (X_1, ..., X_n ; \Theta_0))
>    $$
>    Our test is 
>    $$
>    \psi = \mathbb{1}_{(T_n \geq \chi_{1, 0.05}^2)}=\mathbb{1}_{(T_n \geq 3.84)}
>    $$
>    Now we do the test
>    $$
>    H_0: \Theta = 2 \ \ \text{vs.} \ \ H_1: \Theta \neq 2\\
>    $$
>    with the given data:  $\hat{\Theta}_{MLE} = 2.45,\ \  n = 100$.​
>
>    $$
>    \begin{aligned}
>    T_n &= 2(\ell(X_1, ..., X_n; \hat{\Theta}_{MLE}) - \ell (X_1, ..., X_n ; \Theta_0))\\
>    &= 2 \left(n \log \hat{\Theta}_{MLE} + \left(- \hat{\Theta}_{MLE} - 1\right) {n\over \hat{\Theta}_{MLE}} -\left(n \log \Theta_0 + \left(- \Theta_0 - 1\right) {n\over \hat{\Theta}_{MLE}}\right)\right)\\
>    &= 3.85 > 3.45
>    \end{aligned}
>    $$
>    So we reject the null hypothesis.
>
> 3. **Wald's test:** 
>
>    Under the null hypothesis,
>    $$
>    n I(\Theta) (\hat{\Theta}_{MLE} - \Theta_0)^2 \xrightarrow[]{(d)} \chi_1^2\\
>    \implies
>    n {1\over \hat{\Theta}_{MLE}^2} (\hat{\Theta}_{MLE} - \Theta_0)^2 \xrightarrow[]{(d)} \chi_1^2
>    $$
>    Where the test statistic $T_n'$​ is
>    $$
>    T_n'  =n {1\over \hat{\Theta}_{MLE}^2} (\hat{\Theta}_{MLE} - \Theta_0)^2
>    $$
>    Our test is to reject the null when $T_n$ is greater than or equal to some quantile of a $\chi^2_1$.
>    $$
>    \psi' = \mathbb{1}_{(T_n' \geq \chi_{1,0.05}^2)}= \mathbb{1}_{(T_n' \geq 3.84)}
>    $$
>    where $\chi^2_{1, 0.05}$ is $1-0.05$ quantile of a $\chi_1$.
>
>    If we want a probability of $0.05$​​​​ of rejecting the null hypothesis under the null hypothesis (null is true), we mean we have a probability of $0.05$​​ of making a type I error.
>
>    Now we do the test
>    $$
>    H_0: \Theta = 2 \ \ \text{vs.} \ \ H_1: \Theta \neq 2\\
>    $$
>    with the given data:  $\hat{\Theta}_{MLE} = 2.45,\ \  n = 100$.​
>
>    $$
>    T_n'  =n {1\over \hat{\Theta}_{MLE}^2} (\hat{\Theta}_{MLE} - \Theta_0)^2 = 100  {1\over 2.45^2} (2.45-2)^2 = 3.37 < 3.84
>    $$
>    So we fail to reject the null hypothesis.

