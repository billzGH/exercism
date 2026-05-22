def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    number = input_base
    length = len(digits)
    counter = 0
    new_list = []
    for index, value in enumerate(digits):
        counter += (value * (number ** (length - 1 - index)))
    while counter // output_base != 0:
        new_list.append(counter % output_base)
        counter = counter // output_base
    new_list.append(counter)
    new_list.reverse()
    return new_list