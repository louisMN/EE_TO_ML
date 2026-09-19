# Task: Ask for three resistor values (ohms). Print the series total (R1+R2+R3) and the parallel total (1 / (1/R1 + 1/R2 + 1/R3)), each to 2 decimals.

#Asks user for input
r1 = float(input("Resistor 1: "))
r2 = float(input("Resistor 2: "))
r3 = float(input("Resistor 3: "))

# Performs arithmetic operation
series = r1 + r2 + r3
parallel = 1/ (1/r1 + 1/r2 + 1/r3)

print("\n")
# Displays the output
print(f"Total Equivalent Series Resistance: {series:.2f} ohms")
print(f"Total Equivalent Parallel Resistance: {parallel:.2f} ohms \n")