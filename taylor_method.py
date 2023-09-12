import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 2
n = 10
h = (b-a)/n

t = np.zeros((n+1,1))
w = np.zeros((n+1,1))
w[0] = 0.5

for i in range(0,n+1):
  t[i] = a+i*h

print(t)

def f(t,y):
  return y-t**2+1

def g(t,y):
  return y-t**2-2*t+1

def q(t,y):
  return y-t**2-2*t-1

for i in range(0,n):
  w[i+1] = w[i]+h*f(t[i],w[i])+(h*h*g(t[i],w[i])/2)+(h*h*h*q(t[i],w[i])/6)+(h*h*h*h*q(t[i],w[i])/24)

print(w)

plt.plot(t,w,'r')
plt.plot(t,w,'bo')
plt.title("Raylor method")
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.grid()
plt.show()

