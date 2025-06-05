n = int(input("enter number to check if this is prime:"))
if n == 2 or 3:
    print("this is prime")
for i in range(2,n-1):    
  if n%i == 0:
        print("this is composite")
        break
  else:
        print("this is prime")
        break
        