HANGMAN_ASCII_ART = """Welcome to the Hangman Game!
                    \t __    __
                    \t|  |  |  |
                    \t|  |__|  | __ _ _ __   ___ _  _  ___  ___    __ _ _ ___
                    \t|   __   |/ _` |  _ \\ / _ ` |  '_   `  _  \\ / _` | ' _ \\
                    \t|  |  |  | (_| | | | | (_|  |  |  |  |  |  | (_| | |  | |
                    \t|__|  |__|\\__,_|_| |_|\\__,  | _|  |__|  |__|\\__,_|_|  |_|
                    \t\t\t               __/  |
                    \t\t\t              |_____/"""

MAX_TRIES = 6

print(HANGMAN_ASCII_ART)


# the rode stages
HANGMAN_PHOTOS = {
    "1": "x-------x",
    "2": "x-------x\n|\n|\n|\n|\n|",
    "3": "x-------x\n|       |\n|       0\n|\n|\n|",
    "4": "x-------x\n|       |\n|       0\n|       |\n|\n|",
    "5": "x-------x\n|       |\n|       0\n|      /|\\\n|\n|",
    "6": "x-------x\n|       |\n|       0\n|      /|\\\n|      / \n|",
    "7": "x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"
}

guess_word = input("Guess a word (one word , no spaces) : ")

size_word = len(guess_word)

print("_ " * size_word)

guess_input = input("Guess a letter: ")


def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and not (letter_guessed in old_letters_guessed):
        return True
    return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()

    if (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        print("Add successfully.")
        return True

    else:
        print("X\n" + ' -> '.join(sorted(old_letters_guessed)))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    str_res = list("_" * len(secret_word))
    for i in old_letters_guessed:
        if i in secret_word:
            temp = []
            for pos, char in enumerate(secret_word):
                if char == i:
                    temp.append(pos)
            for index in temp:
                str_res[index] = i

    return " ".join(str_res)


def check_win(secret_word, old_letters_guessed):
    temp = show_hidden_word(secret_word, old_letters_guessed)
    temp = temp.replace(" ", "")
    return temp == secret_word


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[str(num_of_tries)])
