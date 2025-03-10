# Cheatsheet 1

### **Comprehensive Machine Learning Cheatsheet**

### *Linear Classification, Kernel Methods, Stochastic Gradient Descent (SGD), and Neural Networks*

---

## **1. Linear Classification**

### **1.1 Perceptron Algorithm**

**Purpose:**

A fundamental algorithm for binary classification that iteratively finds a linear separator for linearly separable data.

**Initialization:**

- **Weight Vector ($\theta$)**: Initialized to $[0, 0]$
- **Bias ($\theta_0$)**: Initialized to 0

**Algorithm Steps:**

1. **Iterate Through Data Points:**
For each training example $(x^{(i)}, y^{(i)})$:
    - **Activation: $a = \theta \cdot x^{(i)} + \theta_0$**
    - **Prediction: $\hat{y} = \text{sign}(a)$**
    - **Update Rule (if misclassified):**
    If $\hat{y} \neq y^{(i)}$:
        - $\theta \leftarrow \theta + y^{(i)} x^{(i)}$
        - $\theta_0 \leftarrow \theta_0 + y^{(i)}$
2. **Convergence:**
Repeat until all points are correctly classified (no misclassifications) or a maximum number of iterations is reached.

**Key Insights:**

- **Convergence:**
    - **Linearly Separable Data:** The perceptron algorithm converges.
    - **Non-Linearly Separable Data:** The algorithm may diverge (never converge).
- **Impact of Data Order:**
The sequence in which data points are processed can affect the number of updates but not the final separator for linearly separable data.

### **1.2 Maximum Margin Separator (Support Vector Machine - SVM)**

**Purpose:**

Find the optimal linear separator that maximizes the margin (distance to the nearest data points) for better generalization.

**Types:**

- **Hard Margin SVM:**
Assumes data is perfectly separable; no misclassifications allowed.
- **Soft Margin SVM:**
Allows some misclassifications using slack variables $\xi_i$.

**Key Concepts:**

- **Margin (M): $M = \frac{1}{\|\theta\|}$**
- **Support Vectors:**
Data points that lie closest to the decision boundary and define the margin.

**Optimization Problem (Hard Margin):**

$\min_{\theta} \|\theta\|^2 \quad \text{subject to} \quad y^{(i)} (\theta \cdot x^{(i)} + \theta_0) \geq 1 \quad \forall i$ 

**Solution Characteristics:**

- **Parameter Scaling:**
Parameters are scaled such that $\|\theta\| = \sqrt{2}$   when $M = \frac{1}{\sqrt{2}}$.
- **Decision Boundary:**
Defined by $\theta \cdot x + \theta_0 = 0$.

### **1.3 Margin Calculation**

**Formula: $\text{Margin} = \frac{1}{\|\theta\|}$**

**Interpretation:**

- Larger margin implies better generalization.
- For maximum margin separators, the margin is maximized.

### **1.4 Hinge Loss**

**Purpose:**

A loss function used in SVMs to penalize misclassifications and margin violations.

**Formula:**

For each example $i$: $\text{Hinge Loss}_i = \max(0, 1 - y^{(i)} (\theta \cdot x^{(i)} + \theta_0))$

**Sum of Hinge Losses: $\sum_{i=1}^{N} \text{Hinge Loss}_i$**

**Interpretation:**

- **Zero Loss:** Correct classification with a margin of at least 1.
- **Positive Loss:** Indicates misclassification or insufficient margin.

**Impact of Parameter Scaling:**

- **Scaling $\theta$ and $\theta_0$ by a Factor $k$:**
    - **Decision Boundary:** Remains unchanged.
    - **Margin:** Becomes $\frac{1}{k \|\theta\|}$.
    - **Hinge Loss:** Increases for support vectors and may introduce positive losses for previously correctly classified points.

## **2. Kernel Methods**

### **2.1 Introduction to Kernel Methods**

**Purpose:**

Enhance linear algorithms by implicitly mapping data to higher-dimensional feature spaces, enabling the separation of non-linearly separable data.

**Key Concepts:**

- **Feature Map ($\phi$):**
    
    Transforms input data $x$ into a higher-dimensional space.
    
