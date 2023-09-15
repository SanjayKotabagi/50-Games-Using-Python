import random

# Define categories and their corresponding words
categories = {
    "Animals": ["elephant", "giraffe", "penguin", "kangaroo", "octopus"],
    "Fruits": ["banana", "strawberry", "blueberry", "pineapple", "watermelon"],
    "Countries": ["australia", "france", "canada", "japan", "brazil"],
}

def choose_category():
    print("Choose a category:")
    for index, category in enumerate(categories.keys(), 1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(categories):
                return list(categories.keys())[choice - 1]
            else:
                print("Invalid choice. Please select a valid category.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_word(category):
    return random.choice(categories[category])

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    category = choose_category()
    word_to_guess = choose_word(category)
    guessed_letters = []
    attempts = 6

    print("\nLet's play Hangman!")
    print("Category:", category)
    print("Word to guess:", display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
        else:
            print("Invalid input. Please enter a single letter.")

        word_display = display_word(word_to_guess, guessed_letters)
        print(word_display)

        if word_display == word_to_guess:
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

    if word_display != word_to_guess:
        print("\nGame over. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
