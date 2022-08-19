# -*- coding: utf-8 -*-
"""
Created on Mon Aug  15 11:19:50 2022

@author: neural.net_
"""
import numpy as np
import random
import matplotlib.pyplot as plt

def create_data(bias, slope, var):
    x = np.linspace(0, 5, 100).reshape(-1,1)
    y = x*slope + bias
    y += var*np.random.rand(x.shape[0],1)
    return x, y

def random_sample(x, y, num):
    idx = np.random.randint(0, x.shape[0], num)
    return x[idx], y[idx]

def linear_regression(X, Y):
    val = np.linalg.inv(X.T@X)@X.T@Y
    return val

def plot(x_, y_, slope, bias):
    fig, ax = plt.subplots()
    plt.title('Simple Linear Regression')
    ax.scatter(x_, y_, linewidth=2, label='Data Samples')
    x = np.linspace(0, max(x_), 100)
    y = bias + slope*x
    ax.plot(x,y, color = 'r', linewidth=4, label='Linear Approximation')
    ax.set_xlabel('x values')
    ax.set_ylabel('y values')
    ax.legend()


# Initialize data and sample variables.
bias = 1
slope = 0.4
var = 0.3
num_samples = 80

# Create data set for the chosen parameters and randomly sample a given number of data points.
x, y = create_data(bias, slope, var)
x_, y_ = random_sample(x,y,num_samples)

# Reshape input data for matrix operation.
ones = np.ones(len(x_)).reshape(-1,1)
X = np.stack((x_.flatten(), ones[:].flatten()), axis=-1)

# Linear regression.
vals = linear_regression(X, y_)

# Show results.
plot(x_,y_, vals[0], vals[1])
print('---------- Approximated Values')
print('Bias: ' + str(vals[1]) + '\nSlope:' + str(vals[0]))

