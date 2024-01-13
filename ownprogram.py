import numpy as np
import matplotlib.pyplot as plt
import random
from collections import Counter


def check(A,x,y):  #function to check the criticality
    global counter
       
    A[x][y]=A[x][y]-4
    counter+=1
    if(x-1>0): 
         A[x-1][y]+=1
         if(A[x-1][y]>=4): 
             check(A,x-1,y)
    if(x+1<N): 
        A[x+1][y]+=1
        if(A[x+1][y]>=4):
             check(A,x+1,y)
    if(y-1>0):
        A[x][y-1]+=1
        if(A[x][y-1]>=4):
            check(A,x,y-1)
    if(y+1<N):
        A[x][y+1]+=1
        if(A[x][y+1]>=4):
            check(A,x,y+1)

N =20    
Matrix=np.zeros((N,N))       #initializing grid matrix
                      #deciding parameter for counting avalanche sizes
z=[]                      # number of grains and in each entry there is avalanche sizes 
                           #use various initial conditions given in paper like away from equillibrium and flat surface

for i in range(10000):
    counter=0
    x=random.randint(0,N-1)
    y=random.randint(0,N-1)
    Matrix[x][y]+=1
    if(Matrix[x][y]>=4):
        check(Matrix,x,y)
    z.append(counter)

c=Counter(z)
#yy=c.values()
#xx=c.keys()
xx1=(np.array(list(c.keys())))
yy1=(np.array(list(c.values())))
c = len(xx1)
#[0:int(c/10)]
np.savetxt('data.txt', (xx1))
np.savetxt('data2.txt', (yy1/10000.0))
plt.figure(figsize=(10,7))
plt.loglog(xx1,yy1/10000.0,'b.')
plt.show()

    
'''plt.figure(figsize=(5,5))  #try to change this
plt.imshow(Matrix)
plt.colorbar()
plt.show()''' 
