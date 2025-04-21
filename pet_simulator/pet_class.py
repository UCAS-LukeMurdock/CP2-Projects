# Luke Murdock, Pet Class
import random
import math
from faker import Faker
import matplotlib.pyplot as plt
import numpy as np

class Pet: # A class that creates pet objects with many attributes and methods

    # Sets starting attributes during the creation of an object
    def __init__(self,name,species,color,eye_color,age,time,level,money,inventory,health,happy,energy,active):
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

        choice = input(f"\nName: {self.name}\nDescription: {self.name} is a {self.color} {self.species} with {self.eye_color} eyes that is {self.age} years old {well_state}.\n\nTime spent with {self.name} while being {self.age} years old: {self.time}\nLevel: {self.level}\nMoney: ${self.money}\nInventory:{items[:-1]}\n\nHappiness: {self.happy}\nEnergy: {self.energy}\nHealth: {self.health}\nWellness: {self.calc_well()}\n\nStatus Visual(1) Rename(2)  Exit(0)\nChoice: ").strip()
        if choice == "0":
            return
        
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
            print(f"\nThe visualization is a pop-up with a bar graph of {self.name}'s status. (Exit the pop-up to continue)")
            plt.show()

        elif choice == "2":
            rename = input(f"\nWhat do you want to rename {self.name} to?: ").strip().title()
            if rename == '':
                print("\nInvalid Input (The input were empty)")
                return
            print(f"\n{self.name}'s name was changed to {rename}!")
            self.name = rename

    def change_stats(self, happy, energy, health, time=1): # Changes the pet's attributes depending on the parameters
        self.happy += happy
        self.energy += energy
        self.health += health
        self.time += time


    def pet(self): # Increases the pet's happiness by 1 and tells the user they petted theit pet
        self.change_stats(1,0,0)
        return f"\nYou pet {self.name}"

    def feed(self): # Lets the user feed their pet food that they find or have bought which each have different attribute modifications
        choice = input(f"\nWhich food would you like to feed {self.name}?:\nBerry(1) Chips(2) Broccoli(3) Candy(4) Apple(5) Starfruit(6)  Exit(0)\nChoice: ").strip()
        if choice == "0":
            return "\nYou didn't feed your pet"
        elif choice == "1":
            food = f" berry that {self.name} found in a bush!"
            self.change_stats(1,3,4)
        elif choice == "2":
            food = f" chip that {self.name} found somewhere!"
            self.change_stats(7,10,-10)
        elif choice == "3":
            food = " broccoli"
            if "Broccoli garden" not in self.inventory:
                return f"\n{self.name} doesn't own a broccoli garden"
            self.change_stats(-5,10,15)
        elif choice == "4":
            food = " piece of candy"
            if "Candy bag" not in self.inventory:
                return f"\n{self.name} doesn't own a candy bag"
            self.change_stats(15,35,-20)
        elif choice == "5":
            food = "n apple"
            if "Apple tree" not in self.inventory:
                return f"\n{self.name} doesn't own an apple tree"
            self.change_stats(7,12,17)
        elif choice == "6":
            food = " starfruit"
            if "Starfruit" not in self.inventory:
                return f"\n{self.name} doesn't own a starfruit"
            self.change_stats(30,30,30)
            self.inventory.remove("Starfruit")
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        return f"\nYou fed {self.name} a{food}"
        
    def play(self): # Lets the user play or do activites with their pet, leveling up and buying new items unlocks these actions
        choice = input(f"\nWhat would you like to do with {self.name}?:\nGo on a long run(1) Hide-and-seek(2) Treasure hunt(3) Play on a pet videogame console(4) Play with a toy(5)  Exit(0)\nChoice: ").strip()
        limit = 0
        item = "none"
        once = False
        if choice == "0":
            return "\nYou didn't end up playing with your pet"
        elif choice == "1":
            text, change = f"\nYou went on a long, tiring run with {self.name}", [-5,-15,15]
        elif choice == "2":
            limit = 5
            text, change = f"\nYou played a fun game of hide-and-seek with {self.name}", [5,-5,10]
        elif choice == "3":
            limit = 10
            text, change = f"\nYou go on a really fun and energetic treasure hunt with {self.name}", [15,0,15]
        elif choice == "4":
            text, change, item = f"\nYou played pet videogames with {self.name} using the console", [45,5,-10], 'Pet videogame console'
        elif choice == "5":

            def toy_play(): # Lets the user play with their pet using an a certain item/toy which changes the stats/attributes that get changed
                once = False
                toy_choice = input(f"\nWhich toy would you like to use while playing with {self.name}?:\nCollar(1) Bone(2) Stick(3) Ball(4) Yarn(5) Football(6) Wishbone(7) Rope(8) Chew toy(9) Laserpen(10)  Exit(0)\nChoice: ").strip()
                if toy_choice == "0":
                    return "\nYou didn't end up using a toy to play with your pet", [0,0,0], "none", False
                elif toy_choice == "1":
                    toy, change, text = "Collar",[5,-1,5], random.choices([f"\nYou played fetch with {self.name} using the collar",f"\n{self.name} dug and hid the collar and you had to find it and dig it up",f"\nYou rode on {self.name} by holdling on to the collar that's on them"],weights = [10,10,1])[0]
                elif toy_choice == "2":
                    once = True
                    text, toy, change = random.choice([f"\nYou played fetch with {self.name} using the bone and ended up losing it",f"\n{self.name} dug and hid the bone and you couldn't find it"]),"Bone",[10,-5,5]
                elif toy_choice == "3":
                    once = True
                    text, toy, change = f"\nYou played fetch with {self.name} using the stick and it got lost in the foilage","Stick",[-2,0,10]
                elif toy_choice == "4":
                    once = True
                    text, toy, change = f"\nYou played fetch with {self.name} using the ball and it bounced away","Ball",[5,-7,15]
                elif toy_choice == "5":
                    once = True
                    text, toy, change = f"\nYou let {self.name} play with yarn for a while and it eventually got torn to shreds","Yarn",[7,-2,5]
                elif toy_choice == "6":
                    text, toy, change = f"\nYou played fetch with {self.name} using the football","Football",[10,-5,15]
                elif toy_choice == "7":
                    text, toy, change = f"\nYou let {self.name} chew on the wishbone","Wishbone",[7,0,12]
                elif toy_choice == "8":
                    text, toy, change = f"\nYou let {self.name} chew on the rope","Rope",[2,7,10]
                elif toy_choice == "9":
                    text, toy, change = f"\nYou let {self.name} chew on the chew toy and it makes some squeaky sounds","Chew toy",[15,2,2]
                elif toy_choice == "10":
                    text, toy, change = f"\nYou moved and dodged a point of light made from the laserpen that {self.name} tried to catch","Laserpen",[15,1,17]
                else:
                    return "\nInvalid Input (Insert a Corresponding Number)", [0,0,0], "none", False
                return text, change, toy, once

            text, change, item, once = toy_play()
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        
        if item != 'none':
            if item not in self.inventory:
                return f"\n{self.name} doesn't own a {item.lower()}"
            if once == True:
                 self.inventory.remove(item)
        elif limit != 0:
            if self.level < limit:
                f"\n{self.name} doesn't know the skills needed for that activity which are attained at level {limit}"
                return f"\n{self.name} doesn't know the skills for level {limit}"
        if change == [0,0,0]:
            return text
        self.change_stats(change[0],change[1],change[2])
        return text

    def competition(self): # Lets the user choose what to compete in and then sorts their pet and randomly generated pets by best to worst and then gives out prizes depending on what place you get
        choice = input(f"\nWhat competition would you like to do with {self.name}?:\nRace(1) Happiness Pageant(2) Strength Contest(3) Obstacle Course(4) Videogame Battle(5)  Exit(0)\nChoice: ").strip()
        
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
                
                competitor = [comp_stat,happy,energy,health,round((happy + energy + health)/3),fake.first_name(),random.choice(["red","orange","yellow","green","blue","purple",]),random.choice(["cat","dog","lizard","rabbit","chicken","lizard","hamster","frog"])]
                competitors.append(competitor)

            def sort_competitors(comp): # Allows sort() to sort by the competitors by their first index which is what the contest is testing against
                return comp[0]

            competitors.sort(reverse=True, key=sort_competitors)
            print()
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
        
        places = ["0th", "1st", "2nd", "3rd", "4th", "5th"]
        if choice == "0":
            return "\nYou didn't end up competing with your pet"
        elif choice == "1":
            type, limit, comp_info, change = "Race", 1, [self.energy,1,1], [1,-5,5]
        elif choice == "2":
            type, limit, comp_info, change = "Happiness Pageant", 5, [self.happy,0,1], [2,-7,10]
        elif choice == "3":
            type, limit, comp_info, change = "Strength Contest", 10, [self.health,2,1], [3,-12,15]
        elif choice == "4":
            type, limit, comp_info, change = "Obstacle Course", 15, [self.energy+self.health,3,2], [4,-17,20]
        elif choice == "5":
            type, limit, comp_info, change = "Videogame Battle", 20, [self.calc_well(),3,3], [5,-15,25]
            if self.level < limit:
                return f"\n{self.name} doesn't know the skills for level {limit}"
            if "Pet videogame console" not in self.inventory:
                return f"{self.name} doesn't own a pet videogame console"
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        
        if self.level < limit:
            return f"\n{self.name} doesn't know the skills needed for the {type} that are attained at level {limit}"
        outcome, prize = compete(comp_info[0],comp_info[1],comp_info[2])
        prize *= int(choice)
        self.money += prize
        self.change_stats(change[0]+prize, change[1], change[0])
        return f"\n{self.name} competed and got {places[outcome]} place in the {type} and earned ${prize}"
        
    def shop(self): # Lets the user buy items that they have not previously bought if they have enough money
        choice = input(f"\nWhat would you like buy for {self.name}?:\n{self.name}'s Money: ${self.money}\n\n(1) $5 - Chew toy\n(2) $10 - Rope\n(3) $10 - Wishbone\n(4) $15 - Football\n(5) $25 - Laserpen\n(6) $50 - Pet videogame console\n\n(7) $10 - Broccoli garden \n(8) $15 - Candy bag \n(9) $20 - Apple tree \n(10) $30 - Starfruit \n\nExit(0)\nChoice: ").strip()
        if choice == "0":
            return "\nYou didn't end up competing with your pet"
        elif choice == "1":
            bought, spent = "Chew toy", 5
        elif choice == "2":
            bought, spent = "Rope", 10
        elif choice == "3":
            bought, spent = "Wishbone", 10
        elif choice == "4":
            bought, spent = "Football", 15
        elif choice == "5":
            bought, spent = "Laserpen", 25
        elif choice == "6":
            bought, spent = "Pet videogame console", 50
        elif choice == "7":
            bought, spent = "Broccoli garden", 10
        elif choice == "8":
            bought, spent = "Candy bag", 15
        elif choice == "9":
            bought, spent = "Apple tree", 20
        elif choice == "10":
            bought, spent = "Starfruit", 30
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        
        if bought in self.inventory:
            return f"\n{self.name} already owns a {bought}"
        elif self.money < spent:
            return f"\n{self.name} doesn't have enough money to buy the {bought} for ${spent}"
        self.inventory.append(bought)
        self.money -= spent
        self.change_stats(5,0,0)
        return f"\nYou successfully bought the {bought} for {self.name} at the price of ${spent}"

    def sleep(self): # Lets the user choose how long the pet sleeps, changing the stats and then it processes/progresses the pet depending on their stats
        sleep_time = input(f"\nHow long do you want {self.name} to sleep?: Six hours(1) Eight hours(2) Ten hours(3)  Exit(0)\nChoice: ").strip()
    
        if sleep_time == "0":
            return "\nYou didn't let your pet sleep"
        elif sleep_time == "1":
            self.change_stats(-5,25,-5, time=1)
        elif sleep_time == "2":
            self.change_stats(0,17,5, time=2)
        elif sleep_time == "3":
            self.change_stats(0,20,3, time=3)
        else:
            return "\nInvalid Input (Insert a Corresponding Number)"
        
        print(f"\nYou let {self.name} sleep\n\n\nZZZzzz\n\n\n{self.name} woke up")
        if self.energy < 0:
            self.energy = 10
            self.change_stats(0,0,-45, time=7)
            print(f"{self.name} slept for a very long time and no longer feels deprived of energy, though he feels a lot weaker")
        elif self.energy < 40:
            self.change_stats(0,20,-25, time=5)
            print(f"{self.name} slept for longer than you wanted but feels more energized, even though he feels weaker")

        def processing(): # Checks to see if the pet has done enough actions and if it is happy enough and then grows it and levels it up accordingly
            growth, level = 0, self.level
            text = f'{self.name} is still level {level} (Increase their Wellness to potentially level them up)'

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

                if self.level > level:
                    text = f"{self.name} has leveled up from level {level} to level {self.level}!"

                if self.level >= 1 and level < 1:
                    text += f"\n({self.name} now knows the skills to be able to participate in the Race competition)"
                if self.level >= 5 and level < 5:
                    text += f"\n({self.name} now knows the skills to be able to play hide-and-seek and participate in the Happiness Pageant competition)"
                if self.level >= 10 and level < 10:
                    text += f"\n({self.name} now knows the skills to be able to go on a treasure hunt and participate in the Strength Contest competition)"
                if self.level >= 15 and level < 15:
                    text += f"\n({self.name} now knows the skills to be able to participate in the Obstacle Course competition)"
                if self.level >= 20 and level < 20:
                    text += f"\n({self.name} now knows the skills to be able to participate in the Videogame Battle competition)"

            return f"\n{self.name} grew {growth} years overnight and is {'still' if growth == 0 else 'now'} {self.age} years old.\n{text}"

        return processing()
    

    def sick(self): # Makes the pet sick which brings its stats done and takes up time
        time_sick = random.randint(1,4)
        sickness = -math.ceil(self.calc_well() /3)
        if self.calc_well() > 100:
            self.change_stats(round(sickness*1.5),sickness,sickness*2, time_sick)
        else:
            self.change_stats(sickness-5,sickness,sickness-10, time_sick)
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
        if random.choice(["bad","good"]) == "good":
            stat = random.choice([[random.randint(1,7),0,0],[0,random.randint(1,7),0],[0,0,random.randint(1,7)]])
            self.change_stats(stat[0],stat[1],stat[2], time = 0)
            return f"\n{self.name} bursted with {'happiness' if stat[0] != 0 else 'energy' if stat[1] != 0 else 'healthiness'}!"
        else:
            stat = random.choice([[random.randint(-7,-1),0,0],[0,random.randint(-7,-1),0],[0,0,random.randint(-7,-1)]])
            self.change_stats(stat[0],stat[1],stat[2], time = 0)
            return f"\n{self.name} bursted with {'sadness' if stat[0] != 0 else 'tiredness' if stat[1] != 0 else 'unhealthiness'}!"
