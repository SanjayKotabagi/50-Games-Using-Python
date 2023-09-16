import random

# Define the roulette wheel with red and black numbers
roulette_wheel = [
    ("Red", ["3", "9", "12", "18", "21", "27", "30", "36"]),
    ("Black", ["2", "6", "8", "10", "14", "16", "20", "24", "28", "32", "34"]),
    ("Red", ["1", "5", "7", "11", "13", "17", "19", "23", "25", "29", "31", "35"]),
    ("Black", ["4", "15", "22", "26", "33"])
]

# Player's initial balance
balance = 1000

while True:
    # Display player's balance
    print(f"Your balance: ${balance}")

    # Get the player's bet
    bet_amount = int(input("Place your bet (minimum bet is $10): "))
    
    if bet_amount < 10 or bet_amount > balance:
        print("Invalid bet amount. Minimum bet is $10. Try again.")
        continue

    bet_color = input("Bet on Red or Black: ").capitalize()

    if bet_color != "Red" and bet_color != "Black":
        print("Invalid bet choice. Please choose Red or Black. Try again.")
        continue

    # Spin the roulette wheel
    winning_color, winning_number = random.choice(roulette_wheel)
    print(f"The winning number is {winning_number} ({winning_color})")

    # Check if the player's bet is a win
    if bet_color == winning_color:
        print(f"Congratulations! You win ${bet_amount}")
        balance += bet_amount
    else:
        print(f"Sorry, you lose ${bet_amount}")
        balance -= bet_amount

    # Check if the player has run out of money
    if balance <= 0:
        print("You're out of money. Game over.")
        break

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thank you for playing!")
