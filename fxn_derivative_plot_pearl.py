import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from scipy.optimize import fsolve

transformations = standard_transformations + (implicit_multiplication_application,)
x = smp.symbols("x", real=True)
local_dict = {"x": x, "sin": smp.sin, "cos": smp.cos, "tan": smp.tan, "exp": smp.exp, "log": smp.log, "ln": smp.log, "sqrt": smp.sqrt}

f_input = input("Enter the function f(x): ")
f_expr = parse_expr(f_input, local_dict=local_dict, transformations=transformations)
df_expr = smp.diff(f_expr, x)

xmin = float(input("Enter min x for plot: "))
xmax = float(input("Enter max x for plot: "))
x_vals = np.linspace(xmin, xmax, 1000)

f = smp.lambdify(x, f_expr, "numpy")
df = smp.lambdify(x, df_expr, "numpy")
diff_func = smp.lambdify(x, f_expr - df_expr, "numpy")

y_vals = f(x_vals)
dy_vals = df(x_vals)

def find_roots(fdiff, guesses):
    roots = []
    for guess in guesses:
        try:
            root = fsolve(fdiff, guess)[0]
            if not any(np.isclose(root, r, atol=1e-3) for r in roots):
                roots.append(root)
        except:
            continue
    return roots

initial_guesses = np.linspace(xmin, xmax, 20)
roots = find_roots(diff_func, initial_guesses)

plt.plot(x_vals, y_vals, label=f"f(x) = {f_expr}", color="blue")
plt.plot(x_vals, dy_vals, label=f"f'(x) = {df_expr}", color="purple", linestyle="dotted")

if roots:
    print("\nApproximate intersection points (f(x) = f'(x)):")
    for r in roots:
        y_r = f(r)
        print(f"  x = {r:.4f}, y = {y_r:.4f}")
        plt.plot(r, y_r, 'ro')
        plt.annotate(f"({r:.2f}, {y_r:.2f})", (r, y_r), textcoords="offset points", xytext=(5, 5), fontsize=9, color='darkred')
else:
    print("\nNo real intersection points found numerically.")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot of f(x) and f'(x)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
