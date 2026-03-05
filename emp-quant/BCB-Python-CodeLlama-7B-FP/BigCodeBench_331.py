import bisect
import random
def task_func(num, list_length = 5, min_value = 0, max_value = 0):
    """
    Insert a number into a randomly generated sorted list and return the new sorted list.

    Args:
        num (int): The number to be inserted into the list.
        list_length (int, optional): The length of the randomly generated list. Defaults to 5.
        min_value (int, optional): The minimum value of the randomly generated list. Defaults to 0.
        max_value (int, optional): The maximum value of the randomly generated list. Defaults to 0.

    Returns:
        tuple: A tuple containing two lists:
            list[int]: The randomly generated list of integers with the specified length.
            list[int]: A new sorted list containing the original elements and the inserted number.
    """
    # Generate a random list of integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    random_list.sort()

    # Insert the number into the list
    bisect.insort(random_list, num)

    # Return the new sorted list
    return (random_list, random_list)