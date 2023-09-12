import numpy as np

A = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],dtype=float)
B = np.array([[6],[25],[-11],[15]],dtype=float)
x = np.zeros((4,1),dtype = float)
y = np.zeros((4,1),dtype = float)

D = np.zeros((4,4),dtype = float)
L = np.zeros((4,4),dtype = float)
U = np.zeros((4,4),dtype = float)

for i in range(0,4):
  D[i][i] = A[i][i]

for j in range(0,4):
  for i in range(j+1,4):
    U[j][i] = -A[j][i]

for j in range(0,4):
  for i in range(0,j):
    L[j][i] = -A[j][i]

T =np.matmul(np.linalg.inv(D-L),U) 
C = np.matmul(np.linalg.inv(D-L),B)

N = 50
n = 1
tol = 0.00000001

while (n<=N):
  for j in range(0,4):
    sum = 0
    for i in range(j,4):
      sum = sum+T[j][i]*x[i]
    for k in range(0,j):
      sum = sum+T[j][k]*y[k]

    y[j] = sum+C[j]

  k = abs(y-x).max()
  l = abs(y).max()

  if (k/l)< tol:
    print("The approximation solution at iteration",n)
    print(y)
    break
  else:
    print("The approximation solution at iteration",n)
    print(y)

  for t in range(0,4):
    x[t] = y[t]
  
  n=n+1


