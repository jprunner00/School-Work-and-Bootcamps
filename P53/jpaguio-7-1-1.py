#Paguio, Jarred
#42762868

import random
import math
import matplotlib.pyplot as plt

#Randomizing initial coordinates
x = random.random()
y = random.random()
print'Initial coordinates:(',x,y,')'

#Initial angle
theta = random.randint(0,360)
print'Initial angle in degrees:',theta
theta = theta * math.pi / 180
print'Initial angle in radians:',theta

#Initial velocity
v = random.random() * 3
print'Initial velocity:',v
vx = v * math.cos(theta)
print'Initial x-velocity:',vx
vy = v * math.sin(theta)
print'Initial y-velocity',vy

#Time interval and gravity constant
g = -9.8
dt = 0.001

#Ball trajectory path
xcoordinates = []
ycoordinates = []

#Calculating path
while len(xcoordinates)<2000:
    xcoordinates.append(x)
    ycoordinates.append(y)
    
    #Position updates
    x = x + vx * dt
    y = y + vy * dt
    
    #Velocity updates
    if x > 1 or x < 0:
        vx = -1 * vx
    vy = vy + g * dt
    if y < 0:
        vy = -1 * vy - 0.07

#Graph
print'Red circle shows beginning of path.'
plt.plot(xcoordinates,ycoordinates)
plt.plot(xcoordinates[0],ycoordinates[0],'ro')
plt.show()

