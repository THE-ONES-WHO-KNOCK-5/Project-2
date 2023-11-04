# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:56:02 2023

@author: graha
"""

pSugar = 1599
pEthanol = 789
pFiber = 1311
pWater = 997

sugar = 0.2
water = 0.6
fiber = 0.2

def densityCalc(fermenter, Filter, distiller, dehydrator):
    #fermenter = float(input("Input Fermenter value: "))
    #Filter = float(input("Input Filter value: "))
    #distiller = float(input("Input Distiller value: "))
    #dehydrator = float(input("Input Dehydrator value: "))

    p1 = sugar*pSugar + water*pWater + fiber*pFiber
    print ("p1 =", p1)

    E = sugar*0.51*fermenter
    S = sugar*(1.0-fermenter)
    CO2 = sugar*0.49*fermenter

    p2 = (E*pEthanol + S*pSugar + water*pWater + fiber*pFiber)/(1- CO2)
    print ("p2=", p2)

    F = fiber*(1.0-Filter)
    Fwaste = fiber*Filter

    p3 = (E*pEthanol + S*pSugar + water*pWater + F*pFiber)/(1- CO2 - Fwaste)
    print ("p3=", p3)

    S2 = (S*E*((1.0/distiller)-1.0))/(water+S+F)
    W = (water*E*((1.0/distiller)-1.0))/(water+S+F)
    F2 = (F*E*((1.0/distiller)-1.0))/(water+S+F)

    p4 = (E*pEthanol + S2*pSugar + W*pWater + F2*pFiber)/(1- CO2 - Fwaste-(S-S2)-(F-F2)-(water-W))
    print ("p4=", p4)

    W2 = W*(1.0-dehydrator)

    p5 = (E*pEthanol + S2*pSugar + W2*pWater + F2*pFiber)/(1- CO2 - Fwaste-(S-S2)-(F-F2)-(water-W)-W*dehydrator)
    print ("p5=", p5)
