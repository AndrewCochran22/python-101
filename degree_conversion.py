# while(True):
#     try:
#         celsius = float(input("Temperature in Celsius?"))
#         fahrenheit = (celsius * 9/5) + 32
#         print("%s Celsius in Fahrenheit is %s" % (celsius, fahrenheit))
#         break
#     except ValueError:
#         print("We need a number!")

C = float(input("Temp in Celsius? "))
F = (C * 9/5) + 32
print("Temperature in C is %s, temperature in F is %s" % (C, F))