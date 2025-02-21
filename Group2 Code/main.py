#Luke Murdock, Group 2 Code

def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome, ")
    while True:
        choice = input("\nGames(1) Scores(2) Profiles(3) Exit(4)\n")
        if choice == 1:
            games()
        elif choice == 2:
            scores()
        elif choice == 3:
            profiles()
        elif choice == 4:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue

# VINCENT'S CODE -----------------------------------------------------------------------------------------------

# LUKE'S CODE --------------------------------------------------------------------------------------------------
def add(score): # Finds out what to add
    name = input("What is your username?: ").strip()
    #search
    


# FAIRUS'S CODE ------------------------------------------------------------------------------------------------

main()

'''
tasks = []
# 
with open("To Do List/list.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        task = {}
        for detail_index, detail in enumerate(row):
            task.update({detail_types[detail_index]:row[detail_index]})
        tasks.append(task)

def write(): # 
    with open ("To Do List/list.csv", "w", newline="") as file:
        fieldnames = ["Name", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)


        

with open("Movie Recommender/Movies list.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        movie = {}
        for detail_index, detail in enumerate(row):
            movie.update({detail_types[detail_index]:row[detail_index]})
        movies.append(movie)
'''