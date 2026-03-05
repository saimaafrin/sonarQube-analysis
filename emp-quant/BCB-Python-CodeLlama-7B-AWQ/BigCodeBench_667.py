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

    # Create a list to store the top n most frequent letters
    top_n = []

    # Add the most frequent letter to the list
    top_n.append(letter_freq.most_common(1)[0][0])

    # Add the remaining n-1 most frequent letters to the list
    for i in range(1, n):
        top_n.append(letter_freq.most_common(n-i)[i][0])

    return top_n
x = "hello world"
n = 3