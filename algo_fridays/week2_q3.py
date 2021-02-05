import random

def secret_number():
    guess = int(input("Hey user! Can you guess the secret number? "))
    randomnum = random.randint(0, 10)
    if guess == randomnum:
        print("That's it!")
    else:
        print("Wrong number")
        guess2 = input("Try again? Type yes or no: ")                
        if guess2 == "yes":
            return(secret_number())
        else:
            pass

secret_number()