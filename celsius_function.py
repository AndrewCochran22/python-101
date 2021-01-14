def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

celsius = float(input("Pick a celsius temp: "))
print("Your temperature in fahrenheit is: ", celsius_to_fahrenheit(celsius))

       

# while(True):
#     try:
#         celsius = float(input("Temperature in Celsius?"))
#         fahrenheit = (celsius * 9/5) + 32
#         print("%s Celsius in Fahrenheit is %s" % (celsius, fahrenheit))
#         break
#     except ValueError:
#         print("We need a number!")