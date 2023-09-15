import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "dog", "elephant", "fish", "grape", "horse", "igloo", "jacket"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word by entering one letter at a time.")
    print("You have 6 attempts to guess the word. Good luck!")

    while True:
        print(f"\nAttempts left: {attempts}")
        display = display_word(word_to_guess, guessed_letters)
        print(display)

        if display == word_to_guess:
            print("Congratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Wrong guess!")
            attempts -= 1
            if attempts == 0:
                print("Game over. You've run out of attempts.")
                print(f"The word was: {word_to_guess}")
                break

if __name__ == "__main__":
    hangman()
