#Paguio,Jarred
#42762868

from scipy.integrate import quad
import math

def integrand(x):
    return math.exp(-x**2)

a = float(raw_input('Select a number greater than 3: '))
b = 0

ans, err = quad(integrand, b, a)

print(ans)
print 'Error is',err
