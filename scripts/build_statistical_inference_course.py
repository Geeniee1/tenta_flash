from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader


COURSE_DIR = Path(__file__).resolve().parents[1] / "courses" / "statistical_inference_mve155_msg200"
QUESTION_PATTERN = re.compile(r"(?m)^\s*(\d+)\.\s+")

QUESTION_TYPE_LABELS = {
    "sampling_design": "Sampling and design",
    "point_estimation": "Point estimation",
    "bayesian_inference": "Bayesian inference",
    "power_and_multiple_testing": "Multiple testing and power",
    "one_sample_mean_inference": "One-sample mean inference",
    "one_sample_normal_inference": "One-sample normal inference",
    "independent_two_group_comparison": "Independent two-sample comparison",
    "paired_two_group_comparison": "Paired-sample comparison",
    "two_proportion_inference": "Two-proportion inference",
    "categorical_table_inference": "Categorical data analysis",
    "randomized_block_design": "Randomized block design",
    "multi_group_comparison": "One-way ANOVA and non-parametric alternatives",
    "two_way_factorial_design": "Two-way ANOVA",
    "regression": "Regression",
    "goodness_of_fit": "Goodness of fit",
    "theory_and_foundations": "Theory and foundations",
}

DIRECT_TEST_LABELS = {
    "one-sample z-test": "Large-sample test for the mean (Z-test)",
    "one-sample t-test": "One-sample t-test",
    "one-sample proportion z-test": "Large-sample test for the proportion",
    "binomial test": "Binomial test",
    "sign test": "Sign test",
    "two-sample z-test": "Large-sample test for the mean difference",
    "two-sample t-test": "Two-sample t-test",
    "rank-sum test": "Rank sum test",
    "signed-rank test": "Signed rank test",
    "two-sample proportion z-test": "Large-sample test for two proportions",
    "Fisher's exact test": "Fisher's exact test",
    "chi-squared test of goodness of fit": "Chi-squared test of goodness of fit",
    "chi-squared test of homogeneity": "Chi-squared test of homogeneity",
    "chi-squared test of independence": "Chi-squared test of independence",
    "McNemar's test": "McNemar's test",
    "one-way ANOVA": "F-test (One-way ANOVA)",
    "two-way ANOVA": "F-test (Two-way ANOVA)",
    "randomized block ANOVA": "F-test (Randomized block design)",
    "Kruskal-Wallis test": "Kruskal-Wallis test",
    "Friedman test": "Friedman's test",
    "paired t-test": "Paired t-test (one-sample t-test on differences)",
    "t-test for slope": "Tests for intercept and slope",
    "coefficient significance": "Tests for intercept and slope",
    "coefficient t-tests": "Tests for intercept and slope",
    "generalised likelihood ratio test": "Generalised likelihood ratio test",
    "Bayesian hypotheses testing": "Bayesian hypotheses testing",
    "chi-squared test for variance": "Chi-squared test for the variance",
    "custom discrete test": "Custom goodness-of-fit test (review needed)",
}


