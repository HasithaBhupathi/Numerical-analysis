import numpy as np

a = np.array([[1,1],[3,9],[5,25],[7,49],[8,64],[9,81]])
p = 0

x = float(input("Enter the number:"))

for i in range(0,6):
   l = 1
   for k in range(0,6):
      if k!=i:
         m = (x-a[k][0])/(a[i][0]-a[k][0])
         l = l*m
       
   r = l*a[i][1]
   p = p+r
print("The function value of",x,"is",p)
