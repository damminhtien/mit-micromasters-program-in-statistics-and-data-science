# Lecture 6: Visualization of High-Dimensional Data

# **I. Expectation** and **covariance matrix** of a r.v.

## 1. Vector Outer Product I

To find the shape of the matrix  $\mathbf{x} \mathbf{y}^T$, let's first explicitly write down the vectors and their outer product.

Given: $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \in \mathbb{R}^2$, $\mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} \in \mathbb{R}^3$ . The outer product $\mathbf{x} \mathbf{y}^T$ is computed as follows: $\mathbf{x} \mathbf{y}^T = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \begin{pmatrix} y_1 & y_2 & y_3 \end{pmatrix} = \begin{pmatrix} x_1 y_1 & x_1 y_2 & x_1 y_3 \\ x_2 y_1 & x_2 y_2 & x_2 y_3 \end{pmatrix}$ 

So, the shape of the matrix $\mathbf{x} \mathbf{y}^T$ is $2 \times 3$.

## 2. Review Vector Outer Product II

Let's compute the outer product of the vector $\mathbf{x}$ with itself.

Given: $\mathbf{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$

The outer product $\mathbf{x} \mathbf{x}^T$ is computed as:

$$
\mathbf{x} \mathbf{x}^T = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 & 1 \cdot 2 & 1 \cdot 3 \\ 2 \cdot 1 & 2 \cdot 2 & 2 \cdot 3 \\ 3 \cdot 1 & 3 \cdot 2 & 3 \cdot 3 \end{pmatrix} 
$$

$$
\mathbf{x} \mathbf{x}^T = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}
$$

Now, let's identify the specific entries requested:

$(\mathbf{x} \mathbf{x}^T)_{11} = 1$, $(\mathbf{x} \mathbf{x}^T)_{21} = 2$ , $(\mathbf{x} \mathbf{x}^T)_{23} = 6$ , $(\mathbf{x} \mathbf{x}^T)_{12} = 2$ 

Finally, to address the general question:

In general, for any vector $\mathbf{x} \in \mathbb{R}^n$ , the matrix $\mathbf{x} \mathbf{x}^T$ is symmetric. This is because $(\mathbf{x} \mathbf{x}^T)_{ij} = x_i x_j$ , 

Since $x_i x_j = x_j x_i$, we have $(\mathbf{x} \mathbf{x}^T)_{ij} = (\mathbf{x} \mathbf{x}^T)_{ji}$.

**Therefore, the matrix $\mathbf{x} \mathbf{x}^T$ is symmetric.**

## 3. Expectation of a Random Vector

### Part 1

Given a random vector \(\mathbf{X} \in \mathbb{R}^n\), the expected value \(\mathbf{E}[\mathbf{X}]\) is:

- **A vector in \(\mathbb{R}^n\)**.

This is because the expected value (mean) of a random vector is computed by taking the expected value of each component of the vector, resulting in another vector of the same dimension.

### Part 2

Given the random vector \(\mathbf{X} \in \mathbb{R}^3\) which follows a Gaussian distribution:

\[
\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}, \Sigma) = \mathcal{N}\left( \begin{pmatrix} -10 \\ 0 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 & 2 & 0 \\ 2 & 2 & 1 \\ 0 & 1 & 1 \end{pmatrix} \right)
\]

where \(\mathbf{\mu}\) is the mean and \(\Sigma\) is the covariance matrix of \(\mathbf{X}\).

The expected value \(\mathbf{E}[\mathbf{X}]\) is the mean vector \(\mathbf{\mu}\).

So,

\[
\mathbf{E}[\mathbf{X}] = \begin{pmatrix} -10 \\ 0 \\ 2 \end{pmatrix}
\]

Thus, \(\mathbf{E}[\mathbf{X}]\) is:

\[
\mathbf{E}[\mathbf{X}] = [-10, 0, 2]
\]

To summarize:

- \(\mathbf{E}[\mathbf{X}]\) is a vector in \(\mathbb{R}^n\).
- For the given Gaussian random vector \(\mathbf{X}\), \(\mathbf{E}[\mathbf{X}]\) is \([-10, 0, 2]\).

## 4. Variance and Covariance of Random Variable

### Part 1: Variance of $X$

Given the variance of $X$: $\textsf{Var}(X) = \mathbf{E}[X^2] - (\mathbf{E}[X])^2$ 

We also have the equivalent expression: $\textsf{Var}(X) = \mathbf{E}[(X - A)^2]$ 

To find the constant \(A\), we can expand the expression:

$$
\mathbf{E}[(X - A)^2] = \mathbf{E}[X^2 - 2AX + A^2] = \mathbf{E}[X^2] - 2A \mathbf{E}[X] + A^2 
$$

For this to be equal to \(\textsf{Var}(X)\), we need:

\[
\mathbf{E}[X^2] - 2A \mathbf{E}[X] + A^2 = \mathbf{E}[X^2] - (\mathbf{E}[X])^2
\]

By matching terms, we get:

\[
-2A \mathbf{E}[X] + A^2 = - (\mathbf{E}[X])^2
\]

Rearranging terms:

\[
A^2 - 2A \mathbf{E}[X] + (\mathbf{E}[X])^2 = 0
\]

This is a quadratic equation in \(A\), which simplifies to:

\[
(A - \mathbf{E}[X])^2 = 0
\]

Thus:

\[
A = \mathbf{E}[X]
\]

So the answer to the first part is:

**a) \(\mathbf{E}[X]\)**

### Part 2: Covariance of \(X\) and \(Y\)

Given the covariance of \(X\) and \(Y\):

\[
\textsf{Cov}(X, Y) = \mathbf{E}[XY] - \mathbf{E}[X] \mathbf{E}[Y]
\]

We also have the equivalent expression:

\[
\textsf{Cov}(X, Y) = \mathbf{E}[(X - B)(Y - C)]
\]

To find the constants \(B\) and \(C\), we expand the expression:

\[
\mathbf{E}[(X - B)(Y - C)] = \mathbf{E}[XY - XC - YB + BC] = \mathbf{E}[XY] - C \mathbf{E}[X] - B \mathbf{E}[Y] + BC
\]

For this to be equal to \(\textsf{Cov}(X, Y)\), we need:

\[
\mathbf{E}[XY] - C \mathbf{E}[X] - B \mathbf{E}[Y] + BC = \mathbf{E}[XY] - \mathbf{E}[X] \mathbf{E}[Y]
\]

By matching terms, we get:

\[
-C \mathbf{E}[X] - B \mathbf{E}[Y] + BC = - \mathbf{E}[X] \mathbf{E}[Y]
\]

To satisfy this equation, we set:

\[
B = \mathbf{E}[X] \quad \text{and} \quad C = \mathbf{E}[Y]
\]

So the answer to the second part is:

**a) \(B = \mathbf{E}[X], C = \mathbf{E}[Y]\)**

## **5. Covariance Matrix of Random Vectors**

### Part 1: Finding \(A\) for the Covariance Matrix

Given the covariance matrix of \(\mathbf{X}\) defined as:

