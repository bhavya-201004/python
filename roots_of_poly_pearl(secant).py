import sympy as smp
x = smp.symbols("x",real=True)
f1 = input("Enter the polynomial function f(x):")
f_e = smp.sympify(f1)
f = smp.lambdify(x,f_e, "numpy")


def secant_method(f,x0,x1,n=1e-6,m=100):
    for i in range(m):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if abs(f_x1 - f_x0)<1e-14:
            print("denominator is very small,no soln found")
            return None
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        print(f"Iteration {i+1}: x0 = {x0:.6f}, x1 = {x1:.6f}, x2 = {x2:.6f}, f(x2) = {f(x2):.6e}")
        
        if abs(x2-x1) < n:
            print("converged")
            return x2
        x0, x1 = x1, x2
    print("did not converge within given iterations")
    return None

x0 = float(input("Enter initial guess x0: "))
x1 = float(input("Enter initial guess x1: "))
n = float(input("Enter tolerance (e.g., 1e-6): "))

root = secant_method(f, x0, x1, n)

if root is not None:
    print(f"\nEstimated root using Secant Method: {root:.6f}")
else:
    print("No root found within tolerance.")