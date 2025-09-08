import random

from guessing_game import max_attempts


def play_game():
    rounds = int(input("How many rounds would you like to play? "))
    score = 0

    for round_number in range(1, rounds+1):
        number_to_guess = random.randint(1, 20)
        attempts = 0
        max_attempts = 5

        print(f"\nRound {round_number} of {rounds}")
        print("I have picked a number 1 and 20. Can you guess it?")
        print(f"You have {max_attempts} attempts.")

        while attempts < max_attempts:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
                if number_to_guess % 2 == 0:
                    print("Hint:The number is even.")
                else:
                    print("Hint:The number is odd.")
            elif guess > number_to_guess:
                print("Too high!")
                if number_to_guess % 2 == 0:
                    print("Hint:The number is even.")
                else:
                    print("Hint:The number is odd.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                score += 1
                break
        else:
            print("Sorry, the number was {number_to_guess}.")

    print(f"\nGame over! Your final score: {score} out of {rounds}")

    #Start the game
    play_game()