# Lecture 2. Conditioning and Bayes' rule

* Conditional probability

  * $\mathbf{P}(A|B) = \frac{\mathbf{P}(A \cap B)}{\mathbf{P}(B)} $, defined only when $ \mathbf{P}(B) > 0$.

  * Properties: 

    $\mathbf{P}(A|B) \geq 0 $, assuming $ \mathbf{P}(B) > 0.$

    If $A \cap C = \empty$, then $\mathbf{P}(A \cup C | B) = \mathbf{P}(A | B) + \mathbf{P}(C | B)$.

* Three important tools

  * Multiplication rule

    $\mathbf{P}(A \cap B) = \mathbf{P}(B) \mathbf{P}(A|B) = \mathbf{P}(A)\mathbf{P}(B|A).$

    $\mathbf{P}(A^c \cap B \cap C^c) = \mathbf{P}(A^c) \cdot \mathbf{P}(B|A^c) \cdot \mathbf{P}(C^c|A^c \cap B).$

    $\mathbf{P}(A_1 \cap A_2 \cap ... \cap A_n) = \mathbf{P}(A_1) \prod^n_{i=2} \mathbf{P}(A_i | A_1 \cap ... \cap A_{i-1}).$

  * Total probability theorem

    $\mathbf{P}(B) = \sum_i \mathbf{P}(A_i)\mathbf{P}(B|A_i)$, which is a weighted average of $\mathbf{P}(B|A_i)$. Note that $\sum_i \mathbf{P}(A_i) = 1$.

  * Bayes' rule ($\rightarrow$ inference)

    $\mathbf{P}(A_i | B) = \frac{\mathbf{P}(A_i \cap B)}{\mathbf{P}(B)} = \frac{\mathbf{P}(A_i) \mathbf{P}(B | A_i)}{\sum_j \mathbf{P}(A_j) \mathbf{P}(B|A_j)}.$

    Inference: 

    * initial beliefs $\mathbf{P}(A_i)$ on possible causes of an observed event $B$.

    * model of the world under each $A_i: \mathbf{P}(B | A_i)$.

      $A_i \xrightarrow{\text{model } \mathbf{P}(B|A_i)} B$

    * draw conclusions about causes

      $B \xrightarrow{\text{inference } \mathbf{P}(A_i | B)} A_i$

---

There are 1 selected exercise and 3 solved problems.

## Exercise 1 Total probability theorem

We have an infinite collection of biased coins, indexed by the positive integers. Coin $i$ has probability $2^{−i}$ of being selected. A flip of coin $i$ results in Heads with probability $3^{−i}$. We select a coin and flip it. What is the probability that the result is Heads?

**Solution**: 

Using the geometric sum formula $\sum _{i=1}^{\infty }\alpha ^ i =\frac{\alpha }{1-\alpha }$ when $|\alpha| < 1$. By the total probability theorem, for the case of infinitely many scenarios,
$$
\mathbf{P}(\text{Heads})=\sum _{i=1}^{\infty } \mathbf{P}(A_ i)\mathbf{P}(\text{Heads}\mid A_ i)=\sum _{i=1}^{\infty } 2^{-i}3^{-i} =\sum _{i=1}^{\infty } (1/6)^ i =\frac{1/6}{1-(1/6)}=\frac{1}{5}.
$$

## Problem 1 A chess tournament problem

**A chess tournament problem.** This year's Belmont chess champion is to be selected by the following procedure. Bo and Ci, the leading challengers, first play a two-game match. If one of them wins both games, he gets to play a two-game **second round** with Al, the current champion. Al retains his championship unless a second round is required and the challenger beats Al in both games. If Al wins the initial game of the second round, no more games are played.

Furthermore, we know the following:
∙ The probability that Bo will beat Ci in any particular game is 0.6.
∙ The probability that Al will beat Bo in any particular game is 0.5.
∙ The probability that Al will beat Ci in any particular game is 0.7.

