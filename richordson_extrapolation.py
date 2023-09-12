import numpy as np
import math

m = int(input("Enter the order of error:"))
h = float(input("Enter the step:"))
x0 = float(input("Enter the independent variable:"))

n = int(m/2)
a = np.zeros((n,n))

def f(x):
     return x*math.exp(x)

a[0][0] = (f(x0+h)-f(x0-h))/(2*h) ### the value of N1(h)

for i in range(0,n):
   if i==0:
      for j in range(1,n):
         a[j][i]=(f(x0+(h/(2*j)))-f(x0-(h/(2*j))))/(2*h/(2*j))

   else:
      for j in range(i,n):
         a[j][i]=a[j][i-1]+(a[j][i-1]-a[j-1][i-1])/(4**j-1)

print(a)
print("The first dirivative of funtion at ",x0,"is",a[n-1][n-1],"when order of the error is",m)


