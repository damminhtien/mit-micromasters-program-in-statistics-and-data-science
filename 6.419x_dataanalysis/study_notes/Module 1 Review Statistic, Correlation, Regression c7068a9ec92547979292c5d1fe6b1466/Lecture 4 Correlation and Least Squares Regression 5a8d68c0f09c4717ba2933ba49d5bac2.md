# Lecture 4: Correlation and Least Squares Regression

# 1. **Correlation**

In this unit, we will

- Build up the concept of correlations from the more basic concepts of variance and covariance of data.
- Apply the concept of correlation to data from astronomy.

**Covariance:**

In statistics, covariance measures the joint variation between two random variables. For random variables X and Y, the covariance is defined by

$\displaystyle \text {Cov}(X,Y):= \mathbb E[(X-\mu _ X)(Y-\mu _ Y)],$

where $\mu _ X, \mu _ Y$ are expectations of X and Y, respectively.

Given a real data set $\{ (X_1,Y_1), (X_2, Y_2), \dots , (X_ N,Y_ N)\},$ consisting of $N$ samples of pairs of random variables X and Y, the covariance $\text {Cov}(X,Y)$ can be estimated by the **empirical sum**

$$
\displaystyle \text {Cov}(X,Y) \approx \frac{1}{N} \sum _{i=1}^{N} (X_ i-\bar X) (Y_ i-\bar Y),
$$

where mean values $\bar X= \frac{1}{N}\sum _{i=1}^ N X_ i$ and $\bar Y = \frac{1}{N}\sum _{i=1}^ N Y_ i$. 

Similarly, the variance of random variables X and Y have empirical estimates given by

$$
\displaystyle s_ X^2\displaystyle := {\mathbb E[(X-\bar{X})^2]} \approx {\frac{1}{N} \sum _{i=1}^{N} (X_ i-\bar X)^2 }, \qquad \text {and}
$$

$$
\displaystyle s_ Y^2\displaystyle := {\mathbb E[(Y-\bar{Y})^2]} \approx {\frac{1}{N} \sum _{i=1}^{N} (Y_ i-\bar Y)^2 }.
$$

Note that the above estimates for covariance and variance are all biased, and an easy way to correct the bias is applying **Bessel's correction**, where we use N-1 to replace N in all the denominators. In the rest of this lecture, both unbiased and biased estimates may appear.

---

In this exercise, we will investigate the correlation present in astronomical data observed by Edwin Hubble in the period surrounding 1930.

Hubble was interested in the motion of distant galaxies. He recorded the apparent velocity of these galaxies – the speed at which they appear to be receding away from us – by observing the spectrum of light they emit, and the distortion thereof caused by their relative motion to us. He also determined the distance of these galaxies from our own by observing a certain kind of star known as a Cepheid variable which periodically pulses. The amount of light this kind of star emits is related to this pulsation, and so the distance to any star of this type can be determined by how bright or dim it appears.

The following figure shows his data. The Y-axis is the apparent velocity, measured in kilometers per second. Positive velocities are galaxies moving away from us, negative velocities are galaxies that are moving towards us. The X-axis is the distance of the galaxy from us, measured in mega-parsecs (Mpc); one parsec is 3.26 light-years, or 30.9 trillion kilometers.

![Untitled](Lecture%204%20Correlation%20and%20Least%20Squares%20Regression%205a8d68c0f09c4717ba2933ba49d5bac2/Untitled.png)

```python
Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, \
0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, \
1.72, 2.03, 2.02, 2.02, 2.02])

Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0, 373.0, \
93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1.04E3, 1.10E3, \
840.0, 801.0, 519.0])

N = 24
```

Visit code in repository.

# **2. Correcting simple nonlinear relationships**

In this unit, we will

- Investigate how nonlinear relationships in data can be converted to linear relationships so that we may use linear regression.
- Learn how these transforms effect the assumed noise model.
- Judge if a nonlinear transformation needs to be applied to an astronomical data set.
- Investigate the effect (if any) that a nonlinear transform has on this data.

If the true underlying relationship in your data is nonlinear, then attempting to fit a linear model may give poor results in the best circumstances. In the worst circumstances, it can be misleading. You may conclude that there is no correlation present in the data, or that the relationship is linear when in fact it is not.

Generally speaking, fitting a nonlinear relationship must be done using nonlinear regression. However, if the nonlinearity is simple, it can be possible to transform the nonlinear relationship into a linear one.

Consider the following relationship:

$$
\displaystyle \displaystyle Y = \alpha e^{\beta X},
$$

where $\alpha$ and $\beta$ are two parameters. Attempting to directly fit this relationship with a linear model will preform terrible. But if we take the log on both sides, the original model will entail a linear form, i.e.,

$$
\displaystyle \displaystyle \ln {Y} = \beta X + \ln {\alpha },
$$

This looks linear, with $\beta$ being slope and $\ln {\alpha }$ intercept. With this observation, we can transform the data points by letting $Y_ i' = \ln {Y_ i}$, for $i=1, \dots , N$. Under such a transformation, Y' and X will have a linear relationship and we can employ linear regression on the problem.

Let's consider another relationship:

$$
\displaystyle \displaystyle Y = \beta \ln {X} + \alpha ,
$$

in which if we transform X to X' using $X'_ i = ln{X_ i}$, the resulted model become a linear relationship with slope $\beta$ and intercept $\alpha$.

The last example is to consider the following relationship:

$\displaystyle \displaystyle Y^{\gamma } = \alpha X^{\beta }.$

Then taking the log on both sides yields

$$
\displaystyle \displaystyle \ln {Y} = \frac{\beta \ln {X} + \ln {\alpha }}{\gamma },
$$

which is a linear model with slope $\beta /\gamma$ and intercept $\ln {(\alpha )}/\gamma$.

## **The effect of transformations on noise.**

The above three cases cover a wide range of potential nonlinear relationships. If one or more of your variables are positively valued, then it can worthwhile transforming it to its logarithm in order to investigate a potential nonlinear relation in the data.

It should be noted that these transformations can change the statistics of any noise present in the data, and that noise can in turn interfere with the regression. For example, if we have the variates

$$
\displaystyle \displaystyle Y = \alpha e^{\beta X} \epsilon ,
$$

where $\epsilon$ is some multiplicative noise, then

$$
\displaystyle \displaystyle \ln {Y} = \beta X + \ln {\alpha } + \ln {\epsilon },
$$

