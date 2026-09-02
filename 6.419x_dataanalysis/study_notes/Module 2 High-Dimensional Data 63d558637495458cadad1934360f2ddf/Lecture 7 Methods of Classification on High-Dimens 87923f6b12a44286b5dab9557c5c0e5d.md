# Lecture 7: Methods of Classification on High-Dimensional Data

> **Status: source-grounded summary.** This page paraphrases the local high-dimensional classification lecture and adds a reproducible decision checklist.

Source: [local classification lecture](../../lectures/M1%20L2%20Classification%20of%20Hig-Dimensional%20Data.pdf).

## 1. Data representation

Write the data as an n by p matrix X, with row x_i and class label y_i in {1, ..., K}. High-dimensional settings often have p comparable to or larger than n, correlated features, and unstable covariance estimates. Centering and scaling must be fitted on the training data only.

Classification asks for a rule y_hat(x). It is useful to distinguish a model for class probabilities from a discriminant score: a score can classify well without being a calibrated probability.

## 2. Main model families

### Linear and quadratic discriminant analysis

LDA models each class as Gaussian with a shared covariance matrix. The resulting discriminant boundaries are linear. QDA allows a class-specific covariance and therefore gives quadratic boundaries, but it estimates many more parameters and is more fragile when p is large relative to n.

Reduced-rank LDA projects observations into a subspace that separates class means. With K classes, the discriminative mean subspace has dimension at most K - 1; for larger K, PCA on class means can help visualize the leading directions.

### Logistic regression

For two classes, logistic regression models the log-odds:

log(p(x) / (1 - p(x))) = beta_0 + beta^T x.

The default decision threshold 0.5 is a choice, not a law. With class imbalance or asymmetric costs, select a threshold using validation data.

### Support-vector machines

For y_i in {-1, +1}, a soft-margin SVM balances margin size and violations. Its objective is a regularized hinge loss, where the hinge term is max(0, 1 - y_i (w^T x_i + b)).

## 3. Validation and reporting

- Use a held-out test set or cross-validation; leave-one-out is an option when data are scarce.
- Fit scaling, PCA, feature selection, and model tuning inside each training fold.
- Report a confusion matrix and error rate; for imbalanced classes also report per-class recall/precision or a class-balanced metric.
- Compare to a simple baseline, such as the majority class, before interpreting a complex classifier.
- Preserve class proportions in splits when stratification is appropriate.

## 4. Failure modes

1. QDA can become singular or high-variance when covariance matrices are poorly estimated.
2. Correlated or unscaled features can dominate distances and discriminants.
3. Perfect separation can make unregularized logistic estimates unstable or diverge.
4. Selecting genes/features on all data before validation leaks label information.
5. A low error rate can hide systematic failure on a minority class.

For a notebook workflow, see [Analysis1](../../projects/Analysis1.ipynb) and the [reusable project gallery](../../../docs/PROJECTS.md).
