"""Exercism function to rebase a sequence of digits."""

from functools import reduce


def rebase(input_base, digits, output_base):
    """Convert a sequence of digits from one base to another."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    counter = 0
    for digit in digits:
        counter = counter * input_base + digit

    output_digits = []
    while counter:
        counter, remainder = divmod(counter, output_base)
        output_digits.append(remainder)
    output_digits.reverse()

    return output_digits or [0]