and the noise is also transformed. If $\epsilon$ were, for example, log-normally distributed, then under the log transformation it would now be normally distributed.

On the other hand, if we had

$$
\displaystyle \displaystyle Y = \alpha \left( e^{\beta X} + \epsilon \right).
$$

Then

$$
\displaystyle \displaystyle \ln {Y} = \ln {\left(e^{\beta X} + \epsilon \right)} + \ln {\alpha }.
$$

If $\epsilon$ is small, then this is still approximately linear, but if $\epsilon$ is large, we should not expect to see a linear relation. To handle such a situation correctly, we would need nonlinear regression.

---

For this exercise, we will use the following data:

```python
Xs = np.array([ 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5 ])

Ys = np.array([ 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248 ])

N = 9
```

Each data point is one planet in our solar system (with the addition of the planetoid Pluto, which will be henceforth referred to as a planet for simplicity).

The X values are the semi-major axis of each planet's orbit around the Sun. A planetary orbit is elliptical in shape, and the semi-major axis is the longer of the two axes that define the ellipse. When the ellipse is nearly circular (which is true for most planets), the semi-major axis is approximately the radius of said circle. The X values are measured in units of Astronomical Units (AU). One AU is very close to the average distance between the Sun and Earth (defined as 149597870700 meters), hence, the Earth's semi-major axis is essentially 1 AU due to its very circular orbit.

The Y values are the orbital period of the planet, measured in Earth years (365.25 days), so Earth also has a Y = 1 year.

# **3. Multiple linear regression**

In this unit, we will

- Create a model for a predicted variable using two or more predictor variables.
- Derive the estimator for the least squares solution for this model.
- Apply multiple linear regression to exoplanetary data in order to predict planet mass.

If we have more than two observed variables, we can create a model that predicts one variable, Y, based on two or more other variables: X_1, X_2, \ldots , X_ p. Then, the model for one observation of the predicted variable, Y_ i, can be written as

\displaystyle \displaystyle Y_ i = \beta _0 + \beta _1 X_{i,1} + \beta _2 X_{i,2} + \ldots + \beta _ p X_{i,p} +\epsilon _ i,

where X_{i,j} is the j-th feature of data point i, and p is the number of features.

To streamline the derivation, we stack the data in the vector form. In particular, let

\displaystyle \displaystyle \mathrm{{\boldsymbol x}}_ i\displaystyle = \begin{bmatrix} 1 \\ X_{i,1} \\ X_{i,2} \\ \vdots \\ X_{i,p} \end{bmatrix} \in \mathbb {R}^{p+1},\displaystyle \mathrm{{\boldsymbol \beta }}\displaystyle = \begin{bmatrix} \beta _0 \\ \beta _1 \\ \beta _2 \\ \vdots \\ \beta _ p \end{bmatrix} \in \mathbb {R}^{p+1}.

Then the model can be written as

\displaystyle \displaystyle Y_ i = \mathrm{{\boldsymbol x}}_ i^{\intercal }\mathrm{{\boldsymbol \beta }} + \epsilon _ i.

Note that the leading 1 in \mathrm{{\boldsymbol x}}_ i^{\intercal } multiplies by \beta _0 in \mathrm{{\boldsymbol \beta }} to create the intercept. We could have kept the intercept out of the vector product as its own term, but this way reduces the number of terms.

Note that this equation is much like computing one element from the result of a matrix-vector product. We can use this to simplify the expression further, allowing us to write one equation for all observations. First, put all the Y_ i observations and noise terms \epsilon _ i into their own vectors:

\displaystyle \displaystyle \mathrm{{\boldsymbol y}}\displaystyle = \begin{bmatrix} Y_1 \\ Y_2 \\ \vdots \\ Y_ N\end{bmatrix} \in \mathbb {R}^ N,\displaystyle \mathrm{{\boldsymbol \epsilon }}\displaystyle = \begin{bmatrix} \epsilon _1 \\ \epsilon _2 \\ \vdots \\ \epsilon _ N \end{bmatrix} \in \mathbb {R}^ N .

Now, arrange each row vector \mathrm{{\boldsymbol x}}_ i^{\intercal } so that it forms one row of a larger matrix:

\displaystyle \displaystyle {\boldsymbol X}\displaystyle = \begin{bmatrix} \rule[.5ex]{2.5ex}{0.5pt} & \mathrm{{\boldsymbol x}}_1^{\intercal }& \rule[.5ex]{2.5ex}{0.5pt} \\ \rule[.5ex]{2.5ex}{0.5pt} & \mathrm{{\boldsymbol x}}_2^{\intercal }& \rule[.5ex]{2.5ex}{0.5pt} \\ & \vdots & \\ \rule[.5ex]{2.5ex}{0.5pt} & \mathrm{{\boldsymbol x}}_ N^{\intercal }& \rule[.5ex]{2.5ex}{0.5pt} \end{bmatrix} \in \mathbb {R}^{N\times (p+1)}.

Then the model can then be written as

\displaystyle \displaystyle \mathrm{{\boldsymbol y}} = {\boldsymbol X} \mathrm{{\boldsymbol \beta }} + \mathrm{{\boldsymbol \epsilon }}.

---

The multiple linear regression predictive model is thus:

\displaystyle \displaystyle \hat{\mathrm{{\boldsymbol y}}}({\boldsymbol X}) = {\boldsymbol X} \mathrm{{\boldsymbol \beta }}.

And the least squares optimization target is

\displaystyle \displaystyle S(\mathrm{{\boldsymbol \beta }})\displaystyle = \sum _ i^ N (Y_ i - \mathrm{{\boldsymbol y}}_ i(\mathrm{{\boldsymbol x}}_ i))^2\displaystyle = \left(\mathrm{{\boldsymbol y}} - \hat{\mathrm{{\boldsymbol y}}}({\boldsymbol X})\right)^{\intercal }\left(\mathrm{{\boldsymbol y}} - \hat{\mathrm{{\boldsymbol y}}}({\boldsymbol X})\right)\displaystyle = \left(\mathrm{{\boldsymbol y}} - {\boldsymbol X} \mathrm{{\boldsymbol \beta }}\right)^{\intercal }\left(\mathrm{{\boldsymbol y}} - {\boldsymbol X}\mathrm{{\boldsymbol \beta }}\right)

