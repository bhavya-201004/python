import scipy as sp
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt


x = smp.symbols("x",real = True)
f = -2*x**2
df = smp.diff(f,x)
print("function:")
print(f)
print("derivative:")
print(df)


f_lambdified = smp.lambdify(x, f, modules=['numpy'])

x_vals = np.linspace(-10, 10, 400)
y_vals = f_lambdified(x_vals)


plt.plot(x_vals,y_vals,label='f(x) = 2x^2')
plt.xlabel("X-axis")
plt.ylabel("Function")
plt.title("FUNCTION VS VARIABLE")
plt.legend()
plt.show()
