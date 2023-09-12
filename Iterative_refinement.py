import numpy as np

a = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],dtype=float)
b = np.array([[6],[25],[-11],[15]],dtype=float)
x = np.array([[0],[0],[0],[0]],dtype=float)
r = np.array([[0],[0],[0],[0]],dtype=float)
y = np.array([[0],[0],[0],[0]],dtype=float)
xx = np.array([[0],[0],[0],[0]],dtype=float)
a_= np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],dtype=float)
b_= np.array([[6],[25],[-11],[15]],dtype=float)

### Step 0
### solve the system Ax=b using gausian	elimination without row interchange
print("matrix A")
print(a)
print("matrix B")
print(b)

for i in range(0,3):
   for j in range(i+1,4):
     m = a[j][i]/a[i][i]
     a[j]=a[j]-m*a[i]
     b[j]=b[j]-m*b[j]

x[3] = b[3]/a[3][3]  ### back substitution
for k in range(2,-1,-1):
 sum=0
 for i in range(k+1,4):
   sum=sum+a[k][i]*x[i]
 x[k]=(b[k]-sum)/a[k][k]

print("matrix A")
print(a)
print("matrix B")
print(b)

print("Approximation solution x")
print(x)

n = 1
N = 15
tol = 0.0001

### Step 1
while(n<=N):
    ### calculate the residual vector
    for i in range(0,4):
      sum=0
      for k in range(0,4):
        sum=sum+a_[i][k]*x[k]
      r[i]=b_[i]-sum
    
    print("The residual vector at iteration",n)
    print(r)
    ### solve the system Ay=r using gaussian elimination
    for i in range(0,3):
      for j in range(i+1,4):
        m = a_[j][i]/a_[i][i]
        a_[j]=a_[j]-m*a_[i]
        b_[j]=b_[j]-m*b_[i]

    print("matrix A_")
    print(a_)
    print("matrix B_")
    print(b_)

    y[3] = b_[3]/a_[3][3]  ### back substitution
    for k in range(2,-1,-1):
       sum=0
       for i in range(k+1,4):
          sum=sum+a_[k][i]*y[i]
       y[k]=(b_[k]-sum)/a_[k][k]

    print("Approximation solution y") 
    print(y)

    for i in range(0,4):
      xx[i] = y[i]+x[i]
    print("Approximation solution at iteration**",n)
    print(xx)
  
#    if(k==1):
#      con = (abs(y).max()/abs(xx).max())*(10**4)
    """
    d = abs(x-xx).max()
    r = abs(xx).max()

    if((d/r)<tol):
       print("Approximation solution xx at iteration",n)
       print(xx)
       break
    """
    for i in range(0,4):
      x[i] = xx[i]

    n = n+1
    
                          
         
