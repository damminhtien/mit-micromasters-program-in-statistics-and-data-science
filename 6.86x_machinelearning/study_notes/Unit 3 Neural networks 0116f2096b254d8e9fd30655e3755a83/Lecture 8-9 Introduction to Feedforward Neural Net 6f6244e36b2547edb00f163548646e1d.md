# Lecture 8-9: Introduction to Feedforward Neural Networks

# **Introduction to Feedforward Neural Networks**

At the end of this lecture, you will be able to

- Recognize different **layers** in a **feedforward neural network** and the number of **units** in each layer.
- Write down common **activation functions** such as the hyperbolic tangent function $\tanh$, and the **rectified linear function (ReLU)** .
- Compute the output of a simple neural network possibly with **hidden layers** given the **weights** and **activation functions** .
- Determine whether data after transformation by some layers is linearly separable, draw decision boundaries given by the weight vectors and use them to help understand the behavior of the network.

# **Motivation to Neural Networks**

So far, the ways we have performed non-linear classification involve either first mapping $x$ explicitly into some feature vectors $\phi (x)$, whose coordinates involve non-linear functions of $x$ or in order to increase computational efficiency, rewriting the decision rule in terms of a chosen kernel, i.e. the dot product of feature vectors, and then using the training data to learn a transformed classification parameter.

However, in both cases, the feature vectors are **chosen** . They are not learned in order to improve performance of the classification problem at hand.

Neural networks, on the other hand, are models in which the feature representation is learned jointly with the classifier to improve classification performance.

# **Neural Network Units**

A **neural network unit** is a primitive neural network that consists of only the “input layer", and an output layer with only one output. It is represented pictorially as follows:

![Untitled](Lecture%208-9%20Introduction%20to%20Feedforward%20Neural%20Net%206f6244e36b2547edb00f163548646e1d/Untitled.png)

A neural network unit computes a non-linear weighted combination of its input:

$$
\displaystyle \displaystyle \hat{y}\displaystyle =\displaystyle f(z)\quad \text {where } z= w_0 + \sum _{i=1}^ d x_ i w_ i
$$

where $w_i$ are numbers called **weights** , $z$ is a number and is the weighted sum of the inputs $x_ i$, and $f$ is generally a non-linear function called the **activation function** .

The above equation in vector form is:

$$
\displaystyle \displaystyle \hat{y}\displaystyle =\displaystyle f(z)\quad \text {where } z= w_0 + x\cdot w,
$$

where $x=[x_1,\ldots ,x_ d] and w=[w_1,\ldots ,w_ d]^ T$.

The **hyperbolic tangent function** is defined as

$$

\displaystyle \displaystyle \tanh (z)\displaystyle =\displaystyle \frac{e^{z}-e^{-z}}{e^{z}+e^{-z}}=1-\frac{2}{e^{2z}+1}.

$$

# **Introduction to Deep Neural Networks**

A **deep (feedforward) neural network** refers to a neural network that contains not only the input and output layers, but also hidden layers in between. For example, below is a deep feedfoward neural network of 2 hidden layers, with each hidden layer consisting of 5 units:

![](https://courses.edx.org/assets/courseware/v1/0486df10c4615b12bb59dbcce54caa5e/asset-v1:MITx+6.86x+2T2024+type@asset+block/images_lec8_deepneuralnet.svg)

One of the main advantages of deep neural networks is that in many cases, they can learn to extract very complex and sophisticated features from just the raw features presented to them as their input. For instance, in the context of image recognition, neural networks can extract the features that differentiate a cat from a dog based only on the raw pixel data presented to them from images.

The initial few layers of a neural networks typically capture the simpler and smaller features whereas the later layers use information from these low-level features to identify more complex and sophisticated features.

Using the NAND function only as the basic neural network unit, we can build larger neural networks to implement other logic functions.

# **Back-propagation Algorithm**

Once we set up the architecture of our (feedforward) neural network, our goal will be to find weight parameters that minimize our loss function. We will use the **stochastic gradient descent algorithm** (which you learned in [Lecture 4](https://courses.edx.org/courses/course-v1:MITx+6.86x+2T2024/courseware/Unit_1_Linear_Classifiers_and_Generalizations__2_weeks_/lec4_linear_classification_and_generalization/5) and revisited in [lecture 5](https://courses.edx.org/courses/course-v1:MITx+6.86x+2T2024/courseware/unit_2/lec5_linear_regression/5)) to carry out the optimization.

This involves computing the gradient of the loss function with respect to the weight parameters.

Since the loss function is a long chain of compositions of activation functions with the weight parameters entering at different stages, we will break down the computation of the gradient into different pieces via the chain rule; this way of computing the gradient is called the back-propagation algorithm.

In the following problems, we will explore the main step in the stochastic gradient descent algorithm for training the following simple neural network from the video:

![](https://courses.edx.org/assets/courseware/v1/11b35752e19f6465e3f4edb926985e2f/asset-v1:MITx+6.86x+2T2024+type@asset+block/images_l7_p4.png)

This simple neural network is made up of $L$ hidden layers, but each layer consists of only one unit, and each unit has activation function $f$.

As usual, $x$ is the input, $z_ i$ is the weighted combination of the inputs to the $i^{th}$ hidden layer. In this one-dimensional case, weighted combination reduces to products:

$$
\displaystyle \displaystyle z_1\displaystyle =\displaystyle xw_1
$$

$$
\displaystyle \text {for } i=2\ldots L:\quad z_ i\displaystyle =\displaystyle f_{i-1} w_ i \quad \text {where }\, f_{i-1} \, = \, f(z_{i-1}).
$$

We will use the following loss function:

$$
\displaystyle \displaystyle \mathcal{L}(y, f_ L) = (y - f_ L)^2
$$

where $y$ is the true value, and $f_ L$ is the output of the neural network.

## Gradient Descent Update

Let $\eta$ be the learning rate for the stochastic gradient descent algorithm.

Recall that our goal is to tune the parameters of the neural network so as to minimize the loss function. 

The appropriate update rule for the parameter $w_1$ in the stochastic gradient descent algorithm is determined by how the algorithm aims to minimize the loss function $\mathcal{L}(y, f_L)$.

In stochastic gradient descent, the parameters are updated in the direction that reduces the loss function. This is achieved by subtracting the gradient of the loss function with respect to the parameter from the current parameter value, scaled by the learning rate $\eta$. The gradient $\nabla_{w_1} \mathcal{L}(y, f_L)$ indicates the direction of the steepest ascent, so to minimize the loss, we move in the opposite direction.

The appropriate update rule for the parameter $w_1$ is:

$$
w_1 \leftarrow w_1 - \eta \cdot \nabla_{w_1} \mathcal{L}(y, f_L)
$$