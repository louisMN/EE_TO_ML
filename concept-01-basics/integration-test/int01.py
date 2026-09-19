""" Task: A machine requires an operating voltage strictly greater than 4.8V.

    Ask the user for three separate voltage readings (floats).
    Calculate the average of the three.
    Print the average to 2 decimals (e.g., Average: 5.05 V).
    Print True if the average is strictly greater than 4.8, and False otherwise. (No if!). """
threshold_voltage = 4.8

print("Input the three Voltage readings \n")

reading_1 = float(input("Reading 1: "))
reading_2 = float(input("Reading 2: "))
reading_3 = float(input("Reading 3: "))

average = (reading_1 + reading_2 + reading_3) / 3
print(f"Average: {average:.2f} V")
print(average > threshold_voltage)