# Lecture 10-11: Recurrent neural networks (RNNs)

# **Introduction to recurrent neural networks (RNNs)**

At the end of this lecture, you will be able to

- Know the difference between feed-forward and recurrent neural networks(RNNs).
- Understand the role of **gating** and **memory cells** in long-short term memory (LSTM).
- Understand the process of **encoding** of RNNs in modeling sequences.

An inconvenient aspect of feed-forward networks is that we have to manually engineer how history is mapped to a feature vector (representation). However, in fact, this mapping into feature vectors (encoding) is also what we would like to learn. RNN's learn the encoding into a feature vector, unlike feed-forward networks.

## Recurrent Neural Networks (RNNs)

**RNNs** are a class of neural networks designed to handle sequential data. Unlike traditional feedforward neural networks, RNNs have connections that loop back on themselves, allowing information to persist across different time steps. This makes them particularly useful for tasks where the order of inputs is crucial, such as time series analysis, language modeling, and sequence prediction.

### Explanation of the RNN

![Untitled](Lecture%2010-11%20Recurrent%20neural%20networks%20(RNNs)%204c8f90021bb5427c9d4ff4fd2c8aa223/Untitled.png)

The image illustrates the update mechanism in an RNN. It shows the transition from one state (or context) to a new state based on new information:

1. **Context or State ($s_{t-1}$):**
    - This represents the hidden state of the RNN at time step $t-1$. The hidden state carries information about the sequence up to time step $t-1$.
2. **New Information ($x_t$):**
    - This represents the input at the current time step $t$.
3. **Update Function ($\theta$):**
    - This is typically a non-linear function (such as \(\tanh\) or \(\text{ReLU}\)) that combines the previous hidden state and the current input to produce the new hidden state.
4. **New Context or State (\(s_t\)):**
    - This represents the updated hidden state at time step \(t\).

### The Equation

\[ s_t = \tanh(W^{s,s}s_{t-1} + W^{s,x}x_t) \]

Let's break down the equation:

1. **\(s_t\):**
    - The hidden state at time step \(t\).
2. **\(\tanh\):**
    - The hyperbolic tangent activation function, which introduces non-linearity into the model. It ensures that the output values are within the range of -1 to 1.
3. **\(W^{s,s}\):**
    - The weight matrix that connects the previous hidden state \(s_{t-1}\) to the current hidden state \(s_t\). It determines how much influence the previous state has on the current state.
4. **\(W^{s,x}\):**
    - The weight matrix that connects the input \(x_t\) at the current time step to the hidden state \(s_t\). It determines how much influence the current input has on the current state.
5. **\(s_{t-1}\):**
    - The hidden state at the previous time step \(t-1\).
6. **\(x_t\):**
    - The input at the current time step \(t\).

### How It Works

1. **Initialization:**
    - At the initial time step \(t=0\), the hidden state \(s_0\) is typically initialized to a vector of zeros or some other initial value.
2. **State Update:**
    - At each time step \(t\), the RNN updates its hidden state \(s_t\) using the current input \(x_t\) and the previous hidden state \(s_{t-1}\). The update is performed using the given equation.
3. **Non-linear Transformation:**
    - The combined linear transformation \(W^{s,s}s_{t-1} + W^{s,x}x_t\) is passed through the \(\tanh\) activation function to introduce non-linearity and keep the values in a manageable range.
4. **Sequence Processing:**
    - This process is repeated for each time step in the sequence, allowing the RNN to capture information from the entire sequence and update its hidden state accordingly.

RNNs use recurrent connections to maintain a hidden state that evolves over time, capturing information from previous time steps. The equation \( s_t = \tanh(W^{s,s}s_{t-1} + W^{s,x}x_t) \) represents how the hidden state is updated at each time step using the previous hidden state and the current input. The weights \(W^{s,s}\) and \(W^{s,x}\) determine how the previous state and current input influence the new state, respectively.

## Long Short-Term Memory (LSTM) Networks

Long Short-Term Memory (LSTM) networks are a special kind of Recurrent Neural Network (RNN) capable of learning long-term dependencies. They are designed to overcome the limitations of traditional RNNs, particularly the vanishing gradient problem, by using a more sophisticated architecture. LSTMs are well-suited for tasks involving sequences of data, such as time series forecasting, language modeling, and speech recognition.

### LSTM Architecture

An LSTM network consists of cells, each containing four interacting components: the cell state (\(c_t\)), and three gates: the input gate (\(i_t\)), the forget gate (\(f_t\)), and the output gate (\(o_t\)). These gates control the flow of information into and out of the cell state, thereby allowing the network to retain or forget information as needed.

