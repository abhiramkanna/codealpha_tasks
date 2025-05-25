import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

word_list = ["ram", "python", "hangman", "youtube", "weekend", "BIET"]
chosen_word = random.choice(word_list).lower()
display = ['_' for _ in chosen_word]
already_guessed = set()
lives = 6
game_over = False

print("Welcome to Hangman!")
print(" ".join(display))

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    if len(guessed_letter) != 1:
        print("Please enter a single letter.")
        continue
    elif not guessed_letter.isalpha():
        print("Please enter a LETTER.")
        continue
    elif guessed_letter in already_guessed:
        print("You have already guessed that letter. Choose again.")
        continue

    already_guessed.add(guessed_letter)

    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
    else:
        lives -= 1
        print(HANGMAN_PICS[6 - lives])
        print(f"Wrong guess! You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lost! The word was:", chosen_word)
            break

    print(" ".join(display))

    if '_' not in display:
        game_over = True
        print("Congratulations! You won!")


