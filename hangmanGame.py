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
stage_1 = "x-------x"
stage_2 = stage_1 + "\n|\n|\n|\n|\n|"
stage_3 = stage_1 + "\n|       |\n|       0\n|\n|\n|"
stage_4 = stage_1 + "\n|       |\n|       0\n|       |\n|\n|"
stage_5 = stage_1 + "\n|       |\n|       0\n|      /|\\\n|\n|"
stage_6 = stage_1 + "\n|       |\n|       0\n|      /|\\\n|      / \n|"
stage_7 = stage_1 + "\n|       |\n|       0\n|      /|\\\n|      / \\\n|"

# print(stage_1)
# print(stage_2)
# print(stage_3)
# print(stage_4)
# print(stage_5)
# print(stage_6)
# print(stage_7)


guess_word = input("Guess a word: (one word , no spaces) ")

size_word = len(guess_word)

print("_ "*size_word)

guess_input = input("Guess a letter: ")

guess_input = guess_input.lower()


size_guess_char = len(guess_input)


if (size_guess_char > 1) and not(guess_input.isalpha()):
    print("E3")
elif not(guess_input.isalpha()):
    print("E2")
elif size_guess_char > 1:
    print("E1")
else:
    print(guess_input)
