import random
from hangman_words import word_list
from hangman_art import stages

lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
game_over = False

for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

correct_letters = []
used_letters = []

while not game_over:

    print(f"{lives}/6 Lives left")
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print(f"You've already guessed this letter: {guess}")
        continue
    else:
        used_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        lives -= 1
        print("Sorry! You lose a life!")
        if lives == 0:
            game_over = True
            print(f"You lose! It was '{chosen_word}'")

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives])
