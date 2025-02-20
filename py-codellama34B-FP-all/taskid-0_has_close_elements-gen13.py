from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """


    # sorting list of numbers
    numbers.sort()

    # iterating through list and comparing each element to it's successor
    for index in range(len(numbers) - 1):

        # if difference between element and it's successor is less or equal to threshold
        # return True
        if numbers[index + 1] - numbers[index] <= threshold:
            return True

    # if difference between each element and it's successor is greater than threshold
    # return False
    return False
