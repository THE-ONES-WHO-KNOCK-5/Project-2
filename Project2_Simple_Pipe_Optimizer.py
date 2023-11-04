# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:29:03 2023

@author: aust1
"""

import itertools as it
import Project2_Input_Energy_Calculator as ec
import time




# define all possible diameters and relation of diameters to 2D Array Position
diameters = [0.1,0.11,0.12,0.13,0.14,0.15]
diameterDict = {0.1:0,0.11:1,0.12:2,0.13:3,0.14:4,0.15:5}
def optimizePipes():
    minPrice = 1
    maxEnergy = 0
    minset = []

    # building all pipe combos
    pipeLines = ["Salvage", "Questionable", "Better", "Nice", "Outstanding", "Glorious"]
    totalPipes = [[],[],[],[],[],[]]

    for diameter, pipeType in it.product(diameters, pipeLines):
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
                
        totalPipes[diameterDict[diameter]].append({"part": "Pipe", "name": pipeType, "diameter": diameter, "fricFactor": fricFactor, "costRate": costPerMeter})

    # build all angle combos, only using 90 degrees
    bendAngle = 90
    totalAngles = [None,None, None,None, None,None]

    for diameter in diameters:
        pipeLoss = 0.3
        costPerMeter = {0.1:1.28,0.11:1.9,0.12:7,0.13:18,0.14:41,0.15:81}[diameter]
                
        totalAngles[diameterDict[diameter]] = ({"part": "Bend", "angle": bendAngle, "diameter": diameter, "pipeLoss": pipeLoss, "costRate": costPerMeter})

    # build pumps
    ratingMeters = 12
    pumpLines = ["Cheap", "Value", "Standard", "High-Grade", "Premium"]
    totalPumps = []

    for pumpType in pumpLines:
        pumpLoss = {"Cheap": 0.8, "Value": 0.83, "Standard": 0.86, "High-Grade": 0.89, "Premium": 0.92}[pumpType]
        costPerMeter = {"Cheap": 240, "Value": 290, "Standard": 340, "High-Grade": 410, "Premium": 502}[pumpType]
                
        totalPumps.append({"part": "Pump", "name": pumpType, "ratingMeters": ratingMeters, "pumpLoss": pumpLoss, "costRate": costPerMeter}) 
        
    # build Valves
    valveLines = ["Salvage", "Questionable", "Outstanding", "Glorious"]
    totalValves = [[],[],[],[],[],[]]

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
                
        totalValves[diameterDict[diameter]].append({"part": "Valve", "name": valveType, "diameter": diameter, "flowCoef": flowCoef, "costRate": costPerMeter})

    # generate all combonations  total, 40000 a second
    allCombo = 238878720
    readVal = 100000
    for diameterGroup in range(len(diameters)):
        print("group: ", diameterGroup)

        for pipe1, pump, valve1 in it.product(totalPipes[diameterGroup], totalPumps, totalValves[diameterGroup]):
            pipe2 = pipe1
            pipe3 = pipe1
            pipe4 = pipe1
            pipe5 = pipe1
            
            valve2 = valve1
            valve3 = valve1
            valve4 = valve1
            valve5 = valve1
            valve6 = valve1
            valve7 = valve1
            valve8 = valve1

            # solves for energies and prices
            KE, KEin = ec.energyCalc(pipe1["diameter"],pipe2["diameter"],pipe3["diameter"],pipe4["diameter"],pipe5["diameter"],pipe1["fricFactor"],pipe2["fricFactor"],pipe3["fricFactor"],pipe4["fricFactor"],pipe5["fricFactor"],totalAngles[diameterGroup]["pipeLoss"], valve1["flowCoef"], valve2["flowCoef"], valve3["flowCoef"], valve4["flowCoef"], valve5["flowCoef"],valve6["flowCoef"], valve7["flowCoef"], valve8["flowCoef"], pump["pumpLoss"])
            initPrice = pipe1["costRate"]*ec.L1 + pipe2["costRate"]*ec.L2 + pipe3["costRate"]*ec.L3 + pipe4["costRate"]*ec.L4 + pipe5["costRate"]*ec.L5 + totalAngles[diameterGroup]["costRate"] + pump["costRate"]*ec.Q1*(24 * 60 * 60) + valve1["costRate"] + valve2["costRate"] + valve3["costRate"] + valve4["costRate"] + valve5["costRate"] + valve6["costRate"] + valve7["costRate"] + valve8["costRate"]
            dailyPrice = (KEin/3600)*0.1202

            #creates estimated price of facility running for 365 days
            estimatedPrice = initPrice + dailyPrice*365


            #print([pipe1, pump, valve1], "ratio: ",KE , initPrice, dailyPrice)

            # test for most energy to cheapest system ratio
            if KE / initPrice > maxEnergy / minPrice:
                minPrice = estimatedPrice
                KE = maxEnergy
                minset = [pipe1,pipe2,pipe3,pipe4,pipe5, totalAngles[diameterGroup], pump, valve1, valve2, valve3, valve4, valve5, valve6,valve7,valve8]

    print ("$", minPrice, "m^3 / hour of flow")
    print ("Optimal type and diameter for each pipe, valve, pump, and bend:")
    for i in minset:
        print (i)
    
    return initPrice, dailyPrice

