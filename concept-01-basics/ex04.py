# Task: Ohm's Law: ask for current I (amps) and resistance R (ohms) as numbers. Print the voltage V = I × R as e.g. V = 12.50 V (2 decimals).
print("This program calculates the volatge using ohms law, Input both current and resistance below \n") # Message to user

# Collects input values for current and resistance
current = float(input("Current: "))
resistance = float(input("Resistance: "))

# Perfroms the arithmetic proceedure to get the value of voltage and prints out the value
voltage = current * resistance
print(f"Voltage: {voltage:.2f} volts \n")


