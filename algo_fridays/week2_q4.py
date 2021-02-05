import random

def magic8_ball():
    question = (input("Please ask magic8 ball a question: "))
    answers = ["yes", "no", "maybe one day"]
    print(answers[random.randint(0, len(answers)-1)])
    return

magic8_ball()    