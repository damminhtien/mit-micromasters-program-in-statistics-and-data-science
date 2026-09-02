# Unit 2.1: Nonlinear Classification and Linear Regression

> **Status: source-grounded summary.** This page is a learner-authored companion to the local optimization and nonlinear-classification lectures.

Sources: [optimization and regularization lecture](../lectures/Lec4_GeneralizedLinear.pdf) and [feature-map/kernel lecture](../lectures/Lec7_RecommendSys.pdf).

## 1. Feature maps turn nonlinear problems into linear ones

A linear score has the form f(x) = w^T x + b, so its decision boundary is a hyperplane in the original feature space. A feature map phi(x) creates a new representation and fits f(x) = w^T phi(x) + b. The boundary can therefore be nonlinear in x.

Polynomial features are a simple example: a quadratic map can represent terms such as x_1^2, x_1 x_2, and x_2^2. The trade-off is that the feature dimension can grow quickly, increasing computation and the risk of fitting noise.

## 2. Kernel methods

If an algorithm uses transformed data only through inner products, replace phi(x)^T phi(z) with a kernel K(x, z). A valid kernel must produce a positive-semidefinite Gram matrix on every finite sample. Common choices include polynomial and Gaussian/RBF kernels.

For a kernelized binary classifier, a prediction can be written as sign of sum_i alpha_i y_i K(x_i, x) + b. The representation is powerful but less transparent than the original features, and evaluating all training-point interactions can be expensive for large n.

## 3. Regularized objectives

Many models in the course share the pattern:

J(theta) = average training loss + (lambda / 2) * squared L2 norm of w.

The loss fits the data; the penalty discourages large weights and controls generalization. The intercept is commonly excluded from the penalty. Larger lambda means a simpler, more strongly regularized model, but the best value must be selected using validation data rather than the test set.

For least-squares regression, ridge regression minimizes:

average squared residual + lambda * squared L2 norm of w.

With an intercept handled separately, solve the regularized linear system rather than explicitly inverting a matrix.

For a support-vector classifier with y_i in {-1, +1}, the hinge-loss objective is:

average of max(0, 1 - y_i (w^T x_i + b)) + (lambda / 2) * squared L2 norm of w.

## 4. Optimization and validation

- Gradient descent uses the full objective; stochastic or mini-batch updates use a noisy estimate of its gradient.
- Scale features before distance-based, kernel, or regularized models; otherwise units with large numerical scales dominate.
- Fit preprocessing, feature selection, and hyperparameters inside the training fold. Applying them before the split leaks information.
- Use a validation set or cross-validation for lambda, kernel parameters, polynomial degree, and stopping rules. Keep the test set for one final assessment.

## Common failure modes

1. A high-degree feature map can interpolate noise and make generalization worse.
2. An RBF kernel is sensitive to its bandwidth and to feature scaling.
3. Training loss is not evidence of test performance.
4. A linear-looking plot after projection does not prove that the original problem is linearly separable.
5. A lower squared error does not automatically mean a better decision boundary or a more useful scientific model.

The [nonlinear-classification project](../projects/mnist/part1/kernel.py) provides a concrete place to inspect feature maps and kernels. Keep the assumptions above visible when adapting it.
