def prime_find(n):
    prime = []
    a = 2
    while len(prime) < n:
        check = True
        for i in range (2,int(a**0.5 +1)):
            if a%i == 0:
                check = False
                break
        if check:
          prime.append(a)
        a +=1
    return prime

import time


n = int(input("How many prime number do you want:"))
primes = prime_find(n)
print("first",n,"primes numbers are:")
print(primes)




start = time.time()
prime_find(n)
end  = time.time()
print(f"\nFirst {n} prime numbers are:\n{primes}")
time_taken_ms = (end - start) * 1000
print(f"\nTime taken: {time_taken_ms:.3f} milliseconds")