#Ask user for numerical input 'n'
user_input = int(input("I need a numerical input <=10: "))

n = 0
m = 1
count = 0

while count < user_input:
    print(n)
    o = n + m
    n = m
    m = o
    count += 1