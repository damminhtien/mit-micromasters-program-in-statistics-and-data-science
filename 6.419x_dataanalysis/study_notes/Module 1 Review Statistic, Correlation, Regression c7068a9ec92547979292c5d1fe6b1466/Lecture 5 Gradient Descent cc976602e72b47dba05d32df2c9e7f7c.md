# Lecture 5: Gradient Descent

**Please take note:** In these lectures and exercises, we will use \hat{w} to denote the estimator for the model parameters instead of the \hat{\beta } used in the last lecture and exercises. This change in notation is due to a difference in convention between the fields of optimization and statistics. Gradient descent is usually discussed in the context of optimization, where the \hat{w} notation is common. The choice of the letter w comes about due to model parameters often being called “weights" in this field.

For example, in the last lecture we found the solution,  $\hat{\mathrm{{\boldsymbol \beta }}}$, to the ordinary least squares problem as

$$
\displaystyle \displaystyle \hat{\mathrm{{\boldsymbol \beta }}}\displaystyle = \arg \min _{\mathrm{{\boldsymbol \beta }}} \sum _{i=1}^ N \left(Y_ i - \mathrm{{\boldsymbol x}}_ i^{\intercal }\mathrm{{\boldsymbol \beta }}\right)^2.
$$

In this alternative notation, we would be minimizing against $\hat{\mathrm{{\boldsymbol w}}}$ to find the estimator:

$$
\displaystyle \displaystyle \hat{\mathrm{{\boldsymbol \omega }}}\displaystyle = \arg \min _{\mathrm{{\boldsymbol w}}} \sum _{i=1}^ N \left(Y_ i - \mathrm{{\boldsymbol x}}_ i^{\intercal }\mathrm{{\boldsymbol w}}\right)^2.
$$

# **1. Convexity**

In this unit, we will

- Define a loss function and how it is used in optimization.
- Discuss the difference between a global and a local minimum of a loss function.
- Determine if a critical point of the loss function is a minium or a maximum.
- Define the convexity property of a function three ways, and show how each definition is related to the others.

Recall that for the Ordinary Least Squares (OLS) problem

$$
\displaystyle \displaystyle \hat{\mathrm{{\boldsymbol \omega }}}\displaystyle = \arg \min _{\mathrm{{\boldsymbol w}}} \sum _{i=1}^ N \left(Y_ i - \mathrm{{\boldsymbol x}}_ i^{\intercal }\mathrm{{\boldsymbol w}}\right)^2,
$$

we can find the minimum by writing the sum of the squares, $f(\mathrm{{\boldsymbol w}})$, as

$$

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle = \sum {i=1}^ N \left(Y i - \mathrm{{\boldsymbol x}}_ i^{\intercal }\mathrm{{\boldsymbol w}}\right)^2.
$$

Then, we take the derivative of the sum-of-squares and set it to zero:

$$
\displaystyle \displaystyle \left.\frac{\partial f}{\partial \mathrm{{\boldsymbol w}}}\right|_{\mathrm{{\boldsymbol w}} = \hat{\mathrm{{\boldsymbol w}}}}\displaystyle = 0
$$

**Note:** This f quantity is our optimization target, as we're trying to make it as small as possible. In the parlance of the field of optimization, this f is often called the “loss function" (sometimes “cost function" is used). The idea is that it quantifies something that is “lost" or “cost" by a choice of \mathrm{{\boldsymbol w}} and we're trying to minimize this loss.

We seek a condition that implies that any critical point is unique, and that this critical point is a minimum (and thus the global minimum). This condition is called **convexity**. If we arrange our optimization problems such that they are convex, then they will be much easier to solve. Note that a convex function may not have any critical points at all, convexity only guarantees that the number of critical points is either zero or one.

Recall the loss function:

