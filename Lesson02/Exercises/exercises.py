"""
Lesson 2 In-Class Exercises
===========================

Completed practice for:
- Collections
- Nested dictionaries
- Indexing and slicing
- Control flow
- Functions and scope
- Rock-Paper-Scissors logic
"""

import random


# =============================
# Exercise 1: Collections Practice
# =============================

inventory = {
    "Laptop": {"price": 899.99, "stock": 5},
    "Mouse": {"price": 24.99, "stock": 10},
}

# Add one new product.
inventory["Keyboard"] = {"price": 49.99, "stock": 7}

# Update stock for one product.
inventory["Mouse"]["stock"] = 12

# Loop through inventory and print a summary.
for product, details in inventory.items():
    print(
        f"{product}: Price ${details['price']}, "
        f"Stock {details['stock']}"
    )


# =============================
# Exercise 2: Student Tracker
# =============================

students = {
    "Eli": {"grades": [90, 85, 95]},
    "Alice": {"grades": [88, 92, 84]},
}

# Add one student.
students["Bob"] = {"grades": [80, 85, 90]}

# Update one existing grade.
students["Eli"]["grades"][1] = 90

# Compute and print each student's average.
for student, details in students.items():
    grades = details["grades"]
    average = sum(grades) / len(grades)
    print(f"{student}'s average: {average:.2f}")


# =============================
# Exercise 3: Indexing and Slicing
# =============================

sentence = "Python is a useful programming language."

print(f"First 6 characters: {sentence[:6]}")
print(f"Last 9 characters: {sentence[-9:]}")
print(f"Every second character: {sentence[::2]}")


# =============================
# Exercise 4: Control Flow
# =============================

numbers = [10, -4, 0, 7, -2]

for number in numbers:
    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print(f"{number} is zero.")


# =============================
# Exercise 5: Function + Scope
# =============================

course_name = "MSITM.6341"


def summarize_student(name, grades):
    """
    Build a student summary with average grade.

    Args:
        name (str): Student name.
        grades (list[int | float]): Numeric grades.

    Returns:
        str: Summary line.
    """
    average = sum(grades) / len(grades)
    return f"{name} is enrolled in {course_name} with an average of {average:.2f}."


# =============================
# Exercise 6: Pseudo-code to Python
# =============================

"""
Pseudo-code for Rock, Paper, Scissors
1. Store valid choices.
2. Read player choice.
3. Randomly choose computer choice.
4. Compare choices to determine winner.
"""


def determine_rps_winner(player_choice, computer_choice):
    """
    Return round outcome for Rock-Paper-Scissors.

    Args:
        player_choice (str): User choice.
        computer_choice (str): Computer choice.

    Returns:
        str: "Player wins", "Computer wins", or "Tie".
    """
    if player_choice == computer_choice:
        return "Tie"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "Player wins"

    else:
        return "Computer wins"


if __name__ == "__main__":
    print()
    print(summarize_student("Eli", [90, 95, 88]))

    choices = ["Rock", "Paper", "Scissors"]
    player_choice = "Rock"
    computer_choice = random.choice(choices)

    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_rps_winner(player_choice, computer_choice))
