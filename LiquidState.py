# -*- coding: utf-8 -*-
class LiquidState:
    ethanol = None
    sugar = None
    water = None
    fiber = None
    CO2 = None
    rate = None
    
    def __init__(self, ethanol, sugar, water, fiber, CO2, rate):
        self.ethanol = ethanol
        self.sugar = sugar
        self.water = water
        self.fiber = fiber
        self.CO2 = CO2
        self.rate = rate
        
    def getEthanol(self):
        return self.ethanol

    def getSugar(self):
        return self.sugar

    def getWater(self):
        return self.water

    def getFiber(self):
        return self.fiber
    def getCO2(self):
        return self.CO2

    def getRate(self):
        return self.rate

    
    
    