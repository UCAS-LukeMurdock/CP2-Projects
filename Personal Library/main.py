# Luke Murdock, Personal Library

books = {("Fablehaven", "Brandon Mull"), ("Dragonwatch", "Brandon Mull"), ("Five Kingdoms", "Brandon Mull"), ("Beyonders", "Brandon Mull"), ("Michael Vey", "Richard Paul Evans"), ("Percy Jackson", "Rick Riordan"), ("39 Clues", "Rick Riordan"), ("Leven Thumps", "Obert Skye"), ("Pillage", "Obert Skye"), ("Wings of Fire", "Tui T. Sutherland"), ("Lord of the Rings", "J.R.R. Tolkien"), ("The Hobbit", "J.R.R. Tolkien")}

def main(): # This funcion prints the list and lets the user choose what they want to do with the list.
    while True:
        print(books)

        try:
            choice = int(input("Book Library:\n Search(1) Add(2) Remove(3) Exit(4)\n"))
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

def search(): #
    while True:
        try:
            book_title = str(input("Title of The Book You Want Added: ")).title()
        except:
            print("Incorrect Input")
            continue
        break

def add(): #
    while True:
        try:
            book_title = str(input("Title of The Book You Want Added: "))
            book_author = str(input("Author of The Book You Want Added: "))
        except:
            print("Incorrect Input")
            continue
        break

    add_book = (book_title, book_author)
    books.add(add_book)

def remove(): #
    while True:
        book_found = 0
        try:
            book_title = str(input("Title of Book You Want Removed: ")).title()
        except:
            print("Incorrect Input")
            continue
        for book in books:
            if book_title == book[0].title():
                found_book = book
                book_found = 1
        if book_found == 0:
            print("Book Not In Library")
            continue
        elif book_found == 1:
            books.remove(found_book)
            break

main()