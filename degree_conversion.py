while(True):
    try:
        celsius = float(input("Temperature in Celsius?"))
        fahrenheit = (celsius * 9/5) + 32
        print("%s Celsius in Fahrenheit is %s" % (celsius, fahrenheit))
        break
    except ValueError:
        print("We need a number!")