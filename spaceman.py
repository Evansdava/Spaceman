import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letters_guessed.count(letter) == 0:
            return False

    # Only reached if no letters have been shown to be false
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    output = ""
    for letter in secret_word:
        if letters_guessed.count(letter) > 0:
            output += letter.upper()+" "
        else:
            output += "_ "

    return output


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    # Check if the letter guess is in the secret word
    if secret_word.find(guess) != -1: # All secret words/guesses are lowercase
        return True
    else:
        return False

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    guesses_left = 7
    game_over = False

    while (game_over == False):
        # Show the guessed word so far
        print("\n" + get_guessed_word(secret_word, lettersGuessed) + "\n")

        # Show the player information about the game according to the project spec
        print("You have " + str(guesses_left) + " guesses left\n")

        # Ask the player to guess one letter per round and check that it is only one letter
        got_input = False
        while (got_input == False):
            guess = input("Please input your guess: ").lower()
            if len(guess) == 1 and guess.isalpha():
                got_input = True
            elif len(guess) < 1 or not guess.isalpha():
                print("Please guess a letter\n")
            elif len(guess) > 1:
                print("Please only guess one letter at a time\n")
            
        lettersGuessed.append(guess)

        # Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("\nCorrect!\n")
        else:
            guesses_left -= 1
            print("\nIncorrect.\n")

        # Check if the game has been won or lost
        if is_word_guessed(secret_word, lettersGuessed) or guesses_left == 0:
            game_over = True

    if is_word_guessed(secret_word, lettersGuessed):
        print("Congratulations! You win!\n")
    else:
        print("You lose. Better luck next time!\n")

    return input("Play again? (y/n) ")

def test():
    print(is_guess_in_word("a", "apple"))
    print(is_guess_in_word("F", "apple"))

    print(is_word_guessed("apple", ["a", "p", "l", "e"]))
    print(is_word_guessed("apple", ["a", "p", "l", "j", "q", "t"]))

    print(get_guessed_word("apple", ["p", "e"]))
    print(get_guessed_word("apple", ["l", "e", "a"]))

    spaceman("apple")


lettersGuessed = []
#These function calls that will start the game
while spaceman(load_word()).lower()[0] == "y":
    lettersGuessed = []

#test()
