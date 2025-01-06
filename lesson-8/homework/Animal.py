import random

class Animal:
    def __init__(self, name, age, species, health=100):
        self.name = name
        self.age = age
        self.species = species
        self.health = health

    def eat(self):
        self.health += 10
        print(f"{self.name} the {self.species} is eating. Health is now {self.health}.")

    def move(self):
        self.health -= 5
        print(f"{self.name} the {self.species} is moving. Health is now {self.health}.")

    def sleep(self):
        self.health += 5
        print(f"{self.name} the {self.species} is sleeping. Health is now {self.health}.")

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "cow")
        self.milk_production = milk_production

    def graze(self):
        self.health += 15
        print(f"{self.name} the cow is grazing. Health is now {self.health}.")

    def produce_milk(self):
        milk = self.milk_production if self.health > 50 else self.milk_production // 2
        print(f"{self.name} produced {milk} liters of milk.")
        return milk

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "chicken")
        self.egg_count = 0

    def lay_eggs(self):
        if self.health > 30:
            self.egg_count += 1
            print(f"{self.name} laid an egg. Total eggs: {self.egg_count}.")
        else:
            print(f"{self.name} is too unhealthy to lay eggs.")

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "sheep")
        self.wool = 0

    def shear(self):
        if self.wool > 0:
            print(f"{self.name} was sheared for {self.wool} units of wool.")
            wool_collected = self.wool
            self.wool = 0
            return wool_collected
        else:
            print(f"{self.name} has no wool to shear.")
            return 0

    def grow_wool(self):
        self.wool += 1
        print(f"{self.name} is growing wool. Wool count: {self.wool}.")

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.inventory = {"milk": 0, "eggs": 0, "wool": 0}
        self.money = 0

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the farm.")

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.species}), Age: {animal.age}, Health: {animal.health}")

    def daily_routine(self):
        for animal in self.animals:
            animal.eat()
            animal.move()
            animal.sleep()
            if isinstance(animal, Cow):
                milk = animal.produce_milk()
                self.inventory["milk"] += milk
            elif isinstance(animal, Chicken):
                animal.lay_eggs()
                self.inventory["eggs"] += animal.egg_count
                animal.egg_count = 0  # Reset after collecting eggs
            elif isinstance(animal, Sheep):
                animal.grow_wool()

    def sell_products(self):
        earnings = self.inventory["milk"] * 2 + self.inventory["eggs"] * 1 + self.inventory["wool"] * 3
        print(f"Sold products for ${earnings}.")
        self.money += earnings
        self.inventory = {"milk": 0, "eggs": 0, "wool": 0}  # Clear inventory

    def handle_random_events(self):
        for animal in self.animals:
            if random.random() < 0.1:  # 10% chance of illness
                animal.health -= 20
                print(f"Oh no! {animal.name} the {animal.species} is sick. Health is now {animal.health}.")
            if random.random() < 0.05:  # 5% chance of escape
                print(f"Oh no! {animal.name} the {animal.species} has escaped!")
                self.animals.remove(animal)

# Example usage
farm = Farm("Sunny Acres")
cow = Cow("Bessie", 5, milk_production=10)
chicken = Chicken("Clusky", 2)
sheep = Sheep("Wooly", 3)

farm.add_animal(cow)
farm.add_animal(chicken)
farm.add_animal(sheep)

farm.daily_routine()
farm.handle_random_events()
farm.sell_products()

farm.list_animals()
