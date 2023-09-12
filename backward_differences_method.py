import numpy as np
import math

a = np.array([[0,2],[2,10],[4,66],[6,218]])
b = np.zeros((4,4))

for i in range(0,4):
   if i==0:
     for j in range(0,4):
       b[j][0]=a[j][1]

   else:
     for j in range(0,4-i):
       b[j][i]=b[j+1][i-1]-b[j][i-1]

print(b)
h = 2
x = 4.2
r = (x-a[3][0])/h
p = a[3][1]

for i in range(1,4):
  m = 1
  for j in range(0,i):
    m = m*(r+j)

  p=p+(m*b[3-i][i])/math.factorial(i)

print(p)

