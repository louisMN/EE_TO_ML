solar_panel_capacity = int(input("Solar Panel Capacity (Wattage): "))
hours_of_peak_sunlight = float(input("Hours of peak sunlight: ")) # Fixed to float!
battery_capacity = int(input("Battery capacity (Wh): "))

total_energy = solar_panel_capacity * hours_of_peak_sunlight


full_charges = int(total_energy) // battery_capacity
leftover = int(total_energy) % battery_capacity


print(f"Full Charges: {full_charges}, Leftover Wh: {leftover}")