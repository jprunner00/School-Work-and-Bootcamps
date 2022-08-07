#Paguio, Jarred
#42762868

import math

#Bisection method
def bisection(a,b,tol):
    if f(a)*f(b) > 0:
       print("No root found.")
    else:
        while (b-a)/2.0 > tol:
            midpoint = (a + b)/2.0
            if f(midpoint) == 0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return(midpoint)

print("cos(x^2)")
def f(x):
    return(math.cos(x**2))
answer = bisection(-0.5,2.0,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)

print("x^3+2x^2-4x-4")
def f(x):
    return(x**3 + 2*x**2 - 4*x - 4)
answer = bisection(-3,2,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)

#Breaking
print("x^2*cos(x)")
def f(x):
    return((x**2)*math.cos(x))
answer = bisection(1,5,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)
