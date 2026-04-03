# Statistical Inference Review Notes

This draft dataset was generated from the local PDF archive only.
Each card contains a broad study category plus a suggested primary test derived from the compendium and the exam wording.
Questions that are mainly about estimation, design, or theory are left without a named primary test on purpose.

## 140323_aila_sarkka | March 2023 Exam

### Q1
- `question_type`: `Sampling and design`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: maximum likelihood, random sampling, simple random sampling, stratified sampling
- `confidence`: `high`
- `suggested answer`: No single hypothesis test. This is a foundations question about MLE for a proportion, random versus simple random sampling, and the variance of a stratified sample mean under proportional allocation.
- `prompt excerpt`: a) Derive the maximum likelihood estimator for the population proportion and show that it is an unbiased and consistent estimator for the population proportion. b) What are the similarities and differences between random sampling and simple...

### Q2
- `question_type`: `Independent two-sample comparison`
- `primary_test`: `Two-sample t-test`
- `alternative_tests`: Rank sum test
- `tags`: two-sample t-test, rank-sum test, one-sided alternative, independent samples
- `confidence`: `high`
- `suggested answer`: Use an independent two-group comparison. The primary parametric method is a one-sided two-sample t-test, and the requested non-parametric check is a rank-sum style comparison because the two groups of mothers are independent.
- `prompt excerpt`: A group of nurses wants to study if the number of maternity care visits (before birth) has a positive effect on the birth weight of the child. The data (see the table and histograms below) consist of 10 mothers who had had 5 or fewer matern...

### Q3
- `question_type`: `One-sample mean inference`
- `primary_test`: `Large-sample test for the mean (Z-test)`
- `alternative_tests`: none
- `tags`: one-sample z-test, type II error, power, known variance
- `confidence`: `high`
- `suggested answer`: This is a one-sample mean test with known variance, so the core method is the one-sample z-test. The task specifically asks for the type II error or power calculation when the true mean is 9.
- `prompt excerpt`: Assume that we have a sample of size 20 from a normal distribution with mean µ and variance σ2 = 4. We would like to test the null hypothesis H0 : µ = 10 against H1 : µ ̸= 10 at the significance level 0.05. Assume that the true expected val...

### Q4
- `question_type`: `Two-way ANOVA`
- `primary_test`: `F-test (Two-way ANOVA)`
- `alternative_tests`: none
- `tags`: two-way ANOVA, interaction, factorial design
- `confidence`: `high`
- `suggested answer`: Use a two-way ANOVA with detergent and temperature as factors, including the interaction term. The question asks for the model, hypotheses, completed ANOVA table, and interpretation of main effects plus interaction.
- `prompt excerpt`: We want to study how the choice of detergent and water temperature affect the dirt removal of laundry by using two types of detergents (deter) and three different temperatures (temp) by using the analysis of variance. The values of the resp...

### Q5
- `question_type`: `Bayesian inference`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: Poisson-Gamma conjugacy, Bayesian estimation, conjugate prior
- `confidence`: `high`
- `suggested answer`: This is a Bayesian Poisson-Gamma conjugacy question. The main tasks are deriving the posterior under a Gamma prior, explaining why conjugate priors are convenient, and reflecting on what a large sample changes.
- `prompt excerpt`: We have a sample ( x1, x2, ..., xn) drawn from the Poisson distribution Pois(λ) and want to estimate λ by using Bayesian inference. a) Show that gamma distribution is a conjugate prior for the Poisson distribution. The density function of Y...

## 080623_aila_sarkka | June 2023 Exam

### Q1
- `question_type`: `Point estimation`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: method of moments, maximum likelihood, unbiasedness, consistency
- `confidence`: `high`
- `suggested answer`: No single test. This is a point-estimation foundations question covering the method of moments, maximum likelihood, and the definitions of unbiased and consistent estimators.
- `prompt excerpt`: We have a parametric model (probability density f) determined by one parameter θ and we wish to estimate θ from a given random sample (x1, ..., xn). a) Give the basic idea behind the method of moments to estimate θ. b) Give the basic idea b...

