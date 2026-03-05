import heapq
import collections
def task_func(x, n):
    # Create a frequency counter for the letters in the dictionary
    letter_freq = collections.Counter(x)
    
    # Use heapq to find the n most common letters
    most_common_letters = heapq.nmost_common(letter_freq, n)
    
    # Extract the letters from the most common tuples
    result = [letter for letter, freq in most_common_letters]
    
    return result