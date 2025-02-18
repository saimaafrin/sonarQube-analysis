from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Find the smallest and largest numbers
    smallest_number = numbers[0]
    largest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
        if number > largest_number:
            largest_number = number

    # Find the first number greater than the smallest number
    smallest_number_plus = smallest_number
    while True:
        smallest_number_plus += 0.1
        if smallest_number_plus > largest_number:
            break
        if smallest_number_plus in numbers:
            break

    # Find the first number less than the largest number
    largest_number_minus = largest_number
    while True:
        largest_number_minus -= 0.1
        if largest_number_minus < smallest_number:
            break
        if largest_number_minus in numbers:
            break

    # Return the closest pair in order
    if abs(smallest_number_plus - largest_number) < abs(smallest_number - largest_number):
        return (smallest_number, smallest_number_plus)
    else:
        return (largest_number_minus, largest_number)
