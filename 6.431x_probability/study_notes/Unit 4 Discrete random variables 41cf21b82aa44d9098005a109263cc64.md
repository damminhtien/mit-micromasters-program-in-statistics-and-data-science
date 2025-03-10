# Unit 4: Discrete random variables

# Motivation

- Random variables
    - their distribution
    - expectation, variance
- Four main threads
    - definitions, notation
    - properties of expectation and variance
    - conditioning and independence
    - total probability/ expectation theorem
- Focus on discrete random variables
    - pay attention to notation

# Lecture 5: Discrete random variables: PMF and expectation

This lecture introduces random variables, the description of discrete random variables through probability mass functions, and the concept of expectation. The concepts are illustrated in the context of the most common discrete random variables: Bernoulli, uniform, binomial, and geometric.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/ca3078fab429bcc9db6f2b562e12f959/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L05-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/fe59e64db945dbc0bee1468169284f8e/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L05-annotated-slides.pdf)

More information is given in [Sections 2.1-2.4](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/9) of the text.

## 5.1. Definition of random variables

## 5.2. Probability mass function

## 5.3. Bernoulli and indicator random variables

## 5.4. Uniform random variables

## 5.5. Binomial random variables

## 5.6. Geometric random variables

## 5.7. Expectation

## 5.8. Properties of expectation; the expectation rule

## 5.9. Linearity of expectation

# Lecture 6: Variance; Conditioning on an event; Multiple random variables

In this lecture, we introduce the variance of a random variable and some of its properties. We then discuss conditional PMFs, given an event. Finally, we introduce the joint PMF, as a way of describing the distribution of multiple random variables, and develop the linearity property of expectations.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/55a6be8b73b1a9060f8003a1cffb0e6b/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L06-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/364fef85d8e4340712492e316cf2a5e1/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L06-annotated-slides.pdf)

More information is given in [Sections 2.4-2.6](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/10) of the text.

## 6.1. Variance

## 6.2. Conditional PMFs and expectations given an event

## 6.3. Total expectation theorem

## 6.4. Geometric PMF, memorylessness, and expectation

## 6.5. Joint PMFs and the expected value rule

## 6.6. Linearity of expectations and the mean of the binomial

# Lecture 7: Conditioning on a random variable; Independence of random variables

In this lecture, we introduce conditional PMFs, for describing the conditional distribution of a random variable given another. We also introduce the concept of independence of random variables, and present some of the consequences of independence.

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/dfe25fabda68cc9c6fdb1ac352a9660c/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L07-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/ed3e666b7201ed057bc53c61b930a15d/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L07-annotated-slides.pdf)

More information is given in [Sections 2.6-2.7](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/13) of the text.

## 7.1. Conditional PMFs

## 7.2. **Conditional expectation and the total expectation theorem**

## 7.3. **Independence of random variables**

## 7.4. Independence and expectations

## 7.5. **Independence, variances, and the binomial variance**

# Solved problems

## 5.1. PMF of a function of a random variable

PMF of a function of a random variable. Consider a r.v $X$ such that

$$
p_ X(x) = \frac{x^2}{a}, \quad x\in \{ -3,-2,-1,1,2, 3\}
$$

where $a>0$ is a real parameters.

1) Find $a$

2) What is the PMF of a r.v $Z=X^2$

### Solution

1) Because sum of all PMF(x) is 1

Let $\mathbf{p_X}(k)=\mathbf{P}(X=k)$

$p_X(-3)+p_X(-2)+p_X(-1)+p_X(1)+p_X(2)+p_X(3)=1$

$\Rightarrow \frac{(-3)^2}{a}+\frac{(-2)^2}{a}+\frac{(-1)^2}{a}+\frac{(1)^2}{a}+\frac{(2)^2}{a}+\frac{(3)^2}{a}=1$

$\Rightarrow a = 28$

2) $Z=X^2 \Rightarrow Z={1,4,9}$

$p_Z(1)=2/28$

$p_Z(4)=8/28$

$p_Z(9)=18/28$

## 5.2. Coupon collector problem

A particular professor is known for his arbitrary grading policies. Each paper receives a grade from the set $\{A+,A,B,C,D,F\}$, with equal probability, independently of other papers. How many papers do you expect to hand in before you receive each possible grade at least once?

### Solution

Y: the number of papers before receive the new grade from the begin

X: the number of papers before receive the new grade from the last one

Transition from Y (what the problem mentioned) to X, help us get a more natural way to solve this problem

We all know the X is the **Geometric distribution** with the parameter $\frac{6-i}{6}$. So the $\mathbb{E}(X_i)=\frac{6}{6-i}$. 

So, $\mathbb{E}(Y_k)=\mathbb{E}(\sum^{k-1}_{i=0}X_i)=\sum^{k-1}_{i=0}\mathbb{E}(X_i)=\sum^{k-1}_{i=0}\frac{k}{k-i}=k\sum^{k}_{i=1}\frac{1}{i} \approx k\text{ ln}(k)$

## 5.3. Conditioning example

Suppose that $X$ and $Y$ are independent, identically distributed, geometric random variables with parameter $p$. Show that

$$
\mathbf{P}(X=i \mid X+Y=n)=\frac{1}{n-1}, \qquad i=1,2,\ldots ,n-1
$$

### Solution

Use the conditional probability formula of Bayesian to solve