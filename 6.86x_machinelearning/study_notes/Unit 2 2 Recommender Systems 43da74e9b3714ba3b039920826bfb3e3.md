# Unit 2.2: Recommender Systems

> **Status: source-grounded summary.** This page is a learner-authored companion to the local recommender-system material.

Source: [local recommender-system lecture](../lectures/Lec7_RecommendSys.pdf).

## 1. User-item data

Let R_ui be the rating or interaction of user u with item i. The matrix is usually sparse: most R_ui values are unobserved. Keep an observation mask Omega; an unobserved entry is not the same thing as a measured zero rating.

Useful baselines include a global mean mu, user bias b_u, and item bias b_i. A common latent-factor model is:

R_hat_ui = mu + b_u + b_i + p_u^T q_i.

Here p_u and q_i are low-dimensional user and item vectors. Their dot product represents compatibility in a learned latent space.

## 2. Fitting the factors

Train only on observed entries with a regularized objective:

sum over (u, i) in Omega of (R_ui - R_hat_ui)^2, plus lambda times the squared L2 penalties for all user/item factors and biases.

Stochastic gradient descent updates one observed interaction at a time. Alternating least squares fixes the item parameters while solving for users, then reverses the roles. Both approaches optimize a non-convex joint problem and can depend on initialization, rank, learning rate, and regularization.

The repository's [Netflix project](../projects/project4_netflix/) is a related educational matrix-completion example using Gaussian-mixture EM rather than the latent-factor objective above. Its [EM implementation](../projects/project4_netflix/em.py) is reusable, but its zero-as-missing convention and spherical-Gaussian assumptions must be made explicit.

## 3. Evaluation without leakage

Randomly hiding entries can be misleading when interactions are time-dependent or user-dependent. Prefer a split that matches deployment:

- time split for forecasting future interactions;
- user-held-out split for cold-start behavior;
- interaction-held-out split when predicting missing entries for known users and items.

Do not use validation or test ratings to compute normalization statistics, user/item biases, feature selection, or hyperparameter choices. For explicit ratings, RMSE and MAE are common; for ranked recommendations, evaluate top-k precision/recall, hit rate, or NDCG and define the candidate set.

## 4. Limitations and responsible use

- Sparse observations are usually missing-not-at-random: a rating may be missing because a user never encountered the item.
- New users and new items have no learned factors without side information (cold start).
- Popularity bias can reinforce what is already exposed.
- Offline metrics do not prove user satisfaction or causal impact.
- Course datasets may have redistribution restrictions; see the repository [provenance guide](../../docs/PROVENANCE.md).

## Practical checklist

1. Define the interaction and the observation mask.
2. Establish a mean/bias baseline before adding latent factors.
3. Choose rank and regularization using a deployment-shaped validation split.
4. Compare against a simple baseline and report the split and metric.
5. Inspect errors by user, item popularity, time, and missingness pattern.
