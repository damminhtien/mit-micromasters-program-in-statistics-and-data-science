# Midterm 1 Cheat Sheet

# I. Linear Classification

**Problem Overview:**
In linear classification, we aim to find a linear boundary (hyperplane) that separates data points of different classes. Two common algorithms for linear classification are the Perceptron and the Support Vector Machine (SVM).

### 1. Perceptron Algorithm

**Initialization:**

- Initialize the weight vector \(\theta\) and bias \(\theta_0\) to zero.
\[
\theta = [0, 0], \quad \theta_0 = 0
\]

**Update Rule:**

- For each misclassified point \((x_i, y_i)\):
\[
\theta = \theta + y_i x_i
\]
\[
\theta_0 = \theta_0 + y_i
\]

**Iteration:**

- Repeat the update rule until convergence (no more misclassified points or a maximum number of iterations).

**Hinge Loss Calculation:**

- Hinge loss for a data point \((x_i, y_i)\):
\[
L(x_i, y_i) = \max(0, 1 - y_i (\theta \cdot x_i + \theta_0))
\]
- Sum of hinge losses:
\[
\text{Total Hinge Loss} = \sum_{i=1}^{N} L(x_i, y_i)
\]

### 2. Support Vector Machine (SVM)

**Objective:**

- Maximize the margin between the classes while correctly classifying the training data.

**Optimization Problem:**

- Minimize the norm of the weight vector \(\theta\):
\[
\min_{\theta, \theta_0} \frac{1}{2} \|\theta\|^2
\]
- Subject to the constraints:
\[
y_i (\theta \cdot x_i + \theta_0) \geq 1 \quad \forall i
\]

**Margin Calculation:**

- The margin (\(\gamma\)) is given by:
\[
\gamma = \frac{1}{\|\theta\|}
\]

**Modified Parameters:**

- If \(\theta\) and \(\theta_0\) are scaled by a factor (e.g., divided by 2):
\[
\theta' = \frac{1}{2} \theta
\]
\[
\theta_0' = \frac{1}{2} \theta_0
\]

**Hinge Loss with Modified Parameters:**

- Recalculate the hinge loss for each data point with the modified parameters.

### Important Mathematical Concepts:

1. **Dot Product:**
\[
\theta \cdot x = \sum_{i=1}^{d} \theta_i x_i
\]
where \(d\) is the dimension of the vectors.
2. **Sign Function:**
\[
\text{sign}(z) =
\begin{cases}
+1 & \text{if } z > 0 \\
-1 & \text{if } z < 0 \\
0 & \text{if } z = 0
\end{cases}
\]
3. **Euclidean Norm:**
\[
\|\theta\| = \sqrt{\sum_{i=1}^{d} \theta_i^2}
\]

### Summary of Steps for Problem 1:

1. **Initialize Parameters:**
    - Set \(\theta\) and \(\theta_0\) to zero.
2. **Perceptron Updates:**
    - Iterate through data points.
    - Update \(\theta\) and \(\theta_0\) using the Perceptron rule for misclassified points.
3. **Hinge Loss Calculation:**
    - Compute the hinge loss for each data point.
    - Sum the hinge losses.
4. **SVM for Maximum Margin:**
    - Use an SVM solver to find \(\theta\) and \(\theta_0\) that maximize the margin.
    - Calculate the margin.
5. **Modified Parameters:**
    - Adjust \(\theta\) and \(\theta_0\) as specified (e.g., divide by 2).
    - Recompute hinge losses with modified parameters.

By understanding these concepts and steps, you can effectively tackle linear classification problems using both the Perceptron and SVM approaches.

### Perceptron Algorithm

```python
import numpy as np

# Initialize parameters
def initialize_parameters(dimension):
    theta = np.zeros(dimension)
    theta_0 = 0.0
    return theta, theta_0

# Perceptron update rule
def perceptron_update(x, y, theta, theta_0):
    theta += y * x
    theta_0 += y
    return theta, theta_0

# Perceptron algorithm
def perceptron_algorithm(data_points, labels, max_iterations=1000):
    dimension = data_points.shape[1]
    theta, theta_0 = initialize_parameters(dimension)

    for _ in range(max_iterations):
        for x, y in zip(data_points, labels):
            if y * (np.dot(theta, x) + theta_0) <= 0:
                theta, theta_0 = perceptron_update(x, y, theta, theta_0)

    return theta, theta_0

# Example usage
data_points = np.array([
    [0, 0], [2, 0], [3, 0], [0, 2], [2, 2],
    [5, 1], [5, 2], [2, 4], [4, 4], [5, 5]
])
labels = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])

theta, theta_0 = perceptron_algorithm(data_points, labels)
print(f"Theta: {theta}")
print(f"Theta_0: {theta_0}")

```

### Hinge Loss Calculation

```python
# Hinge loss for a single data point
def hinge_loss(x, y, theta, theta_0):
    return max(0, 1 - y * (np.dot(theta, x) + theta_0))

# Sum of hinge losses
def total_hinge_loss(data_points, labels, theta, theta_0):
    return sum(hinge_loss(x, y, theta, theta_0) for x, y in zip(data_points, labels))

# Example usage
hinge_losses = total_hinge_loss(data_points, labels, theta, theta_0)
print(f"Total Hinge Loss: {hinge_losses}")

```

### Support Vector Machine (SVM) using `scikit-learn`