The provided image shows the LSTM equations and their components:

1. **Forget Gate (\(f_t\)):**
\[
f_t = \sigma(W^{f,h} h_{t-1} + W^{f,x} x_t)
\]
The forget gate determines which information from the previous cell state \(c_{t-1}\) should be discarded. It takes the previous hidden state \(h_{t-1}\) and the current input \(x_t\) as inputs, and applies a sigmoid activation function to output a value between 0 and 1.
2. **Input Gate (\(i_t\)):**
\[
i_t = \sigma(W^{i,h} h_{t-1} + W^{i,x} x_t)
\]
The input gate controls which new information is added to the cell state. It also takes \(h_{t-1}\) and \(x_t\) as inputs, and applies a sigmoid activation function.
3. **Output Gate (\(o_t\)):**
\[
o_t = \sigma(W^{o,h} h_{t-1} + W^{o,x} x_t)
\]
The output gate determines what information from the cell state will be outputted to the next hidden state. It uses \(h_{t-1}\) and \(x_t\) as inputs, and applies a sigmoid activation function.
4. **Cell State (\(c_t\)):**
\[
c_t = f_t \odot c_{t-1} + i_t \odot \tanh(W^{c,h} h_{t-1} + W^{c,x} x_t)
\]
The cell state is updated using the forget gate to discard some information from the previous cell state \(c_{t-1}\) and the input gate to add new information. The new information is created by applying the \(\tanh\) function to a weighted combination of \(h_{t-1}\) and \(x_t\), and then combining this with the input gate's output.
5. **Hidden State (\(h_t\)):**
\[
h_t = o_t \odot \tanh(c_t)
\]
The hidden state is updated using the output gate and the cell state. The cell state \(c_t\) is passed through a \(\tanh\) function to ensure the values are between -1 and 1, and then combined with the output gate's output.

```python
import numpy as np

# Define the activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

# Given values
W_f_h = W_f_x = 1
W_i_h = W_i_x = 1
W_o_h = W_o_x = 1
W_c_h = W_c_x = 1
h_t_minus_1 = 1
c_t_minus_1 = 1
x_t = 5

# Forget gate
f_t = sigmoid(W_f_h * h_t_minus_1 + W_f_x * x_t)
# Input gate
i_t = sigmoid(W_i_h * h_t_minus_1 + W_i_x * x_t)
# Output gate
o_t = sigmoid(W_o_h * h_t_minus_1 + W_o_x * x_t)
# New cell state candidate
c_tilde_t = tanh(W_c_h * h_t_minus_1 + W_c_x * x_t)
# New cell state
c_t = f_t * c_t_minus_1 + i_t * c_tilde_t
# New hidden state
h_t = o_t * tanh(c_t)

# Round sigmoid to 1 or 0, and tanh to -1 or 1
f_t_rounded = round(f_t)
i_t_rounded = round(i_t)
o_t_rounded = round(o_t)
c_tilde_t_rounded = round(c_tilde_t)

c_t_rounded = f_t_rounded * c_t_minus_1 + i_t_rounded * c_tilde_t_rounded
h_t_rounded = o_t_rounded * round(tanh(c_t_rounded))

f_t_rounded, i_t_rounded, o_t_rounded, c_t_rounded, h_t_rounded
```

# **From Markov model to recurrent neural networks (RNNs)**

At the end of this lecture, you will be able to

- Formulate, estimate and sample sequences from Markov models.
- Understand the relation between RNNs and Markov model for generating sequences.
- Understand the process of **decoding** of RNN in generating sequences.

### Markov Language Model

A Markov Language Model is a type of probabilistic model that is used to predict the next word in a sequence based on the previous words. It relies on the Markov property, which states that the probability of a word depends only on a fixed number of preceding words. This simplifies the modeling of sequential data by considering a limited context.

### Key Concepts

1. **Markov Property:**
    - The Markov property assumes that the future state (word) depends only on the current state (word) or a fixed number of previous states (words), not on the entire sequence history.
2. **Order of Markov Model:**
    - **First-Order Markov Model:** Considers only the immediately preceding word to predict the next word.
    - **Higher-Order Markov Models:** Consider \(n\) preceding words to predict the next word (e.g., bigrams for second-order, trigrams for third-order).

### Components of a Markov Language Model

