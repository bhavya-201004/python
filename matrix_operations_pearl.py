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


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
        
        
a = create_matrix()
print("the matrix a is:")
print_matrix(a)

b = create_matrix()
print("the matrix b is:")
print_matrix(b)


def add_matrix(m,n):
    result = []
    for i in range (len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(int(m[i][j]+n[i][j]))
        result.append(row)
    return result

if a.shape != b.shape:
    print("Matrix add/sub is not possible. Matrices must have the same dimensions.")

c = add_matrix(a,b)
print("the sum of the given matrices is:")
print_matrix(c) 



def sub_matrix(m,n):
     result = []
     for i in range (len(m)):
         row = []
         for j in range(len(m[0])):
             row.append(int(m[i][j]-n[i][j]))
         result.append(row)
     return result 

d = sub_matrix(a,b)
print("the difference of the given matrices is:")
print_matrix(d) 



def product_matrix(m,n):
    x1 , y1 = len(m) , len(m[0])
    x2 , y2 = len(n) , len(n[0])
    if x2 != y1:
        print("dimension of matrix is not satisfied for multiplication")
    else:
        product = [[0 for _ in range(y2)] for _ in range(x1)]
    for i in range(x1):
        for j in range(y2):
            for k in range(y1):
             product[i][j] += m[i][k] * n[k][j]
    return product
     

e = product_matrix(a,b)
print("product of A*B is:")
print_matrix(e)