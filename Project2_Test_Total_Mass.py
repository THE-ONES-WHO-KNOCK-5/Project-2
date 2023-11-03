# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:10:45 2023

@author: aust1
"""


initMass = 3904169.82
initDensity = 1180.2
initVolume = initMass/initDensity
print("Inital Slurry Volume: ",initVolume, "m^3")
print("m^3/hr: ",initVolume/24, "m^3")
print("m^3/s: ",initVolume/24/60/60, "m^3")



sugar = initMass * .2
water = initMass * 0.6
fiber = initMass * 0.2

fermenter = 0.9
Filter = 0.9
distiller = 0.9
dehydrator = 0.9

E = sugar*0.51*fermenter
S = sugar*(1.0-fermenter)

F = fiber*(1.0-Filter)

S2 = (S*E*((1.0/distiller)-1.0))/(water+S+F)
W = (water*E*((1.0/distiller)-1.0))/(water+S+F)
F2 = (F*E*((1.0/distiller)-1.0))/(water+S+F)

W2 = W*(1.0-dehydrator)

print ("The final mass of ethanol is: ", E)
print ("The final mass of sugar is: ", S2)
print ("The final mass of water is: ", W2)
print ("The final mass of fiber is: ", F2)

purity = (E/(E+S2+F2+W2))*100.0

print ("The final purity of the ethanol is: %", purity)