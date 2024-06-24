# Recitation 14. Chi Squared Goodness of Fit Test

Suppose we have $X_1, \dots , X_ n$ iid with a discrete and finite sample space. We wish to perform hypothesis tests to:

* **Task 1:** Understand whether the data was generated with a distribution with a particular PMF $p^0$.
* **Task 2:** Understand whether the data was generated with a distribution in a family of distributions $\{ \mathbf {P}_\theta \}$​​, where $\theta \in \R^d$​​ models the family of distribution $\{ \mathbf {P}_\theta \}$​​.

In this recitation, we derive the chi-squared goodness of fit test statistic to perform **Task 1** and generalize this test statistic to perform **Task 2**.

1. What is the categorical statistical model and Goodness of fit hypothesis test?
2. What is the reparameterization, Wald's test, and Fisher information matrix?
3. What is the Chi-squared goodness of fit test if ${p}^0$​​​​ equals to a particular PMF?
4. What is the Chi-squared goodness of fit test if ${p}^0$​ belongs to a family of PMFs?

> **Solution:**
>
> 1. Recall *Categorical Statistical Model* is written as $\left(\{a_1, ..., a_k\}, \{\mathbf{P}_{\mathbf{p}}\}_{p \in \Delta_K}\right)$​​​​​​​​​​​​​​ where $\mathbf{p} = [p_1, ...p_K]^T$​​​​​​​​ is the parameter vector, $\Delta_K$​​​​​ is the probability simplex in $\R^K$​​​, $\mathbf{p} \in \R^K$​​​, $\sum\limits^{K-1}_{i=1} p_i =1,\  p_i \geq 0$​.
>
>    Let $X$​​ be a categorical random variable with sample space $\{a_1...a_K\}$​​, then $\mathbf{P}[X=a_i] = p_i$​​, $\mathbf{p}=\begin{bmatrix} p_1 \\ \vdots \\ p_K \end{bmatrix}$​​.
>
>    Recall the *Goodness of fit test*: observe $X_1...X_n$​ be i.i.d. Let $p^0$ be the distribution that generated $X_1 ... X_n$
>    $$
>    H_0: p = p^0\\
>    H_1: p \neq p^0
>    $$
>    
>    Recall the *Wald's Test*: If $\hat{\Theta} =$ MLE and $\Theta \in \R^K$, asymptotic normality is (under the null hypothesis $H_0$)
>    $$
>    n(\theta^0 - \hat{\theta})^T I(\theta^0)(\theta^0 - \hat{\theta}) \xrightarrow[n \rightarrow \infty]{(d)} \chi_k^2
>    $$
>    
>    * $\hat{\mathbf{p}} = [{N_1 \over n} ... {N_K \over n}]^T$​​, where $N_i = \# $​ observations of $a_i$​.
>    
>    * The Fisher information is not invertible since
>      $$
>      (p^0 - \hat{p})^T \mathbb{1} = \sum^{K-1}_{i=1} (p_i^0 - \hat{p}_i) = 0
>      $$
>    
> 2. 
>
> 2. **Reparameterization** of the categorical statistical model:
>
>    Let $\left(\{a_1... a_K\}, \mathbf{P}_{\overline{\mathbf{p}}}\right)$​​​ where $\overline{\mathbf{p}}$​​​ is $K-1$​​​ dimensional $\mathbb{P}[X = a_K] = 1 - \sum_{i=1}^{K-1} \overline{p}_i$​​​. Our test is
>    $$
>    H_0: \overline{p} = \overline{p}^0\\
>    H_1: \overline{p} \neq \overline{p}^0
>    $$
>    where $\overline{\mathbf{p}}^0 = [p_1^0 ... p_{K-1}^0]^T$​​​.
>
>    **Wald's Test**:
>
>    Observe $X_1, ..., X_n$, we need $\overline{\mathbf{p}}_{MLE}, \ \overline{\mathbf{p}}^0, \ I(\overline{\mathbf{p}}^0)$, to write 
>    $$
>    n (\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE})^T I(\overline{\mathbf{p}}^0) (\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE})
>    $$
>    The log-likelihood of $X_1, ..., X_n$:
>    $$
>    \ell (X_1,..., X_n, \overline{\mathbf{p}}) = N_1 \log(\overline{\mathbf{p}_1}) + ... + N_{K-1} \log(\overline{\mathbf{p}}_{K-1})+ N_{K} \log(1- \sum^{K-1}_{i=1}\overline{\mathbf{p}}_{i})
>    $$
>    No matter whether we leave the last coordinate $N_{K} \log(1- \sum^{K-1}_{i=1}\overline{\mathbf{p}}_{i})$​​​​ or not, we have the same  $\overline{\mathbf{p}}_{MLE}$​​​, which is
>    $$
>    \overline{\mathbf{p}}_{MLE} = \left[{N_1 \over n} ... {N_{K-1} \over n}\right]^T
>    $$
>    So
>    $$
>    \hat{p}[X = a_K] = {N_K \over n}
>    $$
>    The Fisher information matrix is
>    $$
>    I(\overline{\mathbf{p}}) = \begin{bmatrix}{1\over \overline{p_1}} + {1 \over \overline{p_K}} & &  & {1\over \overline{p}_K}\\ &{1\over \overline{p_2}} + {1 \over \overline{p_K}} & &  \\ & & ... & \\ {1\over \overline{p}_K} & & & {1\over \overline{p_{K-1}}} + {1 \over \overline{p_K}} \end{bmatrix}_{(K-1) \times (K-1)}
>    $$
>    where $\overline{p}_K = 1 - \sum\limits^{K-1}_{i=1} \overline{p}_i$. Except for the diagonal line, all values equal to ${1\over \overline{p}_K}$​ .
>
>    Equivalently, the Fisher information matrix can be rewritten as
>    $$
>    I(\overline{\mathbf{p}}) = \text{diag} \left(\left[{1\over \overline{p}_1} ... {1\over \overline{p}_{K-1}}\right]^T\right) + {1\over \overline{p}_K} \mathbb{1}_{K-1}\mathbb{1}^T_{K-1}
>    $$
>
> 3. Plugging in the Fisher information, the Chi-squared Goodness of fit is calculated as
>    $$
>    \begin{aligned}
>    n \ \left(\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE}\right)^T I(\overline{\mathbf{p}}^0) \left(\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE}\right) &= n \ \left(\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE}\right)^T \text{diag}\left(\left[{1\over \overline{\mathbf{p}}_1^0} ... {1\over \overline{\mathbf{p}}_{K-1}^0}\right]^T\right)  \left(\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE}\right)\\
>    &+ {n \over \overline{\mathbf{p}}_K^0} \ \left(\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE}\right)^T \left(\mathbb{1}_{K-1} \cdot \mathbb{1}_{K-1}^T \right)  \left(\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}_{MLE}\right)\\
>    &= n \sum^{K-1}_{i=1} { (\overline{\mathbf{p}}^0_i - \overline{\mathbf{p}}^0_{i,MLE})^2 \over \overline{\mathbf{p}_i}^0} + {n \over \overline{\mathbf{p}}_K^0} \ \left[\overline{\mathbf{p}}_{K, MLE} - \overline{\mathbf{p}}_{K}^0 ... \overline{\mathbf{p}}_{K, MLE} - \overline{\mathbf{p}}_{K}^0 \right]^T \cdot \left(\overline{\mathbf{p}}^0 - \overline{\mathbf{p}}^0_{MLE} \right)\\
>    &= n \sum^{K-1}_{i=1} {({\mathbf{p}}^0_i - \hat{\mathbf{p}}^0_{i})^2  \over {\mathbf{p}_i}^0} + n  {({\mathbf{p}}^0_K - \hat{\mathbf{p}}^0_{K})^2  \over {\mathbf{p}_K}^0}
>    \end{aligned}
>    $$
>    So the test statistic of Chi-squared test is
>    $$
>    T_n = n \sum^{K-1}_{i=1} {({\mathbf{p}}^0_i - \hat{\mathbf{p}}^0_{i})^2  \over {\mathbf{p}_i}^0} + n  {({\mathbf{p}}^0_K - \hat{\mathbf{p}}^0_{K})^2  \over {\mathbf{p}_K}^0}\rightarrow \chi_{K-1}^2
>    $$
>
> 4. We test the hypothesis
>    $$
>    H_0: p \in \{\mathbf{P}_{\Theta}\}_{\Theta \in \R^d}\\
>    H_1: p \notin \{\mathbf{P}_{\Theta}\}_{\Theta \in \R^d}
>    $$
>    Suppose $p$ is a binomial distribution with parameter $(k, p)$. The PMF is
>    $$
>    \mathbf{P}(X=k)= {K \choose k}p^k (1-p)^{K-k}
>    $$
>    Let $\{a_0...a_K\}, f_\Theta(a_i) = \mathbf{P}[X=a_i]$, where $\hat{\Theta}$ is MLE of $\Theta$. Observe $X_1, ..., X_n$, MLE = $\hat{p} = \left[ {N_0\over n} ... {N_K\over n} \right]^T$. The test statistic is (under $H_0$)
>    $$
>    T_n = n \sum^K_{i=1} {\left({N_i \over n} - f_{\hat{\Theta}}(a_i) \right)^2\over f_{\hat{\Theta}}(a_i)} \xrightarrow[n \rightarrow \infty]{(d)} \chi^2_{(k+1)-1-d}
>    $$