1. **States:** In the context of language models, states represent words or tokens in the vocabulary.
2. **Transition Probabilities:** These are the probabilities of moving from one state (word) to another. In a first-order Markov model, this is represented as \(P(w_i | w_{i-1})\), where \(w_i\) is the current word and \(w_{i-1}\) is the previous word.
3. **Initial Probabilities:** These are the probabilities of starting with a particular word.

### Transition Probability Matrix

A transition probability matrix captures the probabilities of transitioning from one word to another. Each cell \((i, j)\) in the matrix represents the probability \(P(w_j | w_i)\), the probability of word \(w_j\) following word \(w_i\).

### Example: First-Order Markov Model

Given a sequence of words and their transition probabilities, we can calculate the probability of generating a specific sequence.

### Transition Probability Table

The table below illustrates the transition probabilities for a simple Markov model:

| w_{i-1} | w_i | ML | course | is | UNK | <end> |
| --- | --- | --- | --- | --- | --- | --- |
| <beg> |  | 0.7 | 0.1 | 0.1 | 0.1 | 0.0 |
| ML |  | 0.1 | 0.5 | 0.2 | 0.1 | 0.1 |
| course |  | 0.0 | 0.0 | 0.7 | 0.1 | 0.2 |
| is |  | 0.1 | 0.3 | 0.0 | 0.6 | 0.0 |
| UNK |  | 0.1 | 0.2 | 0.2 | 0.3 | 0.2 |

### Calculating Sequence Probability

To calculate the probability of a sequence like "\<beg> ML course UNK \<end>", we multiply the transition probabilities along the path:
\[ P(\text{<beg> ML course UNK <end>}) = P(\text{ML | <beg>}) \times P(\text{course | ML}) \times P(\text{UNK | course}) \times P(\text{<end> | UNK}) \]
Using the table:
\[ P(\text{<beg> ML course UNK <end>}) = 0.7 \times 0.5 \times 0.2 \times 0.2 = 0.014 \]

### Advantages and Limitations

**Advantages:**

- Simplicity: Markov models are simple to implement and understand.
- Efficiency: They require fewer computations compared to models considering the entire history.

**Limitations:**

- Limited Context: They rely only on a fixed number of preceding words, which can miss long-range dependencies.
- Sparsity: Higher-order models can suffer from data sparsity because the number of possible word combinations increases exponentially with the order of the model.

### Applications

Markov language models are used in various natural language processing tasks such as:

- Text generation
- Speech recognition
- Machine translation
- Predictive text input

### Summary

Markov language models predict the next word in a sequence based on a fixed number of previous words, using transition probabilities. They balance simplicity and efficiency but can be limited by their inability to capture long-range dependencies. Despite their limitations, they form the foundation for more advanced language models, including n-grams and neural network-based models.

## Feature-Based Markov Models and Temporal/Sequence Problems

### Feature-Based Markov Models

**Feature-Based Markov Models** enhance traditional Markov models by incorporating additional features or attributes to improve predictions. Unlike traditional Markov models that rely solely on the state transitions, feature-based Markov models utilize a richer set of information for making predictions.

### Key Concepts:

1. **State Representation:**
    - In a traditional Markov model, a state is typically represented by a single entity (e.g., a word or a specific event).
    - In a feature-based Markov model, a state can be represented by a combination of multiple features (e.g., word identity, part-of-speech tags, semantic features).
2. **Transition Probabilities:**
    - Traditional Markov models compute transition probabilities based on the sequence of states.
    - Feature-based Markov models compute transition probabilities based on the features associated with states, which can provide more context and improve prediction accuracy.
3. **Advantages:**
    - **Incorporates Richer Information:** By including additional features, the model can capture more nuances and dependencies in the data.
    - **Improves Accuracy:** The use of features can lead to more accurate predictions, especially in complex scenarios.
    - **Flexibility:** The model can be adapted to different types of data and applications by selecting relevant features.

### Example:

Consider a text prediction task where we want to predict the next word in a sentence. In a feature-based Markov model, the state might include the current word, its part-of-speech tag, and semantic features like the word's role in the sentence (subject, object, etc.). This enriched state representation can lead to more accurate predictions compared to using the word alone.

### Temporal/Sequence Problems

**Temporal/Sequence Problems** involve data that is ordered in time or sequence, where the prediction task depends on previous elements in the sequence. These problems are common in many domains, including natural language processing, speech recognition, and time series analysis.

### Key Concepts:

1. **Temporal Dependencies:**
    - The key characteristic of temporal/sequence problems is that the prediction of the next element depends on previous elements in the sequence.
    - The strength and nature of these dependencies can vary, and they can span short or long ranges in the sequence.
