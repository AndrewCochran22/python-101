class Person:
    def __init__(self, name, email, phone, friends = []):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
    
    def greet(self, other_person):
        print(f"Hello {other_person.name}, I am {self.name}!")
        return

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}\n{self.name}'s phone number: {self.phone}")

    def add_friend(self, friends):
        self.friends.append(friends)

    def num_friends(self):
        self.friends.len(friends)

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(f"Jordan's email is {jordan.email} and phone number is {jordan.phone}.")

sonny.print_contact_info()

# jordan.friends.append(sonny)
# sonny.friends.append(jordan)

jordan.add_friend(sonny)
sonny.add_friend(jordan)

jordan.num_friends()