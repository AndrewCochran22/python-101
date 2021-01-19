def is_even(num1):
    if num1 % 2 == 0:
        print("True")
    elif num1 % 2 !=0:
        print("False")
    else:
        print("Give a number!")
    return

print(int(input("Give us an even number: ", is_even(10))))