We can find the least squares solution by finding the gradient of S with respect to \mathrm{{\boldsymbol \beta }}and setting it to zero:

\displaystyle \displaystyle \nabla S(\mathrm{{\boldsymbol \beta }}) = \frac{\partial S}{\partial \mathrm{{\boldsymbol \beta }}} = 0.

To find the least squares solution by minimizing the least squares optimization target \( S(\boldsymbol{\beta}) \), we need to compute the gradient of \( S \) with respect to \( \boldsymbol{\beta} \) and set it to zero:

\[
\nabla S(\boldsymbol{\beta}) = \frac{\partial S}{\partial \boldsymbol{\beta}} = 0
\]

Expanding the expression for \( S(\boldsymbol{\beta}) \), we have:

\[
S(\boldsymbol{\beta}) = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\intercal (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})
\]

Taking the derivative of \( S \) with respect to \( \boldsymbol{\beta} \) and setting it to zero yields the normal equations for the least squares solution:

\[
\frac{\partial S}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^\intercal (\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) = 0
\]

Solving this equation gives the least squares estimate for \( \boldsymbol{\beta} \):

\[
\boldsymbol{\beta} = (\mathbf{X}^\intercal \mathbf{X})^{-1} \mathbf{X}^\intercal \mathbf{y}
\]

Using the vector product rule \(\nabla (\mathbf{u}^\intercal \mathbf{v}) = \mathbf{u}^\intercal \nabla \mathbf{v} + \mathbf{v}^\intercal \nabla \mathbf{u}\), we can compute \(\nabla S\) as follows:

\[
\nabla S = -2\mathbf{X}^\intercal (\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) + 2\boldsymbol{\beta}^\intercal \mathbf{X}^\intercal \mathbf{X}
\]

Expanding and rearranging terms, we get:

\[
\nabla S = -2\mathbf{X}^\intercal \mathbf{y} + 2\boldsymbol{\beta}^\intercal \mathbf{X}^\intercal \mathbf{X}
\]

Now, setting \(\nabla S = 0\), we find the least squares estimator:

\[
\boldsymbol{\beta} = (\mathbf{X}^\intercal \mathbf{X})^{-1} \mathbf{X}^\intercal \mathbf{y}
\]

This is the least squares estimator, \(\hat{\boldsymbol{\beta}}\). It's worth noting that for \(\mathbf{X}^\intercal \mathbf{X}\) to be invertible, \(\mathbf{X}\) must be full column rank.

# **4. Model selection and regularization**

In this unit, we will

- Create a statistical test for the significance of a predictor in multiple linear regression.
- Derive the statistical distribution for this test.
- Apply the significance test to the exoplanetary data in order to assess the strength of the predictors.

We consider a dataset of p features and N data points, denoted by

\displaystyle \{ (X_1,Y_1), \dots , (X_ N, Y_ N)\} ,

where X_ i\in \mathbb R^ p, and Y_ i\in \mathbb R. To include the intercept in the model, we assume the first element of X_ i is 1, for all i=1, \dots , N. Then the linear regression model for this dataset can be written in a matrix form

\displaystyle \displaystyle \mathrm{{\boldsymbol y}} = {\boldsymbol X} \mathrm{{\boldsymbol \beta }} + \mathrm{{\boldsymbol \epsilon }},

where \mathrm{{\boldsymbol \beta }} \in \mathbb R^{p}, \mathrm{{\boldsymbol \epsilon }} \in \mathbb R^{N}, \mathrm{{\boldsymbol y}}=(Y_1, \dots , Y_ N)^{\intercal }\in \mathbb R^{N}, and data matrix {\boldsymbol X} is defined by {\boldsymbol X}=(X_1, X_2, \dots , X_ N)^ T \in \mathbb R^{N\times p}.

Furthermore, we assume that the elements of \mathrm{{\boldsymbol \epsilon }} are i.i.d. with normal distribution \mathrm{{\boldsymbol \epsilon }}_ i \sim \mathcal{N}(0,\sigma ), for i=1,\dots , N, and that \mathrm{{\boldsymbol \epsilon }} is independent of data {\boldsymbol X}. When data matrix {\boldsymbol X} is full column rank, the least squares estimate of coefficient \mathrm{{\boldsymbol \beta }} is given by

\displaystyle \displaystyle \hat{\mathrm{{\boldsymbol \beta }}} = ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol y}}.

Then we claim that such an estimator \hat{\mathrm{{\boldsymbol \beta }}} conditions on {\boldsymbol X}satisfies

\displaystyle \displaystyle \mathbb {E}[\hat{\mathrm{{\boldsymbol \beta }}}|{\boldsymbol X}]\displaystyle = \mathrm{{\boldsymbol \beta }},\displaystyle \text {Cov}[\hat{\mathrm{{\boldsymbol \beta }}}|{\boldsymbol X}]\displaystyle = \sigma ^2 ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1},

which implies estimator \hat{\mathrm{{\boldsymbol \beta }}} is conditionally unbiased.

### **Proof**

For the conditional expectation, we have

\displaystyle \displaystyle \mathbb {E}[\hat{\mathrm{{\boldsymbol \beta }}}|{\boldsymbol X}]\displaystyle = \mathbb {E}[({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol y}}|{\boldsymbol X}]\displaystyle = \mathbb {E}[({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }{\boldsymbol X} \mathrm{{\boldsymbol \beta }} + ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol \epsilon }}|{\boldsymbol X}]\displaystyle = \mathrm{{\boldsymbol \beta }} + ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathbb {E}[ \mathrm{{\boldsymbol \epsilon }}|{\boldsymbol X}]\displaystyle = \mathrm{{\boldsymbol \beta }}.

Note that in the last equality, as \mathrm{{\boldsymbol \epsilon }} is independent of {\boldsymbol X}, it holds that \mathbb {E}[ \mathrm{{\boldsymbol \epsilon }}|{\boldsymbol X}]=\mathbb {E}[ \mathrm{{\boldsymbol \epsilon }}]=0.

Moreover, we notice that \hat{\mathrm{{\boldsymbol \beta }}} - \mathrm{{\boldsymbol \beta }} = ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\left( {\boldsymbol X} \mathrm{{\boldsymbol \beta }} + \mathrm{{\boldsymbol \epsilon }} \right) - \mathrm{{\boldsymbol \beta }}=({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol \epsilon }}. Then the covariance matrix for \hat{\mathrm{{\boldsymbol \beta }}} is

