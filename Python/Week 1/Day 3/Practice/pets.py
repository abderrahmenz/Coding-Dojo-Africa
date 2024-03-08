class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}")
        self.pet.noise()


class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.energy += 25

    def eat(self):
        print(f"{self.name} is eating")
        self.energy += 5
        self.health += 10

    def play(self):
        print(f"{self.name} is playing")
        self.health += 5

    def noise(self):
        print(f"{self.name} makes noise")

# Creating an instance of a Pet
my_pet = Pet("Fluffy", "Dog", ["Sit", "Fetch"])

# Creating an instance of a Ninja and assigning the pet instance to the pet attribute
my_ninja = Ninja("Hiro", "Yamamoto", "Biscuits", "Dog Food", my_pet)

# Invoking methods on the Ninja to interact with the pet
my_ninja.feed()
my_ninja.walk()
my_ninja.bathe()