![](https://courses.edx.org/assets/courseware/v1/1649264417c2eb6f4d00dfeac398d043/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_convexity_hatplot.png)

And now observe the derivative of the loss function:

![](https://courses.edx.org/assets/courseware/v1/d266dd21d0b81a6f3393db83d42d2a96/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_convexity_hatplot_grad.png)

We see that the two minima, A and B, correspond to points where the derivative curve intersects the w-axis. Observe, also, that the point where the derivative curve intersects the w-axis, always corresponds to a positive slope, showing that f^{\prime \prime }(w) > 0 there.

This is important: at the global minimum the slope of the derivative curve is positive, so the only way for there to be another (local) minimum is if the curve dips back below the x-axis so that it can again intersect the x-axis with positive slope. And, in fact, we see this in the curve above. After point A, the curve turns over, goes below the axis, and then turns back and intersects the axis at point B with positive slope.

The only way for the derivative curve to do this is for it to have, at some point, a **negative** slope. There means that for a second minimum to exist somewhere, we must have that f^{\prime \prime }(w) < 0 for some range of wvalues.

This allows us to create the following sufficient condition for the uniqueness of the minimum of a loss function: If the second derivative is non-negative everywhere (f^{\prime \prime }(w) \geq 0 for all w) then this implies that the critical point of the function (if it exists) is the unique global minimum.

Such a loss-function is called “convex". For a twice differentiable loss function f, it is convex if and only if the second derivative is non-negative everywhere. We should immediately note that this is not the only way to define convexity.

### Lower bound convexity

1 point possible (graded)

Remember that at the global minimum is a lower bound on the entire loss function. It turns out that, for a convex loss function, every point on the curve can be used to define a line that is a lower bound for the whole function.

This can be shown by the Taylor expansion of the loss function, i.e.,

\displaystyle \displaystyle f(w)\displaystyle = f(w_0) + f'(w_0)(w - w_0) + R_1(w;w_0),

where R_1(w) is the first order remainder function for the Taylor series. This remainder function encapsulates all the higher order derivatives:

\displaystyle \displaystyle R_1(w;w_0)\displaystyle = \frac{1}{2} f^{\prime \prime }(w_0) (w - w_0)^2 + \frac{1}{6} f{\prime \prime \prime }(w_0) (w - w_0)^3 + \mathcal{O}(|w-w_0|^4).

We can examine this remainder by use of the Lagrange form of the remainder function. There exists some w_{*}where w_{*} lies in the interval between w_0 and w such that

\displaystyle \displaystyle R_1(w;w_0)\displaystyle = \frac{f^{\prime \prime }(w_{*})}{2} (w - w_0)^2.

Note that (w - w_0)^2 \geq 0 and for a convex function, f^{\prime \prime }(w_{*}) \geq 0 also. Thus R_1(w;w_0) \geq 0. From this we can conclude that

\displaystyle \displaystyle f(w)\displaystyle = f(w_0) + f'(w_0)(w - w_0) + R_1(w;w_0)\displaystyle \geq f(w_0) + f'(w_0)(w - w_0)\displaystyle = f'(w_0) w + (f(w_0) - f'(w_0) w_0).

So the loss curve, f(w), has a lower bound which is a line with slope f'(w_0) and intercept f(w_0) - f'(w_0) w_0. It is important to note that this is true for any choice of w_0. That is: for any point, w_0, on the curve, we can construct a lower bound function for f(w) where this lower bound is a line that is tangent to f(w_0).

Take the following convex loss function as an example:

![](https://courses.edx.org/assets/courseware/v1/eda85b0e77b2d57f9dc9fa521ced77fa/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_convexity_lowerbound_plot.png)

The blue curve is the loss function itself, while the orange line is the lower bound constructed at w_0.

We can use this lower bound as a definition of convexity as well. A loss function f(w) is convex if and only if the tangent lines,

\displaystyle \displaystyle \ell (w)=f(w_0) + f'(w_0)(w - w_0),

form a lower bound for f(w) for all choices of w_0.

Is the following function convex?

![](https://courses.edx.org/assets/courseware/v1/879135f207215f8195301057195a9eab/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_convexity_sin_plot.png)

The loss function is not convex. We can see this two ways:

- The function has a maximum, so there is location [mathjaxinline]w'[/mathjaxinline] where [mathjaxinline]f^{\prime \prime }(w') < 0[/mathjaxinline], thus the function is not convex by the second order derivative argument.
- There are multiple choices of [mathjaxinline]w_0[/mathjaxinline] (particularly on the left hand side of the curve) where the tangent line does not form a lower bound. That is, if we drew the tangent line at one of these points, part of the curve would intersect with the tangent line and go below it. Thus the function is not convex by the tangent lower bound argument.

### Chord convexity

2 points possible (graded)

From the previous examples, we have seen that convex functions make a “U" shape. It is this shape from which the name “convex" is derived.

If a polygon is convex, then any line drawn between two points on the edge of the polygon will not leave the interior of the polygon. That is, we can't draw a line between two points on the edge of a convex polygon such that the line crosses outside the polygon.

If a function is convex, then the curve of the function describes the edge of a convex shape. Any points above the curve are considered to be inside the shape, while any points below the curve are considered outside the shape.

Thus, we can use the same line drawing argument for defining the convexity of a curve. Consider, again, the following convex loss function:

![](https://courses.edx.org/assets/courseware/v1/17f5af43274dc28824239bb9793ffe47/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_convexity_chord.png)

The blue line is the convex loss function. Two points, w_ a and w_ b are selected on the curve and a line, drawn black, is drawn between them. This line is called a chord. We can see that the chord lies above the curve, so that the curve does not intersect with the chord at any point. This is true for any pair of points, w_ a and w_ b on the curve.

To prove this, we will make use of the previously defined tangent lower bound. Our goal is to show that any point along the chord is an upper bound for the corresponding point along the curve.

We will parameterize this point along the chord using \alpha, so that

\displaystyle \displaystyle w_\alpha\displaystyle = \alpha w_ a + (1-\alpha ) w_ b,\displaystyle f_\alpha\displaystyle = \alpha f(w_ a) + (1-\alpha ) f(w_ b),

where 0 < \alpha < 1. Therefore, (w_\alpha , f_\alpha ) is a point on the chord and (w_\alpha , f(w_\alpha )) is the corresponding point on the curve (shown by the dotted black line).

We can now construct the tangent lower bound at w_\alpha:

\displaystyle \displaystyle f(w)\displaystyle \geq f(w_\alpha ) + f'(w_\alpha ) (w - w_\alpha ),

which is shown by the orange line.

We know from this bound that f(w_ a) and f(w_ b) lie above the tangent line (as shown by the dashed green lines). Thus, we can see visually that the point on the chord must also lie above the tangent line (because the tangent line and chord do not intersect).

We can prove this by first evaluating the bound explicitly for w_ a and w_ b:

\displaystyle \displaystyle f(w_ a)\displaystyle \geq f(w_\alpha ) + f'(w_\alpha ) (w_ a - w_\alpha ),\displaystyle f(w_ b)\displaystyle \geq f(w_\alpha ) + f'(w_\alpha ) (w_ b - w_\alpha ).

Now, we can find a lower bound on f_\alpha:

\displaystyle \displaystyle f_\alpha\displaystyle = \alpha f(w_ a) + (1-\alpha ) f(w_ b)\displaystyle \geq \left(\alpha f(w_\alpha ) + (1-\alpha ) f(w_\alpha )\right) + f'(w_\alpha ) \left[ \alpha (w_ a - w_\alpha ) + (1-\alpha )(w_ b - w_\alpha ) \right]\displaystyle = f(w_\alpha ) + f'(w_\alpha ) \left[ \alpha \left((1-\alpha ) w_ a - (1-\alpha ) w_ b\right) + (1-\alpha )\left(\alpha w_ b - \alpha w_ a\right) \right]\displaystyle = f(w_\alpha ) + f'(w_\alpha ) \left[ \alpha (1-\alpha ) (w_ a - w_ b) - (1-\alpha ) \alpha (w_ a - w_ b) \right]\displaystyle = f(w_\alpha ).

Thus f_\alpha \geq f(w_\alpha ) for all \alpha \in (0, 1) which completes the proof.

Which of the following functions are convex?

![](https://courses.edx.org/assets/courseware/v1/7fb2ad2c8e0b0e73a1fdaafdc7df5f8b/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_convexity_func_grid.png)

- [ ]  
    - [ ]  
    - [ ]  
    - [ ]  

unanswered

And which of those functions have a global minimum?

- [ ]  

Function (A) is indeed convex, as the second derivative of [mathjaxinline]e^ x[/mathjaxinline] is [mathjaxinline]e^ x[/mathjaxinline] which is positive everywhere. However, it does not have a global minimum, as it has no critical points: [mathjaxinline]e^ x \neq 0[/mathjaxinline] everywhere.

Function (B) is also convex. Remember that the definitions of convexity use greater-than-or-equal relations. The second derivative of a line may be zero, but this is technically non-negative as so the line is convex. There is a more restrictive form of convexity called strict convexity that the line does not posses. Much like the exponential, the line has no global minimum despite being convex, as the derivative is non-zero everywhere and thus there are no critical points.

Function (C) is a peicewise function, that is composed of two quadratics. Each quadratic, on its own, is a convex function with a global minimum. However, the peicewise combination is not convex. We can't use the second derivate criterion as the peicewise function is not differentiable at the break. We can use the chord or tangent lower bound criteria, and this function fails both. Despite this, the function has a global minimum.

Function (D) is not convex, though it may look like it at first. Careful examination of the curve will show that it fails the chord and tangent lower bound criteria (consider the tangent near the edges of the bell). If we take the second derivative, we also find that there are places where it is negative, so it fails this criterion too. However, it does have a global minimum, as there is just one critical point and the second derivative is positive at that point.

Something important to consider is that if we take function (D), and transform it using a logarithm, [mathjaxinline]f(w)' = -\ln {(-f(w))} = x^2[/mathjaxinline] then we get a convex function with a global minimum. It is common to use transformation to turn non-convex problems into convex one, and the logarithm is a very common transformation for doing this.

# **2. Multidimensional convexity and local optimization**

In this unit, we will

- Define a multidimensional loss function as well as its critical points.
- Discuss conditions for which a multidimensional critical point is a maximum or minimum.
- Go into further depth on the properties of a saddle point.
- Define two conditions for convexity in multiple dimensions.

### Multidimensional Taylor expansion

1/1 point (graded)

Now let us consider loss functions that are parameterized by multiple weights. We'll arrange the weights such that they form a column vector, \mathrm{{\boldsymbol w}} \in \mathbb R^ d. Then, the loss function is a scalar-valued function of this vector of parameters: f(\mathrm{{\boldsymbol w}})\in \mathbb R.

We can expand f(\mathrm{{\boldsymbol w}}) around a point in parameter space, \mathrm{{\boldsymbol w}}_0, through use of the multidimensional Taylor expansion:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle = f(\mathrm{{\boldsymbol w}}_0) + (\nabla f)(\mathrm{{\boldsymbol w}}_0) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0) + \frac{1}{2} (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0)^{\intercal }(\nabla \nabla f) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0) + \mathcal{O}(\| \mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0\| ^3),

where (\nabla f)(\mathrm{{\boldsymbol w}}_0) is the gradient of f(\mathrm{{\boldsymbol w}}) evaluated at \mathrm{{\boldsymbol w}}_0, and (\nabla \nabla f) is the Hessian matrix which contains all the second derivatives of f.

### Critical points

1 point possible (graded)

Much of the previous discussion transfers over to the multidimensional case.

To start, the critical points of f(\mathrm{{\boldsymbol w}}) are defined as the solutions, \mathrm{{\boldsymbol w}}', to

\displaystyle \displaystyle (\nabla f)(\mathrm{{\boldsymbol w}}')\displaystyle = 0,

where the value on the right hand side is the zero vector.

At a critical point, the Taylor expansion is

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle = f(\mathrm{{\boldsymbol w}}_0) + \frac{1}{2} (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}')^{\intercal }(\nabla \nabla f) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}') + \mathcal{O}(|\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0|^3).

In the immediate vicinity of the critical point, the behavior of the function is governed by the Hessian term: (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}')^{\intercal }(\nabla \nabla f) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}'). Let \mathrm{{\boldsymbol v}} = \mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}' and {\boldsymbol H} = \nabla \nabla f so that we can write this term as \mathrm{{\boldsymbol v}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol v}}.

