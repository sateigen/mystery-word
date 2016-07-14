import random


def difficulty_level():
    while True:
        level = input("Do you want to play [E]asy mode, [N]ormal mode, or [H]ard mode?")
        if not level:
            break
        if level.lower() == "e":
            easy_words()
            return easy_words
        elif level.lower() == "n":
            normal_words()
            return normal_words
        elif level.lower() == "h":
            hard_words()
            return hard_words
        else:
            print("You did not make a valid choice.")
            continue


def easy_words():
    easy_words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            if len(line) > 4 and len(line) <= 7:
                easy_words.append(line)
    return easy_words[random.randrange(len(easy_words))]


def normal_words():
    normal_words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            if len(line) > 6 and len(line) <= 9:
                normal_words.append(line)
    return normal_words[random.randrange(len(normal_words)]


def hard_words():
    hard_words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            if len(line) > 8:
                hard_words.append(line)
    return hard_words[random.randrange(len(hard_words))]
