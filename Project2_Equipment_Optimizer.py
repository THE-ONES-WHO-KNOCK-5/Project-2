# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:18:21 2023

@author: graha
"""

<<<<<<< Updated upstream
import Project2_Density_Calculator as dc

def equipmentCalc(slurryMass):
    sugar = 0.2 * slurryMass
    water = 0.6 * slurryMass
    fiber = 0.2 * slurryMass
    #Proportions of the mass inputs
=======
p1 = 1180.2
p2= 1058.1379688528186
p3= 995.9417873735995
p4= 812.6625000000003
p5= 795.675767918089
# slurry density between systems kg/m^3

Q5 = 100000 * 0.00378541 / 24 #(24 * 60 * 60)
Q4 = (Q5*p4)/p5
Q3 = (Q4*p3)/p4
Q2 = (Q3*p2)/p3
Q1 = (Q2*p1)/p2


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
>>>>>>> Stashed changes

    fermValues = [0.5,0.75,0.9,0.95]
    fermPrices = [320,380,460,1100]
    filtValues = [0.5,0.75,0.9,0.98]
    filtPrices = [200,240,280,480]
    distValues = [0.81,0.9,0.915,0.98]
    distPrices = [390,460,560,1370]
    dehyValues = [0.5,0.75,0.9,0.98]
    dehyPrices = [200,240,280,480]
    #Equipment coefficients and associated prices

<<<<<<< Updated upstream
    qualityDescriptions = ['Scrap', 'Average', 'Premium', 'World-Class']
    #Equipment quality options
=======
combos = []
prices = []
initialPrices = []
dailyPrices = []
#Empty lists
>>>>>>> Stashed changes

    combos = []
    prices = []
    #Empty lists
    costRate = 0

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

<<<<<<< Updated upstream
                    S2 = (S*E*((1.0/distiller)-1.0))/(water+S+F)
                    W = (water*E*((1.0/distiller)-1.0))/(water+S+F)
                    F2 = (F*E*((1.0/distiller)-1.0))/(water+S+F)
=======
                W2 = W*(1.0-dehydrator)
                
                #Amounts of each substance left at the end
                
                purity = (E/(E+S2+F2+W2))*100.0
                #Final purity
                
                if purity >= 98:
                    combo = str(fermValues.index(fermenter)) + str(filtValues.index(Filter)) + str(distValues.index(distiller)) + str(dehyValues.index(dehydrator))
                    initialPrice = float(fermPrices[fermValues.index(fermenter)]*Q1+ filtPrices[filtValues.index(Filter)]*Q2+ distPrices[distValues.index(distiller)]*Q3+ dehyPrices[dehyValues.index(dehydrator)]*Q4)
                    dailyPrice = float(fermEnergy[fermValues.index(fermenter)]*0.1202 + filtEnergy[filtValues.index(Filter)]*0.1202 + distEnergy[distValues.index(distiller)]*0.1202 + dehyEnergy[dehyValues.index(dehydrator)]*0.1202)
                    yearCost = initialPrice + dailyPrice*365
                    combos.append(combo)
                    prices.append(yearCost)
                    initialPrices.append(initialPrice)
                    dailyPrices.append(dailyPrice)
                    #Adds the combination of equipments and the price to a list if the purity is at least 99%
>>>>>>> Stashed changes

                    W2 = W*(1.0-dehydrator)
                    
                    #Amounts of each substance left at the end
                    
                    purity = (E/(E+S2+F2+W2))*100.0
                    #Final purity
                    #print(purity)
                    
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

<<<<<<< Updated upstream
    x = int(combos[prices.index(min(prices))][0])
    x2 = int(combos[prices.index(min(prices))][1])
    x3 = int(combos[prices.index(min(prices))][2])
    x4 = int(combos[prices.index(min(prices))][3])
    #Quality finders
=======
print (qualityDescriptions[x], "Fermenter")
print (qualityDescriptions[x2], "Filter")
print (qualityDescriptions[x3], "Distiller")
print (qualityDescriptions[x4], "Dehydrator")
print ("Initial cost is $", initialPrices[prices.index(min(prices))])
print ("Daily cost is $", dailyPrices[prices.index(min(prices))], "per day" )
#Final printing
>>>>>>> Stashed changes

    print (qualityDescriptions[x], "Fermenter")
    print (qualityDescriptions[x2], "Filter")
    print (qualityDescriptions[x3], "Distiller")
    print (qualityDescriptions[x4], "Dehydrator")
    print ("$", min(prices), "m^3 / hour of flow")
    #Final printing

    print ("The final mass of ethanol is: ", E, " kg")
    print ("The final volume of ethanol is: ", E/ dc.pEthanol * 264.172, " gallons")

    print ("The final mass of sugar is: ", S2, " kg")
    print ("The final mass of water is: ", W2, " kg")
    print ("The final mass of fiber is: ", F2, " kg")
    print ("The final purity of the ethanol is: %", purity)
    #Scrap code

    return min(prices), costRate