- **Kernel Function ($K(x, x')$):**
    
    Represents the dot product in the transformed feature space without explicit computation of $\phi(x)$.
    

### **2.2 Feature Maps and Kernel Functions**

**Example (Quadratic Kernel): $\phi(x) = \begin{bmatrix} x_1^2 \\ \sqrt{2}x_1x_2 \\ x_2^2 \end{bmatrix}$**

**Kernel Function Definition: $K(x, x') = \phi(x)^T \phi(x') = (x \cdot x')^2$**
*Where $z = x \cdot x' = x_1x'_1 + x_2x'_2$, hence $K(x, x') = z^2$.*

### **2.3 Kernel Perceptron Algorithm**

**Purpose:**

Adapt the perceptron algorithm to work in the transformed feature space using kernel functions, allowing classification of non-linearly separable data.

**Algorithm Steps:**

1. **Initialization:**
    - Set all dual coefficients ($\alpha_i$) to 0.
    - Set bias ($\theta_0$) to 0.
2. **Iterate Through Data Points:**
Similar to the linear perceptron but using kernel functions to compute activations: $a = \sum_{j=1}^{N} \alpha_j y^{(j)} K(x^{(j)}, x^{(i)}) + \theta_0$
    - **Prediction: $\hat{y} = \text{sign}(a)$**
    - **Update Rule (if misclassified):**
    If $\hat{y} \neq y^{(i)}$:
        - $\alpha_i \leftarrow \alpha_i + 1$
        - $\theta_0 \leftarrow \theta_0 + y^{(i)}$
3. **Convergence:**
Repeat until all points are correctly classified in the feature space or a maximum number of iterations is reached.

**Key Insights:**

- **Non-Linearly Separable Data:** Kernel methods can find separators by mapping data to higher dimensions.
- **Choice of Kernel:** Determines the nature of the feature space and the classifier's capability.

### **2.4 Kernel Trick**

**Definition:**

A technique that allows the computation of the dot product in the transformed feature space directly using the kernel function, avoiding explicit mapping.

**Mathematical Representation: $K(x, x') = \phi(x)^T \phi(x')$**

**Benefits:**

- **Efficiency:** Avoids computationally expensive transformations.
- **Flexibility:** Enables the use of various kernels to capture different data patterns.

## **3. Stochastic Gradient Descent (SGD) for Support Vector Machines (SVM)**

### **3.1 Objective Function**

**Objective:**

Minimize the regularized hinge loss to train an SVM classifier.

**Function: $J(\theta) = \left[\frac{1}{n}\sum_{i=1}^n \text{Loss}_h(y^{(i)} \theta \cdot x^{(i)})\right] + \frac{\lambda}{2} \|\theta\|^2$** 
Where: $\text{Loss}_h(z) = \max\{0, 1 - z\}$

- $(x^{(i)}, y^{(i)})$ are the training examples.
- $y^{(i)} \in \{1, -1\}$ is the label.
- $\lambda$ is the regularization parameter.

**Note:**

The offset parameter $\theta_0$ is ignored for simplicity.

### **3.2 Gradient of Hinge Loss**

**Gradient Definition:** 

**$\nabla_\theta \text{Loss}_h(y \theta \cdot x) =$**

- $-y \cdot x\text{ if } y \theta \cdot x \leq 1$
- $0 \text{ if } y \theta \cdot x > 1$

**Interpretation:**

- **Misclassified or Within Margin ($y \theta \cdot x \leq 1$):**
Gradient is $-y \cdot x$.
- **Correctly Classified and Outside Margin ($y \theta \cdot x > 1$):**
Gradient is 0.

### **3.3 Stochastic Gradient Update Rule**

**Update Rule:**

Given a learning rate $\eta > 0$ and a randomly selected training example 

$(x^{(i)}, y^{(i)})$: $\theta \leftarrow \theta - \eta \nabla_\theta \text{Loss}_h(y^{(i)} \theta \cdot x^{(i)}) - \eta \lambda \theta$ 

**Detailed Breakdown:**

- **If $y^{(i)} \theta \cdot x^{(i)} \leq 1$: $\theta \leftarrow (1 - \eta \lambda) \theta + \eta y^{(i)} x^{(i)}$**
- **If $y^{(i)} \theta \cdot x^{(i)} > 1$: $\theta \leftarrow (1 - \eta \lambda) \theta$**

**Key Insights:**

- **Regularization Term ($\lambda \|\theta\|^2$):**
Encourages smaller weights to prevent overfitting.
- **Learning Rate ($\eta$):**
Determines the step size during updates.
- **Impact of $\eta$ and $\lambda$:**
    - **Large $\eta$:** Faster updates but risk overshooting.
    - **Proper $\eta$ and $\lambda$:** Balance between convergence speed and model generalization.

**Example Recap:**

- **For $y \theta \cdot x > 1$ and $0.5 < \eta \lambda < 1$:**
    - $\theta$ is shrunk by a factor of $(1 - \eta \lambda)$, increasing the margin.
- **For $y \theta \cdot x \leq 1$:**
    - $\theta$ is updated towards the misclassified point, adjusting the decision boundary.

### **3.4 Example Update Scenarios**

**Scenario 1: Point Correctly Classified ($y \theta \cdot x > 1$)**

- **Action:**
Shrink $\theta$ by $(1 - \eta \lambda)$.
- **Result:**
Increased margin without altering the decision boundary's direction.

**Scenario 2: Point Misclassified or Within Margin ($y \theta \cdot x \leq 1$)**

- **Action:**
Shrink $\theta$ by $(1 - \eta \lambda)$ and adjust $\theta$ towards the point $\eta y x$.
- **Result:**
Moves the decision boundary to better classify the point.

**Additional Example (Problem 3.1):**

- **Regions Mapping in Neural Networks:**
    - **Region I & II:** Mapped to $f_1 > 0, f_2 > 0$
    - **f₁-axis:** Mapped from regions I & II
    - **f₂-axis:** Mapped from regions I & IV
    - **Origin (0,0):** Mapped from regions III & IV

## **4. Neural Networks**

### **4.1 Two-Layer Feed-Forward Neural Network with ReLU Units**

**Architecture:**

- **Input Layer:**
Takes input $x \in \mathbb{R}^2$.
- **Hidden Layer:**
Consists of two ReLU units without offset parameters.
- **Output Layer:**
Produces outputs $f_1$ and $f_2$ based on hidden unit activations.

**ReLU Activation Function: $f(z) = \max(0, z)$**

**Mapping Regions:**

- **Classifier Lines:**
    - $z_1 = x \cdot w_1 = 0$
    - $z_2 = x \cdot w_2 = 0$
- **Regions Defined by Classifiers:**
    - **Region I:** $z_1 > 0, z_2 > 0$
    - **Region II:** $z_1 > 0, z_2 < 0$
    - **Region III:** $z_1 < 0, z_2 < 0$
    - **Region IV:** $z_1 < 0, z_2 > 0$

**Activation Mappings:**

- **Region I:** $(f_1, f_2) = (f(z_1), f(z_2)) = (f_1 > 0, f_2 > 0)$
- **Region II:** $(f_1, f_2) = (f(z_1) > 0, f(z_2) = 0)$
- **Region III:** $(f_1, f_2) = (f(z_1) = 0, f(z_2) = 0)$
- **Region IV:** $(f_1, f_2) = (f(z_1) = 0, f(z_2) > 0)$

**Example Problem Recap (Problem 4.1):**

- **Mapping Regions:**
    - **$\{ f_1 > 0, f_2 > 0 \}$:** Mapped from Region I
    - **f₁-axis:** Mapped from Regions I & II
    - **f₂-axis:** Mapped from Regions I & IV
    - **Origin (0,0):** Mapped from Regions III & IV

**Answer Insights:**

- **All Regions Considered:**
Correct mappings include Regions I, II, III, IV based on the activation outputs.

### **4.2 Adding and Training Additional Hidden Layers**

**Scenario:**

Keeping the hidden layer parameters fixed but adding and training additional hidden layers to further transform the data.

**Question:** Can the resulting neural network solve the classification problem? **Answer: Yes**

**Explanation:**

- **Flexibility of Additional Layers:**
Additional layers can learn complex transformations, enabling the network to handle non-linearly separable data.
- **Example Problem Recap (Problem 4.2):**
    - **Initial Mapping:**
    Certain regions are mapped to specific activation patterns.
    - **Additional Layers:**
    Further transformations can separate classes that were not separable in the initial feature space.

### **4.3 Increasing Hidden Units in Two-Layer Architecture**

**Scenario:**

Sticking to the two-layer architecture but adding many more ReLU hidden units, all without offset parameters.

**Question:** Is it possible to train such a model to perfectly separate the points? **Answer: Yes/ No**

**Explanation:**

- **Yes:**
Adding more hidden units can create multiple linear separators, allowing the network to model complex decision boundaries.
- **No:**
If certain regions (e.g., Region III) are all mapped to the origin and cannot be separated by additional units, perfect separation may be impossible.

**Key Insight:**

- **No Offset Parameters:**
Limits the flexibility of hidden units to shift decision boundaries, potentially hindering perfect separation.
- **Assumption:**
No two data points lie on the same line through the origin, requiring unique separation strategies.

### **4.4 Convolutional Layers vs. Fully Connected Layers in CNNs**

**Question:**

Check True (T) or False (F) for each statement regarding the use of convolutional layers in CNNs versus fully connected layers.

1. **Statement:**
    
    *Since we apply the same convolutional filter throughout the image, we can learn to recognize the same feature wherever it appears.* **Answer: True**
    
2. **Statement:**
    
    *A fully connected layer for an image has more parameters than the size of the image.* **Answer: True**
    
3. **Statement:**
    
    *A fully connected layer can learn to recognize features anywhere in the image even if the features appeared preferentially in one location during training.* **Answer: No**
    

**Explanation:**

- **Convolutional Layers:** Share weights across spatial locations, enabling feature recognition irrespective of position.
- **Fully Connected Layers:** Have separate weights for each input unit, leading to a large number of parameters and limited ability to generalize feature locations.

**Example Problem Recap (Problem 4.4):**

- **Advantages of Convolutional Layers:**
    - **Parameter Efficiency:**
    Fewer parameters compared to fully connected layers.
    - **Spatial Invariance:**
    Recognize features regardless of their position in the input.
- **Disadvantages of Fully Connected Layers:**
    - **High Parameter Count:**
    More parameters, leading to higher computational cost.
    - **Limited Spatial Generalization:**
    Can only recognize features where they were trained to appear.

## **5. Quick Reference Formulas**

### **5.1 Perceptron Updates:**

$\theta \leftarrow \theta + y^{(i)} x^{(i)}$

$\theta_0 \leftarrow \theta_0 + y^{(i)}$

### **5.2 Margin:**

$\text{Margin} = \frac{1}{\|\theta\|}$

### **5.3 Hinge Loss:**

$\max(0, 1 - y^{(i)} (\theta \cdot x^{(i)} + \theta_0))$

### **5.4 Support Vector Condition:**

$y^{(i)} (\theta \cdot x^{(i)} + \theta_0) = 1$

### **5.5 Kernel Function (Quadratic):**

$K(x, x') = (x \cdot x')^2$

### **5.6 SGD Update Rule for SVM:**

$\theta \leftarrow
\begin{cases}
(1 - \eta \lambda) \theta + \eta y^{(i)} x^{(i)} & \text{if } y^{(i)} \theta \cdot x^{(i)} \leq 1 \\
(1 - \eta \lambda) \theta & \text{if } y^{(i)} \theta \cdot x^{(i)} > 1
\end{cases}$ 

### **5.7 Backpropagation Gradient:**

$\nabla_\theta \text{Loss} = \frac{\partial \text{Loss}}{\partial \theta} = \text{vector of partial derivatives}$ 

## **6. Common Concepts and Tips**

- **Linearly Separable vs. Non-Linearly Separable:**
    - **Linearly Separable:** Perceptron converges; SVM finds a perfect separator.
    - **Non-Linearly Separable:** Perceptron may diverge; kernel methods or soft-margin SVMs are required.
- **Support Vectors Identification:**
    - Critical in defining the decision boundary and margin.
- **Kernel Trick:**
    - Enables computation in high-dimensional feature spaces efficiently without explicit mapping.
- **Order Sensitivity:**
    - Perceptron’s convergence and number of updates can depend on the order of data points.
- **Parameter Notation:**
    - **Vectors:** Represented as lists, e.g., $[θ_1, θ_2]$
    - **Operations:** Use explicit symbols (e.g., $+, -, *, /, ^$ )
    - **Functions:** Use standard names with parentheses (e.g., `sin(x)`, `sqrt(x)`, `ln(x)`)
- **Regularization in SGD:**
    - **Purpose:** Prevent overfitting by penalizing large weights.
    - **Effect:** Shrinks weights during updates, increasing the margin.
- **Convolutional Layers vs. Fully Connected Layers:**
    - **Convolutional Layers:**
        - Share weights across spatial locations.
        - Efficient with fewer parameters.
        - Enable spatial invariance.
    - **Fully Connected Layers:**
        - Each input unit connects to every output unit.
        - High parameter count.
        - Limited ability to generalize spatial features.
- **Weight Initialization in Neural Networks:**
    - **Importance:**
    Proper initialization can prevent issues like vanishing/exploding gradients.
    - **Small Weights:**
    Can lead to nearly linear behavior with activation functions like sigmoid.
    - **Large Weights:**
    Can cause activation functions to saturate, behaving like sign functions.

## **7. Common Mistakes to Avoid**

- **Incorrect Parameter Scaling:**
    
    Forgetting to scale $\theta$ and $\theta_0$ correctly for maximum margin.
    
- **Miscomputing Hinge Loss:**
    
    Not applying the max function properly or missing the correct margin.
    
- **Order Sensitivity in Perceptron:**
    
    Assuming the order affects the final separator instead of just the number of updates.
    
- **Notation Errors:**
    
    Using incorrect symbols or formats, leading to incorrect interpretations.
    
- **Misapplying Kernel Functions:**
    
    Incorrectly defining or applying the kernel function relative to the feature map.
    
- **Improper Learning Rate Selection in SGD:**
    - **Too Large $\eta$:** May cause overshooting and divergence.
    - **Too Small $\eta$:** May lead to slow convergence.
- **Ignoring Regularization in SGD:**
    
    Neglecting the impact of the regularization term $\lambda$ on the update rules.
    
- **Weight Initialization Errors in Neural Networks:**
    
    Initializing weights too large or too small can hinder training effectiveness.
    
- **Confusion Between Convolutional and Fully Connected Layers:**
    
    Misunderstanding their roles and advantages can lead to suboptimal network architectures.
    

## **8. Summary**

This comprehensive cheatsheet covers essential concepts in linear classification, kernel methods, stochastic gradient descent (SGD), and neural networks. Key areas include:

- **Linear Classification:**
    
    Understanding the perceptron algorithm, maximum margin separators (SVM), margin calculation, and hinge loss.
    
- **Kernel Methods:**
    
    Utilizing feature maps, kernel functions (e.g., quadratic kernel), the kernel trick, and the kernel perceptron algorithm to handle non-linearly separable data.
    
- **Stochastic Gradient Descent (SGD):**
    
    Optimizing the SVM objective function using SGD, understanding gradient computations for hinge loss, and applying update rules with regularization.
    
- **Neural Networks:**
    
    Exploring two-layer feed-forward networks with ReLU units, mapping input regions to activation regions, the impact of adding layers or hidden units, backpropagation, and the advantages of convolutional layers over fully connected layers.
    

**Key Takeaways:**

- **Perceptron vs. SVM:**
    
    The perceptron algorithm is suitable for linearly separable data, while SVMs aim to maximize the margin for better generalization.
    
- **Kernel Trick:**
    
    Enables efficient computation in higher-dimensional spaces without explicit feature mapping, allowing for flexible decision boundaries.
    
- **SGD for SVM:**
    
    A scalable optimization technique that updates parameters incrementally, balancing hinge loss minimization and regularization to prevent overfitting.
    
- **Neural Network Architecture Choices:**
    - **Convolutional Layers:**
        - Share weights, reducing parameters.
        - Recognize features regardless of location.
    - **Fully Connected Layers:**
        - Higher parameter count.
        - Limited spatial generalization.