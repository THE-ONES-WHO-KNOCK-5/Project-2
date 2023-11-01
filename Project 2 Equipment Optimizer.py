# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:18:21 2023

@author: graha
"""

sugar = 0.2
water = 0.6
fiber = 0.2
#Proportions of the mass inputs

fermValues = [0.5,0.75,0.9,0.95]
fermPrices = [320,380,460,1100]
filtValues = [0.5,0.75,0.9,0.98]
filtPrices = [200,240,280,480]
distValues = [0.81,0.9,0.915,0.95]
distPrices = [320,380,460,1100]
dehyValues = [0.5,0.75,0.9,0.98]
dehyPrices = [200,240,280,480]
#Equipment coefficients and associated prices

qualityDescriptions = ['Scrap', 'Average', 'Premium', 'World-Class']
#Equipment quality options

combos = []
prices = []
#Empty lists

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
                S = sugar*0.49*(1.0-fermenter)

                F = fiber*(1.0-Filter)

                S2 = (S*E*((1.0/distiller)-1.0))/(water+S+F)
                W = (water*E*((1.0/distiller)-1.0))/(water+S+F)
                F2 = (F*E*((1.0/distiller)-1.0))/(water+S+F)

                W2 = W*(1.0-dehydrator)
                
                #Amounts of each substance left at the end
                
                purity = (E/(E+S2+F2+W2))*100.0
                #Final purity
                
                if purity >= 99:
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
print (qualityDescriptions[x2], "Fermenter")
print (qualityDescriptions[x3], "Fermenter")
print (qualityDescriptions[x4], "Fermenter")
print ("$", min(prices), "m^3 / hour of flow" )
#Final printing

#print ("The final mass of ethanol is: ", E)
#print ("The final mass of sugar is: ", S2)
#print ("The final mass of water is: ", W2)
#print ("The final mass of fiber is: ", F2)
#print ("The final purity of the ethanol is: %", purity)
#Scrap code