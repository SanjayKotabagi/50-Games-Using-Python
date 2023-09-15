import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
TOWER_COLOR = (255, 255, 255)
DISK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
DISK_WIDTHS = [200, 150, 100]
DISK_HEIGHT = 20
NUM_DISKS = 3

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Initialize game variables
towers = [[], [], []]
tower_positions = [(150, 400), (400, 400), (650, 400)]
selected_tower = None
moves = 0

# Initialize the Tower of Hanoi with disks on the first tower
for i in range(NUM_DISKS, 0, -1):
    towers[0].append(i)

def draw_tower():
    for x, y in tower_positions:
        pygame.draw.rect(screen, TOWER_COLOR, (x - 10, y, 20, 200))

def draw_disk(tower_index):
    tower = towers[tower_index]
    tower_x, tower_y = tower_positions[tower_index]

    for i, disk in enumerate(tower):
        disk_width = DISK_WIDTHS[disk - 1]
        disk_color = DISK_COLORS[disk - 1]
        disk_x = tower_x - disk_width // 2
        disk_y = tower_y - (i + 1) * DISK_HEIGHT
        pygame.draw.rect(screen, disk_color, (disk_x, disk_y, disk_width, DISK_HEIGHT))

def move_disk(source, target):
    if towers[source]:
        disk = towers[source].pop()
        towers[target].append(disk)
        return True
    return False

def is_winning_state():
    return len(towers[0]) == 0 and len(towers[1]) == 0

def main():
    global selected_tower, moves

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, (tower_x, tower_y) in enumerate(tower_positions):
                    if tower_x - 100 < x < tower_x + 100 and tower_y - 100 < y < tower_y + 100:
                        if selected_tower is None:
                            selected_tower = i
                        else:
                            if move_disk(selected_tower, i):
                                moves += 1
                            selected_tower = None

        screen.fill(BACKGROUND_COLOR)
        draw_tower()

        for i in range(3):
            draw_disk(i)

        if is_winning_state():
            font = pygame.font.Font(None, 36)
            winning_text = font.render(f"Congratulations! You solved it in {moves} moves.", True, (255, 255, 255))
            screen.blit(winning_text, (WIDTH // 2 - 250, HEIGHT // 2 - 18))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
