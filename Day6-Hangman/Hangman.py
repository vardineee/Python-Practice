
import random
from hangman_art import logo,stages
from hangman_words import word_list


print(logo)
chosen_word = random.choice(word_list)


lives = 6

display = []
for item in chosen_word:
    display.append("_")


end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}.")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position]=letter

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word.You lose a life.")
        if lives == 0:
            end_of_game = True
            print(f"The word is {chosen_word}.")
            print("You lose")
    print(f"{''.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
