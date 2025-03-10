# Recitation 10. Gamma Method of Moments

Let $X_1, ..., X_n \stackrel{i.i.d}{\sim} \text{Gamma}(\alpha, \beta)$​​, the PDF is
$$
f(x;\alpha, \beta) = {\beta^{\alpha} \over \Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}, \quad x > 0
$$
The **moment generating function**:
$$
M_x(t) = (1- {t \over \beta})^{-\alpha}, \quad (t < \beta)
$$

1. Find first $4$​ moments of $X \sim \text{Gamma}(\alpha, \beta)$​.
2. Use Method of Moments to find estimators for $\alpha, \beta$.
3. Find the asymptotic distribution of $\hat{a}$.

> **Solution:**
>
> 1. Recall that the first moment is $M_x^{(1)}(0) = \mathbb{E}[X^1]$​​​​, the $k$​​​th moment is $M_x^{(k)}(0) = \mathbb{E}[X^k]$​​​​.
>
>    First, we compute the 1st moment:
>    $$
>    \begin{aligned}
>    M_x'(t) &= {d\over dt} (1- {t \over \beta})^{-\alpha} = -\alpha \cdot \left( 1- {t \over \beta} \right)^{-\alpha - 1}\left(- {1\over \beta}\right)\\
>    \mathbb{E}[X] &= M_x'(0) = {\alpha \over \beta}
>    \end{aligned}
>    $$
>    Then, we compute the 2nd moment:
>    $$
>    \begin{aligned}
>    M_x''(t) &= {d^2\over dt^2} (1- {t \over \beta})^{-\alpha} ={d\over dt} {\alpha \over \beta} \left(1- {t \over \beta}\right)^{-\alpha - 1} = {\alpha(\alpha + 1) \over \beta^2} \left( 1- {t \over \beta} \right)^{-\alpha - 2}\\
>    \mathbb{E}[X^2] &= M_x''(0) = {\alpha(\alpha + 1) \over \beta^2}
>    \end{aligned}
>    $$
>    So the 3rd moment:
>    $$
>    \mathbb{E}[X^3] = M_x'''(0) = {\alpha(\alpha + 1)(\alpha + 2) \over \beta^3}
>    $$
>    And the 4th moment:
>    $$
>    \mathbb{E}[X^4] = M_x''''(0) = {\alpha(\alpha + 1)(\alpha + 2)(\alpha + 3) \over \beta^4}
>    $$
>
> 2. From (1) we have
>    $$
>    m_1 = {\alpha \over \beta}, \quad m_2 = {\alpha^2 + \alpha \over \beta^2}
>    $$
>    and
>    $$
>    \overline{X} = {1\over n} \sum^n_{i=1}X_i, \ \overline{X^2} = {1\over n} \sum^n_{i=1}X_i^2
>    $$
>    Let $\alpha = g_1(m_1, m_2), \ \beta = g_2(m_1, m_2)$​​​, since $m_1^2 = {\alpha^2 \over \beta^2}, \ m_2-  m_1^2 = {\alpha \over \beta^2}$​​,
>    $$
>    g_1(m_1, m_2) = {m_1^2 \over m_2 - m_1^2} = {\alpha^2/\beta^2 \over \alpha/ \beta^2} = \alpha\\
>    g_2(m_1, m_2) = {m_1 \over m_2 - m_1^2} = {\alpha/ \beta \over \alpha/ \beta^2} = \beta
>    $$
>    Then,
>    $$
>    \hat{\alpha} = g_1(\overline{X}, \overline{X^2}) = {\overline{X^1}^2 \over \overline{X^2} - \overline{X^1}^2}\\
>    \hat{\beta} = g_2(\overline{X}, \overline{X^2}) = {\overline{X^1} \over \overline{X^2} - \overline{X^1}^2}
>    $$
>
> 3. We first apply the **multivariate CLT**
>    $$
>    \sqrt{n} \left(\begin{pmatrix}\overline{X}\\ \overline{X^2} \end{pmatrix} - \begin{pmatrix} \mathbb{E}[X_1]\\ \mathbb{E}[X_1^2] \end{pmatrix} \right) \xrightarrow[]{(d)} \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix} , \begin{pmatrix}\text{Var}(X_1) & \text{Cov}(X_1, X_1^2) \\ \text{Cov}(X_1, X_2^2) & \text{Var}(X_1^2) \end{pmatrix} \right)
>    $$
>    where $\begin{pmatrix}\overline{X}\\ \overline{X^2} \end{pmatrix}  = {1\over 2}\sum^n_{i=1}\begin{pmatrix}{X_1}\\ {X_1^2} \end{pmatrix} $​.
>
>    Since $m_k = \mathbb{E}[X_1^k]$​​, $\text{Cov}(X_1, X_1^2) = \mathbb{E}[X^3] - \mathbb{E}[X_1] \mathbb{E}[X_1^2]$, we can rewrite the multivariate CLT to
>    $$
>    \sqrt{n} \left(\begin{pmatrix}\overline{X}\\ \overline{X^2} \end{pmatrix} - \begin{pmatrix} m_1\\ m_2 \end{pmatrix} \right) \xrightarrow[]{(d)} \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix} , \Sigma \right)
>    $$
>    where $\Sigma = \begin{pmatrix} m_2 - m_1^2 & m_3 - m_1m_2\\ m_3 - m_1m_2 & m_4 - m_2^2  \end{pmatrix} $.
>
>    Let $g \begin{pmatrix}\overline{X} \\ \overline{X^2} \end{pmatrix} = {\overline{X}^2 \over \overline{X^2} - \overline{X}^2}$​​​​, we use **multivariate delta method**.
>    $$
>    \sqrt{n} \left(g \begin{pmatrix}\overline{X}\\ \overline{X^2} \end{pmatrix} - g\begin{pmatrix} m_1\\ m_2 \end{pmatrix} \right) \xrightarrow[]{(d)} \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \nabla g^T\begin{pmatrix}m_1 \\ m_2 \end{pmatrix}\Sigma \nabla g\begin{pmatrix}m_1 \\ m_2 \end{pmatrix} \right)
>    $$
>    Let calculate $\nabla g\begin{pmatrix}m_1 \\ m_2 \end{pmatrix}$​​,
>    $$
>    \nabla g\begin{pmatrix}m_1 \\ m_2 \end{pmatrix} =\nabla \left({m_1^2 \over m_2 - m_1^2}\right) = \begin{pmatrix}{m_1(m_2 - m_1^2)+ m_1^2(-2m_1)\over (m_2 - m_1^2)^2} \\ {m_1^2\over (m_2 - m_1^2)^2} \end{pmatrix}
>    $$
>    Therefore, we can compute the asymptotic variance
>    $$
>    \sqrt{n} \left(g \begin{pmatrix}\overline{X}\\ \overline{X^2} \end{pmatrix} - g\begin{pmatrix} m_1\\ m_2 \end{pmatrix} \right) \xrightarrow[]{(d)} \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \nabla g^T\begin{pmatrix}m_1 \\ m_2 \end{pmatrix}\Sigma \nabla g\begin{pmatrix}m_1 \\ m_2 \end{pmatrix} \right)\\
>    \iff \sqrt{n} \left(\hat{\alpha} - \alpha \right) \xrightarrow[]{(d)} \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix}{m_1(m_2 - m_1^2)+ m_1^2(-2m_1)\over (m_2 - m_1^2)^2} \\ {m_1^2\over (m_2 - m_1^2)^2} \end{pmatrix}^T \begin{pmatrix} m_2 - m_1^2 & m_3 - m_1m_2\\ m_3 - m_1m_2 & m_4 - m_2^2  \end{pmatrix} \begin{pmatrix}{m_1(m_2 - m_1^2)+ m_1^2(-2m_1)\over (m_2 - m_1^2)^2} \\ {m_1^2\over (m_2 - m_1^2)^2} \end{pmatrix} \right)\\
>    $$



