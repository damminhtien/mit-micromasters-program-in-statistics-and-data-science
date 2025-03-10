# Lecture 12: Convolutional Neural networks

**Convolutional neural networks (CNNs)**

At the end of this lecture, you will be able to

- Know the differences between feed-forward and Convolutional neural networks (CNNs).
- Implement the key parts in the CNNs, including **convolution** , **max pooling** units.
- Determine the dimension of each channel in different layers with a given CNNs.

The math for training updates to fancy models like CNNs or Transformers isn't fundamentally different from the math for training updates to linear models. Both are gradient descent. For each training example, we view training loss as a function of weights. If we fix all the entries in our weights except one, then we get 1D output (training loss) depending on a 1D input (value for the one entry in our weights that we didn't fix). This can be a horribly complicated function, as in the case of CNNs, but it is made of very simple parts like addition, multiplication, and Relu. It is only complicated because it is a composition of many simple parts, and it is still a 1D to 1D function. So we can use ordinary calculus to compute that derivative. We may do this for each weight entry individually to define our gradient update.

Back propagation is just an organized system for doing that ordinary calculus without working too hard. But there is no fundamentally new ingredient. If you ever get confused about what the right gradients should be, just go back to the 1D to 1D calculus and that'll tell you the right answer.

## Differences Between Feed-Forward Neural Networks and Convolutional Neural Networks (CNNs)

### **1. Architecture**

**Feed-Forward Neural Networks (FFNNs)**:

- **Structure**: Consists of fully connected layers where each neuron in one layer is connected to every neuron in the next layer.
- **Layers**: Typically have an input layer, one or more hidden layers, and an output layer.
- **Connections**: All neurons in a layer are connected to all neurons in the next layer, resulting in a dense network of connections.

**Convolutional Neural Networks (CNNs)**:

- **Structure**: Consists of convolutional layers, pooling layers, and fully connected layers.
- **Layers**:
    - **Convolutional Layers**: Use filters (kernels) to perform convolution operations on the input, detecting local patterns.
    - **Pooling Layers**: Reduce the spatial dimensions of the data, usually by taking the maximum (max pooling) or average (average pooling) value in a window.
    - **Fully Connected Layers**: Similar to those in FFNNs, used at the end of the network for classification or regression.
- **Connections**: Neurons in a convolutional layer are only connected to a local region of the input, reducing the number of connections.

### **2. Data Handling**

**Feed-Forward Neural Networks (FFNNs)**:

- **Data Type**: Primarily handle one-dimensional structured data.
- **Input Representation**: Inputs are typically flattened into a one-dimensional vector, regardless of the original shape (e.g., an image).

**Convolutional Neural Networks (CNNs)**:

- **Data Type**: Designed to handle two-dimensional and three-dimensional spatial data, such as images and videos.
- **Input Representation**: Inputs are kept in their original shape (e.g., a 2D image or a 3D volume) to preserve spatial relationships.

### **3. Parameters and Computational Efficiency**

**Feed-Forward Neural Networks (FFNNs)**:

- **Parameters**: Have a large number of parameters due to the fully connected nature of the layers, leading to high computational cost and risk of overfitting.
- **Efficiency**: Less efficient for high-dimensional inputs like images due to the large number of parameters.

**Convolutional Neural Networks (CNNs)**:

- **Parameters**: Use shared weights (filters), significantly reducing the number of parameters compared to FFNNs.
- **Efficiency**: More efficient for high-dimensional inputs, as the convolution operation is computationally cheaper and leverages local patterns in the data.

### **4. Feature Extraction**

**Feed-Forward Neural Networks (FFNNs)**:

- **Feature Extraction**: No built-in mechanism for feature extraction; relies on the network learning relevant features through the fully connected layers.
- **Spatial Hierarchies**: Cannot inherently detect spatial hierarchies or local patterns in the data.

**Convolutional Neural Networks (CNNs)**:

- **Feature Extraction**: Convolutional layers automatically extract local features such as edges, textures, and shapes.
- **Spatial Hierarchies**: Capable of detecting spatial hierarchies of features, from low-level (edges) to high-level (objects) patterns.

### **5. Use Cases**

**Feed-Forward Neural Networks (FFNNs)**:

- **Applications**: Suitable for tasks with structured data, such as tabular data, time series prediction, and simple pattern recognition.
- **Limitations**: Less effective for image and spatial data processing.

**Convolutional Neural Networks (CNNs)**:

