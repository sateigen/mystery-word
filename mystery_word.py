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
        if letter in guesses:
            board.append(letter.upper() + ' ')
        else:
            board.append("_ ")
    print(''.join(board).strip())
    return ''.join(board).strip()


def ask_for_letter(word):
    good_guesses = []
    bad_guesses = []
    tries_left = 8
    while tries_left > 0:
        letter_guessed = input("What letter would you like to guess?  ").lower()
        if not letter_guessed.isalpha():
            print("That is not a valid choice.")
        elif len(letter_guessed) > 1:
            print("Only one letter at a time. Thank you!")
        elif letter_guessed in good_guesses or letter_guessed in bad_guesses:
            print("You alredy guessed that letter! Try agian.")
        elif letter_guessed in word:
            good_guesses.append(letter_guessed)
            return letter_guessed
        else:
            bad_guesses.append(letter_guessed)
            tries_left -= 1


def is_word_complete(word, guesses):
    complete_word = []
    for letter in word:
        if letter in guesses:
            complete_word.append(letter)
    complete_word = sorted(complete_word)
    word = sorted(list(word))
    if complete_word == word:
        return True
    else:
        return False


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



# if __name__ == '__main__':
#     main()
