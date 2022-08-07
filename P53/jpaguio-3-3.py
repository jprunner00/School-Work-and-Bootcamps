#Paguio, Jarred
#42762868

import random

N=input("How many numbers do you want in a list? ")
sorting=[]

#Creates a list of n numbers
for x in range(N):
    sorting = sorting + [random.randint(0,1000000)]
print "Not sorted: " + str(sorting)

#Bubble Sorting
for i in range(N):
    for x in range(N-1):
        if sorting[x] > sorting[x+1]:
            sorting[x],sorting[x+1]=sorting[x+1],sorting[x]
        
print "Sorted: " + str(sorting)