2. **Sequential Data:**
    - Sequential data can include time series data (e.g., stock prices, weather data), sequences of words (e.g., sentences, paragraphs), or sequences of events (e.g., user actions on a website).
    - The data is typically represented as a sequence of vectors or states that capture relevant information at each time step.
3. **Modeling Approaches:**
    - **Markov Models:** These are suitable for modeling short-term dependencies. They assume that the next state depends only on a fixed number of previous states (Markov property).
    - **Hidden Markov Models (HMMs):** These extend Markov models by incorporating hidden states that influence the observed states, allowing for modeling more complex dependencies.
    - **Recurrent Neural Networks (RNNs):** These are neural network architectures specifically designed for sequence data. They maintain a hidden state that captures information from previous time steps.
    - **Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRUs):** These are advanced types of RNNs that are capable of learning long-term dependencies in sequence data.

### Example:

In speech recognition, the goal is to convert an audio signal into a sequence of words. This is a temporal problem because the recognition of each word depends on the sequence of sounds that have been heard up to that point. Advanced models like LSTMs are used to capture the long-term dependencies and context needed to accurately transcribe the audio signal.

### Comparing Markov Models and Neural Networks for Temporal Problems

- **Markov Models:**
    - Suitable for problems with short-term dependencies.
    - Easier to interpret and understand.
    - Limited in capturing long-term dependencies and complex patterns.
- **Neural Networks (RNNs, LSTMs, GRUs):**
    - Can capture both short-term and long-term dependencies.
    - More flexible and powerful for complex temporal problems.
    - Require more data and computational resources.
    - Can be harder to interpret due to the complexity of the learned representations.

### Summary

Feature-based Markov models and approaches for temporal/sequence problems address the challenge of making predictions based on sequential data. Feature-based Markov models enrich the state representation with additional features to improve prediction accuracy. Temporal/sequence problems are characterized by dependencies over time, and advanced models like RNNs, LSTMs, and GRUs are designed to handle these dependencies effectively, capturing both short-term and long-term relationships in the data.

### Recurrent Neural Networks (RNNs) for Sequences

**Problem with Traditional Markov Models and Fixed History:**

The main issue with traditional first-order and second-order Markov models, as well as their feedforward neural network equivalents, is that they rely on a fixed history length to predict the next state or word. This fixed history can be limiting because it may not capture all the necessary context from the sequence, especially in cases where longer dependencies are crucial. Ideally, the history should be variable and learnable so that the model can decide which past information is important for making predictions.

### Transitioning to Recurrent Neural Networks (RNNs)

To overcome the limitations of fixed history in Markov models, we can use Recurrent Neural Networks (RNNs). RNNs are designed to handle sequences of data by maintaining a hidden state that evolves over time, capturing information from the entire sequence up to the current time step.

### Key Components of RNNs:

1. **Input Representation (\(X_t\)):**
    - At each time step \(t\), we feed the model a one-hot vector of the previous word (\(W_{t-1}\)), denoted as \(X_t\). This vector has a length equal to the size of the vocabulary.
2. **Hidden State (\(S_t\)):**
    - The hidden state \(S_t\) is a vector of activations of the hidden units. It encapsulates the information from the sequence up to time \(t\). If there are \(m\) hidden units, \(S_t\) is an \(m\)-dimensional vector.
    - The hidden state is updated using a parameter matrix \(W_{sx}\) that maps the input \(X_t\) to the hidden state.
3. **Output Representation (\(P_t\)):**
    - Once we have the hidden state activations, we map them into output unit activations to get probabilities of the next word using a parameter matrix \(W_{o}\).
    - The output vector \(P_t\) contains the probability of each word in the vocabulary being the next word in the sequence.

### RNN Architecture:

- **Hidden State Update:**
\[
S_t = \tanh(W_{sx}X_t + W_{ss}S_{t-1})
\]
Here, \(W_{sx}\) is the weight matrix for the input, and \(W_{ss}\) is the weight matrix for the previous hidden state. The \(\tanh\) function introduces non-linearity.
- **Output Calculation:**
\[
P_t = \text{softmax}(W_{o}S_t)
\]
The softmax function transforms the hidden state into a probability distribution over the next words.

### How RNNs Handle Variable History:

- **Memory Mechanism:**
    - The hidden state \(S_t\) carries information from all previous time steps. This means \(S_t\) is influenced not only by the current input \(X_t\) but also by the hidden state \(S_{t-1}\), which itself encapsulates information from earlier in the sequence.
    - This recurrent connection allows the model to consider an arbitrarily long history, making the effective history variable and dependent on the entire sequence seen so far.
