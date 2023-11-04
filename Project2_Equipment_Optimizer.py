# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:18:21 2023

@author: graha
"""


import Project2_Density_Calculator as dc

def equipmentCalc(finalFlowrate):
    pSugar = 1599
    pEthanol = 789
    pFiber = 1311
    pWater = 997
    
    Q5 = finalFlowrate * 0.00378541 / 24 #(24 * 60 * 60)
    # flow rate in a day (m^3/s)
    
    sugar = 0.2
    water = 0.6
    fiber = 0.2
    #Proportions of the mass inputs
    
    fermValues = [0.5,0.75,0.9,0.95]
    fermPrices = [320,380,460,1100]
    fermEnergy = [46600,47200,47500,48000]
    
    filtValues = [0.5,0.75,0.9,0.98]
    filtPrices = [200,240,280,480]
    filtEnergy = [48800,49536,50350,51000]
    
    distValues = [0.81,0.9,0.915,0.98]
    distPrices = [390,460,560,1370]
    distEnergy = [47004,47812,48200,49500]
    
    dehyValues = [0.5,0.75,0.9,0.98]
    dehyPrices = [200,240,280,480]
    dehyEnergy = [48800,49536,50350,51000]
    #Equipment coefficients and associated prices
    
    qualityDescriptions = ['Scrap', 'Average', 'Premium', 'World-Class']
    #Equipment quality options
    
    combos = []
    prices = []
    initialPrices = []
    dailyPrices = []
    purities = []
    ethanolMin = []
    sugarMin = []
    waterMin = []
    fiberMin = []
    p2Min = []
    p3Min = []
    p4Min = []
    p5Min = []
    #Empty lists
    costRate = 0

    for fermenter in fermValues:
        for Filter in filtValues:
            for distiller in distValues:
                for dehydrator in dehyValues:
        
                    E = sugar*0.51*fermenter
                    S = sugar*(1.0-fermenter)
                    CO2 = sugar*0.49*fermenter

                    F = fiber*(1.0-Filter)
                    Fwaste = fiber*Filter

                    S2 = (S*E*((1.0/distiller)-1.0))/(water+S+F)
                    W = (water*E*((1.0/distiller)-1.0))/(water+S+F)
                    F2 = (F*E*((1.0/distiller)-1.0))/(water+S+F)

                    W2 = W*(1.0-dehydrator)

                    purity = (E/(E+S2+F2+W2))*100.0
                    #Final purity
                    
                    p1 = sugar*pSugar + water*pWater + fiber*pFiber
                    p2 = (E*pEthanol + S*pSugar + water*pWater + fiber*pFiber)/(1- CO2)
                    p3 = (E*pEthanol + S*pSugar + water*pWater + F*pFiber)/(1- CO2 - Fwaste)
                    p4 = (E*pEthanol + S2*pSugar + W*pWater + F2*pFiber)/(1- CO2 - Fwaste-(S-S2)-(F-F2)-(water-W))
                    p5 = (E*pEthanol + S2*pSugar + W2*pWater + F2*pFiber)/(1- CO2 - Fwaste-(S-S2)-(F-F2)-(water-W)-W*dehydrator)
                    
                    Q4 = (Q5*p4)/p5
                    Q3 = (Q4*p3)/p4
                    Q2 = (Q3*p2)/p3
                    Q1 = (Q2*p1)/p2
                    
                    if purity >= 98:
                        combo = str(fermValues.index(fermenter)) + str(filtValues.index(Filter)) + str(distValues.index(distiller)) + str(dehyValues.index(dehydrator))
                        initialPrice = float(fermPrices[fermValues.index(fermenter)]*Q1+ filtPrices[filtValues.index(Filter)]*Q2+ distPrices[distValues.index(distiller)]*Q3+ dehyPrices[dehyValues.index(dehydrator)]*Q4)
                        dailyPrice = float(fermEnergy[fermValues.index(fermenter)]*0.1202 + filtEnergy[filtValues.index(Filter)]*0.1202 + distEnergy[distValues.index(distiller)]*0.1202 + dehyEnergy[dehyValues.index(dehydrator)]*0.1202)
                        yearCost = initialPrice + dailyPrice*365
                        combos.append(combo)
                        prices.append(yearCost)
                        purities.append(purity)
                        ethanolMin.append(E)
                        sugarMin.append(S2)
                        waterMin.append(W2)
                        fiberMin.append(F2)
                        p2Min.append(p2)
                        p3Min.append(p3)
                        p4Min.append(p4)
                        p5Min.append(p5)
                        initialPrices.append(initialPrice)
                        dailyPrices.append(dailyPrice)
                        #Adds the combination of equipments and the price to a list if the purity is at least 99%

    #print (combos)
    #print (prices)
    #print (min(prices))
    #print (combos[prices.index(min(prices))])
    #Scrap code

    x = int(combos[prices.index(min(prices))][0])
    x2 = int(combos[prices.index(min(prices))][1])
    x3 = int(combos[prices.index(min(prices))][2])
    x4 = int(combos[prices.index(min(prices))][3])
    #Quality finders
    
    minInitial = initialPrices[prices.index(min(prices))]
    minDaily = dailyPrices[prices.index(min(prices))]
    
    print (qualityDescriptions[x], "Fermenter")
    print (qualityDescriptions[x2], "Filter")
    print (qualityDescriptions[x3], "Distiller")
    print (qualityDescriptions[x4], "Dehydrator")
    print ("Initial cost is $", minInitial)
    print ("Daily cost is $", minDaily, "per day" )
    #Final printing
    
    p2 = p2Min[prices.index(min(prices))]
    p3 = p3Min[prices.index(min(prices))]
    p4 = p4Min[prices.index(min(prices))]
    p5 = p5Min[prices.index(min(prices))]
    
    print ("p1 =", p1)
    print ("p2=", p2)
    print ("p3=", p3)
    print ("p4=", p4)
    print ("p5=", p5)
    
    print ("The final mass of ethanol is: ", ethanolMin[prices.index(min(prices))], " kg")
    print ("The final volume of ethanol is: ", E/ dc.pEthanol * 264.172, " gallons")

    print ("The final mass of sugar is: ", sugarMin[prices.index(min(prices))], " kg")
    print ("The final mass of water is: ", waterMin[prices.index(min(prices))], " kg")
    print ("The final mass of fiber is: ", fiberMin[prices.index(min(prices))], " kg")
    print ("The final purity of the ethanol is: %", purities[prices.index(min(prices))])
    #Scrap code
    
    densities = [p1, p2, p3, p4, p5]
    
    return minInitial, minDaily, costRate, densities