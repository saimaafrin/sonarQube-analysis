
import heapq
import random

def task_func(list_length: int, k: int):
    list_of_ints = [random.randint(0, 100) for i in range(list_length)]
    return (list_of_ints, heapq.nlargest(k, list_of_ints))