import random

def open_word_dict():
    words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            words.append(line.strip().lower())
    return words


def difficulty_level():
    while True:
        level = input("Do you want to play [E]asy mode, [M]edium mode, or [H]ard mode? ")
        if not level:
            break
        elif level.lower() == "e":
            return 'e'
        elif level.lower() == "m":
            return 'm'
        elif level.lower() == "h":
            return 'h'
        else:
            print("You did not make a valid choice.")
            continue


def easy_words(word_list):
    return [word for word in word_list if len(word) >= 4 and len(word) <= 6]


def medium_words(word_list):
    return [word for word in word_list if len(word) >= 6 and len(word) <= 8]


def hard_words(word_list):
    return [word for word in word_list if len(word) >= 8]


def random_word(word_list):
    difficulty_level()
    if 'e':
        easy_word_list = easy_words(word_list)
        return easy_word_list[random.randrange(len(easy_word_list))]
    elif 'm':
        medium_word_list = medium_words(word_list)
        return medium_word_list[random.randrange(len(medium_word_list))]
    else:
        hard_word_list = hard_words(word_list)
        return hard_word_list[random.randrange(len(hard_word_list))]


def display_word(word, guesses):
    board = []
    for letter in word:
        board.append("_")
    for idx, letter in enumerate(list(word)):
        if letter in guesses:
            board[idx] = letter.upper()
        return ' '.join(board)
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    # TODO
    pass


def ask_for_letter(random_word(open_word_dict())):
    secret_word = random_word(open_word_dict)
    good_guesses = []
    bad_guesses = []
    tries_left = 8
    while tries_left < 0:
        letter_guessed = input("What letter would you like to guess?  ").lower()
        if not letter_guessed.isalpha():
            print("That is not a valid choice.")
            continue
        elif len(letter_guessed) > 1:
            print("Only one letter at a time. Thank you!")
            continue
        elif letter_guessed in good_guesses or letter_guessed in bad_guesses:
            print("You alredy guessed that letter! Try agian.")
            continue
        elif letter_guessed in secret_word:
            good_guesses.append(letter_guessed)
        else:
            bad_guesses.append(letter_guessed)
        tries_left -= 1
        return letter_guessed


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    # TODO
    pass


def main():
    random_word(open_word_dict)
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """



if __name__ == '__main__':
    main()

# not working



#not working
def letter_already_guessed(letter):
    if letter in guessed_letters:
        print("You already guessed that letter. Pick another letter.")
        return False
    else:
        return True
