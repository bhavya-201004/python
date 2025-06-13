import sympy as smp


x = smp.symbols("x",real = True)
f = 16*x**2+8*x+4
df = smp.diff(f,x)
print("polynomial:")
print(f)
print("derivative:")
print(df)


g = smp.log(f)
dg = smp.diff(g,x)
print("logarithm:")
print(g)
print("derivative of g:")
print(dg)