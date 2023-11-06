import Project2_Equipment_Optimizer as eo
import Project2_Simple_Pipe_Optimizer as spo
import Project2_Waste_Pipe_Optimizer as wpo

print("\n\n\n\n\n\n\n\n\n\n\n")
print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Team 5: The Ones Who Knock -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
print("\nWelcome to Team 5 Ethanol Simulator!")
print("\nThroughout this simulation, we will calculate the optimal combonation of equipments and prices for the full system anc calculate cost and production.")
print("\nFirst, we will calculate the optimal combonation of equipments and prices for the 4 major systems.")

finalVolume = float(input("\nEnter final amount of Ethanol (Gallons): "))

print("\nStarting with final Ethanol Volume (Gallons),", finalVolume,"Gallons.")
input("\nPress Enter to continue...")

eInit, eDaily, densities, flowrates = eo.equipmentCalc(finalVolume)

input("\nPress Enter to continue...")
print("\nNext, we will calculate the optimal combonation for the pipes, valves, pump, and bends in the system.")
print("\nWe will assume that the pipes, valves, pump, and bends have the same diameter. and each part will have the same type.")

input("\nPress Enter to continue...")

sInit, sDaily = spo.optimizePipes(densities, flowrates)

input("\nPress Enter to continue...")
print("\nFinally, we will calculate the cost of the pipes for waste resources.")

input("\nPress Enter to continue...")

wInit = wpo.wasteCalc(densities, flowrates)

input("\nPress Enter to continue...")

print("\nNow we can solve for total cost and production of the system.")

input("\nPress Enter to continue...")

totalInit = float(eInit) + float(sInit) + float(wInit)
totalDaily = float(eDaily) + float(sDaily)

print("\n$%.2f Inital Upfront." % totalInit)
print("\n$%.2f Daily." % totalDaily)
print("\n$%.2f estimated for a year plus upfront." % (totalInit + totalDaily * 365))
print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Team 5: The Ones Who Knock -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
