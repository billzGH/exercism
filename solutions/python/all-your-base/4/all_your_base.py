"""
Exercism function to rebase a sequence of digits
"""

from functools import reduce

def rebase(input_base, digits, output_base):
    """
    This function converts a sequence of digits in one base, representing a number,
    into a sequence of digits in another base, representing the same number.
    """
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    output_digits = []
    counter = reduce(lambda acc, d: acc * input_base + d, digits, 0)
    
    while counter // output_base != 0:
        output_digits.append(counter % output_base)
        counter = counter // output_base
    output_digits.append(counter)
    output_digits.reverse()
    
    return output_digits