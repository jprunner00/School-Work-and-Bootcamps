#Paguio,Jarred
#42762868

import math
import matplotlib.pyplot as plt

#Initial Values
R = float(raw_input("How many Ohms in this circuit? (Resistance) "))
L = float(raw_input("How many Henry in this circuit? (Inductance) "))
C = float(raw_input("How many Farad in this circuit? (Capacitance) "))
time_limit = float(raw_input("How long do you want to run the circuit in seconds? "))
dt = float(raw_input("How often do you want to check the circuit in seconds? "))
t = float(0)
didt = float(0)
inti = float(0)
i = float(0)
omega = 1 / (L * C)**(1/2)

#Setting up plots
timeplot = []
currentplot = []
chargeplot = []
didtplot = []

#Calculating values
while t < time_limit:
    timeplot.append(t)
    v = math.sin(omega * t)
    inti = inti + i * dt
    chargeplot.append(inti)
    didt = (v - inti / C - R * i) / L
    didtplot.append(didt)
    i = i + didt * dt
    currentplot.append(i)
    t = t + dt
    
#Plotting
fig, ax = plt.subplots()
line1, = ax.plot(timeplot,currentplot,label="Current")
line2, = ax.plot(timeplot,chargeplot,label="Charge")
line3, = ax.plot(timeplot,didtplot,label="Derivative of Current")
ax.legend()
plt.show()
    
    
    
