# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:18:21 2023

@author: graha
"""

import Project2_Density_Calculator as dc

def equipmentCalc(slurryMass):
    sugar = 0.2 * slurryMass
    water = 0.6 * slurryMass
    fiber = 0.2 * slurryMass
    #Proportions of the mass inputs

    fermValues = [0.5,0.75,0.9,0.95]
    fermPrices = [320,380,460,1100]
    filtValues = [0.5,0.75,0.9,0.98]
    filtPrices = [200,240,280,480]
    distValues = [0.81,0.9,0.915,0.98]
    distPrices = [390,460,560,1370]
    dehyValues = [0.5,0.75,0.9,0.98]
    dehyPrices = [200,240,280,480]
    #Equipment coefficients and associated prices

    qualityDescriptions = ['Scrap', 'Average', 'Premium', 'World-Class']
    #Equipment quality options

    combos = []
    prices = []
    #Empty lists
    costRate = None

    #fermenter = float(input("Input Fermenter value: "))
    #Filter = float(input("Input Filter value: "))
    #distiller = float(input("Input Distiller value: "))
    #dehydrator = float(input("Input Dehydrator value: "))
    #Scrap code from when it took inputs

    for fermenter in fermValues:
        for Filter in filtValues:
            for distiller in distValues:
                for dehydrator in dehyValues:
        
                    E = sugar*0.51*fermenter
                    S = sugar*(1.0-fermenter)

                    F = fiber*(1.0-Filter)

                    S2 = (S*E*((1.0/distiller)-1.0))/(water+S+F)
                    W = (water*E*((1.0/distiller)-1.0))/(water+S+F)
                    F2 = (F*E*((1.0/distiller)-1.0))/(water+S+F)

                    W2 = W*(1.0-dehydrator)
                    
                    #Amounts of each substance left at the end
                    
                    purity = (E/(E+S2+F2+W2))*100.0
                    #Final purity
                    print(purity)
                    
                    if purity >= 98:
                        combo = str(fermValues.index(fermenter)) + str(filtValues.index(Filter)) + str(distValues.index(distiller)) + str(dehyValues.index(dehydrator))
                        price = str(fermPrices[fermValues.index(fermenter)] + filtPrices[filtValues.index(Filter)] + distPrices[distValues.index(distiller)] + dehyPrices[dehyValues.index(dehydrator)])
                        combos.append(combo)
                        prices.append(price)
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

    print (qualityDescriptions[x], "Fermenter")
    print (qualityDescriptions[x2], "Filter")
    print (qualityDescriptions[x3], "Distiller")
    print (qualityDescriptions[x4], "Dehydrator")
    print ("$", min(prices), "m^3 / hour of flow" )
    #Final printing

    print ("The final mass of ethanol is: ", E, " kg")
    print ("The final volume of ethanol is: ", E/ dc.pEthanol * 264.172, " gallons")

    print ("The final mass of sugar is: ", S2, " kg")
    print ("The final mass of water is: ", W2, " kg")
    print ("The final mass of fiber is: ", F2, " kg")
    print ("The final purity of the ethanol is: %", purity)
    #Scrap code

    return min(prices), costRate