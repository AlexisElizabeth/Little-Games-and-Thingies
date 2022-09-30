import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

print(logo)
chosen_word = random.choice(word_list)
print(f'TEST: Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")
print(display)

end_of_game = False
guesses_remaining = 6
guessed_letters = ""

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in guessed_letters:
        print("You have already guessed that letter.  Guess again.")
    else:
        if guess not in chosen_word:
            guesses_remaining -= 1
            guessed_letters += guess
            print(display)
            print(stages[guesses_remaining])
            print(f"You have {guesses_remaining} wrong guesses remaining")
            if guesses_remaining == 0:
                end_of_game = True
                print("You lose!")
        else:
            for index in range(0, len(chosen_word)):
                if chosen_word[index] == guess:
                    display[index] = guess
                    guessed_letters += guess
            print(display)
            if "_" in display:
                print(stages[guesses_remaining])
                print(f"You have {guesses_remaining} wrong guesses remaining")
            else:
                end_of_game = True
                print("You win!")