\[
\Sigma = \mathbf{E}[ \mathbf{X} \mathbf{X}^T ] - \mathbf{E}[ \mathbf{X}] \mathbf{E}[ \mathbf{X}]^T,
\]

it can also be expressed as:

\[
\Sigma = \mathbf{E}\left[ (\mathbf{X} - A) (\mathbf{X} - A)^T \right]
\]

To find the matrix \(A\), we expand the expression:

\[
\mathbf{E}\left[ (\mathbf{X} - A) (\mathbf{X} - A)^T \right] = \mathbf{E}\left[ \mathbf{X} \mathbf{X}^T - \mathbf{X} A^T - A \mathbf{X}^T + A A^T \right]
\]

Taking the expectation:

\[
\mathbf{E}[ (\mathbf{X} - A) (\mathbf{X} - A)^T ] = \mathbf{E}[ \mathbf{X} \mathbf{X}^T ] - \mathbf{E}[ \mathbf{X} ] A^T - A \mathbf{E}[ \mathbf{X}^T ] + A A^T
\]

For this to equal \(\Sigma\), we need:

\[
\mathbf{E}[ \mathbf{X} \mathbf{X}^T ] - \mathbf{E}[ \mathbf{X} ] A^T - A \mathbf{E}[ \mathbf{X}^T ] + A A^T = \mathbf{E}[ \mathbf{X} \mathbf{X}^T ] - \mathbf{E}[ \mathbf{X} ] \mathbf{E}[ \mathbf{X}]^T
\]

By matching terms, we see that:

\[

- \mathbf{E}[ \mathbf{X} ] A^T - A \mathbf{E}[ \mathbf{X}^T ] + A A^T = - \mathbf{E}[ \mathbf{X} ] \mathbf{E}[ \mathbf{X}]^T
\]

This equation holds if:

\[
A = \mathbf{E}[ \mathbf{X}]
\]

So the correct answer is:

**a) \(\mathbf{E}[ \mathbf{X}]\)**

### Part 2: Understanding \(\Sigma_{ij}\)

The covariance matrix element \(\Sigma_{ij}\) can be represented in several equivalent forms. Let's analyze the given options:

Given:

\[
\Sigma = \mathbf{E}[ \mathbf{X} \mathbf{X}^T ] - \mathbf{E}[ \mathbf{X}] \mathbf{E}[ \mathbf{X}]^T
\]

Therefore, the element \(\Sigma_{ij}\) is:

1. **a) \(\mathbf{E}[\mathbf{X}_i \mathbf{X}_j]\)**
    
    This term alone represents the expectation of the product of the \(i\)-th and \(j\)-th components of \(\mathbf{X}\), but it does not account for subtracting the mean product. So this option is not entirely correct by itself.
    
2. **b) \(\mathbf{E}[\mathbf{X}_i] \mathbf{E}[\mathbf{X}_j]\)**
    
    This term alone represents the product of the means of the \(i\)-th and \(j\)-th components of \(\mathbf{X}\),
    

but it does not account for the expectation of the product. So this option is also not correct by itself.

1. **c) \((\mathbf{E}[ \mathbf{X} \mathbf{X}^T])*{ij} - (\mathbf{E}[\mathbf{X}] \mathbf{E}[\mathbf{X}]^T)*{ij}\)**
    
    This option directly represents the element \(\Sigma_{ij}\) in the covariance matrix. It is correct.
    
2. **d) \(\mathbf{E}[ \mathbf{X}_i \mathbf{X}_j] - \mathbf{E}[\mathbf{X}]_i \mathbf{E}[\mathbf{X}]_j\)**
    
    This option also correctly represents the element \(\Sigma_{ij}\). It shows the expectation of the product minus the product of the expectations, which is another way to express the covariance element.
    
3. **e) \((\mathbf{E}[\mathbf{X}_i \mathbf{X}_j])^2\)**
    
    This option represents the square of the expectation of the product, which is not related to the covariance matrix element. This option is incorrect.
    
4. **f) \(\textsf{Cov}(\mathbf{X}_i, \mathbf{X}_j)\)**
    
    This option correctly represents the covariance between the \(i\)-th and \(j\)-th components of \(\mathbf{X}\). It is correct.
    

To summarize:

- The correct answers for \(\Sigma_{ij}\) are:
    
    **c) \((\mathbf{E}[ \mathbf{X} \mathbf{X}^T])*{ij} - (\mathbf{E}[\mathbf{X}] \mathbf{E}[\mathbf{X}]^T)*{ij}\)**
    
    **d) \(\mathbf{E}[ \mathbf{X}_i \mathbf{X}_j] - \mathbf{E}[\mathbf{X}]_i \mathbf{E}[\mathbf{X}]_j\)**
    
    **f) \(\textsf{Cov}(\mathbf{X}_i, \mathbf{X}_j)\)**
    

# **II. Empirical Mean and Covariance Matrix of a Vector Data Set**

## 1. Compute the Vector Sample Mean

To compute the sample mean (empirical mean) \(\overline{\mathbf{X}}\) of the given data set, we sum the vectors and then divide by the number of vectors.

Given data vectors:

\[
\mathbf{X}^{(1)} = \begin{pmatrix} 8 \\ 4 \\ 7 \end{pmatrix}, \quad \mathbf{X}^{(2)} = \begin{pmatrix} 2 \\ 8 \\ 1 \end{pmatrix}, \quad \mathbf{X}^{(3)} = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{X}^{(4)} = \begin{pmatrix} 9 \\ 7 \\ 4 \end{pmatrix}
\]

The sample mean \(\overline{\mathbf{X}}\) is calculated as:

\[
\overline{\mathbf{X}} = \frac{1}{4} \left( \mathbf{X}^{(1)} + \mathbf{X}^{(2)} + \mathbf{X}^{(3)} + \mathbf{X}^{(4)} \right)
\]

First, sum the vectors:

\[
\mathbf{X}^{(1)} + \mathbf{X}^{(2)} + \mathbf{X}^{(3)} + \mathbf{X}^{(4)} = \begin{pmatrix} 8 \\ 4 \\ 7 \end{pmatrix} + \begin{pmatrix} 2 \\ 8 \\ 1 \end{pmatrix} + \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 9 \\ 7 \\ 4 \end{pmatrix}
\]

Summing each component:

\[
\begin{pmatrix} 8 + 2 + 3 + 9 \\ 4 + 8 + 1 + 7 \\ 7 + 1 + 1 + 4 \end{pmatrix} = \begin{pmatrix} 22 \\ 20 \\ 13 \end{pmatrix}
\]

Now, divide by the number of vectors (4):

\[
\overline{\mathbf{X}} = \frac{1}{4} \begin{pmatrix} 22 \\ 20 \\ 13 \end{pmatrix} = \begin{pmatrix} \frac{22}{4} \\ \frac{20}{4} \\ \frac{13}{4} \end{pmatrix} = \begin{pmatrix} 5.5 \\ 5 \\ 3.25 \end{pmatrix}
\]

So, the sample mean \(\overline{\mathbf{X}}\) is:

