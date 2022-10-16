# -*- coding: utf-8 -*-
"""ALA_Assignment-1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rYPO5quOyev4H74NAMb--eDgy-u2QifJ

# **Group No. : 18** 

**AU2140166 - Nisarg Patel**

**AU2140057 - Sanket Shah**

**AU2140080 - Patel DivyKumar**

**AU2140141   - Krutarth Trivedi** 

**AU2140220 - Shubham Apat**

# **Contribution :** 

**AU2140166 :** Row reduction of matrices – Calculate the ref/rref of the matrix, Rank of a Matrix

**AU2140057 :** Solve a system of linear equations – Homogenous and Non-Homogenous

**AU2140080 :** Inverse of a Matrix, Multiplication of a Matrix

**AU2140141 :** Calculate the Norm of a matrix

**AU2140220 :**Represent the vectors (Plotting the vectors in 2-D&3-D)
"""

# Program to find inverse of a Matrix

# Functions
# Main function
def Inverse(M, length):
    # initialising adjoint and inverse Matrix as 2D-list
    adjointmatrix = [None for _ in range(length)]
    inversematrix = [None for _ in range(length)]

    for i in range(length):
        adjointmatrix[i] = [None for _ in range(length)]
        inversematrix[i] = [None for _ in range(length)]

    Adjoint(M, adjointmatrix, length)

    if(Find_Inverse(M, adjointmatrix, inversematrix, length)):
        print("Matrix M:")
        printmatrix(M, length)
        print()
        print("The inverse of the matrix M:")
        printmatrix(inversematrix, length)
# function to find inverse of a given matrix
def Find_Inverse(M, adj, inv, length):
    determinant = find_determinant(M, length)
    # condition to check whether determinant exists or not
    if(determinant == 0):
        print("det(M)=0 therefore can not find the inverse")
        return False
    # if determinant exists then
    for i in range(length):
        for j in range(length):
            inv[i][j] = adj[i][j] / determinant
    return True
# functiont to find the adjoint matrix
def Adjoint(M, adjt, length):
    if (length == 1):
        adjt[0][0] = 1
        return
    flag = 1
    temporaryarray = []
    for i in range(length):
        temporaryarray.append([None for _ in range(length)])
    for i in range(length):
        for j in range(length):
            findcofactor(M, temporaryarray, i, j, length)
            if ((i + j) % 2):
                flag = -1
            else:
                flag = 1
            # interchanged i and j as to find the tranpose of the cofactor matrix
            adjt[j][i] = (
                flag)*(find_determinant(temporaryarray, length-1))
# function to find determinant of any matrix
def find_determinant(A, length):
    det = 0
    if(length == 1):
        return A[0][0]
    temporaryarray = []  # To store cofactors
    for i in range(length):
        temporaryarray.append([None for _ in range(length)])
    flag = 1
    for f in range(length):
        findcofactor(A, temporaryarray, 0, f, length)
        det += flag*A[0][f]*find_determinant(temporaryarray, length-1)
        flag = -flag
    return det
# function to find cofactor
def findcofactor(A, temporaryarray, x, y, length):
    i = 0
    j = 0
    for row in range(length):
        for col in range(length):
            if (row != x and col != y):
                temporaryarray[i][j] = A[row][col]
                j += 1
                if (j == length - 1):
                    j = 0
                    i += 1
# function to display matrix in proper format
def printmatrix(M, length):
    for i in range(length):
        for j in range(length):
            print(round(M[i][j], 2), end="  ")
        print()
# Driver Code
A = [[1, -1],
     [0, 2]]

B = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

