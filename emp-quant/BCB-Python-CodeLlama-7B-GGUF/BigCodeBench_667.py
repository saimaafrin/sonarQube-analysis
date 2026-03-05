
import heapq
import collections

def task_func(x, n):
    # Create a dictionary to store the letter frequencies
    freq_dict = collections.Counter(x)

    # Create a list to store the n most frequent letters
    most_freq_letters = []

    # Use heapq to find the n most frequent letters
    for letter, freq in heapq.nlargest(n, freq_dict.items(), key=lambda x: x[1]):
        most_freq_letters.append(letter)

    return most_freq_letters