# Luke Murdock, Personal Library

books = [{"Fablehaven", "Brandon Mull"}, 
        ("Dragonwatch", "Brandon Mull"), 
        ("Five Kingdoms", "Brandon Mull"), 
        ("Beyonders", "Brandon Mull"), 
        ("Michael Vey", "Richard Paul Evans"), 
        ("Percy Jackson", "Rick Riordan"), 
        ("39 Clues", "Rick Riordan"), 
        ("Leven Thumps", "Obert Skye"), 
        ("Pillage", "Obert Skye"),
        ("Wings of Fire", "Tui T. Sutherland"), 
        ("Lord of the Rings", "J.R.R. Tolkien"), 
        ("The Hobbit", "J.R.R. Tolkien"), 
        ("The Stormlight Archive", "Brandon Sanderson"), 
        ("Mistborn", "Brandon Sanderson"), 
        ("Elantris", "Brandon Sanderson"), 
]

books = [
    {
        
    }
]

def main(): # This funcion prints the list and lets the user choose what they want to do with the list.
    while True:
        print(f"\nBook Library:\n{books}")

        try:
            choice = int(input("Search(1) Add(2) Remove(3) Exit(4)\n"))
        except:
            print("Incorrect Input")
            continue

        if choice == 1:
            search()
        elif choice == 2:
            add()
        elif choice == 3:
            remove()
        elif choice == 4:
            break
        else:
            print("Incorrect Integer")
            continue

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
            book_title = str(input("Title of The Book You Want Added: "))
            book_author = str(input("Author of The Book You Want Added: "))
        except:
            print("Incorrect Input")
            continue
        break

    add_book = (book_title, book_author)
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

main()