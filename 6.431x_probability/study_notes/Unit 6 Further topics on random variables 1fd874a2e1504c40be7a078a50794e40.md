# Unit 6: Further topics on random variables

# Motivation

Unit overview slide: [[clean]](https://courses.edx.org/assets/courseware/v1/39d1b6c8d047bc497dc8893946112548/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U6overview.pdf)

In this unit we discuss a number of topics on random variables:

- Methods for calculating the distribution of a function of one or more random variables, including the special case of the sum of two independent random variables
- The concepts of covariance and correlation between two random variables
- An abstract perspective under which conditional expectations are viewed as random variables

# Lecture 11: Derived distribution

[Course | edX](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__11_Derived_distributions)

This lecture develops a method for finding the distribution (PMF or PDF) of a function of one or more random variables with known distribution.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/1b8585e226baa3938df06b2408ea9f1a/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L11cleanslides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/22d77661646e89b846880bb0955256a3/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L11annotatedslides.pdf)

The material in this unit is covered in [Sections 4.1-4.3](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/30) and [Section 4.5](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/36) of the text (omitting the material on transforms).

The same material, in a somewhat more condensed arrangement, in live lecture hall format, is covered in the last 30 minutes of Lecture 10 and in Lectures 11-12, available on OCW ([Lecture 10](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-10-continuous-bayes-rule-derived-distributions/), [Lecture 11](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-11-derived-distributions-convolution-correlation/), [Lecture 12](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-12-iterated-expectations-sum-of-a-random-number-of-random-variables/)) or YouTube ([Lecture 10](http://www.youtube.com/watch?v=H_k1w3cfny8), [Lecture 11](http://www.youtube.com/watch?v=l4NoMKEHQwM), [Lecture 12](http://www.youtube.com/watch?v=P7a4bjE6Crk)).

# Lecture 12: Sums of independent variables, covariance and correlation

[Course | edX](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__12_Sums_of_independent_r_v_s__Covariance_and_correlation)

This lecture covers two different topics: (i) the calculation of the PMF or PDF of the sum of independent random variables; and (ii) the concepts of covariance and correlation, and their main properties.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/e042ffdc66eeeb8c463107a8e78b6a5c/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L12cleanslides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/6f388c061df5f3f1d47bd83cbc315598/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L12annotatedslides.pdf)

More information is given in [Section 4.1](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/31) and [Section 4.2](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/32) of the text.

### Covariance

- Definition

$$
Cov(X,Y)=\mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]=\mathbb{E}[XY]-\mathbb{E}[X]E[Y]
$$

- Covariance properties
    - Covariance of its self   $Cov(X,X)=\mathbb{E}[(X-E[X])^2]=Var(X)=E[X^2]-E[X]^2$
    - Covariance of linear  $Cov(aX+b,Y)=aCov(X,Y)$ (assume 0 means)
    - Covariance of tri-r.v. $Cov(X,Y+Z)=\mathbb{E}[X(Y+Z)]=\mathbb{E}[XY]+\mathbb{E}[XZ]=Cov(X,Y)+Cov(X,Z)$ (assume 0 means)
- Variance of sum r.v.s

$$
Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)
$$

### Correlation

- Dimensionless version of covariance

$$
\rho(X,Y)=\mathbb{E}[\frac{X-\mathbb{E}[X]}{\sigma_X}.\frac{Y-\mathbb{E}[Y]}{\sigma_Y}]=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
$$

- Measure of the degree of “association between X and Y
- Independent ⇒ $\rho=0$, “uncorrelated” (converse is not true)
- $\rho(X,X)=\frac{var(X)}{\sigma_X^2}=1$
- $\rho(X,Y)=1 \Leftrightarrow (X-\mathbb{E}[X])=c(Y-\mathbb{E}[Y])$ (linearly related)
- $Cov(aX+b,Y)=aCov(X,Y) \Rightarrow \rho(aX+b,Y)=\frac{aCov(X,Y)}{|a|\sigma_X\sigma_Y}=sign(a).\rho(X,Y)$

# Lecture 13: Conditional expectation and variance revisited; Sum of a random number of independent r.v.s

[Course | edX](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/jump_to/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__13_Conditional_expectation_and_variance_revisited__Sum_of_a_random_number_of_independent_r_v_s)

This lecture explains that the conditional expectation and variance can be viewed, more abstractly, as random variables, and presents some of their properties, concluding with an application to the calculation of the mean and variance of the sum of a random number of random variables.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/b06ba69158bbe4e438087f16e240a8d1/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L13cleanslides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/5e5e30f21d0b68d7fea3d7c8f3ec7031/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L13annotatedslides.pdf)

More information is given in [Section 4.3](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/33) and [Section 4.5](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/36) of the text.

# Summary

[https://courses.edx.org/assets/courseware/v1/56aefd519182ec1ca3cf79f7c375782c/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U06summaryslides.pdf](https://courses.edx.org/assets/courseware/v1/56aefd519182ec1ca3cf79f7c375782c/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U06summaryslides.pdf)