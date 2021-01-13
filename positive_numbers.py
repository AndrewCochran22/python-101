list = [0, -1, 3, 4, -2, 8, 2]
num = 0

list.sort()

while(num < len(list)):
    if list[num] > 0:
        print(list[num], end = " ")

    num += 1