# Lecture 4. Counting

* Discrete uniform law

  Assuming $\Omega$ consists of $n$ equally likely elements, $A$ is a subset of $\Omega$, and $A$ consists of $k$ elements.
  $$
  \mathbf{P}(A) = {k \over n}
  $$

* Basic counting principle

  Assuming $r$ stages and $n_i$ choices at stage $i$. The number of choices is $n_1 \cdot n_2 ... n_r$.

* Applications

  * Permutations: Number of ways of ordering $n$ elements:

    $n \cdot (n-1) \cdot (n-2) ... 1 = n!$

  * Number of subsets of $\{1,...,n\}$:

    $\sum^n_{k=0} = {n \choose 0} + {n \choose 1} + ... +{n \choose n}=2^n$

  * Combinations:

    $ {n \choose k}$: number of $k$ element subsets of a given $n$ element set.

    ${n \choose k} = \frac{n!}{k!(n-k)!}= n(n-1)(n-2)...(n-k+1) \quad n = 0,1,2,...$

    ${n \choose n} = \frac{n!}{n! 0!} =1, \quad 0! = 1$

    ${n \choose 0} = \frac{n!}{0!n!} = 1$

  * Binomial probabilities:

    In the case of coin tossing,

    $\mathbf{P}(k \text{ head}) = {n \choose k}p^k (1-p)^{n-k}$, where ${n \choose k}$ is binomial coefficient.

  * Partitions:

    $n \geq 1$ distinct items; $r \geq 1$ persons; give $n_i$ items to person $i$. $n_1 + n_2 + ... + n_r = n$.

    Number of partition = $\frac{n!}{n_1!n_2! ...n_r!}$ (multinomial coefficient)
    
  * Multinomial probabilities
  
    Find $\mathbf{P}(n_1 \text{balls of color 1}, n_2 \text{balls of color 2, ..., } n_r \text{ balls of color r})$.
    $$
    \mathbf{P}(\text{get type} (n_1, n_2, ..., n_r)) = \frac{n!}{n_1!n_2!...n_r!} p_1^{n_1}p_2^{n_2}...p_r^{n_r}
    $$


* Example of card deck: 52-card deck, dealt ( fairly ) to 4 players. Find $\mathbf{P}$(each player gets and ace)

  * Number of outcomes: $\frac{52!}{13!13!13!13!}$

  * Outcome with one ace for each person: 

    * distribute the aces: $4\cdot3\cdot2\cdot1$
    * distribute the remaining 48 cards: $\frac{48!}{12!12!12!12!}$

  * Answer: 
    $$
    \frac{4\cdot3\cdot2\cdot\frac{48!}{12!12!12!12!}}{\frac{52!}{13!13!13!13!}}
    $$

  * Another way of thinking: 
    $$
    \frac{39}{51} \cdot \frac{26}{50} \cdot \frac{13}{49} = 0.105
    $$


---

There are 3 selected exercises and 3 solved problems.

## Exercise 1 Use counting to calculate probabilities

Given the set of letters {A, B, C, D, E}. How many five-letter strings can be made if we require that each letter appears exactly once and the letters A and B are next to each other, as either “AB" or “BA"? What is the probability of that? 

**Answer**: 48; 0.4

**Solution**: 

We first choose whether the order will be “AB" or “BA" (2 choices). We then choose the position of the first letter in “AB" or “BA". There are 4 choices, namely positions 1, 2, 3, or 4. We are left with three positions in which the letters C, D, and E can be placed, in any order. The number of ways that this can be done is the number of permutations of these three letters, namely, $3!=3⋅2⋅1=6$. Thus, the answer to this problem is $2⋅4⋅6=48$.

The sample space has $5!=120$ elements. Thus, the desired probability is $48/120=2/5=0.4$.

## Exercise 2 Counting committees

We start with a pool of $n$ people. A chaired committee consists of $k≥1$ members, out of whom one member is designated as the chairperson. The expression $k {n\choose k}$ can be interpreted as the number of possible chaired committees with $k$ members. This is because we have ${n \choose k}$ choices for the $k$ members, and once the members are chosen, there are then $k$ choices for the chairperson. Thus,
$$
c=\sum _{k=1}^ n k {n \choose k}
$$
is the total number of possible chaired committees of any size.

**Answer**: $n 2^{n-1}$

**Solution**: 

We first choose the chairperson, for which there are $n$ choices, and then choose an arbitrary subset of the remaining $n−1$ people, who will be the remaining committee members. For example, this arbitrary subset could be the empty set, which would mean that the committee is of size 1: only the chairperson. There are $2^{n−1}$ possible subsets of a set with $n−1$ elements, and so there are $2^{n−1}$ ways of choosing the remaining committee members. Thus, an alternative expression for the number of possible chaired committees of any size is $n2^{n−1}$.

## Exercise 3 Coin tossing

Find the probability that the $6$th toss out of a total of $10$ tosses is Heads, given that there are exactly $2$ Heads out of the $10$ tosses. As in the preceding segment, continue to assume that all coin tosses are independent and that each coin toss has the same fixed probability of Heads.

**Answer**:  $1/5$

**Solution**: 
$$
\mathbf{P} = \frac{\text{ the 6th toss out of a total of 10 tosses is Heads}}{\text{there are 2 Heads out of the 10 tosses}} = \frac{9}{{10 \choose 2}} = 0.2
$$

## Problem 1 The birthday problem

Consider $n$ people who are attending a party. We assume that every person has an equal probability of being born on any day during the year, independently of everyone else, and ignore the additional complication presented by leap years (i.e., nobody is born on February 29). What is the probability that each person has a distinct birthday?

**Answer**: 
$$
\mathbf{P}(\text{no two birthdays coincide}) = \frac{365 \cdot 364 ... (365 - n + 1)}{365^n}
$$

## Problem 2 Rooks on a chessboard

Eight rooks are placed in distinct squares of an $8×8$ chessboard, with all possible placements being equally likely. Find the probability that all the rooks are safe from one another, i.e., that there is no row or column with more than one rook.

**Answer**: 
$$
\frac{64 \cdot 49 \cdot 36 \cdot 25 \cdot 16 \cdot 9 \cdot 4}{64!/56!}
$$
**Solution**: 

The numerator: divide the chessboard into 8 rows, each with 8 cells. Every time we assign one rook to one cell on the chessboard and do not consider the row with that cell any more until completion.

The denominator: $64 \cdot 63 \cdot 62 ... 56$, the number of different chessboard with 8 rooks.

## Problem 3 Hypergeometric probabilities

An urn contains $n$ balls, out of which exactly $m$ are red. We select $k$ of the balls at random, without replacement (i.e., selected balls are not put back into the urn before the next selection). What is the probability that $i$ of the selected balls are red?

**Answer**: 
$$
\frac{{m \choose i} {{n-m}\choose {k-i}}}{{n \choose k}}
$$
**Solution**: 

The denominator: ${n \choose k}$ choose $k$ balls from $n$ balls.

The numerator: ${m \choose i }$ choose $i$ red balls from $m$ red balls, ${{n-m}\choose {k-i}}$ other chosen balls are not red balls chosen from all non-red balls.

