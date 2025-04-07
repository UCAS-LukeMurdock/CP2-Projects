# Luke Murdock, Scrapped Personal Portfolio

"""
OVERVIEW:
Create a user interface for your projects that shows of the programming projects you are most proud of (Note: you can keep this in the same repository IF you are using all of the projects from this class OR you can create a new repository called "personal_portfolio"). This program will in many ways serve as a programming resume for you so please make sure to make the user interfaces VERY intuitive.

REQUIREMENTS:
-Introduction:
    Brief explanation of what your portfolio is 
    How to use it (keep it short but informative)

-Menu: 
    Create an easy-to-use menu
    Include at least 6 projects you're proud of
    Can be from this class or others
    Example: A numbered list or clickable buttons for each project

-Project Descriptions: For each project, include:
    What the project does
    How you found the programming process
    What you learned
    Your role (if it was a group project)
    Note: This information should appear before the code runs

-Working Projects: 
    Make sure all projects actually work when selected
"""
#from  import as 
from projects import to_do_list, random_password_generator as password_gen, personal_library, movie_recommender as movie, financial_calculator as fin_calc, final_text_advent as final, battle_simulator

def menu(): # Introduces the program and then lets the user choose one of the programs
    print("\n\nWelcome to my Personal Portfolio, where you can see descriptions of and use/play programs that I have made or helped make.") # What it is
    print("To use this program, just type the number that corresponds to the program you want to run and then when it is done you can choose another one or exit this Portfolio.") # How to use it
    while True:
        choice = input("\n\n\nWhich program do you want to use?\n1. Personal Finance Program\n2. High Score Tracker\n3. Music Festival Management\n4. Battle Simulator\n5. Random Password Generator\n6. Movie Recommender\n7. Personal Library\n8. To Do List\n9. Financial Calculator\n10. Text Based Adventure (Final for Programming 1)\n11. Exit this Program\nChoice: ")
        if choice == "1":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            ()
        elif choice == "2":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            ()
        elif choice == "3":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            ()
        elif choice == "4":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            battle_simulator.menu()
        elif choice == "5":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            password_gen.main()
        elif choice == "6":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            movie.main()
        elif choice == "7":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            personal_library.main()
        elif choice == "8":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            to_do_list.main()
        elif choice == "9":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            fin_calc.main()
        elif choice == "10":
            print("\nDescription:\nDoes- \nProcess- \nLearned- \nRole- ")
            final.beach()
        elif choice == "11":
            print("Come Back Soon!")
            break
        else:
            print("Invalid Input (Insert an Integer in the Range)")
menu()

# Fix file_handler stuff
# Need to add group projects, descriptions, and check everything