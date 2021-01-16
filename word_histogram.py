user_input = (input("Please enter a sentence: "))

user = user_input.split()
# print(user)

def word_sentence(user):
    tally = {}
    # for sentence in user:
    for word in user:
        keys = tally.keys()
        if word in keys:
            tally[word] += 1
        else:
            tally[word] = 1
    return tally

print(word_sentence(user))

