import heapq
import random
def task_func(k, list_length=5, min_value=0, max_value=100):
    # Generate a list of random integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    
    # Find the k smallest numbers using heapq
    k_smallest = heapq.nsmallest(k, random_list)
    
    # Return the results as a tuple
    return (random_list, k_smallest)
k = 3
list_length = 10
min_value = 0
max_value = 50