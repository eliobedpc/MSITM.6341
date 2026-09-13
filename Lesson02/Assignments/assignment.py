"""
Lesson 2 Assignment: Rock-Paper-Scissors
========================================

Synchronized topics:
- Collections, conditionals, loops, and functions
- Translating pseudo-code into runnable logic

Important:
- This file is a scaffold only.
- Implement the TODO logic yourself.
"""

import random


# =============================
# Assignment Prompt
# =============================
"""
Build a Rock-Paper-Scissors game where a user plays against the computer.

Required behavior:
1. Validate user input.
2. Generate random computer choices.
3. Decide the winner for each round.
4. Support multiple rounds.
5. Track and print final score.
"""


# =============================
# Pseudo-code
# =============================
"""
1. Start program and show game rules.
2. Create a list: ["Rock", "Paper", "Scissors"].
3. Repeat until player quits:
   a. Ask player for a choice.
   b. Validate input.
   c. Randomly choose computer option.
   d. Compare choices and determine winner.
   e. Update score counters.
4. Print final score summary.
"""


def play_round(user_choice, computer_choice):
    """
    Determine the outcome of one game round.

    Args:
        user_choice (str): Player choice.
        computer_choice (str): Computer choice.

    Returns:
        str: "win", "lose", or "tie".
    """
    if user_choice == computer_choice:
        return "tie"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "win"

    else:
        return "lose"


def get_user_choice(valid_choices):
    """
    Collect and validate one user choice.

    Args:
        valid_choices (list[str]): Allowed options.

    Returns:
        str: Valid player choice.
    """
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()

        if user_choice in valid_choices:
            return user_choice

        print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def run_game():
    """
    Manage the full multi-round game flow.

    Returns:
        None
    """
    choices = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")

    while True:
        print()

        user_choice = get_user_choice(choices)
        computer_choice = random.choice(choices)

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = play_round(user_choice, computer_choice)

        if result == "win":
            print("You win this round!")
            user_score += 1

        elif result == "lose":
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("This round is a tie!")

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("Would you like to play again? (yes/no): ").lower()

        if play_again != "yes":
            break

    print()
    print("Final Score")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print("You won the game!")
    elif computer_score > user_score:
        print("The computer won the game!")
    else:
        print("The game ended in a tie!")


if __name__ == "__main__":
    run_game()
