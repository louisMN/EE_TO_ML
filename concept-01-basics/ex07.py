# Task: Energy bill: ask for an appliance's power (watts), hours used per day, and tariff (currency per kWh). Print the daily cost and 30-day cost, 2 decimals. (Reminder: kWh = watts × hours ÷ 1000.)

# Collects the tariff, appliance, hours run and power rating information from user
tariff = float(input("Tariff: ")) 
appliance = input("What appliance would you like to check: ")
rating = float(input("What is the power rating(watt) of the appliance:"))
hours = int(input(f"How many hours does the {appliance.title()} operate: "))

# Performs arithemetic calculation for the daily cost and the cost after 30 days
daily_cost = (rating/1000) * hours * tariff
thirty_day_cost = daily_cost * 30

# Displays the result
print(f"The cost of running the {appliance.title()} is ${daily_cost:.2f} daily and ${thirty_day_cost:.2f} after thirty days")