# Mathematical background

- **Sets**
    - Set is a collection of distinct elements
        - $\{a,b,c,d\}$ is finite set
        - $\mathbb{R}:$ real numbers is infinite set
        - $\Omega$  is universal set
        - $\empty$ is empty set, $\Omega^c=\empty$
- **De Morgan’s laws**
    - $(\cap_{n}S_n)^c=\cup_nS^c_n$
    - $(\cup_{n}S_n)^c=\cap_nS^c_n$
- **Geometric series**
    - $\sum_{i=0}^{\infty}\alpha^i=1+\alpha+\alpha^2+...=\frac{1}{1-\alpha} \quad |\alpha|<1$
- **The probability of the symmetric difference of 2 events**
    - $\mathbf{P}((A \cap B^c)\cup(A^c \cap B))=\mathbf{P}(A)+\mathbf{P}(B)-2\mathbf{P}(A \cap B)$
- **Bonferroni's inequality**
    - $\mathbf{P}(A_1 \cap A_2) \geq \mathbf{P}(A_1) + \mathbf{P}(A_2)-1$
- **Multinomial probabilities**
    - An urn contains balls of $r$ different colors. We draw $n$ balls, with different draws being independent. For any given draw, there is a probability $p_i$, $i=1,...,r$, of getting a ball of color $i$. Here, the $p_i$'s are nonnegative numbers that sum to 1.
    - Let $n_1,n_2,...,n_r$ be nonnegative integers that sum to $n$. What is the probability that we obtain exactly $n_i$ balls of color $i$, for each $i=1,2,...,r$?
    - $\mathbf{P}(\text{get type }(n_1,n_2,...,n_r))= \frac{n!}{n_1!n_2!...{n_r}!} p_1^{n_1}p_2^{n_2}...p_r^{n_r}$

[https://courses.edx.org/assets/courseware/v1/8307d1e4d8897a5b7fddd3f1806c5a0d/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_mathOverview-annotated.pdf](https://courses.edx.org/assets/courseware/v1/8307d1e4d8897a5b7fddd3f1806c5a0d/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_mathOverview-annotated.pdf)

- **Function**

[https://courses.edx.org/assets/courseware/v1/5b777c9948acf673ef815e452a988d8a/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U04-TH-Functions.pdf](https://courses.edx.org/assets/courseware/v1/5b777c9948acf673ef815e452a988d8a/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U04-TH-Functions.pdf)

- The variance of geometric

![](https://courses.edx.org/assets/courseware/v1/a6865793b86a17a00ae2d425a98d81c7/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U04-TH-Variance_of_geometric.png)

- **The inclusion-exclusion formula**
    
    $$
    \mathbf{P}\left(\bigcup _{k=1}^ nA_ k\right) = \sum _{i}\mathbf{P}(A_ i)-{\sum _{i_1<i_2} \mathbf{P}(A_{i_1}\cap A_{i_2})}+{\sum _{i_1<i_2<i_3}\mathbf{P}(A_{i_1}\cap A_{i_2}\cap A_{i_3})} -\cdots +(-1)^{n-1}\mathbf{P}\left(\bigcap _{k=1}^ nA_ k\right).
    $$
    
    [https://courses.edx.org/assets/courseware/v1/6ad917f24f20fc3a8e91364b7c41ddbd/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U04-TH-Inclusion_exclusion.pdf](https://courses.edx.org/assets/courseware/v1/6ad917f24f20fc3a8e91364b7c41ddbd/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U04-TH-Inclusion_exclusion.pdf)
    
- **Independence of random variables versus independence of events**

![](https://courses.edx.org/assets/courseware/v1/c778e40039bf4938daca277d6c4c6ab3/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_U04-TH-Indep-events-vs-rvs.png)