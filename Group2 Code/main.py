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

main()