### Q2
- `question_type`: `Categorical data analysis`
- `primary_test`: `Chi-squared test of independence`
- `alternative_tests`: none
- `tags`: chi-squared test of independence, contingency table
- `confidence`: `high`
- `suggested answer`: Use a chi-squared test of independence. The data come from one contingency table relating defect type to production shift, so the key question is whether those two categorical variables are associated.
- `prompt excerpt`: A total of 309 furniture defects were recorded and the defects were classified into four types: A, B, C, and D. At the same time, each piece of furniture was identified by the production shift in which it was manufactured. These counts are ...

### Q3
- `question_type`: `Paired-sample comparison`
- `primary_test`: `Paired t-test (one-sample t-test on differences)`
- `alternative_tests`: Signed rank test
- `tags`: paired t-test, confidence interval, signed-rank test, matched pairs
- `confidence`: `high`
- `suggested answer`: Treat this as a matched-pairs problem because each driver responds to both sign types. The main parametric method is a paired t-test, with a confidence interval for the mean difference and a non-parametric signed-rank alternative.
- `prompt excerpt`: An experiment was conducted to compare the mean reaction times to two types of traffic signs: prohibitive (no left turn) and permissive (left turn only). Ten drivers were included in the experiment. The mean reaction times (in milliseconds)...

### Q4
- `question_type`: `One-sample mean inference`
- `primary_test`: `Large-sample test for the mean (Z-test)`
- `alternative_tests`: none
- `tags`: one-sample z-test, sample size, power, known variance
- `confidence`: `high`
- `suggested answer`: This is a one-sample one-sided z-test with known variance. The exam asks for the sample size required to achieve a target power when the true mean is 1.5.
- `prompt excerpt`: Let us have a random sample from a normal distribution with mean µ and variance 100. We test the hypothesis H0 : µ = 0 against H1 : µ > 0. Determine the sample size n needed to achieve 80% power at significance level 5% when the true mean i...

### Q5
- `question_type`: `Regression`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: multiple regression, coefficient interpretation, model fit
- `confidence`: `high`
- `suggested answer`: Use multiple linear regression with mpg as the response and disp, hp, and wt as predictors. The focus is model specification, coefficient interpretation, assumptions, and the meaning of R-squared style fit summaries.
- `prompt excerpt`: We would like to compare 32 different car models in terms of mileage per gallon (mpg), cylinder displacement (disp), horse power (hp), and weight of the car (wt). Particularly, we would like to establish the relationship between ”mpg” as a ...

## 150823_aila_sarkka | August 2023 Exam

### Q1
- `question_type`: `Bayesian inference`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: Bayesian estimation, prior choice, conjugate prior
- `confidence`: `high`
- `suggested answer`: No frequentist test is being selected here. This is a Bayesian foundations question about the basic idea of the Bayesian approach, how a prior is chosen, and what a conjugate prior means.
- `prompt excerpt`: All three questions below (a-c) concern the Bayesian approach to estimate parameters: a) Give the idea behind the Bayesian approach. b) How do you choose the prior distribution? c) What is a conjugate prior? (5p)

### Q2
- `question_type`: `Multiple testing and power`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: multiple testing, binomial count of false positives, independence assumption
- `confidence`: `high`
- `suggested answer`: This is a multiple-testing question. Model the number of false significant findings among 50 independent intervals and compute the probability that at least two intervals falsely suggest an effect.
- `prompt excerpt`: We investigate the effect of a new drug on 50 different factors by computing 50 95% confidence intervals, one for the mean value of each factor (based on the sample size 40 in each case). Suppose that the drug has no effect on any of the 50...