$$
\overline{\mathbf{X}} = [5.5, 5, 3.25]
$$

## 2. **A Formula for the Vector Mean**

To find the matrix $\mathbf{A}$ in the expression: $\frac{1}{n} \sum_{i=1}^n \mathbf{X}^{(i)} = \mathbf{A} \mathbf{1}$ we need to relate this to the given matrix $\mathbb{X}$.

Given $\mathbb{X}$:

$$
\mathbb{X} = \begin{pmatrix} \longleftarrow & \left(\mathbf{X}^{(1)}\right)^T & \longrightarrow \\ \longleftarrow & \left(\mathbf{X}^{(2)}\right)^T & \longleftrightarrow \\ \vdots & \vdots & \vdots \\ \longleftarrow & \left(\mathbf{X}^{(n)}\right)^T & \longleftrightarrow \end{pmatrix} 
$$

Since $\mathbf{X}^{(i)}$ are column vectors, the matrix $\mathbb{X}$ has the form:

$$
\mathbb{X} = \begin{pmatrix} \mathbf{X}^{(1)} & \mathbf{X}^{(2)} & \cdots & \mathbf{X}^{(n)} \end{pmatrix}^T 
$$

To find the empirical mean, we average the vectors $\mathbf{X}^{(i)}$: $\frac{1}{n} \sum_{i=1}^n \mathbf{X}^{(i)}$

The sum of the vectors can be written in matrix form as $\mathbb{X}^T \mathbf{1}$, where $\mathbf{1}$ is an $n \times 1$ vector of ones:

$$
\mathbb{X}^T \mathbf{1} = \begin{pmatrix} \mathbf{X}^{(1)} & \mathbf{X}^{(2)} & \cdots & \mathbf{X}^{(n)} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{pmatrix} 
$$

This matrix multiplication results in a vector where each element is the sum of the corresponding elements of the vectors $\mathbf{X}^{(i)}$. To obtain the mean, we divide by $n$: $\frac{1}{n} \mathbb{X}^T \mathbf{1}$ 

So, the empirical mean can be written as: $\mathbf{A} \mathbf{1} = \frac{1}{n} \mathbb{X}^T \mathbf{1}$

Comparing this with the form $\mathbf{A} \mathbf{1}$, we identify $\mathbf{A}$ as: $\mathbf{A} = \frac{1}{n} \mathbb{X}^T$ 

Therefore, the matrix $\mathbf{A}$ is: $\mathbf{A} = \frac{1}{n} \text{trans}(X)$

## **3. The Sample Covariance for a Data Set of Vectors**

To compute the empirical covariance matrix \(\mathbf{S}\) for the given data set, we need to follow these steps:

1. Compute the empirical mean \(\overline{\mathbf{X}}\).
2. Compute the sum of the outer products of each vector with itself.
3. Subtract the outer product of the empirical mean with itself from the result obtained in step 2.

Given the data set:

\[
\mathbf{X}^{(1)} = \begin{pmatrix} 8 \\ 4 \\ 7 \end{pmatrix}, \quad \mathbf{X}^{(2)} = \begin{pmatrix} 2 \\ 8 \\ 1 \end{pmatrix}, \quad \mathbf{X}^{(3)} = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{X}^{(4)} = \begin{pmatrix} 9 \\ 7 \\ 4 \end{pmatrix}
\]

The empirical mean \(\overline{\mathbf{X}}\) is:

\[
\overline{\mathbf{X}} = \frac{1}{4} \left( \mathbf{X}^{(1)} + \mathbf{X}^{(2)} + \mathbf{X}^{(3)} + \mathbf{X}^{(4)} \right) = \frac{1}{4} \begin{pmatrix} 8+2+3+9 \\ 4+8+1+7 \\ 7+1+1+4 \end{pmatrix} = \frac{1}{4} \begin{pmatrix} 22 \\ 20 \\ 13 \end{pmatrix} = \begin{pmatrix} 5.5 \\ 5 \\ 3.25 \end{pmatrix}
\]

Now, we need to compute the empirical covariance matrix \(\mathbf{S}\):

\[
\mathbf{S} = \frac{1}{4} \sum_{i=1}^{4} \left(\mathbf{X}^{(i)} (\mathbf{X}^{(i)})^T \right) - \overline{\mathbf{X}} \overline{\mathbf{X}}^T
\]

First, calculate each outer product \(\mathbf{X}^{(i)} (\mathbf{X}^{(i)})^T\):

\[
\mathbf{X}^{(1)} (\mathbf{X}^{(1)})^T = \begin{pmatrix} 8 \\ 4 \\ 7 \end{pmatrix} \begin{pmatrix} 8 & 4 & 7 \end{pmatrix} = \begin{pmatrix} 64 & 32 & 56 \\ 32 & 16 & 28 \\ 56 & 28 & 49 \end{pmatrix}
\]

\[
\mathbf{X}^{(2)} (\mathbf{X}^{(2)})^T = \begin{pmatrix} 2 \\ 8 \\ 1 \end{pmatrix} \begin{pmatrix} 2 & 8 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 16 & 2 \\ 16 & 64 & 8 \\ 2 & 8 & 1 \end{pmatrix}
\]

\[
\mathbf{X}^{(3)} (\mathbf{X}^{(3)})^T = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} \begin{pmatrix} 3 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 9 & 3 & 3 \\ 3 & 1 & 1 \\ 3 & 1 & 1 \end{pmatrix}
\]

\[
\mathbf{X}^{(4)} (\mathbf{X}^{(4)})^T = \begin{pmatrix} 9 \\ 7 \\ 4 \end{pmatrix} \begin{pmatrix} 9 & 7 & 4 \end{pmatrix} = \begin{pmatrix} 81 & 63 & 36 \\ 63 & 49 & 28 \\ 36 & 28 & 16 \end{pmatrix}
\]

Summing these outer products:

\[
\sum_{i=1}^{4} \mathbf{X}^{(i)} (\mathbf{X}^{(i)})^T = \begin{pmatrix} 64 & 32 & 56 \\ 32 & 16 & 28 \\ 56 & 28 & 49 \end{pmatrix} + \begin{pmatrix} 4 & 16 & 2 \\ 16 & 64 & 8 \\ 2 & 8 & 1 \end{pmatrix} + \begin{pmatrix} 9 & 3 & 3 \\ 3 & 1 & 1 \\ 3 & 1 & 1 \end{pmatrix} + \begin{pmatrix} 81 & 63 & 36 \\ 63 & 49 & 28 \\ 36 & 28 & 16 \end{pmatrix}
\]

\[
= \begin{pmatrix} 158 & 114 & 97 \\ 114 & 130 & 65 \\ 97 & 65 & 67 \end{pmatrix}
\]

Now, divide by \(n = 4\):

\[
\frac{1}{4} \sum_{i=1}^{4} \mathbf{X}^{(i)} (\mathbf{X}^{(i)})^T = \begin{pmatrix} 39.5 & 28.5 & 24.25 \\ 28.5 & 32.5 & 16.25 \\ 24.25 & 16.25 & 16.75 \end{pmatrix}
\]

