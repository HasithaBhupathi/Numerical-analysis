import numpy as np

a = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],dtype=float)
b = np.array([[6],[25],[-11],[15]],dtype=float)
x0 = np.array([[0],[0],[0],[0]],dtype=float) 
x = np.array([[0],[0],[0],[0]],dtype=float)
d = np.zeros((4,4),dtype=float)
l = np.zeros((4,4),dtype=float)
u = np.zeros((4,4),dtype=float)

n = 1
N = 50
tol = 0.00000001
w = 1.25

print("Initial point x0")
print(x0)

#### find D,L,U such that A=D-L-U
for i in range(0,4):  
  d[i][i] = a[i][i]
  for j in range(i+1,4):
     u[i][j]=-a[i][j]
  for k in range(i+1,4):
     l[k][i]=-a[k][i]
   
t = np.matmul(np.linalg.inv(d-w*l),(1-w)*d+w*u)
c = np.matmul(w*np.linalg.inv(d-w*l),b)

while(n<=N):

   x = np.matmul(t,x0)+c
   k = abs(x-x0).max()
   l = abs(x).max()
  
   if(k/l)<tol:
     print("The number of iterations:",n)
     print("The approximation solution x")
     print(x)
     break
   else:
     print("The approximation solution x at iteration",n)
     print(x)

   for q in range(0,4):
     x0[q] = x[q]

   n=n+1

