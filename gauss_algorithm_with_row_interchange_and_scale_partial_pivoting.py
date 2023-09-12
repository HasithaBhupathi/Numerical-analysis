import numpy as np

a = np.array([[1.0,-1.0,3.0],[3.0,-3.0,1.0],[1.0,1.0,0.0]])
b = np.array([[2.0],[-1.0],[3.0]])

#a = np.array([[2.11,-4.21,0.921],[4.01,10.2,-1.12],[1.09,0.987,0.832]])
#b = np.array([[2.01],[-3.09],[4.21]])
s = np.array([[0],[0],[0]])

for j in range(0,3):
   s[j]=abs(a[j]).max()   
   if (s[j]==0):
      print("There is no unique solution")
      break;
print(a)
print(b)
print(s)
for i in range(0,2):
    print(i)
    ratio = np.array([[0.0],[0.0],[0.0]])
    for j in range(i,3):
       ratio[j] = abs(a[j][i])/s[j]    #### find the ratio of jth row

    print(ratio)
    max_ratio = ratio.max()

    for j in range(i,3):
       if (ratio[j]==max_ratio):  #### check what is the row given maximum ratio
           p = j
           print(p)
           break;

    a[[i,p]]=a[[p,i]]  #### interchange ith row and pth row of a
    b[[i,p]]=b[[p,i]]  #### interchange ith row and pth row of b
    s[[i,p]]=s[[j,i]]  #### interchange ith row ans pth row of s
    print(a)
    print(b)
    print(s)

    for j in range(i+1,3):
       m = a[j][i]/a[i][i]   #### gauss elimination for row
       a[j] = a[j]-m*a[i]
       b[j] = b[j]-m*b[i]
    print(a)
    print(b)
    print(s)

if (a[2][2]==0):
   print("There is no unique solution")

b[2] = b[2]/a[2][2]  #### back substution

for j in range(1,-1,-1):
  sum = 0
  for k in range(j+1,3):
     sum=sum+a[j][k]*b[k]
  b[j]=(b[j]-sum)/a[j][j]

print(b)


