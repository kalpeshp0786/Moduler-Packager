"""
Custom Mathematical Utility Module
"""

import math
import random
import string


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return math.factorial(number)


def compound_interest(principal, rate, time):
    if principal < 0:
        raise ValueError("Principal cannot be negative.")

    if rate < 0:
        raise ValueError("Rate cannot be negative.")

    if time < 0:
        raise ValueError("Time cannot be negative.")

    amount = principal * (1 + rate / 100) ** time

    return amount


def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    return math.pi * radius ** 2


def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")

    return length * width


def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")

    return 0.5 * base * height


def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits + "!@#$%&*?"

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%&*?")
    ]

    for i in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)