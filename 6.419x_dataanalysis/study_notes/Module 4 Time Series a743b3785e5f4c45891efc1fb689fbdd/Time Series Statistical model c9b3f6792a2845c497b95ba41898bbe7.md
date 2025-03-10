# Time Series: Statistical model

At the end of the is lecture, you should be able to

- State, describe, and apply the definition and properties of **white noise model, autoregressive model and random walk model** .
- State, describe, and apply the definition and property of **moving average model and ARMA model** .
- **Fit autoregressive model** to time series data and use **Yule-Walker equation** to estimate the coefficients.

## White Noise Model in Time Series Analysis

![Untitled](Time%20Series%20Statistical%20model%20c9b3f6792a2845c497b95ba41898bbe7/Untitled.png)

![Untitled](Time%20Series%20Statistical%20model%20c9b3f6792a2845c497b95ba41898bbe7/Untitled%201.png)

### Definition

The white noise model is one of the simplest and most fundamental models in time series analysis. It serves as a benchmark for understanding more complex models and as a baseline for the residuals of fitted models. A white noise time series \(\{W_t\}\) consists of random variables that exhibit the following properties:

1. **Zero Mean**:
\[
\mu_W(t) = \mathbb{E}[W_t] = 0
\]
This means that the expected value of the series at any time point \(t\) is zero.
2. **Constant Variance**:
\[
\gamma_W(t, t) = \text{Var}(W_t) = \sigma_W^2
\]
The variance of the series is constant over time, denoted by \(\sigma_W^2\).
3. **Zero Autocovariance**:
\[
\gamma_W(t, s) = \text{Cov}(W_t, W_s) = 0 \quad \text{for} \quad t \neq s
\]
There is no correlation between different time points. The series values are completely independent of each other.

### Characteristics

- **Stationarity**: A white noise series is inherently stationary because its statistical properties (mean, variance, autocovariance) do not change over time.
- **Independence**: Each value in a white noise series is independent of all other values. This lack of correlation means there are no detectable patterns or dependencies.
- **Distribution**: In many cases, the white noise series is assumed to be normally distributed. However, it can follow any distribution with the specified properties of zero mean, constant variance, and zero autocovariance.

### Purpose in Time Series Analysis

The white noise model itself is not typically used for forecasting or understanding the underlying process of a time series because it contains no information about dependencies or patterns. Instead, it serves several important roles:

1. **Residual Analysis**: After fitting a time series model (e.g., ARIMA, SARIMA), the residuals (the differences between the observed values and the fitted values) should ideally follow a white noise process. If the residuals are white noise, it indicates that the model has effectively captured all the underlying structure and dependencies in the data.
2. **Model Evaluation**: By checking if the residuals from a fitted model are white noise, we can assess the adequacy of the model. If the residuals exhibit any structure or autocorrelation, it suggests that the model has not fully captured the underlying process, and further modeling is necessary.
3. **Benchmark**: White noise serves as a benchmark for randomness. If a time series is determined to be white noise, it implies that there are no predictable patterns, trends, or dependencies that can be exploited for forecasting.

### Detection of White Noise

To determine whether a time series is white noise, the following steps are commonly undertaken:

1. **Check for Stationarity**:
    - Plot the time series to visually inspect for any trends, seasonal variations, or changes in variance.
    - Use statistical tests such as the Augmented Dickey-Fuller (ADF) test to formally test for stationarity.
2. **Examine the Autocovariance Function (ACF)**:
    - Compute the sample autocovariance function \(\hat{\gamma}_W(h)\) for different lags \(h\).
    - Plot the autocorrelation function (ACF) to visualize the dependence structure. For a white noise series, the ACF should be close to zero for all non-zero lags.

### Estimation of Autocovariance Function

Since the true autocovariance function is unknown, it is estimated from the data. The sample autocovariance function for a white noise series is given by:

\[ \hat{\gamma}*W(h) = \frac{1}{n} \sum*{t=1}^{n-h} (W_t - \bar{W})(W_{t+h} - \bar{W}) \]