Assume no tie games are possible and all games are independent.

\1. Determine the a priori probabilities that
(a) the second round will be required.
(b) Bo will win the first round.
(c) Al will retain his championship this year.

\2. Given that the second round is required, determine the conditional probabilities that
(a) Bo is the surviving challenger.
(b) Al retains his championship.

\3. Given that the second round was required and that it comprised only one game, what is the conditional probability that it was Bo who won the first round?

**Solution**: 

\1. 

a) $\mathbf{P}(\text{2nd Rnd Req}) = (0.6)^2 + (0.4)^2 = 0.52$

b) $\mathbf{P}(\text{Bo Wins 1st Rnd}) = (0.6)^2 = 0.36$

c) $\mathbf{P}(\text{Al Champ})\\ = 1 - \mathbf{P}(\text{Bo Champ}) - \mathbf{P}(\text{Ci Champ})\\ = 1 - (0.6)^2 \cdot (0.5)^2 - (0.4)^2 \cdot (0.3)^2\\ = 0.8956$

\2.

a) $\mathbf{P}(\text{Bo Challenger | 2nd Rnd Req}) = \frac{(0.6)^2}{0.52} = \frac{0.36}{0.52} = 0.6923$

b) $\mathbf{P}(\text{Al Champ | 2nd Rnd Req}) \\=\mathbf{P}(\text{Al Champ | Bo CHallenger, 2nd Rnd Req}) \cdot \mathbf{P}(\text{Bo Challenger| 2nd Rnd Req})\\ + \mathbf{P}(\text{Al Champ | Ci Challenger, 2nd Rnd Req}) \cdot \mathbf{P}(\text{Ci CHallenger| 2nd Rnd Req})\\=(1-(0.5)^2) \cdot 0.6923 + (1-(0.3)^2) \cdot 0.3077\\ = 0.7992$.

c) $\mathbf{P}(\text{Bo Challenger| \{(2nd Rnd Req)} \cap\text{(One Game)\}})\\ = \frac{(0.6)^2 \cdot (0.5)}{(0.6)^2 \cdot 0.5 + (0.4)^2 \cdot (0.7)}\\ = \frac{(0.6)^2 (0.5)}{0.2920}\\ = 0.6164$

## Problem 2 A coin tossing puzzle

A coin is tossed twice. Alice claims that the event of getting two Heads is at least as likely if we know that the first toss is Heads than if we know that at least one of the tosses is Heads. Is she right? Does it make a difference if the coin is fair or unfair? 

**Solution**: 

Let $A$ be the event that the first toss is a head and let $B$ be the event that the second toss is a head. We must compare the conditional probabilities $\mathbf{P}(A ∩ B | A)$ and $\mathbf{P}(A ∩ B | A ∪ B)$.

Since $\mathbf{P}(A \cup B) \geq \mathbf{P}(A)$, the conditional probability $\mathbf{P}(A ∩ B | A)$ is as least as large, regardless of whether the coin is fair or not.

## Problem 3 Oscar's lost dog in the forest

Oscar has lost his dog in either forest A (with probability $0.4$) or in forest B (with probability $0.6$).

If the dog is in forest A and Oscar spends a day searching for it in forest A, the conditional probability that he will find the dog that day is $0.25$. Similarly, if the dog is in forest B and Oscar spends a day looking for it there, he will find the dog that day with probability $0.15$.

The dog cannot go from one forest to the other. Oscar can search only in the daytime, and he can travel from one forest to the other only overnight.

The dog is alive during day $0$, when Oscar loses it, and during day $1$, when Oscar starts searching. It is alive during day $2$ with probability $2/3$. In general, for $n≥1$, if the dog is alive during day $n−1$, then the probability it is alive during day $n$ is $2/(n+1)$. The dog can only die overnight. Oscar stops searching as soon as he finds his dog, either alive or dead.

a) In which forest should Oscar look on the first day of the search to maximize the probability he finds his dog that day?

