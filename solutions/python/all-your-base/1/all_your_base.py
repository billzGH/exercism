def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for d in digits:
        if 0 > d or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    n = input_base
    length = len(digits)
    counter = 0
    new_list = []
    for i, v in enumerate(digits):
        counter += (v * (n ** (length - 1 - i)))
    while counter // output_base != 0:
        new_list.append(counter % output_base)
        counter = counter // output_base
    new_list.append(counter)
    new_list.reverse()
    return new_list