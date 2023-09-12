x0 = 1.2
i=1

def f(x):
   return x**3+2*x-1

def g(x):
   return 3*(x**2)+2

while abs(f(x0))>=0.0001 and i<50:

   x0=x0-(f(x0)/g(x0))
   print(x0)
   i=i+1

print(i)
