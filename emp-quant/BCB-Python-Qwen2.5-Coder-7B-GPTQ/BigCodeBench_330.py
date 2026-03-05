import heapq
import random
def task_func(list_length: int, k: int):
    # Generate a random list of integers
    random_list = [random.randint(1, 100) for _ in range(list_length)]
    
    # Find the k largest numbers using heapq
    k_largest = heapq.nlargest(k, random_list)
    
    return random_list, k_largest
list_length = 10
k = 3