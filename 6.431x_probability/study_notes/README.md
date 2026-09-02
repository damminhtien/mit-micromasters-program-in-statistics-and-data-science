# 6.431x study notes

This index turns the Probability archive into a deliberate learning path. The unit pages are learner-authored summaries and source links; they are not a replacement for the official course or textbook.

## Unit map

| Unit | Focus | Local note |
| --- | --- | --- |
| 1 | Probability models and axioms | [Unit 1](Unit%201%20Probability%20models%20and%20axioms%20b67b1a47557449e78f97d2073dfd1d98.md) |
| 2 | Conditioning and independence | [Unit 2](Unit%202%20Conditioning%20and%20Independence%207137eff04f6c489d9d2c37c1ae7dd0c8.md) |
| 3 | Counting | [Unit 3](Unit%203%20Counting%207cbf2339e5f34195a84d3d67426faa8f.md) |
| 4 | Discrete random variables | [Unit 4](Unit%204%20Discrete%20random%20variables%2041cf21b82aa44d9098005a109263cc64.md) |
| 5 | Continuous random variables | [Unit 5](Unit%205%20Continuous%20random%20variables%202ef777e2df5e4110aba854247a590fb8.md) |
| 6 | Further topics on random variables | [Unit 6](Unit%206%20Further%20topics%20on%20random%20variables%201fd874a2e1504c40be7a078a50794e40.md) |
| 7 | Bayesian inference | [Unit 7](Unit%207%20Bayesian%20inference%209da02c265b674e0fb6c3a70c7d160d37.md) |
| 8 | Limit theorems and classical statistics | [Unit 8](Unit%208%20Limit%20theorems%20and%20classical%20statistics%207244e311a3714e47908f4d403e1d90b8.md) |
| 9 | Bernoulli and Poisson processes | [Unit 9](Unit%209%20Bernoulli%20and%20Poisson%20processes%203e0aa58afd1a48ec8192244f4674da63.md) |
| 10 | Markov chains | [Unit 10](Unit%2010%20Markov%20chains%20dbea4041e4214472a31f4b3638a187d4.md) |

## Problem-solving checklist

1. Define the sample space and the random variables before writing a probability.
2. Decide whether the problem needs conditioning, independence, or a change of representation.
3. State whether a random variable is discrete or continuous; do not confuse a density with a probability.
4. For an expectation or variance, check integrability and use linearity before expanding algebra.
5. For asymptotic approximations, state the i.i.d., finite-mean, or finite-variance assumptions that justify them.
6. For a Markov chain, fix the row/column convention for the transition matrix before multiplying it.

## Formula spine

- Total probability: P(A) = sum_b P(A | B = b) P(B = b) for a discrete partition.
- Bayes' rule: P(A | B) = P(B | A) P(A) / P(B), when P(B) > 0.
- Conditional expectation: E[X] = E[E[X | Y]].
- Total variance: Var(X) = E[Var(X | Y)] + Var(E[X | Y]).
- CLT pattern: sqrt(n) (X_bar - mu) / sigma is approximately standard normal for large n under the usual assumptions.
- Markov evolution: with row vectors, pi_(t+1) = pi_t P and an invariant distribution satisfies pi = pi P.

For the course calendar, mathematical background, and source links, use the [course README](../README.md). For formula-level review, use the [cheat sheet](Cheat%20sheet%204394aea41da8498689ae6b6e033fc865.md), then verify every result against the relevant unit page.
