import heapq
import random
def task_func(k, list_length=5, min_value=0, max_value=100):
    """
    Find the k smallest numbers in a randomly generated list using heapq.

    Args:
        k (int): The number of smallest numbers to find.
        list_length (int, optional): The length of the randomly generated list. Defaults to 5.
        min_value (int, optional): The minimum value in the randomly generated list. Defaults to 0.
        max_value (int, optional): The maximum value in the randomly generated list. Defaults to 100.

    Returns:
        tuple: A tuple containing two lists:
            list[int]: The randomly generated list of integers with the specified length.
            list[int]: The k smallest numbers found using heapq.
    """
    # Generate a list of random integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]

    # Find the k smallest numbers using heapq
    k_smallest = heapq.nsmallest(k, random_list)

    return (random_list, k_smallest)
k = 3
list_length = 5
min_value = 0
max_value = 100
random_list = [random.randint(min_value, max_value) for _ in range(list_length)]
k_smallest = heapq.nsmallest(k, random_list)