Next, calculate \(\overline{\mathbf{X}} \overline{\mathbf{X}}^T\):

\[
\overline{\mathbf{X}} \overline{\mathbf{X}}^T = \begin{pmatrix} 5.5 \\ 5 \\ 3.25 \end{pmatrix} \begin{pmatrix} 5.5 & 5 & 3.25 \end{pmatrix} = \begin{pmatrix} 30.25 & 27.5 & 17.875 \\ 27.5 & 25 & 16.25 \\ 17.875 & 16.25 & 10.5625 \end{pmatrix}
\]

Finally, subtract the outer product of the mean from the scaled sum of outer products:

\[
\mathbf{S} = \begin{pmatrix} 39.5 & 28.5 & 24.25 \\ 28.5 & 32.5 & 16.25 \\ 24.25 & 16.25 & 16.75 \end{pmatrix} - \begin{pmatrix} 30.25 & 27.5 & 17.875 \\ 27.5 & 25 & 16.25 \\ 17.875 & 16.25 & 10.5625 \end{pmatrix}
\]

\[
= \begin{pmatrix} 9.25 & 1 & 6.375 \\ 1 & 7.5 & 0 \\ 6.375 & 0 & 6.1875 \end{pmatrix}
\]

Thus, the covariance matrix \(\mathbf{S}\) has the dimensions \(3 \times 3\), and the specific entries are:

\[
\mathbf{S}_{11} = 9.25
\]

\[
\mathbf{S}_{21} = 1
\]

\[
\mathbf{S}_{32} = 0
\]

To summarize:

- Dimension of \(\mathbf{S}\): \(3 \times 3\)
- \(\mathbf{S}_{11} = 9.25\)
- \(\mathbf{S}_{21} = 1\)
- \(\mathbf{S}_{32} = 0\)

## 4. **Formula for the Empirical Covariance Matrix**

Let \mathbf{x} denote a 3 \times 1 column vector and let \mathbf{1} denote the 3 \times 1 column vector with all entries equal to 1. Suppose that the entries of \mathbf{x} sum to 0. That is,

| \mathbf{x}_1 + \mathbf{x}_2 + \mathbf{x}_3 = 0. |  |
| --- | --- |

What is (\mathbf{1} \mathbf{1}^ T) \mathbf{x}?

To find the correct formula for the empirical covariance matrix $\mathbf{S}$ using the given data matrix $\mathbb{X}$, we need to relate the formula:

$$
\mathbf{S} = \frac{1}{n} \sum_{i=1}^n \left(\mathbf{X}^{(i)} (\mathbf{X}^{(i)})^T\right) - \overline{\mathbf{X}} \overline{\mathbf{X}}^T 
$$

to a matrix form involving $\mathbb{X}$.

Step-by-Step Analysis:

1. **Data Matrix $\mathbb{X}$:**
    
    $$
    \mathbb{X} = \begin{pmatrix}
    \leftarrow & \left(\mathbf{X}^{(1)}\right)^T & \rightarrow \\
    \leftarrow & \left(\mathbf{X}^{(2)}\right)^T & \rightarrow \\
    \vdots & \vdots & \vdots \\
    \leftarrow & \left(\mathbf{X}^{(n)}\right)^T & \rightarrow
    \end{pmatrix} 
    $$
    
    Here, each row of $\mathbb{X}$ corresponds to a transpose of the sample vectors $\mathbf{X}^{(i)}$.
    
2. **Empirical Mean:**
    
    $$
    \overline{\mathbf{X}} = \frac{1}{n} \sum_{i=1}^n \mathbf{X}^{(i)} 
    $$
    
    We can express the empirical mean as:
    
    $$
    \overline{\mathbf{X}} = \frac{1}{n} \mathbb{X}^T \mathbf{1}
    $$
    
    where $\mathbf{1}$ is an $n \times 1$ vector of ones.
    
3. **Outer Product Form:**
    
    The term $\frac{1}{n} \sum_{i=1}^n \left(\mathbf{X}^{(i)} (\mathbf{X}^{(i)})^T\right)$ can be represented as: $\frac{1}{n} \mathbb{X}^T \mathbb{X}$ 
    
4. **Mean Outer Product:**
    
    The term $\overline{\mathbf{X}} \overline{\mathbf{X}}^T$ can be written as:
    
    $$
    \overline{\mathbf{X}} \overline{\mathbf{X}}^T = \left(\frac{1}{n} \mathbb{X}^T \mathbf{1}\right) \left(\frac{1}{n} \mathbf{1}^T \mathbb{X}\right) = \frac{1}{n^2} \mathbb{X}^T \mathbf{1} \mathbf{1}^T \mathbb{X}
    $$
    
5. **Combining the Terms:**
    
    Combining these, the empirical covariance matrix is:
    
    $$
    \mathbf{S} = \frac{1}{n} \mathbb{X}^T \mathbb{X} - \frac{1}{n^2} \mathbb{X}^T \mathbf{1} \mathbf{1}^T \mathbb{X}
    $$
    
    This can be rewritten as:
    
    $$
    \mathbf{S} = \frac{1}{n} \mathbb{X}^T \left( I_n - \frac{1}{n} \mathbf{1} \mathbf{1}^T \right) \mathbb{X}
    $$
    

## 5. **Matrix Products Involving Outer Products**

Let $\mathbf{x}$ denote a $3 \times 1$ column vector and let $\mathbf{1}$ denote the $3 \times 1$ column vector with all entries equal to 1. Suppose that the entries of $\mathbf{x}$ sum to 0. That is, $\mathbf{x}_1 + \mathbf{x}_2 + \mathbf{x}_3 = 0$.

Matrix multiplication is associative, so we may write $(\mathbf{1} \mathbf{1}^ T) \mathbf{x}= \mathbf{1} (\mathbf{1}^ T \mathbf{x}).$

Note that $\mathbf{1}^ T \mathbf{x}= \mathbf{x}^1 + \mathbf{x}^2 + \mathbf{x}^3 = 0$ by assumption. Hence, the first response is correct.

$$
(\mathbf{1} \mathbf{1}^ T) \mathbf{x}= \begin{pmatrix} 1\\ 1\\ 1\end{pmatrix}(0) = \begin{pmatrix}  0 \\ 0 \\ 0 \end{pmatrix}.
$$

## **6. An Orthogonal Projection Matrix I**

The matrix

| H = I_ n - \frac{1}{n} \mathbf{1} \mathbf{1}^ T |  |
| --- | --- |

arises in the formula for the empirical covariance matrix of a data set. For simplicity, let's set n = 3. Then we have

Let \mathbf{x} = (2, -1, -2)^ T.

What is H \mathbf{x}?

What is H^2 \mathbf{x}?

To solve the given problem, we need to compute \(H \mathbf{x}\) and \(H^2 \mathbf{x}\) for the given vector \(\mathbf{x}\).

First, let's define the matrix \(H\):

\[
H = I_n - \frac{1}{n} \mathbf{1} \mathbf{1}^T
\]

For \(n = 3\), this matrix becomes:

\[
H = I_3 - \frac{1}{3} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \end{pmatrix}
\]

