# Unit 3: Counting

> **Status: learner-authored study guide.** Use this page as a compact problem-solving companion; the course and OCW lecture links remain the primary sources.

[Course | edX](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__4_Counting)

[Lecture slides: clean](https://courses.edx.org/assets/courseware/v1/6247d54f01b8f50d4eb7c85e4549cdb0/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L04-clean-slides.pdf) · [annotated](https://courses.edx.org/assets/courseware/v1/70238703550d39dbf146b44896b92ae3/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L04-annotated-slides.pdf)

More information is available in [Section 1.6 of the course text](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/7).

## 1. The counting principle

If a procedure has m stages and stage j has n_j possible outcomes after the earlier choices are fixed, the total number of outcomes is the product n_1 n_2 ... n_m. The key question is whether the stages describe distinct choices without double-counting.

Use a tree or a table when the number of choices changes after each stage. For equally likely outcomes:

P(event) = number of favorable outcomes / number of possible outcomes.

This shortcut is valid only after the sample space has been defined and shown to be equiprobable.

## 2. Permutations and combinations

- Ordered selection of k distinct objects from n: n (n - 1) ... (n - k + 1) = n! / (n - k)!.
- Unordered selection of k distinct objects from n: choose(n, k) = n! / [k! (n - k)!].
- Arrangements with repeated types: n! / (n_1! n_2! ... n_r!).
- Distributing n identical objects into r labeled bins allows zero counts: choose(n + r - 1, r - 1).

The distinction is simple but decisive: if swapping two selected objects changes the outcome, order matters and combinations alone undercount.

## 3. Partitions and inclusion-exclusion

A partition of a sample space is a collection of disjoint events whose union is the whole space. Partitions make case-based counting auditable:

P(A) = sum_j P(A intersect B_j) when {B_j} is a partition.

For two events:

|A union B| = |A| + |B| - |A intersect B|.

The subtraction removes outcomes counted twice. For three or more events, alternate additions and subtractions of intersections. In practice, define the events first, then mark which overlaps are possible before applying the formula.

## 4. Binomial and multinomial patterns

For n independent binary trials with success probability p, the probability of exactly k successes is:

choose(n, k) p^k (1 - p)^(n - k).

The combination factor counts the positions of the successes. If there are r categories with probabilities p_1, ..., p_r and counts n_1, ..., n_r summing to n, the multinomial probability is:

n! / (n_1! ... n_r!) times product_j p_j^(n_j).

These formulas require a fixed number of trials, independence, and stable category probabilities. Sampling without replacement usually violates the binomial assumptions.

## 5. A reliable counting workflow

1. Describe one elementary outcome in words.
2. Decide whether order, repetition, and labels matter.
3. Choose a direct product, permutation, combination, partition, or complement argument.
4. Check whether outcomes are equally likely before converting counts into probabilities.
5. Test the result on a small case where enumeration is possible.

## Common traps

- Using combinations when the order of arrival or assignment matters.
- Treating dependent draws as independent.
- Forgetting that “at least one” is often easier through the complement.
- Counting the same arrangement multiple times because identical objects were labeled temporarily.
- Applying a favorable-over-total ratio to a non-uniform sample space.

Continue with [Unit 4: discrete random variables](Unit%204%20Discrete%20random%20variables%2041cf21b82aa44d9098005a109263cc64.md) to turn counts into probability mass functions and expectations.
