"""
Lesson 3 In-Class Exercises
===========================

Topics:
- Classes and objects
- Inheritance
- Encapsulation
- Modules
- Packages
- Polymorphism
"""

import os

import math_operations
from geometry import circle, rectangle

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# ========================
# Exercise 1: Classes and Objects
# ========================


class Book:
    """Represent one book with core metadata."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self):
        """
        Return one formatted summary string for the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}."


# ========================
# Exercise 2: Inheritance
# ========================


class Person:
    """Base class for person data."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        """Return base info text."""
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    """Subclass that adds student-specific data."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_info(self):
        """Return combined info including student ID."""
        return f"{super().get_info()}, Student ID: {self.student_id}"


# ========================
# Exercise 3: Encapsulation
# ========================


class BankAccount:
    """Practice private attributes and controlled updates."""

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# ========================
# Exercise 4: Working with Modules
# ========================

print("Addition:", math_operations.add(10, 5))
print("Subtraction:", math_operations.subtract(10, 5))
print("Multiplication:", math_operations.multiply(10, 5))
print("Division:", math_operations.divide(10, 5))


# ========================
# Exercise 5: Using Packages
# ========================

print("Circle area:", circle.area(5))
print("Circle circumference:", circle.circumference(5))

print("Rectangle area:", rectangle.area(10, 4))


# ========================
# Exercise 6: Polymorphism
# ========================


class Shape:
    """Base class for polymorphism exercise."""

    def area(self):
        return 0


class CircleShape(Shape):
    """Circle subclass."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class RectangleShape(Shape):
    """Rectangle subclass."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":

    # Exercise 1
    book = Book("Python Basics", "John Smith", 2026)
    print(book.book_info())

    # Exercise 2
    person = Person("Eli", 40)
    student = Student("Eli", 40, "S12345")

    print(person.get_info())
    print(student.get_info())

    # Exercise 3
    account = BankAccount("Eli", 1000)

    print(f"Starting balance: ${account.get_balance()}")

    account.deposit(500)
    print(f"After deposit: ${account.get_balance()}")

    account.withdraw(200)
    print(f"After withdrawal: ${account.get_balance()}")

    # Exercise 6
    shapes = [
        Shape(),
        CircleShape(5),
        RectangleShape(10, 4)
    ]

    for shape in shapes:
        print(f"Shape area: {shape.area()}")
