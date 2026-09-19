# Task: Battery runtime estimator: ask for battery capacity (mAh) and device draw (mA). Print runtime formatted as 37h 30m (use // and %). Then print True if runtime ≥ 24 hours else False — without using if (a comparison like total_hours >= 24 already produces a bool).

battery_capacity = int(input("Battery capacity (mAh): "))
device_draw = int(input("Device draw: "))

hours = battery_capacity // device_draw
minutes = (((battery_capacity % device_draw) * 60)// device_draw)

print(f"Run time: {hours}h {minutes}m ")

print(hours>= 24)