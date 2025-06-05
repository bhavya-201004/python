def odd_even(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")
        
odd_even(90)

#recursion
def play(n):
    if n==0:
        return
    print(n)
    play(n-1)
    
play(10)