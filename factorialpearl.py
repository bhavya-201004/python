n=int(input("Enter number to find factorial:"))
factorial=1
for i in range(1,n+1):
    factorial*= i
print(factorial)



def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)

print(factorial(n))