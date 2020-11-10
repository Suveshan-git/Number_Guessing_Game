# NUMBER GUESSING GAME
import random

# Setup the range
range_set = int(input("Enter a number you want the range to be set to: "))
print(f"The range is set to (1-{range_set})")
random_number = random.randint(1, range_set)
# print(random_number)

# Ask the user to guess
tries = 1
guess = int(input("Enter your guess: "))

# Check if the guess hit, was too low or was too high
while guess != random_number:
    if guess < random_number:
        print("Too low")
        guess = int(input("Enter your guess: "))
        tries += 1
    elif guess > random_number:
        print("Too high")
        guess = int(input("Enter your guess: "))
        tries += 1

tries +=1
print(f"HIT! Congratulations! You got it in {tries} tries.")

