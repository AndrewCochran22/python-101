def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return c

fahrenheit = float(input("Pick a fahrenheit temp: "))
print("Your temperature in celsius is: ", fahrenheit_to_celsius(fahrenheit))

       