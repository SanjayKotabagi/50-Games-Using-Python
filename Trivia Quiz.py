import random

# Define a list of trivia questions and their possible answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Paris"],
        "answer": "Paris",
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars",
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare",
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["Giraffe", "Elephant", "Blue Whale", "Hippopotamus"],
        "answer": "Blue Whale",
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"],
        "answer": "Nitrogen",
    },
    {
        "question": "In which country did the Olympic Games originate?",
        "options": ["Greece", "Italy", "France", "United States"],
        "answer": "Greece",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Gl", "Au", "Ag"],
        "answer": "Au",
    },
    {
        "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "options": ["Venus", "Mars", "Jupiter", "Mercury"],
        "answer": "Venus",
    },
    {
        "question": "Who wrote the novel '1984'?",
        "options": ["George Orwell", "Aldous Huxley", "F. Scott Fitzgerald", "J.K. Rowling"],
        "answer": "George Orwell",
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Brain", "Skin", "Liver"],
        "answer": "Skin",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
        "answer": "Leonardo da Vinci",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Jupiter",
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "South Korea", "Japan", "Vietnam"],
        "answer": "Japan",
    },
    {
        "question": "What is the chemical symbol for oxygen?",
        "options": ["O", "Ox", "Oy", "Oxg"],
        "answer": "O",
    },
    {
        "question": "Who wrote the play 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare",
    },
    {
        "question": "Which gas is known as 'Laughing Gas'?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrous Oxide", "Argon"],
        "answer": "Nitrous Oxide",
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2",
    },
    {
        "question": "Which country is known as the 'Land Down Under'?",
        "options": ["Canada", "Russia", "Australia", "Brazil"],
        "answer": "Australia",
    },
]


# Function to shuffle the order of answer options
def shuffle_options(options):
    shuffled_options = options.copy()
    random.shuffle(shuffled_options)
    return shuffled_options

# Function to display a question and its answer options
def ask_question(question_data):
    question = question_data["question"]
    options = shuffle_options(question_data["options"])
    answer = question_data["answer"]

    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    user_answer = input("Your answer (enter the number): ")

    try:
        user_answer = int(user_answer)
        if 1 <= user_answer <= len(options):
            user_answer = options[user_answer - 1]
        else:
            user_answer = None
    except ValueError:
        user_answer = None

    if user_answer == answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong. The correct answer is {answer}\n")
        return 0

# Main quiz loop
def main():
    score = 0

    print("Welcome to the Trivia Quiz!\n")

    for i, question_data in enumerate(questions, 1):
        print(f"Question {i}:")
        score += ask_question(question_data)

    print(f"You answered {score}/{len(questions)} questions correctly.")

if __name__ == "__main__":
    main()
