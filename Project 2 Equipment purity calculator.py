# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:20:35 2023

@author: graha
"""

sugar = 0.2
water = 0.6
fiber = 0.2

fermenter = float(input("Input Fermenter value: "))
Filter = float(input("Input Filter value: "))
distiller = float(input("Input Distiller value: "))
dehydrator = float(input("Input Dehydrator value: "))

E = sugar*0.51*fermenter
S = sugar*(1.0-fermenter)

F = fiber*(1.0-Filter)

S2 = (S*E*((1.0/distiller)-1.0))/(water+S+F)
W = (water*E*((1.0/distiller)-1.0))/(water+S+F)
F2 = (F*E*((1.0/distiller)-1.0))/(water+S+F)

W2 = W*(1.0-dehydrator)

#print ("The final mass of ethanol is: ", E)
#print ("The final mass of sugar is: ", S2)
#print ("The final mass of water is: ", W2)
#print ("The final mass of fiber is: ", F2)

purity = (E/(E+S2+F2+W2))*100.0

print ("The final purity of the ethanol is: %", purity)