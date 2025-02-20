from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """

    # create empty list
    result: List[int] = []

    # create range with a and b
    range_list: List[int] = list(range(a, b+1))

    # append numbers from range to result
    for number in range_list:
        # create string of number
        number_string: str = str(number)

        # iterate through number string
        for digit in number_string:
            # convert digit to int
            digit: int = int(digit)

            # if number is even
            if digit % 2 == 0:
                # append number to result
                result.append(digit)

    # return list of even integers from a to b
    return result
