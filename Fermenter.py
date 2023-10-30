# -*- coding: utf-8 -*-
import LiquidState


class Fermenter:
    powerUsage = None
    efficiency = None
    costPerHour = None
    def __init__(self, powerUsage, efficiency, costPerHour):
        self.powerUsage = powerUsage
        self.efficiency = efficiency
        self.costPerHour = costPerHour
                
    def getCost(self, state: LiquidState):
        return state.getRate() * self.costPerHour
                