where \(\bar{W}\) is the sample mean. Under appropriate technical conditions, the distribution of the estimator is:

\[ \hat{\gamma}_W(h) \sim N\left(0, \frac{\sigma_W^2}{n}\right) \]

This means that the estimated autocovariance function \(\hat{\gamma}_W(h)\) follows a normal distribution with mean zero and variance \(\frac{\sigma_W^2}{n}\). We do not expect the theoretical ACF to be exactly zero but approximately zero, considering the estimation error.

### Summary

The white noise model is crucial in time series analysis as it provides a reference point for randomness and a baseline for model residuals. It is characterized by zero mean, constant variance, and zero autocovariance for non-zero lags. Detecting white noise involves ensuring stationarity and examining the autocovariance function. If the residuals of a fitted model are white noise, it indicates that the model has successfully captured the underlying structure of the data.

### Practical Example with Python

Let's illustrate the detection of white noise using Python:

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller

# Generate a white noise series
np.random.seed(0)
white_noise = np.random.normal(0, 1, 100)

# Plot the time series
plt.figure(figsize=(10, 4))
plt.plot(white_noise)
plt.title("White Noise Time Series")
plt.show()

# Perform ADF test for stationarity
adf_test = adfuller(white_noise)
print(f"ADF Statistic: {adf_test[0]}")
print(f"p-value: {adf_test[1]}")

# Plot the ACF
plot_acf(white_noise, lags=20)
plt.show()

```

This code generates a white noise series, plots it, performs an Augmented Dickey-Fuller test to check for stationarity, and plots the autocorrelation function. The ACF plot should show values close to zero for all non-zero lags, confirming the white noise nature of the series.

### Properties of White Noise

A white noise time series has the following properties:

1. **Zero Mean**:
    - Each observation has a mean of zero.
    \[
    \mu_W(t) = \mathbb{E}[W_t] = 0
    \]
2. **Constant Variance**:
    - The variance of each observation is constant over time.
    \[
    \text{Var}(W_t) = \sigma_W^2
    \]
3. **Zero Autocovariance**:
    - The autocovariance between observations at different times is zero.
    \[
    \gamma_W(t, s) = \text{Cov}(W_t, W_s) = 0 \quad \text{for} \quad t \neq s
    \]
4. **Zero Autocorrelation**:
    - The autocorrelation between observations at different times is zero.
    \[
    \rho_W(t, s) = \frac{\gamma_W(t, s)}{\sigma_W^2} = 0 \quad \text{for} \quad t \neq s
    \]
5. **Stationarity**:
    - A white noise series is inherently stationary, meaning its statistical properties (mean, variance, and autocovariance) do not change over time.

### How to Determine if a Series is a White Noise Model

To determine if a time series is a white noise model, the following steps are typically undertaken:

### 1. Visual Inspection

**Plot the Time Series**:

- Plot the series to check for obvious patterns, trends, or seasonal components. A white noise series should appear as random fluctuations around a constant mean.

### 2. Statistical Tests for Stationarity

**Augmented Dickey-Fuller (ADF) Test**:

- Perform the ADF test to check for stationarity. The null hypothesis of the ADF test is that the series has a unit root (is non-stationary). A significant p-value (typically less than 0.05) indicates stationarity.

```python
from statsmodels.tsa.stattools import adfuller

# Example white noise series
white_noise = np.random.normal(0, 1, 100)
adf_test = adfuller(white_noise)
print(f"ADF Statistic: {adf_test[0]}")
print(f"p-value: {adf_test[1]}")

```

### 3. Autocorrelation Function (ACF) Analysis

**Compute and Plot the ACF**:

- Plot the ACF to visualize the correlation structure. For a white noise series, the autocorrelations should be close to zero for all non-zero lags. Significant spikes at non-zero lags indicate the presence of dependencies.

```python
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(white_noise, lags=20)
plt.show()

