import numpy as np

def create_matrix():
    m = int(input("Enter size of rows of matrix:"))
    n = int(input("Enter size of column of matrix:"))
    matrix = np.zeros((m,n),dtype = int)
    for i in range(m):
        for j in range(n):
            element = int(input(f"Enter elements at position({i+1},{j+1}):"))
            matrix[i,j] = element
    return matrix

a = create_matrix()
print("the matrix a is:")
print(a)

b = create_matrix()
print("the matrix b is:")
print(b)