The matrix \(\mathbf{1} \mathbf{1}^T\) is:

\[
\mathbf{1} \mathbf{1}^T = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}
\]

So, \(H\) is:

\[
H = I_3 - \frac{1}{3} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} - \begin{pmatrix} \frac{1}{3} & \frac{1}{3} & \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} & \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} & \frac{1}{3} \end{pmatrix}
\]

\[
H = \begin{pmatrix} 1 - \frac{1}{3} & 0 - \frac{1}{3} & 0 - \frac{1}{3} \\ 0 - \frac{1}{3} & 1 - \frac{1}{3} & 0 - \frac{1}{3} \\ 0 - \frac{1}{3} & 0 - \frac{1}{3} & 1 - \frac{1}{3} \end{pmatrix} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} & -\frac{1}{3} \\ -\frac{1}{3} & \frac{2}{3} & -\frac{1}{3} \\ -\frac{1}{3} & -\frac{1}{3} & \frac{2}{3} \end{pmatrix}
\]

Now, let's find \(H \mathbf{x}\) where \(\mathbf{x} = \begin{pmatrix} 2 \\ -1 \\ -2 \end{pmatrix}\):

\[
H \mathbf{x} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} & -\frac{1}{3} \\ -\frac{1}{3} & \frac{2}{3} & -\frac{1}{3} \\ -\frac{1}{3} & -\frac{1}{3} & \frac{2}{3} \end{pmatrix} \begin{pmatrix} 2 \\ -1 \\ -2 \end{pmatrix}
\]

We will compute each component of \(H \mathbf{x}\):

\[
(H \mathbf{x})^{(1)} = \frac{2}{3} \cdot 2 + (-\frac{1}{3}) \cdot (-1) + (-\frac{1}{3}) \cdot (-2) = \frac{4}{3} + \frac{1}{3} + \frac{2}{3} = \frac{7}{3}
\]

\[
(H \mathbf{x})^{(2)} = (-\frac{1}{3}) \cdot 2 + \frac{2}{3} \cdot (-1) + (-\frac{1}{3}) \cdot (-2) = -\frac{2}{3} - \frac{2}{3} + \frac{2}{3} = -\frac{2}{3}
\]

\[
(H \mathbf{x})^{(3)} = (-\frac{1}{3}) \cdot 2 + (-\frac{1}{3}) \cdot (-1) + \frac{2}{3} \cdot (-2) = -\frac{2}{3} + \frac{1}{3} - \frac{4}{3} = -\frac{5}{3}
\]

So, \(H \mathbf{x}\) is:

\[
H \mathbf{x} = \begin{pmatrix} \frac{7}{3} \\ -\frac{2}{3} \\ -\frac{5}{3} \end{pmatrix}
\]

**\(H^2 \mathbf{x}\)**

Next, we need to find \(H^2 \mathbf{x}\):

\[
H^2 \mathbf{x} = H (H \mathbf{x})
\]

Given that \(H \mathbf{x} = \begin{pmatrix} \frac{7}{3} \\ -\frac{2}{3} \\ -\frac{5}{3} \end{pmatrix}\), we need to compute:

\[
H^2 \mathbf{x} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} & -\frac{1}{3} \\ -\frac{1}{3} & \frac{2}{3} & -\frac{1}{3} \\ -\frac{1}{3} & -\frac{1}{3} & \frac{2}{3} \end{pmatrix} \begin{pmatrix} \frac{7}{3} \\ -\frac{2}{3} \\ -\frac{5}{3} \end{pmatrix}
\]

We will compute each component of \(H^2 \mathbf{x}\):

\[
(H^2 \mathbf{x})^{(1)} = \frac{2}{3} \cdot \frac{7}{3} + (-\frac{1}{3}) \cdot (-\frac{2}{3}) + (-\frac{1}{3}) \cdot (-\frac{5}{3}) = \frac{14}{9} + \frac{2}{9} + \frac{5}{9} = \frac{21}{9} = \frac{7}{3}
\]

\[
(H^2 \mathbf{x})^{(2)} = (-\frac{1}{3}) \cdot \frac{7}{3} + \frac{2}{3} \cdot (-\frac{2}{3}) + (-\frac{1}{3}) \cdot (-\frac{5}{3}) = -\frac{7}{9} - \frac{4}{9} + \frac{5}{9} = -\frac{6}{9} = -\frac{2}{3}
\]

\[
(H^2 \mathbf{x})^{(3)} = (-\frac{1}{3}) \cdot \frac{7}{3} + (-\frac{1}{3}) \cdot (-\frac{2}{3}) + \frac{2}{3} \cdot (-\frac{5}{3}) = -\frac{7}{9} + \frac{2}{9} - \frac{10}{9} = -\frac{15}{9} = -\frac{5}{3}
\]

So, \(H^2 \mathbf{x}\) is:

\[
H^2 \mathbf{x} = \begin{pmatrix} \frac{7}{3} \\ -\frac{2}{3} \\ -\frac{5}{3} \end{pmatrix}
\]

Summary

- \((H \mathbf{x})^{(1)} = \frac{7}{3}\)
- \((H \mathbf{x})^{(2)} = -\frac{2}{3}\)
- \((H \mathbf{x})^{(3)} = -\frac{5}{3}\)
- \((H^2 \mathbf{x})^{(1)} = \frac{7}{3}\)
- \((H^2 \mathbf{x})^{(2)} = -\frac{2}{3}\)
- \((H^2 \mathbf{x})^{(3)} = -\frac{5}{3}\)

Note that \(H\) is an idempotent matrix, meaning \(H^2 = H\), so \(H^2 \mathbf{x} = H \mathbf{x}\).

## **7. An Orthogonal Projection Matrix** II

As in the previous problem, we consider the matrix $H = I_ n - \frac{1}{n} \mathbf{1} \mathbf{1}^ T$

and for simplicity let $n = 3$. Let $\mathbf{x} = (2, -1, -2)^ T$.

What is $H^{100} \mathbf{x}$?

Given the matrix $H = I_n - \frac{1}{n} \mathbf{1} \mathbf{1}^T$ and the vector $\mathbf{x} = (2, -1, -2)^T$, we need to find $H^{100} \mathbf{x}$ for $n = 3$.

From the previous problem, we know that $H$ is an idempotent matrix, meaning $H^2 = H$. This property extends to higher powers of $H$: $H^k = H \quad \text{for any } k \geq 1$ 

Thus: $H^{100} = H$ 

So, we only need to compute $H \mathbf{x}$ once, as done in the previous problem.

The matrix $H$ is:

$$
H = I_3 - \frac{1}{3} \mathbf{1} \mathbf{1}^T = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} & -\frac{1}{3} \\ -\frac{1}{3} & \frac{2}{3} & -\frac{1}{3} \\ -\frac{1}{3} & -\frac{1}{3} & \frac{2}{3} \end{pmatrix} 
$$

We previously computed $H \mathbf{x}$ as:

