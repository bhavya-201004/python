import numpy as np
n = int(input("Give size of array:"))
element = []
for i in range(n):
    m = int(input(f"Give element of {i+1} position:"))
    element.append(m)
a = np.array(element)
print(a)

largest = second_largest = float('-inf')


for num in a:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

            
if second_largest == float('-inf'):
    print("second largest number is: -1")
else:
    print("second largest number is:", second_largest) 
