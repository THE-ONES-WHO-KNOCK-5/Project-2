# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:13:06 2023

@author: aust1
"""
from LiquidState import LiquidState
from Fermenter import Fermenter

scrap = Fermenter(46600, 0.5, 320)
slurry = LiquidState(0,0,0,0,50)

print(scrap.getCost(slurry))