### Q3
- `question_type`: `Two-proportion inference`
- `primary_test`: `Large-sample test for two proportions`
- `alternative_tests`: Fisher's exact test
- `tags`: confidence interval for difference in proportions, two-sample proportion z-test, Fisher's exact test
- `confidence`: `high`
- `suggested answer`: Use inference for two proportions. The main methods are a confidence interval for the difference in proportions and a two-sample proportion z-test, with Fisher's exact test as the small-sample exact fallback.
- `prompt excerpt`: To investigate whether the proportion of red M&M candies in the plain and peanut variants of the candy is the same, a random sample of each variant was collected. In the sample of 56 plain candies, 12 were red, and in the sample of 32 peanu...

### Q4
- `question_type`: `Randomized block design`
- `primary_test`: `F-test (Randomized block design)`
- `alternative_tests`: Friedman's test
- `tags`: randomized block ANOVA, Friedman test, blocked design
- `confidence`: `high`
- `suggested answer`: This is a randomized block design because every driver rates every mirror. The primary method is blocked ANOVA, and a Friedman-type non-parametric backup is the natural alternative if normal-model assumptions fail.
- `prompt excerpt`: An experiment was conducted to compare the glare characteristics of four types of rearview mirrors of cars. Ten drivers were randomly selected to participate in the experiment. Each driver was exposed to glare produced by a headlight locate...

### Q5
- `question_type`: `Regression`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: correlation, confidence interval for correlation
- `confidence`: `high`
- `suggested answer`: This is a correlation and linear-association question. The task is to interpret the estimated correlation between exam and project scores and understand what a confidence interval that includes zero implies.
- `prompt excerpt`: To pass a course one has to pass an exam and do a project. The teacher has graded the exams and the projects and computed (estimated) the correlation coefficient between the two scores. (The correlation coefficient between two stochastic va...

## 120324_tony_johansson | March 2024 Exam

### Q1
- `question_type`: `Sampling and design`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: random sampling, simple random sampling, unbiasedness, consistency
- `confidence`: `high`
- `suggested answer`: No single hypothesis test. This question is about sampling design and the sample mean: random versus simple random sampling, unbiasedness, consistency, and how those choices affect standard errors and confidence interval width.
- `prompt excerpt`: No calculations are required for this problem. Suppose we are interested in the average age in a population of size N. (a) (2p) Explain the difference in using a random sample and a simple random sample for this problem. (b) (2p) What does ...

### Q2
- `question_type`: `Categorical data analysis`
- `primary_test`: `Chi-squared test of homogeneity`
- `alternative_tests`: Chi-squared test of independence
- `tags`: chi-squared test of homogeneity, chi-squared test of independence, design critique
- `confidence`: `medium`
- `suggested answer`: The design critique comes first, but the intended inferential tool is a chi-squared test for a board-type-by-success table. If the experiment were properly designed with separate board groups, the natural method would be a chi-squared test of homogeneity.
- `prompt excerpt`: Johanna is shopping for a new skateboard, and is choosing between three boards of different types; vert, street and all–round. For each board, she attempts the same trick over and over again until she feels satisfied, and records the number...

### Q3
- `question_type`: `Point estimation`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: maximum likelihood, bias, standard error, consistency
- `confidence`: `high`
- `suggested answer`: No single hypothesis test. This is a point-estimation question centered on maximum likelihood for a shifted exponential family, plus the bias, standard error, and consistency of the resulting estimators.
- `prompt excerpt`: Consider a distribution family D(α, β) where α, β > 0, characterized by the probability density function f(x) =  βe−β(x−α), x ≥ α, 0, x < α. In words, X ∼ D (α, β) if it can be written as X = α + Y where Y ∼ Exp(β). You will be helped by k...

### Q4
- `question_type`: `Goodness of fit`
- `primary_test`: `Custom goodness-of-fit test (review needed)`
- `alternative_tests`: none
- `tags`: custom discrete test, counting argument, null versus larger-support alternative
- `confidence`: `medium`
- `suggested answer`: This is not one of the standard named tests from the course list, but it is still a hypothesis-testing design problem. Build a custom test around the number of distinct messages observed under the null model m = 8 versus the larger-support alternative.
- `prompt excerpt`: (6p) A magic 8–ball is a fortune–telling toy which containsm ∈ N distinct hidden messages. When shaken, it randomly displays one of the m messages. Propose a test for H0 : m = 8 against H1 : m > 8 based on shaking the ball n = 8 times. Choo...

### Q5
- `question_type`: `Independent two-sample comparison`
- `primary_test`: `Rank sum test`
- `alternative_tests`: none
- `tags`: rank-sum test, independent samples, distribution comparison
- `confidence`: `medium`
- `suggested answer`: Treat this as an independent two-group comparison with a heavy-skew or outlier-sensitive outcome. The safer first-choice method is a rank-sum test comparing the platform price distributions rather than a mean-based t-test.
- `prompt excerpt`: Sandra sells art through two different online platforms (A and B). Each platform is auction–based, meaning the price paid is determined by customers. To tell which platform tends to end up with a higher price, she creates twentyfour copies ...

## 270824_aila_sarkka | August 2024 Exam

### Q1
- `question_type`: `Theory and foundations`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: credibility interval, p-value, chi-squared homogeneity, chi-squared independence
- `confidence`: `high`
- `suggested answer`: No single test needs to be selected. This is a theory question about what a credibility interval means, how to define a p-value, and how the chi-squared tests of homogeneity and independence differ in design and interpretation.
- `prompt excerpt`: a) Define a 95% credibility interval. b) Define the p-value of a test. c) What is the difference between the χ2 test of homogeneity and the χ2 test of independence? (6p)

