import numpy as np

a = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],dtype=float)
b = np.array([[6],[25],[-11],[15]],dtype=float)
x0 = np.array([[0],[0],[0],[0]],dtype=float)
x = np.array([[0],[0],[0],[0]],dtype=float)

n = 1
N = 50
tol = 0.00000001
w = 1.25

print("Initial point x0")
print(x0)

while(n<=N):
  
  for i in range(0,4):

    sum2 = 0
    for j in range(i+1,4):
      sum2=sum2+a[i][j]*x0[j]

    sum1 = 0
    for k in range(0,i):
      sum1=sum1+a[i][k]*x[k]

    x[i] = (1-w)*x0[i]+(w*(b[i]-sum1-sum2))/a[i][i]

  k = abs(x-x0).max()
  l = abs(x).max()
  
  if (k/l)<tol:
    print("The aproximation solution at iteration",n)
    print(x)
    break
  else:
    print("Approximation solution x at iteration",n)
    print(x)
  
  for t in range(0,4):
    x0[t] = x[t]
  
  n=n+1

