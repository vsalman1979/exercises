import random

# Import the data from the uploaded file
from game_data import data

def format_entity(entity):
    """Format the entity data into a printable string."""
    name = entity['name']
    description = entity['description']
    country = entity['country']
    return f"{name}, a {description}, from {country}"

def check_guess(guess, a_followers, b_followers):
    """Check if the guess is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def higher_lower_game():
    print("Welcome to the Higher or Lower Game!")

    score = 0
    game_should_continue = True
    entity_b = random.choice(data)

    while game_should_continue:
        # Set entity A as the previous entity B, and select a new entity B
        entity_a = entity_b
        entity_b = random.choice(data)

        # Ensure entity A and B are different
        while entity_a == entity_b:
            entity_b = random.choice(data)

        print(f"Compare A: {format_entity(entity_a)}.")
        print("VS")
        print(f"Against B: {format_entity(entity_b)}.")

        # Ask the user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower counts for both entities
        a_follower_count = entity_a['follower_count']
        b_follower_count = entity_b['follower_count']

        # Check if the user is correct
        is_correct = check_guess(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

# Run the game
higher_lower_game()