\displaystyle \displaystyle \text {Cov}[\hat{\mathrm{{\boldsymbol \beta }}}|{\boldsymbol X}]\displaystyle =\mathbb {E}[(\hat{\mathrm{{\boldsymbol \beta }}} - \mathrm{{\boldsymbol \beta }})(\hat{\mathrm{{\boldsymbol \beta }}} - \mathrm{{\boldsymbol \beta }})^{\intercal }|{\boldsymbol X}]\displaystyle =\mathbb {E}[(({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol \epsilon }})(({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol \epsilon }})^{\intercal }|{\boldsymbol X}]\displaystyle = ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathbb {E}[\mathrm{{\boldsymbol \epsilon }}\mathrm{{\boldsymbol \epsilon }}^{\intercal }|{\boldsymbol X}] {\boldsymbol X} ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1}\displaystyle = \sigma ^2 ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }{\boldsymbol X} ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1}\displaystyle = \sigma ^2 ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1},

where we use the fact that \mathbb {E}[\mathrm{{\boldsymbol \epsilon }}\mathrm{{\boldsymbol \epsilon }}^{\intercal }] = \sigma ^2 I.

So far we have already found the conditional expectation and covariance matrix for estimator \hat{\mathrm{{\boldsymbol \beta }}}, but in \text {Cov}[\hat{\mathrm{{\boldsymbol \beta }}}|{\boldsymbol X}], we are still unaware of \sigma. The good news is that we can show that there exists a conditional unbiased estimator for \sigma ^2, given by

\displaystyle \displaystyle \hat{\sigma }^2 = \frac{\sum _ i^ N (Y_ i - \mathrm{{\boldsymbol x}}_ i^{\intercal }\hat{\mathrm{{\boldsymbol \beta }}})^2}{N-p}.

### Detail derivation

First, due to the fact that \mathbb {E}[\mathrm{{\boldsymbol \epsilon }}] = 0, we notice that

\displaystyle \displaystyle \mathbb {E}[\mathrm{{\boldsymbol y}}|{\boldsymbol X}]\displaystyle = \mathbb {E}[{\boldsymbol X} \mathrm{{\boldsymbol \beta }} | {\boldsymbol X}]\displaystyle = {\boldsymbol X} \mathrm{{\boldsymbol \beta }}.

This further leads to

\displaystyle \displaystyle \mathbb {E}[(\mathrm{{\boldsymbol y}} - \mathbb {E}[\mathrm{{\boldsymbol y}}|{\boldsymbol X}])(\mathrm{{\boldsymbol y}} - \mathbb {E}[\mathrm{{\boldsymbol y}}|{\boldsymbol X}])^{\intercal }|{\boldsymbol X}]\displaystyle = \mathbb {E}[\mathrm{{\boldsymbol \epsilon }}\mathrm{{\boldsymbol \epsilon }}^{\intercal }| {\boldsymbol X}]\displaystyle = \sigma ^2 I.

Inspired by this equality, the variance of \mathrm{{\boldsymbol y}} could be used to estimate \sigma:

\displaystyle \displaystyle \sigma ^2\displaystyle = \frac{1}{N-1} \sum _ i^ N (Y_ i - \mathrm{{\boldsymbol x}}_ i^{\intercal }\mathrm{{\boldsymbol \beta }})^2

However, we don't have access to \mathrm{{\boldsymbol \beta }} directly, just its estimate, so we can't just compute the variance directly as it requires knowing the mean. Instead we must find

\displaystyle \displaystyle S\displaystyle = \sum _ i^ N (Y_ i - \mathrm{{\boldsymbol x}}_ i^{\intercal }\hat{\mathrm{{\boldsymbol \beta }}})^2\displaystyle = (\mathrm{{\boldsymbol y}} - {\boldsymbol X} \hat{\mathrm{{\boldsymbol \beta }}})^{\intercal }(\mathrm{{\boldsymbol y}} - {\boldsymbol X} \hat{\mathrm{{\boldsymbol \beta }}})\displaystyle = (\mathrm{{\boldsymbol y}} - {\boldsymbol X} ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol y}})^{\intercal }(\mathrm{{\boldsymbol y}} - {\boldsymbol X} ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }\mathrm{{\boldsymbol y}})\displaystyle = ({\boldsymbol X}\mathrm{{\boldsymbol \beta }} + \mathrm{{\boldsymbol \epsilon }})^{\intercal }(I - {\boldsymbol X} ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal })^2 ({\boldsymbol X}\mathrm{{\boldsymbol \beta }} + \mathrm{{\boldsymbol \epsilon }})\displaystyle = \mathrm{{\boldsymbol \epsilon }}^{\intercal }(I - {\boldsymbol H})^2 \mathrm{{\boldsymbol \epsilon }}

where {\boldsymbol H} = {\boldsymbol X} ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} {\boldsymbol X}^{\intercal }.

We can verify that \mathbb {E}[(I - {\boldsymbol H}) \mathrm{{\boldsymbol \epsilon }} | {\boldsymbol X}] = 0, and thus S is a sum of squares each with mean 0.

Now note that {\boldsymbol H} is idempotent, and so (I - {\boldsymbol H}) is also idempotent. In addition, the rank of an idempotent matrix is equal to the trace of the matrix. So \text {rank}(I - {\boldsymbol H}) = N - \text {rank}({\boldsymbol H}), and the rank of {\boldsymbol H} is equal to the number of columns in {\boldsymbol X}, denoted by p. (Note that p includes any intercept column, in the slides p-1 is used so that p is just the number of model parameters.) Thus \text {rank}(I - {\boldsymbol H}) = N - p.

As the variance of \epsilon is \sigma ^2, it follows that \mathrm{{\boldsymbol \epsilon }}/\sigma is a standard normally distributed random variable. Then, from Cochran's theorem, we have that

\displaystyle \displaystyle \frac{S}{\sigma ^2}\displaystyle = \frac{\mathrm{{\boldsymbol \epsilon }}^{\intercal }}{\sigma } (I - {\boldsymbol H}) \frac{\mathrm{{\boldsymbol \epsilon }}}{\sigma },

is \chi ^2 distributed with number of degrees of freedom equal to \text {rank}(I - {\boldsymbol H}).

Therefore

