# Luke Murdock, Character Handler
from file_handler import read_file, write_file, intput

def create():
    points_left = 16
    name = input("Character's Name: ")
    print("Your character has four stats: Health, Strength, Defense, Speed\nThey are given 16 point overall and you decide which states these point are allocated to")

    def stat_input(stat_type):
        stat = intput(f"Character's {stat_type} Stat: ", 0,points_left)
        points_left = points_left -stat
        return stat
    health = stat_input("Health")
    stren = stat_input("Strength")
    defen = stat_input("Defense")
    speed = stat_input("Speed")
    print(f"Name: {name} H: {health} St: {stren} D: {defen} Sp: {speed}")

        #Recursion and point stuff

create()

def display():
    pass

def remove():
    pass
