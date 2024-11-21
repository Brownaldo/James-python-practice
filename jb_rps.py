#Set up prompt asking player for rock, paper or scissors
import random

def play_game():
    print("Welcome to Rock, Paper, Scissors, prepare to lose")
    player_choice = input("Enter Rock, Paper or Scissors...")
    print(f"You have picked {player_choice}.")
    
    options = ["Rock", "Paper", "Scissors"]
    random_number = random.randint(0,2)
    computer_choice = options[random_number]
    print(f"Computer have picked {computer_choice}.")

    if player_choice == computer_choice:
        print("This is a draw!")
    elif player_choice == "Rock" and computer_choice == "Paper":
        print("So computer wins!")
    elif player_choice == "Paper" and computer_choice == "Scissors":
        print("So scmputer wins!")
    elif player_choice == "Scissors" and computer_choice == "Rock":
        print("So Computer wins")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("Sooo You win!")
    elif player_choice == "Paper" and computer_choice == "Rock":
        print("Sooo You win!")
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("Sooo You win")
play_game()


#Player Enters the prompt of rock, paper or scissors

#Choice from the computer

#pair win conditions

#tells you who has won


