def sum_upto(n):
    if n==0:
        return 0
    return n + sum_upto(n-1)
    
    
print(sum_upto(10))






#recursion
def play(n):
    if n==0:
        return
    print(n)
    play(n-1)
    
play(10)






def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)

print(factorial(n))