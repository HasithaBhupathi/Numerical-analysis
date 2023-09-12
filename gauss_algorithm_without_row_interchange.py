import numpy as np

#a = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
#b = np.array([[6],[25],[-11],[15]])

A = np.array([[1,1,1],[1,2,3],[1,2,4]])
B = np.array([[6],[10],[0]])

#A= np.array([[1,-1,3],[3,-3,1],[1,1,0]])  we should be row interchange
#B = np.array([[2],[-1],[3]])

for i in range(0,2):
   
   if (A[i][i]==0):
     print("We can not use gauss algorithm without row interchange")
     break;          
  
   for j in range(i+1,3):
     m = A[j][i]/A[i][i]
     A[j] = A[j]-m*A[i]
     B[j] = B[j]-m*B[i]
     
       
print(A)
print(B)



