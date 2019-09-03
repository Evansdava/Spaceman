# Spaceman Project

## Description
Spaceman is a guessing game.  There is a mystery word which the user tries to guess one letter at a time.  

## Spec
Read the [spec here](https://docs.google.com/document/d/1y1WPgJERAuLRJjeSXTf5znjhsrtPjnzPKfD03_f6v7w/edit?usp=sharing) for more details

## Pseudocode
When the program is run, a random word from a predetermined list is chosen to be guessed.
A short intro is displayed, showing the rules of the game.
After confirmation from the user, blank spaces representing letters of the secret word are displayed and the user is prompted for a guess.
    This guess is checked against the letters of the secret word:
        If correct, that letter (or letters) is filled in, with unguessed letters still blank.
        If incorrect, the number of guesses left is reduced.
        The user is notified of the outcome of their guess, and prompted for another.
        This repeats until the word is guessed or there are no guesses left.
    If the word is guessed, the user wins.
    If all guesses are exhausted, the user loses.
    The user is prompted to play again regardless of outcome.
