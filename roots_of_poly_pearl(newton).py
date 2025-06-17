import sympy as smp
x = smp.symbols("x",real=True)
f1 = input("Enter the polynomial function f(x):")
f_e = smp.sympify(f1)

f_prime_e = smp.diff(f_e,x)

f = smp.lambdify(x,f_e, "numpy")
f_prime = smp.lambdify(x,f_prime_e,"numpy")


#def newton_raphson(xg,n,m=100):
   # for i in range(m):
     #   fx = f(xg)
     #   fpx = f_prime(xg)
       # if abs(fpx)<1e-12:
       #     print("derivative is zero.no soln found")
       #     return None
   # x1 = xg - fx/fpx
   # print(f"step {i}: x = {x1:.6f} , f(x)= {f(x1):.6f}")
   # if abs(x1 - xg)<n:
  #          return x1
   # xg = x1
   # print("didn't converge within the given iterations:")
    #return None
    
def newton_raphson(xg, n, m=100):
    for i in range(m):
        fx = f(xg)
        fpx = f_prime(xg)

        # Debug print
        print(f"Debug: At step {i}, xg = {xg}, f(x) = {fx}, f'(x) = {fpx}")

        if abs(fpx) < 1e-12:
           # print("Derivative is approximately zero. No solution found.")
            return None

        x1 = xg - fx / fpx
        print(f"Step {i}: x = {x1:.6f}, f(x) = {f(x1):.6f}")

        if abs(x1 - xg) < n:
            return x1

        xg = x1

    print("Didn't converge within the given iterations.")
    return None

xg= float(input("Enter initial guess:"))
n = float(input("Enter precision of zero(e.g 1e-6):" ))

root = newton_raphson(xg,n)
if root is not None:
    print(f"\nRoot found:{root:.6f}")