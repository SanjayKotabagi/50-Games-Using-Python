import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Morse Code Translator")

# Initialize font
font = pygame.font.Font(None, 36)

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' ',
}

# Function to translate text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
        else:
            morse_code += ' '
    return morse_code

# Function to draw text on the screen
def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main loop
def main():
    input_text = ''
    morse_code = ''
    translating_to_morse = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if translating_to_morse:
                        morse_code = text_to_morse(input_text)
                    else:
                        # Implement Morse code to text translation here
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_SPACE:
                    input_text += ' '
                else:
                    input_text += event.unicode

        screen.fill(BLACK)

        if translating_to_morse:
            draw_text("Text to Morse Code:", 50, 50)
            draw_text(input_text, 50, 100)
            draw_text("Press Enter to Translate", 50, 150)
            draw_text("Morse Code:", 50, 250)
            draw_text(morse_code, 50, 300)
        else:
            # Implement drawing for Morse code to text translation here
            pass

        pygame.display.flip()

if __name__ == "__main__":
    main()
