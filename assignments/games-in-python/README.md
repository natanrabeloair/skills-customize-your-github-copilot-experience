
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python using strings, loops, conditionals, and user input. The game should randomly choose a word, track the player's guesses, and clearly report whether the player wins or loses.

## 📝 Tasks

### 🛠️ Select a Secret Word

#### Description
Choose a random word from a predefined list of words and store it as the secret word.

#### Requirements
Completed program should:

- Define a list containing at least five words.
- Select one word randomly from the list.
- Store the selected word in a variable named `secret_word`.

### 🛠️ Track Guesses and Display Progress

#### Description
Ask the player to enter letters and update the game state as guesses are made.

#### Requirements
Completed program should:

- Accept a letter guess using `input()`.
- Track guessed letters in a collection.
- Display the current progress using underscores, such as `_ _ _`.
- Show the number of incorrect guesses remaining.
- Prevent duplicate guesses from being counted more than once.

### 🛠️ Complete the Game Loop

#### Description
Use a loop to continue the game until the player guesses the word or runs out of attempts.

#### Requirements
Completed program should:

- Continue prompting for guesses while the game is active.
- Reveal correctly guessed letters in the hidden word.
- End when every letter in the word is revealed.
- End when the player reaches the maximum number of incorrect guesses.
- Print a clear win or loss message.
- Use the starter code as a guide and complete the TODO sections.
