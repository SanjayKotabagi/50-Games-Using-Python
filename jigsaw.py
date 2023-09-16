import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3

# Colors
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jigsaw Puzzle")

# Load and slice the image into puzzle pieces
image = pygame.image.load("Nature.jpeg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))
piece_size = WIDTH // GRID_SIZE
pieces = []

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        x = col * piece_size
        y = row * piece_size
        piece = image.subsurface(pygame.Rect(x, y, piece_size, piece_size))
        pieces.append((piece, pygame.Rect(x, y, piece_size, piece_size)))

random.shuffle(pieces)

# Main game loop
selected_piece = None
dragging = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not dragging:
                for piece, piece_rect in pieces:
                    if piece_rect.collidepoint(event.pos):
                        selected_piece = piece
                        pieces.remove((piece, piece_rect))
                        dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                x, y = event.pos
                nearest_x = round(x / piece_size) * piece_size
                nearest_y = round(y / piece_size) * piece_size
                piece_rect = pygame.Rect(nearest_x, nearest_y, piece_size, piece_size)
                pieces.append((selected_piece, piece_rect))
                selected_piece = None
                dragging = False

    screen.fill(WHITE)

    for piece, piece_rect in pieces:
        screen.blit(piece, piece_rect.topleft)

    if selected_piece:
        x, y = pygame.mouse.get_pos()
        screen.blit(selected_piece, (x - piece_size // 2, y - piece_size // 2))

    pygame.display.flip()