- **Applications**: Highly effective for image and spatial data processing, including tasks like image classification, object detection, and segmentation.
- **Advantages**: Superior performance on tasks involving spatial hierarchies and local pattern recognition.

### **Detailed Example: Image Classification**

**Feed-Forward Neural Networks (FFNNs)**:

- For an image classification task, an FFNN would first flatten the image into a one-dimensional vector, losing the spatial information.
- For example, a $28 \times 28$ pixel image (e.g., from MNIST dataset) would be flattened into a 784-dimensional vector before being passed through the network.

**Convolutional Neural Networks (CNNs)**:

- For the same image classification task, a CNN would retain the $28 \times 28$ pixel structure of the image.
- The convolutional layers would apply filters to detect edges, textures, and other features, followed by pooling layers to reduce the dimensionality, and finally fully connected layers for classification.

**Example CNN Architecture**:

1. **Input Layer**: $28 \times 28 \times 1$ (grayscale image)
2. **Convolutional Layer**: Apply 32 filters of size $3 \times 3$, output shape $26 \times 26 \times 32$
3. **Pooling Layer**: $2 \times 2$ max pooling, output shape $13 \times 13 \times 32$
4. **Convolutional Layer**: Apply 64 filters of size $3 \times 3$, output shape $11 \times 11 \times 64$
5. **Pooling Layer**: $2 \times 2$ max pooling, output shape $5 \times 5 \times 64$
6. **Fully Connected Layer**: Flatten to 1600 units, connected to a dense layer with 128 neurons
7. **Output Layer**: Dense layer with 10 neurons for classification (e.g., 10 digits in MNIST)

In summary, while both feed-forward neural networks and convolutional neural networks are powerful tools for various machine learning tasks, CNNs are specifically designed to handle spatial data more effectively through local connectivity, weight sharing, and efficient feature extraction, making them ideal for tasks such as image and video processing.

## Convolution

### Continuous Convolution

**Definition**:

