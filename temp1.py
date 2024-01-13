# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:56:30 2017

@author: Vatsalya
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#import random
import matplotlib.cm as cm
#from collections import Counter

def drawf(t, Matrix):
    plt.figure(figsize=(100,100))  #try to change this
    plt.matshow(Matrix, cmap=cm.hot)
    plt.colorbar()
    plt.annotate('Sandpile at t = %d' % t, (0,0), (0, -10), xycoords='axes fraction', textcoords='offset points', va='top')
   # plt.title('Sandpile at t = %d' % t)

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

N =50   
Matrix=np.zeros((N,N))       #initializing grid matrix
                      #deciding parameter for counting avalanche sizes
z=[]                      # number of grains and in each entry there is avalanche sizes 
b = 1                        #use various initial conditions given in paper like away from equillibrium and flat surface
#t = np.linspace(0,60,b)

for k in range(b):
    for i in range(10000):
        counter=0
#        x=random.randint(0,N-1)
 #       y=random.randint(0,N-1)
        x=int(N/2)
        y = int(N/2)
        Matrix[x][y]+=1
        if(Matrix[x][y]>=4):
            check(Matrix,x,y)
        #z.append(counter)
        file_name='_temp%05d.png' % i
    # file_name = _temp(i).png
        drawf(i, Matrix) 
        plt.savefig(file_name) 
        plt.clf()
"""plt.figure(figsize=(10,10))  #try to change this
plt.imshow(Matrix)
plt.colorbar()
plt.show()"""
"""c=Counter(z)
#yy=c.values()
#xx=c.keys()
xx1=(np.array(list(c.keys())))
yy1=(np.array(list(c.values())))
c = len(xx1)
#[0:int(c/10)]
X = np.log10(xx1[0:int(c/5)])
Y = np.log10(yy1[0:int(c/5)]/10000.0)
X[0]=0
z1 = np.polyfit(X,Y,1)
print "Slope = %s"  %z1[0]

np.savetxt('data.txt', (xx1))
np.savetxt('data2.txt', (yy1/10000.0))
plt.figure(figsize=(10,7))
plt.loglog(xx1,yy1/10000.0,'b.')
plt.show()
X = np.log10(xx1[0:int(c/10)])
Y = np.log10(yy1[0:int(c/10)]/10000.0)"""

import os
os.system("rm _movie.mpg") 
os.system("C:\Users\Vatshalya\Desktop\Python Scripts\plot_codes " +
         " -i _temp%05d.png -b:v 1800 _movie.mpg")
# make a mpg file using the _temp files
os.system("rm _temp*.png")

'''plt.hist2d(Matrix[:,0], Matrix[:,1], bins=10, normed=True, vmin=0, vmax=4)
plt.colorbar(norm=mcolors.NoNorm)
plt.show()'''

