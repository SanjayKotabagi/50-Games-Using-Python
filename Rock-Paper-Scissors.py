import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to end): ").lower()

        if player_choice == "quit":
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chooses {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    rock_paper_scissors()