$$
H \mathbf{x} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} & -\frac{1}{3} \\ -\frac{1}{3} & \frac{2}{3} & -\frac{1}{3} \\ -\frac{1}{3} & -\frac{1}{3} & \frac{2}{3} \end{pmatrix} \begin{pmatrix} 2 \\ -1 \\ -2 \end{pmatrix} = \begin{pmatrix} \frac{7}{3} \\ -\frac{2}{3} \\ -\frac{5}{3} \end{pmatrix} 
$$

Therefore, since \(H^{100} = H\):

\[
H^{100} \mathbf{x} = H \mathbf{x} = \begin{pmatrix} \frac{7}{3} \\ -\frac{2}{3} \\ -\frac{5}{3} \end{pmatrix}
\]

To summarize:

- \((H^{100} \mathbf{x})^{(1)} = \frac{7}{3}\)
- \((H^{100} \mathbf{x})^{(2)} = -\frac{2}{3}\)
- \((H^{100} \mathbf{x})^{(3)} = -\frac{5}{3}\)

## **8. Concept Check: Orthogonal Projections**

Let \mathrm{{\boldsymbol X}}_1, \ldots , \mathrm{{\boldsymbol X}}_ n \in \mathbb {R}^ d denote a data set and let

| \mathbb {X} = \begin{pmatrix}  \longleftarrow &  \mathbf{X}_1^ T &  \longrightarrow \\ \longleftarrow &  \mathbf{X}_2^ T &  \longrightarrow \\ \vdots &  \vdots &  \vdots \\ \longleftarrow &  \mathbf{X}_ n^ T &  \longrightarrow \\ \end{pmatrix}. |  |
| --- | --- |

Recall that the empirical covariance matrix S of this data set can be expressed as

| S = \frac{1}{n} \mathbb {X}^ T H \mathbb {X} |  |
| --- | --- |

where

| H = I_ n - \frac{1}{n} \mathbf{1} \mathbf{1}^ T. |  |
| --- | --- |

The matrix H \in \mathbb {R}^{n \times n} is an **orthogonal projection** .

In general, we say that a matrix M is an **orthogonal projection onto a subspace S** if

1. M is symmetric,
2. M^2 = M, and
3. S = \{ \mathrm{{\boldsymbol y}} : \, M \mathbf{x}= y \, \, \text {for some} \, \, \mathbf{x}\in \mathbb {R}^ n \}

To analyze the properties of the matrix \(H\), we need to check each given statement against the properties of \(H\).

First, let's recall the definition of \(H\):

\[
H = I_n - \frac{1}{n} \mathbf{1} \mathbf{1}^T
\]

where \(I_n\) is the \(n \times n\) identity matrix, and \(\mathbf{1}\) is the \(n \times 1\) vector with all entries equal to 1.

Checking the Statements

a) For any positive integer \(k\) and any vector \(\mathbf{x} \in \mathbb{R}^n\), we have \(H^k \mathbf{x} = H \mathbf{x}\).

Since \(H\) is idempotent (\(H^2 = H\)), it follows that for any positive integer \(k\), \(H^k = H\). Therefore:

\[
H^k \mathbf{x} = H \mathbf{x}
\]

This statement is **true**.

b) For any positive integer \(k\) and any vector \(\mathbf{x} \in \mathbb{R}^n\), we have \(H^k \mathbf{x} = \mathbf{x}\).

This statement implies that \(H\) acts as the identity matrix for any vector \(\mathbf{x}\), which is not true. \(H\) is a projection matrix, not the identity matrix, and does not leave all vectors unchanged. Therefore:

This statement is **false**.

c) The matrix \(H\) is a projection onto the subspace of vectors perpendicular to the vector \(\mathbf{1} \in \mathbb{R}^n\), which has all of its entries equal to 1.

To check this, observe that the matrix \(H\) projects onto the subspace orthogonal to \(\mathbf{1}\). Since \(\mathbf{1}\mathbf{1}^T\) projects any vector onto the span of \(\mathbf{1}\), \(H = I_n - \frac{1}{n} \mathbf{1} \mathbf{1}^T\) projects onto the orthogonal complement of the span of \(\mathbf{1}\). Therefore:

This statement is **true**.

d) The matrix \(H\) is a projection onto the subspace \(\left\{ \mathbf{x} : \frac{1}{n} \sum_{i=1}^n x_i = 0 \right\} \subset \mathbb{R}^n\).

This subspace consists of vectors whose components sum to zero, meaning their coordinate-wise average is zero. This subspace is indeed the orthogonal complement of the span of \(\mathbf{1}\). Since \(H\) projects onto this subspace, this statement is **true**.

Summary

- **a) For any positive integer \(k\) and any vector \(\mathbf{x} \in \mathbb{R}^n\), we have \(H^k \mathbf{x} = H \mathbf{x}\).** (True)
- **b) For any positive integer \(k\) and any vector \(\mathbf{x} \in \mathbb{R}^n\), we have \(H^k \mathbf{x} = \mathbf{x}\).** (False)
- **c) The matrix \(H\) is a projection onto the subspace of vectors perpendicular to the vector \(\mathbf{1} \in \mathbb{R}^n\), which has all of its entries equal to 1.** (True)
- **d) The matrix \(H\) is a projection onto the subspace \(\left\{ \mathbf{x} : \frac{1}{n} \sum_{i=1}^n x_i = 0 \right\} \subset \mathbb{R}^n\).** (True)

# **III. Measuring the Spread of a Point Cloud**

## **1. Projection onto a Line**

Let [mathjaxinline]\mathbf{u}\in \mathbb {R^ d}[/mathjaxinline] denote a unit vector (*i.e.*, [mathjaxinline]\sum _{i = 1}^ d (\mathbf{u}^ i)^2 = 1[/mathjaxinline]). In this unit, we will frequently refer to a unit vector as a **direction** , because we are primarily interested in the direction in which [mathjaxinline]\mathbf{u}[/mathjaxinline] is pointing.

In general, the **projection** of a vector [mathjaxinline]\mathbf{x}\in \mathbb {R}^ d[/mathjaxinline] onto a **unit vector** [mathjaxinline]\mathbf{u}[/mathjaxinline] is defined to be

| [mathjax]\text {proj}_{\mathbf{u}} \mathbf{x}:= \left(\mathbf{u}\cdot \mathbf{x}\right) \mathbf{u}.[/mathjax] |  |
| --- | --- |

Note that if the vector onto which we project is not given as a unit vector but a vector, say [mathjaxinline]\mathbf v[/mathjaxinline], with length [mathjaxinline]\left\| \mathbf v \right\|[/mathjaxinline], then form the unit vector [mathjaxinline]\, \displaystyle \mathbf{u}=\frac{\mathbf v}{\left\| v \right\| }[/mathjaxinline] and apply the same formula as above: [mathjaxinline]\, \displaystyle \text {proj}_{\mathbf v} \mathbf{x}\, = \, \left(\frac{\mathbf v}{\left\| \mathbf v \right\| } \cdot \mathbf{x}\right) \frac{\mathbf v}{\left\| \mathbf v \right\| }\, =\, \left(\frac{\mathbf v\cdot \mathbf{x}}{\left\| \mathbf v \right\| ^2} \right) \mathbf v.[/mathjaxinline]

