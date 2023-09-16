import random
import time

# Constants
MAP_WIDTH = 10
MAP_HEIGHT = 5
ENEMY_SYMBOL = 'E'
TOWER_SYMBOL = 'T'
EMPTY_SYMBOL = '.'
DELAY = 1  # Time delay between game updates (in seconds)

# Initialize the game map
game_map = [[EMPTY_SYMBOL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

# Define the tower and enemy classes
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shoot(self):
        return random.randint(1, 10)  # Random damage

class Enemy:
    def __init__(self):
        self.x = MAP_WIDTH - 1
        self.y = random.randint(0, MAP_HEIGHT - 1)

    def move(self):
        self.x -= 1

# Function to display the game map
def display_map():
    for row in game_map:
        print(' '.join(row))
    print()

# Initialize the game
player_score = 0
towers = []

while True:
    # Clear the map
    for row in game_map:
        row[:] = [EMPTY_SYMBOL] * MAP_WIDTH

    # Create and move enemies
    enemy = Enemy()
    enemies = [enemy]

    # Check if towers can shoot enemies
    for tower in towers:
        for enemy in enemies:
            if tower.x == enemy.x and tower.y == enemy.y:
                damage = tower.shoot()
                print(f"Tower at ({tower.x},{tower.y}) shoots an enemy for {damage} damage!")
                enemies.remove(enemy)
                player_score += damage

    # Move remaining enemies
    for enemy in enemies:
        enemy.move()

    # Update the game map
    for tower in towers:
        game_map[tower.y][tower.x] = TOWER_SYMBOL

    for enemy in enemies:
        game_map[enemy.y][enemy.x] = ENEMY_SYMBOL

    # Display the game map and score
    display_map()
    print(f"Player Score: {player_score}")

    # Check if the game is over
    if enemy.x < 0:
        print("Game Over!")
        break

    # Add a delay for game update
    time.sleep(DELAY)

    # Player can choose to build a tower
    build_tower = input("Build a tower? (yes/no): ").lower()
    if build_tower == "yes":
        tower_x = int(input("Enter tower X coordinate: "))
        tower_y = int(input("Enter tower Y coordinate: "))
        if game_map[tower_y][tower_x] == EMPTY_SYMBOL:
            towers.append(Tower(tower_x, tower_y))
