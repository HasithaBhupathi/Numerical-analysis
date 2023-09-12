import numpy as np

#A = np.array([[1.0,-1.0,3.0],[3.0,-3.0,1.0],[1.0,1.0,0]])
#A =  np.array([[3.0,-3.0,1.0],[1.0,1.0,0.0],[1.0,-1.0,3.0]])
A = np.array([[1.0,3.0,-1.0],[3.0,1.0,-3.0],[1.0,0.0,1.0]])
B = np.array([[2.0],[-1.0],[3.0]])

L = np.identity(3,dtype=complex)
U = np.identity(3,dtype=complex)

### Step 1
if A[0][0]==0:
    print("Factorization imposible")
else:
    L[0][0] = np.sqrt(A[0][0])
    U[0][0]=L[0][0]

### Steps 2
    for j in range(1,3):  
        U[0][j] = A[0][j]/L[0][0]  ### find first row of u
        L[j][0] = A[j][0]/U[0][0]  ### find first column of l

### Step 3
    
    for i in range(1,2):
        ###Step4
        sum = 0
        for k in range(0,i):
            sum = sum+(L[i][k]*U[k][i])
                    
        if (A[i][i]-sum)==0:
           print("Factorization imposible")
        else:
           L[i][i] =np.sqrt(A[i][i]-sum)   ### find Uii and Lii
           U[i][i] = L[i][i]
           
        ### Step 5
        for j in range(i+1,3):
           sum = 0
           for k in range(0,i):
             sum=sum+(L[i][k]*U[k][j])

           U[i][j]=(A[i][j]-sum)/L[i][i] ## ith row of U
           
           sum = 0
           for k in range(0,i):
             sum = sum+(L[j][k]*U[k][i])

           L[j][i] = (A[j][i]-sum)/U[i][i] ## ith column of L

                                 
### Step 6
    sum = 0
    for k in range(0,2):
       sum = sum+(L[2][k]*U[k][2])

    if (A[2][2]-sum)==0:
        print("A is singular but A=LU")
        L[2][2]=0
    else:
        L[2][2] = np.sqrt(A[2][2]-sum)
        U[2][2]=L[2][2]

### Step 7
print("Upper traingular")
print(U)

print("Lower traingular")
print(L)

print("A metrix")
print(A)

print("L*U")
print(np.matmul(L,U))

### A=LU
### Ax=B
### L(Ux)=B take Ux = y
### Ly= B we can solve this using forward substitution
### Ux=y we can solve this using back substitution

###### forward substituion
y = np.array([[0.0],[0.0],[0.0]],dtype=complex)
y[0] = B[0]/L[0][0]

for i in range(1,3):
  sum = 0
  for k in range(0,i):
    sum = sum+(L[i][k]*y[k])

  y[i]=(B[i]-sum)/L[i][i]

print("y")
print(y)
###### backward substitution
x = np.array([[0.0],[0.0],[0.0]],dtype=complex)
x[2] = y[2]/U[2][2]

for i in range(1,-1,-1):
  sum = 0
  for k in range(i+1,3):
    sum=sum+(U[i][k]*x[k])
  
  x[i] =(y[i]-sum)/U[i][i]

print("x")
print(x)