Now, if

\displaystyle \displaystyle \mathrm{{\boldsymbol v}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol v}}\displaystyle > 0

for all non-zero vectors \mathrm{{\boldsymbol v}} \neq 0, then the critical point is a minimum; much like how we concluded in the one-dimensional case that if the second derivative of the loss function was positive, then we had a minimum.

The property \mathrm{{\boldsymbol v}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol v}} > 0 for all \mathrm{{\boldsymbol v}}\neq 0 is a property of the matrix {\boldsymbol H}. A matrix {\boldsymbol H} is called positive definite if and only if this property is true. In addition, the eigenvalues of a real-valued symmetric matrix are all positive if and only if the matrix is positive definite. If this case, our Hessian is always real-valued and symmetric, so we can use the eigenvalues to investigate the positive definite property for the Hessian.

It follows that if a real-valued symmetric matrix is positive definite, then this implies that the determinant is also positive.

Recall that the determinant is the product of all the eigenvalues of the matrix.

### Saddle points

1 point possible (graded)

In the one dimensional case we found that if the second derivative is zero at a critical point, then that critical point may be a saddle point. In multiple dimensions, we can get more information out of the Hessian matrix and are thus able to make stronger statements on the existence of a saddle point.

First, let us examine a relaxation on the positive definite property of a matrix. A matrix {\boldsymbol H} is called a positive semi-definite matrix if and only if