```

### 4. Statistical Test for Autocorrelation

**Ljung-Box Test**:

- The Ljung-Box test checks whether any group of autocorrelations is significantly different from zero. The null hypothesis is that the data are independently distributed (i.e., the series is white noise).

```python
from statsmodels.stats.diagnostic import acorr_ljungbox

ljung_box_test = acorr_ljungbox(white_noise, lags=[10], return_df=True)
print(ljung_box_test)

```

### 5. Estimate the Autocovariance Function

**Estimate \(\hat{\gamma}_W(h)\)**:

- Calculate the sample autocovariance function. For a white noise series, \(\hat{\gamma}_W(h) \approx 0\) for all non-zero lags.

```python
def autocovariance(x, h):
    n = len(x)
    mu = np.mean(x)
    return np.sum((x[:n-h] - mu) * (x[h:] - mu)) / n

gamma_estimates = [autocovariance(white_noise, h) for h in range(1, 11)]
print(gamma_estimates)

```

### Summary of Steps

1. **Visual Inspection**:
    - Plot the series to check for randomness without visible patterns or trends.
2. **Stationarity Test**:
    - Use the ADF test to confirm the series is stationary.
3. **ACF Analysis**:
    - Plot the ACF to ensure autocorrelations are close to zero for all non-zero lags.
4. **Ljung-Box Test**:
    - Perform the Ljung-Box test to check for significant autocorrelations.
5. **Estimate Autocovariance**:
    - Calculate and inspect the sample autocovariance function to confirm near-zero values for all non-zero lags.

By following these steps, one can determine if a time series is a white noise model, confirming that it has no predictable patterns or dependencies and serves as a good benchmark for model residuals.

## Autoregressive Model (AR Model)

![Untitled](Time%20Series%20Statistical%20model%20c9b3f6792a2845c497b95ba41898bbe7/Untitled%202.png)

![Untitled](Time%20Series%20Statistical%20model%20c9b3f6792a2845c497b95ba41898bbe7/Untitled%203.png)

### Definition

An autoregressive model (AR model) is a time series model used to describe a series where the current value of the series is expressed as a linear combination of its previous values and a random noise term. The order \( p \) of an autoregressive process indicates the number of previous values (lags) included in the model.

A time series \(\{X_t\}_t\) is an autoregressive process of order \(p\), denoted \(\text{AR}(p)\), if:

\[ X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + W_t \]

where:

- \(\phi_1, \phi_2, \ldots, \phi_p\) are the parameters of the model.
- \(\{W_t\}_t\) is a white noise process with mean zero and constant variance \(\sigma_W^2\).
- \(W_t\) is uncorrelated with \(X_s\) for \(s < t\).

### Properties

1. **Stationarity**:
    - For the AR process to be stationary, the roots of the characteristic equation associated with the AR polynomial must lie outside the unit circle.
2. **Recursive Nature**:
    - The AR model is recursive, meaning each value \(X_t\) depends on its past values. This dependency can be expanded by repeatedly substituting the expression for previous terms.

### Characteristic Equation

For an \(\text{AR}(p)\) model, the characteristic equation is given by:

\[ \phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p \]

where \( B \) is the backshift operator (\(B^k X_t = X_{t-k}\)). The model is stationary if all roots of this equation lie outside the unit circle in the complex plane.

### Example: AR(1) Model

An autoregressive process of order 1, \(\text{AR}(1)\), is given by:

\[ X_t = \phi_1 X_{t-1} + W_t \]

- The process is stationary if \(|\phi_1| < 1\).
- The mean of the process is zero (\(\mu_X = 0\)).
- The variance of the process is \(\sigma_X^2 = \frac{\sigma_W^2}{1 - \phi_1^2}\).

The autocovariance function \(\gamma(h)\) for the AR(1) process is:

\[ \gamma(h) = \phi_1^h \gamma(0) \]
\[ \gamma(0) = \frac{\sigma_W^2}{1 - \phi_1^2} \]

The autocorrelation function \(\rho(h)\) is:

\[ \rho(h) = \phi_1^h \]

### General AR(p) Model

For an \(\text{AR}(p)\) model, the autocovariance function \(\gamma(h)\) and the autocorrelation function \(\rho(h)\) can be derived using the Yule-Walker equations.

**Yule-Walker Equations**:

The Yule-Walker equations for an \(\text{AR}(p)\) process are:

\[ \gamma(h) = \sum_{k=1}^p \phi_k \gamma(h-k) + \sigma_W^2 \delta_{h,0} \]

where \(\delta_{h,0}\) is the Kronecker delta function, which is 1 if \(h = 0\) and 0 otherwise.

### Recursive Nature of the AR Model

The AR model is recursive. We can express \(X_t\) in terms of any previous term \(X_{t-h}\) by repeatedly substituting the expression for previous terms.

For example, consider an \(\text{AR}(2)\) model:

\[ X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + W_t \]

Substituting \(X_{t-1} = \phi_1 X_{t-2} + \phi_2 X_{t-3} + W_{t-1}\) into the equation:

\[ X_t = \phi_1 (\phi_1 X_{t-2} + \phi_2 X_{t-3} + W_{t-1}) + \phi_2 X_{t-2} + W_t \]
\[ X_t = \phi_1^2 X_{t-2} + \phi_1 \phi_2 X_{t-3} + \phi_1 W_{t-1} + \phi_2 X_{t-2} + W_t \]
\[ X_t = (\phi_1^2 + \phi_2) X_{t-2} + \phi_1 \phi_2 X_{t-3} + \phi_1 W_{t-1} + W_t \]

This demonstrates the recursive nature of the AR model, where each term depends on all previous terms.

### Autocovariance Function and ACF

The autocovariance function \(\gamma_X(h)\) of a stationary AR process is non-zero for all time lags \(h\) and decays to zero exponentially as \(h\) increases. This behavior is different from a white noise process, where the autocovariance is zero for all non-zero lags.

### Example with Python

Let's consider a practical example using Python to simulate an AR(2) process and plot its autocorrelation function.

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess

# Define AR(2) parameters
phi = np.array([1, -0.75, 0.25])  # Note the sign change for statsmodels
ar = np.r_[1, -phi[1:]]  # Add 1 for the AR(2) process

# Generate the AR(2) process
np.random.seed(42)
ar2_process = ArmaProcess(ar)
simulated_data = ar2_process.generate_sample(nsample=1000)

# Plot the simulated data
plt.figure(figsize=(10, 4))
plt.plot(simulated_data)
plt.title("Simulated AR(2) Process")
plt.show()

# Plot the ACF
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(simulated_data, lags=30)
plt.show()

```

