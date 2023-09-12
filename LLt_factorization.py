import numpy as np

a = np.array([[10,5,2],[5,3,2],[2,2,3]],dtype=float)
B = np.array([[2],[-1],[3]])
l = np.identity(3)
y = np.array([[0],[0],[0]],dtype=float)
x = np.array([[0],[0],[0]],dtype=float)

print("matrix A")
print(a)

#### step 1(find L such that A=LLt)
l[0][0] = np.sqrt(a[0][0])

for j in range(1,3):   #### find the first column of L
  l[j][0] = a[j][0]/l[0][0]

for i in range(1,2):   #### find tha diagonal elemants up to n-1 columns
   sum = 0
   for k in range(0,i):
     sum = sum+(l[i][k]*l[i][k])
   l[i][i] = np.sqrt(a[i][i]-sum)

   for j in range(i+1,3):  #### find ith column of L
      sum = 0
      for k in range(0,i):
        sum=sum+l[j][k]*l[i][k]
      l[j][i] = (a[j][i]-sum)/l[i][i]

sum = 0
for k in range(0,2):  #### find Lnn elemant
  sum=sum+l[2][k]*l[2][k]
l[2][2] = np.sqrt(a[2][2]-sum)

print("matrix L")
print(l)

print("matrix Lt")
print(l.transpose())

print("multiplication of LLt")
print(np.matmul(l,l.transpose()))

### Ax = B
### LLtx = B
### Ltx = y
### Ly = B

#### step 2(Solve the system Ly = B)
y[0] = B[0]/l[0][0]

for j in range(1,3): ### forward substitution
  sum=0
  for k in range(0,j):
    sum=sum+l[j][k]*y[k]

  y[j]=(B[j]-sum)/l[j][j]

print("matrix B")
print(B)

print("Solution of the system Ly=B here y=Ltx")
print(y)


#### step 3(solve the system Ltx = y)
Lt = l.transpose()

x[2]=y[2]/Lt[2][2]

for j in range(1,-1,-1):
  sum=0
  for k in range(j+1,3):
    sum=sum+Lt[j][k]*x[k]

  x[j]=(y[j]-sum)/Lt[j][j]

print("The solution of the system Ltx = y")
print(x)
