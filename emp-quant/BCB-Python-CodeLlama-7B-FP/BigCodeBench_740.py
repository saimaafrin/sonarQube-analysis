from collections import Counter
import heapq
def task_func(my_dict):
    """
    Find the 3 most common letters in the dictionary.
    """
    # Create a Counter object from the dictionary
    counter = Counter(my_dict)
    # Get the 3 most common letters
    most_common_letters = counter.most_common(3)
    # Return the list of most common letters
    return most_common_letters