#Paguio, Jarred
#42762868

import matplotlib.pyplot as plt
import math
import numpy as np

def f(x):
    return math.sin(x)

#Range of function
a=-2
b=2

#Indicates the step (Inverse of 20 leads to 0.05)
s=20

#Number of terms
N=input("How many terms? ")

#Blank lists
x=[]
y=[]

for i in range(N):
    xi=i*(b-a)/(1.0*s)
    x.append(xi)
    y.append(f(xi))

u = np.arange(0,2*np.pi,0.05)
v = np.sin(u)

#Shows the approximation vs the sine wave
#May not be able to see the approximation due to the overlap of the approximation and the exact (Slightly darker part of the line shows the overlap)
plt.plot(x,y,u,v)
plt.show()