In this problem, we set [mathjaxinline]d = 2[/mathjaxinline] and let [mathjaxinline]\mathbf{u}= \frac{1}{\sqrt{5}}(1, 2)^ T[/mathjaxinline]. Suppose we have a data set consisting of three points given by

|  | [mathjaxinline]\displaystyle \mathrm{{\boldsymbol X}}_1[/mathjaxinline] | [mathjaxinline]\displaystyle = (1,2)^ T[/mathjaxinline] |  |  |
| --- | --- | --- | --- | --- |
|  | [mathjaxinline]\displaystyle \mathrm{{\boldsymbol X}}_2[/mathjaxinline] | [mathjaxinline]\displaystyle = (3,4)^ T[/mathjaxinline] |  |  |
|  | [mathjaxinline]\displaystyle \mathrm{{\boldsymbol X}}_3[/mathjaxinline] | [mathjaxinline]\displaystyle = (-1, 0)^ T.[/mathjaxinline] |  |  |

Find the vectors [mathjaxinline]\text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_1[/mathjaxinline], [mathjaxinline]\text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_2[/mathjaxinline], and [mathjaxinline]\text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_3[/mathjaxinline]. (Also plot them on a piece of paper.)

Note that [mathjaxinline]\mathbf{u}[/mathjaxinline] is a unit vector:

| [mathjax]\left\| \mathbf{u} \right\| _2^2 = \frac{1}{5} (1^2 + 2^2) = 1.[/mathjax] |  |
| --- | --- |

By this fact and the given formula for the projection, we see that

|  | [mathjaxinline]\displaystyle \text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_1[/mathjaxinline] | [mathjaxinline]\displaystyle = (\frac{1}{\sqrt{5}} (1,2)^ T \frac{1}{\sqrt{5}} \cdot (1,2)^ T) \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix}[/mathjaxinline] |  |  |
| --- | --- | --- | --- | --- |
|  | [mathjaxinline]\displaystyle \text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_2[/mathjaxinline] | [mathjaxinline]\displaystyle = (\frac{1}{\sqrt{5}} (1,2)^ T \cdot (3,4)^ T) \frac{1}{\sqrt{5}} \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix} = \begin{pmatrix} \frac{11}{5} \\ \frac{22}{5} \\ \end{pmatrix} \approx \begin{pmatrix} 2.2 \\ 4.4 \end{pmatrix}[/mathjaxinline] |  |  |
|  | [mathjaxinline]\displaystyle \text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_3[/mathjaxinline] | [mathjaxinline]\displaystyle = (\frac{1}{\sqrt{5}} (1,2)^ T \cdot (-1,0)^ T) \frac{1}{\sqrt{5}} \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix} = \begin{pmatrix} -0.2 \\ -0.4 \\ \end{pmatrix}[/mathjaxinline] |  |  |

**Remark 1**

: Observe that the point [mathjaxinline](1,2)^ T[/mathjaxinline] is already on the line that points in the direction of [mathjaxinline]\mathbf{u}[/mathjaxinline]. Hence, the projection of this point onto [mathjaxinline]\mathbf{u}[/mathjaxinline] leaves this point fixed.

**Remark 2**

: A geometric interpretation of [mathjaxinline]\text {proj}_{\mathbf{u}} \mathbf{x}[/mathjaxinline] is given by the following. Consider the line [mathjaxinline]L_1[/mathjaxinline] that points in the direction of [mathjaxinline]\mathbf{u}[/mathjaxinline]. Formally, this is defined as

| [mathjax]L_1 := \{ \lambda \mathbf{u}: \, \lambda \in \mathbb {R} \} .[/mathjax] |  |
| --- | --- |

Now consider the (unique) line [mathjaxinline]L_2[/mathjaxinline] that has the following properties:

- It passes through the endpoint of the vector [mathjaxinline]\mathbf{x}[/mathjaxinline],
- it passes through a point on the line [mathjaxinline]L_1[/mathjaxinline], and
- it is perpendicular to [mathjaxinline]L_1[/mathjaxinline].

The **intersection** of [mathjaxinline]L_1[/mathjaxinline] and [mathjaxinline]L_2[/mathjaxinline] is defined to be the endpoint of the vector [mathjaxinline]\text {proj}_{\mathbf{u}} \mathbf{x}[/mathjaxinline].

You should compare this definition with the formula given for the projection and see, at least visually, that they give the same result.

## **2. Empirical Variance of a Data Set in a Given Direction**

Consider the statistical set-up from the previous problem. In particular, recall that [mathjaxinline]\mathbf{u}= \frac{1}{\sqrt{5}} (1,2)^ T[/mathjaxinline] and

|  | [mathjaxinline]\displaystyle \mathrm{{\boldsymbol X}}_1 \, =\, \begin{pmatrix} 1\\ 2\end{pmatrix},\, \mathrm{{\boldsymbol X}}_2 \, = \, \begin{pmatrix} 3\\ 4\end{pmatrix},\, \mathrm{{\boldsymbol X}}_3 \, =\, \begin{pmatrix} -1 \\ 0\end{pmatrix}.[/mathjaxinline] |  |  |
| --- | --- | --- | --- |

Observe that for [mathjaxinline]i = 1,2,3[/mathjaxinline], the number [mathjaxinline]\mathbf{u}\cdot \mathrm{{\boldsymbol X}}_ i[/mathjaxinline] (where [mathjaxinline]\mathbf{u}[/mathjaxinline] is a unit vector) gives the **signed distance** from the origin to the endpoint of the projection [mathjaxinline]\text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_ i[/mathjaxinline]. By **signed distance** , we mean that [mathjaxinline]\left| \mathbf{u}\cdot \mathrm{{\boldsymbol X}}_ i \right|[/mathjaxinline] is the length of [mathjaxinline]\text {proj}_{\mathbf{u}} \mathrm{{\boldsymbol X}}_ i[/mathjaxinline] and

|  | [mathjaxinline]\displaystyle \mathbf{u}\cdot \mathrm{{\boldsymbol X}}_ i > 0[/mathjaxinline] | [mathjaxinline]\displaystyle \Longrightarrow \mathrm{{\boldsymbol X}}_ i \, \, \text {points approximately in the direction of } \, \mathbf{u}[/mathjaxinline] |  |  |
| --- | --- | --- | --- | --- |
|  | [mathjaxinline]\displaystyle \mathbf{u}\cdot \mathrm{{\boldsymbol X}}_ i < 0[/mathjaxinline] | [mathjaxinline]\displaystyle \Longrightarrow \mathrm{{\boldsymbol X}}_ i \, \, \text {points approximately in the opposite direction of } \, \mathbf{u}\,[/mathjaxinline] |  |  |

Compute the empirical variance of the data set

Vector \(\mathbf{u}\)

The variance \(\textsf{Var}(\mathrm{{\boldsymbol X}}^1)\) can be expressed as \(\mathbf{u}^T \Sigma \mathbf{u}\) where \(\mathbf{u}\) is a unit vector in the direction of the first coordinate axis.

