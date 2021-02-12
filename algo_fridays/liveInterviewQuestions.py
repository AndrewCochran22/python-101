# Given array of random strings
# Write function that returns new array
# Only 4 letters or more
# randomStrings = ['elephant', 'cat', 'penguin', 'bird', 'dog', 'rat', 'lion, 'parrot']
randomStrings = ['elephant', 'cat', 'penguin', 'bird', 'dog', 'rat', 'lion', 'parrot'];

def fourOrMore():
    newArray = [];
    for word in randomStrings:
        if len(word) >= 4:
            newArray.append(word);
    return newArray;

print(fourOrMore())