- Continuous convolution is an integral that expresses the amount of overlap of one function $f$ as it is shifted over another function $g$.
- The continuous convolution of two functions $f(t)$ and $g(t)$ is defined as: $(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau$

**Key Points**:

1. **Integration**: The integral computes the area under the product of the two functions as one is shifted over the other.
2. **Signal Processing**: Widely used in signal processing for filtering signals.
3. **Properties**:
    - **Commutative**: $f * g = g * f$
    - **Associative**: $f * (g * h) = (f * g) * h$
    - **Distributive**: $f * (g + h) = (f * g) + (f * h)$
4. **Applications**:
    - Used in solving differential equations.
    - Applies in physics for systems response analysis.

### Discrete Convolution

**Definition**:

- Discrete convolution is a sum that represents the amount of overlap between two discrete signals as one is shifted over the other.
- The discrete convolution of two sequences \( f[n] \) and \( g[n] \) is defined as:
\[
(f * g)[n] = \sum_{m=-\infty}^{\infty} f[m] g[n - m]
\]

**Key Points**:

1. **Summation**: The summation computes the total product of the two sequences as one is shifted over the other.
2. **Signal Processing**: Commonly used in digital signal processing for filtering discrete signals.
3. **Properties**:
    - **Commutative**: \( f * g = g * f \)
    - **Associative**: \( f * (g * h) = (f * g) * h \)
    - **Distributive**: \( f * (g + h) = (f * g) + (f * h) \)
4. **Implementation**:
    - Used in algorithms for image and audio processing.
    - Basis for convolutional neural networks (CNNs) in deep learning.

### Transition from Continuous to Discrete Convolution

1. **Sampling**:
    - Continuous signals are sampled at discrete intervals to create discrete signals.
    - The continuous integral is replaced by a discrete sum.
2. **Applications in Digital Systems**:
    - Continuous systems modeled by differential equations translate to difference equations in discrete systems.
    - Discrete convolution allows for practical implementations in digital computing.
3. **Practical Computation**:
    - Discrete convolution is easier to compute using digital computers compared to continuous convolution which requires numerical integration.
    - Efficient algorithms like the Fast Fourier Transform (FFT) facilitate rapid computation of discrete convolutions.

### Example: Convolution on 2D Discrete Signals

**Given**:

- Input image \( f \):
\[
f = \begin{bmatrix}
1 & 2 & 1 \\
2 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
\]
- Filter \( g' \):
\[
g' = \begin{bmatrix}
1 & 0.5 \\
0.5 & 1
\end{bmatrix}
\]

**Convolution Calculation**:

- Slide the filter over the image and compute the dot product at each valid position.

**Resulting Output**:
\[
h = \begin{bmatrix}
4 & 4 \\
4 & 3
\end{bmatrix}
\]

- Sum of elements in the output matrix:
\[
\text{Sum} = 4 + 4 + 4 + 3 = 15
\]

### Python Code for 2D Convolution:

```python
import numpy as np

def convolution_2d(f, g):
    """
    Perform 2D convolution without zero padding.
    Parameters:
    f (np.array): Input 2D signal (image)
    g (np.array): 2D Filter (kernel)

    Returns:
    np.array: Convolution result
    """
    f = np.array(f)
    g = np.array(g)

    # Get dimensions
    f_rows, f_cols = f.shape
    g_rows, g_cols = g.shape

    # Calculate the dimensions of the output
    output_rows = f_rows - g_rows + 1
    output_cols = f_cols - g_cols + 1

    # Initialize the output matrix
    output = np.zeros((output_rows, output_cols))

    # Perform the convolution
    for i in range(output_rows):
        for j in range(output_cols):
            output[i, j] = np.sum(f[i:i+g_rows, j:j+g_cols] * g)

    return output

# Input image
f = np.array([
    [1, 2, 1],
    [2, 1, 1],
    [1, 1, 1]
])

# Filter (kernel)
g = np.array([
    [1, 0.5],
    [0.5, 1]
])

# Perform convolution without zero padding
output = convolution_2d(f, g)
print("Convolution result without zero padding:")
print(output)

# Calculate the sum of the elements in the output matrix
sum_of_elements = np.sum(output)
print("Sum of the elements in the output matrix:", sum_of_elements)

```

### Key Takeaways

- Both continuous and discrete convolutions are essential in different fields of signal processing.
- Continuous convolution deals with integrals, while discrete convolution deals with summations.
- Discrete convolution is particularly crucial in digital signal processing and forms the backbone of convolutional neural networks used in deep learning.
- Understanding the transition from continuous to discrete convolution is important for practical implementations in computing and engineering.

## Pooling Layer in Convolutional Neural Networks (CNNs)

The pooling layer is a critical component of Convolutional Neural Networks (CNNs) used primarily for down-sampling or reducing the dimensions of feature maps while retaining important spatial features. This process helps in reducing the computational load, controlling overfitting, and providing some degree of translation invariance.

### **Types of Pooling**

1. **Max Pooling**
2. **Average Pooling**

### **Max Pooling**

**Operation**:

- Max pooling operates by dividing the input into distinct rectangular regions and taking the maximum value from each region.
- This helps in retaining the most prominent features within each region, making the network more robust to small changes and distortions.

**Example**:

- Consider a \(4 \times 4\) input matrix with a \(2 \times 2\) pooling window and a stride of 2:
\[
\text{Input} = \begin{bmatrix}
1 & 3 & 2 & 4 \\
5 & 6 & 7 & 8 \\
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8
\end{bmatrix}
\]
- Max pooling with a \(2 \times 2\) window and stride 2:
\[
\text{Output} = \begin{bmatrix}
6 & 8 \\
6 & 8
\end{bmatrix}
\]
- Here, the maximum values from each \(2 \times 2\) region are selected.

### **Average Pooling**

**Operation**:

- Average pooling works by dividing the input into distinct rectangular regions and computing the average value from each region.
- This method smoothens the feature map, reducing the effect of minor fluctuations and noise.

**Example**:

- Using the same \(4 \times 4\) input matrix with a \(2 \times 2\) pooling window and a stride of 2:
\[
\text{Input} = \begin{bmatrix}
1 & 3 & 2 & 4 \\
5 & 6 & 7 & 8 \\
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8
\end{bmatrix}
\]
- Average pooling with a \(2 \times 2\) window and stride 2:
\[
\text{Output} = \begin{bmatrix}
3.75 & 5.25 \\
3.5 & 5.5
\end{bmatrix}
\]
- Here, the average values from each \(2 \times 2\) region are computed.

### **Key Properties of Pooling Layers**

1. **Down-Sampling**:
    - Pooling layers reduce the spatial dimensions (width and height) of the input feature maps, which decreases the computational complexity and the number of parameters.
    - Example: A \(32 \times 32\) feature map down-sampled by a \(2 \times 2\) pooling layer with a stride of 2 results in a \(16 \times 16\) feature map.
2. **Translation Invariance**:
    - Pooling provides a degree of translation invariance, meaning the network can recognize features even when they are slightly shifted or distorted.
    - This property is crucial for tasks like image recognition where the exact position of features may vary.
3. **Control Overfitting**:
    - By reducing the size of the feature maps, pooling layers help control overfitting. Smaller feature maps reduce the risk of the network learning noise and irrelevant details.

### **Example in a CNN Architecture**

Consider a CNN for image classification with an input size of \(32 \times 32 \times 3\) (RGB image). A typical architecture might include:

1. **Convolutional Layer**:
    - Applies 64 filters of size \(3 \times 3\)
    - Output shape: \(32 \times 32 \times 64\)
2. **Pooling Layer**:
    - Max pooling with a \(2 \times 2\) window and stride 2
    - Output shape: \(16 \times 16 \times 64\)
3. **Another Convolutional Layer**:
    - Applies 128 filters of size \(3 \times 3\)
    - Output shape: \(16 \times 16 \times 128\)
4. **Another Pooling Layer**:
    - Max pooling with a \(2 \times 2\) window and stride 2
    - Output shape: \(8 \times 8 \times 128\)

The pooling layers in this architecture progressively reduce the spatial dimensions of the feature maps, making the network more efficient while preserving the most critical information.

### **Summary**

Pooling layers in CNNs are essential for reducing the spatial dimensions of feature maps while retaining important information. They help in making the network more computationally efficient, providing translation invariance, and controlling overfitting. Max pooling and average pooling are the most common types, with max pooling being more popular due to its ability to capture the most prominent features in each region.

## Understanding Gradient Descent and Backpropagation in Complex Models

### **Gradient Descent (GD)**

**Fundamentals**:

- Gradient Descent is an optimization algorithm used to minimize the loss function in machine learning models.
- The key idea is to iteratively adjust the model's weights in the direction of the steepest decrease in the loss function.
- For each weight \( w_i \), the update rule is:
\[
w_i := w_i - \eta \frac{\partial L}{\partial w_i}
\]
where \( \eta \) is the learning rate and \( \frac{\partial L}{\partial w_i} \) is the partial derivative of the loss \( L \) with respect to \( w_i \).

### **Training Loss as a Function of Weights**

**1D to 1D Function**:

- For each training example, we view the training loss as a function of the model's weights.
- If we fix all weights except one, the loss becomes a function of a single variable (the unfixed weight), transforming a multi-dimensional problem into a 1D problem.
- Despite the complexity of CNNs or Transformers, this simplification allows us to use ordinary 1D calculus to compute derivatives.

**Ordinary Calculus**:

- The function can be complicated, involving operations like addition, multiplication, and activation functions (e.g., ReLU).
- The derivative of this 1D function with respect to the single weight can be computed using standard calculus rules.
- By computing this derivative for each weight, we define the gradient update for the entire model.

### **Backpropagation**

**Concept**:

- Backpropagation is an algorithm used to efficiently compute the gradients of the loss function with respect to each weight in a neural network.
- It applies the chain rule of calculus to propagate the gradient backward through the network from the output layer to the input layer.

**Steps**:

1. **Forward Pass**: Compute the output of the network and the loss.
2. **Backward Pass**: Compute the gradients of the loss with respect to each weight using the chain rule.

**Mathematical Basis**:

- Consider a neural network with an output \( y \) that depends on weights \( w_1, w_2, \ldots, w_n \).
- The loss \( L \) is a function of the output \( y \):
\[
L = f(y)
\]
- Using the chain rule, the gradient of \( L \) with respect to each weight \( w_i \) is:
\[
\frac{\partial L}{\partial w_i} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial w_i}
\]

**Organized System**:

- Backpropagation systematically applies these derivatives layer by layer, from the output to the input.
- For each layer, it computes the gradient of the loss with respect to the weights in that layer, using the gradients from the subsequent layer.

### **Gradient Descent in CNNs and Transformers**

**Convolutional Neural Networks (CNNs)**:

- CNNs use layers that perform convolution operations, followed by non-linear activation functions and pooling layers.
- The loss function still depends on the weights of the filters in the convolutional layers.
- Backpropagation in CNNs involves computing the gradients of the loss with respect to these filter weights and updating them using gradient descent.

**Transformers**:

- Transformers consist of attention mechanisms and feed-forward networks, used primarily for sequence-to-sequence tasks.
- The loss function depends on the weights in the attention layers and the feed-forward layers.
- Backpropagation in Transformers involves computing the gradients of the loss with respect to these weights and updating them using gradient descent.

### **Visualizing Gradient Descent**

**Illustrative Cartoons**:

- Visualizations of gradient descent can help in understanding the shared thread across different models, despite the varying complexities.
- These visualizations typically represent the iterative process of weight updates in a simplified manner, focusing on the core principle of minimizing the loss function.

**Bird's Eye View**:

- At a high level, the process of gradient descent in any neural network involves:
    1. Computing the forward pass to get the output and loss.
    2. Performing the backward pass to compute gradients.
    3. Updating the weights using the gradients.

**Takeaway**:

- The underlying mathematics of gradient descent and backpropagation are consistent across different models, whether simple linear models or complex structures like CNNs and Transformers.
- By understanding these fundamental principles, one can apply them to various neural network architectures, leveraging their strengths for specific tasks.

### Summary

1. **Gradient Descent**:
    - Iterative optimization algorithm for minimizing the loss function.
    - Updates weights by moving in the direction of the negative gradient.
2. **Training Loss as a Function of Weights**:
    - Simplifies the multi-dimensional problem to a 1D problem by fixing all but one weight.
    - Allows the use of ordinary calculus to compute derivatives.
3. **Backpropagation**:
    - Efficiently computes gradients using the chain rule.
    - Propagates gradients from the output layer back to the input layer.
4. **CNNs and Transformers**:
    - Both use gradient descent and backpropagation, despite their complex architectures.
    - The core principles remain the same, involving forward passes, loss computation, backward passes, and weight updates.

Understanding these concepts provides a strong foundation for working with various neural network models and optimizing their performance through gradient descent.

## Example of a CNN

Let's compute the output of the CNN for the given input image \( I \) and filter \( F \).

### Given:

- **Input Image \( I \)**:
\[
I = \begin{bmatrix}
1 & 0 & 2 \\
3 & 1 & 0 \\
0 & 0 & 4
\end{bmatrix}
\]
- **Filter \( F \)**:
\[
F = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\]

### Steps to Compute the Output

1. **Convolution**:
2. **ReLU Activation**:
3. **Max Pooling**:

### 1. Convolution

The convolution operation involves sliding the filter over the input image and computing the dot product at each valid position. The stride is 1, so the filter moves one step at a time.

**Convolution Calculation**:
\[
\begin{aligned}
&\text{Output}[0, 0] = (1 \cdot 1) + (0 \cdot 0) + (3 \cdot 0) + (1 \cdot 1) = 1 + 0 + 0 + 1 = 2 \\
&\text{Output}[0, 1] = (0 \cdot 1) + (2 \cdot 0) + (1 \cdot 0) + (0 \cdot 1) = 0 + 0 + 0 + 0 = 0 \\
&\text{Output}[1, 0] = (3 \cdot 1) + (1 \cdot 0) + (0 \cdot 0) + (0 \cdot 1) = 3 + 0 + 0 + 0 = 3 \\
&\text{Output}[1, 1] = (1 \cdot 1) + (0 \cdot 0) + (0 \cdot 0) + (4 \cdot 1) = 1 + 0 + 0 + 4 = 5 \\
\end{aligned}
\]

So, the convolution result is:
\[
\text{Conv}(I) = \begin{bmatrix}
2 & 0 \\
3 & 5
\end{bmatrix}
\]

### 2. ReLU Activation

Apply the ReLU activation function to the convolution output:
\[
\text{ReLU}(x) = \max(0, x)
\]

Applying ReLU:
\[
\text{ReLU}(\text{Conv}(I)) = \begin{bmatrix}
\max(0, 2) & \max(0, 0) \\
\max(0, 3) & \max(0, 5)
\end{bmatrix} = \begin{bmatrix}
2 & 0 \\
3 & 5
\end{bmatrix}
\]

### 3. Max Pooling

Perform max pooling with a \(2 \times 2\) window and stride 1. However, since the size of the result from ReLU is \(2 \times 2\), max pooling over the entire \(2 \times 2\) matrix results in a single value, which is the maximum value in the matrix.

**Max Pooling Calculation**:
\[
\text{Max Pool}(\text{ReLU}(\text{Conv}(I))) = \max\left(\begin{bmatrix}
2 & 0 \\
3 & 5
\end{bmatrix}\right) = 5
\]

### Final Answer

The output of the CNN is:
\[ 5 \]