\displaystyle \displaystyle \mathbb {E}[\frac{S}{\sigma ^2}|{\boldsymbol X}]\displaystyle = N - p.

We can now use this as an estimator of \sigma ^2:

\displaystyle \displaystyle \hat{\sigma }^2\displaystyle = \frac{S}{N-p}

Now, we are ready to use z-test to test the null hypothesis that \beta _ j = 0. Recall the covariance matrix {Cov}[\hat{\mathrm{{\boldsymbol \beta }}}|{\boldsymbol X}] = \sigma ^2 ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1}. We denote the j-th diagonal element of ({\boldsymbol X}^{\intercal }{\boldsymbol X})^{-1} by \Sigma ^2_ j. Then, under the null hypothesis, we have

\displaystyle \displaystyle \frac{\hat{\beta }_ j - 0}{\sigma \Sigma _ j}\displaystyle \sim \mathcal{N}(0, 1),

where \sigma \Sigma _ j is the conditional standard deviation of \hat{\beta }_ j.

Now the convariance estimator

\displaystyle \displaystyle \hat{\sigma }^2\displaystyle = \frac{{| | \mathrm{{\boldsymbol y}} - {\boldsymbol X} \hat{\mathrm{{\boldsymbol \beta }}} | |}^2}{N-p}

is an estimator for \sigma ^2, and

\displaystyle \displaystyle (N-p)\frac{\hat{\sigma }^2}{\sigma ^2}\displaystyle \sim \chi ^2_{N-p}

where p is the number of columns in \hat{X}.

If Z \sim \mathcal{N}(0,1) and \omega \sim \chi ^2_ n then

\displaystyle \displaystyle \frac{Z}{\sqrt{\frac{\omega }{n}}}\displaystyle \sim t_ n

is t-distributed with n degrees of freedom.

Therefore

\displaystyle \displaystyle T_ j\displaystyle = \frac{ \frac{\hat{\beta }_ j - 0}{\sigma \Sigma _ j} }{ \sqrt{\frac{(N-p)\frac{\hat{\sigma }^2}{\sigma ^2}}{N-p}} }\displaystyle = \frac{\hat{\beta }_ j}{\hat{\sigma } \Sigma _ j}

is t distributed with N-p degrees of freedom and can be used as a t-test to test the hypothesis that \beta _ j = 0.

# **5. Step sizes and quadratic bounds**

In this unit, we will

- Discuss failure modes for gradient descent and how this will inform our choice of step size.
- Create bounds on the second derivatives of the loss function.
- Use these bounds to create quadratic upper and lower bounds on the loss function itself.
- Show how this quadratic lower bound reduces to the tangent lower bound when the loss function is convex.
- Use this to create a process for iteratively guessing and refining the choice of step size.

A good choice of the step size parameter, \alpha, is critical for good performance in gradient descent.

Recall that we defined the step size in terms of an estimate of the Hessian:

\displaystyle \displaystyle (\nabla \nabla f)(\mathrm{{\boldsymbol w}}_ t)\displaystyle \approx \frac{1}{\alpha } {\boldsymbol I},

If the step size is too large, then we are effectively underestimating the curvature of the loss function. If we are already near the minimum, and we underestimate the curvature, then we will “step over" the minimum, and the next iteration will result in the gradient descent doubling back on itself.

There is an even worse scenario, if the step size is large enough, the next update, \mathrm{{\boldsymbol w}}_{t+1}, can actually be further from the minimum than the current position, \mathrm{{\boldsymbol w}}_ t. For convex loss functions, the gradient increases as we get further from the minimum, so we can end up in a situation where

\displaystyle \displaystyle {| | (\nabla f)(\mathrm{{\boldsymbol w}}_{t+1}) | |}^2\displaystyle > {| | (\nabla f)(\mathrm{{\boldsymbol w}}_{t}) | |}^2.

If this happens, the gradient descent procedure will never converge. Remember that one of the convergence criteria we defined was

\displaystyle \displaystyle {| | (\nabla f)(\mathrm{{\boldsymbol w}}_ t) | |}^2\displaystyle < \epsilon .

If the norm of the gradient is increasing instead of decreasing, this criteria will never be met.

Now let us consider the other end of the spectrum: when the step size is too small.

This is much more benign situation. By choosing a step size that is too small, we have overestimated the curvature of the loss function. This means that if we are close to the minimum, we will “under step" and land somewhere between the minimum and our current position. But unlike before, we will be closer to the minimum, and so the norm of the gradient will decrease (if the function is convex). Therefore repeated iteration will eventually converge.

The only pathology to be aware of is that as the step size gets smaller, we will require more steps to reach our stopping criterion. If the step size is too small, we might not reach the minimum before our computational budget (total CPU time, maximum iterations, etc) has been exceeded and we are forced to stop.

Therefore we can conclude that when we are required to choose the step size, it is better to choose a strategy that will underestimate the step size. This is the “conservative" choice, as it result in lower risk for the convergence of the procedure at the expense of additional computational time.

### Bounding the curvature

1 point possible (graded)

Recall that if we know the Hessian, and the loss function is convex, we can use the Newton update rule

\displaystyle \displaystyle \mathrm{{\boldsymbol w}}_{t+1}\displaystyle = \mathrm{{\boldsymbol w}}_ t - \left[ (\nabla \nabla f)(\mathrm{{\boldsymbol w}}_ t) \right]^{-1} (\nabla f)(\mathrm{{\boldsymbol w}}_ t)^{\intercal }.

We abandoned this for the step size on the grounds that we might not be able to compute the Hessian; or, even if we can, the function may not be convex, and adjusting the Hessian for non-convex functions is computationally demanding. Even if we don't know the Hessian directly, we may be able to extract some information from the second order derivatives of the loss function.

In one dimension, the second derivative f^{\prime \prime }(w_ t) at a point w_ t tells us the curvature of the function. Recall that in multiple dimensions, there is no single number that measures curvature, as a function can be curving downward in one direction while curving upward in another direction, such as at a saddle point. Instead, we can perform an eigendecomposition of the Hessian matrix, which gives us a series of eigenvalues, \lambda _ i, and associated eigenvectors, \mathrm{{\boldsymbol v}}_ i. The eigenvectors are directions in our parameter space, and the associated eigenvalues are the measure of curvature in the direction of that eigenvector.

