from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    # create a dictionary to count the numbers of even and odd numbers
    num_dict = {
        0: 0,
        1: 0,
        -1: 0,
    }
    # iterate through the string representation of the number
    # check if each number is even or odd and update the dictionary
    for digit in str(num):
        if int(digit) % 2 == 0:
            num_dict[0] += 1
        else:
            num_dict[1] += 1
    # return the number of even and odd numbers
    return num_dict[0], num_dict[1]
