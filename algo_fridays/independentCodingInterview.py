# Function with 2 arguments
# Join strings together
# Reverse newString
# string1 = "hello";
# string2 = "you";

# def addAndReverse(string1, string2):
#     return string2[::-1], string1[::-1];

# print(addAndReverse(string1, string2));

# Function that takes string and returns 4th char
# If string too short, print "too short of a string"

def find4thChar(string):
    if len(string) < 4:
        print("too short of a string");
    else:
        print(string[3])
    return

find4thChar("hello");
find4thChar("hey");
find4thChar("hi");