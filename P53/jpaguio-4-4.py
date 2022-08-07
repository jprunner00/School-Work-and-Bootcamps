#Paguio, Jarred
#42762868

import math

#False Positive (Position?)
def falsePosition(a,b,tol):
    condition = True
    while condition:
        x = a - (b - a) * f(a) / (f(b) - f(a))
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        condition = abs(f(x)) > tol
    return(x)

print("cos(x^2)")
def f(x):
    return(math.cos(x**2))
answer = falsePosition(-0.5,2.0,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)

#Infinite loop
#print("x^3+2x^2-4x-4")
#def f(x):
    #return(x**3 + 2*x**2 - 4*x - 4)
#answer = falsePosition(-3,2,0.000001)
#print'Root:',answer
#print'Function at root:',f(answer)
#print'Answer 10^-1:',round(answer, 1)
#print'Answer 10^-2:',round(answer, 2)
#print'Answer 10^-5:',round(answer, 5)

#Getting a root before the boundry
print("x^2*cos(x)")
def f(x):
    return((x**2)*math.cos(x))
answer = falsePosition(1,5,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)
