import numpy as np
import math

a = np.array([[0,0],[2,4],[4,56],[6,204],[8,496],[10,980]])
b = np.zeros((6,6))

for i in range(0,6):
  if i ==0:
    for j in range(0,6):
      b[j][i] = a[j][1]

  else:
      for j in range(0,6-i):
         b[j][i]=b[j+1][i-1]-b[j][i-1]

h = 2
x = float(input("Inter number:"))
r = (x-a[0][0])/h
p = a[0][1]

for j in range(1,6):
  m = 1
  for i in range(0,j):
    m = m*(r-i)

  p = p+(m*b[0][j])/math.factorial(j)

print("function value is",p)



