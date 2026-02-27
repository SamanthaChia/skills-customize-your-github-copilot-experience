
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a text-based Hangman game in Python that reinforces string manipulation, loops, conditionals, and user input. Students will practice designing control flow and working with lists.

## 📝 Tasks

### 🛠️ Word Selection Setup

#### Description
Create a list of words and write a function to randomly choose one each time the game starts. You may hard‑code the list or load it from a file.

#### Requirements
Completed program should:

- Contain a predefined list of at least 10 words
- Randomly select a word using the `random` module
- Never reveal the chosen word until the game ends


### 🛠️ Game Loop and Guessing Logic

#### Description
Implement the main game loop that asks the player for letter guesses and updates the display accordingly. Track correct and incorrect guesses and limit the number of wrong attempts.

#### Requirements
Completed program should:

- Prompt the player for a single-letter guess each turn
- Reveal correctly guessed letters in the word (e.g. `h _ n g m a n`)
- Decrement remaining attempts on incorrect guesses
- End the game when the word is guessed or attempts run out
- Print a win message if the player succeeds or a lose message showing the full word


### 🛠️ Input Validation and Replay Option

#### Description
Add checks so the user cannot enter invalid input (like more than one character or non‑letters) and give the option to play again after the game finishes.

#### Requirements
Completed program should:

- Reject non‑alphabetical or multi‑character entries with a friendly warning
- Allow the player to start a new game without restarting the program


---

Good luck, and have fun coding your Hangman game!