\[
\mathbf{u} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
\]

So:
\[
\mathbf{u}^1 = 1, \quad \mathbf{u}^2 = 0
\]

Vector \(\mathrm{{\boldsymbol v}}\)

The variance \(\textsf{Var}(\mathrm{{\boldsymbol X}}^2)\) can be expressed as \(\mathrm{{\boldsymbol v}}^T \Sigma \mathrm{{\boldsymbol v}}\) where \(\mathrm{{\boldsymbol v}}\) is a unit vector in the direction of the second coordinate axis.

\[
\mathrm{{\boldsymbol v}} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
\]

So:
\[
\mathrm{{\boldsymbol v}}^1 = 0, \quad \mathrm{{\boldsymbol v}}^2 = 1
\]

Vector \(\mathrm{{\boldsymbol w}}\)

The variance \(\textsf{Var}(\mathrm{{\boldsymbol X}}^1 + \mathrm{{\boldsymbol X}}^2)\) can be expressed as \(\mathrm{{\boldsymbol w}}^T \Sigma \mathrm{{\boldsymbol w}}\) where \(\mathrm{{\boldsymbol w}}\) is a vector in the direction of \(\mathrm{{\boldsymbol X}}^1 + \mathrm{{\boldsymbol X}}^2\).

Given that \(\mathrm{{\boldsymbol X}}^1 + \mathrm{{\boldsymbol X}}^2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \cdot \mathrm{{\boldsymbol X}}\), the vector \(\mathrm{{\boldsymbol w}}\) in this direction is:

\[
\mathrm{{\boldsymbol w}} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
\]

So:
\[
\mathrm{{\boldsymbol w}}^1 = 1, \quad \mathrm{{\boldsymbol w}}^2 = 1
\]

Summary

- \(\mathbf{u}^1 = 1, \quad \mathbf{u}^2 = 0\)
- \(\mathrm{{\boldsymbol v}}^1 = 0, \quad \mathrm{{\boldsymbol v}}^2 = 1\)
- \(\mathrm{{\boldsymbol w}}^1 = 1, \quad \mathrm{{\boldsymbol w}}^2 = 1\)

## **3. A Preview of Principal Component Analysis**

This problem illustrates some of the main ideas behind principal component analysis, which will be explored in detail later in this lecture as well as the next lecture.

Let [mathjaxinline]\mathrm{{\boldsymbol X}}_1, \ldots , \mathrm{{\boldsymbol X}}_ n \in \mathbb {R}^ d[/mathjaxinline] denote a data set, and let [mathjaxinline]\mathbb {X}[/mathjaxinline] denote the matrix whose [mathjaxinline]i[/mathjaxinline]-th row is [mathjaxinline]\mathrm{{\boldsymbol X}}_ i^ T[/mathjaxinline]. Let

| [mathjax]S = \frac{1}{n} \mathbb {X}^ T \left(I_ n - \frac{1}{n} \mathbf{1} \mathbf{1}^ T \right) \mathbb {X}[/mathjax] |  |
| --- | --- |

denote the empirical covariance matrix for this data set.

Consider the optimization problem

| [mathjax]\displaystyle \text {argmax}_{\mathbf{u}: \left\| \mathbf{u} \right\| _2^2 =1 } \mathbf{u}^ T S \mathbf{u}.[/mathjax] |  |
| --- | --- |

Let [mathjaxinline]\mathbf{u}^*[/mathjaxinline] denote the unit vector that maximizes [mathjaxinline]\mathbf{u}^ T S \mathbf{u}[/mathjaxinline].

Consider the optimization problem

| [mathjax]\displaystyle \text {argmax}_{\mathbf{u}: \left\| \mathbf{u} \right\| _2^2 =1 } \mathbf{u}^ T S \mathbf{u}.[/mathjax] |  |
| --- | --- |

Let [mathjaxinline]\mathbf{u}^*[/mathjaxinline] denote the unit vector that maximizes [mathjaxinline]\mathbf{u}^ T S \mathbf{u}[/mathjaxinline].

Which of the following is a correct interpretation of [mathjaxinline]\mathbf{u}^*[/mathjaxinline]? (Choose all that apply.)

To solve the optimization problem and interpret \(\mathbf{u}^*\), let's first understand the optimization problem itself:

\[
\text{argmax}_{\mathbf{u}: \|\mathbf{u}\|_2^2 = 1} \mathbf{u}^T S \mathbf{u}
\]

This is a classic problem in principal component analysis (PCA) where we seek the direction \(\mathbf{u}^*\) that maximizes the variance of the data when projected onto this direction. The covariance matrix \(S\) captures the spread of the data, and \(\mathbf{u}^*\) is the eigenvector corresponding to the largest eigenvalue of \(S\). This vector represents the first principal component.

Let's analyze each option given:

Option a)

\(\mathbf{u}^*\) gives a direction such that the data set \(\mathbf{u}^{*T} \mathbf{X}_1, \mathbf{u}^{*T} \mathbf{X}_2, \ldots, \mathbf{u}^{*T} \mathbf{X}_n\) is clustered closely together.

**Interpretation**: This statement implies that \(\mathbf{u}^*\) minimizes the spread of the projected data points, which is incorrect. The correct interpretation is that \(\mathbf{u}^*\) maximizes the spread (variance) of the projected data points.

**Conclusion**: This statement is **false**.

Option b)

\(\mathbf{u}^*\) is the direction that maximizes the empirical variance of the (projected) data points \(\mathbf{u}^{*T} \mathbf{X}_1, \mathbf{u}^{*T} \mathbf{X}_2, \ldots, \mathbf{u}^{*T} \mathbf{X}_n\).

**Interpretation**: This statement correctly identifies that \(\mathbf{u}^*\) maximizes the variance of the data points when projected onto this direction.

**Conclusion**: This statement is **true**.

Option c)

If \(\mathbf{u}^{*T} S \mathbf{u}^*\) is very large, then if we project our data set onto the line spanned by \(\mathbf{u}^*\), we expect the projected data set to be fairly 'spread out' (i.e., the projected data set should have relatively large empirical variance).

**Interpretation**: This statement is consistent with the purpose of finding \(\mathbf{u}^*\). A large value of \(\mathbf{u}^{T} S \mathbf{u}^\) indicates that the data, when projected onto \(\mathbf{u}^*\), has high variance, meaning it is spread out.

**Conclusion**: This statement is **true**.

Summary:

The correct interpretations of \(\mathbf{u}^*\) are:

- *b) \(\mathbf{u}^*\) is the direction that maximizes the empirical variance of the (projected) data points \(\mathbf{u}^{*T} \mathbf{X}_1, \mathbf{u}^{*T} \mathbf{X}_2, \ldots, \mathbf{u}^{T} \mathbf{X}_n\).*
- **c) If \(\mathbf{u}^{*T} S \mathbf{u}^*\) is very large, then if we project our data set onto the line spanned by \(\mathbf{u}^*\), we expect the projected data set to be fairly 'spread out' (i.e., the projected data set should have relatively large empirical variance).**