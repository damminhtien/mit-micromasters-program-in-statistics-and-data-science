# Unit 3: Methods of estimation

> **Status: source-grounded summary.** This page is a learner-authored companion to the local Unit 3 lecture. It summarizes the core estimators and states the assumptions that control their use.

[Local source: Unit 3 estimation lecture](../lectures/U03_Estimation.pdf)

## 1. Estimation setup

Let X_1, ..., X_n be i.i.d. observations from a model P_theta, where theta belongs to the parameter space Theta. An estimator is a statistic theta_hat_n = T(X_1, ..., X_n); after observing data, its realized value is an estimate. The distinction matters because bias, variance, and consistency describe the random estimator over repeated samples.

Useful diagnostics:

- Bias: Bias_theta(theta_hat) = E_theta[theta_hat] - theta.
- Variance: Var_theta(theta_hat).
- Mean-squared error: MSE_theta(theta_hat) = Var_theta(theta_hat) + Bias_theta(theta_hat)^2.
- Consistency: theta_hat_n converges to theta in probability (or almost surely, when the stronger statement is proved).

An unbiased estimator is not automatically best: a small bias can be worthwhile if it reduces variance and therefore MSE.

## 2. Maximum likelihood estimation

For a density or mass function p_theta, the likelihood of observed data x = (x_1, ..., x_n) is L_n(theta; x) = product_i p_theta(x_i).

The log-likelihood is ell_n(theta; x) = log L_n(theta; x). The maximum-likelihood estimator chooses theta_hat_MLE in the parameter space that maximizes L_n, equivalently ell_n.

The log form is numerically and algebraically preferable because it converts products into sums. A practical workflow is: write the support and likelihood, simplify the log-likelihood, differentiate only when the parameter is interior, check boundaries, and compare candidate optima.

### Examples

- If X_i ~ Bernoulli(p), then p_hat_MLE = X_bar.
- If X_i ~ Normal(mu, sigma^2) with both parameters unknown, then mu_hat_MLE = X_bar and sigma2_hat_MLE = n^(-1) sum_i (X_i - X_bar)^2. The variance MLE is biased downward; the n - 1 denominator gives the usual unbiased sample variance.

MLE is invariant under one-to-one transformations: if theta_hat maximizes the likelihood, then g(theta_hat) maximizes the likelihood for g(theta), provided the parameterization is used consistently.

## 3. Fisher information and asymptotic normality

For one observation, write ell_theta(X) = log p_theta(X). Under regularity conditions, Fisher information is:

I(theta) = Var_theta(partial ell_theta / partial theta) = -E_theta[second partial derivative of ell_theta].

For a d-dimensional parameter, I(theta) is a matrix and n i.i.d. observations contribute n I(theta). When the model is identifiable, the true parameter is interior, the support does not change with theta, and the usual differentiability and moment conditions hold:

sqrt(n) * (theta_hat_MLE - theta_star) converges in distribution to Normal(0, I(theta_star)^(-1)).

This is a large-sample approximation, not a finite-sample identity. Boundary parameters, non-identifiability, singular information, or changing support can invalidate the usual result.

## 4. Method of moments

The k-th population moment is m_k(theta) = E_theta[X^k], while the sample moment is m_hat_k = n^(-1) sum_i X_i^k. With d unknown parameters, the method-of-moments estimator solves:

m_j(theta_hat) = m_hat_j for j = 1, ..., d.

Examples:

- Bernoulli(p): m_1(p) = p, so p_hat = X_bar.
- Normal(mu, sigma^2): m_1 = mu and m_2 = mu^2 + sigma^2, so mu_hat = X_bar and sigma2_hat = mean(X^2) - X_bar^2.

The equations can have no solution, multiple solutions, or a solution outside the parameter space. Always check admissibility after solving.

## 5. M-estimators

An M-estimator minimizes an empirical loss:

theta_hat_n = argmin_theta [ n^(-1) sum_i rho(X_i, theta) ].

MLE is an M-estimator with rho(x, theta) = -log p_theta(x). Other choices of rho target means, medians, quantiles, or robust estimates. The choice of loss is a modeling decision: it controls sensitivity to outliers and determines which population quantity is being estimated.

## Estimation checklist

1. State the sampling model and parameter space.
2. Write the likelihood or loss using only observed data.
3. Check identifiability, boundaries, and whether the solution lies in Theta.
4. Report bias, variance, MSE, or asymptotic uncertainty when relevant.
5. Treat a normal approximation as conditional on its regularity assumptions.

For related confidence intervals and hypothesis tests, continue to [Unit 4](Unit%204%20Parametric%20hypothesis%20testing%2042f16cd1dba14e4c8e42799978eb757d.md).
