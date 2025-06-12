import numpy as np
import matplotlib.pyplot as plt
 
x = [1,2,3,4,5,6,7,]
y = [1,4,9,16,25,36,49]

plt.plot(x,y,color = "red",linewidth = 1.5,linestyle = "dotted")

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("LINE GRAPH")
plt.rcParams['figure.dpi'] = 900


plt.show