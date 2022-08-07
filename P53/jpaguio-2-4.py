#Paguio, Jarred
#42762868

import matplotlib.pyplot
import random

rng=[]

for x in range (0,25):
    rng=rng+[random.randint(65,75)]
    
print rng

y=range(0,25)

print y

matplotlib.pyplot.plot(y,rng)

matplotlib.pyplot.savefig("jpaguio-graph-2-4")
