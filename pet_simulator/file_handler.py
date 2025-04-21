# Luke Murdock, Read & Write to Files and Finding the active pet
import csv
from pet_class import Pet

def read_file(): # Turns a file into the pet class
    pets = []
    with open("pet_simulator/pet.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                continue
            pet = Pet(row[0],row[1],row[2],row[3],int(row[4]),int(row[5]),int(row[6]),int(row[7]),eval(row[8]),int(row[9]),int(row[10]),int(row[11]),eval(row[12]))
            pets.append(pet)
    return pets

def write_file(pets): # Writes the pet class to the file
    with open ("pet_simulator/pet.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name","species","color","eye color","age","time","level","money","inventory","health","happy","energy","active"])
        for pet in pets:
            writer.writerow([pet.name, pet.species, pet.color, pet.eye_color, pet.age, pet.time, pet.level, pet.money, pet.inventory, pet.health, pet.happy, pet.energy, pet.active])

def active_pet(pets): # Finds the active pet's index
    for ind, pet in enumerate(pets):
        if pet.active == True:
            return ind