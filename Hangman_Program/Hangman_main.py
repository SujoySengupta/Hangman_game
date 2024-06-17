
import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

print(hangman_art.logo)

end_of_game = False
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\n---You lose.---")
            print(f"The answer was {chosen_word}.")

    #Joining all the elements in the list and turning it into a String.
    print(f"{' '.join(display)}")

    #Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\n---You win.---")

    print(hangman_art.stages[lives])
