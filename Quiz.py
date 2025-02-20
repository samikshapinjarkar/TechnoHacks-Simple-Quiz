
import random

# Quiz questions categorized by topics
quiz_data = {
    "Science": [
        {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "answer": "H2O"},
        {"question": "What planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
        {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"question": "Which part of the plant conducts photosynthesis?", "options": ["Root", "Stem", "Leaf", "Flower"], "answer": "Leaf"}
    ],
    "History": [
        {"question": "Who was the first President of the United States?", "options": ["Abraham Lincoln", "George Washington", "John Adams", "Thomas Jefferson"], "answer": "George Washington"},
        {"question": "In which year did World War II end?", "options": ["1941", "1945", "1939", "1950"], "answer": "1945"},
        {"question": "Who discovered America?", "options": ["Christopher Columbus", "Marco Polo", "James Cook", "Vasco da Gama"], "answer": "Christopher Columbus"},
        {"question": "The Great Wall of China was built to protect against which invaders?", "options": ["Romans", "Mongols", "Persians", "Vikings"], "answer": "Mongols"}
    ],
    "Technology": [
        {"question": "Who founded Microsoft?", "options": ["Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg"], "answer": "Bill Gates"},
        {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Central Power Unit", "Computer Processing Unit", "Core Processing Utility"], "answer": "Central Processing Unit"},
        {"question": "Which company developed the iPhone?", "options": ["Microsoft", "Apple", "Samsung", "Google"], "answer": "Apple"},
        {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Tech Machine Learning", "Hyperlink Transfer Markup Language", "Home Tool Management Language"], "answer": "Hyper Text Markup Language"}
    ]
}

def ask_question(question_data):
    """Displays a question and gets the user's answer."""
    print("\n" + question_data["question"])
    options = question_data["options"]
    random.shuffle(options)  # Shuffle options for randomness

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your answer: "))
            if 1 <= choice <= len(options):
                return options[choice - 1] == question_data["answer"]
            else:
                print("Invalid choice. Enter a number from the options.")
        except ValueError:
            print("Please enter a valid number.")

def run_quiz():
    """Runs the quiz, asks questions, and calculates the score."""
    print("\nWelcome to the Quiz Game!")
    print("Choose a topic:")
    
    topics = list(quiz_data.keys())
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic}")

    while True:
        try:
            topic_choice = int(input("Enter the topic number: "))
            if 1 <= topic_choice <= len(topics):
                selected_topic = topics[topic_choice - 1]
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nStarting quiz on {selected_topic}!\n")
    questions = quiz_data[selected_topic]
    random.shuffle(questions)

    score = 0
    for question_data in questions:
        if ask_question(question_data):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {question_data['answer']}\n")

    print(f"Quiz finished! Your final score: {score}/{len(questions)}")
    print("\nThanks for playing! 🎉")

if __name__ == "__main__":
    while True:
        run_quiz()
        retry = input("Do you want to play again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Goodbye!")
            break
