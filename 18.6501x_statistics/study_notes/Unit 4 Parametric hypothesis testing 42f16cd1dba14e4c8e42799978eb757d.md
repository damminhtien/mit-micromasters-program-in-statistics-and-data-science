# Unit 4: Parametric hypothesis testing

> **Status: source-grounded summary.** This page is a learner-authored companion to the local Unit 4 lecture and focuses on the decisions that are commonly confused in practice.

[Local source: Unit 4 parametric hypothesis-testing lecture](../lectures/U04_Parametric_hypo_test.pdf)

## 1. The testing problem

Specify a null hypothesis H0 and an alternative H1 before looking at the result. A test is a rule that maps the observed data to “reject H0” or “do not reject H0”. The alternative may be one-sided or two-sided, and the direction must follow the scientific question.

The test statistic should have a known or approximated distribution under H0. A critical region is chosen so that the probability of rejecting H0 when H0 is true is at most alpha. This alpha is the level of the test.

## 2. Errors, power, and p-values

- Type I error: reject H0 when H0 is true. Its probability is controlled by alpha.
- Type II error: do not reject H0 when H1 is true. Its probability depends on the actual parameter value.
- Power at parameter theta: probability of rejecting H0 when theta is the data-generating value; power = 1 - Type II error.

A p-value is the probability, assuming H0, of obtaining a test statistic at least as extreme as the observed one in the pre-specified direction. It is not the probability that H0 is true, and it is not the size of the effect.

## 3. A practical test workflow

1. Define the parameter, H0, H1, and the direction of the alternative.
2. State the sampling model and any nuisance parameters.
3. Choose a statistic whose null distribution is known or well approximated.
4. Set alpha before evaluating the data.
5. Compute the statistic and p-value, or compare it with the critical value.
6. Report the decision, effect estimate, uncertainty interval, and assumptions.

“Do not reject H0” means the evidence was insufficient at the chosen level; it does not prove H0.

## 4. Confidence intervals and optimality

For regular one-parameter tests, inverting a family of level-alpha tests produces a confidence set with nominal coverage 1 - alpha. This connection is useful, but the confidence level is a long-run coverage statement, not the posterior probability that one fixed interval contains the parameter.

The Neyman-Pearson principle identifies the most powerful test for a simple null against a simple alternative at a fixed level through a likelihood-ratio rule. For composite hypotheses, nuisance parameters and uniformly most powerful tests require additional structure.

## 5. What can go wrong

- A statistically significant result can be practically unimportant when the effect is tiny.
- A non-significant result can reflect low power, high variance, or a small sample rather than evidence of no effect.
- Choosing the tail, alpha, or model after seeing the data invalidates the nominal calibration.
- Multiple testing increases the chance of at least one false positive; use a declared correction or control target.
- Non-robust parametric tests can fail under dependence, heavy tails, outliers, or a misspecified sampling model.

Keep the [estimation summary](Unit%203%20Methods%20of%20estimation%20d2e2d1f847394b4180c34cb673bbbf87.md) nearby: a test should be connected to an effect estimate and its uncertainty, not reported as a p-value alone.
