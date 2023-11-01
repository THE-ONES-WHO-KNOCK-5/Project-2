# -*- coding: utf-8 -*-
class LiquidState:
    ethanol = None
    sugar = None
    water = None
    fiber = None
    rate = None
    
    def __init__(self, rate, ethanol, sugar, water, fiber):
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

    def getDensity(self):
        totalMass = self.ethanol + self.sugar + self.water + self.fiber
        eMass = self.ethanol / totalMass * 789
        sMass = self.sugar / totalMass * 1599
        wMass = self.water / totalMass * 997
        fMass = self.fiber / totalMass * 1311
        return eMass + sMass + wMass + fMass
    
    