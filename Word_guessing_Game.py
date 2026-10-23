import random
import re
from pathlib import Path


def read_words():
    words_file = Path(__file__).with_name("words.txt")

    if not words_file.exists():
        print("words.txt not found. Using built-in words instead.")
        return ["apple", "banana", "orange", "python", "planet", "guitar", "computer", "castle"]

    with words_file.open("r", encoding="utf-8") as file:
        words = [word.strip().lower() for word in file if word.strip()]

    return words


def display_word(secret_word, guessed_letters):
    word_to_display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += "_"

    print(word_to_display)


def get_guess(guessed_letters):
    while True:
        try:
            guess = input("Enter a letter: ").strip().lower()
        except EOFError:
            print("\nInput closed. Exiting the game.")
            raise SystemExit
        except KeyboardInterrupt:
            print("\nGame cancelled.")
            raise SystemExit

        if len(guess) != 1:
            print("Enter only one letter.")
        elif not re.fullmatch(r"[a-z]", guess):
            print("Enter only letters from a to z.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def is_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)


def main():
    words = read_words()
    if not words:
        print("No words loaded.")
        return

    secret_word = random.choice(words)
    attempts = 6
    guessed_letters = []

    print("Welcome to the Word Guessing Game!")
    print("Guess the secret word one letter at a time.")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        display_word(secret_word, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
            if is_word_guessed(secret_word, guessed_letters):
                print(f"Congratulations! You guessed the word: {secret_word}")
                return
        else:
            print("Wrong guess.")
            attempts -= 1

    print(f"Game over! The word was: {secret_word}")


if __name__ == "__main__":
    main()