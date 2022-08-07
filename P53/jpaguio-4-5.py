#Paguio, Jarred
#42762868

import math

#Newton's Method
def dx(f,x):
    return abs (0-f(x))

def newtons(f,df,a,tol):
    delta = dx(f,a)
    while delta > tol:
        a = a - f(a)/df(a)
        delta = dx(f,a)
    return(a)

print("cos(x^2)")
def f(x):
    return(math.cos(x**2))
def df(x):
    return((-2)*x*math.sin(x**2))
answer = newtons(f,df,-0.5,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)

#Breaks, divides by 0
#print("x^3+2x^2-4x-4")
#def f(x):
    #return(x**3 + 2*x**2 - 4*x - 4)
#def df(x):
    #return(3*x**2 + 4*x - 4)
#answer = newtons(f,df,-3,0.000001)
#print'Root:',answer
#print'Function at root:',f(answer)
#print'Answer 10^-1:',round(answer, 1)
#print'Answer 10^-2:',round(answer, 2)
#print'Answer 10^-5:',round(answer, 5)

print("x^2*cos(x)")
def f(x):
    return((x**2)*math.cos(x))
def df(x):
    return(2*x*math.cos(x) - x**2*math.sin(x))
answer = newtons(f,df,1,0.000001)
print'Root:',answer
print'Function at root:',f(answer)
print'Answer 10^-1:',round(answer, 1)
print'Answer 10^-2:',round(answer, 2)
print'Answer 10^-5:',round(answer, 5)
