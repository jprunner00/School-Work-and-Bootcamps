#Paguio, Jarred
#42762868

import random

N=input("How many numbers do you want in a list? ")
sorting=[]

#Creates a list of n numbers
for x in range(N):
    sorting = sorting + [random.randint(0,1000000)]
print "Not sorted: " + str(sorting)

#Insertion Sorting
for x in range(1,N):
    temp=sorting[x]
    y = x-1
    while y >= 0 and temp < sorting[y]:
        sorting[y+1] = sorting[y]
        y=y-1
    sorting[y+1]=temp

print "Sorted: " + str(sorting)
