import numpy as np

a = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],dtype=float)
b = np.array([[6],[25],[-11],[15]],dtype=float)
x0 = np.array([[0],[0],[0],[0]],dtype=float)
x = np.array([[0],[0],[0],[0]],dtype=float)
d = np.zeros((4,4),dtype=float)
l = np.zeros((4,4),dtype=float)
u = np.zeros((4,4),dtype=float)

#### Find D,L,U such that A = D-L-U
for i in range(0,4):
  d[i][i]=a[i][i]

for i in range(1,4):
  for j in range(0,i):
     l[i][j]=-a[i][j]

for i in range(0,3):
  for j in range(i+1,4):
     u[i][j] = -a[i][j]

#### define the matrix T,C such that T=D'(U+L) and C = D'b
t=np.matmul(np.linalg.inv(d),(u+l))
c=np.matmul(np.linalg.inv(d),b)

n = 1
N=50
tol = 0.00000001

print("Initial point x0")
print(x0)

while(n<=N):

    x = np.matmul(t,x0)+c

    k=abs(x-x0).max()
    l=abs(x).max()

    if (k/l)<tol:
      print("The approximation solution at iteration",n)
      print(x)
      break
    else:
      print("Aproximation solution at iteration",n)
      print(x)
    
    for q in range(0,4):
      x0[q] = x[q]
    
    n=n+1

