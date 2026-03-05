import heapq
import collections
def task_func(x, n):
    """
    Find the n most common letters in a dictionary, x, where the key letters and the values are their frequencies.
    The function should output with:
        list: The n most frequent letters.
    """
    # Create a dictionary to store the letter frequencies
    letter_freq = collections.Counter(x)

    # Create a heap to store the top n most frequent letters
    top_n = []

    # Add the first n letters to the heap
    for letter in letter_freq.most_common(n):
        heapq.heappush(top_n, letter)

    # Add the remaining letters to the heap
    for letter in letter_freq.most_common():
        if letter not in top_n:
            heapq.heappush(top_n, letter)

    # Return the top n most frequent letters
    return [letter for letter, _ in top_n]
x = {'a': 5, 'b': 3, 'c': 2, 'd': 1}