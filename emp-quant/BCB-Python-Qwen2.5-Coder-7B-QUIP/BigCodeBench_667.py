
import heapq
import collections

def task_func(x, n):
    # Create a list of tuples with the letter and its frequency
    letter_freq = [(letter, freq) for letter, freq in x.items()]
    
    # Use heapq.nlargest to get the n most frequent letters
    most_common = heapq.nlargest(n, letter_freq, key=lambda item: item[1])
    
    # Extract the letters from the list of tuples
    most_common_letters = [item[0] for item in most_common]
    
    return most_common_letters