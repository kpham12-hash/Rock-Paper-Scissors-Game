# Actual Code

import random 

while True: 
    user_guess = input("Pick one: Rock, Paper, or Scissors: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_guess}")
    print(f"Computer chose: {computer_choice}")

    if user_guess == computer_choice:
        print("It's a tie!")
    elif user_guess == 'rock' and computer_choice == "scissors":
        print("You win!!!")
    elif user_guess == "scissors" and computer_choice == "paper":
        print("You win!!!!")
    elif user_guess == "paper" and computer_choice == "rock":
        print("You win!!!")
    else:
        print(computer_choice)
        print("The computer wins!")

    play_again = input("Do you want to play again? (y/n)").lower()

    if play_again != "y":
        break