\displaystyle \displaystyle \mathrm{{\boldsymbol v}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol v}}\displaystyle \geq 0

for all non-zero vectors \mathrm{{\boldsymbol v}} \neq 0. In addition, a real-valued symmetric matrix is positive semi-definite if and only if all the eigenvalues of the matrix are non-negative.

Certainly all positive definite matrices are also positive semi-definite. But if a real-valued symmetric matrix has all positive eigenvalues except for one or more zero eigenvalues, then the matrix is positive semi-definite but not positive definite. More importantly, if \mathrm{{\boldsymbol v}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol v}} = 0 for all vectors \mathrm{{\boldsymbol v}}, then the matrix {\boldsymbol H} is also positive semi-definite.

This leaves us in a situation much like we were in with the one dimensional case. A Hessian matrix this is entirely zero could be a minimum, or a maximum, or a saddle point. For example, the loss functions

\displaystyle \displaystyle f(w_1, w_2)\displaystyle = w_1^4 + w_2^4,\displaystyle f(w_1, w_2)\displaystyle = w_1^4 - w_2^4,\displaystyle f(w_1, w_2)\displaystyle = - w_1^4 - w_2^4,

all have zero matrices for their Hessian matrix at the critical point w_1=w_2=0; but the first has a minimum, the second a saddle point, and the third a maximum.

