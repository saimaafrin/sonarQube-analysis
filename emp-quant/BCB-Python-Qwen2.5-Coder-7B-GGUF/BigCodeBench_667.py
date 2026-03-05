
import heapq
import collections

def task_func(x, n):
    # Create a counter object from the dictionary
    letter_counter = collections.Counter(x)
    
    # Use heapq to find the n most common elements
    most_common_letters = heapq.nmost_common(letter_counter, n)
    
    # Extract the letters from the most common elements
    result = [letter for letter, frequency in most_common_letters]
    
    return result