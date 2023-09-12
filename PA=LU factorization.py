import numpy as np

A = np.array([[1.0,-1.0,3.0],[3.0,-3.0,1.0],[1.0,1.0,0.0]])
p = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
B = np.array([[2.0],[-1.0],[3.0]])
y = np.array([[0.0],[0.0],[0.0]])
x = np.array([[0.0],[0.0],[0.0]])

print("matrix A ")
print(A)

#### Step 1(find permutation matrix of A)

for i in range(0,2):
    
    for j in range(i,3):
       if(A[j][i]!=0):
         row = j
         break;   
    
    if(row!=i):
      
       A[[i,row]]=A[[row,i]]   ### row interchange of A
       p[[i,row]]=p[[row,i]]   ### row interchange pf P
       print("matrix A")
       print(A)    

    for k in range(i+1,3):
       m = A[k][i]/A[i][i]     ### gauss eliminaton
       A[k] = A[k]-m*A[i]
             
    print("matrix A ")
    print(A)

print("permutation matrix of A ")
print(p)

#### Step 2(Find LU such that PA=c=LU)

A = np.array([[1.0,-1.0,3.0],[3.0,-3.0,1.0],[1.0,1.0,0.0]])
c = np.matmul(p,A)
print("matrix c such that c = pA")
print(c)

L = np.identity(3)
U = np.identity(3)

if c[0][0]==0:
    print("Factorization imposible")
else:
    U[0][0] = c[0][0]/L[0][0]


    for j in range(1,3):  
        U[0][j] = c[0][j]/L[0][0]  ### find first row of U
        L[j][0] = c[j][0]/U[0][0]  ### find first column of L

    
    for i in range(1,2):
        sum = 0
        for k in range(0,i):
            sum = sum+(L[i][k]*U[k][i])
                    
        if (c[i][i]-sum)==0:
           print("Factorization imposible")
        else:
           U[i][i] = (c[i][i]-sum)/L[i][i]   #### find Uii dor i=2,....,n-1
           
        
        for j in range(i+1,3):
           sum = 0
           for k in range(0,i):
             sum=sum+(L[i][k]*U[k][j])

           U[i][j]=(c[i][j]-sum)/L[i][i] ## find ith row of U
           
           sum = 0
           for k in range(0,i):
             sum = sum+(L[j][k]*U[k][i])

           L[j][i] = (c[j][i]-sum)/U[i][i] ## ith column of L

                                 
    sum = 0
    for k in range(0,2):
       sum = sum+(L[2][k]*U[k][2])

    if (c[2][2]-sum)==0:
        print("A is singular but A=LU")
        U[2][2]=0
    else:
        U[2][2] = (c[2][2]-sum)/L[2][2]


print("Upper traingular matrix U")
print(U)

print("Lower traingular matrix L")
print(L)

print("c metrix such that c=LU")
print(c)

print("L*U")
print(np.matmul(L,U))

pt = p.transpose()
D = np.matmul(pt,L)  #### D = (transpose of p)*U
print("matrix D such  that D = Pt*L ")
print(D)

### (pt)LUx=B
### D=(pt)L
### DUx=B
### y= Ux
### Dy=B

#### Step 3(solve the system Dy=B)
print("matrix B ")
print(B)

for i in range(0,2):
    
    for j in range(i,3):
       if(D[j][i]!=0):
         row = j
         break;   
    
    if(row!=i):
      
       D[[i,row]]=D[[row,i]]   ### row interchange of D and B
       B[[i,row]]=B[[row,i]]
       print("matrix D ")
       print(D)    

    for k in range(i+1,3):
       m = D[k][i]/D[i][i]  ### gauss elimination 
       D[k] = D[k]-m*D[i]
       B[k] = B[k]-m*B[i]  
             
    print("matrix D ")
    print(D)

print("matrix B ")
print(B)

if (D[2][2]==0):
   print("There is no unique solution")

else:
   y[2] = B[2]/D[2][2]    ### back substitution

   for j in range(1,-1,-1):
      sum = 0
      for i in range(j+1,3):
         sum = sum+D[j][i]*y[i]

      y[j]=(B[j]-sum)/D[j][j]
      
print("matrix y ")
print(y)

#### Step 4(solve ux = y)

if (U[2][2]==0):
   print("There is no unique solution")

else:
   x[2] = y[2]/U[2][2]    ### back substitute

   for j in range(1,-1,-1):
      sum = 0
      for i in range(j+1,3):
         sum = sum+U[j][i]*x[i]

      x[j]=(y[j]-sum)/U[j][j]

print("The solution x of the system")
print(x)
