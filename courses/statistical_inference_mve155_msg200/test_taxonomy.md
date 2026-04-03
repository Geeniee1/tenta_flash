# Statistical Inference Test Taxonomy

This course dataset now stores two layers on each card:

- `question_type`: the broad study category used for practical filtering
- `primary_test`: the main named test, when the exam question is really a test-selection problem

## Where this differs from the proposed list

The compendium supports most of the list you gave, but two recurring course patterns need to be added or clarified:

- `Paired t-test`: the compendium treats paired samples by reducing to one-sample inference on the differences. In exam practice, this behaves like its own recurring pattern and should be tagged explicitly.
- `Chi-squared test for the variance`: the course also uses one-sample normal-theory variance inference. This appears in the March 20, 2026 exam and fits naturally with the compendium's exact mean and variance inference material.

There is also a practical dataset issue:

- not every exam question is a named hypothesis test
- some questions are mainly about sampling design, point estimation, Bayesian estimation, multiple-testing logic, or regression theory

For those questions, `primary_test` is intentionally left blank and the broad `question_type` carries the study value instead.

## Named test families currently used

- Large-sample test for the mean (Z-test)
- One-sample t-test
- Large-sample test for the mean difference
- Two-sample t-test
- Paired t-test (one-sample t-test on differences)
- Rank sum test
- Signed rank test
- Large-sample test for two proportions
- Fisher's exact test
- Chi-squared test of goodness of fit
- Chi-squared test of homogeneity
- Chi-squared test of independence
- Chi-squared test for the variance
- F-test (One-way ANOVA)
- F-test (Two-way ANOVA)
- F-test (Randomized block design)
- Kruskal-Wallis test
- Friedman's test
- Tests for intercept and slope
- Model utility test
- Generalised likelihood ratio test
- Bayesian hypotheses testing

## Broad non-test categories currently used

- Sampling and design
- Point estimation
- Bayesian inference
- Multiple testing and power
- Theory and foundations
- Regression
