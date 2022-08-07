#Paguio, Jarred
#42762868

import math
import matplotlib.pyplot as plt
import random

def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

cities = (random.sample(range(1,12),11))

coordinates = {
    "1" : [1500, 10],
    "2" : [20, 300],
    "3" : [3020, 1195],
    "4" : [1400, 985],
    "5" : [10, 1100],
    "6" : [2090, 400],
    "7" : [3075, -20],
    "8" : [1090, 1040],
    "9" : [1700, 1000],
    "10" : [1500, 190],
    "11" : [25, 950]
}

xcoordinates = []
ycoordinates = []
totaldistance = []
totaldistance1 = 1000000
for h in range(1000):
    a = random.randint(0,10)
    b = random.randint(0,10)
    if b is a:
        b = random.randint(0,10)
    cities[a],cities[b] = cities[b],cities[a]
    print cities
    for i in range(len(cities)-1):
        city1 = (coordinates.get(str(cities[i])))
        city2 = (coordinates.get(str(cities[i+1])))
        x1 = (city1[0])
        y1 = (city1[1])
        x2 = (city2[0])
        y2 = (city2[1])
        totaldistance.append(distance(x1, x2, y1, y2))
    totaldistance2 = sum(totaldistance)
    print'Shortest distance calculated prior:',totaldistance1
    print'Distance calculated:',totaldistance2
    totaldistance = []
    if totaldistance2 < totaldistance1:
        totaldistance1 = totaldistance2
    else:
        cities[b],cities[a] = cities[a],cities[b]

print'Shortest distance:',totaldistance1
print'City order with the shortest distance:',cities

for i in range(len(cities)-1):
    city1 = (coordinates.get(str(cities[i])))
    city2 = (coordinates.get(str(cities[i])))
    xcoordinates.append(city1[0])
    xcoordinates.append(city2[0])
    ycoordinates.append(city1[1])
    ycoordinates.append(city2[1])

plt.plot(xcoordinates, ycoordinates)
plt.show()
