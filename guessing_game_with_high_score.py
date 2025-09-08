import random
import os

HIGH_SCORE_FILE = "high_score.txt"

def get_high_score():
    """Read the high score from the file, or return 0 if file doesn't exist."""
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    return 0

def save_high_score(score):
    """Save the new high score to the file."""
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))

def play_round():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("\nI have picked a number between 1 and 20. Can you guess it?")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
            give_hint(number_to_guess)
        elif guess > number_to_guess:
            print("Too high!")
            give_hint(number_to_guess)
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            return 1  # 1 point for correct guess
    else:
        print(f"Sorry, the number was {number_to_guess}.")
        return 0

def give_hint(number):
    if number % 2 == 0:
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")

def play_game():
    print("Welcome to the Guessing Game with High Score!")
    score = 0
    high_score = get_high_score()
    print(f"Current high score: {high_score}")

    while True:
        rounds = int(input("\nHow many rounds do you want to play? "))
        for _ in range(rounds):
            score += play_round()
        print(f"\nYour score this session: {score} points!")

        if score > high_score:
            print("🎉 NEW HIGH SCORE! 🎉")
            save_high_score(score)
            high_score = score
        else:
            print(f"High score remains: {high_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()
