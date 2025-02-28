#Luke Murdock, Word Counter
from file_handle import count

def main():
    print("Welcome to this program that will add a word count and a time stamp to the end of a specified text file")
    while True:
        try:
            choice = int(input("\nAdd Word Count and Time Stamp to File(1) Exit(2)\n").strip())
        except:
            print("Invalid Input Type")
        if choice == 1:
            print(count(input("What is your desired text file's (.txt) relative path?:\n")))
        elif choice == 2:
            print("Come Back Soon!")
            break
        else:
            print("Not In Range")
main()