import matplotlib.pyplot as plt
import numpy as np

def linear_equation(m, x, b):
    return m * x + b

def least_sqr(x, y):
    n = len(x)
    xSum = np.sum(x)
    ySum = np.sum(y)
    xySum = np.sum(x * y)
    x2 = np.sum(x**2)
    mfit = (n * xySum - xSum * ySum) / (n * x2 - xSum**2)
    bfit = (ySum - mfit * xSum) / n
    return mfit, bfit

np.random.seed(0)  # For reproducibility

x = np.arange(0, 4, 0.01)
mtru = 3
btru = 6
ytru = linear_equation(mtru, x, btru)

# Generate noise from normal distribution with mean=0 and std=0.2
noise = np.random.normal(0, 0.2, len(x))
ynoise = ytru + noise

mfit, bfit = least_sqr(x, ynoise)
yfit = linear_equation(mfit, x, bfit)

plt.scatter(x, ynoise, color='green', label="Noisy data", s=10)
plt.plot(x, yfit, color='magenta', label="Least Squares Fit", linewidth=2)
plt.plot(x, ytru, color='blue', label="True Line", linestyle='--', linewidth=2)
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y')
plt.title('Least Squares Fit vs True Line')
plt.grid(True)
plt.show()