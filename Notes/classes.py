# Luke Murdock, Class Notes

# Class and object example that we have used:
sentence  = "the quick brown fox jumped over the lazy dog"

print(sentence.upper())

# Creating a Class Example
class subject:
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room
    def __str__(self):
        return(f'\nName: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}\nRoom: {self.room}')

first = subject("CS Principles", 1, "Ms. LaRose", 200)
second = subject("CP2", 2, "Ms. LaRose", 200)
third = subject("CP3!", 2, "Ms. LaRose", 200)

# print(first)
# print(second)

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return(f'{self.name} is a {self.species} and they have {self.hp} HP and do {self.dmg} amount of a damage in battle.')
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f'{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}.')

            if opponent.hp <= 0:
                print(f'{opponent.name} is knocked out. {self.name} wins!')
            else:
                self.hp -= opponent.dmg
                print(f'{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp}.')

                if self.hp <= 0:
                    print(f'{self.name} is knocked out. {opponent.name} wins!')

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spiky = pokemon("Spiky", "Jolteon", 150, 100)

fluffy.battle(spiky)
slimy.battle(spiky)

# What is a class in python?
    # A class is a blueprint for an object.
# What is an object in python?
    # An object is an instance of a class.
# How do python classes relate to python objects?
    # Python classes create python objects.
# How do you create a python class?
    # You create one by using 'class class_name:' and then the methods (functions) inside of it.
# What are methods?
    # Methods are functions that exists for a specific class.
# How do you create a python object?
    # To create a python object you "call" the class and put in the needed parameters.
# How do you call a method for an object?
    # You call a method for an object by using 'object.method()'.
# Why do we use python classes?
    # We use python classes because they let us easily create multiple objects that contain multiple similar things that we choose.