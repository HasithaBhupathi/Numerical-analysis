import numpy as np

a = np.array([[10,5,2],[5,3,2],[2,2,3]],dtype = float)
B = np.array([[2],[-1],[3]],dtype = float)
d = np.identity(3,dtype=float)
l = np.identity(3,dtype=float)
v = np.array([[0],[0],[0]],dtype=float)
y = np.array([[0],[0],[0]],dtype=float)
x = np.array([[0],[0],[0]],dtype=float)

#### step 1(find LD sutch that A=LDLt)
for i in range(0,3):
   
   for j in range(0,i):
      v[j]=l[i][j]*d[j][j]
   
   sum = 0
   for k in range(0,i):
     sum=sum+l[i][k]*v[k]

   d[i][i]=a[i][i]-sum

   for j in range(i+1,3):
     sum = 0
     for k in range(0,i):
       sum=sum+l[j][k]*v[k]
       
     l[j][i]=(a[i][j]-sum)/d[i][i]


print("matrix A")
print(a)

print("matrix L")
print(l)

print("matrix D")
print(d)

print("matrix multiplication LDLt")
LD = np.matmul(l,d)
LDLt = np.matmul(LD,l.transpose())
print(LDLt)

### Ax = B
### LDLtx = B
### LD = S
### Ltx = y
### Sy = B

### step 2(solve the system Sy = B)
    
S = np.matmul(l,d)
print("matrix S=LD")
print(S)

print("matrix B")
print(B)

for i in range(0,2):
    
    for j in range(i,3):
       if(S[j][i]!=0):
         row = j
         break;   
    
    if(row!=i):
      
       S[[i,row]]=S[[row,i]]   ### row interchange
       B[[i,row]]=B[[row,i]]
       print("matrix S")
       print(S)    

    for k in range(i+1,3):
       m = S[k][i]/S[i][i]  ### gauss algorith 
       S[k] = S[k]-m*S[i]
       B[k] = B[k]-m*B[i]  
             
    print("matrix S")
    print(S)

print("matrix B")
print(B)
if (S[2][2]==0):
   print("There is no unique solution")

else:
   y[2] = B[2]/S[2][2]    ### back substitute

   for j in range(1,-1,-1):
      sum = 0
      for i in range(j+1,3):
         sum = sum+S[j][i]*y[i]

      y[j]=(B[j]-sum)/S[j][j]

      
print("solution y")
print(y)

#### step 3(solve Ltx = y)
lt = l.transpose()

x[2] = y[2]/lt[2][2]

for j in range(1,-1,-1):
  sum = 0
  for k in range(j+1,3):
    sum=sum+lt[j][k]*x[k]

  x[j] = (y[j]-sum)/lt[j][j]

print("matrix Lt")
print(l.transpose())

print("Solution x")
print(x)
