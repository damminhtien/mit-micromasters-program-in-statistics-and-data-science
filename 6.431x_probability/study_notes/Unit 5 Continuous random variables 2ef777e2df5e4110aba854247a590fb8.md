# Unit 5: Continuous random variables

# Motivation

- Why continuous?
    - Physical quantities are often continuous
    - The power of calculus
    - Convenient approximations
- Same threads as in the discrete case
    - Definitions, notation
    - Properties of expectation and variance
    - Conditioning and independence
    - Total probability/expectation theorem
- Additional elements
    - Some concepts are more subtle
    - Interesting versions of Bayes’ rule

# Lecture 8: Probability density function

[Course | edX](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__8_Probability_density_functions)

In this lecture, we focus on a single continuous random variable, described in terms of a probability density function. We discuss the expectation, variance, and a new concept – the cumulative distribution function. We illustrate the concepts through specific examples of common random variables (uniform, exponential) and finally introduce the very important normal distribution.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/7f81a79c9c8ffe07a624955383a79316/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L08cleanslides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/5cf77ed9458e92c9b91d01c47649aba7/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L08annotatedslides.pdf)

More information is given in [Sections 3.1-3.3](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/19) of the text.

## 8.1. PDFs

## 8.2. **Uniform and piecewise constant PDFs**

## 8.3. **Means and variances**

## 8.4. Cumulative distribution function CDF

## 8.5. Normal random variable

# Lecture 9: Conditioning on an event; Multiple r.v.’s

[Course | edX](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__9_Conditioning_on_an_event__Multiple_r_v_s)

In this lecture, we introduce the conditional distribution of a random variable given an event, and then introduce the joint PDF as a way of describing the joint distribution of multiple random variables.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/aaa368319ef0c9e123487b93b02c2e08/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L09cleanslides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/57a0f6872b97da46ba13d1c799fdf344/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L09annotatedslides.pdf)

More information is given in [Section 3.4](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/23) and in the beginning of [Section 3.5](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/24) of the text.

## 9.1. **Conditioning a continuous random variable on an event**

## 9.2. **Memorylessness of the exponential PDF**

## 9.3. **Total probability and expectation theorems**

## 9.4. Mixed random variables

## 9.5. Joint PDFs

## 9.6. From the joint to the marginal

## 9.7. Continuous analogs of various properties

## 9.8. Joint CDFs

# Lecture 10: Conditioning on a random variables; Independence; Bayes’rule

[Course | edX](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__10_Conditioning_on_a_random_variable__Independence__Bayes_rule)

In this lecture, we introduce conditional PDFs, for describing the conditional distribution of a continuous random variable given another. We also introduce the concept of independence of continuous random variables and present some of the consequences of independence. We finally develop four variants of the Bayes rule, including variants that apply to the case where one random variable is discrete and another is continuous.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/21bf3a1f5fc510a0a86fd798691bc416/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L10cleanslides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/6c8c83fc76d5a7e1051ad1db173e976d/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L10annotatedslides.pdf)

More information is given in [Sections 3.5 and 3.6](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/24) of the text.

## 10.1. Conditional PDFs

## 10.2. Total probability and total expectation theorems

## 10.3. Independence

## 10.4. Independence normals

## 10.5. Bayes rule variations

## 10.6. Mixed Bayes rule

## 10.7. Inference of the bias of a coin

# Solved problems

## 6. Circular uniform PDF

**Circular uniform PDF.** Ben throws a dart at a circular target of radius $r$. We assume that he always hits the target and that all points of impact $(x,y)$ are equally likely. Compute the joint PDF $f_{X,Y}(x,y)$ of the random variables $X$ and $Y$, and compute the conditional PDF $f_{X|Y}(x|y)$.

[https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@sequential_Solved_problemsxxx/block-v1:MITx+6.431x+1T2024+type@vertical+block@ch8-s6-tab6](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@sequential_Solved_problemsxxx/block-v1:MITx+6.431x+1T2024+type@vertical+block@ch8-s6-tab6)

## 7. **The absent minded professor**

**The absent minded professor.** An absent-minded professor schedules two student appointments for the same time. The appointment durations are independent and exponentially distributed with mean 30 minutes. The first student arrives on time, but the second student arrives 5 minutes late. What is the expected value of the time between the arrival of the first student and the departure of the second student?

[https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@sequential_Solved_problemsxxx/block-v1:MITx+6.431x+1T2024+type@vertical+block@ch8-s6-tab7](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@sequential_Solved_problemsxxx/block-v1:MITx+6.431x+1T2024+type@vertical+block@ch8-s6-tab7)