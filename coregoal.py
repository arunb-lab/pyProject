import random

secret_number = random.randint(1, 100) # Pick a number between 1 and 100
max_attempts = 7
attempts = 0

print("I'm thinking of a number between 1 and 100. You have 7 guesses.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Brilliant! You guessed it in {attempts} tries.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
else:
    # This block runs only if the while loop completes naturally (no break)
    print(f"Game over! The number was {secret_number}.")