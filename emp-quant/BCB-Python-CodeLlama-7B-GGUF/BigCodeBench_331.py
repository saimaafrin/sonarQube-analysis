
import bisect
import random

def task_func(num, list_length=5, min_value=0, max_value=0):
    """
    Insert a number into a randomly generated sorted list and return the new sorted list.

    Args:
        num (int): The number to be inserted into the list.
        list_length (int, optional): The length of the list. Defaults to 5.
        min_value (int, optional): The minimum value of the list. Defaults to 0.
        max_value (int, optional): The maximum value of the list. Defaults to 0.

    Returns:
        tuple: A tuple containing two lists:
            list[int]: The randomly generated list of integers with the specified length.
            list[int]: A new sorted list containing the original elements and the inserted number.
    """
    if max_value == 0:
        max_value = min_value + list_length
    list_of_ints = random.sample(range(min_value, max_value), list_length)
    list_of_ints.sort()
    bisect.insort(list_of_ints, num)
    return (list_of_ints, list_of_ints)