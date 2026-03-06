
from collections import Counter
import heapq

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(my_dict):
    # Filter out non-letter keys and convert all letters to lowercase
    filtered_dict = {key.lower(): value for key, value in my_dict.items() if key.isalpha()}
    
    # Count the occurrences of each letter
    letter_counts = Counter(filtered_dict)
    
    # Get the 3 most common letters
    most_common_letters = [item[0] for item in letter_counts.most_common(3)]
    
    return most_common_letters