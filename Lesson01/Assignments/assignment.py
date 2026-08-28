"""
Lesson 1 Assignment: Python Basics
==================================

Synchronized topics:
- Variables, data types, and operators
- Conditionals and basic function design
"""


# =============================
# Task 1: Simple Calculator
# =============================


def calculate(num_one, num_two, operator):
    """
    Calculate a result using two numbers and one operator.

    Args:
        num_one (float): First number.
        num_two (float): Second number.
        operator (str): Arithmetic operator (+, -, *, /).

    Returns:
        float | str: Numeric result or a friendly error message.
    """

    if operator == "+":
        return num_one + num_two

    elif operator == "-":
        return num_one - num_two

    elif operator == "*":
        return num_one * num_two

    elif operator == "/":
        if num_two == 0:
            return "Error: Cannot divide by zero."
        return num_one / num_two

    else:
        return "Error: Invalid operator."


# =============================
# Task 2: Area of a Rectangle
# =============================


def rectangle_area(length, width):
    """
    Return the area of a rectangle.

    Args:
        length (float): Rectangle length.
        width (float): Rectangle width.

    Returns:
        float | str: Computed area or an error message.
    """

    if length <= 0 or width <= 0:
        return "Error: Length and width must be positive numbers."

    return length * width


if __name__ == "__main__":

    # =============================
    # Task 1: Calculator Input
    # =============================

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    math_operator = input("Enter an operator (+, -, *, /): ")

    calculation_result = calculate(
        first_number,
        second_number,
        math_operator
    )

    print(f"Calculator result: {calculation_result}")

    # =============================
    # Task 2: Rectangle Input
    # =============================

    rectangle_length = float(input("Enter the rectangle length: "))
    rectangle_width = float(input("Enter the rectangle width: "))

    area_result = rectangle_area(
        rectangle_length,
        rectangle_width
    )

    print(f"Rectangle area: {area_result}")