EXAMS = [
    {
        "id": "140323_aila_sarkka",
        "title": "March 2023 Exam",
        "date": "2023-03-14",
        "examiner": "Aila Sarkka",
        "source_candidates": ["140323_aila_sarkka.pdf", "ExamMarch2023.pdf"],
        "notes": "Draft mapping generated from the local PDF archive; review suggested methods before final release.",
        "cards": [
            {
                "question": "1",
                "question_type": "sampling_design",
                "tags": ["maximum likelihood", "random sampling", "simple random sampling", "stratified sampling"],
                "answer": "No single hypothesis test. This is a foundations question about MLE for a proportion, random versus simple random sampling, and the variance of a stratified sample mean under proportional allocation.",
                "hints": ["Treat this as estimation plus sampling design.", "Look for MLE, sampling terminology, and stratified variance."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "independent_two_group_comparison",
                "tags": ["two-sample t-test", "rank-sum test", "one-sided alternative", "independent samples"],
                "answer": "Use an independent two-group comparison. The primary parametric method is a one-sided two-sample t-test, and the requested non-parametric check is a rank-sum style comparison because the two groups of mothers are independent.",
                "hints": ["Two independent groups.", "Continuous outcome: birth weight.", "Question explicitly asks for both parametric and non-parametric methods."],
                "classification_confidence": "high",
            },
            {
                "question": "3",
                "question_type": "one_sample_mean_inference",
                "tags": ["one-sample z-test", "type II error", "power", "known variance"],
                "answer": "This is a one-sample mean test with known variance, so the core method is the one-sample z-test. The task specifically asks for the type II error or power calculation when the true mean is 9.",
                "hints": ["Normal model.", "Variance is known.", "The key output is beta or power, not just a reject/do-not-reject decision."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "two_way_factorial_design",
                "tags": ["two-way ANOVA", "interaction", "factorial design"],
                "answer": "Use a two-way ANOVA with detergent and temperature as factors, including the interaction term. The question asks for the model, hypotheses, completed ANOVA table, and interpretation of main effects plus interaction.",
                "hints": ["Two factors: detergent and temperature.", "Check both main effects and interaction."],
                "classification_confidence": "high",
            },
            {
                "question": "5",
                "question_type": "bayesian_inference",
                "tags": ["Poisson-Gamma conjugacy", "Bayesian estimation", "conjugate prior"],
                "answer": "This is a Bayesian Poisson-Gamma conjugacy question. The main tasks are deriving the posterior under a Gamma prior, explaining why conjugate priors are convenient, and reflecting on what a large sample changes.",
                "hints": ["Poisson likelihood.", "Gamma prior.", "Posterior stays in the same family."],
                "classification_confidence": "high",
            },
        ],
    },
    {
        "id": "080623_aila_sarkka",
        "title": "June 2023 Exam",
        "date": "2023-06-08",
        "examiner": "Aila Sarkka",
        "source_candidates": ["080623_aila_sarkka.pdf", "ExamJune2023.pdf"],
        "notes": "The PDF header says Tuesday, June 8, 2023, even though June 8, 2023 was a Thursday. The numeric date is used for identifiers.",
        "cards": [
            {
                "question": "1",
                "question_type": "point_estimation",
                "tags": ["method of moments", "maximum likelihood", "unbiasedness", "consistency"],
                "answer": "No single test. This is a point-estimation foundations question covering the method of moments, maximum likelihood, and the definitions of unbiased and consistent estimators.",
                "hints": ["Estimator theory.", "No hypothesis test to choose here."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "categorical_table_inference",
                "tags": ["chi-squared test of independence", "contingency table"],
                "answer": "Use a chi-squared test of independence. The data come from one contingency table relating defect type to production shift, so the key question is whether those two categorical variables are associated.",
                "hints": ["One table.", "Two categorical variables: defect type and shift."],
                "classification_confidence": "high",
            },
            {
                "question": "3",
                "question_type": "paired_two_group_comparison",
                "tags": ["paired t-test", "confidence interval", "signed-rank test", "matched pairs"],
                "answer": "Treat this as a matched-pairs problem because each driver responds to both sign types. The main parametric method is a paired t-test, with a confidence interval for the mean difference and a non-parametric signed-rank alternative.",
                "hints": ["Same drivers see both conditions.", "Analyze the within-driver differences."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "one_sample_mean_inference",
                "tags": ["one-sample z-test", "sample size", "power", "known variance"],
                "answer": "This is a one-sample one-sided z-test with known variance. The exam asks for the sample size required to achieve a target power when the true mean is 1.5.",
                "hints": ["Known variance 100.", "One-sided alternative.", "This is a power/sample-size calculation."],
                "classification_confidence": "high",
            },
            {
                "question": "5",
                "question_type": "regression",
                "tags": ["multiple regression", "coefficient interpretation", "model fit"],
                "answer": "Use multiple linear regression with mpg as the response and disp, hp, and wt as predictors. The focus is model specification, coefficient interpretation, assumptions, and the meaning of R-squared style fit summaries.",
                "hints": ["Several predictors.", "Continuous response."],
                "classification_confidence": "high",
            },
        ],
    },
    {
        "id": "150823_aila_sarkka",
        "title": "August 2023 Exam",
        "date": "2023-08-15",
        "examiner": "Aila Sarkka",
        "source_candidates": ["150823_aila_sarkka.pdf", "ExamAugust2023.pdf"],
        "notes": "Draft mapping generated from the local PDF archive; review suggested methods before final release.",
        "cards": [
            {
                "question": "1",
                "question_type": "bayesian_inference",
                "tags": ["Bayesian estimation", "prior choice", "conjugate prior"],
                "answer": "No frequentist test is being selected here. This is a Bayesian foundations question about the basic idea of the Bayesian approach, how a prior is chosen, and what a conjugate prior means.",
                "hints": ["Focus on Bayesian vocabulary.", "No rejection region is requested."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "power_and_multiple_testing",
                "tags": ["multiple testing", "binomial count of false positives", "independence assumption"],
                "answer": "This is a multiple-testing question. Model the number of false significant findings among 50 independent intervals and compute the probability that at least two intervals falsely suggest an effect.",
                "hints": ["Many intervals.", "All null effects are assumed true.", "Independence is the key assumption."],
                "classification_confidence": "high",
            },
            {
                "question": "3",
                "question_type": "two_proportion_inference",
                "tags": ["confidence interval for difference in proportions", "two-sample proportion z-test", "Fisher's exact test"],
                "answer": "Use inference for two proportions. The main methods are a confidence interval for the difference in proportions and a two-sample proportion z-test, with Fisher's exact test as the small-sample exact fallback.",
                "hints": ["Two candy variants.", "Binary outcome: red or not red."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "randomized_block_design",
                "tags": ["randomized block ANOVA", "Friedman test", "blocked design"],
                "answer": "This is a randomized block design because every driver rates every mirror. The primary method is blocked ANOVA, and a Friedman-type non-parametric backup is the natural alternative if normal-model assumptions fail.",
                "hints": ["Drivers are blocks.", "Mirrors are treatments.", "Same drivers see all mirrors."],
                "classification_confidence": "high",
            },
            {
                "question": "5",
                "question_type": "regression",
                "tags": ["correlation", "confidence interval for correlation"],
                "answer": "This is a correlation and linear-association question. The task is to interpret the estimated correlation between exam and project scores and understand what a confidence interval that includes zero implies.",
                "hints": ["Linear association only.", "Interpret both point estimate and interval."],
                "classification_confidence": "high",
            },
        ],
    },
    {
        "id": "120324_tony_johansson",
        "title": "March 2024 Exam",
        "date": "2024-03-12",
        "examiner": "Tony Johansson",
        "source_candidates": ["120324_tony_johansson.pdf", "mve155_msg200_240312_sols.pdf"],
        "notes": "This PDF bundles the exam with solutions. The draft dataset uses only the exam questions.",
        "cards": [
            {
                "question": "1",
                "question_type": "sampling_design",
                "tags": ["random sampling", "simple random sampling", "unbiasedness", "consistency"],
                "answer": "No single hypothesis test. This question is about sampling design and the sample mean: random versus simple random sampling, unbiasedness, consistency, and how those choices affect standard errors and confidence interval width.",
                "hints": ["Sampling terminology.", "Compare estimator precision under different sampling schemes."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "categorical_table_inference",
                "tags": ["chi-squared test of homogeneity", "chi-squared test of independence", "design critique"],
                "answer": "The design critique comes first, but the intended inferential tool is a chi-squared test for a board-type-by-success table. If the experiment were properly designed with separate board groups, the natural method would be a chi-squared test of homogeneity.",
                "hints": ["Board type versus success/failure.", "The first part asks whether the design justifies a chi-squared analysis at all."],
                "classification_confidence": "medium",
            },
            {
                "question": "3",
                "question_type": "point_estimation",
                "tags": ["maximum likelihood", "bias", "standard error", "consistency"],
                "answer": "No single hypothesis test. This is a point-estimation question centered on maximum likelihood for a shifted exponential family, plus the bias, standard error, and consistency of the resulting estimators.",
                "hints": ["Estimator derivation, not test selection.", "Shifted exponential structure."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "goodness_of_fit",
                "tags": ["custom discrete test", "counting argument", "null versus larger-support alternative"],
                "answer": "This is not one of the standard named tests from the course list, but it is still a hypothesis-testing design problem. Build a custom test around the number of distinct messages observed under the null model m = 8 versus the larger-support alternative.",
                "hints": ["Count distinct observed categories.", "Uniform draws under the null."],
                "classification_confidence": "medium",
            },
            {
                "question": "5",
                "question_type": "independent_two_group_comparison",
                "tags": ["rank-sum test", "independent samples", "distribution comparison"],
                "answer": "Treat this as an independent two-group comparison with a heavy-skew or outlier-sensitive outcome. The safer first-choice method is a rank-sum test comparing the platform price distributions rather than a mean-based t-test.",
                "hints": ["Independent groups of artworks sold on two platforms.", "The question asks about difference in distribution, not just average price."],
                "classification_confidence": "medium",
            },
        ],
    },
    {
        "id": "270824_aila_sarkka",
        "title": "August 2024 Exam",
        "date": "2024-08-27",
        "examiner": "Aila Sarkka",
        "source_candidates": ["270824_aila_sarkka.pdf", "MVE155MSG200_August2024.pdf"],
        "notes": "Draft mapping generated from the local PDF archive; review suggested methods before final release.",
        "cards": [
            {
                "question": "1",
                "question_type": "theory_and_foundations",
                "tags": ["credibility interval", "p-value", "chi-squared homogeneity", "chi-squared independence"],
                "answer": "No single test needs to be selected. This is a theory question about what a credibility interval means, how to define a p-value, and how the chi-squared tests of homogeneity and independence differ in design and interpretation.",
                "hints": ["Definitions only.", "Distinguish study design as well as the null hypothesis."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "one_sample_mean_inference",
                "tags": ["confidence interval for mean", "sample size", "known variance"],
                "answer": "This is one-sample mean inference with known standard deviation. The core tasks are reading the confidence level implied by a given interval and solving for the sample size needed to keep the same width at 95% confidence.",
                "hints": ["Known sigma.", "Interval width drives the sample-size calculation."],
                "classification_confidence": "high",
            },
            {
                "question": "3",
                "question_type": "point_estimation",
                "tags": ["pooled variance", "two-sample t-test", "unbiasedness", "consistency"],
                "answer": "No new test is being chosen; this is about the pooled variance estimator used inside the equal-variance two-sample t-test. The question focuses on why that estimator is unbiased and consistent.",
                "hints": ["Connect the estimator to the equal-variance two-sample t-test.", "Proof question, not a reject/do-not-reject problem."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "multi_group_comparison",
                "tags": ["one-way ANOVA", "Kruskal-Wallis test"],
                "answer": "Use one-way ANOVA to compare the four pesticide groups, and use the Kruskal-Wallis test as the requested non-parametric check. The design has four independent treatment groups with one quantitative response.",
                "hints": ["Four pesticides.", "Independent land areas.", "ANOVA plus non-parametric backup."],
                "classification_confidence": "high",
            },
            {
                "question": "5",
                "question_type": "regression",
                "tags": ["simple linear regression", "quadratic regression", "t-test for slope"],
                "answer": "This is a regression-modeling question. Start with simple linear regression, interpret the slope test and fit quality, then consider a quadratic extension because the scatter plot suggests curvature.",
                "hints": ["One predictor first.", "Then assess whether curvature improves the model."],
                "classification_confidence": "high",
            },
        ],
    },
    {
        "id": "180325_aila_sarkka",
        "title": "March 2025 Exam",
        "date": "2025-03-18",
        "examiner": "Aila Sarkka",
        "source_candidates": ["180325_aila_sarkka.pdf", "ExamMarch2025.pdf"],
        "notes": "Draft mapping generated from the local PDF archive; review suggested methods before final release.",
        "cards": [
            {
                "question": "1",
                "question_type": "sampling_design",
                "tags": ["finite population correction", "optimal allocation", "blocking", "randomization"],
                "answer": "No single hypothesis test. This is a sampling-and-design question covering finite population correction, stratified allocation formulas, and when blocking plus randomization should be used in experimental design.",
                "hints": ["Sampling formulas plus experimental design concepts.", "Look for FPC and allocation rules."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "bayesian_inference",
                "tags": ["Poisson MLE", "Gamma prior", "credible interval", "confidence interval versus credible interval"],
                "answer": "This is Bayesian inference for a Poisson model. The tasks combine MLE, a Gamma prior, posterior derivation, one way to form a credible interval, and the interpretation gap between credible and confidence intervals.",
                "hints": ["Poisson likelihood.", "Gamma prior.", "Compare Bayesian and frequentist interval language."],
                "classification_confidence": "high",
            },
            {
                "question": "3",
                "question_type": "two_proportion_inference",
                "tags": ["two-sample proportion z-test", "one-sided test", "p-value threshold"],
                "answer": "Use a one-sided two-proportion comparison because the claim is that heavy-duty packaging lowers the damage rate. The question asks both for the significance test at 0.05 and for the smallest significance level that would still reject.",
                "hints": ["Two packaging types.", "Binary damage outcome.", "One-sided alternative."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "multi_group_comparison",
                "tags": ["one-way ANOVA", "Kruskal-Wallis test"],
                "answer": "This is another four-group comparison problem. Start with one-way ANOVA on the pesticide groups, then use the Kruskal-Wallis test as the non-parametric comparison and discuss the boxplot evidence.",
                "hints": ["Four independent pesticide groups.", "ANOVA plus non-parametric cross-check."],
                "classification_confidence": "high",
            },
            {
                "question": "5",
                "question_type": "one_sample_mean_inference",
                "tags": ["one-sample z-test", "sample size", "power", "known variance"],
                "answer": "This is a one-sample z-test with known variance under a one-sided alternative. The exam asks for the rejection region, the sample size that gives 90% power when the true mean is delta, and the limiting behavior as delta goes to zero.",
                "hints": ["Known variance 9.", "One-sided alternative.", "Power-based sample-size question."],
                "classification_confidence": "high",
            },
            {
                "question": "6",
                "question_type": "regression",
                "tags": ["multiple regression", "coefficient significance", "model fit"],
                "answer": "Use multiple linear regression for the Happiness response. The focus is writing the model, interpreting which covariates matter, understanding overall fit, and stating the residual assumptions needed for inference.",
                "hints": ["Several predictors.", "Check both coefficient tests and overall fit."],
                "classification_confidence": "high",
            },
        ],
    },
    {
        "id": "280825_aila_sarkka",
        "title": "August 2025 Exam",
        "date": "2025-08-28",
        "examiner": "Aila Sarkka",
        "source_candidates": ["280825_aila_sarkka.pdf", "MVE155MSG200WithSolutionsAugust2025.pdf"],
        "notes": "The PDF header says Tuesday, August 28, 2025, even though August 28, 2025 was a Thursday. The numeric date is used for identifiers.",
        "cards": [
            {
                "question": "1",
                "question_type": "point_estimation",
                "tags": ["unbiasedness", "consistency", "sample mean"],
                "answer": "No single test. This is a core estimator-properties question: identify the two important properties and show that the sample mean has them under the usual random-sample assumptions.",
                "hints": ["Unbiasedness and consistency.", "Estimator theory, not hypothesis testing."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "independent_two_group_comparison",
                "tags": ["two-sample z-test", "power", "sample size", "equal variances"],
                "answer": "This is an independent two-group mean comparison with known variance structure, framed as a sample-size and power calculation. The target procedure is the one-sided two-sample normal-theory test for the difference in means.",
                "hints": ["Two independent samples.", "Common variance known symbolically.", "Power at 80%."],
                "classification_confidence": "high",
            },
            {
                "question": "3",
                "question_type": "power_and_multiple_testing",
                "tags": ["multiple testing", "at least two false positives", "independence assumption"],
                "answer": "This is a multiple-testing problem. Count how often 95% intervals miss the normal value when all null effects are actually true, and make the independence assumptions explicit.",
                "hints": ["Many confidence intervals.", "All true nulls.", "Need an assumption about independence."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "independent_two_group_comparison",
                "tags": ["two-sample t-test", "rank-sum test", "one-sided alternative", "independent samples"],
                "answer": "Use an independent two-group comparison. The parametric method is a one-sided two-sample t-test for fertilizer versus no fertilizer, and the non-parametric companion is a rank-sum style test because the samples are independent.",
                "hints": ["Two plant groups.", "Continuous growth outcome.", "Parametric and non-parametric analyses are both requested."],
                "classification_confidence": "high",
            },
            {
                "question": "5",
                "question_type": "two_way_factorial_design",
                "tags": ["two-way ANOVA", "interaction", "factorial experiment"],
                "answer": "This is a two-way factorial experiment with three dosage levels for each active ingredient. Use two-way ANOVA with interaction to write the model, fill the table, and interpret the factor and interaction effects.",
                "hints": ["Two factors, each with three levels.", "Interaction term matters."],
                "classification_confidence": "high",
            },
            {
                "question": "6",
                "question_type": "regression",
                "tags": ["multiple regression", "coefficient t-tests", "prediction interval"],
                "answer": "Use multiple linear regression with media advertisement and point-of-sale cost as predictors. The tasks are significance testing for coefficients and a prediction-style calculation for a new supermarket.",
                "hints": ["Two predictors.", "Interpret t-statistics and produce a prediction."],
                "classification_confidence": "high",
            },
        ],
    },
    {
        "id": "200326_aila_sarkka",
        "title": "March 2026 Exam",
        "date": "2026-03-20",
        "examiner": "Aila Sarkka",
        "source_candidates": ["200326_aila_sarkka.pdf", "MVE155MSG200March2026WithSolutions.pdf"],
        "notes": "This PDF bundles the exam with solutions. The draft dataset uses only the exam questions.",
        "cards": [
            {
                "question": "1",
                "question_type": "sampling_design",
                "tags": ["stratified sampling", "proportional allocation", "confidence interval", "allocation strategy"],
                "answer": "No single hypothesis test. This is a stratified-sampling design question about proportional allocation, how to build a confidence interval for the population mean from stratified samples, and how that compares with simple random sampling.",
                "hints": ["Three strata.", "Allocation choice matters.", "Think precision, not hypothesis testing."],
                "classification_confidence": "high",
            },
            {
                "question": "2",
                "question_type": "categorical_table_inference",
                "tags": ["chi-squared test of independence", "odds ratio", "contingency table"],
                "answer": "Use a chi-squared test of independence on the education-by-number-of-children table. The follow-up asks for an odds ratio interpretation comparing college education with the chance of having more than three children.",
                "hints": ["One contingency table.", "Association between two categorical variables."],
                "classification_confidence": "high",
            },
            {
                "question": "3",
                "question_type": "independent_two_group_comparison",
                "tags": ["two-sample t-test", "rank-sum test", "independent samples"],
                "answer": "Treat this as an independent two-group comparison because different cars received radial and belted tires. The question asks you to choose between a normal-theory two-sample test and a non-parametric rank-based alternative after checking distributional assumptions.",
                "hints": ["Two separate groups of cars.", "Fuel economy is quantitative.", "Normality assessment matters."],
                "classification_confidence": "high",
            },
            {
                "question": "4",
                "question_type": "one_sample_normal_inference",
                "tags": ["normality assessment", "one-sample t-test", "chi-squared test for variance"],
                "answer": "This is a one-sample normal-theory inference problem. First assess whether a normal model is reasonable, then perform a one-sided one-sample t-test for the mean and a chi-squared test for the variance under normality.",
                "hints": ["QQ-plot plus skewness and kurtosis.", "Mean test and variance test both appear."],
                "classification_confidence": "high",
            },
            {
                "question": "5",
                "question_type": "bayesian_inference",
                "tags": ["negative binomial MLE", "Beta conjugate prior", "Bayesian estimation"],
                "answer": "This is Bayesian inference for a Negative Binomial model with known r. The main ideas are the MLE for p, Beta conjugacy for p, and the resulting posterior-based estimate or interval logic.",
                "hints": ["Negative Binomial likelihood.", "Beta prior for a probability parameter."],
                "classification_confidence": "high",
            },
            {
                "question": "6",
                "question_type": "regression",
                "tags": ["simple linear regression", "maximum likelihood", "regression line property"],
                "answer": "This is a simple linear regression derivation question. Use the likelihood or least-squares algebra to show the intercept formula and then interpret the geometric consequence for the fitted regression line.",
                "hints": ["Show that the fitted line passes through the sample means.", "Regression derivation, not model selection."],
                "classification_confidence": "high",
            },
        ],
    },
]


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"-\n\s*", "", text)
    text = re.sub(r"Problems page \d+ of \d+", " ", text)
    text = re.sub(r"Tentamentsskrivning:.*?(?=\n|$)", " ", text)
    text = re.sub(r"EXAM: Statistical inference \(MVE155/MSG200\)", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text


def collapse_spaces(text: str) -> str:
    return " ".join(text.split())


def display_question_type(question_type: str) -> str:
    return QUESTION_TYPE_LABELS.get(question_type, question_type.replace("_", " ").title())


def classify_tests(question_type: str, tags: list[str]) -> tuple[str, list[str]]:
    recognized: list[str] = []
    seen: set[str] = set()

    def add(label: str) -> None:
        if label and label not in seen:
            recognized.append(label)
            seen.add(label)

    for tag in tags:
        if tag in DIRECT_TEST_LABELS:
            add(DIRECT_TEST_LABELS[tag])

    if question_type == "one_sample_mean_inference" and not recognized and "known variance" in tags:
        add("Large-sample test for the mean (Z-test)")

    if question_type == "regression":
        has_coefficient_test = any(
            tag in {"t-test for slope", "coefficient significance", "coefficient t-tests"} for tag in tags
        )
        if has_coefficient_test:
            add("Tests for intercept and slope")
            if "model fit" in tags:
                add("Model utility test")
        elif not recognized and "model fit" in tags and "coefficient interpretation" not in tags:
            add("Model utility test")

    if question_type == "one_sample_normal_inference":
        if "one-sample t-test" in tags:
            add("One-sample t-test")
        if "chi-squared test for variance" in tags:
            add("Chi-squared test for the variance")

    primary_test = recognized[0] if recognized else ""
    alternative_tests = recognized[1:]
    return primary_test, alternative_tests


def extract_question_map(pdf_path: Path) -> dict[str, str]:
    raw_text = "\n".join((page.extract_text() or "") for page in PdfReader(str(pdf_path)).pages)
    text = clean_text(raw_text)
    matches = list(QUESTION_PATTERN.finditer(text))
    question_map: dict[str, str] = {}
    seen_numbers: set[str] = set()
    end_of_exam = len(text)

    for match in matches:
        number = match.group(1)
        if number in seen_numbers:
            end_of_exam = match.start()
            break
        seen_numbers.add(number)

    exam_text = text[:end_of_exam]
    matches = list(QUESTION_PATTERN.finditer(exam_text))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(exam_text)
        number = match.group(1)
        prompt = collapse_spaces(exam_text[start:end]).replace("Good luck!", "").strip()
        prompt = re.sub(r"\bSolutions?\b\s*$", "", prompt).strip()
        question_map[number] = prompt
    return question_map


def resolve_source_pdf(source_dir: Path, candidates: list[str]) -> Path:
    for candidate in candidates:
        path = source_dir / candidate
        if path.exists():
            return path
    raise FileNotFoundError(f"None of the source PDFs were found: {candidates}")


def build_course(source_dir: Path) -> None:
    COURSE_DIR.mkdir(parents=True, exist_ok=True)

    course_payload = {
        "id": "statistical_inference_mve155_msg200",
        "code": "MVE155/MSG200",
        "name": "Statistical Inference",
        "description": "Draft flashcards and compendium-aligned test mappings derived from the local MVE155/MSG200 archive.",
        "tags": ["statistics", "hypothesis testing", "bayesian inference", "regression", "anova"],
    }

    exams_payload = []
    cards_payload = []
    review_lines = [
        "# Statistical Inference Review Notes",
        "",
        "This draft dataset was generated from the local PDF archive only.",
        "Each card contains a broad study category plus a suggested primary test derived from the compendium and the exam wording.",
        "Questions that are mainly about estimation, design, or theory are left without a named primary test on purpose.",
        "",
    ]

    for exam in EXAMS:
        pdf_path = resolve_source_pdf(source_dir, exam["source_candidates"])
        questions = extract_question_map(pdf_path)

        exams_payload.append(
            {
                "id": exam["id"],
                "course_id": "statistical_inference_mve155_msg200",
                "title": exam["title"],
                "date": exam["date"],
                "examiner": exam["examiner"],
                "notes": exam["notes"],
                "source_pdf": exam["source_candidates"][0],
            }
        )

        review_lines.extend([f"## {exam['id']} | {exam['title']}", ""])

        for card in exam["cards"]:
            question_number = card["question"]
            prompt = questions.get(question_number)
            if not prompt:
                raise KeyError(f"Question {question_number} was not found in {pdf_path.name}")

            card_id = f"{exam['id']}_q{question_number}"
            question_type = display_question_type(card["question_type"])
            primary_test, alternative_tests = classify_tests(card["question_type"], card["tags"])
            cards_payload.append(
                {
                    "id": card_id,
                    "exam_id": exam["id"],
                    "prompt": prompt,
                    "answer": card["answer"],
                    "question_type": question_type,
                    "primary_test": primary_test,
                    "alternative_tests": alternative_tests,
                    "tags": card["tags"],
                    "hints": card["hints"],
                    "source_pdf": exam["source_candidates"][0],
                    "source_question": question_number,
                    "classification_confidence": card["classification_confidence"],
                }
            )

            review_lines.extend(
                [
                    f"### Q{question_number}",
                    f"- `question_type`: `{question_type}`",
                    f"- `primary_test`: `{primary_test or 'No single named test'}`",
                    (
                        f"- `alternative_tests`: {', '.join(alternative_tests)}"
                        if alternative_tests
                        else "- `alternative_tests`: none"
                    ),
                    f"- `tags`: {', '.join(card['tags'])}",
                    f"- `confidence`: `{card['classification_confidence']}`",
                    f"- `suggested answer`: {card['answer']}",
                    f"- `prompt excerpt`: {prompt[:240]}{'...' if len(prompt) > 240 else ''}",
                    "",
                ]
            )

    (COURSE_DIR / "course.json").write_text(json.dumps(course_payload, indent=2) + "\n", encoding="utf-8")
    (COURSE_DIR / "exams.json").write_text(json.dumps(exams_payload, indent=2) + "\n", encoding="utf-8")
    (COURSE_DIR / "cards.json").write_text(json.dumps(cards_payload, indent=2) + "\n", encoding="utf-8")
    (COURSE_DIR / "review_notes.md").write_text("\n".join(review_lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build the draft statistical inference course dataset.")
    parser.add_argument("--source-dir", type=Path, required=True, help="Directory containing the source PDFs")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    build_course(args.source_dir.expanduser().resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
