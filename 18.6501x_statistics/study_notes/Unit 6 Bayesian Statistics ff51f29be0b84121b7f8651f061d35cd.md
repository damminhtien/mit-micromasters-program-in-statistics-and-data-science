# Unit 6: Bayesian Statistics

# [Lecture 18: Introduction to Bayesian Statistics](https://learning.edx.org/course/course-v1:MITx+18.6501x+1T2024/block-v1:MITx+18.6501x+1T2024+type@sequential+block@u6s1_Bayes1)

### **Bayesian Statistics Part 1**

At the end of this lecture, you will be able to do the following:

- Describe the **Bayesian approach** to statistical decision making.
- Explain the mechanisms of the Bayesian approach, particularly the **prior and posterior beliefs** .
- Understand the role and significance of the prior distribution in a Bayesian set-up.
- Identify the **Beta distribution** and its role in Bayesian statistics as a prior distribution on a one-dimensional parameter.

The Unit 5 slides below, which are for the next **2 lectures** , are also available in the resource tab at the top of this course site.

Materials: [[slide]](https://courses.edx.org/asset-v1:MITx+18.6501x+1T2022+type@asset+block@lectureslides_chap5-annot.pdf)

## 18.1. **Introduction to the Bayesian Framework**

**New concepts will come into play**

1. **Prior and Posterior Distributions**:
    - **Prior Distribution**: Represents your beliefs about the values of parameters before seeing the data. It's a distribution over the possible values of a parameter based on prior knowledge.
    - **Posterior Distribution**: Represents updated beliefs about the parameters after considering the data. It's derived from the prior distribution and the likelihood of the observed data, integrating all information known up to that point.
2. **Bayes’ Formula**:
    - Bayes' formula is used to update the probability estimate for a hypothesis as more evidence or information becomes available. It relates the conditional and marginal probabilities of events A and B:
    
    $$
    P(H \mid E) = \frac{P(E \mid H) \times P(H)}{P(E)}
    $$
    
    Where:
    
    - $P(H \mid E)$ is the posterior probability of the hypothesis (H) given the evidence (E).
    - $P(E \mid H)$ is the likelihood of observing the evidence given that the hypothesis is true.
    - $P(H)$ is the prior probability of the hypothesis.
    - $P(E)$ is the total probability of the evidence across all possible hypotheses.
3. **Priors: Improper, Non-informative**:
    - **Improper Priors**: These are prior distributions that are not proper probability distributions because they do not integrate to one. They are often used in theoretical or computational contexts to simplify calculations.
    - **Non-informative Priors**: These are priors designed to have minimal impact on the posterior distribution, used when little prior information is available. They aim to represent a state of ignorance about the parameters before seeing the data.
4. **Bayesian Estimation: Posterior Mean, Maximum a Posteriori (MAP)**:
    - **Posterior Mean**: The mean of the posterior distribution, providing a point estimate of the parameter that incorporates both the data and prior beliefs.
    - **Maximum a Posteriori (MAP)**: The mode of the posterior distribution. It represents the most likely value of the parameter given the data and the prior distribution.
5. **Bayesian Confidence Region**:
    - Bayesian confidence regions are intervals or areas in the parameter space that are believed, with a certain probability, to contain the true parameter value. These regions are based on the posterior distribution and reflect the uncertainty of the parameter estimates given the data and the priors.

### Exercise 1: **Frequentist vs. Bayesian I**

1. **In Bayesian statistics, the true parameter is modeled as a random variable, or at the very least, the uncertainty regarding the true parameter is modeled as such.**
    - **True.** This is a fundamental aspect of Bayesian statistics. Unlike the frequentist approach, where parameters are considered fixed but unknown quantities, Bayesian statistics treats them as random variables. This allows for modeling the uncertainty about these parameters explicitly through probability distributions.
2. **In most practical applications of Bayesian statistics, we are trying to estimate the true parameter only from the observation data and our chosen model.**
    - **False.** This statement is misleading as it closely aligns with the frequentist approach, which typically relies on data from observations to make inferences about parameters without considering prior beliefs or information. In contrast, Bayesian statistics not only uses the data and the model but also incorporates prior knowledge or beliefs about the parameters through prior distributions.
3. **In Bayesian statistics, we use the data to update our prior belief about a parameter and transform it into a posterior belief, which is reflected by a posterior distribution.**
    - **True.** This statement correctly describes the Bayesian approach. Bayesian inference uses Bayes' Theorem to update the probability estimate for a hypothesis as more evidence or information becomes available. This process transforms the prior distribution, based on initial beliefs before seeing the data, into a posterior distribution, which combines the prior with the likelihood of the observed data.

### Exercise 2: Frequentist vs. Bayesian II

Which of the following scenarios require a Bayesian approach, rather than a frequestist approach, in order to utilize all information provided? (Choose all that apply.)

1. On any given day, the weather is either rainy with probability p, or not rainy, with probability 1-p. If the weather is rainy, then the commute times of individuals are i.i.d. exponential random variables, with parameter \lambda _1. If it is not rainy, then the commute times of individuals are, again, i.i.d. exponential random variables, with parameter \lambda _2. Assume that, you observe commute time of n different individuals to the workplace, and based on this, you want to understand whether the weather is rainy or not.
2. On any given day, if the weather is rainy, then the commute times of individuals are i.i.d. exponential random variables, with parameter \lambda _1. If it is not rainy, then the commute times of individuals are, again, i.i.d. exponential random variables, with parameter \lambda _2. Assume that, you observe commute time of n different individuals to the workplace, and based on this, you want to understand whether the weather is rainy or not.
3. A professor's mood often swings, and he is either happy with probability \alpha, or sad, with probability 1-\alpha, independent of everything else. If he is happy, he solves any problem he is asked, in a time which has a p.d.f. f_1(x) supported on (0,\infty ). If his mood is sad, then he solves a problem, in a time, which has p.d.f. f_2(x), again, supported on (0,\infty ). Assuming that his attempts to each problem are i.i.d. trials; his students ask him n questions to determine whether he is happy or sad.
4. A professor's mood often swings. If he is happy, he solves any problem he is asked, in a time which has a p.d.f. f_1(x) supported on (0,\infty ). If his mood is sad, then he solves a problem, in a time, which has p.d.f. f_2(x), again, supported on (0,\infty ). Assuming that his attempts to each problem are i.i.d. trials; his students ask him n questions to determine whether he is happy or sad.

**Solution:**

The Bayesian views are first and third choices. Recall that, the Bayesian view allows us to reflect our prior belief about the hypotheses that are being considered. In the first choice, the first hypothesis is, weather is rainy; and the second hypothesis is it is not rainy; and we have a prior. In the second choice, however, we only state the distribution of the observation under each hypotheses, while not stating our prior belief about hypotheses; hence, it is **not** Bayesian.

Similarly, in the third choice, there are two hypotheses; namely, "Professor is happy" and "Professor is sad". We put a prior on them, and stated how the observations (i.e., problem solving time) are distributed under each hypothesis, which again represents a Bayesian approach. Finally, the last part is **not** Bayesian due to the absence of a prior.

### Exercise 3: Designing Priors for an Experiment: Coin tossing

In a coin tossing experiment, let Y_1,Y_2,\dots ,Y_ n be i.i.d. random variables corresponding to the toss of the same coin whose bias \theta is unknown. Assume that the model is

$$
\mathbf{P}_{Y\mid \theta }={\rm Ber}(\theta ),
$$

and that the coin lands heads or tails with some positive probability. We want to design a prior for the unknown bias, in order to estimate the bias of the coin.

Which one of the following distributions would be a realistic candidate to model the prior on the set of all possible biases \Theta?

**Solution:**

The answer is the uniform distribution.

Since the bias, \theta is a parameter for the coin tossing, we have, \Theta = [0,1]. Namely, we need a distribution supported on the set [0,1].

- The Bernoulli distribution may not be used as it only allows the bias to be 0 or 1, which means that the coin either always lands heads or tails, whereas we assumed that the coin lands heads or tails with some positive probability.
- Since the exponential distribution is supported on (0,\infty ), it cannot be a correct candidate for the prior.
- A uniform distribution is a possible candidate; which reflects that we believe equally for each value of the \theta \in [0,1].
- Finally, a Gaussian distribution is, again, not a possible candidate, since it has a support of (-\infty ,\infty ).

### Exercise 4: Scientist in the Desert

Suppose that a crazy scientist is traveling with his car in the desert. All of a sudden, he realizes that the engine's oil lamp is broken. Hence, he needs to estimate the remaining oil level to determine whether he can continue driving or should instead seek help. Since he has studied Bayesian statistics before, he wants to set up an experiment to estimate the oil level of his car, but for this, he needs a prior distribution on the oil level. Let us denote the density of the prior on the oil level by f_ o(x). The scientists knows that at any given time, the oil level x is guaranteed to be a real number in the interval [0,100].

Which properties should f_ o(\cdot ) obey in order to result in a valid probability distribution and also reflect the scientist's knowledge of the car? (Choose all that apply.)

1. f_ o(x)\geq 0, for every x\in [0,100].
2. \displaystyle \int *0^{100}f* o(x)\; dx = 1.
3. \displaystyle \int *{-\infty }^{0}f* o(x)\; dx =0.
4. \displaystyle \int *{100}^\infty f* o(x)\; dx= 0.
5. \max *{x\in [0,100]}f* o(x)=f_ o(50), namely, f_ o(\cdot ) attains its maximum, in the midpoint of the interval.
6. f_ o(\cdot ) should be a decreasing function, on [0,50), and on (50,\infty ].

**Solution:**

First of all, independent of the experiment, the conditions for f_ o(\cdot ) to be a valid p.d.f., it should be non-negative on its support and must integrate to one on its support. The first two choices satisfy these conditions.

Furthermore, we must also have,

$$
\int _{-\infty }^{0}f_ o(x)\;  dx =0 = \int _{100}^{\infty }f_ o(x)\;  dx,
$$

since the oil level is between [0,100].

The last two parts are not necessarily properties of a probability distribution. As a counterexample, the truncated normal distribution centered at x=40 satisfies neither of the last two properties.

### Exercise 5: Prior Design for a Gambler

While on your way to work, you see a gambler who invites people to bet on a coin that he is repeatedly tossing. You suspect that his coin is biased and that he is cheating people out of their money; in particular, you think that it is more likely for the coin to be biased one way or the other, and that it is unlikely that the coin is fair. In order to further understand this, you decide to model the bias of the coin, \theta, using Bayesian statistics.

You have a **prior belief** is that the gambler's coin is *biased* (remember that the bias can be either way: either towards Heads or Tails). One reasonable criterion for the prior to reflect the belief stated above is for \pi (\theta ) to attain its minimum at 1/2, be *strictly decreasing* from [\epsilon , \frac{1}{2}], and lastly *strictly increasing* from [\frac{1}{2}, 1-\epsilon ]. Which of the following priors satisfies this given criterion? (Choose all that apply.)

(Note: for each answer choice, the denominator Z is chosen to make sure that the integral of the density over its support is equal to 1. Moreover, we restrict ourself to the bias values in the interval [\epsilon , 1-\epsilon ], rather than the actual interval, (0,1). Here we assume that \epsilon is a very small number, e.g. \epsilon = 10^{-5}. You may want to use software to graph the given functions.)

1. \pi (\theta )\sim {\rm Unif}[\epsilon ,1-\epsilon ]
2. \pi (\theta )= \frac{\theta ^2+(1-\theta )^2}{Z}, \theta \in [\epsilon ,1-\epsilon ]
3. \pi (\theta )= \frac{\theta (1-\theta )}{Z}, \theta \in [\epsilon ,1-\epsilon ]
4. \pi (\theta )= \frac{1/\theta +1/(1-\theta )}{Z}, \theta \in [\epsilon ,1-\epsilon ]

**Solution:**

- As the uniform distribution weights each possibility equally, it cannot be a correct choice.
- Note that $f(\theta )=\theta ^2+(1-\theta )^2 = 2\theta ^2-2\theta +1\implies f'(\theta )=4\theta -2.$

Setting the first derivative equal to 0, we obtain that, f(\theta ) attains its minimum at 1/2, and so does \pi (\theta ). It also implies that \pi (\theta ) is indeed decreasing in [\epsilon , \frac{1}{2}] and increasing in [\frac{1}{2}, 1-\epsilon ].

- As discussed in the lecture, the function \theta (1-\theta ) obtains its **maximum** at \theta =1/2, so it cannot be a suitable prior for this experiment.
- Finally, as $\pi (\theta )\propto \frac{1}{\theta (1-\theta )},$
    
    and f(\theta )=\theta (1-\theta ) attains its maximum at 1/2, \pi (\theta ) attains its minimum at 1/2. In addition, \pi (\theta ) is decreasing in [\epsilon , \frac{1}{2}] and increasing in [\frac{1}{2}, 1-\epsilon ], as desired.
    

### Exercise 5: An Observation Model

Let $\theta \sim \pi (\theta )$ be a parameter supported on \mathbb {Z}, the integers. Suppose that we observe random variables $Y_ i=\theta X_ i$ for i = 1, \ldots , n. The outcomes of X_1, \ldots , X_ n are unknown to you, but you do know that they are i.i.d. and uniformly distributed on the set \{ -1,0,1\}. Assume that X_ i is independent of \theta for all i.

Compute each of the probabilities below:

- $\mathbb {P}(Y_1=6 \text { and } Y_2=0|\theta =3)$=?
- $\mathbb {P}(Y_1=7 \text { and } Y_2=-7 \text { and } Y_3\in \{ 0,7\} |\theta = -7)=$?
- $\mathbb {P}(Y_1=Y_2+Y_3|\theta =5)$=?

**Solution:**

- Note that, conditional on \theta =3,
    
    
    | Y_1=6,Y_2=0 \implies X_1=2, X_2=0. |  |
    | --- | --- |
    
    Since X_1\in \{ -1,0,1\}, this probability is 0, as X_1 cannot be 2.
    
- Similar to the item above, we have, conditional on \theta =-7,
    
    
    | Y_1=7,Y_2=-7,Y_3\in \{ 0,7\} \implies X_1=-1,X_2=1\quad \text {and}\quad X_3\in \{ 0,1\} . |  |
    | --- | --- |
    
    In particular,
    
    | \mathbb {P}(Y_1=7 \text {and} Y_2=-7 \text {and} Y_3\in \{ 0,7\} |\theta = -7) = \mathbb {P}(X_1=-1 \text {and} X_2=1 \text {and} X_3\in \{ 0,1\} ), |  |
    | --- | --- |
    
    which, by using independence, is equal to,
    
    | \mathbb {P}(X_1=-1 \text {and} X_2=1 \text {and} X_3\in \{ 0,1\} ) = \mathbb {P}(X_1=-1)\mathbb {P}(X_2=1)\mathbb {P}(X_3\in \{ 0,1\} )=\frac{1}{3}\cdot \frac{1}{3}\cdot \frac{2}{3}=\frac{2}{27}. |  |
    | --- | --- |
- Note that,
    
    
    | Y_1=Y_2+Y_3 \iff X_1 = X_2+X_3. |  |
    | --- | --- |
    
    In particular, using the law of total probability,
    
    | \mathbb {P}(X_1=X_2+X_3)=\sum _{i=-1}^1\mathbb {P}(X_1=X_2+i|X_3=i)\mathbb {P}(X_3=i)=\frac{1}{3}\cdot \frac{1}{3}+\frac{2}{9}\cdot \frac{1}{3}+\frac{2}{9}\cdot \frac{1}{3} = \frac{7}{27}. |  |
    | --- | --- |
    
    since, \mathbb {P}(X_3=i)=1/3 for each i\in \{ -1,0,1\} and
    
    - if i = -1, then X_1 = X_2 -1 iff (X_1, X_2) = (0, 1) or (X_1, X_2) = (-1, 0);
    - if i = 0, then X_1 = X_2 in three possible ways: X_1 = X_2 = j for j \in \{ -1,0,1\}; and
    - if i = 1, then X_1 = X_2 + 1 iff (X_1, X_2) = (1,0) or (X_1, X_2) = (0, -1).

### Exercise 6: Probability Review: Bayes' Rule

Assume that, each person is Republican or Democrat with probability 1/2 for each; independent of any other person. If two persons are of same political view, they become friends with probability a; and if they are of opposite political view, they become friends with probability b.

What is the probability that Amy and Ben are friends?

Given that Amy and Ben are two friends, what is the probability that they have the same political views?

**Solution:**

- Let [mathjaxinline]E[/mathjaxinline] be the event that Amy and Ben are friends, and let [mathjaxinline]\sigma _ A[/mathjaxinline] denote the view of Amy; and [mathjaxinline]\sigma _ B[/mathjaxinline] denote the view of Ben. Observe that,
    
    
    |  | [mathjaxinline]\displaystyle \mathbb {P}(\sigma _ A=\sigma _ B)[/mathjaxinline] | [mathjaxinline]\displaystyle =\mathbb {P}(\sigma _ A=\sigma _ B=\text {Republican})+\mathbb {P}(\sigma _ A=\sigma _ B=\text {Democrat})[/mathjaxinline] |  |  |
    | --- | --- | --- | --- | --- |
    |  |  | [mathjaxinline]\displaystyle =\frac{1}{2}\cdot \frac{1}{2}+\frac{1}{2}\cdot \frac{1}{2}[/mathjaxinline] |  |  |
    |  |  | [mathjaxinline]\displaystyle =1/2,[/mathjaxinline] |  |  |
    
    where, the first line uses the definition (namely, Amy and Ben have the same political view, if and only if, either both are Democrat; or both are Republican), and the second line uses the independence, and uniformity of the distribution. Similarly, [mathjaxinline]\mathbb {P}(\sigma _ A\neq \sigma _ B)=1/2[/mathjaxinline]. With this,
    
    | [mathjax]\mathbb {P}(E)=\mathbb {P}(E|\sigma _ A=\sigma _ B)\mathbb {P}(\sigma _ A=\sigma _ B)+\mathbb {P}(E|\sigma _ A\neq \sigma _ B)\mathbb {P}(\sigma _ A\neq \sigma _ B)=\frac{a+b}{2},[/mathjax] |  |
    | --- | --- |
    
    using the law of total probability.
    
- Our goal is to compute,
    
    
    | [mathjax]\mathbb {P}(\sigma _ A=\sigma _ B|E),[/mathjax] |  |
    | --- | --- |
    
    which, by Bayes' rule;
    
    |  | [mathjaxinline]\displaystyle \mathbb {P}(\sigma _ A=\sigma _ B|E)[/mathjaxinline] | [mathjaxinline]\displaystyle =\frac{\mathbb {P}(E|\sigma _ A=\sigma _ B)\mathbb {P}(\sigma _ A=\sigma _ B)}{\mathbb {P}(E)}[/mathjaxinline] |  |  |
    | --- | --- | --- | --- | --- |
    |  |  | [mathjaxinline]\displaystyle =\frac{a\cdot (1/2)}{((a+b)/2)}[/mathjaxinline] |  |  |
    |  |  | [mathjaxinline]\displaystyle =\frac{a}{a+b}.[/mathjaxinline] |  |  |

## 18.2. **The Posterior Distribution, Bayes' Formula**

### Exercise 7: Prior Implications to Posterior: True or False

Consider the case of a binary parameter \theta \in \{ 0, 1\}. We have the prior distribution \pi (\theta ) that satisfies \pi (0)=p and \pi (1)=1-p, for some 0 \leq p \leq 1. Then, we observe X_1, \ldots, X_ n with corresponding conditional likelihood function L(X_1, \ldots , X_ n | \theta ) that is positive for both \theta =0 and \theta =1. Which of the following statements about the posterior distribution \pi (\theta |X_1, \ldots , X_ n) is true? (Choose all that apply.)

1. If p=0, then the posterior distribution will be identical to the prior distribution.
2. If p=1, then the posterior distribution will be identical to the prior distribution.
3. If p < \frac{1}{2}, then in the posterior distribution, \pi (\theta =0|X_1, \ldots , X_ n) \leq \pi (\theta =1|X_1, \ldots , X_ n) will necessarily be true.
4. If p > \frac{1}{2}, then in the posterior distribution, \pi (\theta =0|X_1, \ldots , X_ n) \geq \pi (\theta =1|X_1, \ldots , X_ n) will necessarily be true.

**Solution:**

In the cases where p=0 or p=1, the prior distribution would have one of \pi (0) or \pi (1) as 1 and the other as zero. As Bayes' rule gives that the posterior distribution \pi (\theta |X_1, \ldots , X_ n) is the conditional likelihood function L(X_1, \ldots , X_ n|\theta ) multiplied by the prior distribution, this means that if the prior is 0 for a certain \theta, the product will still be zero in the (un-normalized) posterior.

Furthermore, as we've assumed the likelihood to be positive for any \theta, the product will be positive in the (un-normalized) posterior. Hence, after normalization, we will get a posterior probability of 1 for the \theta that has a probability of 1 in the prior, and a 0 for the other, making the posterior identical to the prior. Thus the choices

**“If p=0, then the posterior distribution will be identical to the prior distribution."**

and

**“If p=1, then the posterior distribution will be identical to the prior distribution."**

are correct.

The third and fourth choices are incorrect because it is possible for the likelihood function to skew the posterior probability in the other direction. For example, consider a prior with \pi (0)=0.3, \pi (1)=0.7, as well as likelihoods L(X_1, \ldots , X_ n | \theta =0)=0.9 and L(X_1, \ldots , X_ n | \theta =1)=0.1. Then Bayes' rule gives \pi (\theta =0|X_1, \ldots , X_ n)=\frac{(0.3)(0.9)}{(0.3)(0.9)+(0.7)(0.1)}=\frac{27}{34} and \pi (\theta =1|X_1, \ldots , X_ n)=\frac{(0.7)(0.1)}{(0.3)(0.9)+(0.7)(0.1)}=\frac{7}{34}, so we get \pi (\theta =0|X_1, \ldots , X_ n) > \pi (\theta =1|X_1, \ldots , X_ n), contrary to the third statement.

A similar example where the roles of \theta =0 and \theta =1 are reversed would disprove the fourth choice.

### **Exercise 8: Updating Prior (Belief Propagation)**

In this problem, we will explore how to update the belief successively, having observed data. The model is as follows:

- \theta \in \Theta, the parameter space; and \pi (\cdot ) is the prior distribution of \theta.
- We observe i.i.d. (conditional on the parameter) data X_1, \ldots, X_ n and calculate the likelihood function L_ n(X_1, \ldots , X_ n|\theta ) (as in the setting of maximum likelihood estimation)
- Write \phi (X_1, \ldots , X_ n) as a placeholder function that depends on X_1, \ldots , X_ n, but not on the parameter \theta. (\phi could stand for different functions in different equations. It's simply a placeholder whenever we want to collect terms that only depend on X_1, \ldots , X_ n.)

In this context, we add observations one by one, computing the likelihood L_ i(X_1, \ldots , X_ i|\theta ) and posterior \pi (\theta |X_1, \ldots , X_ i) after each observation i. Which of the following identities are true? (Choose all that apply.)

**Solution:**

All the choices are correct. To see this, we proceed as follows. For brevity of notation, let \alpha _ n = \pi (\theta |X_1,\dots ,X_ n); \beta _ n=L_ n(X_1,X_2,\dots ,X_ n|\theta ). We also use X as a compact notation to represent X_1,X_2,\dots ,X_ n, so that \phi (X) corresponds to \phi (X_1, \ldots , X_ N).

- Note that, using Bayes' rule,
    
    
    |  | \displaystyle \alpha _ n(\theta ) | \displaystyle =\pi (\theta |X_1,\dots ,X_ n)=\frac{p_ n(X_1,\dots ,X_ n|\theta )\pi (\theta )}{\int _\Theta p_ n(X_1,\dots ,X_ n|t)\pi (t)\; dt} |  |  |
    | --- | --- | --- | --- | --- |
    |  |  | \displaystyle =\pi (\theta )\beta _ n(\theta )\phi (X), |  |  |
    
    where, \phi (X) captures the term in the denominator. This does not depend on \theta as we have already integrated over the variable.
    
- Similarly, using the independence of X_1,\dots ,X_ n conditional on \theta,
    
    
    | \beta _ n(\theta )=p_ n(X_1,\dots ,X_ n|\theta )=p_{n-1}(X_1,\dots ,X_{n-1}|\theta )\cdot p(X_ n|\theta )=\beta _{n-1}(\theta )\cdot p(X_ n|\theta ). |  |
    | --- | --- |
- For this part, note that,
    
    
    |  | \displaystyle \alpha _ n(\theta ) | \displaystyle =\pi (\theta |X_1,\dots ,X_ n) |  |  |
    | --- | --- | --- | --- | --- |
    |  |  | \displaystyle =\frac{p_ n(X_1,\dots ,X_ n|\theta )\pi (\theta )}{\widetilde{\phi }(X)} |  |  |
    |  |  | \displaystyle =\frac{p_{n-1}(X_1,\dots ,X_{n-1}|\theta )\pi (\theta )p(X_ n|\theta )}{\phi (X)} |  |  |
    |  |  | \displaystyle \propto p(X_ n|\theta )\underbrace{p_{n-1}(X_1,\dots ,X_{n-1}|\theta )\pi (\theta )}_{\propto \alpha _{n-1}(\theta )} |  |  |
    |  |  | \displaystyle \propto \alpha _{n-1}(\theta )p(X_ n|\theta ). |  |  |
- This follows by rearranging the first identity and taking the reciprocal of \phi.

# [Lecture 19: Jeffreys Prior and Bayesian Confidence I](https://learning.edx.org/course/course-v1:MITx+18.6501x+1T2024/block-v1:MITx+18.6501x+1T2024+type@sequential+block@u6s2_Bayes2)

At the end of this lecture, you will be able to do the following:

- Explain the important factors involved in choosing a prior distribution.
- Distinguish between **conjugate priors** and **non-conjugate priors** .
- Compute **Jeffreys Prior** and understand the intuition behind its significance.
- Apply **Bayesian statistics** in simple estimation and inference problems.
- **Compare and contrast** results from **Bayesian** and **frequentist** statistical methods.

## **19.1. Jeffreys Prior**

**Jeffreys Prior** is an attempt to incorporate frequentist ideas of likelihood in the Bayesian framework, as well as an example of a *non-informative prior*. This prior depends on the statistical model used for the observation data and the likelihood function. Mathematically, it is the prior \pi _{J}(\theta ) that satisfies

| \pi _{J}(\theta ) \propto \sqrt{\text {det} I(\theta )}, |  |
| --- | --- |

where I(\theta ) is the **Fisher Information matrix** of the statistical model associated with X_1, \ldots, X_ n in the frequentist approach, provided that it exists.

In the one-variable case, Jeffreys prior reduces to

| \pi _{J}(\theta ) \propto \sqrt{I(\theta )}. |  |
| --- | --- |

The Fisher information matrix I(\theta ) here is treated as a *linear transformation* matrix which maps one coordinate space to another (the logic behind such a mapping would be explained soon). In linear transformation terms, taking the determinant represents the ratio of volumes of corresponding spaces between coordinate system, which explains the intuition behind the use of \text {det} \ I(\theta ).

### Fisher Information and MLE Interpretation

Let our parameter of interest be \theta. As computing Jeffreys prior makes use of the Fisher information I(\theta ), it is somehow related to the frequentist MLE approach (which has variance I(\theta )^{-1}). This yields interpretations of Jeffreys prior in terms of frequentist notions of estimation, uncertainty, and information.

For each statement, fill in the blank with the appropriate choice (more / less), then choose the option that represents your answers in order.

1. The Jeffreys prior gives more weight to values of \theta whose MLE estimate has **less** uncertainty.
2. As a result, the Jeffreys prior yields more weight to values of \theta where the data has **more** information towards deciding the parameter.
3. The Fisher information can be taken as a proxy for how much, at a particular parameter value \theta, would equivalent shifts to the parameter influence the data. Thus, Jeffreys prior gives more weight to regions where the potential outcomes are **more** sensitive to slight changes in \theta.

### Area Interpretation of Jeffreys Prior

We start with a fixed one-parameter statistical model where we use the MLE as our estimate, and consider the case where the number of samples n gets large. For each potential estimate \theta, we construct using the asymptotic MLE variance the 95\% confidence interval X(\theta ) centered at \theta. Then, we consider the area over the interval X(\theta ) under the curve based on the Jeffreys prior. This area i**s the same regardless of \theta**.

## **19.2. Reparametrization Invariance: Intuition**

The lecture clip covered the **reparametrization invariance** property of Jeffreys prior. It states that if \eta is a reparametrization of \theta (i.e. \eta = \phi (\theta )) for some one-to-one map \phi), then the pdf \tilde{\pi }(\cdot ) of \eta satisfies

| \tilde{\pi }(\eta ) \propto \sqrt{\text {det} \tilde{I}(\eta )}. |  |
| --- | --- |

We examine the Jeffreys prior further. In the (typical) case where we have a single parameter, \sqrt{\text {det} \tilde{I}(\theta )} reduces to \sqrt{\tilde{I}(\theta )}. The Fisher information determines both the MLE asymptotic variance and Jeffreys prior, and as you've seen earlier is a measure of how *informative* the prior is towards the data. It in fact measures the how detectable marginal movements of \theta are based on the observations.

This motivates the use of Jeffreys prior. The main motivation for using such a prior is because certain parametrizations may compress meaningful differences in \theta into a small interval, whilst yielding large room for less impactful differences. In this case, a naive approach of using the uniform distribution would give an undue large weight to areas where modifying \theta will not change the outcome much. Jeffreys prior directly adjusts for this through the Fisher information which is closely tied to MLE uncertainty.

This adjustment based on a quantitiative measure of uncertainty facilitates accurate conversion between parametrizations. Scaling based on the square root of the Fisher information allows us to abstract from an artificial view imposed by a particular parametrization into a universal measuring stick of parameter impact. The distribution given by Jeffreys prior is based on this universal measure, independent of our parametrization. As a result, regardless of the parametrization, Jeffreys prior would give the same distribution.

Now, it remains to explain why exactly the *square root* of the Fisher information was chosen. Recall that the asymptotic variance of the MLE is I(\theta )^{-1}. Then the uncertainty, in the units of \theta, is measured through the asymptotic standard deviation, which is I(\theta )^{-\frac{1}{2}}. In the multidimensional case, the distribution of the MLE approaches a multivariate Gaussian, where we have to take the square root of the asymptotic variance matrix in order to obtain an expression that's in the same units of the parameter vector and thus quantifies uncertainty accordingly.

### Reparametrization Invariance: Mechanics

Suppose a student claims that the reparametrization invariance principle allows us to do the following.

“Suppose that we have the Jeffreys prior for a statistical model using parameter \theta, and we want to convert to parameter \eta =\phi (\theta ), where \phi is an invertible function. Then we could simply substitute every occurrence of \theta in the prior pdf with \phi ^{-1}(\eta ) instead, and this would give us Jeffreys prior with parameter \eta."

Is the above approach correct? If not, what is/are the error(s)?

- [ ]  The above approach is correct and would give us the correct Jeffreys prior with \eta as parameter.
- [ ]  The above approach is incorrect as we are supposed to use \phi (\eta ) instead of \phi ^{-1}(\eta ).
- [ ]  The above approach is incorrect because the reparametrization invariance principle states that the Jeffreys prior is identical regardless of parameterization.
- [ ]  The above approach is incorrect because we have to also multiply by a factor of \frac{d \theta }{d \eta } = \frac{1}{\phi '(\theta )} to obtain the correct Jeffreys prior.
- [ ]  The above approach is incorrect because the reparametrization invariance principle does not allow us to convert between parametrizations that have different Fisher information functions.