
import heapq
import random

def task_func(list_length: int = 5, k: int = 3):
    # Generate a random list of integers
    random_list = [random.randint(1, 100) for _ in range(list_length)]
    
    # Find the k largest numbers using heapq.nlargest
    k_largest_numbers = heapq.nlargest(k, random_list)
    
    return (random_list, k_largest_numbers)