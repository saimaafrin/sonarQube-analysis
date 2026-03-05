
from collections import Counter
import heapq
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def task_func(my_dict):
    # Create a Counter object from the dictionary
    counter = Counter(my_dict)
    # Get the 3 most common letters
    most_common_letters = counter.most_common(3)
    return most_common_letters