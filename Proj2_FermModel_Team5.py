import Project2_Equipment_Optimizer as eo

print("\n\n\n\n\n\n\n\n\n\n\n")
print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Team 5: The Ones Who Knock -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
print("\nWelcome to Team 5 Ethanol Simulator!")
print("\nThroughout this simulation, we will calculate the optimal combonation of equipments and prices for the full system anc calculate cost and production.")
print("\nFirst, we will calculate the optimal combonation of equipments and prices for the 4 major systems.")
initMass = 3082239.92728
print("\nStarting with inital slurry mass (kg),", initMass,"kg")
input("\nPress Enter to continue...")


eo.equipmentCalc(initMass)