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

    # Use heapq to find the n most frequent letters
    most_freq_letters = heapq.nlargest(n, letter_freq, key=letter_freq.get)

    return most_freq_letters