
import heapq
import collections

def task_func(x, n):
    # Create a dictionary to store the frequencies
    freq_dict = collections.Counter(x)

    # Use heapq to find the n most frequent letters
    most_freq = heapq.nlargest(n, freq_dict, key=lambda x: x[1])

    return most_freq