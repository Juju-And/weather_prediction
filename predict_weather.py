import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
# print(repr(X))
Y = data.iloc[:, 1]
# print(type(Y))
plt.scatter(X, Y)
# plt.show()
plt.savefig('results/model_1.png')

# Building the model
a = 0
b = 0

L = 0.0001  # The learning rate
epochs = 1000  # The number of interations to perform gradient descent

n = float(len(X))  # Number of elements in X

# Performing Gradient Descent
for i in range(epochs):
    # print(type(a))
    # print(type(b))
    # print(type(X))
    Y_pred = a * X + b  # The current predicted value of Y
    D_a = (-2 / n) * sum(X * (Y - Y_pred))  # Derivative wrt a
    D_b = (-2 / n) * sum(Y - Y_pred)  # Derivative wrt b
    a = a - L * D_a  # Update a
    b = b - L * D_b  # Update b

# print(a, b)

# Making predictions
Y_pred = a * X + b
# print(repr(Y_pred))
plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
plt.xlabel("Day of the month")
plt.ylabel("Temperature in Celsius")
plt.figtext(.7, .8, "a = {}\nb = {}".format(a, b), fontsize=16)
# plt.show()
plt.savefig('results/model_2.png')
