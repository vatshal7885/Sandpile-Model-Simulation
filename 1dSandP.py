import numpy as np
import random
import matplotlib.pyplot as plt
from collections import Counter

grains = 100000  # number of grains
N = 100            # size of matrix

global criticalH
criticalH = 5       # critical level for toppling to occur

counter = 0
distribution = []

def dropgrain(M, x, N):
    global counter
    k = 1

    if x < 0  or x > N-1:
        k = 0
        pass

    if k:
        
        M[x]=M[x]+1
        if(M[x-1]>0):
            M[x-1]-=1
        if M[x] >= criticalH:
            M[x] = M[x] - criticalH # reset the cell value and distribute to neighbors
            counter += 1          # count the toppling
            dropgrain(M, x+1, N)
            #dropgrain(M, x-1, N)
            

M = np.random.randint(50000,size = N)

for i in range(grains):
    counter = 0
    x = random.randint(0, N-1)
    dropgrain(M,x,N)
    distribution.append(counter)          
       

c=Counter(distribution)

xx1=(np.array(list(c.keys())))
yy1=(np.array(list(c.values())))
c1 = len(xx1)
X = np.log10(xx1[0:int(c1/10)])
Y = np.log10(yy1[0:int(c1/10)]/10000.0)
X[0]=0
np.savetxt('X.txt', (X))
np.savetxt('Y.txt', (Y))
#plt.plot(X,Y)
z1 = np.polyfit(X,Y,1)
print "Slope = %s"  %round(z1[0],3)
#print ((xx1))

plt.figure(figsize=(10,7))
plt.ylabel('flip distribution', fontsize = 18)
plt.xlabel('flips f',fontsize = 18)
plt.loglog(xx1,yy1/100000.0,'b.', markersize=12,  label = r'$Slope = %s$' %round(z1[0],3))
plt.figtext(0.80, 0.045, 'PHY473', color='black', weight='roman', size='small')
plt.savefig('1d1.png')
plt.show()
X = np.log10(xx1)
Y = np.log10(yy1/10000.0)
plt.figure(figsize=(10,7))
plt.ylabel('log(D(s))', fontsize = 18)
plt.xlabel('log(s)',fontsize = 18)
plt.plot(X,Y,'b.', markersize=12)
a = np.linspace(0,2,len(X))
b = z1[0]*a+ z1[1]
plt.plot(a,b,'k--', markersize = 12)
plt.title('Linear fit')
plt.figtext(0.80, 0.045, 'PHY473', color='black', weight='roman', size='small')
plt.savefig('1dlinear.png')
plt.show()
