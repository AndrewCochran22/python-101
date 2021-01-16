santa_asks = input("What all do you want for X-Mas? ")
santa_asks2 = input("Have you been good or bad this year? ")

def goodies(santa_asks):
    return santa_asks

def good_bad(santa_asks2):
    if santa_asks2 == good:
        Print("")
    elif str(santa_asks2) == bad:
        Print("bad")
    else:
        Print("If you pick wrong your bad!")
    return

wants = goodies(santa_asks)
print("Great! Krampus won't eat you this year...you get " + wants + "!")

