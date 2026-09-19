# Task: Voltage divider: ask for Vin, R1, R2. Print Vout = Vin × R2 / (R1 + R2) and the circuit current I = Vin / (R1 + R2) in milliamperes, both to 2 decimals.
# Collects values for Input Voltage(vin), Resistor 1(r1) and Resistor 2(r2) 
vin = float(input("Vin: ")) 
r1 = float(input("Resistor 1: "))
r2 = float(input("Resistor 2: "))

# Performs arithemetic operations to get vout and current
vout = vin * (r2 / (r1 + r2))
current = vin / (r1 + r2)

# Displays the output
print("\n")
print(f"current: {current:.2f} mA")
print(f"Output Voltage (Vout): {vout:.2f} volts \n")