import numpy as np

A = np.array([[5,12],[6,13],[9,14],[11,16]])
n = 4
m = 2
### newton divided difference table
B = np.zeros((n,1))
C = np.zeros((n,n))

for j in range(0,n):
  B[j][0]=A[j][0]

for i in range(0,n):
    for j in range(0,n-i):
        if i==0:
          C[j][0]=A[j][1]           
        else:
          C[j][i]=(C[j+1][i-1]-C[j][i-1])/(B[j+i][0]-B[j][0])


### define the function
p = C[0][0]
x = 7

for k in range(1,n):
    m =1
    for t in range(0,k):
      m = m*(x-B[t])
    p=p+C[0][k]*m

print(p)




