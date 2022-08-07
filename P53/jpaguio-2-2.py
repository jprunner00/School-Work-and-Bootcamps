#Paguio, Jarred
#42762868

#Finding roots for ax^2+bx+c=0 with 2, 1 , and imaginary roots

print 'This program finds roots for binomial ax^2+bx+c'
a = int(raw_input("Input a value for a: "))
b = int(raw_input("Input a value for b: "))
c = int(raw_input("Input a value for c: "))

discriminant = (b**2) - (4*a*c)
print "The discriminant is " + str(discriminant) + "."

if(discriminant > 0):
    root1 = ((-b + (discriminant**.5)) / (2*a))
    root2 = ((-b - (discriminant**.5)) / (2*a))
    print "Two real roots exist: " + str(root1) + " and " + str(root2) + "."
elif(discriminant == 0):
    root = ((-b) / (2*a))
    print "One real root exists: " + str(root) + "."
elif(discriminant < 0 ):
    root = ((-b) / (2*a))
    imaginary = (((-discriminant)**0.5) / (2*a))
    print "Two imaginary roots exist: " + str(root) + "+" + str(imaginary) + "i"  + " and " + str(root) + "-" + str(imaginary) + "i."
