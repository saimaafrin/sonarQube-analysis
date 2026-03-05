
from collections import Counter
import heapq
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def task_func(my_dict):
    # Count the occurrences of each letter
    letter_counts = Counter(my_dict.keys())
    # Find the 3 most common letters
    most_common_letters = heapq.nlargest(3, letter_counts, key=letter_counts.get)
    return most_common_letters