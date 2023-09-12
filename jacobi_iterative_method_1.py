import numpy as np

a = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],dtype=float)
b = np.array([[6],[25],[-11],[15]],dtype=float)
x0 = np.array([[0],[0],[0],[0]],dtype=float)
x = np.array([[0],[0],[0],[0]],dtype=float)

n = 1
N=50
tol = 0.00000001

print("Initial solution point x0")
print(x0)

while(n<=N):

  for i in range(0,4):
    sum = 0
    for j in range(0,4):
      if j!=i:
        sum=sum+a[i][j]*x0[j]

    x[i]=(b[i]-sum)/a[i][i]

  k=abs(x-x0).max()
  l=abs(x).max()
  
  if (k/l)<tol:
    print("Number of iterations: ",n)
    print("The approximation solution x")
    print(x)
    break
  else:
    print("Aproximation solution at iteration",n)
    print(x)

  for t in range(0,4):
    x0[t] = x[t]
  
  n = n+1


