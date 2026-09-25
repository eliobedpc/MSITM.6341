"""
Lesson 3 Assignment: OOP and Modules Refactor
=============================================

Synchronized topics:
- Classes and objects
- Encapsulation
- Modules and imports

Objective:
- Refactor a command-line game using class-based design
  and simple logging.
"""

import random


class GameManager:
    """
    Manage game state and round flow.
    """

    def __init__(self):
        """Initialize game configuration and score tracking."""
        self.user_score = 0
        self.computer_score = 0
        self.round_count = 0
        self.valid_choices = ["Rock", "Paper", "Scissors"]

    def play_round(self, user_choice):
        """
        Process one round and update state.

        Args:
            user_choice (str): Player input.

        Returns:
            str: Round result string.
        """

        computer_choice = random.choice(self.valid_choices)
        self.round_count += 1

        if user_choice == computer_choice:
            result = "Tie"

        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "Player wins"
            self.user_score += 1

        else:
            result = "Computer wins"
            self.computer_score += 1

        return (
            f"Round {self.round_count}: "
            f"You chose {user_choice}, "
            f"Computer chose {computer_choice}. "
            f"{result}."
        )

    def summary(self):
        """
        Return final game summary text.

        Returns:
            str: Summary for player and computer score.
        """

        return (
            f"Final Score - "
            f"Player: {self.user_score}, "
            f"Computer: {self.computer_score}, "
            f"Rounds Played: {self.round_count}"
        )


class Logger:
    """
    Simple text logger for assignment events.
    """

    def __init__(self, filename):
        """
        Store output log filename.

        Args:
            filename (str): Log file path.
        """
        self.filename = filename

    def write_line(self, message):
        """
        Append one message line to the log file.

        Args:
            message (str): Text line to write.
        """

        with open(self.filename, "a") as log_file:
            log_file.write(message + "\n")


def main():
    """
    Entry point for your class-based assignment.
    """

    game = GameManager()
    logger = Logger("game_log.txt")

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = input(
            "Choose Rock, Paper, or Scissors: "
        ).capitalize()

        if user_choice not in game.valid_choices:
            print("Invalid choice. Please try again.")
            continue

        result = game.play_round(user_choice)

        print(result)
        logger.write_line(result)

        play_again = input(
            "Would you like to play again? (yes/no): "
        ).lower()

        if play_again != "yes":
            break

    final_summary = game.summary()

    print(final_summary)
    logger.write_line(final_summary)


if __name__ == "__main__":
    main()
