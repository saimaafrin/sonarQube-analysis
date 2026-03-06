
import heapq
import collections

def task_func(x, n):
    # Create a dictionary with the letter as the key and its frequency as the value
    letter_freq = collections.Counter(x)

    # Create a heap to store the top n most frequent letters
    heap = []

    # Add the first n letters to the heap
    for letter, freq in letter_freq.most_common(n):
        heapq.heappush(heap, (freq, letter))

    # Add the remaining letters to the heap
    for letter, freq in letter_freq.items():
        if freq > heap[0][0]:
            heapq.heappushpop(heap, (freq, letter))

    # Return the top n most frequent letters
    return [heap[0][1] for _ in range(n)]