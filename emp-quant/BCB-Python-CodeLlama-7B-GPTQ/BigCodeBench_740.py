from collections import Counter
import heapq
def task_func(my_dict):
    """
    Create a dictionary in which the keys are letters and the values are random integers.
    Find the 3 most common letters in the dictionary.
    """
    # Create a Counter object from the dictionary
    counter = Counter(my_dict)

    # Get the 3 most common letters
    most_common_letters = counter.most_common(3)

    # Return the 3 most common letters
    return most_common_letters
my_dict = {}