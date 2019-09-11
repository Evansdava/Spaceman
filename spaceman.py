import random


def load_word(mode):
    """
    A function that reads a text file of words and randomly selects one to use
    as the secret word from the list.

    Args:
        mode (int): The type of return to be used. 0 is default, returning
        a single, random, mystery word. 1 is the list of words used

    Returns:
        string: The secret word to be used in the spaceman guessing game
        used if mode == 0
        list: The list of possible words, used if mode == 1

    """
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    if mode == 0:
        return secret_word
    elif mode == 1:
        return words_list


def sinister_spaceman(secret_word, letters_guessed):
    """
    A function that resets the secret word after each correct guess.

    Args:
        secret_word (string): The random word the user is trying to guess.
        letters_guessed (list of strings): The list of letters that have been
        guessed so far.

    Returns:
        string: A word that has all the same letters guessed as the current
        secret word.

    """
    # Load the list of possible words
    words_list = load_word(1)

    # Trim list of words down to only words which match the length of the
    # secret word
    index = 0
    while index < len(words_list):
        if len(words_list[index]) != len(secret_word):
            words_list.pop(index)
        else:
            index += 1

    # Determine which letters have been guessed, removing whitespace
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    guessed_word = guessed_word.replace(" ", "").lower()

    # Pare down the list of possible words based on what's been guessed
    char = 0
    for letter in guessed_word:
        index = 0
        if letter != "_":
            while index < len(words_list):
                if words_list[index][char] != letter:
                    words_list.pop(index)
                else:
                    index += 1
        char += 1

    # Return a random possible word
    return random.choice(words_list)


def is_word_guessed(secret_word, letters_guessed):
    """
    A function that checks if all the letters of the secret word have been
    guessed.

    Args:
        secret_word (string): The random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in
        letters_guessed, False otherwise

    """
    # Loop through the letters in the secret_word and check if a letter is not
    # in letters_guessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    # Only reached if no letters have been shown to be false
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    A function that is used to get a string showing the letters guessed so far
    in the secret word and underscores for letters that have not been guessed
    yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user
        has guessed correctly, the string should contain the letter at the
        correct position.  For letters in the word that the user has not yet
        guessed, shown an _ (underscore) instead.

    """

    # Loop through the letters in secret word and build a string that shows the
    # letters that have been guessed correctly so far that are saved in
    # letters_guessed and underscores for the letters that have not been
    # guessed yet
    output = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output += letter.upper() + " "
        else:
            output += "_ "

    return output


def is_guess_in_word(guess, secret_word):
    """
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    """
    # Check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False


def spaceman(secret_word):
    """
    A function that controls the game of spaceman. Will start spaceman in the
    command line.

    Args:
      secret_word (string): the secret word to guess.

    """
    # The user gets as many guesses as letters in the word, with a minimum of 5
    guesses_left = len(secret_word)
    if guesses_left < 5:
        guesses_left = 5
    game_over = False
    letters_guessed = []

    print(f"""
            Welcome to Spaceman! You will have to guess a mystery word, one
            letter at a time. You have {str(guesses_left)} guesses to do so.
            The word changes every time you correctly guess, so watch out!
            Don't worry though, you don't have to re-guess any letters, that's
            done for you.

            Good luck!""")
    input("""
            Press enter/return to begin
            """)

    while (game_over is False):
        # Show the guessed word so far
        print("\n" + get_guessed_word(secret_word, letters_guessed) + "\n")

        # Show the player information about the game according to the project
        # spec
        print(f"You have {str(guesses_left)} guesses left\n")

        # Show the letters that have already been guessed
        # Syntax from ewall on Stack Overflow
        # https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically
        print(f"You have already guessed: ", end=" ")
        for letter in sorted(letters_guessed):
            print(letter.upper(), sep=" ", end=" ", flush=True)
        print("\n")

        # Ask the player to guess one letter per round and check that it is
        # only one letter
        got_input = False
        while (got_input is False):
            guess = input("Please input your guess: ").lower()
            if len(guess) < 1 or not guess.isalpha():
                print("Please guess a letter\n")
            elif len(guess) > 1:
                print("Please only guess one letter at a time\n")
            elif guess in letters_guessed:
                print("You've already guessed that letter\n")
            elif len(guess) == 1 and guess.isalpha():
                got_input = True

        letters_guessed.append(guess)

        # Check if the guessed letter is in the secret or not and give the
        # player feedback
        if is_guess_in_word(guess, secret_word):
            print("\nCorrect!\n")
            secret_word = sinister_spaceman(secret_word, letters_guessed)
        else:
            guesses_left -= 1
            print("\nIncorrect.\n")

        # Check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed) or guesses_left == 0:
            game_over = True

    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations! You win!\n")
    else:
        print("You lose. Better luck next time!\n")

    print(f"The word was {secret_word.upper()} \n")

    return input("Play again? (y/n) ")


def test():
    print(is_guess_in_word("a", "apple"))
    print(is_guess_in_word("F", "apple"))

    print(is_word_guessed("apple", ["a", "p", "l", "e"]))
    print(is_word_guessed("apple", ["a", "p", "l", "j", "q", "t"]))

    print(get_guessed_word("apple", ["p", "e"]))
    print(get_guessed_word("apple", ["l", "e", "a"]))

    print(sinister_spaceman("apple", ["a", "e"]))
    print(sinister_spaceman("apple", ["a", "p"]))
    print(sinister_spaceman("apple", ["e", "l"]))

    # spaceman("apple")


# test()

# Run the game as long as the user inputs "yes" or a variant thereof after
# playing
while spaceman(load_word(0)).lower()[0] == "y":
    pass
