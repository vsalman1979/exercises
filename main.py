import random

class TrueFalseGame:
    def __init__(self):
        self.questions = [
            {"question": "Nintendo started out as a playing card manufacturer.", "correct_answer": "True"},
            {"question": "The retail disc of Tony Hawk's Pro Skater 5 only comes with the tutorial.", "correct_answer": "True"},
            {"question": "In the 'Shrek' film franchise, Donkey is played by Eddie Murphy.", "correct_answer": "True"},
            {"question": "Hippopotomonstrosesquippedaliophobia is the irrational fear of long words.", "correct_answer": "True"},
            {"question": "The movie 'The Nightmare before Christmas' was all done with physical objects.", "correct_answer": "True"},
            {"question": "Soulja Boy's - Crank That won a Grammy for Best Rap Song in 2007.", "correct_answer": "False"},
            {"question": "The US emergency hotline is 911 because of the September 11th terrorist attacks.", "correct_answer": "False"},
            {"question": "The Republic of Malta is the smallest microstate worldwide.", "correct_answer": "False"},
            {"question": "In 'Super Mario 64', collecting 100 coins on a level will give you a 1-UP.", "correct_answer": "False"},
            {"question": "The logo for Snapchat is a Bell.", "correct_answer": "False"},
            {"question": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.", "correct_answer": "True"},
            {"question": "The proof for the Chinese Remainder Theorem used in Number Theory was NOT developed by its first publisher, Sun Tzu.", "correct_answer": "True"},
            {"question": "'Kamea,' the Gilbertese Islander word for dog, is derived from the English phrase 'Come here!'", "correct_answer": "True"},
            {"question": "Faust is a playable character in the 'Guilty Gear' series.", "correct_answer": "True"},
            {"question": "In Until Dawn, both characters Sam and Mike cannot be killed under any means until the final chapter of the game.", "correct_answer": "True"},
            {"question": "The Python programming language gets its name from the British comedy group 'Monty Python.'", "correct_answer": "True"},
            {"question": "Lead Singer Rivers Cuomo of American rock band Weezer attended Harvard.", "correct_answer": "True"},
            {"question": "In 'Resident Evil', only Chris has access to the grenade launcher.", "correct_answer": "False"},
            {"question": "'Resident Evil 7' is the first first-person Resident Evil game.", "correct_answer": "False"}
        ]

    def play(self):
        print("Welcome to the True or False Game!")

        name = input("What's your name? ")
        age = input("How old are you? ")
        print(f"Hello, {name}! You're {age} years old.")

        while True:
            rounds = int(input("How many questions would you like to answer? "))
            score = 0

            for _ in range(rounds):
                question_data = random.choice(self.questions)
                question = question_data["question"]
                correct_answer = question_data["correct_answer"]

                print(f"\nQuestion: {question}")
                answer = input("Answer (True/False): ")

                if answer == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {correct_answer}.")

            print(f"\nGame Over! Your score is {score} out of {rounds}.")

            play_again = input("Would you like to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                print("Thanks for playing! Goodbye!")
                break

# Main execution
if __name__ == "__main__":
    game = TrueFalseGame()
    game.play()