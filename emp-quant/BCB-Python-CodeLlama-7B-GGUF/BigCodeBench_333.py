
import heapq
import random

def task_func(k, list_length=5, min_value=0, max_value=100):
    """
    Generate a list of random integers and find the k smallest numbers using heapq.

    Args:
        k (int): The number of smallest numbers to find.
        list_length (int, optional): The length of the list to generate. Defaults to 5.
        min_value (int, optional): The minimum value in the list. Defaults to 0.
        max_value (int, optional): The maximum value in the list. Defaults to 100.

    Returns:
        tuple: A tuple containing two lists:
            list[int]: The randomly generated list of integers.
            list[int]: The k smallest numbers found using heapq.
    """
    # Generate a list of random integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]

    # Find the k smallest numbers using heapq
    smallest_numbers = heapq.nsmallest(k, random_list)

    return (random_list, smallest_numbers)

random_list, smallest_numbers = task_func(k, list_length, min_value, max_value)

print(f"Random list: {random_list}")
print(f"Smallest numbers: {smallest_numbers}")