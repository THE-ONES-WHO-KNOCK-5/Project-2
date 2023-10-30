# -*- coding: utf-8 -*-
class LiquidState:
    ethanol = None
    sugar = None
    water = None
    fiber = None
    rate = None
    
    def __init__(self, ethanol, sugar, water, fiber, rate):
        self.ethanol = ethanol
        self.sugar = sugar
        self.water = water
        self.fiber = fiber
        self.rate = rate
        
    def getEthanol(self):
        return self.ethanol

    def getSugar(self):
        return self.sugar

    def getWater(self):
        return self.water

    def getFiber(self):
        return self.fiber

    def getRate(self):
        return self.rate

    
    
    