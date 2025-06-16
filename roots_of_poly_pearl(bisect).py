import sympy as smp

x = smp.symbols("x",real = True)
f1 = input("Enter the function f(x):")
f_e = smp.sympify(f1)
f = smp.lambdify(x,f_e,"math")
##bisection method
def bisection(a,b,n):
    if f(a)*f(b)>=0:
        print("interval is not correct:f(a) and f(b) must have oppositre signs")
        return None
    step = 0
    while(b-a) >= n:
        c = (a+b)/2
        print(f"Step {step}:c ={c:.6f}, f(c) ={f(c):.6f}")
        if f(c) == 0.0:
           break
        if f(c)*f(a)<0:
           b = c
        else:
           a = c
        step +=1
        
    return c   

i = float(input("give lower limit of f:"))
j = float(input("give upper limit of f:"))
m = float(input("give precision to find root(e.g 1e-6):"))

root = bisection(i,j,m)
if root is not None:
    print(f"\napproximate root is:{root:.6f}")