Thus, we can find an upper bound, L, to the curvature at point \mathrm{{\boldsymbol w}}_ t by computing the eigenvalues of the Hessian and using the maximum eigenvalue:

\displaystyle \displaystyle L\displaystyle = \max _{i} \lambda _ i.

We then approximate the Hessian by this upper bound, and in doing so find a step size:

\displaystyle \displaystyle (\nabla \nabla f)(\mathrm{{\boldsymbol w}}_ t)\displaystyle \approx L I = \frac{1}{\alpha } {\boldsymbol I},

so \alpha = 1/L.

This would make for a pretty useless approximation if we needed to compute the full eigendecomposition of the Hessian to find the maximum eigenvalue. But we need not: the maximum eigenvalue is also given by the spectral norm of the matrix. This matrix norm is defined as

\displaystyle \displaystyle {| |{\boldsymbol H}| |}_2\displaystyle = \max _{\mathrm{{\boldsymbol u}} \neq 0} \frac{\mathrm{{\boldsymbol u}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol u}}}{\mathrm{{\boldsymbol u}}^{\intercal }\mathrm{{\boldsymbol u}}}.

This is a little easier to understand if we restrict the vectors in the maximization to unit vectors, so that \mathrm{{\boldsymbol u}}^{\intercal }\mathrm{{\boldsymbol u}} = 1:

\displaystyle \displaystyle {| |{\boldsymbol H}| |}_2\displaystyle = \max _{{| |\mathrm{{\boldsymbol n}}| |}^2 = 1} \mathrm{{\boldsymbol n}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol n}}.

So to find the spectral norm, we find the unit vector \mathrm{{\boldsymbol n}} that maximizes the term \mathrm{{\boldsymbol n}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol n}}, then we define the spectral norm as the value of the term at that maximum. We can think of this as finding a direction which the Hessian-vector product, {\boldsymbol H}\mathrm{{\boldsymbol n}}, maximizes. The Hessian is a symmetric matrix, and for a symmetric matrix the spectral norm is equal to the maximum eigenvalue:

\displaystyle \displaystyle {| |{\boldsymbol H}| |}_2\displaystyle = \max _{i} \lambda _ i.

So we can use this to set the step size to \alpha = ({| |{\boldsymbol H}| |}_2)^{-1}.

Another technique we could try is to just compute the diagonals of the Hessian, and take the maximum:

\displaystyle \displaystyle L\displaystyle = \max _{i} \frac{\partial ^2 f}{\partial w_ i^2}(\mathrm{{\boldsymbol w}}_ t)

**Global bounds.**

So far, we have only tried to set the step size by estimating the curvature **locally** : by computing the second order derivatives at the location \mathrm{{\boldsymbol w}}_ t. This local strategy has advantages and disadvantages.

If the curvature is decreasing toward the minimum, then using the local curvature for the step size results in an adaptive step size that speeds up convergence. If the curvature begins increasing as we move toward the minimum, then we may end up with a step size that is consistently too large. This is because a bound on the local curvature is not a bound on the global curvature.

A particularly bad failure case would be if the curvature increases sharply near the minimum. It may take a long time to converge in this scenario, as the gradient descent will repeatedly over-step the minimum.

If we know some global information, such as the maximum curvature of the function, then we could use this to ensure that the step size does not get too large.

It turns out that we can't hope for this in general. Consider the following convex loss function:

\displaystyle \displaystyle f(w) = x^4.

There is no maximum curvature for this loss function, in the sense that we can't set an upper bound on it. This is because the second derivative, f^{\prime \prime }(w) = 12 x^2, continues to increase with x without bound.

Still, it is possible to find a maximum curvature within a certain region. Again, if we consider the interval -w_ a \leq w \leq w_ a for the loss function f(w) = x^4, then we can place a bound on the second derivative of f^{\prime \prime }(w) \leq 12 w_ a^2.

**Quadratic bounds.**

Recall that we wrote the loss function in terms of its Taylor expansion and the remainder term:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle = f(\mathrm{{\boldsymbol w}}_ t) + (\nabla f)(\mathrm{{\boldsymbol w}}_ t) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t) + R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_ t).

And that this remainder term is given in terms of some \mathrm{{\boldsymbol w}}_{*} that is an element of the line between \mathrm{{\boldsymbol w}} and \mathrm{{\boldsymbol w}}_ t:

\displaystyle \displaystyle R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_ t)\displaystyle = \frac{1}{2} (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t)^{\intercal }(\nabla \nabla f)(\mathrm{{\boldsymbol w}}_{*}) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t).

Suppose we know an upper bound on the spectral norm of the Hessian, {\boldsymbol H} = \nabla \nabla f, within some region \mathcal{R}:

\displaystyle \displaystyle {| |{\boldsymbol H}(w)| |}_2 \leq M \quad \quad \forall \mathrm{{\boldsymbol w}} \in \mathcal{R}.

Then we know by the definition of the spectral norm that the remainder term has an upper bound of M:

\displaystyle \displaystyle R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_ t)\displaystyle \leq \frac{1}{2} M {| | \mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t | |}^2.

Now we can use this to find a quadratic upper bound on the loss function:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle \leq f(\mathrm{{\boldsymbol w}}_ t) + (\nabla f)(\mathrm{{\boldsymbol w}}_ t) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t) + \frac{1}{2} M {| | \mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t | |}^2.

Correspondingly, we can now use a step size \alpha = 1/M.

Generally speaking, we don't need to find M exactly to have a conservative step size. We just need to find an L, such that L \geq M, then we can use a step size of \alpha = 1/L.

For the sake of completeness (and academic interest), we can also define a lower bound if we know the minimal eigenvalue of the Hessian:

\displaystyle \displaystyle m \leq \left( \min _{i} \lambda _ i(\mathrm{{\boldsymbol w}}) \right) \quad \quad \forall \mathrm{{\boldsymbol w}}.

This puts a lower bound on the remainder term:

\displaystyle \displaystyle R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_ t)\displaystyle \geq \frac{1}{2} m {| | \mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t | |}^2,

and so

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle \geq f(\mathrm{{\boldsymbol w}}_ t) + (\nabla f)(\mathrm{{\boldsymbol w}}_ t) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t) + \frac{1}{2} m {| | \mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t | |}^2.

