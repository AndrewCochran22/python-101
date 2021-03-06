from pet import Pet, CuddlyPet
from treat import ColdPizza, Bacon, VeganSnack
from toy import Toy
from menu import Menu

# Begin with no pets.
pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "Give a toy to all your pets",
    "Give all pets a treat",
    "View status of pets",
    "Do nothing",
    "Pet levels naturally lower",
]

adoption_menu = [
    "Pet",
    "CuddlyPet"
]

treat_menu = [
    "ColdPizza",
    "Bacon",
    "VeganSnack"
]

def main():   
    app = Menu("Please choose an Option: ", main_menu)
    types = Menu("Please choose a type of pet: ", adoption_menu)
    treats = Menu("Please pick a treat: ", treat_menu)

    while True:
        choice = app.get_choice()
        if (choice == 1):
            pet_name = input("What would you like your pet name to be? ")
            type_choice = types.get_choice()
            if (type_choice == 1):
                pets.append(Pet(pet_name))
            elif (type_choice == 2):
                pets.append(CuddlyPet(pet_name))
            num_pets = len(pets)
            print(f"\n\nYou now have {num_pets} pets.\n\n\n")

        elif (choice == 2):
            for pet in pets:
                pet.get_love()

        elif (choice == 3):
            for pet in pets:
                pet.eat_food()

        elif (choice == 4):
            for pet in pets:
                pet.get_toy(Toy())

        elif (choice == 5):
            print("Please choose what type of treat: ")
            treat_choice = treats.get_choice()
            if treat_choice == 1:
                for pet in pets:
                    pet.eat_treat(ColdPizza())
            elif treat_choice == 2:
                for pet in pets:
                    pet.eat_treat(Bacon())
            elif treat_choice == 3:
                for pet in pets:
                    pet.eat_treat(VeganSnack())

        elif (choice == 6):
            for pet in pets:
                print(pet)

        elif (choice == 7):
            for pet in pets:
                pet.be_alive()

        for pet in pets:
            pet.be_alive()

main()