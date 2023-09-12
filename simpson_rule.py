import numpy as np

#### simpson's rule
a = float(input("Enter the lower limit:"))
b = float(input("Enter the upper limit:"))
n = int(input("Enter the number of sub intervales:"))
h = (b-a)/n

x = np.zeros((n+1,1))

for i in range(0,n+1):
  x[i] = a+i*h

def f(x):
   return x**3+x**2+5*x+9

sum = f(x[0])-f(x[n])

for i in range(1,n,2):
   sum = sum+4*f(x[i])+2*f(x[i+1])
   
value = (sum*h)/3
print("The integrate value is",value,"when we use simpson's rule")

#### test the acuracy using scipy
from scipy.integrate import quad

I = quad(f,a,b)
print("The correct integrate value is",I)

