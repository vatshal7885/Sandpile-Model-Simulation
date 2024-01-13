import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from collections import Counter
def drawf(t,x):
    plt.matshow(x, cmap=cm.viridis)
    plt.colorbar()
    #plt.axis((0,20,0,1))
	#plt.xlabel('x') 
	#plt.ylabel('P(x,t)')
    plt.figtext(0.20, 0.04, 'Grain count = %d' % t, color='black', weight='roman', size='x-large')
    #plt.title('Grain count = %05.1f' % t)

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
b=10                        #use various initial conditions given in paper like away from equillibrium and flat surface
t = np.linspace(0,10000,10000)

for i in range(10000):
    counter=0
    x=int(N/4)-1
    y=int(N/4)-1
    x1 = int(3*N/4)-1
    y1 = int(N/4)-1
    x2 = int(N/4)-1
    y2 = int(3*N/4)-1
    x3 =int(3*N/4)-1
    y3 = int(3*N/4)-1
    Matrix[x][y]+=1
    Matrix[x1][y1]+=1
    Matrix[x2][y2]+=1
    Matrix[x3][y3]+=1
    if(Matrix[x][y]>=4):
        check(Matrix,x,y)
    if(Matrix[x1][y1]>=4):
        check(Matrix,x1,y1)
    if(Matrix[x2][y2]>=4):
        check(Matrix,x2,y2)
    if(Matrix[x3][y3]>=4):
        check(Matrix,x3,y3)
    #z.append(counter)
    file_name='_temp%05d.png' % i
    # file_name = _temp(i).png
    drawf(t[i], Matrix) 
    plt.savefig(file_name) 
    plt.clf()
    '''if k == 1:
        c=Counter(z)
        xflat=(np.array(list(c.keys())))
        yflat=(np.array(list(c.values())))
        plt.figure(figsize=(10,7))
        #plt.subplot(211)
        plt.loglog(xflat,yflat/10000.0,'b.')
        plt.ylabel('D(s)', fontsize = 18)
        plt.xlabel('s',fontsize = 18)
        plt.title('Power Law on flat surface')
        plt.figtext(0.80, 0.045, 'PHY473', color='black', weight='roman', size='small')
        plt.savefig('plot1.png')

c=Counter(z)
#yy=c.values()
#xx=c.keys()
xx1=(np.array(list(c.keys())))
yy1=(np.array(list(c.values())))
c1 = len(xx1)
#[0:int(c/10)]
X = np.log10(xx1[0:int(c1/10)])
Y = np.log10(yy1[0:int(c1/10)]/10000.0)
X[0]=0
z1 = np.polyfit(X,Y,1)
print "Slope = %s"  %z1[0]

plt.figure(figsize=(10,7))
#plt.subplot(212)
plt.loglog(xx1,yy1/10000.0,'b.')
plt.ylabel('D(s)', fontsize = 18)
plt.xlabel('s',fontsize = 18)
plt.title('Power Law on irregular surface')
plt.figtext(0.80, 0.045, 'PHY473', color='black', weight='roman', size='small')
plt.savefig('plot2.png')
plt.show()
X = np.log10(xx1)
Y = np.log10(yy1/10000.0)
plt.figure(figsize=(10,7))
plt.ylabel('log(D(s))', fontsize = 18)
plt.xlabel('log(s)',fontsize = 18)
plt.plot(X,Y,'b.')
a = np.linspace(0,3,1000)
b = z1[0]*a+ z1[1]
plt.plot(a,b,'k--')
plt.title('Linear fit')
plt.figtext(0.80, 0.045, 'PHY473', color='black', weight='roman', size='small')
plt.savefig('plot3.png')
plt.show()'''
