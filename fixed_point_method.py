i=0
p0 = 1
n = 50

def g(x):
  return ((1/2)*(-(x**3)-x+1))**(1/2)

p = g(p0)

while abs(p-p0)>=0.0001:

##    p = g(p0)
    p0 = p
    p = g(p0)
    print(abs(p-p0))
    i=i+1

print("Number of iteration: ",i)
print("Approximate solution is: ",p)
   


