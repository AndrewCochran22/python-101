#User input for #.
#Print out all numbers from 1 to that number.
#Divisible by 3, print "fizz".
#Divisible by 5, print "buzz".
#Divisible by 3 and 5, print "fizzbuzz".

number = int(input("Pick a number! "))

for num in range(number + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("# fizzbuzz")
    elif num % 3 == 0:
        print("# fizz")
    elif num % 5 == 0:
        print("# buzz")
    else:
        print("#", num)

     
    
    