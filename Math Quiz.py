import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 36
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quiz")

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)

# Function to generate a random math question
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*", "/"])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 // num2

    question = f"{num1} {operator} {num2} = ?"
    return question, result

# Function to display text on the screen
def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
def main():
    score = 0
    num_questions = 5

    for _ in range(num_questions):
        question, answer = generate_question()

        input_text = ""
        input_rect = pygame.Rect(250, 250, 300, 50)
        active = True

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text.isdigit():
                            if int(input_text) == answer:
                                score += 1
                                feedback = "Correct!"
                            else:
                                feedback = "Wrong!"
                            active = False
                            input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            screen.fill(BLACK)

            draw_text(question, 100, 100)
            draw_text("Score: " + str(score), 20, 20)
            draw_text(input_text, input_rect.x + 10, input_rect.y + 10, GRAY)
            pygame.draw.rect(screen, GRAY, input_rect, 2)

            if 'feedback' in locals():
                draw_text(feedback, 300, 400)

            pygame.display.flip()

            pygame.time.delay(1000)  # Pause for 1 second before the next question

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
