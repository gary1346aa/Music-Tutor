import numpy as np
from numpy import *
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
from fastdtw import fastdtw
import math

Tpitch = np.array(tone)
Spitch = np.array(tone1)

where_are_NaNs = isnan(Tpitch)
Tpitch[where_are_NaNs] = 0
dtw_Tpitch = Tpitch[np.nonzero(Tpitch)]

where_are_NaNs1 = isnan(Spitch)
Spitch[where_are_NaNs1] = 0
dtw_Spitch = Spitch[np.nonzero(Spitch)]


distance, path = fastdtw(dtw_Tpitch,dtw_Spitch, dist=euclidean)
print(distance)
T=[]
S=[]

for i in xrange(1,len(path)):
    T.append(path[i][0])
    S.append(path[i][1])

correct = 0
for i in xrange(1,len(T)):
    #print np.abs(p[i]-q[i])
    if(np.abs(T[i]-S[i])<0.5):
        correct = correct+1
acc = float(correct)/len(T)
print "ACC: %f"%acc


dtwpitch  = np.array(Spitch)
dtwpitch[:] = float('nan')
    
index = 1;
total = 0; correctNum = 0;
while index < len(S):
    note = Spitch[S[index]];
    #print "note = %f"%note
    istart = index;

    while index < len(S) and Spitch[S[index]]==note:
            index = index+1
    iend = index-1;  
    #for i in xrange(T[istart],T[iend],-1):
        #print np.abs(dtw_Spitch[S[i]-note])
        #if (np.abs(dtw_Spitch[T[i]-note])<0.5):
            #correctNum = correctNum+1
    #correctNum = correctNum + sum(abs(dtw_spitch(p(istart):p(iend)) - note ) < 0.5);
   
    for i in xrange(T[istart],T[iend]-1):
        dtwpitch[i] = note;
        #print "warping at frame %i"%i+ ".....Original_pitch %f "%original_p + "to pitch %f" %note
   
    #total = total + S[iend]-S[istart]+1; 
   
        #note = cpitch(q(index));
        #note
        #figure; subplot(2,1,1); plot(spitch(p(istart:iend))); title(sprintf('%.2f', note)); pause;
#print correctNum
#print total
#score = float(correctNum)/total * 100;
#print score
#dtw
ax = plt.subplot(111)


a2 = np.arange(0,len(tone))
b2 = tone
#mask = b.nonzero()
ax.plot(a2,b2,"c",lw=4,label = 'Teacher pitch')

a1 = np.arange(0,len(dtwpitch))
b1 = dtwpitch
#mask = b1.nonzero()
ax.plot(a1,b1,"k",lw=2,label = 'dtw Student pitch')

#a = np.arange(0,len(tone1))
#b = tone1
#mask = b.nonzero()
#ax.plot(a,b,"r",lw=1,label = 'Student pitch')


plt.xlim(0,len(x))
plt.ylim(36,80)
plt.xlabel("frame") 
plt.ylabel("semitone") 
plt.title("DTW of Pitch detection")
ax.legend()
plt.show() 
