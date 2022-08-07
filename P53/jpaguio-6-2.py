#Paguio,Jarred
#42762868

import math

x = float(raw_input('Input a value for x. '))

def recur_sin(x):
    if x < 0.1:
        return x - (x**3) / 6
    else:
        return 2*math.sin(x/2)*math.cos(x/2)

def recur_cos(x):
    if x < 0.1:
        return 1 - (x**2) / 2
    else:
        return 1 - 2*(math.sin(x/2))**2

print('Sine Recursion: ',recur_sin(x))
print('Python Sine function: ',math.sin(x))
print('Cosine Recursion: ',recur_cos(x))
print('Python Cosine function: ',math.cos(x))

    
