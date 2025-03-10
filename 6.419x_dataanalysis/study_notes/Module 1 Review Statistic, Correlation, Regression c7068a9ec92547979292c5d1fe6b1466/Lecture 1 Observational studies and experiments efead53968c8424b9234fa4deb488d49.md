# Lecture 1: Observational studies and experiments

# **1. Lecture introduction**

This lecture sets up the basics of randomized experiments, hypothesis testing, and data modeling. The next two lectures will then cover further methods for hypothesis testing and approaches to multiple hypothesis testing. They will build on the basic methods in this lecture to achieve better methodological accuracy and more generalizable models.

The discussion will be guided by a study conducted by the Health Insurance Program that offered mammographies for early detection of breast cancer, where the objective is to determine whether offering mammographies will lead to fewer deaths due to breast cancer. From this example, we will discuss two main considerations:

- the role of proper **experimental design** in setting up the study
- considerations for the **data collection process** in order to do **valid inference**

As you follow the discussion videos, your main take-away should not be particular details about this study. Rather, you should focus on developing an intuition on the important considerations for a study, as you may be conducting similar experiments or analyzing similar datasets of your interest in the future.

# **2. Introducing the mammography study**

Breast cancer is one of the most common fatal diseases among women. The earlier breast cancer is detected in a patient, the more likely it is for the patient to have a recovery and thus survive the disease. Screenings, as a result, play a large role in preventing breast cancer fatalities, and women over the age of 50 are nowadays advised to undergo a mammography once every two years.

While it may be intuitive to reason that mammographies prevent breast cancer fatalities through early detection, there are reasons to confirm this with data. For example, a local government may be considering standardizing mammographies as part of a healthcare plan. Having an estimate of the actual effect will allow one to evaluate the benefits of doing so in light of its costs.

# 3. Introduction to experimental design and hypothesis testing

## **3.1. Experimental design: variables**

Consider the overarching task to determine whether mammographies are effective in preventing breast cancer deaths. An experiment frames this in terms of assessing the effect of one variable to another. The most basic setting has two variables:

- the **treatment variable** , also called the **independent variable** , is what we are able to modify and is what causes the changes to other variables
- the **outcome variable** , also called the **dependent variable** , is what we observe and is what is affected by the treatment variable.

The goal of the experimental and statistical procedures is to establish the link between the treatment and the outcome variables. We call the overall procedure the **experimental design** .

## **3.2. Treatment and outcome variables in the mammography study**

For the mammography study, we determine what is the *treatment variable* and what is the *outcome variable*. We start with the outcome variable since it is more straightforward.

- For the *outcome variable*, we could set this to be **whether a given person (in the study) dies of breast cancer**. This is the real-life outcome that we intend to prevent. It is also a defined quantity (in both an aggregate and unit treatment terms).
- For the *treatment variable*, a natural first answer is whether or not a specific individual underwent mammography. It is, however, functionally infeasible to directly apply the “treatment" of making someone undergo mammography, since they may be simply unwilling to. We thus settle on the **treatment variable** to be whether someone is **offered** mammography,

By carefully defining the treatment and outcome variables in this study, we are able to specify what this study will analyze. The concrete definitions for these variables will also guide the data collection and analysis procedure.

## **3.3. Hypothesis testing**

The essence of hypothesis testing can be boiled down to the scenario where we have a claim and corresponding data that could help us evaluate its accuracy. In short, we want to answer the questions whether the data supports the claim or not. The claim is called the “hypothesis," and so the procedure is called “hypothesis testing."

Ideally, if we have access to all possible data in all possible outcomes of the world, we can reduce this to an arithmetic computation. In a more realistic situation, however, we only have a subset of the population that we have selected to work with. This generates an element of uncertainty, as we cannot control exactly which sample we obtain, and this is what gives rise to statistics.

We will start off by covering the data collection process, which is the process by which we generate these samples. This is part of the larger concept of experimental design, which also covers the procedure where we take the collected data to perform the appropriate inference about the hypotheses we have set up.

# 4. Study considerations and properties

From our setup so far, we discuss a few relevant points in designing our study. 

- Patient selection: Some populations are more likely to develop breast cancer than others depending on their prior health background, so the interpretation of any result we obtain will depend on how we have defined our selection procedure. In general, how we select the treatment and control groups will influence the population for which the conclusion is valid.
- Control group: We need to compare the outcome variable for those who have received the treatment with a baseline (i.e, the control group). Here, the control group (who were not offered a mammography) must be a **comparable** set of people to the treatment group (who have been offered a mammography).
- Features of the patients: One way to make accurate comparison and interpretation of results is to ensure that the treatment group is representative across factors such as health status, age, and ethnicity, and is similar along these dimensions as the control group. This way, we can attribute any differences in outcome to the treatment rather than differences in covariates. In a general study, it is upon the researchers' discretion to determine which features to be careful about. 

An approach that addresses the three points above is called the **Randomized Controlled Trial (RCT)** .

# 5. Randomized Controlled Trials (RCT)

A **Randomized Controlled Trial (RCT)** is an experimental design in which treatments are assigned at random.

