# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:33:50 2023

@author: graha
"""

import math as m
def energyCalc(d1, d2, d3, d4, d5, f1, f2, f3, f4, f5, L, K1, K2, K3, K4, K5, K6, K7, K8, pump):
    # slurry density between systems kg/m^3
    p1 = 1180.2
    p2= 1058.1379688528186
    p3= 995.9417873735995
    p4= 812.6625000000003
    p5= 795.675767918089
    
    # flow rate in a day (m^3/s)
    Q5 = 100000 * 0.00378541 / (24 * 60 * 60)
    Q4 = (Q5*p4)/p5
    Q3 = (Q4*p3)/p4
    Q2 = (Q3*p2)/p3
    Q1 = (Q2*p1)/p2
    
    # time between rate change (one second)
    t = 1
    
    # calculates masses between systems (kg)
    M1 = p1 * Q1 * t
    M2 = p2 * Q2 * t
    M3 = p3 * Q3 * t
    M4 = p4 * Q4 * t
    M5 = p5 * Q5 * t
    
    # pipe distances (m)
    L1 = 1 + 0.762
    L2 = 0.762 + 1.524
    L3 = 3.048
    L4 = 3.048
    L5 = 1.324 + 3 + 10.716
    
    # pipe diameter (m)
    #d1 = float(input("Input Initial pipe diameter: "))
    #d2 = float(input("Input 2nd pipe diameter: "))
    #d3 = float(input("Input 3rd pipe diameter: "))
    #d4 = float(input("Input 4th pipe diameter: "))
    #d5 = float(input("Input final pipe diameter: "))
    
    # pipe friction ()
    #f1 = float(input("Input Initial pipe friction: "))
    #f2 = float(input("Input 2nd pipe friction: "))
    #f3 = float(input("Input 3rd pipe friction: "))
    #f4 = float(input("Input 4th pipe friction: "))
    #f5 = float(input("Input final pipe friction: "))
    
    # pipe loss coeffienient for bend (mu)
    #L = float(input("Input pipe loss coefficient: "))
    
    # set valves coeffienct
    #K1 = float(input("Input Flow coefficient of valve 1: "))
    #K2 = float(input("Input Flow coefficient of valve 2: "))
    #K3 = float(input("Input Flow coefficient of valve 3: "))
    #K4 = float(input("Input Flow coefficient of valve 4: "))
    #K5 = float(input("Input Flow coefficient of valve 5: "))
    #K6 = float(input("Input Flow coefficient of valve 6: "))
    #K7 = float(input("Input Flow coefficient of valve 7: "))
    #K8 = float(input("Input Flow coefficient of valve 8: "))
    
    # pump effieciency
    #pump = float(input("Input pump efficiency: "))
    
    # calculate pipe cross section
    A1 = m.pi * (d1/2)**2
    A2 = m.pi * (d2/2)**2
    A3 = m.pi * (d3/2)**2
    A4 = m.pi * (d4/2)**2
    A5 = m.pi * (d5/2)**2
    
    Eout = 0.5 * p5 * (Q5/A5)**2
    
    # calculates pipe friction
    Hdw1 = M1 * ((f1*(Q1**2)*L1)/(m.pi**2 * d1**5))
    Hdw2 = M2 * ((f2*(Q2**2)*L2)/(m.pi**2 * d2**5))
    Hdw3 = M3 * ((f3*(Q3**2)*L3)/(m.pi**2 * d3**5))
    Hdw4 = M4 * ((f4*(Q4**2)*L4)/(m.pi**2 * d4**5))
    Hdw5 = M5 * ((f5*(Q5**2)*L5)/(m.pi**2 * d5**5))
    
    Hdwtotal = Hdw1 + Hdw2 + Hdw3 + Hdw4 + Hdw5
    
    # calculates bends
    Hbend = M5 * L * (((Q5/(m.pi * (d5/2))**2))/2)
    
    # calculates valves
    Hv1 = M1 * K1 * (((Q1/(m.pi * (d1/2))**2))/2)
    Hv2 = M2 * K1 * (((Q2/(m.pi * (d2/2))**2))/2)
    Hv3 = M2 * K1 * (((Q2/(m.pi * (d2/2))**2))/2)
    Hv4 = M3 * K1 * (((Q3/(m.pi * (d3/2))**2))/2)
    Hv5 = M3 * K1 * (((Q3/(m.pi * (d3/2))**2))/2)
    Hv6 = M4 * K1 * (((Q4/(m.pi * (d4/2))**2))/2)
    Hv7 = M4 * K1 * (((Q4/(m.pi * (d4/2))**2))/2)
    Hv8 = M5 * K1 * (((Q5/(m.pi * (d5/2))**2))/2)
    
    Hvtotal = Hv1 + Hv2 + Hv3 + Hv4 + Hv5 + Hv6 + Hv7 + Hv8
    
    # solves for total energy
    KE = -(Eout - Hdwtotal - Hbend - Hvtotal)
    Ein = KE/pump
    
    print ("Input energy required is:", Ein , "kJ")
    
    return KE, Ein

"""
d1 = float(input("Input Initial pipe diameter: "))
d2 = float(input("Input 2nd pipe diameter: "))
d3 = float(input("Input 3rd pipe diameter: "))
d4 = float(input("Input 4th pipe diameter: "))
d5 = float(input("Input final pipe diameter: "))

# pipe friction ()
f1 = float(input("Input Initial pipe friction: "))
f2 = float(input("Input 2nd pipe friction: "))
f3 = float(input("Input 3rd pipe friction: "))
f4 = float(input("Input 4th pipe friction: "))
f5 = float(input("Input final pipe friction: "))

# pipe loss coeffienient (mu)
L = float(input("Input pipe loss coefficient: "))

# set valves coeffienct
K1 = float(input("Input Flow coefficient of valve 1: "))
K2 = float(input("Input Flow coefficient of valve 2: "))
K3 = float(input("Input Flow coefficient of valve 3: "))
K4 = float(input("Input Flow coefficient of valve 4: "))
K5 = float(input("Input Flow coefficient of valve 5: "))
K6 = float(input("Input Flow coefficient of valve 6: "))
K7 = float(input("Input Flow coefficient of valve 7: "))
K8 = float(input("Input Flow coefficient of valve 8: "))

# pump effieciency
pump = float(input("Input pump efficiency: "))

energyCalc(d1, d2, d3, d4, d5, f1, f2, f3, f4, f5, L, K1, K2, K3, K4, K5, K6, K7, K8, pump)
"""