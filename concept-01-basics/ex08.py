# Task: econds converter: ask for a whole number of seconds. Convert it using only // and % and print e.g. 98765 seconds = 1 days, 3 hours, 26 minutes, 5 
# Collect Time in seconds
time = int(input("Enter the time in seconds. Note it must be a whole number: "))

# Perform arithmetic operation
seconds = time % 60
minutes = (time % (24 * 60 * 60) % 3600) // 60
hours = ((time % (24 * 60 * 60)) // 3600) 
days = time // (24 * 60 * 60)

# Display the result
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

