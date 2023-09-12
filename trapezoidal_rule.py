import numpy as np

a = float(input("Enter the lower limit:"))
b = float(input("Enter the upper limit:"))
n = int(input("Enter the number of sub intervals:"))
h = (b-a)/n

x = np.zeros((n+1,1))

for i in range(0,n+1):
  x[i] = a+i*h
   
def f(x):
   return x**3+x**2+5*x+3

sum = 0

for i in range(1,n):
   sum = sum+2*f(x[i])   

value = (f(x[0])+sum+f(x[n]))*(h/2)
print("The integrat value is",value,"when we use the trapezoidal rule")


#### check the correctness
from scipy.integrate import quad

I = quad(f,a,b)
print("The correct integral value is",I)
