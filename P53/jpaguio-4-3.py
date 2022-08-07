#Paguio, Jarred
#42762868

import math

#Secant method
def secant(a,b,tol):
    x = a
    if f(a)*f(b) < 0:
        while abs(f(x)) > tol:
            x = (a * f(b) - b * f(a)) / (f(b) - f(a))
            a = b
            b = x
        return(x)

print("cos(x^2)")
def f(x):
    return(math.cos(x**2))
answer = secant(-0.5,2.0,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)

#Divides by zero eventually so it breaks
#print("x^3+2x^2-4x-4")
#def f(x):
    #return(x**3 + 2*x**2 - 4*x - 4)
#answer = secant(-3,2,0.000001)
#print'Root:',answer
#print'Function at root:',f(answer)
#print'Answer 10^-1:',round(answer, 1)
#print'Answer 10^-2:',round(answer, 2)
#print'Answer 10^-5:',round(answer, 5)

#Breaking
print("x^2*cos(x)")
def f(x):
    return((x**2)*math.cos(x))
answer = secant(1,5,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)

                  
    