Although this is not particularly useful for our investigation of the step size, we can use this to connect back to our original definition of the lower bound tangent hyperplane. If f is convex, then we know that the smallest eigenvalue is equal to or larger than zero. So we can set m=0 in the above formula, and the result is the lower bound tangent hyperplane. If f is not convex, then the smallest eigenvalue will be negative. If the smallest eigenvalue is negative, then the term on the right in the above equation is negative, and we get a lower bound that curves downward.

Deciding on the step size through the estimation of the curvature requires us to know something about the second order derivatives of the loss function. However, it is commonly the case that we really don't know anything about the function other than the value of the function, f(\mathrm{{\boldsymbol w}}), and its gradient \nabla f.

In this case, we can attempt to estimate the right step size by examining how the value of the function changes.

We will approach the problem from the opposite direction this time, by first assuming a step size, and then observing what this assumption implies about the curvature. Let \mathrm{{\boldsymbol w}}_ t be the current location of the gradient descent, as before. Then we will write the step size for this iteration as \alpha _ t, so that it too is a function of the iteration number t.

Before, we estimated the second order derivative as L, then set the step size as \alpha _ t=1/L. Now, we set the step size as \alpha _ t, which implies that we have assumed the second order derivative to be L=1/\alpha _ t.

From this, we can find a quadratic upper bound:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle \leq f(\mathrm{{\boldsymbol w}}_ t) + (\nabla f)(\mathrm{{\boldsymbol w}}_ t) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t) + \frac{1}{2} \frac{1}{\alpha _ t} {| | \mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_ t | |}^2.

The gradient descent update step finds the minimum of this quadratic, and updates the current location to this minimum:

\displaystyle \displaystyle \mathrm{{\boldsymbol w}}_{t+1}\displaystyle = \mathrm{{\boldsymbol w}}_ t - \alpha _ t (\nabla f)(\mathrm{{\boldsymbol w}}_ t)^{\intercal }

We can substitute this into the quadratic upper bound to find the implied upper bound at \mathrm{{\boldsymbol w}}_{t+1}:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}}_{t+1})\displaystyle \leq f(\mathrm{{\boldsymbol w}}_ t) + (\nabla f)(\mathrm{{\boldsymbol w}}_ t) \alpha _ t \left(-(\nabla f)(\mathrm{{\boldsymbol w}}_ t)^{\intercal }\right) + \frac{1}{2} \frac{1}{\alpha _ t} {| | \alpha _ t (\nabla f)(\mathrm{{\boldsymbol w}}_ t)^{\intercal }| |}^2\displaystyle = f(\mathrm{{\boldsymbol w}}_ t) - \alpha _ t {| | (\nabla f)(\mathrm{{\boldsymbol w}}_ t) | |}^2 + \frac{1}{2} \alpha _ t {| | (\nabla f)(\mathrm{{\boldsymbol w}}_ t)^{\intercal }| |}^2\displaystyle = f(\mathrm{{\boldsymbol w}}_ t) - \frac{1}{2} \alpha _ t {| | (\nabla f)(\mathrm{{\boldsymbol w}}_ t) | |}^2

If, after calculating f(\mathrm{{\boldsymbol w}}_{t+1}), we find that it actually violates this upper bound, then we know that the step size was too large, and our implied estimate of the curvature was too small. So we decrease the step size, \alpha _ t \rightarrow \alpha _ t/2, and try again. Decreasing the step size implies a larger curvature of the loss function, so the resulting upper bound will now be higher.

With the new step size in hand, we calculate a new \mathrm{{\boldsymbol w}}_{t+1} and then the new upper bound at this location, and check the inequality again. If, again, it violates the upper bound, we reduce by half again, and repeat. If the upper bound is not violated, and holds for the new location \mathrm{{\boldsymbol w}}_{t+1}, then we save this as the new current location for the gradient descent and use this value of the step size as the initial guess for the next iteration: \alpha _{t+1} = \alpha _ t.

# **6. Stochastic gradient descent**

In this unit, we will

- Discuss the problem of running gradient descent on large data sets.
- Define stochastic gradient descent, which helps to alleviate this problem.
- Discuss the variance introduced by this stochastic process.
- Show why a step size schedule is needed for good performance in stochastic gradient descent.

### Large data sets

2 points possible (graded)

When a data set is large, we would ideally want to split up our loss function into a sum of individual loss functions for each data point:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle = \sum _{i=1}^ N f_ i(\mathrm{{\boldsymbol w}}),

where f_ i(\mathrm{{\boldsymbol w}}) is the individual data point loss functions.

For example, in a least squares regression, we choose f_ i to be the square of the residual for measured data point y_ i with prediction \hat{y}_ i:

\displaystyle \displaystyle f_ i(\mathrm{{\boldsymbol w}})\displaystyle = (y_ i - \hat{y}_ i)^2,

so that the loss function f is a sum of these squared residuals.

The gradient of the loss function is then the sum of gradients for each individual data-point loss function:

\displaystyle \displaystyle (\nabla f)(\mathrm{{\boldsymbol w}})\displaystyle = \sum _{i=1}^ N (\nabla f_ i)(\mathrm{{\boldsymbol w}}).

This requires the computation of the gradient for each and every data point before we can find the total gradient of the loss function.

### Stochastic gradient descent

1 point possible (graded)

Even if we can fit a large data set in the memory of our computer, computing the gradient of f requires iterating over every data point. This can be a considerably lengthy process, and must be repeated often for each step in the gradient descent process. Instead, we seek to reduce the number of data points that are required for computing the gradient. We will do this by taking a subsample of the data.

Notice that we can freely rescale the loss function by a multiplicative constant:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle \rightarrow f(\mathrm{{\boldsymbol w}}) = \frac{1}{N} \sum _{i=1}^ N f_ i(\mathrm{{\boldsymbol w}}).

This looks a lot like a mean. Therefore, if we define our data set to be a population, then we can write the loss function as an expectation over this population:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle \rightarrow f(\mathrm{{\boldsymbol w}}) = \mathbb {E}[f_ i(\mathrm{{\boldsymbol w}})].

We can then estimate the update step by using the gradient for only one data point,

\displaystyle \displaystyle \hat{\mathrm{{\boldsymbol w}}}_{t+1}\displaystyle = \mathrm{{\boldsymbol w}}_ t - \alpha _ t (\nabla f_ i)(\mathrm{{\boldsymbol w}}_ t).

The data point to use should be chosen randomly at each iteration step.

