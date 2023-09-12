import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,Function

### natural qubic spline interpolation

x=np.array([0.9,1.3,1.9,2.1,2.6,3])
a=np.array([1.3,1.5,1.85,2.1,2.6,2.7])

M=np.size(x)
n=M-1

### step 1
h=np.zeros((n,1))

for i in range(0,n):
    h[i]=x[i+1]-x[i]


### step 2
FPO=FPN=100
alpha = np.zeros((n+1,1))
alpha[0]=3*(a[1]-a[0])/h[0]-3*FPO
alpha[n]=3*FPN-(3*(a[n]-a[n-1])/h[n-1])

### step 3
for i in range(1,n):
        alpha[i-1]=3*(a[i+1]-a[i])/h[i]-3*(a[i]-a[i-1])/h[i-1]


### step 4       
l = np.zeros((n+1,1))
mu = np.zeros((n,1))
z = np.zeros((n+1,1))

l[0] = 2*h[0]
mu[0] = 0.5
z[0] = alpha[0]/l[0]

### step 5
for i in range(1,n):
   l[i]=2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
   mu[i]=h[i]/l[i]
   z[i]=(alpha[i-1]-h[i-1]*z[i-1])/l[i]   

### step 6
l[n] = h[n-1]*(2-mu[n-1])
z[n] = (alpha[n]-h[n-1]*z[n-1])/l[n]
c = np.zeros((n+1,1))
c[n] = z[n]

### step 7
b=np.zeros((n,1))
d=np.zeros((n,1))

for j in range(n-1,-1,-1):
    c[j]=z[j]-mu[j]*c[j+1]
    b[j]=(a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
    d[j]=(c[j+1]-c[j])/(3*h[j])


###### ploting graph
X=[]
Y=[]
for j in range(0,n):
    k = x[j]
    f=lambda i:a[j]+b[j]*(i-x[j])+c[j]*((i-x[j])**2)+d[j]*((i-x[j])**3)

    #### find a function value
    if x[j]<=1.9 and 1.9<x[j+1]:
       answer = f(1.9)
       print(answer)

    nx=[]
    nY=[]
               
    while k<=x[j+1]:
        nx.append(k)
        nY.append(f(k))
        k += 0.001
    X.append(nx)
    Y.append(nY)
    


plt.plot(x,a,'yo',X[0],Y[0],'r',X[1],Y[1],'b',X[2],Y[2],'g',X[3],Y[3],'c',X[4],Y[4],'m')
plt.title("Natural qubic spline interpolation")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(["(x,y)","S0","S1","S2","S3","S4"])
plt.grid()
plt.show()

#### create function using sympy package
z = symbols('x')
for j in range(0,n):
   f=Function("f")(x)
   f=a[j]+b[j]*(z-x[j])+c[j]*((z-x[j])**2)+d[j]*((z-x[j])**3)
   print("s",j,"=",f)
