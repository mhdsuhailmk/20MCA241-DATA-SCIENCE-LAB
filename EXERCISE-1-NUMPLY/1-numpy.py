#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np

#MATRIX 1
r1 = int(input("ENTER THE NO. OF ROWS OF MATRIX 1:"))
c1 = int(input("ENTER THE NO. OF COLUMNS OF MATRIX 1:"))  

matrix1 = []

print("ENTER THE VALUES :")
#INPUT
for i in range(r1):          
    a =[]
    for j in range(c1):      
         a.append(int(input()))
    matrix1.append(a)
  

#MATRIX 2
r2 = int(input("ENTER THE NO. OF ROWS OF MATRIX 2:"))
c2 = int(input("ENTER THE NO. OF COLUMNS OF MATRIX 2:"))

matrix2 = []

print("ENTER THE VALUES:")  
#INPUT
for i in range(r2):          
    a =[]
    for j in range(c2):      
         a.append(int(input()))
    matrix2.append(a)
  

# For printing the matrix1
print("THE FIRST MATRIX IS:")
for i in range(r1):
    for j in range(c1):
        print(matrix1[i][j], end = " ")
    print()


# For printing the matrix2
print("THE SECOND MATRIX IS:")
for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j], end = " ")
    print()

#Q1
print("\nDOT PRODUCT IS:")
print(np.dot(matrix1, matrix2))


#Q2
print("\nTRANSPOSE OF MATRIX 1 IS:")
print(np.transpose(matrix1))

print("\nTRANSPOSE OF MATRIX 2 IS:")
print(np.transpose(matrix2))


#Q3
print("\nTRACE OF MATRIX 1 IS:")
print(np.trace(matrix1))

print("\nTRACE OF MATRIX 2 IS:")
print(np.trace(matrix2))


#Q4
print("\nRANK OF MATRIX 1 IS:")
rank = np.linalg.matrix_rank(matrix1)
print(rank)

print("\nRANK OF MATRIX 2 IS:")
rank = np.linalg.matrix_rank(matrix2)
print(rank)


#Q5
print("\nDETERMINANT OF MATRIX 1 IS:")
print(np.linalg.det(matrix1))

print("\nDETERMINANT OF MATRIX 2 IS:")
print(np.linalg.det(matrix2))


#Q6
print("\nINVERSE OF MATRIX 1 IS:")
print(np.linalg.inv(matrix1))

print("\nINVERSE OF MATRIX 2 IS:")
print(np.linalg.inv(matrix2))


#Q7
print("\nEIGEN VALUES OF MATRIX 1 IS:")
vl,vc = np.linalg.eig(matrix1)
print(vl)

print("\nEIGEN VECTOR OF MATRIX 1 IS:")       
print(vc)


print("\nEIGEN VALUES OF MATRIX 2 IS:")
vl,vc = np.linalg.eig(matrix1)
print(vl)

print("\nEIGEN VECTOR OF MATRIX 2 IS:")       
print(vc)
         
         
         


# In[ ]:



