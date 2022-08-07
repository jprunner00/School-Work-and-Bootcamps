#Paguio, Jarred
#42762868

import math
import matplotlib.pyplot as plt

def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

cities = raw_input("Input numbers 1-11 with a space in between. ")

cities = cities.split()

print(cities)

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

for i in range(len(cities)-1):
    city1 = (coordinates.get(cities[i]))
    city2 = (coordinates.get(cities[i+1]))
    x1 = (city1[0])
    y1 = (city1[1])
    x2 = (city2[0])
    y2 = (city2[1])
    totaldistance.append(distance(x1, x2, y1, y2))
    xcoordinates.append(x1)
    xcoordinates.append(x2)
    ycoordinates.append(y1)
    ycoordinates.append(y2)
print(sum(totaldistance))

plt.plot(xcoordinates, ycoordinates)
plt.show()
