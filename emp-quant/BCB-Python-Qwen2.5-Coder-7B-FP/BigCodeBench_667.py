import heapq
import collections
def task_func(x, n):
    # Create a frequency counter for the letters in the dictionary values
    letter_counter = collections.Counter(letter for word in x.values() for letter in word)
    
    # Use heapq to find the n most common letters
    most_common_letters = heapq.nmost_common(letter_counter, n)
    
    # Extract the letters from the most common tuples
    result = [letter for letter, count in most_common_letters]
    
    return result