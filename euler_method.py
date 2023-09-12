import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
   return y-t**2+1

a = 0
b = 2
n = 4
h = (b-a)/n

t = np.zeros((n+1,1))
w = np.zeros((n+1,1))
w[0] = 0.5

for i in range(0,n+1):
   t[i]=a+i*(b-a)/n

print(t)

for i in range(0,n):
    w[i+1] = w[i]+h*f(t[i],w[i])
  
print(w)

plt.plot(t,w,'bo')
plt.plot(t,w,'r')
plt.title("Euler's method")
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.grid()
plt.show()
