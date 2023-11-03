# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:29:03 2023

@author: aust1
"""

import itertools as it
import Project2_Input_Energy_Calculator as ec

# building all pipe combos
pipeLines = ["Salvage", "Questionable", "Better", "Nice", "Outstanding", "Glorious"]
diameters = [0.1,0.11,0.12,0.13,0.14,0.15]
totalPipes = []

for pipeType, diameter in it.product(pipeLines, diameters):
    fricFactor = None
    costPerMeter = None
    
    if pipeType == "Salvage":
        fricFactor = 0.05
        costPerMeter = {0.1:1,0.11:1.2,0.12:2.57,0.13:6.3,0.14:14,0.15:26}[diameter]
    elif pipeType == "Questionable":
        fricFactor = 0.03
        costPerMeter = {0.1:1.2,0.11:1.44,0.12:3.08,0.13:7.56,0.14:16,0.15:31}[diameter]
    elif pipeType == "Better":
        fricFactor = 0.02
        costPerMeter = {0.1:1.44,0.11:1.72,0.12:3.7,0.13:9.07,0.14:20,0.15:37}[diameter]

    elif pipeType == "Nice":
        fricFactor = 0.01
        costPerMeter = {0.1:2.16,0.11:2.58,0.12:5.55,0.13:14,0.14:29,0.15:55}[diameter]

    elif pipeType == "Outstanding":
        fricFactor = 0.005
        costPerMeter = {0.1:2.7,0.11:3.23,0.12:6.94,0.13:17,0.14:37,0.15:69}[diameter]

    elif pipeType == "Glorious":
        fricFactor = 0.002
        costPerMeter = {0.1:2.97,0.11:3.55,0.12:7.64,0.13:19,0.14:40,0.15:76}[diameter]
    else:
        fricFactor = None
        costPerMeter = None
            
    totalPipes.append({"name": pipeType, "diameter": diameter, "fricFactor": fricFactor, "costRate": costPerMeter})
    
# build all angle combos, only using 90 degrees
bendAngle = 90
diameters = [0.1,0.11,0.12,0.13,0.14,0.15]
totalAngles = []

for diameter in diameters:
    pipeLoss = 0.3
    costPerMeter = {0.1:1.28,0.11:1.9,0.12:7,0.13:18,0.14:41,0.15:81}[diameter]
            
    totalAngles.append({"angle": bendAngle, "diameter": diameter, "pipeLoss": pipeLoss, "costRate": costPerMeter})

# build pumps
ratingMeters = 12
pumpLines = ["Cheap", "Value", "Standard", "High-Grade", "Premium"]
totalPumps = []

for pumpType in pumpLines:
    pumpLoss = {"Cheap": 0.8, "Value": 0.83, "Standard": 0.86, "High-Grade": 0.89, "Premium": 0.92}[pumpType]
    costPerMeter = {"Cheap": 240, "Value": 290, "Standard": 340, "High-Grade": 410, "Premium": 502}[pumpType]
            
    totalPumps.append({"name": pumpType, "ratingMeters": ratingMeters, "pumpLoss": pumpLoss, "costRate": costPerMeter}) 
    
# build Valves
valveLines = ["Salvage", "Questionable", "Outstanding", "Glorious"]
diameters = [0.1,0.11,0.12,0.13,0.14,0.15]
totalValves = []

for valveType, diameter in it.product(valveLines, diameters):
    flowCoef = None
    costPerMeter = None
    
    if valveType == "Salvage":
        flowCoef = 800
        costPerMeter = {0.1:1,0.11:1.2,0.12:2.57,0.13:6.3,0.14:14,0.15:26}[diameter]
    elif valveType == "Questionable":
        flowCoef = 700
        costPerMeter = {0.1:1.2,0.11:1.44,0.12:3.08,0.13:7.56,0.14:16,0.15:31}[diameter]

    elif valveType == "Outstanding":
        flowCoef = 600
        costPerMeter = {0.1:2.7,0.11:3.23,0.12:6.94,0.13:17,0.14:37,0.15:69}[diameter]

    elif valveType == "Glorious":
        flowCoef = 500
        costPerMeter = {0.1:2.97,0.11:3.55,0.12:7.64,0.13:19,0.14:40,0.15:76}[diameter]
    else:
        flowCoef = None
        costPerMeter = None
            
    totalValves.append({"name": valveType, "diameter": diameter, "flowCoef": flowCoef, "costRate": costPerMeter})



# generate all combonations
for pipe1, pipe2, pipe3, pipe4, pipe5, angle, pump, valve1, valve2, valve3, valve4, valve5, valve7, valve8 in it.product(totalPipes, totalPipes, totalPipes, totalPipes, totalPipes, totalAngles, totalPumps, totalValves, totalValves, totalValves, totalValves, totalValves, totalValves, totalValves, totalValves):
    KE, input = ec.energyCalc(pipe1["diameter"],pipe2["diameter"],pipe3["diameter"],pipe4["diameter"],pipe5["diameter"],pipe1["fricFactor"],pipe2["fricFactor"],pipe3["fricFactor"],pipe4["fricFactor"],pipe5["fricFactor"],angle["pipeLoss"], valve1["flowCoef"], valve2["flowCoef"], valve3["flowCoef"], valve4["flowCoef"], valve5["flowCoef"], valve7["flowCoef"], valve8["flowCoef"], pump["pumpLoss"])
    print(KE)