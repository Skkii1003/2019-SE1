def filter_even_numbers(numbers):
    evennumbers = []

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            evennumbers.append(numbers[i])
    return evennumbers
