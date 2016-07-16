import os
import random
import sys

def open_word_dict():
    words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            words.append(line.strip().lower())
    return words


def easy_words(word_list):
    return [word for word in word_list if len(word) >= 4 and len(word) <= 6]


def medium_words(word_list):
    return [word for word in word_list if len(word) >= 6 and len(word) <= 8]


def hard_words(word_list):
    return [word for word in word_list if len(word) >= 8]


def random_word(word_list):
    clear_screen()
    while True:
        level = input("Do you want to play [E]asy mode, [N]ormal mode, or [H]ard mode? ")
        if level.lower() == "e":
            easy_word_list = easy_words(word_list)
            return easy_word_list[random.randrange(len(easy_word_list))]
        elif level.lower() == "n":
            medium_word_list = medium_words(word_list)
            return medium_word_list[random.randrange(len(medium_word_list))]
        elif level.lower() == "h":
            hard_word_list = hard_words(word_list)
            return hard_word_list[random.randrange(len(hard_word_list))]
        else:
            print("You did not make a valid choice.")
            continue


def display_word(word, guesses):
    clear_screen()
    board = []
    print('')
    for letter in word:
        if letter in guesses:
            board.append(letter.upper() + ' ')
        else:
            board.append("_ ")
    print(''.join(board).strip())
    return ''.join(board).strip()


def ask_for_letter(word):
    # clear_screen()
    good_guesses = []
    bad_guesses = []
    tries_left = 8
    while tries_left > 0 :
        print('*' * 30)
        print("\nTries Left: {}".format(tries_left))
        print("Letters not in my word: {}".format(', '.join(bad_guesses)))
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
        elif letter_guessed in word:
            good_guesses.append(letter_guessed)
            print(good_guesses)
        else:
            print("That letter is not in my word.")
            bad_guesses.append(letter_guessed)
            tries_left -= 1

        display_word(word, good_guesses)
        if is_word_complete(word, good_guesses):
            print("YOU WIN! You guessed my word!")
            play_again()
    if len(bad_guesses) == 8:
        print("I WIN! You did not guess my word. It was {}.".format(word))
        play_again()


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


def play_again():
    play_again = input("Do you want to play again? Y/n ").lower()
    if play_again == 'y':
        main()
    else:
        print("\nThanks for playing!\n")
        sys.exit()


def game_directions():
    print("\nWelcome to the Mystery Word Game.")
    print("I will pick a random word that you will have to guess.")
    print("You may only guess one letter at a time, and your guess must be a letter.")
    print("If you guess every letter in the word with less than 8 mistakes, you win!\n")
    print("Easy mode includes words between 4 and 6 letters long.")
    print("Normal mode includes words between 6 and 8 letters long.")
    print("Hard mode includes words that are 8 letters or longer.\n")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    game_directions()
    is_playing = input("Press any key to begin playing, or 'Q' to quit.")
    if is_playing == 'q':
        sys.exit()
    else:
        answer = random_word(open_word_dict())
        print("My word has {} letters in it. Good luck!\n".format(len(answer)))
        ask_for_letter(answer)
        clear_screen()


if __name__ == '__main__':
    main()
