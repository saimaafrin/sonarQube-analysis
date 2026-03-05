
import heapq
import random

def task_func(k, list_length = 5, min_value = 0, max_value = 100):
    list_of_numbers = [random.randint(min_value, max_value) for i in range(list_length)]
    heapq.heapify(list_of_numbers)
    smallest_numbers = []
    for i in range(k):
        smallest_numbers.append(heapq.heappop(list_of_numbers))
    return (list_of_numbers, smallest_numbers)