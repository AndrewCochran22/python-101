# list = [0, -1, 2, 5, 3, -3, -4, 10]
# num = 0

# list.sort()

# while(num < len(list)):
#     if list[num] > 0:
#         print(list[:num], end = " ")

#     num += 1

    #append positives to new list
    #newList.append(checkedPositiveNumber)
    #print the new LIst at the end of your loop

numbers = [-1, -2, -6, 2, 6, 1, -5, 6]

numbers.sort()

for num in numbers:
    new_number = []
    if num > 0:
        new_number.append(num)
        print(num, end = " ")