### Q2
- `question_type`: `One-sample mean inference`
- `primary_test`: `Large-sample test for the mean (Z-test)`
- `alternative_tests`: none
- `tags`: confidence interval for mean, sample size, known variance
- `confidence`: `high`
- `suggested answer`: This is one-sample mean inference with known standard deviation. The core tasks are reading the confidence level implied by a given interval and solving for the sample size needed to keep the same width at 95% confidence.
- `prompt excerpt`: We have conducted a study where we want to estimate the mean weight of a specific species of sheep. We assume that the weight is normally distributed with standard deviation 5 (kg). Based on the weights of 100 (independent) sheep, we obtain...

### Q3
- `question_type`: `Point estimation`
- `primary_test`: `Two-sample t-test`
- `alternative_tests`: none
- `tags`: pooled variance, two-sample t-test, unbiasedness, consistency
- `confidence`: `high`
- `suggested answer`: No new test is being chosen; this is about the pooled variance estimator used inside the equal-variance two-sample t-test. The question focuses on why that estimator is unbiased and consistent.
- `prompt excerpt`: A pooled sample variance is used to estimate the common population variance in a two sample t-test. • Show that the pooled sample variance is an unbiased estimator for the population variance. • The pooled sample variance is also a consiste...

### Q4
- `question_type`: `One-way ANOVA and non-parametric alternatives`
- `primary_test`: `F-test (One-way ANOVA)`
- `alternative_tests`: Kruskal-Wallis test
- `tags`: one-way ANOVA, Kruskal-Wallis test
- `confidence`: `high`
- `suggested answer`: Use one-way ANOVA to compare the four pesticide groups, and use the Kruskal-Wallis test as the requested non-parametric check. The design has four independent treatment groups with one quantitative response.
- `prompt excerpt`: A farmer compared the effect of four types of pesticides (Pest 1-4) in order to avoid unpleasant plant pests. Each pesticide was used to treat 5 different land areas. The table below gives the counts of larvae for the four pesticides. Pest ...

### Q5
- `question_type`: `Regression`
- `primary_test`: `Tests for intercept and slope`
- `alternative_tests`: none
- `tags`: simple linear regression, quadratic regression, t-test for slope
- `confidence`: `high`
- `suggested answer`: This is a regression-modeling question. Start with simple linear regression, interpret the slope test and fit quality, then consider a quadratic extension because the scatter plot suggests curvature.
- `prompt excerpt`: We investigate whether ”value added per work-hour” (value below) is affected by the size of the store (size below) by using regression analysis. The variable ”value added per work-hour” is defined as the surplus available to pay for labor, ...

