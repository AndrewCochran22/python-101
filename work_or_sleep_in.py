day = int(input('Day (0-6)?'))

if (day == 0) or (day == 6):
    print("Sleep in")

elif (day >= 1) and (day <=5):
    print("Work")

else:
    print("Incorrect parameters.")