```python
from sklearn.svm import SVC

# SVM for maximum margin
def svm_algorithm(data_points, labels):
    svm = SVC(kernel='linear', C=1e10)  # Large C for hard margin
    svm.fit(data_points, labels)
    theta = svm.coef_[0]
    theta_0 = svm.intercept_[0]
    return theta, theta_0

# Example usage
theta, theta_0 = svm_algorithm(data_points, labels)
print(f"Theta (SVM): {theta}")
print(f"Theta_0 (SVM): {theta_0}")

```

### Modified Parameters

```python
# Modify parameters by dividing by 2
def modify_parameters(theta, theta_0, factor=2):
    return theta / factor, theta_0 / factor

# Example usage
theta_prime, theta_0_prime = modify_parameters(theta, theta_0)
print(f"Modified Theta: {theta_prime}")
print(f"Modified Theta_0: {theta_0_prime}")

# Recalculate total hinge loss with modified parameters
hinge_losses_prime = total_hinge_loss(data_points, labels, theta_prime, theta_0_prime)
print(f"Total Hinge Loss with Modified Parameters: {hinge_losses_prime}")

```

### Summary

- **Initialize Parameters:** Use zeros for \(\theta\) and \(\theta_0\).
- **Perceptron Update Rule:** Update \(\theta\) and \(\theta_0\) for misclassified points.
- **Perceptron Algorithm:** Iterate through data points to find the linear separator.
- **Hinge Loss Calculation:** Compute hinge loss for evaluating classifier performance.
- **Support Vector Machine (SVM):** Use `scikit-learn` to find the maximum margin separator.
- **Modify Parameters:** Adjust \(\theta\) and \(\theta_0\) by a factor and recalculate hinge losses.

This cheat sheet provides the essential code snippets to implement linear classification using Perceptron and SVM in Python with NumPy.

# II. Cheat Sheet for Problem 2: Kernel Methods

### 1. Kernel Perceptron Algorithm

**Feature Map:**
Given the feature map for the quadratic kernel:
\[
\phi(x) = \begin{bmatrix} x_1^2 \\ \sqrt{2} x_1 x_2 \\ x_2^2 \end{bmatrix}
\]

**Kernel Function:**
The kernel function \(K(x, x')\) based on the feature map is:
\[
K(x, x') = \phi(x)^T \phi(x')
\]
In terms of the dot product \(z = x \cdot x'\), the kernel function is:
\[
K(x, x') = (x \cdot x')^2
\]

**Initialization:**

- Initialize \(\theta\) and \(\theta_0\) to zero:
\[
\theta = [0, 0, 0]^T, \quad \theta_0 = 0
\]

**Update Rule:**

- For each misclassified point \((x_i, y_i)\) with mistake count \(m_i\):
\[
\theta = \theta + m_i y_i \phi(x_i)
\]
\[
\theta_0 = \theta_0 + m_i y_i
\]

### 2. Hinge Loss Calculation

**Hinge Loss for a Single Point:**
\[
L(x_i, y_i) = \max(0, 1 - y_i (\theta^T \phi(x_i) + \theta_0))
\]

**Total Hinge Loss:**
\[
\text{Total Hinge Loss} = \sum_{i=1}^{N} L(x_i, y_i)
\]

### 3. Decision Boundary

**Decision Function:**
The decision function for a point \(x\) is:
\[
f(x) = \theta^T \phi(x) + \theta_0
\]

A point \(x\) is correctly classified if:
\[
\text{sign}(f(x)) = y
\]

### 4. Python Code for Kernel Perceptron

```python
import numpy as np

# Data points and labels
data_points = np.array([
    [0, 0], [2, 0], [1, 1], [0, 2], [3, 3],
    [4, 1], [5, 2], [1, 4], [4, 4], [5, 5]
])
labels = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])

# Mistake counts for each point
mistakes = np.array([1, 65, 11, 31, 72, 30, 0, 21, 4, 15])

# Feature map function for the quadratic kernel
def feature_map(x):
    x1, x2 = x
    return np.array([x1**2, np.sqrt(2)*x1*x2, x2**2])

# Initialize theta and theta_0
theta = np.zeros(3)
theta_0 = 0.0

# Update theta and theta_0 based on mistakes
for x, y, m in zip(data_points, labels, mistakes):
    phi_x = feature_map(x)
    theta += m * y * phi_x
    theta_0 += m * y

# Round theta and theta_0 for final output
theta_rounded = np.round(theta, 2)
theta_0_rounded = round(theta_0, 2)

print(f"Theta: {theta_rounded}")
print(f"Theta_0: {theta_0_rounded}")

# Function to compute the decision function f(x)
def decision_function(x, theta, theta_0):
    phi_x = feature_map(x)
    return np.dot(theta, phi_x) + theta_0

# Check if all points are correctly classified
correctly_classified = True
for x, y in zip(data_points, labels):
    fx = decision_function(x, theta_rounded, theta_0_rounded)
    if np.sign(fx) != y:
        correctly_classified = False
        break

print(f"All points correctly classified: {correctly_classified}")

```

### Summary

- **Feature Map**: Transforms the input space using \(\phi(x) = \begin{bmatrix} x_1^2 \\ \sqrt{2} x_1 x_2 \\ x_2^2 \end{bmatrix}\).
- **Kernel Function**: \(K(x, x') = (x \cdot x')^2\).
- **Kernel Perceptron Algorithm**: Updates weights based on the quadratic kernel.
- **Hinge Loss**: Measures classification error.
- **Decision Boundary**: Determines classification correctness.

This cheat sheet provides a comprehensive overview and the necessary code snippets to implement and analyze the kernel perceptron algorithm using the quadratic kernel in Python.