b) Oscar looked in forest A on the first day but didn't find his dog. What is the probability that the dog is in forest A?

c) Oscar flips a fair coin to determine where to look on the first day and finds the dog on the first day. What is the probability that he looked in forest A?

d) Oscar decides to look in forest A for the first two days. What is the probability that he finds his dog alive for the first time on the second day?

e) Oscar decides to look in forest A for the first two days. Given that he did not find his dog on the first day, find the probability that he does not find his dog dead on the second day.

f) Oscar finally finds his dog on the fourth day of the search. He looked in forest A for the first 3 days and in forest B on the fourth day. Given this information, what is the probability that he found his dog alive?

**Answer**: 

a) Forest A; b) $1/3$; c) $10/19$; d) $0.05$; e) $35/36$; f) $2/15$;

**Solution**: 
$$
\begin{aligned}
S_A &=  \text{event that Oscar searches for his dog in forest A}\\
S_B &= \text{event that Oscar searches for his dog in forest B}\\
A &=  \text{event that his dog is lost in forest A}\\
B &=  \text{event that his dog is lost in forest B}\\
F_i &= \text{event that Oscar finds his dog on day }i\\
L_i &= \text{event that his dog is alive on day }i
\end{aligned}
$$
a) Oscar has two choices represented by the following tree diagrams:

![oscar-dog1](../assets/images/oscar-dog1.jpg)

Comparing
$$
\mathbf{P}(F_1 \cap S_ A) = (0.4)(0.25) = 0.1\\
\mathbf{P}(F_1 \cap S_ B) = (0.6)(0.15) = 0.09\\
$$
Therefore, he should choose to search in forest A.

b) The desired probability is
$$
\mathbf{P}(A\mid S_ A \cap F^ c_1) = \frac{\mathbf{P}(A \cap S_ A \cap F^ c_1)}{\mathbf{P}(S_ A \cap F^ c_1)} = \frac{(0.4)(0.75)}{(0.4)(0.75) + (0.6)(1)} = \frac{1}{3}.
$$
c) we get the following diagram

![oscar-dog2](../assets/images/oscar-dog2.jpg)

The desired probability is
$$
\mathbf{P}(S_ A \mid F_1) = \frac{\mathbf{P}(S_ A \cap F_1)}{\mathbf{P}(F_1)} = \frac{(0.5)(0.4)(0.25)}{(0.5)(0.4)(0.25) + (0.5)(0.6)(0.15)} = \frac{10}{19}.
$$
d) The following diagram illustrates the sequence of possible events

![oscar-dog3](../assets/images/oscar-dog3.png)

The desired probability is 
$$
\mathbf{P}(A \cap F_1^ c \cap L_2 \cap F_2 \mid S_ A) = (0.4)(0.75)(2/3)(0.25) = 0.05.
$$
e) Using the diagram in d), the desired probability is 
$$
\begin{aligned}
&\mathbf{P}(\text{Oscar does not find dead dog on day 2} \mid F^ c_1 \cap S_ A)\\
&= 1 - \mathbf{P}(\text{Oscar does find dead dog on day 2} \mid F^ c_1 \cap S_ A)\\
&=1 - \frac{\mathbf{P}(S_ A \cap A \cap F_1^ c \cap L_2^ c \cap F_2)}{\mathbf{P}(F_1^ c \cap S_ A)}\\
&=1 - \frac{(0.4)(0.75)(1/3)(0.25)}{(0.4)(0.75)+(0.6)(1.0)}\\
&= \frac{35}{36}.
\end{aligned}
$$
f) We know that Oscar found his dog and we know it took 4 days. It doesn't matter, then, where he searched. We just want the probability the dog survived to day 4. This probability is 
$$
\mathbf{P}(L_4) = \left(\frac{2}{2+1}\right)\left(\frac{2}{3+1}\right)\left(\frac{2}{4+1}\right) = \frac{2}{15}.
$$