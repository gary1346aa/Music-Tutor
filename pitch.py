##pitch detection
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import math
import essentia
from essentia.standard import*
import essentia.streaming
import matplotlib.pyplot as plt
import numpy as np

ghgh
# we start by instantiating the audio loader:
loader1 = essentia.standard.MonoLoader(filename='/Users/tsaiyunyun/Desktop/scomb1.1.wav')
loader2 = essentia.standard.MonoLoader(filename='/Users/tsaiyunyun/Desktop/scomb2.1.wav')

# and then we actually perform the loading:
audio1 = loader1()
audio2 = loader2()

mp = MultiPitchKlapuri(hopSize = 256)
mp1 = MultiPitchKlapuri(hopSize = 256)
MP = mp(audio1)
MP1 = mp1(audio2)

tone = []
tone1 = []
miss = []
all_miss = []

for i in xrange(len(MP)):
    semitone = 69+(12* math.log(MP[i][0]/440,2))
    tone.append(semitone) 

for i in xrange(1,len(tone)):
    if tone[i-1]!=float('nan') and np.abs(tone[i]-tone[i-1])>=7:
        outlier = tone[i]
        for j in xrange(i+1,i+4):
            print j
            if j<len(tone) and np.abs(outlier-tone[j])>=7:
                for k in xrange(i,j-1):
                    tone[k] = float('nan')
                 

                
for i in xrange(len(MP1)):
    tone1.append(69+(12* math.log(MP1[i][0]/440,2)))
    
for i in xrange(1,len(tone1)):
    if tone1[i-1]!=float('nan') and np.abs(tone1[i]-tone1[i-1])>=7:
        outlier = tone1[i]
        for j in xrange(i+1,i+6):
            print j
            if j<len(tone1) and np.abs(outlier-tone1[j])>=7:
                for k in xrange(i,j-1):
                    tone1[k] = float('nan')
       


    
for j in xrange(1,len(tone)):
    #print np.abs(tone[j]-tone1[j])
    if np.abs(tone[j]-tone1[j])>1:
        miss.append(j)
        print "In frame %i "%j + "......difference %f"%np.abs(tone[j]-tone1[j])

ax = plt.subplot(111)
x = np.arange(0,len(tone))
y = tone

x1 = np.arange(0,len(tone1))
y1 = tone1
ax.plot(x,y,"c",lw=4,label = 'Teacher Pitch') 
ax.plot(x1,y1,"k",lw=2,label = 'Student Pitch')
plt.xlim(0,len(MP))
plt.ylim(36,80)


plt.xlabel("frame") 
plt.ylabel("semitone") 
plt.title("smooth Pitch detection") 
ax.legend()
plt.show() 