### Conclusion

An autoregressive model of order \(p\) (AR(p)) is a foundational tool in time series analysis, modeling the current value of a series as a linear combination of its past \(p\) values and a white noise term. The AR model is recursive, meaning each term depends on all previous terms. The autocovariance function of an AR process is non-zero for all lags and decays exponentially, reflecting the dependencies in the series. Understanding and applying AR models are crucial for effectively analyzing and forecasting time series data.

## Random Walk Model

![Untitled](Time%20Series%20Statistical%20model%20c9b3f6792a2845c497b95ba41898bbe7/Untitled%204.png)

![Untitled](Time%20Series%20Statistical%20model%20c9b3f6792a2845c497b95ba41898bbe7/Untitled%205.png)

### Definition

A random walk is a time series model where each value in the series is the sum of the previous value and a random perturbation. Formally, a time series \(\{X_t\}_{t \ge 1}\) is a random walk if:

\[ X_t = X_{t-1} + W_t \]

where \(\{W_t\}*t\) is a white noise process with mean zero and constant variance \(\sigma_W^2\), and \(W_t\) is uncorrelated with all past values \(X*{s}\) for \(s < t\).

### Properties of Random Walk

1. **Initial Value**:
    - The series starts from an initial value \(X_0\), which can be any constant or random value.
2. **Cumulative Sum of White Noise**:
    - The value of \(X_t\) is the cumulative sum of all previous white noise terms plus the initial value:
    \[
    X_t = X_0 + \sum_{i=1}^{t} W_i
    \]
