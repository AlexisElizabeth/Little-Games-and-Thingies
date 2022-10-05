#!/usr/bin/env python

from random import randint

def main():

    # Make printing this and getting difficulty be its own function.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficult.  Type 'easy' or 'hard': ")
    if difficulty == "easy":
        guesses_remaining = 10
    else:
        guesses_remaining = 5
    
    # make getting & printing the secret number a function
    secret_number = randint(1, 101)
    
    print(secret_number)
    
    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} guesses remaining to guess the number.")

        # make the part in here a function
        guess = int(input("Make a guess: "))
        if guess > 100 or guess < 0:
            print("This is not a number between 1 and 100")
        elif secret_number == guess:  #  I'd recommend putting this elif clause last.
            print(f"You got it! The answer was {secret_number}")
            guesses_remaining = 0
            # just exit the program here with exit().
        elif guess > secret_number:
            print("Too high.")
        elif guess < secret_number:
            print("Too low.")
        else:
            print("I don't understand")
        # keep this out of the function
        guesses_remaining -= 1
    
    if guesses_remaining == 0 and secret_number != guess:
        print(f"You lose! The answer was {secret_number}")


if __name__ == '__main__':
    main()