## 180325_aila_sarkka | March 2025 Exam

### Q1
- `question_type`: `Sampling and design`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: finite population correction, optimal allocation, blocking, randomization
- `confidence`: `high`
- `suggested answer`: No single hypothesis test. This is a sampling-and-design question covering finite population correction, stratified allocation formulas, and when blocking plus randomization should be used in experimental design.
- `prompt excerpt`: a) When should one use the finite population correction? b) In stratified sampling with k strata, the sample mean becomes ¯X = kX j=1 wj ¯Xj, where wi is the stratum fraction and ¯Xi the sample mean in stratum i, i = 1, ..., k. Compute the ...

### Q2
- `question_type`: `Bayesian inference`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: Poisson MLE, Gamma prior, credible interval, confidence interval versus credible interval
- `confidence`: `high`
- `suggested answer`: This is Bayesian inference for a Poisson model. The tasks combine MLE, a Gamma prior, posterior derivation, one way to form a credible interval, and the interpretation gap between credible and confidence intervals.
- `prompt excerpt`: Let us have a sample x1, ..., xn from Pois(µ) distribution with the probability mass function P (X = x) = (µx/x!) e−µ, x = 0, 1, ... a) Find the maximum likelihood estimate for µ. b) Use a Gamma prior to derive a posterior distribution and ...

### Q3
- `question_type`: `Two-proportion inference`
- `primary_test`: `Large-sample test for two proportions`
- `alternative_tests`: none
- `tags`: two-sample proportion z-test, one-sided test, p-value threshold
- `confidence`: `high`
- `suggested answer`: Use a one-sided two-proportion comparison because the claim is that heavy-duty packaging lowers the damage rate. The question asks both for the significance test at 0.05 and for the smallest significance level that would still reject.
- `prompt excerpt`: To test the effectiveness of protective packaging, a company shipped 1200 orders in regular packaging, of which 20 arrived in damaged condition, and 1500 orders in heavy-duty packaging, of which 15 arrived in damaged condition. a) Based on ...

### Q4
- `question_type`: `One-way ANOVA and non-parametric alternatives`
- `primary_test`: `F-test (One-way ANOVA)`
- `alternative_tests`: Kruskal-Wallis test
- `tags`: one-way ANOVA, Kruskal-Wallis test
- `confidence`: `high`
- `suggested answer`: This is another four-group comparison problem. Start with one-way ANOVA on the pesticide groups, then use the Kruskal-Wallis test as the non-parametric comparison and discuss the boxplot evidence.
- `prompt excerpt`: A farmer used analysis of variance to compare the effect of four types of pesticides (Pest 1-4) in order to avoid unpleasant plant pests. Each pesticide was used to treat 5 different land areas. The table below on the left gives the counts ...

### Q5
- `question_type`: `One-sample mean inference`
- `primary_test`: `Large-sample test for the mean (Z-test)`
- `alternative_tests`: none
- `tags`: one-sample z-test, sample size, power, known variance
- `confidence`: `high`
- `suggested answer`: This is a one-sample z-test with known variance under a one-sided alternative. The exam asks for the rejection region, the sample size that gives 90% power when the true mean is delta, and the limiting behavior as delta goes to zero.
- `prompt excerpt`: Assume you have a sample x1, ..., xn of normal random variables with mean µ and known variance σ2 = 9 and want to test H0 : µ = 0 against H1 : µ > 0. at significance level α = 0.05. a) Compute the rejection region (which depends on n). b) A...

