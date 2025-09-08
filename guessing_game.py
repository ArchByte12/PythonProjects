import random #let us pick a random number

#game setup
number_to_guess = random.randint(1,20)
attempts = 0
max_attempts = 5

print("Welcome to the Guessing Game")
print("I have picked a number between 1 and 20. Can you guess it?")
print("You have", max_attempts, "attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Your guess is too low.")
        #Hint: is the number even or odd?
        if number_to_guess%2==0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    elif guess > number_to_guess:
        print("Your guess is too high.")
        if number_to_guess%2==0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
else:
    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}")