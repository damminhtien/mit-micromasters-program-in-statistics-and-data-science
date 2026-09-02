# 6.419x study notes

This index groups the Data Analysis notes by module and points to the source-grounded lecture summaries. The notebooks and reports are separate practice artifacts; they should not be treated as official solutions.

## Module map

| Module | Theme | Local entry point | Status |
| --- | --- | --- | --- |
| M0 | Experiments, testing, regression, and gradient descent | [Module 1 notes](Module%201%20Review%20Statistic,%20Correlation,%20Regression%20c7068a9ec92547979292c5d1fe6b1466.md) | Notes |
| M1 | High-dimensional data | [Module 2 notes](Module%202%20High-Dimensional%20Data%2063d558637495458cadad1934360f2ddf.md) | Lectures 6–8 source-grounded |
| M2 | Network analysis | [Module 3 notes](Module%203%20Network%20Analysis%20ae3c43d05729443d9af793ccde2f20ea.md) | Notes and projects |
| M3 | Time series | [Module 4 notes](Module%204%20Time%20Series%20a743b3785e5f4c45891efc1fb689fbdd.md) | Notes |
| M4 | Gaussian processes | [Material resources](Material%20Resources%2006486b3ba96e4b9aa7e14d8f5cf1d924.md) | External links; local note incomplete |

## Analytical workflow

1. Define the scientific question and distinguish observational from experimental evidence.
2. Inspect scale, missingness, dependence, and the (n)-versus-(p) regime.
3. Choose a representation before choosing a model: transform, center, scale, and reduce dimension when justified.
4. Separate training, validation, and test decisions; do not select features using the test set.
5. Report uncertainty, sensitivity to distance or tuning choices, and failure modes.

The [course README](../README.md) contains the calendar and project runbook. The [reusable project gallery](../../docs/PROJECTS.md) maps the accompanying notebooks to their data and limitations.