### Q6
- `question_type`: `Regression`
- `primary_test`: `Tests for intercept and slope`
- `alternative_tests`: Model utility test
- `tags`: multiple regression, coefficient significance, model fit
- `confidence`: `high`
- `suggested answer`: Use multiple linear regression for the Happiness response. The focus is writing the model, interpreting which covariates matter, understanding overall fit, and stating the residual assumptions needed for inference.
- `prompt excerpt`: We have a dataset of 156 countries, that contains information about the Happiness index (Happiness) that can be explained by the social support from the state (Social), healthy life expectancy (Healthy), freedom to make choices in life (Fre...

## 280825_aila_sarkka | August 2025 Exam

### Q1
- `question_type`: `Point estimation`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: unbiasedness, consistency, sample mean
- `confidence`: `high`
- `suggested answer`: No single test. This is a core estimator-properties question: identify the two important properties and show that the sample mean has them under the usual random-sample assumptions.
- `prompt excerpt`: a) What are the two important properties of a point estimator? b) Show that the sample mean has these properties. (5p)

### Q2
- `question_type`: `Independent two-sample comparison`
- `primary_test`: `Large-sample test for the mean difference`
- `alternative_tests`: none
- `tags`: two-sample z-test, power, sample size, equal variances
- `confidence`: `high`
- `suggested answer`: This is an independent two-group mean comparison with known variance structure, framed as a sample-size and power calculation. The target procedure is the one-sided two-sample normal-theory test for the difference in means.
- `prompt excerpt`: We would like to compare the means µ1 and µ2 of two (independent) samples of equal size. Let the alternative hypothesis be one-sided ( µ1 > µ2), and the variables normally distributed with a common variance σ2. Determine the sample size n n...

### Q3
- `question_type`: `Multiple testing and power`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: multiple testing, at least two false positives, independence assumption
- `confidence`: `high`
- `suggested answer`: This is a multiple-testing problem. Count how often 95% intervals miss the normal value when all null effects are actually true, and make the independence assumptions explicit.
- `prompt excerpt`: We investigate the effect of a new drug on 50 different factors by computing 50 95% confidence intervals for the mean values of these factors based on sample size 40 for each effect. Assume that the method has no effect on any of the 50 fac...

### Q4
- `question_type`: `Independent two-sample comparison`
- `primary_test`: `Two-sample t-test`
- `alternative_tests`: Rank sum test
- `tags`: two-sample t-test, rank-sum test, one-sided alternative, independent samples
- `confidence`: `high`
- `suggested answer`: Use an independent two-group comparison. The parametric method is a one-sided two-sample t-test for fertilizer versus no fertilizer, and the non-parametric companion is a rank-sum style test because the samples are independent.
- `prompt excerpt`: A group of ecologists study the effect of a fertilizer on plant growth. They gave this fertilizer to a group of plants (Group A) and no fertilizer to another group of plants (Group B). The growth of plants in millimeters, over six weeks, an...

### Q5
- `question_type`: `Two-way ANOVA`
- `primary_test`: `F-test (Two-way ANOVA)`
- `alternative_tests`: none
- `tags`: two-way ANOVA, interaction, factorial experiment
- `confidence`: `high`
- `suggested answer`: This is a two-way factorial experiment with three dosage levels for each active ingredient. Use two-way ANOVA with interaction to write the model, fill the table, and interpret the factor and interaction effects.
- `prompt excerpt`: The amount of improvement of a genetic disease is measured for 18 patients who are randomly assigned to the nine experimental configurations, with two patients to each configuration, corresponding to three dosage levels of each of the activ...

### Q6
- `question_type`: `Regression`
- `primary_test`: `Tests for intercept and slope`
- `alternative_tests`: none
- `tags`: multiple regression, coefficient t-tests, prediction interval
- `confidence`: `high`
- `suggested answer`: Use multiple linear regression with media advertisement and point-of-sale cost as predictors. The tasks are significance testing for coefficients and a prediction-style calculation for a new supermarket.
- `prompt excerpt`: It was studied how the sale of a product ( y) is affected by media advertisement costs ( x1) and point-of-sale costs ( x2) by using multiple regression. Sixteen stores were selected for the test. a) The sample correlation coefficient comput...

## 200326_aila_sarkka | March 2026 Exam

