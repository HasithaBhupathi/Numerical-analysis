import numpy as np

A = np.array([[1.0,-1.0,3.0],[3.0,-3.0,1.0],[1.0,1.0,0.0]])
B = np.array([[2.0],[-1.0],[3.0]])

#A = np.array([[1.0,-1.0,3.0],[1.0,1.0,0.0],[3.0,-3.0,1.0]])
#B = np.array([[2.0],[3.0],[-1.0]])

#A = np.array([[1.0,-1.0,3.0],[-2.0,1.0,0.0],[-3.0,-3.0,1.0]])
#B = np.array([[2.0],[3.0],[-1.0]])

### i column number
### j row number
print(A)
for i in range(0,2):
    
    for j in range(i,3):
       if(A[j][i]!=0):
         row = j
         break;   
    
    if(row!=i):
      
       A[[i,row]]=A[[row,i]]   ### row interchange
       B[[i,row]]=B[[row,i]]
       print(A)    

    for k in range(i+1,3):
       m = A[k][i]/A[i][i]  ### gauss algorith 
       A[k] = A[k]-m*A[i]
       B[k] = B[k]-m*B[i]  
             
    print(A)

if (A[2][2]==0):
   print("There is no unique solution")

else:
   B[2] = B[2]/A[2][2]    ### back substitute

   for j in range(1,-1,-1):
      sum = 0
      for i in range(j+1,3):
         sum = sum+A[j][i]*B[i]

      B[j]=(B[j]-sum)/A[j][j]
      
print(B)
