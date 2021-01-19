class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is a {self.species} and is {self.age} years old."

thor = Cat("Thor", 7)
steve = Cat("Steve", 5)
paul = Cat("Paul", 12)

print(thor.description())
print(steve.description())
print(paul.description())

# print(f"{thor.name} is {thor.species} and is {thor.age} years old.")
# print(f"{steve.name} is {steve.species} and is {steve.age} years old.")

# print("%s is %s years old." % (thor.name, thor.age))
# print("{} is {} years old." .format(thor.name, thor.age))