##  Word Guessing Game

This project contains a simple **Word Guessing Game** implemented in Python. The game can be found in the file [`Word guessing game.py`](./Word%20guessing%20game.py).

##  Overview

The Word Guessing Game is a command-line game where the player tries to guess a randomly chosen word by suggesting letters within a limited number of attempts. It is similar in spirit to the traditional game of Hangman.

##  Features

- Random word selection from a predefined list
- User-friendly command-line interface for guessing letters
- Input validation to prevent repeated or invalid guesses
- Tracks and displays correct and incorrect guesses
- Limited number of attempts to guess the word
- Reveals the word and result (win/lose) at the end

##  How to Run

1. Make sure you have Python installed (version 3.x recommended).
2. Download or clone this repository to your local machine.
3. Navigate to the `Word_guessing_game` folder.
4. Run the script with:

   ```bash
   python "Word guessing game.py"
   ```

##  Customization

- You can modify the list of words used in the game by editing the word list section in `Word guessing game.py`.
- Adjust the number of allowed attempts by changing the relevant variable in the script.

##  Example Gameplay

```
Welcome to the Word Guessing Game!
The word has 6 letters.
Current word: _ _ _ _ _ _
Guess a letter: e
Good job! 'e' is in the word.

Current word: _ e _ _ _ _
...
Congratulations! You've guessed the word: pepper
```

##  File Structure

- `Word guessing game.py` — Main Python script containing the game logic.

##  License

This project is for educational purposes and personal use.

---

Feel free to improve or expand the game!
