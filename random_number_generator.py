import random

top_of_range = input("Type a number: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number larger than 0.")
        quit()
else:
    print("That is not a number!")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Guess a number! ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("That is not a number!")
        continue

    if user_guess == random_number:
        print(f"Correct! You got the number in {guesses} tries!")
        break
    elif user_guess < random_number:
        print("Guess is too low.")
    else: 
        print("Guess is too high!")