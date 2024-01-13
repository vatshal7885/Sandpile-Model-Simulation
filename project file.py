#! /Library/Frameworks/Python.framework/Versions/Current/bin/python


# I ripped off the mencoder stuff from thee matplotlib website
# That stuff is copyright Josh Lifton 2004, used with permission
# The rest is copyright J. Emrys Landivar 2010
#
# 'Permission is hereby granted to use and abuse this document
# so long as proper attribution is given.'


import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.colorbar as cbar
from numpy.random import randn
from scipy import integrate
import matplotlib
matplotlib.use('Agg')
import subprocess                 # For issuing commands to the OS.
import os
import sys                        # For determining the Python version.



table_size=31 #the size of the table that the sandpile is on
z_crit=4  #the critical size of a stack of grains, it will fall if there are more grains that that
num_grains=1000 #how many grains to drop
z=np.zeros((table_size+2,table_size+2)) #thisis the sandpile and the table it rests on
add_location=(table_size/2+1,table_size/2+1) # sets the middle of the table to drop grains on

#
print 'Executing on', os.uname()
print 'Python version', sys.version
print 'matplotlib version', matplotlib.__version__

not_found_msg = """
The mencoder command was not found;
mencoder is used by this script to make an avi file from a set of pngs.
"""  #this was shamelessly ripped off from elsewhere

try:
    subprocess.check_call(['mencoder'])
except subprocess.CalledProcessError:
    print "mencoder command was found"
    pass # mencoder is found, but returns non-zero exit as expected
    # This is a quick and dirty check; it leaves some spurious output
    # for the user to puzzle over.
except OSError:
    print not_found_msg
    sys.exit("quitting\n")



z2=z.copy()
fig=plt.figure()


for g in xrange(num_grains):
    z[add_location[0],add_location[1]] += 1 #drop a grain
    for x in xrange(1,table_size+1): 
        for y in xrange(1,table_size+1):
            if z2[x,y] > z_crit:  #check for colapse
                    z[x,y]-=4   #colapse
                    z[x+1,y]+=1
                    z[x-1,y]+=1
                    z[x,y+1]+=1
                    z[x,y-1]+=1
    z2=z.copy()
    
    #drop the grains over the edge off the table.
    z[0,0:table_size+2]=np.zeros(table_size+2)
    z[0:table_size+2,table_size+1]=np.zeros(table_size+2)
    z[0:table_size+2,0]=np.zeros(table_size+2)
    z[table_size+1,0:table_size+2]=np.zeros(table_size+2)
    
    #plotting!!
    ax=fig.add_subplot(111)
    ax.set_title('Height of the Sandpile')
    cax = ax.imshow(z, interpolation='nearest')
    cax.set_clim(vmin=0, vmax=8)
    cbar = fig.colorbar(cax, ticks=[0,3, 5, 8], orientation='vertical')

    filename = str('%03d' % g) + '.png'
    plt.savefig(filename, dpi=100)
    print 'Wrote file', filename
    
    plt.clf()

#print sum(sum(z))

#make the movie

command = ('mencoder',
            'mf://*.png',
            '-mf',
            'type=png:w=800:h=600:fps=25',
            '-ovc',
            'lavc',
            '-lavcopts',
            'vcodec=mpeg4',
            '-oac',
            'copy',
            '-o',
            'output.avi')

#os.spawnvp(os.P_WAIT, 'mencoder', command)

print "\n\nabout to execute:\n%s\n\n" % ' '.join(command)
subprocess.check_call(command)

print "\n\n The movie was written to 'output.avi'"

print "\n\n You may want to delete *.png now.\n\n"
POSTED BY DOC MERLIN AT 7/16/2010 02:54:00 AM   
LABELS: CELLULAR AUTOMATA, CODE, ORGANIZED CRITICALITY
