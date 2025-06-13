import numpy as np
import matplotlib.pyplot as plt
x = []
y = []
def prime_find(n):
    prime = []
    a = 2
    while len(prime) < n:
        check = True
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                check = False
                break
        if check:
            prime.append(a)
        a += 1
    return prime

import time

max_n = int(input("time to find prime numbers: "))

for i in range(1, max_n + 1):
    start = time.perf_counter()
    primes = prime_find(i)
    end = time.perf_counter()
    time_taken = (end - start) * 1_000_000  # convert to microseconds
    x.append(i)
    y.append(time_taken)
plt.plot(x,y,color = "purple",linestyle = "solid")
plt.xlabel("number of primes")
plt.ylabel("time taken")
plt.title("NUMBER OF PRIMES VS TIME GRAPH")

plt.xticks(range(0,max_n +1,75))
plt.yticks(range(0,int(max(y)+10),1500))
plt.show()
    