- **Learnable Attention:**
    - The RNN learns to focus on relevant parts of the history through training. By optimizing the weights \(W_{sx}\) and \(W_{ss}\), the RNN can adjust which parts of the sequence are most influential for making predictions at each time step.

### Comparison with Feedforward Networks:

- **Feedforward Networks:**
    - Process inputs in a single pass, without maintaining a state across time steps. They are limited to fixed-size input contexts.
- **Recurrent Neural Networks:**
    - Maintain a hidden state that evolves over time, allowing them to process sequences of varying lengths and capture long-term dependencies.

### True/False Statement:

**The hidden state at step $t$ only contains information about words close to $t$: False.**

- The hidden state $S_t$ contains information about the entire sequence up to time $t$, not just the words close to $t$. In theory, it can retain information from the beginning of the sequence, although the ability to remember long-term dependencies may degrade over time in standard RNNs. Advanced architectures like LSTMs and GRUs address this issue more effectively.

### Summary:

RNNs extend the capabilities of traditional Markov models by using a hidden state that evolves over time, capturing variable-length history and long-term dependencies. This allows RNNs to better model sequences and make more accurate predictions based on the entire context of the input data.

### Detailed Explanation: RNN Decoding

Recurrent Neural Networks (RNNs) are versatile tools for sequence generation, including tasks like language translation and image captioning. Here's a detailed explanation of how RNNs decode a vector into a sentence and how they can be adapted to work with various input modalities.

### Basics of RNN Decoding

**Initial State:**

- When generating a sequence from scratch, the initial state $s_0$ is typically a zero vector, and the process begins with a special token, such as a "beginning" symbol.
- For translating a vector into a sentence, the initial state is set to the given vector, rather than starting from zeros. This vector could represent a sentence, an image, or any other context.

**Sequential Generation:**

1. **Initial Step:**
    - The RNN takes the initial state (now the provided vector) and generates a probability distribution over the first word using the softmax function.
    - A word is sampled from this distribution and used as the input for the next step.
2. **Subsequent Steps:**
    - The sampled word, along with the updated hidden state, is fed into the RNN to generate the next word.
    - This process repeats, with the RNN updating its hidden state and generating new words, until an "end" symbol is generated, signaling the completion of the sequence.

### Translating a Vector into a Sentence

When translating a vector into a sentence, the RNN's hidden state evolves, taking into account both the vector's encoded information and the sequence of words generated so far.

1. **Using the Vector as the Initial State:**
    - The provided vector initializes the hidden state of the RNN.
    - This vector can be an encoded representation of a sentence, an image, or other data modalities.
2. **Generating the Sequence:**
    - At each time step, the RNN generates a probability distribution over the possible next words.
    - A word is sampled based on this distribution, updating the hidden state and serving as the input for the next step.
3. **Handling Different Modalities:**
    - For image captioning, the image is first encoded into a vector using a Convolutional Neural Network (CNN).
    - This vector initializes the RNN (or LSTM), which then generates a caption word-by-word.

### Example: Image Captioning

**Process:**

1. **Image Encoding:**
    - A CNN processes the image and encodes it into a fixed-size vector.
2. **RNN Initialization:**
    - This vector initializes the RNN's hidden state.
3. **Sequence Generation:**
    - The RNN generates a sequence of words describing the image, using the same process of updating hidden states and sampling words until an "end" token is produced.

**Training:**

- The architecture is trained using pairs of images and their corresponding captions.
- During training, the model learns to map image features to sequential word predictions.

**Example Output:**

- Given an image of a person riding a motorcycle on a dirt road, the RNN might generate: "A person riding a motorcycle on a dirt road."
- The accuracy of the generated description depends on the model's training data and ability to generalize from examples.

### Key Points from the Lecture:

1. **Markov Models:**
    - Understanding Markov models, their formulation, estimation, and sampling.
2. **Transition to Neural Networks:**
    - Translating Markov models into feedforward neural networks.
    - Extending feedforward networks into RNNs to handle sequences.
3. **RNN Sequence Generation:**
    - Using RNNs to generate sequences by evolving the hidden state and predicting the next word at each step.
    - Applying this framework to various contexts, such as sentences, images, and more.

### Summary:

RNNs are powerful tools for sequence generation, capable of translating vectors into sentences or other sequential data. By using an initial state derived from a vector (representing a sentence, image, or other modality), RNNs can generate coherent sequences through a process of iterative prediction and state updating. This makes RNNs suitable for a wide range of applications, from language translation to image captioning and beyond.