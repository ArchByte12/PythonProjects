import random

from guessing_game import number_to_guess


def play_round():
    number_to_guess=random.randint(1,20)
    attempts=0
    max_attempts=5

    print("\nI have picked a number from 1 to 20. Can you guess it?")
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
            return 1 #return 1 point for correct guess
    else:
        print(f"Sorry, the number was {number_to_guess}")
        return 0 #no points for failure

def give_hint(number):
    if number % 2 == 0:
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")

def play_game():
    print("Welcome to Guessing Game!")
    score=0

    while True:
        rounds = int(input("\nHow many rounds do you want to play? "))
        for _ in range(rounds):
            score+=play_round()
        print(f"Your score this session: {score} points!")

        play_again=input("\nDo you want to play again? (yes/no) ").lower()
        if play_again == "no":
            print("Thank you for playing!")
            break

#Start the game
play_game()