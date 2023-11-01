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

    def fermentLiquid(self, state: LiquidState):
        return LiquidState(.51 * state.getSugar() * self.efficiency + state.getEthanol(),state.getSugar() * (1 - self.efficiency),state.getWater(),state.getFiber(),state.getCO2 + 0.49 * state.getSugar() * self.efficiency, state.getRate())
