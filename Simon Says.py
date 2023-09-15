import random
import time

# Define the possible commands
commands = [
    "APPLE", "BANANA", "CHERRY", "ORANGE", "LEMON",
    "STRAWBERRY", "GRAPE", "BLUEBERRY", "RASPBERRY", "BLACKBERRY",
    "WATERMELON", "CANTALOUPE", "PINEAPPLE", "KIWI", "MANGO",
    "APRICOT", "PEACH", "PLUM", "NECTARINE", "PEAR",
    "CARROT", "BROCCOLI", "CAULIFLOWER", "CABBAGE", "CELERY",
    "CUCUMBER", "TOMATO", "POTATO", "ONION", "GARLIC",
    "RADISH", "LETTUCE", "SPINACH", "KALE", "CILANTRO",
    "BASIL", "MINT", "ROSEMARY", "THYME", "OREGANO",
    "LAVENDER", "SAGE", "DILL", "PARSLEY", "CHIVES",
    "SUNFLOWER", "DAFFODIL", "TULIP", "ROSE", "LILY",
    "DAISY", "IRIS", "TULIP", "PEONY", "MARIGOLD",
    "VIOLET", "PANSY", "DAHLIA", "ZINNIA", "CARNATION",
    "SANDCASTLE", "SEASHELL", "BEACHBALL", "SUNGLASSES", "SWIMSUIT",
    "BEACHTOWEL", "SNORKEL", "SUNSCREEN", "FLIPFLOPS", "SURFBOARD",
    "PICNIC", "BARBECUE", "HOTDOG", "HAMBURGER", "CORNDOG",
    "PIZZA", "PASTA", "SALAD", "ICECREAM", "SODA",
    "COOKIES", "CAKE", "CHOCOLATE", "CANDY", "JELLYBEANS",
    "LOLLIPOP", "GUMBALL", "CUPCAKE", "DONUT", "PIE",
    "CHICKEN", "HOTDOG", "BURGER", "FRIES", "NACHOS",
    "TACOS", "PIZZA", "SUSHI", "PASTA", "SALAD",
    "TENNIS", "SOCCER", "BASKETBALL", "VOLLEYBALL", "BASEBALL",
    "FOOTBALL", "HOCKEY", "SWIMMING", "RUNNING", "CYCLING",
    "JUMPING", "YOGA", "PILATES", "WRESTLING", "BOXING",
    "SKIING", "SNOWBOARDING", "SKATING", "GOLF", "RUGBY",
    "DANCING", "CHEERLEADING", "WATERPOLO", "DIVING", "SURFING",
    "BOATING", "KAYAKING", "CANOEING", "RAFTING", "SAILING",
    "FISHING", "HUNTING", "CAMPING", "HIKING", "BACKPACKING",
    "PICNIC", "BARBECUE", "HOTDOG", "HAMBURGER", "CORNDOG",
    "PIZZA", "PASTA", "SALAD", "ICECREAM", "SODA",
    "COOKIES", "CAKE", "CHOCOLATE", "CANDY", "JELLYBEANS",
    "LOLLIPOP", "GUMBALL", "CUPCAKE", "DONUT", "PIE",
    "CHICKEN", "HOTDOG", "BURGER", "FRIES", "NACHOS",
    "TACOS", "PIZZA", "SUSHI", "PASTA", "SALAD",
    "SANDCASTLE", "SEASHELL", "BEACHBALL", "SUNGLASSES", "SWIMSUIT",
    "BEACHTOWEL", "SNORKEL", "SUNSCREEN", "FLIPFLOPS", "SURFBOARD",
    "PICNIC", "BARBECUE", "HOTDOG", "HAMBURGER", "CORNDOG",
    "PIZZA", "PASTA", "SALAD", "ICECREAM", "SODA",
    "COOKIES", "CAKE", "CHOCOLATE", "CANDY", "JELLYBEANS",
    "LOLLIPOP", "GUMBALL", "CUPCAKE", "DONUT", "PIE",
    "CHICKEN", "HOTDOG", "BURGER", "FRIES", "NACHOS",
    "TACOS", "PIZZA", "SUSHI", "PASTA", "SALAD",
    "SANDCASTLE", "SEASHELL", "BEACHBALL", "SUNGLASSES", "SWIMSUIT",
    "BEACHTOWEL", "SNORKEL", "SUNSCREEN", "FLIPFLOPS", "SURFBOARD",
    "HOLIDAY", "VACATION", "ADVENTURE", "EXPLORE", "DISCOVER",
    "RELAX", "ESCAPE", "TRAVEL", "JOURNEY", "VOYAGE",
    "EXPEDITION", "DESTINATION", "EXCURSION", "TOUR", "RETREAT",
    "EXPLORE", "DISCOVER", "HOLIDAY", "VACATION", "ADVENTURE"
]

# Function to generate a random command
def generate_command():
    return random.choice(commands)

# Function to display a sequence of commands
def display_sequence(sequence):
    for command in sequence:
        print("Simon says:", command)
        time.sleep(1)  # Wait for 1 second before the next command
        clear_screen()

# Function to clear the screen (works in Windows and Linux)
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get the player's input
def get_player_input():
    player_sequence = input("Your turn (enter commands separated by spaces): ").strip().upper().split()
    return player_sequence

# Function to check if the player's input matches the sequence
def check_player_input(player_sequence, sequence):
    return player_sequence == sequence

# Main game loop
def main():
    print("Welcome to Simon Says!")
    score = 0

    while True:
        sequence = []
        sequence.append(generate_command())
        display_sequence(sequence)

        player_sequence = get_player_input()
        if check_player_input(player_sequence, sequence):
            score += 1
            print(f"Good job! Your score: {score}\n")
        else:
            print(f"Wrong sequence! Game over. Your score: {score}\n")
            break

if __name__ == "__main__":
    main()
