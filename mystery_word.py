import random


def difficulty_level():
    while True:
        level = input("Do you want to play [E]asy mode, [N]ormal mode, or [H]ard mode? ")
        if not level:
            break
        if level.lower() == "e":
            return 4
        elif level.lower() == "n":
            return 6
        elif level.lower() == "h":
            return 8
        else:
            print("You did not make a valid choice.")
            continue


def choose_word():
    length_of_words = difficulty_level()
    easy_words = []
    normal_words = []
    hard_words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            if length_of_words == 4 and len(line) > 4 and len(line) <= 7:
                easy_words.append(line.strip())
            elif length_of_words == 6 and len(line) > 6 and len(line) <= 9:
                normal_words.append(line.strip())
            elif length_of_words == 8 and len(line) > 8:
                hard_words.append(line.strip().lower())
    if len(easy_words):
        return easy_words[random.randrange(len(easy_words))]
    elif len(normal_words):
        return normal_words[random.randrange(len(normal_words))]
    else:
        return hard_words[random.randrange(len(hard_words))]


def lines_for_word():
    word = choose_word()
    print("_ " * len(word))


# not working
def ask_for_letter():
    guessed_letters = []
    count = 1
    while count < 9:
        letter_guessed = input("What letter would you like to guess?  ").lower()
        if not letter_guessed.isalpha():
            print("That is not a valid choice.")
            continue
        elif len(letter_guessed) > 1:
            print("Only one letter at a time. Thank you!")
            continue
        elif letter_already_guessed(letter_guessed):
            guessed_letters.append(ask_for_letter())
        count += 1
        return letter


#not working
def letter_already_guessed(letter):
    if letter in guessed_letters:
        print("You already guessed that letter. Pick another letter.")
        return False
    else:
        return True
