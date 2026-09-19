# Task: Operator drill: ask for two floats a and b. Print all seven math results (+, -, *, /, //, %, **), labeled, one per line — e.g. a // b = 3.0.

#Collects user input
num_1 = float(input("Num 1:"))
num_2 = float(input("Num 2:"))

# Performs differnet operation
add = num_1 + num_2
sub = num_1 - num_2
muptiplication = num_1 * num_2
division =  num_1 / num_2
floor_division = num_1 // num_2
mod = num_1 % num_2
exponential = num_1 ** num_2

print("\n")
print(f"addition: {add}")
print(f"subtraction: {sub}")
print(f"multiplication: {muptiplication}")
print(f"division: {division}")
print(f"floor_division: {floor_division}")
print(f"modulus: {mod}")
print(f"exponential: {exponential}")