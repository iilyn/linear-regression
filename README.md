# linear-regression
## Simple Linear Regression

Simple linear regression is an approach to model the underlying data $D$ by using the linear relation $y = mx +b$ between the independet variable $x$ and the dependent variable $y$.

<p align="center">
<img src = "https://user-images.githubusercontent.com/110230895/185675894-7228b543-9c1a-42a1-9d1c-5112a485465c.png"\>
</p>

In the following, the regression is dony by using the least squares appraoch. 
Thereby, the optimal model parameterization $\theta = [b, m]^T$, where $b$ is the bias and $m$ is the slope, is computed by using the mean sqaured error (MSE) loss:

```math
MSE = \frac{1}{N} \sum_{i=1}^N (y_i - (mx_i +b))^2,
```
for each sample $i \in N$.

The closed form solution for the optimal regression parameterization is computed by
```math
\theta = \left( \mathbf{X}^T\mathbf{X} \right) ^{-1} \mathbf{X}^TY,
```
where ${X} \in \mathbb{R}^{N\times (M+1)}$ holds the $N$ data samples for the $M$ independent variables.
