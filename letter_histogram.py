user_input = str(input("Give us the first word that pops into your head: "))

def letter_tally(user_input):
    tally = {}
    for word in user_input:
        for letter in word:
            keys = tally.keys()
            if letter in keys:
                tally[letter] += 1
            else:
                tally[letter] = 1
    return tally
   
print(letter_tally(user_input))