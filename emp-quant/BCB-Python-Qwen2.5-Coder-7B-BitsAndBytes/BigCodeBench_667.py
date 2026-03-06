
import heapq
import collections

def task_func(x, n):
    # Create a counter object to count the frequency of each letter
    letter_counter = collections.Counter(x)
    
    # Use heapq.nmost_common to get the n most common letters
    most_common_letters = letter_counter.most_common(n)
    
    # Extract just the letters from the tuples
    result = [letter for letter, freq in most_common_letters]
    
    return result