We start with a large enough set of individuals (or “units"), divide them randomly into a treatment group and a control group. (In the language of experimental design, each distinguishable individual for which membership in the treatment or control group can be uniquely decided is called a **unit**.)

The treatment is applied to the treatment units, while the control units are either simply set aside for observation or are given a placebo treatment. Then, by the Law of Large Numbers, we will expect the difference in averages of any relevant feature between the two groups to be fairly small. This allows us take the difference of the mean of the outcome variables in the two groups in order to estimate the treatment effect.

RCTs are very common in medicine to evaluate a new medical product, such as a drug or a vaccine. The simplest case of an RCT is a drug trial, where patients for a particular disease are randomly assigned to the treatment or the control group. The patients in a treatment group receive the new drug being studied, while those in the control group receive a placebo drug. This placebo drug can either be an existing standard treatment or a drug with no medical effect (for example, a sugar pill). Then, we can later compare the outcomes of the patients who received the new drug as compared to those who received the placebo drug.

**Stratification in a randomized control trial**

One common modification to a RCT is to use **stratification** . Here, we pre-divide the population into groups and then sample proportionately from each group. This allows us to not leave the unbiasedness of our sampling, with regards to a particular classification or feature, up to chance. Stratification also enables **subgroup analysis** , which is analyzing the treatment effect within a particular group.

In the drug trial scenario, a common stratification will be done by splitting patients into groups according to certain demographic categories. This is due to there being a difference in many physiological functions across groups of different age, gender, or ethnicity. The randomized assignment can then be done within each group, which allows for valid inference both within each subgroup or as a whole by aggregating the results across groups.

**Sample size concerns**

In subgroup analyses, and in RCT's where our sample is small, however, we wil likely run into *sample size issues*, which could affect the precision of the estimate. When we are only sampling a small number of points, it is more likely for us to either hit a large number of consecutively large or consecutively small points, as compared to when our sample is large. Thus, a particular difference in outcome means will in some sense mean *less* in a small sample. We need a relatively large sample to detect a treatment effect that is small.

# 6. Ethical and Human Considerations in a Study

In a study, we have to be careful about human factors because overlooking these can cause biases in the whole experiment. Such biases can cause lapses in the causal reasoning which can invalidate the statistical conclusions of a study. In the academic peer review process, whether the proposed methodology addresses such biases is carefully reviewed. Besides methodological concerns, ethical considerations will also guide the choice of procedures performed throughout a study.

**Double blindness**

In any experiment that involves human subjects, factors related to human behavior may influence the outcome, obscuring treatment effects. For example, if patients in a drug trial are made aware that they actually received the new treatment pill, their behavior may change in a number of ways, such as by being more or less careful with their health-related choices. Such changes are very difficult to model, so we seek to minimize their effect as much as possible.

The standard way to resolve this is through a **double-blind study** , also called a **blinded experiment** . Here, human subjects are prevented from knowing whether they are in the treatment or control groups. At the same time, whoever is in charge of the experiment and anyone else who could interact with the patient are also prevented from directly knowing whether a patient is in the treatment or the control group. This is to prevent a variety of cognitive biases such as [observer bias](https://en.wikipedia.org/wiki/Observer_bias) or [confirmation bias](https://en.wikipedia.org/wiki/Confirmation_bias) that could influence the experiment.

In some cases, it is impossible to ensure that a study is completely *double-blind*. In the mammography study, for example, patients will definitely know whether they received a mammography. If we modify the treatment instead to whether a patient is *offered* mammography (which they could decline), then we neither have nor want double-blindness. Here, the patient's decision regarding whether to take the mammography once offered, and his/her subsequent behavior, is part of the causal effect that we are assessing.

**Ethical considerations and consent**

In this example, it is partly due to ethical considerations that we decided on our treatment to be whether a patient is offered mammography, rather than performing a mammography itself. Suppose, however, we are intent to assess the causal effect of actually performing the mammography. Then one option is to perform a large number of mammographies and then randomly discarding half of them (without any further action).

However, this option is ethically questionable, since giving half of the patients possibly false information about their breast cancer risk is dangerous. Every study involving human subjects has related ethical considerations, and all such research are subject to review by an appropriate review board.

In addition, **consent** is a major component in modern ethical standards, meaning that it is required for those in the study to understand its parameters and agree to its terms. Anyone involved as a subject in an experiment or study should be informed of its risks and possible consequences. (For example, see this [reference guide about consent](https://umc.edu/Research/Research-Offices/Clinical-Trials/Researchers/Road-Map/Study-Assessment/Design-ICF.html) in an experimental study.)

# 7. Randomization, and Control Variables

**Randomization**

A randomized control trial (RCT) allows us to identify the causal effect by ensuring that in expectation, the treatment and control group are identically distributed in terms of any relevant feature (or any feature, for that matter). The mammography study is such an example. Here, we can take a large sample of 62,000 adult women who are enrolled in a particular insurance plan, and offer 31,000 of them a mammography (the treatment) and do not offer the remaining 31,000 (the control).

Depending on the pair of treatment and outcome variables, it may not be possible to use an RCT to identify the causal effect. Suppose a researcher wishes to evaluate the effect of smoking on lung cancer incidence. We cannot directly change the person's behavior with regards to smoking, so we cannot formulate a RCT for this causal effect. However, if we tweak the treatment to be something that we can assign and thus randomize, such as whether one is given advice on the dangers of smoking, then this time we can assess the causal effect.

In situations where randomization is impossible, our best option is an **observational study**, where we attempt to estimate a causal effect from existing data. For example, when studying the effects of particular genes in humans, editing genes is considered unethical and hence not done. There are methods such as *instrumental variables* that allows us to use the causal effect from one treatment to estimate another relationship that we are more interested in. These methods, however, are out of scope for this course. (The course [14.310x Data Analysis for Social Scientists](https://mitxonline.mit.edu/courses/course-v1:MITxT+14.310x/) gives a fairly detailed overview of this technique.)

# 8. Observational study: confounding and control variables

Now, what could we do if randomization is not feasible? This means that methods-wise, we are limited to an **observational study** , where the researchers do not *apply* any treatment but rather only *observe* them. The complication in this scenario that it is unlikely for this treatment to be randomized.

**Confounding variables**

As the treatment is not randomized, we are unable to assess the causal effect by taking a difference in means. A bias in the difference in means arises when, even without any treatment, the units that are more likely to be treated have a different baseline outcome than the units that are less likely to be treated. As a result, we are unable to discern whether the difference is from the treatment's effect or from a difference in baseline values. This phenomenon is called **confounding** , and any external variable that can be identified to influence both the treatment and the outcome variables is called a **confounding variable** .

The stratification approach discussed earlier is a possible remedy to this. If the confounding variable is a demographic category, then balancing the treatment variable within each category resolves the issue. In the smoking example, a confounding variable is that people who are older both smoke more and are more susceptible to lung cancer. Then, sampling an equal number of smokers and non-smokers within each age group corrects for this confounding variable.

**Use of control variables**

The use of **control variables** is another fix to this issue. The study of control variables in the context of causality is complex, so we give a brief overview of what makes an appropriate control variable. In an ideal setting, we select controls that will capture all possible sources of bias, factors that lead to both the treatment and outcome values. Most studies will only identify a subset of these sources, however. After identifying the controls, there are a whole array of techniques to account for their effects, the most common of which is *multivariate regression*.

For example, consider a study that investigates the effect of years of education on income at age 30. We expect someone from a well-off family to stay in school longer for many reasons, one of which is the high cost of higher education. At the same time, one's socioeconomic status while growing up affects future income for reasons unrelated to education, such as through higher expectations and better informal networks. Thus, family income is an appropriate control.

**Control variable pitfalls and causality**

Next, we consider what could make a control variable inappropriate. Consider a study that investigates the effect of smoking on stroke incidence, as discussed in the video. Then, suppose hospitalization is proposed as a control variable, meaning that, for example, we conduct the observational study with patients in a particular hospital as our sample. This time, the control may in fact introduce bias, because both smoking and stroke can cause hospitalization, the former, albeit more indirectly. This will negatively bias the estimated relationship, because if we condition on hospitalized patients, the effect of one cause will crowd out the effect of the other.

Causal diagram of smoking, stroke, and hospitalization

![](https://courses.edx.org/assets/courseware/v1/561c113555d3a73f2c310e99502026d0/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_causal_diag.png)

To further illustrate why control on a common descendant variable in a casual diagram will lead to inference bias, we can see another simpler example:

Let X and Y be independent Bernoulli random variables (e.g. coin flips) and let Z= (X XOR Y). The relationship between X, Y and Z can be summarized in this causal graph: X \rightarrow Z \leftarrow Ywhere we have no arrow from X to Y or vice versa because X and Y are independent.

Now suppose we want to find out if X and Y are independent. If we look at many realizations of X and Ywe will come to the correct conclusion that the two are indeed independent. However, if we condition on Z, we will conclude that X and Y are negatively correlated so that the estimated effect of X on Y is negatively biased. To see why this is the case notice that if Z=1, then whenever X=0, Y must be 1. Zhere is a bad control because conditioning on it opens a so called "back-door" path from X to Y.

# **9. Initial data analysis and causal effect identification**

**Experiment Setup**

Let's first recap the experimental design for the HIP study. The population is the set of 700,000 female enrollees in the insurance program. For this experiment, 62,000 women were selected randomly and split into two groups: 31,000 in the control and 31,000 in the treatment groups. Those in the control group receive the standard healthcare as part of the insurance plan, while those in the treatment group in addition are offered four free mammographies (breast cancer screens) a year for five years; if anything abnormal were detected, she got early treatment. She could also choose to reject the screening.

**Examining Results**

In this experiment, 10,800 women rejected the screening while rest of 20,200 women accepted the screening. The main quantity of interest for each group is the death rate from breast cancer in the five years of follow-up. The number in each group and the rate are shown in the third column of the table, under the label "Breast cancer." Aside from this rate, the study also took note of the death rate from all other causes aside from breast cancer. This is similarly shown in the fourth column of the table. Later on, we will discuss why this statistic is also important.

HIP study: First large-scale randomized controlled experiment on mammography performed in 1960s

![](https://courses.edx.org/assets/courseware/v1/b3fb9b2a1e5ed662a4428098bf8f067b/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_HIP_Test.png)

How do we use the results from the table? If we want to show that being in the treatment group has an effect on reducing deaths due to breast cancer, then we clearly have to compare the death rate between this group and the control. To counter-check, however, we have to argue that the two groups are similar enough in terms of risk factors related to mortality. Indeed, if the rate of death from all other causes, as seen in the fourth column, is much higher in one group than another, then this is evidence that there may be a substantial difference. This difference may lead to different base rates of breast cancer deaths, which in turn make a direct comparison of the death rate inaccurate.

**Using other metrics in the table to assess a comparison**

The fourth column of the chart shows us why the only appropriate comparison is the full (\text {Total}) \text {Treatment} group with the \text {Control}group. The death rates due to all other cases are 27 and 28 per 1000, which are not very far. On the other hand, a common error is to compare the \text {Screened} and the \text {Control}. For these two groups, the \text {All other} death rates are 21 and 28 per 1000 respectively, which are significantly further apart. (For now, we are using a subjective judgement to decide on whether the \text {All other} death rates are significantly different. The methods in the following videos will apply to this as well.)

What causes the large difference in the rates of \text {All other} causes of death between the \text {Screened} group and the \text {Control} group? It is likely that conditional on being offered the screenings, whether a patient accepted the screenings or not gives information about their mortality rates. For example, those who accepted the mammography may tend to care more about their health and hence are less likely to die of other natural causes. It could also be that those already undergoing treatment for another disease will refuse due to possible complications.

In short, we want there to be no distinguishing factor between the groups we compare.

**Causal Effect Identification and Calculation**

Finally, we calculate the causal effect and also more precisely define what it represents. This is an **intention-to-treat analysis**, which focuses on the *intention* of offering a treatment rather than the actual treatment itself. In such an analysis, we compare the whole treatment group (everyone offered) against the whole control group.

From the table, we can get the following figures:

- Death rate from breast cancer in control group: 0.00203 (=\frac{63}{31000})
- Death rate from breast cancer in treatment group: 0.00126 (=\frac{39}{31000})

Hence, we can estimate the treatment effect to of offering mammography to be the difference in death rates: 0.00203 - 0.00126 = 0.00077, or around 0.77 deaths per 1000.

# 10. **Statistical models: Bernoulli and binomial models**

As an interlude, we will review the Bernoulli and binomial models. The Bernoulli model describes discrete events or their corresponding indicator variables, while the binomial model describes the sum of a fixed number of independent indicator variables. Both models are based on a probability parameter p, which corresponds to the probability that a given event occurs.

An **indicator variable** is a random variable that has a corresponding event. The indicator variable takes on the value 1 if the event occurs and the value 0if the event does not occur.

## **10.1. Bernoulli Distribution**

Bernoulli random variables are used to model random experiments with only two possible outcomes. In our example, an individual in the mammography study can experience only two possible outcomes: death attributed to breast cancer, represented by the outcome 1, or not, represented by 0.

A Bernoulli random variable with parameter p is a random variable that takes the value 1 with probability p and the value 0 with probability 1-p. The Bernoulli distribution is the discrete probability distribution of a Bernoulli random variable. Hence, we can write the Bernoulli probability mass function (pmf) as

$$
\displaystyle f(x)\displaystyle = \begin{cases} p & \text{if } x = 1 \\ 1-p & \text{if } x = 0 \end{cases}\displaystyle = p^ x(1-p)^{1-x}\displaystyle = px + (1-p)(1-x),
$$

where the bottom two expressions are alternate forms that could make calculations more tractable. From this pmf, we can derive its expectation to be p, the parameter itself, and its variance to be p-p^2 = p(1-p).

In many applications of the **Bernoulli model** with multiple indicator variables, they are **independent and identically distributed (i.i.d.)**, meaning that the indicator variables are mutually independent and that they are all Bernoulli with the same parameter p. The **Binomial distribution**, which will be discussed later, models this special case of multiple Bernoulli random variables.

### Bernoulli Model Exercise

Consider an application of the Bernoulli model to the mammography study, and index the patients in the control group from 1 to 31000. Define X_1, \ldots , X_{31000} to be random variables where X_ i is an indicator variable for whether patient i died of breast cancer.

Suppose that our model for breast cancer deaths is as follows: X_1,\ldots , X_{31000}\stackrel{\text {i.i.d}}{\sim } Bernoulli(p). Which of the following statements correctly describes the model?

a) In the model's data generating process, each participant has a probability p of dying from breast cancer and each participant's death is independent from other participants
b) Of the 31000 participants, 31000p are observed to die from breast cancer
c) Of the 31000 participants, a fixed set of 31000p patients have a probability of 1 of dying from breast cancer and while another set of 31000(1-p) patients have a probability of 0 of dying from breast cancer.

The correct description of the model is:

a) In the model's data generating process, each participant has a probability \( p \) of dying from breast cancer and each participant's death is independent from other participants.

### Explanation:

In the Bernoulli model, each patient's death due to breast cancer is modeled as an independent Bernoulli random variable \( X_i \) with parameter \( p \). This means that for each patient, the probability of dying from breast cancer is \( p \), and the outcome for each patient is independent of the others.

### Analysis of Other Statements:

- **Statement b):** This statement is not accurate because it implies a deterministic outcome where exactly \( 31000p \) participants die from breast cancer. In reality, the number of deaths will follow a binomial distribution with parameters \( n = 31000 \) and \( p \), and the actual number of deaths can vary around \( 31000p \) due to random variation.
- **Statement c):** This statement is incorrect because it suggests that a fixed set of participants are predetermined to die with certainty, while another set will not die, which does not align with the Bernoulli model where each participant's outcome is a random event with a probability \( p \).

The Bernoulli model described by statement a) correctly captures the essence of the model, where each participant independently has a probability \( p \) of experiencing the event of interest (death from breast cancer).

## **10.2. Binomial Distribution**

The **binomial random variable** with parameters n (trials) and p (probability) is defined as the sum of n independent Bernoulli random variables, all with parameter p. In the mammography example, if we model the deaths due to breast cancer in the control group by

$$
X_1,\ldots , X_{31000}\stackrel{\text {i.i.d}}{\sim } \text {Bernoulli}(p),
$$

then the number of such patient deaths can be modelled as a binomial random variable with parameter p. In statistical language, we say that a binomial random variable is the sum of *independent Bernoulli trials*, where each Bernoulli trial represents a single indicator variable.

From the definition, we can compute the probability mass function (pmf) of a binomial random variable Y with parameters n and p to be

$$
f(Y = k) = \binom {n}{k} \cdot p^ k \cdot (1-p)^{n-k}.
$$

where

- \displaystyle \binom {n}{k} is the number of different ways of choosing k out of the n Bernoulli variables.
- p^ k is the probability that a given set of k Bernoulli random variables all take value 1.
- (1-p)^{n-k} is the probability that a given set of n-k Bernoulli random variables all take value 0.

**Modelling breast cancer deaths in the control group**

We now model the number of breast cancer deaths in the control group as a binomial variable. First, since there are 63 deaths out of 31000 patients in the control group, we can estimate the parameter \displaystyle p = \frac{63}{31000} = 0.00203 (or 2.03 per 1000). That is, each patient's death is modeled as a Bernoulli variable with parameter p. The total number of breast cancer deaths is then a binomial model with 31000 Bernoulli trials and probability 0.00203 for each trial.

Binomial distribution with n = 31000 and p = 0.00203

![](https://courses.edx.org/assets/courseware/v1/efbc22cac2aee9bf30425e4200ee21d1/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_binomial_distribution.png)

### Binomial Calculation Exercise

Consider a binomial model where each of 31000 individuals has a probability of 0.00203 (or 2.03 per 1000) of dying due to breast cancer. Use the binomial pmf to calculate the probability that exactly 63 of the 31000 patients die of breast cancer.

(Enter a numerical answer accurate to at least 4 decimal places. You could compute the binomial coefficient in Python using the `scipy.special.comb(n, k)` command as part of the SciPy package. )

```python
from scipy.special import comb

# Define the parameters
n = 31000
p = 0.00203
k = 63

# Calculate the binomial pmf
binom_pmf = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
binom_pmf
```

## 10.3. **Poisson Distribution**

The **Poisson random variable** is based on taking the limit of a binomial distribution with a fixed mean np. As we take n \rightarrow \infty, the distribution converges to a fixed discrete pmf which we parameterize by \lambda = np. Indeed, we can compute the probability of k successes, substitute p = \lambda / n, and then take the limit.

$$
\displaystyle \lim _{n\to \infty } \binom {n}{k} p^ k (1-p)^{n-k}\displaystyle = \lim _{n\to \infty } \frac{n!}{k!(n-k)!} p^ k (1-p)^{n-k}\displaystyle = \lim _{n\to \infty } \frac{n(n-1)\ldots (n-k+1)}{k!} \left(\frac{\lambda }{n}\right)^ k \left(1-\left(\frac{\lambda }{n}\right)\right)^{n-k}\displaystyle = \lim _{n\to \infty } \frac{n(n-1)\ldots (n-k+1)}{n^ k} \frac{n^ k}{k!} \displaystyle = (1) \frac{\lambda ^ k}{k!} e^{-\lambda } = \frac{e^{-\lambda } \lambda ^ k}{k!}.\displaystyle = \lim _{n\to \infty } \left( \frac{n(n-1)\ldots (n-k+1)}{n^ k} \right) \frac{\lambda ^ k}{k!} \left(1-\left(\frac{\lambda }{n}\right)\right)^{n-k}\frac{\lambda ^ k}{n^ k} \left(1-\left(\frac{\lambda }{n}\right)\right)^{n-k}
$$

Therefore, when data follows binomial distribution with large n (number of trials) and small p (probability of success), Poisson(np) is a good approximation to Binomial(n,p).

Another interpretation of the Poisson random variable is in terms of a random process called the **Poisson process**. This is defined as a process where events can occur at any time in continuous time, with an average rate given by the parameter \lambda and satisfying the following conditions:

- Events occur independently of each other.
- The probability that an event occurs in a given length of time is constant.

**Application of the Poisson distribution**

We again consider the mammography study. In the control group, there are 31000 patients and we estimated the probability of each patient dying from breast cancer to be 0.00203.

Let n=31000 be number of independent Bernoulli trials and p=0.00203 be a constant probability of breast cancer death. We can then approximate the number of deaths as Poisson, under the following assumptions:

- One individual's death from breast cancer is independent from every other individual's death from breast cancer.
- The probability that a death occur in a five year window does not change over time.
- \text {Binomial}(31000,p) is well-approximated by \text {Poisson}(31000p), which is justified by \text {Binomial}(31000,0.00203) has a large n and a small p.

From the approximation definition, the plot of the pmf of Poisson(63) is thus very similar to the plot of the pdf of Binomial(31000, p).

Poisson distribution pmf with \lambda = 63

![](https://courses.edx.org/assets/courseware/v1/d5c753bd61dd8275a90901b7302263e0/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_poisson_distribution.png)

# **11. Hypothesis testing set-up: null and alternative hypotheses, test statistic**

Going back to the HIP mammography study, recall that we are interested to find out whether offering a mammography for early detection reduces deaths due to breast cancer. This is an **intent-to-treat** analysis, where the treatment variable is whether a patient is *offered* mammography, as this is what is relevant for policy purposes. From the study with 31000 patients in each of the control and treatment groups, data is collected and summarized in the table below.

HIP study: First large-scale randomized controlled experiment on mammography performed in 1960s

![](https://courses.edx.org/assets/courseware/v1/b3fb9b2a1e5ed662a4428098bf8f067b/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_HIP_Test.png)

We can see that the death rate per 1000 women due to breast cancer goes down from 2.0 in the control group to 1.3 in the treatment group. While this is a sizeable reduction, due to variance in different datasets, it may be the case that this reduction happened just by chance. Indeed, it is possible that if we are to repeat the study, the treatment group may now have a higher death rate. The role of

**hypothesis testing**

is to assess how significant the change was in the death rate.

## **Hypothesis testing and modelling overview**

A high-level summary of **hypothesis testing** is that it involves calculating the *probability*, under a given model, that an observation equal to or more extreme than what is observed in the treatment group is obtained, conditioned on the treatment having no effect. In the mammography study, we wish to calculate the probability that the treatment group has an observed death rate of 0.0013 or below, assuming that each patient in the treatment group has the same probability of death as in the control group.

The role of a **statistical model** is in calculating this probability. Without a model and its corresponding assumptions, we cannot determine how likely a particular observation in the treatment group is. In the mammography study, we use a Bernoulli model for the individual deaths, with the additional assumption that the deaths are independent and identically distributed. A Bernoulli model has a parameter, which we call \pi in this application. We can thus write the model, on the individual level, as

| X_1, X_2, \ldots , X_{31000} \stackrel{\text {i.i.d}}{\sim } \text {Bernoulli}(\pi ). |  |
| --- | --- |

In this example, we use the Poisson approximation of the sum of independent Bernoulli random variables, and the parameter \lambda for the Poisson approximation is based on the sum of the expected values of the Bernoulli r.v.'s. Since there are 31000 of them, each with parameter \pi, the parameter is then \lambda =31000\pi. Hence, we can model the *total* number of deaths due to breast cancer in the treatment group as

| Y = X_1 + X_2 + \ldots + X_{31000} \sim \text {Poisson}(31000\pi ). |  |
| --- | --- |

### **Null and alternative hypotheses**

Now, we formalize and generalize the hypothesis testing setup. We define two contrasting statements that together summarize the hypothesis testing objective. They are the **null hypothesis** and the **alternative hypothesis** . In a treatment-control experimental setting, they take on the following roles:

- Null hypothesis H_0: claim that the treatment *does not* have a significant effect on the outcome, also known as the *status-quo*.
- Alternative hypothesis H_ A: claim that the treatment *does* have a significant effect on the outcome.

When we have a *parameteric statistical model*, H_0 and H_ A can be formulated in terms of restrictions on the parameter. Indeed, in the mammography study, we can formulate the two contrasting claims on whether mammography is effective. This formulation is based on comparing the parameter \pi in the treatment group to the estimated parameter of 0.00203 in the control group.

- Null hypothesis H_0: \pi = 0.00203 (or equivalently, \lambda = 63), implying that offering mammography did not affect the breast cancer death rate
- Alternative hypothesis H_ A: \pi < 0.00203 (or equivalently, \lambda < 63), implying that offering mammography had the effect of decreasing the breast cancer death rate.

In general, if we have a parametric statistical model with parameter \theta, the null and alternative hypotheses are expressed as claims that the parameter is in sets \Theta _0 and \Theta _ A respectively. These two sets are assumed to be disjoint, but their union need not be equivalent to the whole parameter space. We do not impose this last requirement because the focus of hypothesis testing is to compare which of the two hypotheses is more likely to be the case, and we may ignore parameter values that are outside our scope of interest.

Now, we describe the procedure of hypothesis testing, given a statistical model and a pair of null and alternative hypotheses.

## **Hypothesis testing and the test statistic**

Hypothesis testing involves distinguishing between the **null hypothesis** and the **alternative hypothesis**. Under the null hypothesis, we have a baseline distribution (or set of distributions) of the observation from the model and the corresponding parameter(s). Based on the observation, we decide whether or not to **reject the null hypothesis**.

- We **reject the null hypothesis** if we deem it *relatively unlikely* for the null hypothesis to be true, given the observations.
- We **fail to reject the null hypothesis** if we *do not have sufficient evidence* from the observation to discredit the null hypothesis.

Notice the asymmetry between the two hypotheses. The conclusion from hypothesis testing is whether or not the null hypothesis is rejected. This results from the formulation of the null hypothesis being the *status quo*. If we decide to reject the null hypothesis, then the findings from the experiment as a whole is called **significant** .

The decision whether to reject the null hypothesis is based on a **test statistic** . The test statistic is a function of the random variables modelling the data. Hence it is a random variable itself, and its distribution depends on the parameters defining the model. For any specific hypothesis test, the test statistic that we choose needs to distinguish between the null and the alternative hypotheses, and have a distribution that is known and computable.

In the mammography example, we choose the test statistic T = Y = X_1 + X_2 + \ldots + X_{31000}, the number of deaths due to breast cancer in the treatment group. We expect Y to take a smaller value under the alternative hypothesis H_ A: \pi < 0.00203 than the null hypothesis H_0: \pi = 0.00203, so it will allow us to distinguish between the two. We also know the distribution of Y.

### **Significance level**

We will use the distribution of the test statistic under the null hypothesis to answer the following question:

*"Assuming that the null hypothesis is true, how likely is it for the test statistic to be at least as extreme (in the direction of the alternative hypothesis) as the one we have computed?"*

To answer this question in the mammography example, we compute the probability of the test statistic Y taking a more extreme value than the observed value 39, under the null H_0: \pi = 0.00203. Under the Poisson approximation, this is the probability of Y \leq 39 under the model Y \sim \text {Poisson}(63).

In the general hypothesis testing framework, we will then **reject the null hypothesis** if this probability is small enough, since this implies that if the null hypothesis is true, a test statistic as extreme as what we had observed is very unlikely. The **significance level**  \alpha refers to this probability threshold. In many applications, \alpha = 0.05 is used.

![](https://courses.edx.org/assets/courseware/v1/d01354a7a5c509c1f7580f5406bef8db/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_Hypothesis_Test.png)

1. Suppose we now instead have 30000 participants in the treatment group and 31000 participants in the control group. As before, we base the null hypothesis on the breast cancer death rate observed in the control group, which is 0.00203, and define Y as the number of deaths in the treatment group.
    
    Given that we now have different sized treatment and control groups, can we still model Y as a \text {Poisson} variable (approximated from a Binomial) and perform the same hypothesis test using Y as the test statistic? If so, what is the null hypothesis in terms of the parameter \lambda (of the Poisson model)?
    
    correct
    
2. Recall that we have the model X_1,\ldots , X_{31000}\sim Bernoulli(\pi) for the outcomes for each patient in the treatment group. We wish to distinguish between H_0: \pi = 0.00203 and H_ A: \pi <0.00203 using the test statistic T. How does T distinguish between H_0 and H_ A?
    
    correct
    
3. What is the distribution of T under H_0?
    
    correct
    
4. A hypothesis test is based on a given significance level \alpha. Following convention, we set \alpha = 0.05. For what observed value of T should we reject H_0?
    
    correct
    
5. In the data collected, what is the observed test statistic T? From this, do we reject the null hypothesis at a significance level of 0.05?   correct
    
    T =
    

The number of deaths due to breast cancer in the treatment group, Y, follows a \text {Binomial}(30000,\pi ) distribution. Under the null hypothesis, we have \pi = 0.00203. Therefore Y can be approximated by \text {Poisson}(30000\pi ), which under the null is \text {Poisson}(30000(0.00203)) = \text {Poisson}(60.9). Hence, we can approximate the distribution of T := Y under the null hypothesis using the \text {Poisson}(60.9) distribution.

1. Since we assumed that X_1,\ldots , X_{31000}\sim \text {Bernoulli}(\pi ), then \displaystyle T = \sum _{i=1}^{31000} X_ i \sim \text {Binomial}(31000,\pi ). Sum of independent Bernoulli random variables is a binomial random variable. We can see that under H_0, T should be larger, and under H_ A, T should be smaller. Therefore, T is a variable that changes with \pi, and can distinguish between H_0 and H_ A.
    
    Note that we are doing an one-tailed test. If T is much larger than 0.00203\cdot 31000, even though it is away from the expected 0.00203\cdot 31000, we will still think the data is compatible with the null hypothesis. Under null hypothesis, \pi = 0.00203. Therefore, T follows \text {Binomial}(31000,0.00203).
    
2. As discussed above, T\sim \text {Binomial}(31000,0.00203).
3. The threshold is x for which \mathbf{P}(\textrm{Binomial}(31000,0.00203)<x) = \alpha, which can be computed using the Python command scipy.stats.binom.ppf(0.05, 31000, 0.00203).
4. T = 39 is the number of observed death in the treatment group. As T\leq 49, we reject the null hypothesis.

## **Significance level and the p-value**

Recall that hypothesis testing is based on the probability that the test statistic takes on its current value or a more extreme one, assuming that the null hypothesis H_0 is true. This probability is defined as the **p-value**. From the definition of the significance level, another intrepretation is that the p-value is the smallest significance level \alpha such that we will reject the null hypothesis.

In other words, the p-value measures the "compatibility" of the observed data with the null hypothesis. The *lower* the P value, the less likely such data will be observed given the null hypothesis. Thus, the null hypothesis will be less convincing compared to the alternative hypothesis and we are *more likely* to reject it.

The p-value can be calculated by summing up or integrating values along the tail of the test statistic pmf/pdf towards the direction of the alternative hypothesis.

![](https://courses.edx.org/assets/courseware/v1/8641eb43022f4b954f2ab1a9dd6fd978/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_poisson_p_val.png)

The p-value is always between 0 and 1 and depends on the model. In the mammography study, the binomial model gives a slightly higher p-value (0.0012) than when the Poisson approximation is used (0.0008). In the exercise below, we will apply the concept of the p-value to the mammography study.

### P Value Exercise

2 points possible (graded)

1. Which of the following correctly describes the formula for the p-value in the mammography study, given an observation of Y = 39 deaths due to breast cancer in the treatment group of 31000? 
unanswered

2. Suppose that we are instead interested in whether offering mammography makes a difference in the breast cancer death rate. We thus change the alternative hypothesis to H_ A: \pi \neq 0.00203 while maintaining the null hypothesis H_0: \pi = 0.00203. Let Y be the observed number of deaths in treatment group. Which of the following correctly represents the p-value of an observation, in terms of the observation Y? unanswered

1. The p-value is defined as the probability of observing the observed or more extreme value of test statistic under H_0, in the direction towards H_ A. In this case, it is the probability of observing T \le 39under H_0.
2. In a two-tailed test, the p-value is the probability that the variable Y is at least as far from the value in the H_0 as the observed value. The corresponding test statistic is thus |T-63|, which will tend to have smaller values (i.e. T closer to 63) when \pi = 0.00203, rather than when \pi is far from 0.00203. Moreover, the deviation from the null hypothesis H_0 is 24 in the observation.

Let's analyze each part of the exercise:

### Part 1: Describing the Formula for the p-value

Given an observation of \( Y = 39 \) deaths due to breast cancer in the treatment group of 31,000, we need to identify the correct formula for the p-value in the mammography study.

### Options:

1. \( \mathbf{P}_{H_0}(T \leq 39) \): The probability under \( H_0 \) to obtain the observed value or a more extreme value of the test statistic.
2. \( \mathbf{P}_{H_0}(T = 39) \): The probability under \( H_0 \) to obtain the observed value of the test statistic.
3. \( \mathbf{P}_{H_A}(T = 39) \): The probability under \( H_A \) to obtain the observed value of the test statistic.
4. \( \mathbf{P}_{T < 39}(H_0) \): The probability that \( H_0 \) is true given the observed or more extreme value of the test statistic.

### Analysis:

- **Option 1** correctly describes the p-value as the probability under the null hypothesis \( H_0 \) to obtain the observed value or a more extreme value of the test statistic. This matches the definition of the p-value.
- **Option 2** incorrectly describes the p-value as it only considers the probability of observing the exact value of the test statistic under \( H_0 \).
- **Option 3** incorrectly describes the p-value as it considers the probability under the alternative hypothesis \( H_A \).
- **Option 4** incorrectly describes the p-value as it interprets the probability in the opposite direction (i.e., given the test statistic, it calculates the probability of the null hypothesis being true).

Thus, the correct description for the p-value in this context is:

\[ \mathbf{P}_{H_0}(T \leq 39) \]

### Part 2: p-value for the Alternative Hypothesis \( H_A: \pi \neq 0.00203 \)

We change the alternative hypothesis to \( H_A: \pi \neq 0.00203 \) while maintaining the null hypothesis \( H_0: \pi = 0.00203 \). We need to identify the correct representation of the p-value for an observation \( Y \).

### Options:

1. \( \mathbf{P}_{H_0}(|Y-63| \geq 24) \): The probability under \( H_0 \) to obtain the observed value or a more extreme value of the test statistic.
2. \( \mathbf{P}_{H_0}(Y \leq 39) \): The probability under \( H_0 \) to obtain the observed value of the test statistic.

### Analysis:

- **Option 1** correctly represents the p-value for a two-sided test. The absolute difference \( |Y - 63| \geq 24 \) accounts for the deviation in both directions (greater than or less than 63) from the expected value under the null hypothesis.
- **Option 2** only considers the one-sided probability, which is insufficient for a two-sided alternative hypothesis \( H_A: \pi \neq 0.00203 \).

Thus, the correct representation of the p-value for the observation \( Y \) in terms of the new alternative hypothesis is:

\[ \mathbf{P}_{H_0}(|Y - 63| \geq 24) \]

## **Type I error and type II error**

Hypothesis testing is an uncertain process due to inherent variation in the observations. There is thus the possibility of having the wrong conclusion, called **error**. The two types of error are as follows:

- **Type I error (false positive)**: We reject H_0 (equivalently, find the result *significant*) when H_0 is actually true. In the mammography study, it is concluding that offering mammography decreases the likelihood of breast cancer death even if it actually does not.
- **Type II error (false negative)** : We do not reject H_0 (equivalent, find the result *not significant*) when H_ A is actually true. In the mammography study, it is not concluding that offering mammography decreases the likelihood of breast cancer death when it actually does.

The two types of errors are shown in the off-diagonal entries in the matrix below. Note that the diagonal entries refer to a *correct* conclusion of either correctly *rejecting* or *failing to reject* the null hypothesis H_0 in favor of the alternative hypothesis H_ A.

![](https://courses.edx.org/assets/courseware/v1/208338a4cdae7edea059e017638ceee6/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_type_error.png)

We note that the *significance* level is in fact the probability of a *type I error*. Thus, setting the significance level to \alpha is equivalent to allowing this level of *type I error* to occur.

**Power of a test**

A related concept is the **power** of a test, which is defined as the probability of rejecting H_0 when H_ A is true, i.e. the probability of *correctly* rejecting the null hypothesis. In other words, Power = 1 - \mathbf{P}(Type II error).

The simplest case to discuss the power of a test is when we have a **simple hypothesis test**, which is when the test is parametric and both the null and the alternative hypotheses consist of a single parameter value. In the mammography study, we can for example have the following hypotheses on the parameter \pi.

- Null Hypothesis H_0: \pi = 0.002 (blue distribution on the right)
- Alternative Hypothesis H_ A: \pi = 0.0013 (orange distribution on the left)

The distribution of the test statistic under the null and the alternative hypotheses are shown in the plot below. The blue distribution on the right corresponds to the null hypothesis H_0, while the orange distribution on the left corresponds to the alternative hypothesis H_ A.

![](https://courses.edx.org/assets/courseware/v1/05e72462c6b04707e4ddc34fcd4549aa/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_power.png)

We reject H_0 if our sample has a p-value less than \alpha = 0.05, i.e. any value on the x-axis to the left of the vertical line separating the colored from the non-colored regions. The power is then the area to the left of this line that is under the curve given H_ A (the left curve), i.e. the area of the orange and blue regions combined.

### Type I and Type II Errors

3 points possible (graded)

1. Which of the following statement(s) is/are true?

Type I error + Type II error = 1

\mathbf{P}(Type I error) + \mathbf{P}(Type II error) = 1

\mathbf{P}(Type I error) = \alpha (significance level)= \mathbf{P}_{H_0}(\textrm{Reject } H_0) and is set by us

\mathbf{P}(Type I error) = \alpha (significance level) = \mathbf{P}_{H_0}(\textrm{Reject } H_0) and depends on the data

2. What is power of a test? Select all that applies.

1-\mathbf{P}(type II error)

\mathbf{P}*{H* A}(reject H_0)

1-\mathbf{P}(type I error)

\mathbf{P}_{H_0}(reject H_0)

3. Which of the following statement(s) is/are true?

Once we set \mathbf{P}(Type I error), \mathbf{P}(Type II error) is automatically set, does not depend on the data, and cannot be computed.

Once we set \mathbf{P}(Type I error), \mathbf{P}(Type II error) depends on both the data and the test statistic, and can be computed.

Once we set \mathbf{P}(Type I error), \mathbf{P}(Type II error) depends on the test statistic but not the data, and can be computed.

Once we set \mathbf{P}(Type I error), \mathbf{P}(Type II error) depends on the data and the test statistic, and can sometimes be computed.

With the same data set and the same \mathbf{P}(Type I error) but using a different test statistic, \mathbf{P}(Type II error) can differ.

We should look for \alpha such that \mathbf{P} (Type I error) + \mathbf{P} (Type II error) is minimized.

1. The third statement is true.

- The first statement is incorrect: type I error and type II error refer to events, not probabilities.
- The second statement is incorrect: P(Type I error) = P_{H_0}(reject null), P(Type II error) = P_{H_ A}(fail to reject null). They are conditional probabilities that are conditioned on different events, so they do not in general sum up to 1.
- The third statement is correct: the type I error is entirely controllable because we decide on the boundary for the test statistic as to whether we will reject the null hypothesis.

2. The power of a test is the probability of rejecting H_0 when H_0 is indeed false, and the Type II error is an error where we fail to reject H_0 when H_ A is true.

3. In a simple hypothesis test setting, the significance level \alpha and the test statistic together define the rejection region. We can then compute the probability of a type II error as the probability that the test statistic takes a value outside the rejection region, under the alternative hypothesis. The observation (data), which is a realization of the test statistic, will not effect the rejection region.

If we use a different test statistic, then its distribution under the null hypothesis and the alternative hypothesis can also change. Hence, even under the same significance level, the type II error can be different.

## **Hypothesis testing trade-offs: Type I vs II error, double vs single tailed**

This video discusses the trade-offs faced in hypothesis testing. In summary,

- There is a direct tradeoff between reducing the type I and type II errors. In nearly all cases, with a fixed test statistic, reducing the type I error results into increasing the type II error, and vice versa.
- Keeping the significance level constant, a one-sided hypothesis test has a higher power than the corresponding two-sided hypothesis test. An exception is when the distribution of the observation under the alternative hypothesis is bimodal.