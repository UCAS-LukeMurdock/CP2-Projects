# Luke Murdock, Personal Library

books = [
    {
        "title": "Fablehaven",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 2
    },
    {
        "title": "Dragonwatch",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 5,
        "times read": 1
    },
    {
        "title": "Five Kingdoms",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 5,
        "times read": 2
    },
    {
        "title": "Beyonders",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 1
    },
    {
        "title": "Michael Vey",
        "author": "Richard Paul Evans",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 1
    },
    {
        "title": "Rick Riordan",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 1
    },
    {
        "title": "Leven Thumps",
        "author": "Obert Skye",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 0
    },
    {
        "title": "Wings of Fire",
        "author": "Tui T. Sutherland",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 3
    },
    {
        "title": "The Stormlight Archive",
        "author": "Brandon Sanderson",
        "genre": "Fantasy",
        "stars": 5,
        "times read": 1
    },
    {
        "title": "Refugee",
        "author": "Alan Gratz",
        "genre": "Historical Fiction",
        "stars": 3,
        "times read": 1
    },
]

def num_input(prompt, data_type, range = 0): # Checks and solves errors in int and float inputs
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

def simple_display(): # Displays the Titles and Authors
    print(f"")
    pass

def display_all(): # Displays All of the Information
    pass

def search(): # This function searchs for the user's key word inside of the titles and authors of the books in the list and prints them
    search_results = []
    while True:
        try:
            search_word = str(input("Search for Title or Author: ")).upper()
        except:
            print("Incorrect Input")
            continue
        break

    for book in books:
        if search_word in book[0].upper() or search_word in book[1].upper():
            search_results.append(book)
    print(f"\nSearch Results: {search_results}")

def add(): # This funciton adds the user's desired book's title and author to the library list
    while True:
        try:
            title = input("Title of The Book You Want Added: ")
            author = input("Author of The Book You Want Added: ")
            genre = input("Genre of The Book You Want Added: ")
            stars = num_input("Rating out of 5 Stars for The Book You Want Added: ")
            times_read = num_input("The Amount of Times You Have Read The Book You Want Added: ")
        except:
            print("Incorrect Input")
            continue
        break

    add_book = {
        "title": title,
        "author": author,
        "genre": genre,
        "stars": stars,
        "times read": times_read}
    
    books.append(add_book)

def remove(): # This function removes the user's desired book from the list, if it's in the list
    while True:
        book_found = 0
        try:
            book_title = str(input("Title of Book You Want Removed: ")).upper()
        except:
            print("Incorrect Input")
            continue
        for book in books:
            if book_title == book[0].upper():
                found_book = book
                book_found = 1
        if book_found == 0:
            print("Book Not In Library")
            continue
        elif book_found == 1:
            books.remove(found_book)
            break

def main(): # This funcion prints the list and lets the user choose what they want to do with the list.
    while True:

        try:
            choice = int(input("Simple Display(1) Display All(2) Search(3) Add(4) Remove(5) Exit(6)\n"))
        except:
            print("Incorrect Input")
            continue

        if choice == 1:
            simple_display()
        elif choice == 2:
            display_all()
        elif choice == 3:
            search()
        elif choice == 4:
            add()
        elif choice == 5:
            remove()
        elif choice == 6:
            break
        else:
            print("Incorrect Integer")
            continue

main()