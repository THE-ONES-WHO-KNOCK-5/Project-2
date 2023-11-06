# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:51:27 2023

@author: graha
"""

import math as m
import Project2_Equipment_Optimizer as eo    

# pipe distances (m)
L1 = 1 + 0.762
L2 = 0.762 + 1.524
L3 = 3.048
L4 = 3.048
L5 = 1.324 + 3 + 10.716

LCO2 = 3.048 + 1
Lfilt = 1
Ldist = 1
Ldehy = 1

# slurry density between systems kg/m^3
p1= eo.equipmentCalc(100000)[2][0]
p2= eo.equipmentCalc(100000)[2][1]
p3= eo.equipmentCalc(100000)[2][2]
p4= eo.equipmentCalc(100000)[2][3]
p5= eo.equipmentCalc(100000)[2][4]

# flow rate in a day (m^3/s)
Q1 = eo.equipmentCalc(100000)[3][0]
Q2 = eo.equipmentCalc(100000)[3][1]
Q3 = eo.equipmentCalc(100000)[3][2]
Q4 = eo.equipmentCalc(100000)[3][3]
Q5 = eo.equipmentCalc(100000)[3][4]


# time between rate change (one second)
t = (24 * 60 * 60)

# calculates masses between systems (kg)
M1 = p1 * Q1 * t
M2 = p2 * Q2 * t
M3 = p3 * Q3 * t
M4 = p4 * Q4 * t
M5 = p5 * Q5 * t

# calculates masses of waste materials
MCO2 = M1 - M2
Mfiber = M2 - M3
Mdistiller = M3 - M4
Mwater = M4 - M5

ventDiameters = [1.0,1.25,1.5]
ventFriction = 0.002
ventCosts = [228,414,700]
ventPrices = []

pipeDiameters = [0.10,0.11,0.12,0.13,0.14,0.15]
pipeFrictions = [0.05,0.03,0.02,0.01,0.005,0.002]
pipecosts = [[1,1.2,1.44,2.16,2.70,2.97],[1.2,1.44,1.72,2.58,3.23,3.55],[2.57,3.08,3.70,5.55,6.94,7.64],[6.30,7.56,9.07,14,17,19],[14,16,20,29,37,40],[26,31,37,55,69,76]]
filtPrices = []
distPrices = []
dehyPrices = []

qualityDescriptions = ["Salvage","Questionable","Better","Nice","Outstanding","Glorious"]

for d in ventDiameters:
    if d >= (ventFriction * LCO2):
        priceCO2 = LCO2 * ventCosts[ventDiameters.index(d)]
        ventPrices.append(priceCO2)
print (min(ventPrices))

for d in pipeDiameters:
    for f in pipeFrictions:
        if d >= (f * Lfilt):
            priceFilt = Lfilt * pipecosts[pipeDiameters.index(d)][pipeFrictions.index(f)]
            filtPrices.append(priceFilt)
print (qualityDescriptions[filtPrices.index(min(filtPrices))], "Fiber pipe of diameter:", pipeDiameters[filtPrices.index(min(filtPrices))], "m")
print (min(filtPrices))



for d in pipeDiameters:
    for f in pipeFrictions:
        if d >= (f * Ldist):
            priceDist = Ldist * pipecosts[pipeDiameters.index(d)][pipeFrictions.index(f)]
            distPrices.append(priceDist)
print (min(distPrices))

for d in pipeDiameters:
    for f in pipeFrictions:
        if d >= (f * Ldehy):
            priceDehy = Ldehy * pipecosts[pipeDiameters.index(d)][pipeFrictions.index(f)]
            dehyPrices.append(priceDehy)
print (min(dehyPrices))