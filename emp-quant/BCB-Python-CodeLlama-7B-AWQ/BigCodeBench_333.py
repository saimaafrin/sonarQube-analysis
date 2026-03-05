import heapq
import random
def task_func(k, list_length = 5, min_value = 0, max_value = 100):
    """
    Generates a list of random integers and returns the k smallest numbers using heapq.

    Args:
        k (int): The number of smallest numbers to return.
        list_length (int, optional): The length of the list to generate. Defaults to 5.
        min_value (int, optional): The minimum value in the list. Defaults to 0.
        max_value (int, optional): The maximum value in the list. Defaults to 100.

    Returns:
        tuple: A tuple containing two lists:
            list[int]: The randomly generated list of integers with the specified length.
            list[int]: The k smallest numbers found using heapq.
    """
    # Generate a list of random integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]

    # Use heapq to find the k smallest numbers
    k_smallest = heapq.nsmallest(k, random_list)

    return (random_list, k_smallest)