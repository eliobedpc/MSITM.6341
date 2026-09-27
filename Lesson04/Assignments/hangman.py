"""
Lesson 4 Group Assignment: Hangman
Main Script
=================================

This file controls the main game flow and replay option.
"""

from hangman_helpers import (
    WORD_LIST,
    choose_word,
    display_word,
    process_guess,
)


def play_hangman():
    """
    Coordinate one full game round.

    Pseudo-code:
    1. Choose a secret word.
    2. Create an empty set of guessed letters.
    3. Set the number of tries.
    4. Show the hidden word.
    5. Ask the player for one letter.
    6. Validate the player's input.
    7. Update guessed letters and tries.
    8. Repeat until the player wins or runs out of tries.
    """

    secret_word = choose_word(WORD_LIST)
    guessed_letters = set()
    tries_left = 6

    print("\nWelcome to Hangman!")
    print("Guess the secret word one letter at a time.")
    print(f"You have {tries_left} incorrect tries.\n")

    while tries_left > 0:
        current_display = display_word(secret_word, guessed_letters)

        print("Word:", current_display)
        print(f"Tries left: {tries_left}")

        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Check for a win before asking for another guess.
        if "_" not in current_display:
            print("\nCongratulations! You guessed the word!")
            print(f"The word was: {secret_word}")
            return

        guess = input("Enter one letter: ").lower().strip()

        # Input validation.
        if len(guess) != 1:
            print("Please enter only one letter.\n")
            continue

        if not guess.isalpha():
            print("Please enter a letter from A-Z.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        old_tries = tries_left
        guessed_letters, tries_left = process_guess(
            secret_word,
            guessed_letters,
            guess,
            tries_left,
        )

        if tries_left < old_tries:
            print(f"Sorry, '{guess}' is not in the word.\n")
        else:
            print(f"Good guess! '{guess}' is in the word.\n")

    # The loop ends when no tries remain.
    print("\nGame over!")
    print(f"The secret word was: {secret_word}")


if __name__ == "__main__":
    # Replay loop.
    while True:
        play_hangman()

        replay = input(
            "\nWould you like to play again? (yes/no): "
        ).lower().strip()

        if replay != "yes":
            print("Thanks for playing Hangman!")
            break