As long as we choose f_ i uniformly from the data set, we find that this estimator is unbiased:

\displaystyle \displaystyle \mathbb {E}[\hat{\mathrm{{\boldsymbol w}}}_{t+1}]\displaystyle = \mathrm{{\boldsymbol w}}_ t - \alpha _ t \mathbb {E}[ (\nabla f_ i)(\mathrm{{\boldsymbol w}}_ t) ]\displaystyle = \mathrm{{\boldsymbol w}}_ t - \alpha _ t (\nabla f)(\mathrm{{\boldsymbol w}}_ t)\displaystyle = \mathrm{{\boldsymbol w}}_{t+1}.

This is known as stochastic gradient descent.

In order to ensure that we use all available data, we should choose the maximum number of iterations to be several times larger than the data set. There are also variations on this scheme where the data point used at each step is selected sequentially an array of data points. In that case, the update rule would be

\displaystyle \displaystyle \hat{\mathrm{{\boldsymbol w}}}_{t+1}\displaystyle = \mathrm{{\boldsymbol w}}_ t - \alpha _ t (\nabla f_{t\text { mod }N})(\mathrm{{\boldsymbol w}}_ t).

A sequential stochastic gradient descent can be useful if selecting random data points on the fly is computationally expensive. This can occur for some storage mediums, such as hard drives, which have a slow random access time. By reading the data sequentially, we improve performance by ordering our read requests to the storage medium.

### SGD variance

1 point possible (graded)

However, the variance of this estimator can be quite large. This means that while on average, the estimator is equal to the whole data-set update rule, any individual \hat{\mathrm{{\boldsymbol w}}}_{t+1} can be quite scattered.

We can combat this variance in two ways. First, notice that

\displaystyle \displaystyle \textrm{Var}\left( \hat{\mathrm{{\boldsymbol w}}}_{t+1} \right)\displaystyle = \alpha _ t^2 \textrm{Var}\left( (\nabla f_ i)(\mathrm{{\boldsymbol w}}_ t) \right).

We can't control the variance of the gradients, that is dependent on our data set. What we can control is the step size, and by reducing the step size we also reduce the variance in the estimator.

Second, we can modify the estimator so that it computes an average over a small sample, \mathcal{S}, of size |\mathcal{S}| = k:

\displaystyle \displaystyle \tilde{\mathrm{{\boldsymbol w}}}_{t+1}\displaystyle = \tilde{\mathrm{{\boldsymbol w}}}_ t - \alpha _ t \frac{1}{k} \sum _{i \in \mathcal{S}} (\nabla f_ i)(\mathrm{{\boldsymbol w}}_ t),

where the sample is drawn uniformly from the population without replacement. Now the variance will be

\displaystyle \displaystyle \textrm{Var}\left( \tilde{\mathrm{{\boldsymbol w}}}_{t+1} \right)\displaystyle \approx \frac{\alpha _ t^2}{k} \textrm{Var}\left( (\nabla f_ i)(\mathrm{{\boldsymbol w}}_ t) \right),

when k is much smaller than the population size. So we can see that by increasing the size of the sample, we decrease the variance of the estimator as well. This is known as mini-batch stochastic gradient descent.

What happens to the variance if we choose the mini-batch to be the same size as the data set (k=N)?

Recall that the stochastic gradient descent estimator is unbiased:

\displaystyle \displaystyle \mathbb {E}[\hat{\mathrm{{\boldsymbol w}}}_ t]\displaystyle = \mathrm{{\boldsymbol w}}_ t.

The variance is then defined as

\displaystyle \displaystyle \textrm{Var}\left( \hat{\mathrm{{\boldsymbol w}}}_ t \right)\displaystyle = \mathbb {E}[(\hat{\mathrm{{\boldsymbol w}}}_ t - \mathrm{{\boldsymbol w}}_ t)(\hat{\mathrm{{\boldsymbol w}}}_ t - \mathrm{{\boldsymbol w}}_ t)^{\intercal }].

For the mini-batch, we have something similar, as it too is an unbiased estimator:

\displaystyle \displaystyle \textrm{Var}\left( \tilde{\mathrm{{\boldsymbol w}}}_ t \right)\displaystyle = \mathbb {E}[(\tilde{\mathrm{{\boldsymbol w}}}_ t - \mathrm{{\boldsymbol w}}_ t)(\tilde{\mathrm{{\boldsymbol w}}}_ t - \mathrm{{\boldsymbol w}}_ t)^{\intercal }].

But with the mini-batch estimator, if k=N, then the mini-batch gradient is just the same as the total gradient, and so we get \tilde{\mathrm{{\boldsymbol w}}}_ t = \mathrm{{\boldsymbol w}}_ t and so the variance is zero.

This makes sense: when the mini-batch is the same size as the data set, the update rule is no longer stochastic, as there is only one way to select the mini-batch (the entire data set, recall that the mini-batch is drawn without replacement). As it is no longer stochastic, there is no longer any variance in the gradients computed.

**Step size schedule**

Oftentimes, the variance of stochastic gradient descent is most problematic near the minimum.

When we are far from the minimum, the gradients for all data points tend to point in the same direction, as so the variance in the gradients is small.

But near the minimum, the gradients for each data point become more scattered in their directions. We can get an intuitive idea for why this is by examining each f_ i individually. Each f_ i has its own minimum, found by

\displaystyle \displaystyle \frac{\partial f_ i}{\partial \mathrm{{\boldsymbol w}}} (\mathrm{{\boldsymbol w}}_ i^{*})\displaystyle = 0

and denoted as \mathrm{{\boldsymbol w}}_ i^{*}.

The minimums for each f_ i are scattered closely around the true minimum for f as a whole. So when we are far from the true minimum, the gradients for each f_ i – which generally points towards \mathrm{{\boldsymbol w}}_ i^{*} – will tend to point in the same direction. But once we are close to the minimum, the individual data-point minimums \mathrm{{\boldsymbol w}}_ i^{*} will be scattered all around us, and so the gradients will tend to point in all different directions.

We could set a very small step size for the entire procedure, but this would be wasteful at the beginning when the variance is the gradients is smaller. Instead, we create a step size “schedule", which is an \alpha _ t that is a function of the step number, t. For example

\displaystyle \displaystyle \alpha _ t = \frac{1}{1+t}.

Now, the step size can start out large and then be reduced as we converge toward the minimum.