import numpy as np
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
#from scipy.misc import derivative

x = smp.symbols("x", real =True)
f = smp.exp(smp.sin(x))
df = smp.diff(f,x)
print("function")
smp.pprint(f)
print("derivative:",df)