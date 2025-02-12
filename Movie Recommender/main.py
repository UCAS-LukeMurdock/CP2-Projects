#Luke Murdock, Movie Recommender
import csv

movies = []

def num_input(prompt, range = 0, data_type = "int"): # Checks and solves errors in int and float inputs (Has Range If Needed)
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt))
            elif data_type == "float":
                response = float(input(prompt))
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

# 
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

def display(): # 
    print("Movies:\n")
    for movie in movies:
        print(f"Title- {movie["Title"]}\nDirector- {movie["Director"]}\nGenre- {movie["Genre"]}\nRating- {movie["Rating"]}\nLength (min)- {movie["Length(min)"]}\nNotable Actors- {movie["Notable Actors"]}\n")

def recommend(): # 
    all_results = []
    print("\nFilter Options: Genre(1) Directors(2) Length(3) Actors(3)")
    filter_1 = input("\nFirst Filter: ").upper().trim()
    filter_2 = input("Second Filter: ").upper().trim()
    all_results.extend(searcher(filter_1))
    all_results.extend(searcher(filter_2))
    print("Search Results:\n")
    if all_results == []:
        print("None")
    else:
        for result in all_results:
            print(f"Title- {result["Title"]}\nDirector- {result["Director"]}\nGenre- {result["Genre"]}\nRating- {result["Rating"]}\nLength (min)- {result["Length(min)"]}\nNotable Actors- {result["Notable Actors"]}\n")
    
def searcher(filter):
    results = []
    


    return results

def main(): # 
    print("Welcome, this is a program with 105 movies which can be displayed or recommended")
    while True:
        choice = num_input("Display(1) Recommend(2)\n")
        if choice == 1:
            display()
        elif choice == 2:
            recommend()
        else:
            print("Something Broke!")

main()