While a zero matrix fits the definition of a positive semi-definite matrix, all the eigenvalues of a zero matrix must be zero. This suggests that if we examine the eigenvalues directly, we might get a clearer picture.

Recall that each eigenvalue is associated with an eigenvector, and the eigenvectors describe a direction that the matrix acts upon. For the Hessian matrix at a critical point, we can interpret its eigenvalue-eigenvector pair as follows: the eigenvector is a vector that points towards a direction away from the critical point, and the eigenvalue shows if the curvature of f(\mathrm{{\boldsymbol w}}) is positive, negative, or zero in that direction.

**Note:** We will use the word “curvature" here to mean the rate of change of the gradient (so the sign and magnitude of the second derivative). In geometry, there are many different notions of curvature, so you may see the term defined differently in other contexts.

If a Hessian matrix has at least one positive eigenvalue, then we know that there is a direction away from the critical point where the loss function curves upwards. Meanwhile, if the same Hessian matrix also has at least one negative eigenvalue, then we know that there is a direction away from the critical point where the loss function curves downwards. A mixture of curving upwards and downwards is the definition of a saddle point, so we now know that the critical point associated with this Hessian is a saddle point.

Take, for example, the following loss function, shown below:

![](https://courses.edx.org/assets/courseware/v1/5d2fe2600b6c1439b9003baef19fa1ff/asset-v1:MITx+6.419x+2T2024+type@asset+block/images_convexity_saddle.png)

In this example, a saddle point is located at the origin (where the black vertical line intersects the surface). The black vector is an eigenvector that points in the direction of positive curvature. The red vector is an eigenvector that points in the direction of negative curvature.

In general, a real-valued symmetric matrix with both positive and negative eigenvalues is called an indefinite matrix, and the product \mathrm{{\boldsymbol v}}^{\intercal }{\boldsymbol H} \mathrm{{\boldsymbol v}} for any specific \mathrm{{\boldsymbol v}} may be positive, negative, or zero.

We can now find one condition for convexity in multiple dimensions: f is convex if and only if the Hessian is positive semi-definite everywhere.

Just as in the one-dimensional case, we can write the Taylor expansion with a remainder term, R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_0):

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle = f(\mathrm{{\boldsymbol w}}_0) + (\nabla f)(\mathrm{{\boldsymbol w}}_0) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0) + R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_0).

