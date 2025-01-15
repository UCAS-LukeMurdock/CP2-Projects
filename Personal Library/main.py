# Luke Murdock, Personal Library

books = {"Fablehaven", "Dragonwatch", "Five Kingdoms", "Beyonders", "Michael Vey", "Percy Jackson", "39 Clues", "Leven Thumps", "Pillage", "Wings of Fire", "Lord of the Rings", "The Hobbit"}

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


def add(): #
    while True:
        try:
            add_book = str(input("Book You Want Added: ")).title()
        except:
            print("Incorrect Input")
            #Problem
        if add_book not in books:
            print("Not in")
            continue
        else:
            break

    books.append(add_book)
def remove(): #
    try:
        remove_book = str(input("Book You Want Added: ")).title()
    except:
        print("Incorrect Input")
    books.remove(remove_book)

