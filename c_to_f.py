def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

celsius = float(input("Pick a celsius temp: "))
print("Your temperature in fahrenheit is: ", celsius_to_fahrenheit(celsius))

       