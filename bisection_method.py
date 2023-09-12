i=1
a=0
b=1
p0 = (a+b)/2
n = 50

def f(x):
   return x**3+2*(x**2)+x-1

if f(a)*f(b)<0:
    print("We can use the bisection method")
    while abs(f(p0))>=0.0001 and i<=n:
    
        if f(a)*f(p0) <0:
           b = p0
           p0 = (a+b)/2
    
        elif f(p0)*f(b) <0:
           a=p0
           p0=(a+b)/2
        
        else:
           print("The solution is ",p0)
        
        i = i+1

    print("The solution is",p0)
    print("f(p0):",f(p0))
    print("Number of iteration ",i)

else:
   print("We can not use bisection method")

