import math as m
import itertools as it
import Project2_Input_Energy_Calculator as ec
import time
    
# pipe distances (m)
L1 = 1 + 0.762
L2 = 0.762 + 1.524
L3 = 3.048
L4 = 3.048
L5 = 1.324 + 3 + 10.716


def energySystem(d1, d2, d3, d4, f1, f2, f3, f4, densities, flowrates):

    # slurry density exiting systems kg/m^3
    p1 = 1.87
    p2 = 1311
    p3 = distDensity
    p4 = 997

    # flow rate in a day (m^3/s)
    Q1 = flowrates[0]
    Q2 = flowrates[1]
    Q3 = flowrates[2]
    Q4 = flowrates[3]

    t = (24 * 60 * 60)

    # calculates masses between systems (kg)
    M1 = p1 * Q1 * t
    M2 = p2 * Q2 * t
    M3 = p3 * Q3 * t
    M4 = p4 * Q4 * t

    A1 = m.pi * (d1/2)**2
    A2 = m.pi * (d2/2)**2
    A3 = m.pi * (d3/2)**2
    A4 = m.pi * (d4/2)**2
    
    E1 = 0.5 * p1 * (Q1/A1)**2
    E2 = 0.5 * p2 * (Q2/A2)**2
    E3 = 0.5 * p3 * (Q3/A3)**2
    E4 = 0.5 * p4 * (Q4/A4)**2
    
    Etotal = E1 + E2 + E3 + E4

    Hdw1 = M1 * ((f1*(Q1**2)*L1)/(m.pi**2 * d1**5))
    Hdw2 = M2 * ((f2*(Q2**2)*L2)/(m.pi**2 * d2**5))
    Hdw3 = M3 * ((f3*(Q3**2)*L3)/(m.pi**2 * d3**5))
    Hdw4 = M4 * ((f4*(Q4**2)*L4)/(m.pi**2 * d4**5))

    Hdwtotal = Hdw1 + Hdw2 + Hdw3 + Hdw4

    return Etotal - Hdwtotal






# define all possible diameters and relation of diameters to 2D Array Position
diameters = [0.1,0.11,0.12,0.13,0.14,0.15]
gasVal = [1,1.25, 1.5]
gasCost = [228, 414, 700]

diameterDict = {0.1:0,0.11:1,0.12:2,0.13:3,0.14:4,0.15:5}

def optimizeWaste(densities, flowrates, distDensity):
    minPrice = 99999999999999999999999999999999999999999999999999
    maxEnergy = 0
    minset = []


    # building all gas combos
    totalGas = []
    for diameter, costPerMeter in zip(gasVal, gasCost):
        totalGas.append({"part": "Gas", "diameter": diameter, "fricFactor": 0.002, "costRate": costPerMeter})

    # building all pipe combos
    pipeLines = ["Salvage", "Questionable", "Better", "Nice", "Outstanding", "Glorious"]
    totalPipes = []

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
                
        totalPipes.append({"part": "Pipe", "name": pipeType, "diameter": diameter, "fricFactor": fricFactor, "costRate": costPerMeter})


    for pipe1, pipe2, pipe3, pipe4 in it.product(totalGas, totalPipes, totalPipes, totalPipes):

        # solves for energies and prices
        KE = energySystem(pipe1["diameter"], pipe2["diameter"], pipe3["diameter"], pipe4["diameter"], pipe1["fricFactor"], pipe2["fricFactor"], pipe3["fricFactor"], pipe4["fricFactor"], densities, flowrates, distDensity)
        initPrice = pipe1["costRate"]*ec.L1 + pipe2["costRate"]*ec.L2 + pipe3["costRate"]*ec.L3 + pipe4["costRate"]*ec.L4


        #print([pipe1, pump, valve1], "ratio: ",KE , initPrice, dailyPrice)

        # test cheapest cost as long as there is enough energy for waste to leave the pipe
        if initPrice < minPrice or KE > 0:
            minPrice = initPrice
            KE = maxEnergy
            minset = [pipe1,pipe2,pipe3,pipe4,]

    print ("$", minPrice, " Initical price.")
    print ("Optimal type and diameter for each pipe:")
    for i in minset:
        print (i)
    
    return initPrice