3. **Non-Stationarity**:
    - The random walk model is inherently non-stationary. Its mean and variance depend on time, violating the conditions for stationarity.
4. **Mean**:
    - The mean of \(X_t\) is equal to the initial value \(X_0\):
    \[
    \mathbb{E}[X_t] = \mathbb{E}[X_0] + \mathbb{E}\left[\sum_{i=1}^{t} W_i\right] = X_0 + 0 = X_0
    \]
5. **Variance**:
    - The variance of \(X_t\) increases linearly with time:
    \[
    \text{Var}(X_t) = \text{Var}\left(\sum_{i=1}^{t} W_i\right) = \sum_{i=1}^{t} \text{Var}(W_i) = t \sigma_W^2
    \]
6. **Autocovariance**:
    - The autocovariance function of a random walk depends on the time indices:
    \[
    \gamma_X(h) = \text{Cov}(X_t, X_{t-h}) = \min(t, t-h) \sigma_W^2
    \]

### Random Walk with Drift

A random walk with drift is a random walk that includes a deterministic linear trend component. Formally, a time series \(\{Y_t\}_{t \ge 1}\) is a random walk with drift if:

\[ Y_t = \delta \cdot t + X_t \]
\[ Y_t = \delta + Y_{t-1} + W_t \]

where:

- \(\delta\) is the drift term (a constant).
- \(\{X_t\}_{t \ge 1}\) is a random walk process without drift.

### Properties of Random Walk with Drift

1. **Mean**:
    - The mean of \(Y_t\) includes the linear trend component:
    \[
    \mathbb{E}[Y_t] = \mathbb{E}[\delta \cdot t + X_t] = \delta \cdot t + \mathbb{E}[X_t] = \delta \cdot t + X_0
    \]
2. **Variance**:
    - The variance of \(Y_t\) is the same as that of the random walk:
    \[
    \text{Var}(Y_t) = \text{Var}(X_t) = t \sigma_W^2
    \]
3. **Autocovariance**:
    - The autocovariance function of \(Y_t\) includes the linear trend component:
    \[
    \gamma_Y(h) = \text{Cov}(Y_t, Y_{t-h}) = \text{Cov}(\delta \cdot t + X_t, \delta \cdot (t-h) + X_{t-h})
    \]

Since the deterministic trend \(\delta\) does not contribute to the covariance (it is constant), the autocovariance remains the same as for the random walk:
\[
\gamma_Y(h) = \text{Cov}(X_t, X_{t-h}) = \min(t, t-h) \sigma_W^2
\]

### Characteristics and Implications

- **Random Walk**:
    - Non-stationary: The mean and variance change over time.
    - Used to model stock prices and other financial data where future values are influenced by past values plus some random error.
    - Hard to predict long-term behavior due to its non-stationarity.
- **Random Walk with Drift**:
    - Adds a constant trend to the non-stationary random walk.
    - Used to model processes with a consistent trend over time, like inflation rates or other economic indicators.
    - The presence of drift makes the series trend upward or downward over time.

### Example with Python

Let's simulate a random walk and a random walk with drift, and visualize them using Python.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
np.random.seed(42)
n = 100  # Number of time points
sigma_W = 1  # Standard deviation of white noise

# Random walk
W = np.random.normal(0, sigma_W, n)
X = np.cumsum(W)  # Cumulative sum to create random walk

# Random walk with drift
delta = 0.5  # Drift term
Y = delta * np.arange(n) + X

# Plot the series
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(X, label='Random Walk')
plt.title('Random Walk')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(Y, label='Random Walk with Drift', color='orange')
plt.title('Random Walk with Drift')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()

```

### Conclusion

The random walk model is a simple yet powerful model in time series analysis, representing a series where each value is the sum of the previous value and a random error term. It is inherently non-stationary, with a mean and variance that change over time. The random walk with drift adds a deterministic linear trend to the random walk, modeling processes with a consistent upward or downward trend. Both models are widely used in financial and economic applications to represent unpredictable and trending behaviors.