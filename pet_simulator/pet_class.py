# Luke Murdock, Pet Class
import random
from faker import Faker
import matplotlib.pyplot as plt
import numpy as np

class Pet: # A class that creates pet objects with many attributes and methods
    def __init__(self,name,species,color,eye_color,age,time,level,money,inventory,health,happy,energy,active): # Sets starting attributes during the creation of an object
        self.name = name
        self.species = species
        self.color = color
        self.eye_color = eye_color
        self.age = age

        self.time = time
        self.level = level
        self.money = money
        self.inventory = inventory

        self.health = health
        self.happy = happy
        self.energy = energy

        self.active = active

    def __str__(self): # When an object fron this class is printed it will print like this, with all of its details
        return (f'\nName: {self.name}\nSpecies: {self.species}\nColor: {self.color}\nEye Color: {self.eye_color}\nAge: {self.age}\nTime: {self.time}\nLevel: {self.level}\nmoney: {self.money}\ninventory: {self.inventory}\nhealth: {self.health}\nhappy: {self.happy}\nenergy: {self.energy}\nactive: {self.active}')
    

    def calc_well(self): # This returns the average of a pet's status called wellness
        return round((self.health + self.happy + self.energy)/3)

    def status(self): # This displays the status of the pet and lets the user see a visual of it and rename the pet
        if self.calc_well() >= 100:
            well_state = 'and feels extremely well'
        elif self.calc_well() >= 85:
            well_state = 'and feels really well'
        elif self.calc_well() >= 75 :
            well_state = 'and feels well'
        elif self.calc_well() >= 50 :
            well_state = 'but feels fine, though not too well'
        elif self.calc_well() >= 25 :
            well_state = 'but does not feel well'
        elif self.calc_well() > 0 :
            well_state = 'but feels very unwell'
        else:
            well_state = 'but feels moribund'

        items = ""
        for item in self.inventory:
            items += f" {item},"

        choice = input(f"\nName: {self.name}\nDescription: {self.name} is a {self.color} {self.species} with {self.eye_color} eyes that is {self.age} years old {well_state}.\n\nTime spent with {self.name} while being {self.age} years old: {self.time}\nLevel: {self.level}\nMoney: ${self.money}\nInventory:{items[:-1]}\n\nHappiness: {self.happy}\nEnergy: {self.energy}\nHealth: {self.health}\nWellness: {self.calc_well()}\n\nType '0' to exit, '1' for a visualization, and the pet's new name, if you want to rename {self.name}.\nChoice: ").strip().title()
        
        if choice == "1": # This makes the visual bar graph
            stats = ('Happy', 'Energy', 'Health', 'Wellness')
            stat_counts = {'Stat': np.array([self.happy, self.energy, self.health, self.calc_well()])}
            width = 0.6
            fig, ax = plt.subplots()
            bottom = np.zeros(4)
            for stat, stat_count in stat_counts.items():
                p = ax.bar(stats, stat_count, width, label=stat, bottom=bottom)
                bottom += stat_count
                ax.bar_label(p, label_type='center')
            ax.set_title(f"{self.name}'s Status")
            ax.legend()
            print(f"The visualization is a pop-up with a bar graph of {self.name}'s status. (Exit the pop-up to continue)")
            plt.show()

        elif choice != "0" and choice != "":
            print(f"\n{self.name}'s name was changed to {choice}!")
            self.name = choice

    def change_stats(self, happy, energy, health, time=1): # Changes the pet's attributes depending on the parameters
        self.happy += happy
        self.energy += energy
        self.health += health
        self.time += time


    def pet(self): # Increases the pet's happiness by 1 and tells the user they petted theit pet
        self.change_stats(1,0,0)
        return f"\nYou pet {self.name}"

    def feed(self): # Lets the user feed their pet food that they find or have bought which each have different attribute modifications
        choice = input(f"\nWhich food would you like to feed {self.name}?:\nBerry(1) Chips(2) Broccoli(3) Candy(4) Apple(5) Starfruit(6)  Exit(0)\nChoice: ")
        if choice == "0":
            return "\nYou didn't feed your pet"
        elif choice == "1":
            print(f"\n{self.name} found a berry in a bush!")
            self.change_stats(1,3,4)
        elif choice == "2":
            print(f"\n{self.name} found a chip somewhere!")
            self.change_stats(7,10,-10)
        elif choice == "3":
            if "Broccoli garden" not in self.inventory:
                return f"\n{self.name} doesn't own a broccoli garden"
            self.change_stats(-5,10,15)
        elif choice == "4":
            if "Candy bag" not in self.inventory:
                return f"\n{self.name} doesn't own a candy bag"
            self.change_stats(15,35,-20)
        elif choice == "5":
            if "Apple tree" not in self.inventory:
                return f"\n{self.name} doesn't own an apple tree"
            self.change_stats(7,12,17)
        elif choice == "5":
            if "Starfruit" not in self.inventory:
                return f"\n{self.name} doesn't own a starfruit"
            self.change_stats(30,30,30)
            self.inventory.remove("Starfruit")
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        return f"\nYou fed {self.name}"
        
    def play(self): # Lets the user play or do activites with their pet, leveling up and buying new items unlocks these actions
        choice = input(f"\nWhat would you like to do with {self.name}?:\nGo on a long run(1) Hide-and-seek(2) Treasure hunt(3) Play on a pet videogame console(4) Play with a toy(5)  Exit(0)\nChoice: ")
        if choice == "0":
            return "\nYou didn't end up playing with your pet"
        elif choice == "1":
            self.change_stats(-5,-15,15)
            return f"\nYou went on a long, tiring run with {self.name}"
        elif choice == "2":
            if self.level < 5:
                return f"\n{self.name} doesn't know the skills for level 5"
            self.change_stats(5,-5,10)
            return f"\nYou played a fun game of hide-and-seek with {self.name}"
        elif choice == "3":
            if self.level < 5:
                return f"\n{self.name} doesn't know the skills for level 10"
            self.change_stats(15,0,15)
            return f"\nYou go on a really fun and energetic treasure hunt with {self.name}"
        elif choice == "4":
            if "\nPet videogame console" not in self.inventory:
                return f"{self.name} doesn't own a pet videogame console"
            self.change_stats(45,5,-10)
            return f"\nYou played pet videogames with {self.name} using the console"
        elif choice == "5":

            def toy_play(): # Lets the user play with their pet using an a certain item/toy which changes the stats/attributes that get changed
                toy_choice = input(f"\nWhich toy would you like to play with {self.name}?:\nCollar(1) Bone(2) Stick(3) Ball(4) Yarn(5) Football(6) Wishbone(7) Rope(8) Chew toy(9) Laserpen(10)  Exit(0)\nChoice: ")
                if choice == "0":
                    return "\nYou didn't end up using a toy to play with your pet"
                elif choice == "1":
                    self.change_stats(5,-1,5)
                    return random.choices([f"\nYou played fetch with {self.name} using the collar",f"\n{self.name} dug and hid the collar and you had to find it and dig it up",f"\nYou rode on {self.name} by holdling on to the collar that's on them"],weights = [10,10,1])
                elif choice == "2":
                    if "\nBone" not in self.inventory:
                        return f"{self.name} doesn't have a bone"
                    self.change_stats(10,-5,5)
                    return random.choice([f"\nYou played fetch with {self.name} using the bone",f"\n{self.name} dug and hid the bone and you had to find it and dig it up"])
                elif choice == "3":
                    if "\nStick" not in self.inventory:
                        return f"{self.name} doesn't have a stick"
                    self.change_stats(-2,0,10)
                    return f"\nYou played fetch with {self.name} using the stick"
                elif choice == "4":
                    if "\nBall" not in self.inventory:
                        return f"{self.name} doesn't have a ball"
                    self.change_stats(5,-7,15)
                    return f"\nYou played fetch with {self.name} using the ball"
                elif choice == "5":
                    if "\nYarn" not in self.inventory:
                        return f"{self.name} doesn't have yarn"
                    self.change_stats(7,-2,5)
                    return f"\nYou let {self.name} play with yarn for a while"
                elif choice == "6":
                    if "\nFootball" not in self.inventory:
                        return f"{self.name} doesn't own a football"
                    self.change_stats(10,-5,15)
                    return f"\nYou played fetch with {self.name} using the football"
                elif choice == "7":
                    if "\nWishbone" not in self.inventory:
                        return f"{self.name} doesn't own a wishbone"
                    self.change_stats(7,0,12)
                    return f"\nYou let {self.name} chew on the wishbone"
                elif choice == "8":
                    if "\nRope" not in self.inventory:
                        return f"{self.name} doesn't own a rope"
                    self.change_stats(2,7,10)
                    return f"\nYou let {self.name} chew on the rope"
                elif choice == "9":
                    if "\nChew toy" not in self.inventory:
                        return f"{self.name} doesn't own a chew toy"
                    self.change_stats(15,2,2)
                    return f"\nYou let {self.name} chew on the chew toy and it makes some squeaky sounds"
                elif choice == "10":
                    if "\nLaserpen" not in self.inventory:
                        return f"{self.name} doesn't own a laserpen"
                    self.change_stats(15,1,17)
                    return f"\nYou moved and dodged a point of light made from the laserpen that {self.name} tried to catch"
                else:
                    return "\nInvalid Input (Insert a Corresponding Number)"

            return toy_play()
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"

    def competition(self): # Lets the user choose what to compete in and then sorts their pet and randomly generated pets by best to worst and then gives out prizes depending on what place you get
        choice = input(f"\nWhat competition would you like to do with {self.name}?:\nRace(1) Happiness Pageant(2) Strength Contest(3) Obstacle Course(4) Videogame Battle(5)  Exit(0)\nChoice: ")
        
        def compete(stat,stat_ind,amount): # This is what makes the competitors and sorts them from best to worst
            fake = Faker()
            competitors = [[stat,self.happy,self.energy,self.health,self.calc_well(),self.name,self.color,self.species]]
            for i in range(0,4):
                happy,energy,health = random.randint(50,100),random.randint(50,100),random.randint(50,100)
                if amount == 1:
                    comp_stat = [happy,energy,health][stat_ind]
                elif amount == 2:
                    comp_stat = energy + health
                elif amount == 3:
                    comp_stat = round((happy + energy + health)/3)
                
                competitor = [comp_stat,happy,energy,health,round((happy + energy + health)/3),random.choice(fake.first_name()),random.choice(["red","orange","yellow","green","blue","purple",]),random.choice("cat","dog","lizard","rabbit","chicken","lizard","hamster","frog")]
                competitors.append(competitor)

            def sort_competitors(comp): # Allows sort() to sort by the competitors by their first index which is what the contest is testing against
                return comp[0]

            competitors.sort(reverse=True, key=sort_competitors)
            for ind, competitor in enumerate(competitors):
                if competitor[5] == self.name:
                    place = ind +1
                print(f"{ind+1}. {competitor[5]} | {competitor[6]} {competitor[7]} | {competitor[1]} Happy | {competitor[2]} Energy | {competitor[3]} Health | {competitor[4]} Wellness | ")
            money = 0
            if place == 1:
                money = 5
            elif place == 2:
                money = 3
            elif place == 3:
                money = 1
            return place, money

        if choice == "0":
            return "\nYou didn't end up competing with your pet"
        elif choice == "1":
            if self.level < 5:
                return f"\n{self.name} doesn't know the skills for level 1"
            outcome, prize = compete(self.energy,1,1)
            prize *= 1
            self.money += prize
            self.change_stats(0,-5,5)
            return f"\n{self.name} competed and got {outcome} place in the Race and earned ${prize}"
        elif choice == "2":
            if self.level < 5:
                return f"\n{self.name} doesn't know the skills for level 5"
            outcome, prize = compete(self.happy,0,1)
            prize *= 2
            self.money += prize
            self.change_stats(5,-7,10)
            return f"\n{self.name} competed and got {outcome} place in the Happiness Pageant and earned ${prize}"
        elif choice == "3":
            if self.level < 5:
                return f"\n{self.name} doesn't know the skills for level 10"
            outcome, prize = compete(self.health,2,1)
            prize *= 3
            self.money += prize
            self.change_stats(10,-12,15)
            return f"\n{self.name} competed and got {outcome} place in the Strength Contest and earned ${prize}"
        elif choice == "4":
            if self.level < 5:
                return f"\n{self.name} doesn't know the skills for level 15"
            outcome, prize = compete(self.energy + self.health,3,2)
            prize *= 4
            self.money += prize
            self.change_stats(15,-17,20)
            return f"\n{self.name} competed and got {outcome} place in the Obstacle Course and earned ${prize}"
        elif choice == "5":
            if self.level < 5:
                return f"\n{self.name} doesn't know the skills for level 20"
            if "\nPet videogame console" not in self.inventory:
                return f"{self.name} doesn't own a pet videogame console"
            outcome, prize = compete(self.calc_well(),3,3)
            prize *= 5
            self.money += prize
            self.change_stats(20,-15,25)
            return f"\n{self.name} competed and got {outcome} place in the Videogame Battle and earned ${prize}"
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        
    def shop(self): # Lets the user buy items that they have not previously bought if they have enough money
        choice = input(f"\nWhat would you like buy for {self.name}?:\n\nChew toy $5 (1)\nRope $10 (2)\nWishbone $10 (3)\nFootball $15 (4)\nLaserpen $25 (5)\nPet videogame conssole $50 (6)\n\nBroccoli garden $10 (7)\nCandy bag $15 (8)\nApple tree $20 (9)\nStarfruit $50 (10)\n\nExit(0)\nChoice: ")
        if choice == "0":
            return "\nYou didn't end up competing with your pet"
        elif choice == "1":
            if "\nChew toy" in self.inventory:
                return f"{self.name} already owns a chew toy"
            bought, spent = "Chew toy", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "2":
            if "\nRope" in self.inventory:
                return f"{self.name} already owns a rope"
            bought, spent = "Rope", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "3":
            if "\nWishbone" in self.inventory:
                return f"{self.name} already owns a wishbone"
            bought, spent = "Wishbone", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "4":
            if "\nFootball" in self.inventory:
                return f"{self.name} already owns a football"
            bought, spent = "Football", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "5":
            if "\nLaserpen" in self.inventory:
                return f"{self.name} already owns a Laserpen"
            bought, spent = "Laserpen", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "6":
            if "\nPet videogame console" in self.inventory:
                return f"{self.name} already owns a pet videogame console"
            bought, spent = "Pet videogame console", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "7":
            if "\nBroccoli garden" in self.inventory:
                return f"{self.name} already owns a broccoli garden"
            bought, spent = "Broccoli garden", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "8":
            if "\nCandy bag" in self.inventory:
                return f"{self.name} already owns a candy bag"
            bought, spent = "Candy bag", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "9":
            if "\nApple tree" in self.inventory:
                return f"{self.name} already owns a apple tree"
            bought, spent = "Apple tree", 5
            self.inventory.append(bought)
            self.money -= spent
        elif choice == "10":
            if "\nStarfruit" in self.inventory:
                return f"{self.name} already owns a starfruit"
            bought, spent = "Starfruit", 5
            self.inventory.append(bought)
            self.money -= spent
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        self.happy += 5
        return f"\nYou successfully bought {bought} for {self.name} at the price of ${spent}"

    def sleep(self): # Lets the user choose how long the pet sleeps, changing the stats and then it processes/progresses the pet depending on their stats
        sleep_time = input(f"\nHow long do you want {self.name} to nap?: Six hours(1) Eight hours(2) Ten hours(3)  Exit(0)\nChoice: ")
        if sleep_time == "0":
            return "\nYou didn't let your pet sleep"
        elif sleep_time == "1":
            self.change_stats(0,7,2, 1)
        elif sleep_time == "2":
            self.change_stats(0,6,5, 2)
        elif sleep_time == "1":
            self.change_stats(0,4,5, 3)
            print(f"\nYou let {self.name} sleep\n\n\nZZZzzz\n\n\n{self.name} woke up")

        def processing(): # Checks to see if the pet has done enough actions and if it is happy enough and then grows it and levels it up accordingly
            if self.time >= 20:
                growth = round(self.time/20)
                self.time = 0
                self.age += growth
                if self.calc_well() >= 100:
                    self.level += 5
                elif self.calc_well() >= 85:
                    self.level += 3
                elif self.calc_well() >= 75:
                    self.level += 2
                elif self.calc_well() >= 50:
                    self.level += 1
            return f"\n{self.name} has grown {growth} years and is now {self.age} years old. {self.name} is {'now also' if self.calc_well() >= 75 else 'still'} level {self.level}."

        return processing()
    

    def sick(self): # Makes the pet sick which brings its stats done and takes up time
        time_sick = random.randint(1,4)
        self.change_stats(-20,-25,-15, time_sick)
        return f"\n{self.name} got sick for enough time that you could have done {time_sick} activites with them!"
    
    def find_toy(self): # Lets the pet find a toy that they can use in play-time
        toy = random.choice(["Bone","Ball","Stick","Yarn"])
        self.inventory.append(toy)
        return f"\n{self.name} found a toy!\nIt's a {toy}"
    
    def find_money(self): # Lets the pet find some money
        money = random.randint(1,7)
        self.money += money
        return f"\n{self.name} found ${money}!"
    
    def stat_burst(self): # Lets the pet randomly increase one of their stats
        stat = random.choice([[random.randint(1,7),0,0],[0,random.randint(1,7),0],[0,0,random.randint(1,7)]])
        self.change_stats(stat[0],stat[1],stat[2], time = 0)
        return f"\n{self.name} feels bursted with {'happiness' if stat[0] != 0 else 'energy' if stat[1] != 0 else 'healthiness'}!"
