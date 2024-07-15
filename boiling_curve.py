# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Vidhya Kommineni
# Section:      562
# Assignment:   Lab 5 individual
# Date:         9/30/22

from math import*

xa = 1.3
ya = 1000
xb = 5
yb = 7000
xc = 30
yc = 1.5*10**6
xd = 120
yd = 2.5*10**4
xe = 1200
ye = 1.5*10**6

#calculating the m
ma  = log (yb/ya)/ log (xb/xa)
mb = log (yc/yb)/ log (xc/xb)
mc = log (yd/yc) / log (xd / xc)
md = log (yc/yd)/ log(xe / xd)

#getting excess 
excess = float(input("Enter the excess temperature: "))

#Calculating heat flux for point A
if xa <= excess and excess <= xb:
    x0 = xa
    y0 = ya
    m = ma
    x = excess
    y = y0 * (x/x0) ** m
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
#Calculating for point B
elif xb <= excess and excess < xc:
    x0 = xb
    y0 = yb
    m = mb
    x = excess
    y =  y0 * (x/x0) ** m
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
#Calculating for point C
elif xc <= excess and excess < xd:
    x0 = xc
    y0 = yc
    m = mc
    x = excess
    y =  y0 * (x/x0) ** m
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
#Calculating for point D
elif xd <= excess and excess <= xe:
    x0 = xd
    y0 = yd
    m = md
    x = excess
    y =  y0 * (x/x0) ** m
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
#Prints it only if none of the above ones work
else:
    print("Surface heat flux is not available")