
import heapq
import random

def task_func(list_length: int, k: int):
    """
    Generates a list of random integers and returns the k largest numbers using heapq.

    Args:
        list_length (int): The length of the list to be generated.
        k (int): The number of largest numbers to be returned.

    Returns:
        tuple: A tuple containing two lists:
            list[int]: The randomly generated list of integers.
            list[int]: The k largest numbers found using heapq.
    """
    list_ = [random.randint(1, 100) for _ in range(list_length)]
    heap = []
    for i in list_:
        if len(heap) < k:
            heapq.heappush(heap, i)
        else:
            if i > heap[0]:
                heapq.heapreplace(heap, i)
    return list_, heap