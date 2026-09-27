"""
Lesson 4 Group Assignment: Hangman
Helper Module
=================================

Reusable functions for:
- Choosing a secret word
- Displaying the hidden word
- Processing player guesses
"""

import random


# Combined word lists from the group contributions.
WORD_LIST = [
    "apple",
    "soccer",
    "school",
    "pizza",
    "family",
    "summer",
    "music",
    "travel",
    "coffee",
    "garden",
    "python",
    "computer",
    "programming",
    "keyboard",
    "internet",
    "function",
    "variable",
    "software",
    "database",
    "algorithm",
]


def choose_word(word_list):
    """
    Select a secret word.

    Args:
        word_list (list[str]): Candidate words.

    Returns:
        str: Secret word.

    Pseudo-code:
    1. Receive a list of possible words.
    2. Randomly select one word from the list.
    3. Return the selected word.
    """
    return random.choice(word_list)


def display_word(secret_word, guessed_letters):
    """
    Build display text with underscores for missing letters.

    Args:
        secret_word (str): Target word.
        guessed_letters (set[str]): Guessed characters.

    Returns:
        str: Display form of the word.

    Pseudo-code:
    1. Create an empty display list.
    2. Check each letter in the secret word.
    3. Show the letter if it has been guessed.
    4. Otherwise show an underscore.
    5. Join and return the display.
    """
    display = []

    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")

    return " ".join(display)


def process_guess(secret_word, guessed_letters, guess, tries_left):
    """
    Update state based on a user guess.

    Args:
        secret_word (str): Target word.
        guessed_letters (set[str]): Existing guesses.
        guess (str): New guess from user.
        tries_left (int): Remaining attempts.

    Returns:
        tuple[set[str], int]: Updated guessed set and tries left.

    Pseudo-code:
    1. Check whether the letter was already guessed.
    2. If not, add it to the guessed letters.
    3. If the guess is not in the secret word, remove one try.
    4. Return the updated guessed letters and tries.
    """
    if guess in guessed_letters:
        return guessed_letters, tries_left

    guessed_letters.add(guess)

    if guess not in secret_word:
        tries_left -= 1

    return guessed_letters, tries_left
