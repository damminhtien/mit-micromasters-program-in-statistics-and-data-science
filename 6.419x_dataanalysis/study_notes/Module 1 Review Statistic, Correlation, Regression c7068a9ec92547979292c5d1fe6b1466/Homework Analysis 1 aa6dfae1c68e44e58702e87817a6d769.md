# Homework/Analysis 1

**Data Download:** Download [statsreview_release.zip](https://courses.edx.org/assets/courseware/v1/89585644fe14105840b6e9b99fb1a2b0/asset-v1:MITx+6.419x+2T2024+type@asset+block/release_statsreview_release1.zip). The `data_and_materials` folder contains all the data files and the two papers needed for this homework.

This homework is divided into multiple problems, each of which may have automatically graded questions or a report writing component. They are:

- Problem 1.1: Requires a written report (16 points).
- Problem 1.2: Automatically graded (15 points).
- Problem 1.3: 1 Automatically graded problem (2 points), requires a written report (23 points).
- Problem 1.4: Automatically graded (10 points).
- Problem 1.5: Some parts automatically graded (5 points), other parts require a written report (15 points).
- Problem 1.6: Automatically graded (14 points).
- Problem 1.7 (Optional): Automatically graded (0 points).

You will be expected to write a small report for each question that requires it, and assemble them into one document that will be submitted through the peer grading interface. You will then be expected to grade 3 of your peer's reports, according to a rubric that will be provided after the due date. Peer review is an important part of scientific research, and so you will be expected to develop this skill as part of this and future homeworks and analyses.

During peer grading, you will assign points based on the supplied rubric. The rubric will serve as a detailed guide; however, some of the reports that you read may not follow the structure in the rubric exactly. In these cases, you should examine the rubric to find the important concepts that are being graded, and then assess for yourself if the report demonstrates understanding of those concepts. If you are unsure on whether to assign a point or not, we ask that you err on the side of leniency and give the report the point in question.

# **Objectives and Prerequisites**

At the end of this homework, you should be able to

1. Discuss the effectiveness of an experimental design. Understand the elements of experimental design including placebo effect, double-blindness. Discuss which test statistic measures the treatment effect, identify the potential biases in this test statistic, and find support in other parts of the data to validate.
2. Conduct hypothesis testing in complicated problems. Conduct multiple hypotheses testing. Hypotheses testing includes coming up with a statistical model for the data along with the hypothesis to be tested based on the research question asked, defining suitable test statistic flexibly, characterizing the asymptotic distribution of the test statistic, running the test and identifying statistical significance (commonly used examples include t-test, fisher exact test, z-test, and likelihood-ratio test). Multiple hypotheses testing includes conducting various forms of correction (Holm-Bonferroni correction, Benjamini-Hochberg correction). Carry out all these in code given a data set.
3. Understand the mathematics and statistics of p-value and the consequence of these in real applications.
4. Understand the computational and algorithmic (numerical) aspect of fitting a parametric statistical model to data. In this module in particular, this parametric statistical model is ordinary least sqaures (OLS). This entails understanding OLS as an optimization problem, and being able to write down the closed-form solution. Understand that a general method for solving such convex optimization problem is gradient descent. Be able to derive gradient of a general loss function and be able to implement gradient descent.
5. Understand the complexity of algorithms, the memory needed, and reason about the computational demand of algorithms. In this module in particular, this algorithm is gradient descent. Be able to count how much computation is needed for an algorithm, and how much memory is needed. Understand linear algebra operations on computer. Be able to reason about an algorithm's performance given the specific structure of the data matrix (underdetermined and overdetermined). For gradient descent in particular, understand the parameters' effect on gradient descent, and be able to transform, normalize, or adjust data for better and faster convergence of gradient descent.

**Prerequisites:**

1. Understand basics of experimental design, understand why randomized controlled experiment leads to causal claim.
2. Be able to use regression (linear, logistic), plot, implement basic algorithm (write function, write for-loop) in R studio or Python.
3. Practical knowledge of linear algebra.
4. Understand basic probability distributions, especially the definition and basic properties of Gaussian, Poisson, Bernoulli, Binomial.
5. Basic calculus, able to compute derivatives.

# **Problem 1.1 The Salk Vaccine Field Trial**

**Include your answers to all parts of this problem in your written report.**

**The written report usually comes from open-ended questions. There might not be single standard answer. If you hold some opinion and then you justify it with reasonable explanations, you will get the grades.**

**Introduction**

*Hint: This problem is rather qualitative. Quantitative statistic skills like forming hypothesis testing or finding test statistics are not necessary.*

The first polio epidemic hit the United States in 1916. By the 1950s several vaccines against the disease had been discovered. The one developed by Jonas Salk seemed the most promising in laboratory trials. By 1954, the National Foundation for Infantile Paralysis (NFIP) was ready to try the vaccine in the real world.

They ran a controlled experiment to analyze the effectiveness of the vaccine. The data is shown in the first table below (grade refers to educational stage).

| **NFIP Study** |  |  |
| --- | --- | --- |
|  | **Size** | **Polio rate per 100,000** |
| Grade 2 (vaccine) | 225000 | \qquad 25\qquad |
| Grade 1 and 3 (no vaccine) | 725000 | \qquad 54\qquad |
| Grade 2 (no consent) | 125000 | \qquad 44\qquad |

From this table, you interpret that the experiment was run the following way:

- Vaccines were offered to Grade 2 students, but some Grade 2 students did not consent and opted out of the offered vaccine.
- Vaccines were not offered to Grade 1 and Grade 3 students.

The experiment was later repeated as a randomized controlled double-blind experiment. The data is shown in the second table below.

| **Randomized Controlled Double-Blind Experiment** |  |  |
| --- | --- | --- |
|  | **Size** | **Polio rate per 100,000** |
| Treatment (vaccine) | 200000 | \qquad 28\qquad |
| Control (Salt Injection) | 200000 | \qquad 71\qquad |
| No consent | 350000 | \qquad 46\qquad |

The "No consent" group here means they are people who refused to participate in the whole experiment.

In this problem, you will compare these two studies.

1. (**2 points**) How would you run a randomized controlled double-blind experiment to determine the effectiveness of the vaccine? Write down procedures for the experimenter to follow. (*We recommend \sim 100 words. Maximum 200 words*)
To run a randomized controlled double-blind experiment to determine the effectiveness of the vaccine, follow these procedures:
    1. **Recruit Participants**: Gather a large, diverse sample of individuals eligible for the vaccine. Ensure the sample size is sufficient to detect a statistically significant difference in outcomes.
    2. **Random Assignment**: Randomly assign participants to two groups: the treatment group (receiving the vaccine) and the control group (receiving a placebo, such as a salt injection). Ensure the groups are of equal size to maintain balance.
    3. **Double-Blind Design**: Ensure neither the participants nor the experimenters administering the injections know who receives the vaccine and who receives the placebo. This prevents bias in administering or reporting outcomes.
    4. **Informed Consent**: Obtain informed consent from all participants, explaining the study's purpose, procedures, potential risks, and benefits.
    5. **Data Collection**: Monitor and record the incidence of polio in both groups over a specified period. Use consistent methods to diagnose and document cases.
    6. **Analysis**: Compare the polio rates between the treatment and control groups using appropriate statistical tests (e.g., t-test or z-test) to determine if there is a significant difference in incidence rates.
    7. **Reporting**: Ensure transparency by reporting the methodology, statistical analysis, and results in detail, highlighting any limitations or potential biases.
    
    This design ensures that the observed effects can be attributed to the vaccine while minimizing biases and confounding factors.
    
2. (**3 points**) For each of the NFIP study, and the Randomized controlled double blind experiment above, which numbers (or estimates) show the effectiveness of the vaccine? Describe whether the estimates suggest the vaccine is effective.(*We recommend \sim 100 words. Maximum 200 words*)
**NFIP Study:**
    - **Grade 2 (vaccine)**: Polio rate = 25 per 100,000
    - **Grade 1 and 3 (no vaccine)**: Polio rate = 54 per 100,000
    - **Grade 2 (no consent)**: Polio rate = 44 per 100,000
    
    The lower polio rate in the vaccinated Grade 2 group (25 per 100,000) compared to the unvaccinated groups (54 and 44 per 100,000) suggests that the vaccine is effective in reducing the incidence of polio.
    
    **Randomized Controlled Double-Blind Experiment:**
    
    - **Treatment (vaccine)**: Polio rate = 28 per 100,000
    - **Control (salt injection)**: Polio rate = 71 per 100,000
    - **No consent**: Polio rate = 46 per 100,000
    
    The treatment group with the vaccine had a significantly lower polio rate (28 per 100,000) compared to the control group receiving the placebo (71 per 100,000). This substantial difference indicates that the vaccine is effective in preventing polio.
    
    Both studies suggest that the vaccine is effective, with the randomized controlled double-blind experiment providing stronger evidence due to its rigorous design.
    
3. Let us examine how reliable the estimates are for the NFIP study. A train of potentially problematic but quite possible scenarios cross your mind:
    - (**a**) (**2 points**) *Scenario:* What if Grade 1 and Grade 3 students are different from Grade 2 students in some ways? For example, what if children of different ages are susceptible to polio in different degrees?
        
        Can such a difference influence the result from the NFIP experiment? If so, give an example of how a difference between the groups can influence the result. Describe an experimental design that will prevent this difference between groups from making the estimate not reliable.
        
        (*We recommend \sim 100 words. Maximum 200 words*)
        
        Yes, differences between Grade 1, Grade 2, and Grade 3 students can influence the results of the NFIP experiment. For example, if younger children (Grade 1) are more susceptible to polio due to a weaker immune system compared to older children (Grade 2 and 3), the higher polio rates observed in Grades 1 and 3 could be due to age differences rather than the lack of vaccination. This confounding variable would make it appear that the vaccine is more effective than it actually is.
        
        To prevent this, a randomized controlled trial (RCT) should be used where students are randomly assigned to either the vaccine group or a placebo group within the same grade. This design ensures that any age-related susceptibility to polio is evenly distributed across both groups. Additionally, ensuring double-blind procedures, where neither the participants nor the administrators know who receives the vaccine or placebo, would further eliminate bias. This way, the observed differences in polio rates can be more reliably attributed to the vaccine's effectiveness rather than to age-related differences.
        
    - (**b**) (**2 points**) Polio is an infectious disease. The NFIP study was not done blind; that is, the children know whether they get the vaccine or not. Could this bias the results? If so, Give an example of how it could bias the results. Describe an aspect of an experimental design that prevent this kind of bias.
        
        (*We recommend \sim 100 words. Maximum 200 words*)
        
        Yes, knowing whether they received the vaccine could bias the results in the NFIP study. For example, vaccinated children might engage in riskier behavior because they believe they are protected, potentially increasing their exposure to polio. Conversely, unvaccinated children might be more cautious to avoid infection, thereby reducing their exposure risk. This behavior could skew the polio rates independently of the vaccine's effectiveness.
        
        To prevent this bias, the experiment should be conducted as a double-blind study. In this design, neither the participants nor the administrators know who receives the vaccine and who receives a placebo. This approach ensures that the behavior of the participants does not influence the outcome, and the observed differences in polio rates can be more accurately attributed to the vaccine's effectiveness.
        
    - (**c**) (**2 points**) Even if the act of “getting vaccine" does lead to reduced infection, it does not necessarily mean that it is the vaccine itself that leads to this result. Give an example of how this could be the case. Describe an aspect of experimental design that would eliminate biases not due to the vaccine itself.
        
        (*We recommend \sim 50 words. Maximum 200 words*)
        
        If the act of "getting the vaccine" leads to reduced infection, it might be due to psychological effects or behavioral changes rather than the vaccine itself. For example, vaccinated children might adopt healthier habits, such as better hygiene, because they feel more protected.
        
        To eliminate such biases, the study should include a placebo group in a double-blind randomized controlled trial. In this design, one group receives the actual vaccine, while the control group receives a placebo (e.g., a salt injection). Neither the participants nor the administrators know who receives the vaccine or placebo. This design ensures that any observed reduction in infection rates can be attributed to the vaccine's efficacy rather than to behavioral changes or psychological effects related to the act of vaccination.
        
4. (**2 points**) In both experiments, neither control groups nor the no-consent groups got the vaccine. Yet the no-consent groups had a lower rate of polio compared to the control group. Why could that be?
    
    (*We recommend \sim 50 words. Maximum 200 words*)
    
    The no-consent groups had a lower rate of polio compared to the control groups in both experiments, which could be due to several factors:
    
    1. **Self-Selection Bias**: The no-consent group consists of individuals who opted out of the experiment. These individuals might differ systematically from those who participated, possibly being more health-conscious or having better overall health practices. Such differences can lead to lower polio rates independently of the vaccine.
    2. **Socioeconomic Factors**: Those who did not consent might come from different socioeconomic backgrounds compared to those who participated. Higher socioeconomic status often correlates with better access to healthcare, nutrition, and hygiene, which can reduce the incidence of infectious diseases like polio.
    3. **Avoidance Behavior**: Individuals in the no-consent group might have been more cautious about their health and exposure to diseases, knowing they did not receive the vaccine. This heightened awareness and avoidance behavior could result in lower infection rates.
    
    To control for such biases, it's essential to ensure that participants are randomly assigned to treatment and control groups, and that these groups are as similar as possible in all relevant characteristics except for the intervention being tested. This minimizes the influence of confounding factors and provides a clearer assessment of the vaccine's effectiveness.
    
5. (**3 points**) In the randomized controlled trial, the children whose parents refused to participate in the trial got polio at the rate of 46 per 100000, while the children whose parents consented to participate got polio at a slighter higher rate of 49 per 100000 (treatment and control groups taken together). On the basis of these numbers, in the following year, some parents refused to allow their children to participate in the experiment and be exposed to this higher risk of polio. Were their conclusion correct? What would be the consequence if a large group of parents act this way in the next year's trial?
    
    (*We recommend \sim 100 words. Maximum 200 words*)
    
    The conclusion drawn by the parents is not necessarily correct. The slightly higher polio rate among children whose parents consented (49 per 100,000) compared to those who did not (46 per 100,000) may not be due to the participation in the trial itself. Instead, it could be due to random variation or other confounding factors such as differences in behavior, health practices, or socioeconomic status between the groups.
    
    If a large group of parents refuse to allow their children to participate in the next year's trial, it could lead to a biased sample that is not representative of the overall population. This self-selection bias could result in unreliable data, making it difficult to accurately assess the vaccine's effectiveness. Additionally, with fewer participants, the statistical power of the study decreases, making it harder to detect significant differences between the treatment and control groups. This could delay the determination of the vaccine's true efficacy and potentially prolong the period before a safe and effective vaccine can be widely administered.
    

# **Problem 1.2 Gamma-ray**

The file `gamma-ray.csv` contains a small quantity of data collected from the Compton Gamma Ray Observatory, a satellite launched by NASA in 1991 (http://cossc.gsfc.nasa.gov/). For each of 100 sequential time intervals of variable lengths (given in seconds), the number of gamma rays originating in a particular area of the sky was recorded. You would like to check the assumption that the emission rate is constant.

## Part (a,b)

The model for the data can be completed as follows:

\[ G_i \sim \text{Poisson}(\lambda_i \cdot t_i) \]

Here, \(G_i\) denotes the number of gamma rays in time interval \(i\), \(\lambda_i\) denotes the average rate of gamma rays per second in time interval \(i\), and \(t_i\) denotes the length in seconds of this time interval. This model assumes that the number of gamma rays in each interval follows a Poisson distribution with mean \(\lambda_i \cdot t_i\).

## Part (c)

**Null Hypothesis \( H_0 \):**

\[ \lambda_0 = \lambda_1 = \cdots = \lambda_{99} \]

This null hypothesis states that the emission rate \(\lambda\) is constant across all time intervals.

**Alternative Hypothesis \( H_A \):**

\[ \lambda_i \neq \lambda_j \text{ for some } i \text{ and } j \]

This alternative hypothesis states that the emission rate \(\lambda\) is not constant and varies across different time intervals.

## Part (d)

What is(are) the most plausible parameter value(s) for the null model given the observations? Derive the MLE(s), i.e., maximum likelihood estimators. Calculate the value of the estimator(s) from the data.

(Please enter the value with a precision of **three** significant figures, your answer will be graded with a **2%** tolerance. *Hint: Please pay attention to the definition of significant figures. You can find more details from this [Web link.](https://en.wikipedia.org/wiki/Significant_figures)*)

```python
# Calculate the MLE for lambda
lambda_mle = total_events / total_time
```

## Part (e)

What is(are) the most plausible parameter value(s) for the alternative model given the observations? Derive the MLE(s) formula(ae). (You do not need to calculate the value(s).)

For the alternative model, where \(\lambda_i\) can vary for different intervals, we need to find the MLE for each \(\lambda_i\) separately.

Given that each \(G_i \sim \text{Poisson}(\lambda_i \cdot t_i)\), the likelihood function for \(\lambda_i\) is:
\[ L(\lambda_i) = \frac{(\lambda_i t_i)^{G_i} e^{-\lambda_i t_i}}{G_i!} \]

The log-likelihood function for all intervals is:
\[ \ln L(\lambda_1, \lambda_2, \ldots, \lambda_n) = \sum_{i=1}^{n} \left[ G_i \ln (\lambda_i t_i) - \lambda_i t_i - \ln(G_i!) \right] \]

Simplifying the log-likelihood for each \(\lambda_i\):
\[ \ln L(\lambda_i) = G_i \ln (\lambda_i t_i) - \lambda_i t_i - \ln(G_i!) \]

Taking the derivative of the log-likelihood function with respect to \(\lambda_i\) and setting it to zero to find the MLE:
\[ \frac{d}{d\lambda_i} \ln L(\lambda_i) = \frac{G_i}{\lambda_i} - t_i = 0 \]

Solving for \(\lambda_i\):
\[ \frac{G_i}{\lambda_i} = t_i \]
\[ \lambda_i = \frac{G_i}{t_i} \]

Thus, the MLE for \(\lambda_i\) is:
\[ \lambda_i = \frac{G_i}{t_i} \]

These are the most plausible parameter values for the alternative model given the observations. Each \(\lambda_i\) is estimated independently based on the number of gamma rays \(G_i\) and the length of the time interval \(t_i\).

## Part (f)

### f_1

Which one of the following is a good test statistic for the data:

"Sanity check": test statistics should be a quantity that helps you measure how likely the observed data is given your null hypothesis.

$$
\Lambda (x)= -2 \ln (\frac{\max f(G_0,G_1,\cdots ,G_{99}|\lambda )}{\max f(G_0,G_1,\cdots ,G_{99}|\lambda _0,\cdots , \lambda _{99})})
$$

### f_2

The asymptotic distribution for \Lambda (x) is:

The likelihood ratio test statistic \(\Lambda(x)\) asymptotically follows a chi-squared distribution with degrees of freedom equal to the difference in the number of parameters estimated under the alternative and null hypotheses.

In this case:

- Under the null hypothesis, there is one parameter \(\lambda\).
- Under the alternative hypothesis, there are 100 parameters \(\lambda_0, \lambda_1, \ldots, \lambda_{99}\).

Therefore, the degrees of freedom for the chi-squared distribution is \(100 - 1 = 99\).

Thus, the asymptotic distribution for \(\Lambda(x)\) is:

\[ \chi^2_{99} \]

### f_3

Determine the rejection region at a significance level of 0.05. (Please enter the value with a precision of **three**significant figures, your answer will be graded with a **2%** tolerance.) The rejection region is

To determine the rejection region at a significance level of 0.05 for a chi-squared distribution with 99 degrees of freedom, we need to find the critical value corresponding to the 95th percentile of the \(\chi^2_{99}\) distribution. This critical value marks the boundary of the rejection region for the null hypothesis.

Using a chi-squared distribution table or a statistical software, we find the critical value for \(\chi^2_{99}\) at the 95th percentile.

Let's calculate this value using Python.

```python
from scipy.stats import chi2

# Determine the critical value for the chi-squared distribution with 99 degrees of freedom at the 95th percentile
critical_value = chi2.ppf(0.95, df=99)

critical_value
```

Let me calculate this for you.

The critical value for the chi-squared distribution with 99 degrees of freedom at the 95th percentile is approximately \(123.225\).

Therefore, the rejection region at a significance level of 0.05 is:

\[ \Lambda(x) > 123.225 \]

This means we would reject the null hypothesis if the calculated test statistic \(\Lambda(x)\) exceeds this critical value.

### f_4

Given the observed data, the value of the test statistic is: (Please enter the value with a precision of **three**significant figures, your answer will be graded with a **2%** tolerance.)

Its p-value is: (Please enter the value with a precision of **three** significant figures, your answer will be graded with a **2%** tolerance.)

```python
import numpy as np
from scipy.special import gammaln

# Define log-likelihood calculation functions
def log_likelihood_null(data, lambda_mle):
    return np.sum(data['count'] * np.log(lambda_mle * data['seconds'] + 1e-10) - 
                  lambda_mle * data['seconds'] - 
                  gammaln(data['count'] + 1))

def log_likelihood_alternative(data):
    return np.sum(data.apply(lambda row: row['count'] * np.log(row['count'] + 1e-10) - 
                                        row['count'] - 
                                        gammaln(row['count'] + 1), axis=1))

# Compute log-likelihoods
log_likelihood_null_value = log_likelihood_null(gamma_ray_data, lambda_mle)
log_likelihood_alternative_value = log_likelihood_alternative(gamma_ray_data)

# Compute test statistic
test_statistic_final = -2 * (log_likelihood_null_value - log_likelihood_alternative_value)

# Compute p-value
p_value_final = chi2.sf(test_statistic_final, df=99)

test_statistic_final, p_value_final
```

### f_5

Given the p-value of \(0.336\), which is greater than the significance level of \(0.05\), we do not have sufficient evidence to reject the null hypothesis.

Therefore, we shall:

**Cannot reject our null hypothesis, emission rate appears to be constant.**

# **Problem 1.3**

Read the statement by the American Statistical Association about p-values (Wasserstein and Lazar: The ASA's statement on p-values: context, process, and purpose)

[Web link.](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)

[PDF link.](https://www.tandfonline.com/doi/pdf/10.1080/00031305.2016.1154108)

(Note that the statement itself appears after the editorial.)

### **Key Points from ASA's Statement on p-values:**

1. **P-values can indicate incompatibility with a model**: They show how incompatible the data are with a specified statistical model but do not measure the probability that the hypothesis is true or that the data were produced by random chance alone.
2. **Avoiding bright-line thresholds**: Decisions should not be based solely on whether a p-value passes a specific threshold (e.g., p < 0.05). This can lead to erroneous beliefs and poor decision making.
3. **Full reporting and transparency**: Proper inference requires full reporting and transparency. Selective reporting of results based on p-values can lead to false conclusions.
4. **Effect size and importance**: P-values do not measure the size of an effect or its importance. Smaller p-values do not necessarily imply larger or more important effects.
5. **Context and evidence**: A p-value without context or additional evidence provides limited information.

## Part (a)

### a_1

Your colleague on education studies really cares about what can improve the education outcome in early childhood. He thinks the ideal planning should be to include as much variables as possible and regress children's educational outcome on the set. Then we select the variables that are shown to be statistically significant and inform the policy makers. Is this approach likely to produce the intended good policies? (*We recommend \sim 50 words. Maximum 200 words*)

Your colleague's approach of including as many variables as possible and selecting those that are statistically significant to inform policy makers is unlikely to produce good policies. This method, known as data dredging or p-hacking, can lead to several issues:

1. **Multiple Testing Problem**: Including many variables increases the likelihood of false positives due to multiple comparisons. This means some variables might appear significant purely by chance.
2. **Overfitting**: Including too many variables can lead to overfitting, where the model describes random noise rather than the underlying relationship. This reduces the model's generalizability to new data.
3. **Misinterpretation of P-values**: P-values do not measure the size or importance of an effect. Statistically significant variables may not be practically significant.
4. **Transparency and Reproducibility**: Selective reporting of statistically significant results without full transparency can lead to misleading conclusions and hinder reproducibility.

### Recommendations:

- **Pre-specify Variables**: Choose variables based on theoretical considerations and prior research.
- **Correction for Multiple Comparisons**: Use techniques like Bonferroni correction or false discovery rate control to account for multiple testing.
- **Report Effect Sizes and Confidence Intervals**: These provide a better understanding of the practical significance of the results.
- **Validation**: Use cross-validation or external validation datasets to ensure the model's robustness.
- **Full Reporting**: Transparently report all analyses and decisions to ensure validity and reproducibility.

### a_2

Your friend hears your point, and think it makes sense. He also hears about that with more data, relations are less likely to be observed just by chance, and inference becomes more accurate. He asks, if he gets more and more data, will the procedure he proposes find the true effects? *Hint: You might need to design some experiment.* (*We recommend \sim250 words. Maximum 350 words*)

Your friend's belief that more data can lead to more accurate inferences is generally correct, but it does not guarantee that the procedure he proposes will find the true effects. Here are some key points to consider:

### Key Considerations:

1. **Large Sample Size**: With more data, the statistical power increases, making it easier to detect true effects. However, it also means that even very small, possibly trivial effects, can become statistically significant.
2. **Multiple Testing Problem**: Increasing the number of variables increases the risk of false positives, regardless of sample size. This can be managed with corrections for multiple comparisons, but it complicates the analysis.
3. **Model Complexity**: Including too many variables without theoretical justification can lead to overfitting. Overfitting happens when the model captures noise rather than the underlying relationships, reducing its generalizability.

### Experimental Design:

To demonstrate the impact of your friend's approach with increasing data, consider designing a simulation experiment:

1. **Simulation Setup**:
    - Generate a synthetic dataset with a known true model. For instance, assume children's educational outcomes are influenced by a few key variables (e.g., parental education, income, and early childhood interventions).
    - Add a large number of irrelevant variables (noise) to the dataset.
2. **Procedure**:
    - Start with a small sample size and fit a regression model including all variables.
    - Gradually increase the sample size and refit the model each time.
    - Track which variables are identified as statistically significant at each step.
3. **Analysis**:
    - Assess how often the true key variables are identified as significant versus how often noise variables are incorrectly identified as significant.
    - Apply corrections for multiple comparisons to see how the results change.

### Expected Outcome:

With increasing data, the key variables should more consistently be identified as significant, demonstrating the benefits of larger sample sizes. However, without proper handling of multiple comparisons and overfitting, noise variables may also frequently be identified as significant, illustrating the pitfalls of the proposed procedure.

### Conclusion:

While more data can improve the accuracy of inferences, the procedure of including as many variables as possible and selecting those that are statistically significant is still flawed. Proper experimental design, theoretical grounding, and statistical corrections are essential to ensure that true effects are identified without being overwhelmed by false positives.

By carefully designing an experiment, your friend can see firsthand that more data helps but does not solve the fundamental issues associated with data dredging and overfitting. Robust statistical practices are essential to finding true effects.

## Part (b)

### b_1

An economist collects data on many nation-wise variables and surprisingly find that if they run a regression between chocolate consumption and number of Nobel prize laureates, the coefficient to be statistically significant. Should he conclude that there exists a relationship between Nobel prize and chocolate consumption?

No, the economist should not conclude that there exists a relationship between Nobel prize and chocolate consumption based solely on the statistically significant coefficient from the regression analysis. Further analysis considering potential confounding factors, multiple comparisons, and validation is necessary before making such a conclusion.

### b_2

A neuroscience lab is interested in how consumption of sugar and coco may effect development of intelligence and brain growth. They collect data on chocolate consumption and number of Nobel prize laureates in each nation, and finds the correlation to be statistically significant. Should they conclude that there exists a relationship between chocolate consumption and intelligence? (*We recommend \sim 100 words. Maximum 200 words*)

No, the neuroscience lab should not conclude that there exists a relationship between chocolate consumption and intelligence based solely on the statistically significant correlation between chocolate consumption and the number of Nobel prize laureates. Correlation does not imply causation, and this observed relationship may be influenced by confounding variables such as economic factors, education systems, and overall health and nutrition in different nations. Additionally, the significance could be due to chance given multiple comparisons. To establish a causal relationship, more rigorous studies, such as controlled experiments or longitudinal studies, are needed to account for these potential confounders and validate the findings in different contexts.

### b_3

In order to study the relation between chocolate consumption and intelligence, what can they do? (*We recommend \sim100 words. Maximum 200 words*)

To study the relationship between chocolate consumption and intelligence, the neuroscience lab should conduct more rigorous and controlled studies. Here are some steps they can take:

1. **Experimental Studies**: Design randomized controlled trials (RCTs) where participants are randomly assigned to consume different amounts of chocolate. Measure changes in intelligence and brain growth over time using standardized tests and neuroimaging techniques.
2. **Longitudinal Studies**: Follow a cohort of individuals over an extended period, tracking their chocolate consumption and changes in cognitive abilities and brain development. This helps to establish temporal relationships.
3. **Control Confounding Variables**: Include variables such as socioeconomic status, education, overall diet, and health factors in the analysis to control for potential confounders.
4. **Mechanistic Studies**: Conduct laboratory experiments to investigate the biological mechanisms through which chocolate components (e.g., flavonoids) might influence brain function and development in animal models or cell cultures.
5. **Replication**: Replicate the findings in different populations and settings to ensure the robustness and generalizability of the results.

By combining these approaches, the lab can gather more comprehensive and reliable evidence on whether and how chocolate consumption may influence intelligence and brain growth.

### b_4

The lab runs a randomized experiment on 100 mice, add chocolate in half of the mice's diet and add in another food of the equivalent calories in another half's diet. They find that the difference between the two groups time in solving a maze puzzle has p-value lower than 0.05. Should they conclude that chocolate consumption leads to improved cognitive power in mice? (*We recommend \sim 100 words. Maximum 200 words*)

The lab's finding that the difference in maze-solving times between the two groups of mice has a p-value lower than 0.05 suggests a statistically significant effect of chocolate consumption on cognitive performance. However, several factors should be considered before concluding that chocolate consumption leads to improved cognitive power in mice:

1. **Replication**: The experiment should be replicated to ensure the results are consistent and not due to chance.
2. **Effect Size**: The magnitude of the difference should be assessed to determine if it is practically significant, not just statistically significant.
3. **Control for Confounders**: Ensure that other factors (e.g., stress levels, health status) are controlled for and did not influence the results.
4. **Mechanistic Insight**: Investigate the biological mechanisms through which chocolate might affect cognition to support the observed effect.
5. **Long-Term Effects**: Assess if the cognitive improvements are sustained over time and not just a short-term effect.

If these considerations are met, the lab can be more confident in concluding that chocolate consumption may lead to improved cognitive power in mice. However, further research would be needed to generalize these findings to other contexts, including humans.

### b_5

The lab collects individual level data on 50000 humans on about 100 features including IQ and chocolate consumption. They find that the relation between chocolate consumption and IQ has a p-value higher than 0.05. However, they find that there are some other variables in the data set that has p-value lower than 0.05, namely, their father's income and number of siblings. So they decide to not write about chocolate consumption, but rather, report these statistically significant results in their paper, and provide possible explanations.

Is this approach correct? (*We recommend \sim 50 words. Maximum 150 words*)

## Part (c)

A lab just finishes a randomized controlled trial on 10000 participants for a new drug, and find a treatment effect with p-value smaller than 0.05. After a journalist interviewed the lab, he wrote a news article titled "New trial shows strong effect of drug X on curing disease Y." Is this title appropriate? What about "New drug proves over 95% success rate of drug X on curing disease Y"? (*We recommend \sim 50 words. Maximum 150 words*)

## Part (d)

Your boss wants to decide on company's spending next year. He thinks letting each committee debates and propose the budget is too subjective a process and the company should learn from its past and let the fact talk. He gives you the data on expenditure in different sectors and the company's revenue for the past 25 years. You run a regression of the revenue on the spending on HR sector, and find a large effect, but the effect is not statistically significant. Your boss saw the result and says “Oh, then we shouldn't increase our spending on HR then".

Is his reasoning right? (*We recommend \sim 50 words. Maximum 150 words*)

This approach is problematic and may lead to misleading conclusions. Selectively reporting only statistically significant results, known as "p-hacking" or "cherry-picking," can inflate the likelihood of false positives and distort the scientific record. Instead, the lab should report all findings, including the non-significant relationship between chocolate consumption and IQ, to provide a complete and transparent analysis. This ensures that the reported results are reliable and not the product of selective reporting. Additionally, discussing potential confounding variables and the context of the findings will lead to more robust and credible scientific conclusions.

## Part (e)

Even if a test is shown as significant by replication of the same experiment, we still cannot make a scientific claim.

True or False? (*We recommend \sim 50 words. Maximum 150 words*)

False. Replication is a critical component of scientific research. If a test shows significant results and these findings are replicated through independent studies, it strengthens the evidence for a scientific claim. However, scientific claims should also be supported by robust study design, thorough analysis, and consideration of potential confounders and biases. Replication adds credibility, but comprehensive scientific evaluation is necessary to make well-supported claims.

## Part (f)

Your lab mate is writing up his paper. He says if he reports all the tests and hypothesis he has done, the results will be too long, so he wants to report only the statistical significant ones.

Is this OK? If not, why? (*We recommend \sim 100 words. Maximum 200 words*)

No, it is not okay for your lab mate to report only the statistically significant results. This practice, known as selective reporting or "p-hacking," can lead to biased conclusions and inflate the likelihood of false positives. It distorts the scientific record and misleads readers by presenting an incomplete picture of the research findings.

Full transparency in reporting all tests and hypotheses is essential to provide a complete and accurate representation of the research. This includes non-significant results, which are important for understanding the context and robustness of the findings. Comprehensive reporting allows other researchers to fully evaluate the evidence, replicate studies, and build a reliable body of scientific knowledge.

## Part(g)

If I see a significant p-values, it could be the case that the null hypothesis is consistent with truth, but my statistical model does not match reality.

True or False? (*We recommend \sim 100 words. Maximum 200 words*)

True. A significant p-value indicates that the observed data are unlikely under the null hypothesis, assuming the statistical model is correct. However, it is possible that the null hypothesis is consistent with the truth, but the statistical model used does not accurately represent reality. Model misspecification, such as incorrect assumptions about the distribution of the data or omitted variables, can lead to misleading p-values. Therefore, a significant p-value does not guarantee that the null hypothesis is false; it may instead reflect flaws in the statistical model. It is crucial to ensure that the model assumptions are valid and the model appropriately fits the data.