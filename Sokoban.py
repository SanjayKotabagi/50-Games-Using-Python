import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 40
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
PLAYER_COLOR = (0, 0, 255)
BOX_COLOR = (255, 0, 0)
TARGET_COLOR = (0, 255, 0)
WALL_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
PLAYER_IMAGE = pygame.image.load("player.png")  # Replace with your player image
BOX_IMAGE = pygame.image.load("box.png")        # Replace with your box image
TARGET_IMAGE = pygame.image.load("target.png")  # Replace with your target image

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sokoban")

# Load level
level = [
    "######",
    "#  P #",
    "#   $#",
    "#   .#",
    "#  @ #",
    "######"
]

# Initialize game variables
player_pos = (1, 1)
boxes = [(2, 3)]
targets = [(4, 3)]
walls = [(x, y) for y, row in enumerate(level) for x, cell in enumerate(row) if cell == '#']

# Load images
player_image = pygame.transform.scale(PLAYER_IMAGE, (GRID_SIZE, GRID_SIZE))
box_image = pygame.transform.scale(BOX_IMAGE, (GRID_SIZE, GRID_SIZE))
target_image = pygame.transform.scale(TARGET_IMAGE, (GRID_SIZE, GRID_SIZE))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            dx, dy = 0, 0
            if event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
            elif event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1

            new_pos = (player_pos[0] + dx, player_pos[1] + dy)
            if new_pos not in walls:
                if new_pos in boxes:
                    box_index = boxes.index(new_pos)
                    new_box_pos = (new_pos[0] + dx, new_pos[1] + dy)
                    if new_box_pos not in walls and new_box_pos not in boxes:
                        boxes[box_index] = new_box_pos
                        player_pos = new_pos
                else:
                    player_pos = new_pos

    # Check for win
    if set(boxes) == set(targets):
        print("You win!")
        pygame.quit()
        sys.exit()

    # Draw the game
    screen.fill(BACKGROUND_COLOR)

    for x, y in walls:
        pygame.draw.rect(screen, WALL_COLOR, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    for x, y in targets:
        screen.blit(target_image, (x * GRID_SIZE, y * GRID_SIZE))

    for x, y in boxes:
        screen.blit(box_image, (x * GRID_SIZE, y * GRID_SIZE))

    screen.blit(player_image, (player_pos[0] * GRID_SIZE, player_pos[1] * GRID_SIZE))

    pygame.display.update()
