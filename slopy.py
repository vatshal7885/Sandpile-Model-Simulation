import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter

iterations = 100000  # number of iterations
N = 50            # size of matrix

global threshold
threshold = 4        # critical level for toppling to occur

topple = 0
topplesize = []

def initializeMatrix(N):
    return np.random.randint(4, size=(N,N))

def drop(M, x, y, N):
    global topple
    withinBounds = True

    if x < 0  or x > N-1 or y < 0 or y > N-1:
        withinBounds = False
        pass

    if withinBounds:
        if M[x,y-1]>M[x,y]+1 and M[x-1,y]>M[x,y]+1:
            M[x-1,y]=M[x-1,y]-1
            M[x,y-1]=M[x,y-1]-1
            M[x,y] = M[x,y] + 2
        else:
            M[x,y]=M[x,y]+1
         
		
        if M[x,y] >= threshold:
            M[x,y] = M[x,y] - 4 # reset the cell value and distribute to neighbors
            topple += 1          # count the toppling
            drop(M, x+1, y, N)
            drop(M, x-1, y, N)
            drop(M, x, y-1, N)
            drop(M, x, y+1, N)

M = initializeMatrix(N)
 

for i in range(iterations):
    topple = 0
    x = random.randint(0, N-1)
    y = random.randint(0, N-1)
    drop(M, x, y, N)
    topplesize.append(topple)          
        

c=Counter(topplesize)

xx1=(np.array(list(c.keys())))
yy1=(np.array(list(c.values())))
c1 = len(xx1)
X = np.log10(xx1[0:int(c1/10)])
Y = np.log10(yy1[0:int(c1/10)]/10000.0)
X[0]=0
z1 = np.polyfit(X,Y,1)
print "Slope = %s"  %z1[0]
#print ((xx1))
plt.figure(figsize=(10,7))
plt.loglog(xx1,yy1/100000.0,'r.')
plt.show()