# 6. Question 6:

# Write a function called sameFrequency which accepts two positive integers
# The function should return True if both numbers have the same frequency of digits
# Some Examples:
# print(sameFrequency(182, 281)) #true
# print(sameFrequency(34, 14)) #false
# print(sameFrequency(3589578, 5879385)) #true
# print(sameFrequency(22, 222)) #false

def sameFrequency(posint1, posint2):
    posint1 = int(input("Positive integer 1: "))
    posint2 = int(input("Positive integer 2: "))

    # if len(posint1) != len(posint2):
    #     print("False")
    #     return

    dict = {}
    dict2 = {}

    for pos in posint1:
        if pos in dict:
            dict[pos] += 1
        else:
            dict[pos] = 1
    print(dict)

sameFrequency(input, input)