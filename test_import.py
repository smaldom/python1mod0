# Simple example of importing a program that you write
# as a module and using a function from that program

import fixed_GPT_code as GPT

length = 50
width = 20
rain = 12

gallons = GPT.calculate_runoff(length, width, rain)

print(length, width, rain, "=", gallons)