import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Galgje!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Raad een letter of woord! ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("U heeft deze letter al geraden", guess)
            elif guess not in word:
                print(guess, "is niet in het woord!.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Gefeliciteerd,", guess, "is in het woord")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("U heeft het woord al geraden.", guess)
            elif guess != word:
                print(guess, "is niet het woord.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Fout!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("U heeft het woord geraden!")
    else:
        print("Het woord was " + word + ".")


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,

                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Opnieuw? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
