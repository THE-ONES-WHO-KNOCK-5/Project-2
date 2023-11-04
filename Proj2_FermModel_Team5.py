import Project2_Equipment_Optimizer as eo
import Project2_Simple_Pipe_Optimizer as spo

print("\n\n\n\n\n\n\n\n\n\n\n")
print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Team 5: The Ones Who Knock -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
print("\nWelcome to Team 5 Ethanol Simulator!")
print("\nThroughout this simulation, we will calculate the optimal combonation of equipments and prices for the full system anc calculate cost and production.")
print("\nFirst, we will calculate the optimal combonation of equipments and prices for the 4 major systems.")
initMass = 3082239.92728
print("\nStarting with inital slurry mass (kg),", initMass,"kg")
input("\nPress Enter to continue...")

eInit, eDaily = eo.equipmentCalc(initMass)

input("\nPress Enter to continue...")
print("\nNext, we will calculate the optimal combonation for the pipes, valves, pump, and bends in the system.")
print("\nWe will assume that the pipes, valves, pump, and bends have the same diameter. and each part will have the same type.")

input("\nPress Enter to continue...")

sInit, sDaily = spo.optimizePipes()

input("\nPress Enter to continue...")
print("\nFinally, we will calculate the cost of the pipes for waste resources.")

input("\nPress Enter to continue...")

wInit, wDaily = 0, 0

input("\nPress Enter to continue...")

print("Now we can solve for total cost and production of the system.")

input("\nPress Enter to continue...")

totalInit = float(eInit) + float(sInit) + float(wInit)
totalDaily = float(eDaily) + float(sDaily) + float(wDaily)

print("\n$" + str(totalInit) + " Inital Upfront.")
print("\n$" + str(totalDaily) + " Daily.")
print("\n$" + str(totalInit + totalDaily * 365) + " estimated for a year.")