It turns out that there is some \mathrm{{\boldsymbol w}}_{*} that is an element of the line between \mathrm{{\boldsymbol w}} and \mathrm{{\boldsymbol w}}_0 such that

\displaystyle \displaystyle R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_0)\displaystyle = \frac{1}{2} (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0)^{\intercal }(\nabla \nabla f)(\mathrm{{\boldsymbol w}}_{*}) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0).

If the loss function is convex, then the Hessian is positive semi-definite, so by definition R_1(\mathrm{{\boldsymbol w}};\mathrm{{\boldsymbol w}}_0) \geq 0; and, in analogy to the one dimensional case, we find a lower bound

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}})\displaystyle \geq f(\mathrm{{\boldsymbol w}}_0) + (\nabla f)(\mathrm{{\boldsymbol w}}_0) (\mathrm{{\boldsymbol w}} - \mathrm{{\boldsymbol w}}_0).

In two dimensions, the expression on the right is an equation of a plane. In more than two dimensions, it is the equation of a hyperplane.

Thus, we have found a **tangent hyperplane** that is a lower bound for the loss function. And this tangent hyperplane exists for all choices of \mathrm{{\boldsymbol w}}.

Much like in the one dimensional case, we have the following condition: the loss function f(\mathrm{{\boldsymbol w}}) is convex if and only if there exists a lower bound tangent hyperplane for all \mathrm{{\boldsymbol w}}.

# **3. Quadratic minimization and gradient descent**

In this unit, we will

- Create a local, quadratic approximation for a function at a specific point.
- Use this to create an iterative process for finding the minimum of a convex function using the Hessian.
- Adapt this method for situations where we don't know or can't find the Hessian matrix.
- Use this adaption to define the gradient descent method.

Although convexity ensures that a loss function has some nice properties – such as a unique (global) minimum – it does not guarantee that the loss function can be solved exactly.

For example, the following loss function

\displaystyle \displaystyle f(x)\displaystyle = x^4 - \frac{x^3}{5} + \frac{x^2}{4} - \frac{x}{3}

is convex; but, as a forth order polynomial, it has no simple closed form equation for the minimum.

Instead of trying to find a single equation for the minimum, we can make a guess at the minimum and iteratively refine this guess to bring it closer to the true minimum. Let the initial guess for the minimum be denoted as w_0. We can now approximate the loss function and use this approximation to refine our guess.

Previously, we found that a convex loss function has a lower bound

\displaystyle \displaystyle f(w)\displaystyle \geq f(w_0) + f'(w_0) (w - w_0);

however, this would not make a particularly useful approximation for our current problem, as the line equation on the right hand side has no minimum.

Instead, we can go one order up. Recall that the lower bound was derived from the Taylor expansion

\displaystyle \displaystyle f(w)\displaystyle = f(w_0) + f'(w_0) (w - w_0) + \frac{1}{2} f^{\prime \prime }(w_0) (w - w_0)^2 + \mathcal{O}(|w-w_0|^3).

We can create an approximation, denoted by g_0, by truncating this expansion at the second order:

\displaystyle \displaystyle g_0(w)\displaystyle = f(w_0) + f'(w_0) (w - w_0) + \frac{1}{2} f^{\prime \prime }(w_0) (w - w_0)^2

As f is convex, we know that f^{\prime \prime }(w_0) \geq 0, and so g_0 will also be convex, and has a global minimum that we can find.

### Newton's method of minimization

1 point possible (graded)

Using this approximation, we can find the minimum by taking the derivative with respect to w:

\displaystyle \displaystyle \frac{\partial g_0}{\partial w}(w)\displaystyle = f'(w_0) + f^{\prime \prime }(w_0) (w - w_0),

setting this derivative to zero at w=w_1, gives the location of the minimum, w_1, at

