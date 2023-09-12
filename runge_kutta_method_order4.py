import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 2
N = 10
h = (b-a)/N

t = np.zeros((N+1,1))
w = np.zeros((N+1,1))
w[0] = 0.5

for i in range(0,N+1):
  t[i] = a+i*h

print(t)

def f(t,y):
   return y-t**2+1

for i in range(0,N):
   k1 = h*f(t[i],w[i])
   k2 = h*f(t[i]+h/2,w[i]+k1/2)
   k3 = h*f(t[i]+h/2,w[i]+k2/2)
   k4 = h*f(t[i+1],w[i]+k3)
   w[i+1] = w[i]+(k1+2*k2+2*k3+k4)/6

print(w)

plt.plot(t,w,"bo")
plt.plot(t,w,'r')
plt.title("Midpoint method")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid()
plt.show()

