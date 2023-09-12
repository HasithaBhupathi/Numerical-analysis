import numpy as np

x = np.array([3,5])
h = 2

def f(x):
  return  x**3+2*(x**2)+5*x

#### forward difference formula
value_1 = (f(x[1])-f(x[0]))/h
print("forward difference value:",value_1)

#### backward difference formula
value_2 = (f(x[1])-f(x[0]))/h
print("back word difference value:",value_2)

####  three point endpoint formula
x = np.array([3,5,7])
h = 2
value_3 = (-3*f(x[0])+4*f(x[1])-f(x[2]))/(2*h)
print("Three point end point formular:",value_3)

#### three point midpoint formular
value_4 = (f(x[2])-f(x[0]))/(2*h)
print("Three point mid point formular:",value_4)

#### five point midpoint formula
x = np.array([3,5,7,9,11])
h = 2
value_5 = (f(x[0])-8*f(x[1])+8*f(x[3])-f(x[4]))/(12*h)
print("Five point midpoint formular:",value_5)

#### five point endpoint formula
value_6 = (-25*f(x[0])+48*f(x[1])-36*f(x[2])+16*f(x[3])-3*f(x[4]))/(12*h)
print("five point endpoint formular:",value_6)

#### secound derivative midpoint formula
x = np.array([3,5,7])
h = 2
value_7 = (f(x[0])-2*f(x[1])+f(x[2]))/(h*h)
print("Secound derivative midpoint formula:",value_7)

