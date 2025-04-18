# Luke Murdock, Read & Write to Files, Integer Input Handler, and other Handlers
import csv


class Pet: # 
    def __init__(self,name,species,color,eye_color,age,level,money,inventory,health,hunger,happy,energy,active):
        self.name = name
        self.species = species
        self.color = color
        self.eye_color = eye_color
        self.age = age

        self.level = level
        self.money = money
        self.inventory = inventory

        self.health = health
        self.hunger = hunger
        self.happy = happy
        self.energy = energy

        self.active = active

    def __str__(self):
        (f'\nName: {self.name}\nSpecies: {self.species}\nColor: {self.color}\nEye Color: {self.eye_color}\nAge: {self.age}\n: {self.level}\nmoney: {self.money}\ninventory: {self.inventory}\nhealth: {self.health}\nHunger: {self.hunger}\nhappy: {self.happy}\nenergy: {self.energy}\nactive: {self.active}')

def read_file(): # Turns a file into the pet class
    pets = []
    with open("pet_simulator/pet.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                continue
            pet = Pet(row[0],row[1],row[2],row[3],row[4],row[5],row[6],eval(row[7]),row[8],row[9],row[10],row[11],row[12])
            pets.append(pet)
    return pets

def write_file(pets): # Writes the pet class to the file
    with open ("pet_simulator/pet.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name","species","color","eye color","age","level","money","inventory","health","hunger","happy","energy","active"])
        for pet in pets:
            writer.writerow([pet.name, pet.species, pet.color, pet.eye_color, pet.age, pet.level, pet.money, pet.inventory, pet.health, pet.hunger, pet.happy, pet.energy, pet.active])

def active_pet(pets): # Finds the active user's index
    for ind, pet in enumerate(pets):
        if pet.active == True:
            return ind