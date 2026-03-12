import random

print(
    "Winning rules of the game ROCK PAPER SCISSORS are:\n"
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissors wins \n"
)


while True:
    print("Enter your choice \n 0-Rock \n 1-Paper \n 2-scissor")
    user_choice = int(input("Enter choice : "))
    while user_choice > 3 or user_choice < 0:
        print("Invalid user choice1")
        break

    choice = ""
    if user_choice == 0:
        choice = "rock"
    elif user_choice == 1:
        choice = "paper"
    else:
        choice = "scissor"
    print("User choice is : ", choice)
    print("Now it's computer turn... ")
    comp_choice = ""

    computer_choice = random.randint(0, 3)
    if comp_choice == 0:
        comp_choice == "rock"
    elif comp_choice == 1:
        comp_choice = "rock"
    else:
        comp_choice = "scissor"
    print("computer choice is ", comp_choice)

    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0 and computer_choice == 1:
        print("You win !")
    elif user_choice == 0 and computer_choice == 2:
        print("You win !")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer win")
    elif user_choice == 1 and computer_choice == 0:
        print("computer win")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer will one ")
    elif user_choice == 2 and computer_choice == 1:
        print("you win !!")
        
    print("Do you want to play again . ")
    ans=input("Yes or No").lower()
    if ans== "n":
        break
    
    


print("Thanks for playing !!!")
