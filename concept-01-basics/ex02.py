# Task: Create 4 variables — one int, one float, one str, one bool. Print each variable's value and its type using type() (e.g. 12 <class 'int'>).
# Solution

voltage = 2 #Initialize votltage
current = 1.5 #Initialize current
name = "Generator" #Initialize name of equipment
state = True #Initialize state of equipment if ON or OFF. True = ON, False = OFF.

#prints out the variable value and the type of variable each variable is
print(f"{voltage} {type(voltage)}")
print(f"{current} {type(current)}")
print(f"{name} {type(name)}")
print(f"{state} {type(state)}")