### Q1
- `question_type`: `Sampling and design`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: stratified sampling, proportional allocation, confidence interval, allocation strategy
- `confidence`: `high`
- `suggested answer`: No single hypothesis test. This is a stratified-sampling design question about proportional allocation, how to build a confidence interval for the population mean from stratified samples, and how that compares with simple random sampling.
- `prompt excerpt`: Last year, 5000 students were enrolled in a small college. We are given a list of their names, and for each person we are also told whether they come directly from high school (Group A), whether they have a degree already (Group B) or wheth...

### Q2
- `question_type`: `Categorical data analysis`
- `primary_test`: `Chi-squared test of independence`
- `alternative_tests`: none
- `tags`: chi-squared test of independence, odds ratio, contingency table
- `confidence`: `high`
- `suggested answer`: Use a chi-squared test of independence on the education-by-number-of-children table. The follow-up asks for an odds ratio interpretation comparing college education with the chance of having more than three children.
- `prompt excerpt`: A random sample of 200 married men, all retired, were classified according to education and number of children: Number of children Education 0-1 2-3 Over 3 Elementary 14 36 32 Secondary 20 42 16 College 12 18 10 a) Test, at significance lev...

### Q3
- `question_type`: `Independent two-sample comparison`
- `primary_test`: `Two-sample t-test`
- `alternative_tests`: Rank sum test
- `tags`: two-sample t-test, rank-sum test, independent samples
- `confidence`: `high`
- `suggested answer`: Treat this as an independent two-group comparison because different cars received radial and belted tires. The question asks you to choose between a normal-theory two-sample test and a non-parametric rank-based alternative after checking distributional assumptions.
- `prompt excerpt`: The manager of a taxi company is trying to decide whether it is better to use radial tires ( x) or regular belted tires ( y) in terms of fuel economy. Twelve cars were equipped with radial tires and driven over a test course and another set...

### Q4
- `question_type`: `One-sample normal inference`
- `primary_test`: `One-sample t-test`
- `alternative_tests`: Chi-squared test for the variance
- `tags`: normality assessment, one-sample t-test, chi-squared test for variance
- `confidence`: `high`
- `suggested answer`: This is a one-sample normal-theory inference problem. First assess whether a normal model is reasonable, then perform a one-sided one-sample t-test for the mean and a chi-squared test for the variance under normality.
- `prompt excerpt`: Assume that you have a sample x1, ..., xn of size n = 15, from a distribution with mean µ and variance σ2. Your goal is to find the distribution of Xi’s (i.e. the corresponding random variables). You have the following information about the...

### Q5
- `question_type`: `Bayesian inference`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: negative binomial MLE, Beta conjugate prior, Bayesian estimation
- `confidence`: `high`
- `suggested answer`: This is Bayesian inference for a Negative Binomial model with known r. The main ideas are the MLE for p, Beta conjugacy for p, and the resulting posterior-based estimate or interval logic.
- `prompt excerpt`: The random variable X follows a Negative Binomial (NB) distribution with parameters ( r, p), r ∈ N = {0, 1, ...}, p ∈ (0, 1), i.e. X ∼ NB(r, p), if P(X = k) = k + r − 1 k  (1 − p)kpr for k ∈ N. Intuitively, the NB distribution can be seen...

### Q6
- `question_type`: `Regression`
- `primary_test`: `No single named test`
- `alternative_tests`: none
- `tags`: simple linear regression, maximum likelihood, regression line property
- `confidence`: `high`
- `suggested answer`: This is a simple linear regression derivation question. Use the likelihood or least-squares algebra to show the intercept formula and then interpret the geometric consequence for the fitted regression line.
- `prompt excerpt`: Consider a simple linear regression model Y = β0 + β1x + σZ, Z ∼ N(0, 1), σ > 0. Assume you have observed some i.i.d. data from this model which we denote by (x1, y1), ...,(xn, yn). a) Show that the maximum likelihood estimate for β0 equals...
