import numpy as np
import matplotlib.pyplot as plt
import random
from collections import Counter
from matplotlib.colors import LogNorm

N  = 500
x = np.zeros(N)
for i in range(N):
    x[i] = int(200000/(i+1)**1.5)
    
grain = np.random.randint(1000,2000,1)
initialsum = sum(x)
stored = grain[0]

# = np.linspace(0,N,N)
y = np.linspace(0,N,N)
#plt.loglog(y,x)
#prob = np.random.randint(0,2,10)
for i in range(N-1):
    quant = int(0.8*(x[i])**(1.5))
    prob = np.random.randint(0,2,1)
    if (prob):
        x[i+1] +=quant
        x[i]-= quant
         
exit1 = int((x[N-1])**0.8)
finalsum = sum(x)-exit1
print stored, initialsum, finalsum, exit1
print finalsum-initialsum
y = np.linspace(0,N,N)
plt.plot(y,x)
#plt.colorbar()
plt.show()