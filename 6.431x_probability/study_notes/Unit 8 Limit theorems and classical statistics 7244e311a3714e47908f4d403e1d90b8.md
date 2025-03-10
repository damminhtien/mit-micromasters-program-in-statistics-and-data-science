# Unit 8: Limit theorems and classical statistics

# Motivation

Unit overview slide: [[clean]](https://courses.edx.org/assets/courseware/v1/1c157716d845a92f5b87c6907baa6bcf/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U08-overview-slide.pdf)

Printable transcript available [here](https://courses.edx.org/assets/courseware/v1/4b97474cc3fc0cb224322d8893d5afe4/asset-v1:MITx+6.431x+1T2024+type@asset+block/transcripts_U08-Overview.pdf).

The material in this unit is covered in [Sections 5.1-5.4](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/38) and [9.1](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/68) of the text.

The same material, in live lecture hall format, can be found on OCW ([Lecture 19](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-19-weak-law-of-large-numbers/), [Lecture 20](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-20-the-central-limit-theorem/), [Lecture 23](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-23-classical-statistical-inference-i/)) and YouTube ([Lecture 19](http://www.youtube.com/watch?v=3eiio3Tw7UQ), [Lecture 20](http://www.youtube.com/watch?v=Tx7zzD4aeiA), [Lecture 23](http://www.youtube.com/watch?v=4UJc0S8APm4)).

In this lecture, we will learn

- $X,X_1,...,X_n$ i.i.d.
    - Weak law of large nummbers: $\frac{X_1+...+X_n}{n} \rightarrow \mathbb{E}[X]$
    - Central limit theorem: $X_1+...+X_n \approx \text{Normal distribution}$
- Estimating an unknown mean
    - accuracy of estimates
    - confidence intervals
- Classical statistics more generally
    - the philosophy
    - sample mean-based estimators
    - general methods (maximum likelihood)

# Lecture 18: Inequalities, convergence and the Weak Law of Large Numbers

Printable transcript available [here](https://courses.edx.org/assets/courseware/v1/44dbb9ade43f6dbf29d011fa463e7934/asset-v1:MITx+6.431x+1T2024+type@asset+block/transcripts_L18-Overview.pdf).

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/ddd41498e3d7aedd848267fbe4f49fe7/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L18-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/1d52249d662b098a3c9803e1de0757d6/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L18-annotated-slides.pdf)

The material in this lecture is covered in [Sections 5.1-5.3](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/39) of the text.

# [Lecture 19: The Central Limit Theorem](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__19_The_Central_Limit_Theorem__CLT_)

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/ac950ece6a1ab8c9aac5f8057ec1c1da/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L19-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/3d36b84f7f15203aaa1005f1e4a37569/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L19-annotated-slides.pdf)

The material in this lecture is covered in [Section 5.4](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/41) of the text.

**Note:** In all of the numerical examples in this lecture, one can of course bypass the normal table and use an online tool, such as the one found [here](http://stattrek.com/online-calculator/normal.aspx) or [here](http://onlinestatbook.com/2/calculators/normal_dist.html). Note also that such tools also allow you to go backwards, from the value of $\Phi (x)$ to the value of $x$.

# [Lecture 20: An introduction to classical statistics](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__20_An_introduction_to_classical_statistics)

This lecture provides a brief introduction to the so-called classical (non-Bayesian) statistical methods. Besides presenting the general framework, it includes a discussion of estimation based on sample means, confidence intervals, and maximum likelihood estimation.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/e00faa01de9afcbe03df96082f11c77d/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L20-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/5faf36c8620223354a754197363df5f0/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L20-annotated-slides.pdf)

The material in this lecture is covered in [Section 9.1](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/70) of the text.