\displaystyle \displaystyle w_1\displaystyle = w_0 - \frac{f'(w_0)}{f^{\prime \prime }(w_0)}.

This can be repeated iteratively. Let w_ t be the current guess at iteration step t, then the next guess is

\displaystyle \displaystyle w_{t+1}\displaystyle = w_ t - \frac{f'(w_ t)}{f^{\prime \prime }(w_ t)}.

This is known as Newton's method of optimization.

**Note:** We need to be careful of the possibility that f^{\prime \prime }(w_ t) is zero. For a practical algorithm, we would need to check if the second derivative is very small, and either terminate the algorithm, or threshold it to a larger positive value so as to allow the algorithm to continue.

In multiple dimensions this generalizes by using the gradient, \nabla f, and the Hessian matrix, \nabla \nabla f:

\displaystyle \displaystyle \mathrm{{\boldsymbol w}}_{t+1}\displaystyle = \mathrm{{\boldsymbol w}}_ t - \left[ (\nabla \nabla f)(\mathrm{{\boldsymbol w}}_ t) \right]^{-1} (\nabla f)(\mathrm{{\boldsymbol w}}_ t)^{\intercal }.

(Note that the second term in this expression can also be written as \left[ (\nabla \nabla f)(\mathrm{{\boldsymbol w}}_ t) \right]^{-1} (\nabla f)(\mathrm{{\boldsymbol w}}_ t) when a column vector gradient is being used instead of a row vector gradient.)

---

The iterative procedure of Newton's method requires some condition to stop the iteration.

There is no single correct condition, but a common condition is to stop when the norm of the gradient is below some threshold, \epsilon, that is very close to zero:

\displaystyle \displaystyle {| | (\nabla f)(\mathrm{{\boldsymbol w}}_ t) | |}^2\displaystyle < \epsilon .

Another is to also compute the value of the loss function, f(\mathrm{{\boldsymbol w}}_ t), at each iteration, and then stop when the difference between the functions is below a threshold, \epsilon, that is close to zero:

\displaystyle \displaystyle f(\mathrm{{\boldsymbol w}}_{t-1}) - f(\mathrm{{\boldsymbol w}}_{t})\displaystyle < \epsilon .

### Gradient descent

Newton's method is a simple and effective way of minimizing a convex function. However, it requires the computation of the Hessian matrix, \nabla \nabla f.

It is quite common that the Hessian is too computationally demanding to compute. In these cases, we must take a guess at the value of the Hessian.

Let the guess be

\displaystyle \displaystyle (\nabla \nabla f)(\mathrm{{\boldsymbol w}}_ t)\displaystyle \approx \frac{1}{\alpha } {\boldsymbol I},

where \alpha is some positive real number, and I is the identity matrix.

Now the iterative update procedure becomes

\displaystyle \displaystyle \mathrm{{\boldsymbol w}}_{t+1}\displaystyle = \mathrm{{\boldsymbol w}}_ t - \alpha (\nabla f)(\mathrm{{\boldsymbol w}}_ t)^{\intercal }.

This is called gradient descent, as this procedure requires knowledge of only the gradient. The parameter \alphais called the step size. At each iteration, gradient descent moves \mathrm{{\boldsymbol w}}_ t in the opposite direction of the gradient (remember the gradient points “uphill") by a distance equal to the norm of the gradient times the step size parameter \alpha.

Will gradient descent work for non-convex functions? Hint: see if you can come up with some loss functions where gradient descent will fail.

The correct answer is:

**Partially: if there is a minimum, gradient descent may find it, but there is no guarantee.**

### Explanation:

- **Gradient Descent in Non-Convex Functions**: Gradient descent can be applied to non-convex functions, but its performance and guarantees change compared to convex functions.
- **Local Minima and Saddle Points**: In non-convex functions, there can be multiple local minima, saddle points, and possibly a global minimum. Gradient descent might converge to a local minimum or get stuck at a saddle point rather than finding the global minimum.
- **No Guarantee**: There is no guarantee that gradient descent will find the global minimum in a non-convex function. It might find a local minimum, and whether this local minimum is satisfactory depends on the specific problem and requirements.

### Examples of Gradient Descent Failing in Non-Convex Functions:

1. **Multiple Local Minima**:
\[
f(x) = \sin(x) + 0.1x
\]
Gradient descent might get stuck in one of the many local minima of the sine function, depending on the starting point.
2. **Saddle Points**:
\[
f(x, y) = x^2 - y^2
\]
Gradient descent can get stuck at the saddle point at (0, 0), where the gradient is zero but it is not a minimum.

Therefore, while gradient descent can be used on non-convex functions, its effectiveness is limited by the nature of the function, and it might not always find the global minimum.