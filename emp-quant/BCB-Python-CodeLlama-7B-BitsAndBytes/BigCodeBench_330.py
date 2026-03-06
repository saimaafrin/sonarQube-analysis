
import heapq
import random

def task_func(list_length: int, k: int):
    """
    Find the k largest numbers in a random-generated list using heapq.

    Args:
        list_length (int): The length of the list to be generated.
        k (int): The number of largest numbers to be found.

    Returns:
        tuple: A tuple containing two lists:
            list[int]: The randomly generated list of integers with the specified length.
            list[int]: The k largest numbers found using heapq.
    """
    # Generate a random list of integers
    random_list = [random.randint(1, 100) for _ in range(list_length)]

    # Find the k largest numbers using heapq
    largest_numbers = heapq.nlargest(k, random_list)

    return (random_list, largest_numbers)