I = [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
C = [[1, -1, -5, 7, 5],
     [-9, 1, 63, 14, 5],
     [2, 12, 1, 47, 5],
     [3, 78, 0, 1, 5],
     [41, 96, 23, 1, 5]]
print("\nTestcase:1\n") 
Inverse(I, 4)
print("---------------------------------")
print("\nTestcase:2\n") 
Inverse(A, 2)
print("---------------------------------")
print("\nTestcase:3\n") 
Inverse(B, 3)
print("---------------------------------")
print("\nTestcase:4\n") 
Inverse(C, 5)
print()

# Program To find Multiplication
mat1 = [[12,7,3], 
        [4 ,5,6], 
        [7 ,8,9]] 
mat2 = [[5,8,1], 
        [6,7,3], 
        [4,5,9]] 

result = [[0 for x in range(3)] for y in range(3)]  
#  loops Running  
for a in range(len(mat1)): 
    for b in range(len(mat2[0])): 
        for c in range(len(mat2)): 
  
            # resulted matrix 
            result[a][b] += mat1[a][c] * mat2[c][b] 
print("For first matrix :")
print (result)
print()
print("--------------------------")

mat3=[[4,5],[6,9]]
mat4=[[8,9],[1,2]]

result = [[0 for x in range(2)] for y in range(2)]  
  
#  loops Running  
for a in range(len(mat3)): 
    for b in range(len(mat4[0])): 
        for c in range(len(mat4)): 
  
            # resulted matrix 
            result[a][b] += mat3[a][c] * mat4[a][c] 
print("For second matrix :")
print (result)

print("---------Verification----------------")
print()
import numpy as np
print(np.dot(mat3,mat4))
print("----------")
print(np.dot(mat1,mat2))

#Solve a system of linear equations – Homogenous and Non-Homogenous
from sympy import Matrix
def equationsolve(X,M):
  XS = X
  n = len(X)
  MS = M
  indices = list(range(n))
  for rf in range(n):
      rfScaler = 1.0 / XS[rf][rf]
      for j in range(n):
          XS[rf][j] *= rfScaler
      MS[rf][0] *= rfScaler
      cal1 = rf+1; cal2 = rf+1
      for i in indices[0:rf] + indices[rf+1:]:
          msScaler = XS[i][rf]
          for j in range(n):
              XS[i][j] = XS[i][j] - msScaler * XS[rf][j]
          MS[i][0] = MS[i][0] - msScaler * MS[rf][0]
          cal1 = i+1; cal2 = rf+1
  return MS


X=[[2,3,4],[6,5,4],[2,3,6]]
M=[[6],[12],[8]]
Solve_M=Matrix(equationsolve(X,M))
Solve_M

# Program To find norm of a matrix
from math import sqrt
X = [[3],[6],[10]] #column matrix
k,j = len(X),len(X[0]) #rows and columns
XY=[[X[i][j] for i in range(k)]for j in range(j)]
norm = sqrt(sum([XY[0][i]*X[i][0] for i in range(k)]))
XP=[[-i[0]/norm] for i in X]
print("Norm :")
print(norm)
print()
print("-----------------Verification--------------------------")
print()
import numpy as np
# initialize matrix
mat = np.array([[3],[6],[10]])
# compute norm of matrix
mat_norm = np.linalg.norm(mat)
print("Norm:")
print(mat_norm)

#Represent the vectors (Plotting the vectors in 2-D)
import matplotlib.pyplot as plt

# Intiallization of arrows of vectors
x_pos = [0, 0]
y_pos = [0, 0]
x_direct = [1, 0]
y_direct = [1, -1]

# plotting
fig, ax = plt.subplots(figsize=(12, 7))
ax.quiver(x_pos, y_pos, x_direct, y_direct, scale=5)

ax.axis([-1.5, 1.5, -1.5, 1.5])

plt.show()

#Represent the vectors (Plotting the vectors in 3-D)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#input of vectors
vectors=np.array( [ [0,0,1,1,-2,0], [0,0,2,1,1,0],[0,0,3,2,1,0],[0,0,4,0.5,0.7,0]]) 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for vector in vectors:
    v = np.array([vector[3],vector[4],vector[5]])
    vlength=np.linalg.norm(v)
    ax.quiver(vector[0],vector[1],vector[2],vector[3],vector[4],vector[5],
            pivot='tail',length=vlength,arrow_length_ratio=0.3/vlength)
  #plotting
ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([0,4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

# Rank of Matrix
class rankOfMatrix(object):
	def __init__(self, m):
		self.rm = len(m)
		self.cm = len(m[0])
		
	def swap(self, m, r1, r2, c):
		for i in range(c):
			temp = m[r1][i]
			m[r1][i] = m[r2][i]
			m[r2][i] = temp
			
	def display(self, m, r, c):
		for i in range(r):
			for j in range(c):
				print (" " + str(m[i][j]))
			print ('\n')

	def rank_Of_Matrix(self, m):
		rank = self.cm
		for r in range(0, rank, 1):

			if m[r][r] != 0:
				for c in range(0, self.rm, 1):
					if c != r:
						multiplier = (m[c][r] / m[r][r])

						for i in range(rank):
							m[c][i] -= (multiplier * m[r][i])

			else:
				reduce = True

				for i in range(r + 1, self.rm, 1):
					if m[i][r] != 0:
						self.swap(m, r, i, rank)
						reduce = False
						break

				if reduce:
					rank -= 1

					for i in range(0, self.rm, 1):
						m[i][r] = m[i][rank]

				r -= 1

		return (rank)

m = [[-5,8,9],
	[2,8,9],
	[4,1,0]]
RankMatrix = rankOfMatrix(m)
print ("Rank of the Matrix is : ")
print((RankMatrix.rank_Of_Matrix(m)))

print("---------------------Verification----------------------")
import numpy as np
print("The Rank of Matrix using numpy is as follows : ")
print(np.linalg.matrix_rank(m))

# Row Reduce Matrix