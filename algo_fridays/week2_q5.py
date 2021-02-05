def anagram():
    string = str(input("First word: "))
    string2 = str(input("Second word: "))
    if len(string) != len(string2):
        print("False")
        return
    dict = {}
    dict2 = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    print(dict)
    for letters in string2:
        if letters in dict2:
            dict2[letters] += 1
        else:
            dict2[letters] = 1
    print(dict2)
    if dict == dict2:
        print("True")
    else:
        print("False")

anagram()