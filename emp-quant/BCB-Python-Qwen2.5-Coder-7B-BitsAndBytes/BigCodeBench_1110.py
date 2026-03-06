
from collections import Counter
from operator import itemgetter
import itertools

def task_func(word_dict):
    # Initialize an empty list to store all letters from the words
    all_letters = []
    
    # Iterate over each word in the dictionary
    for word in word_dict.values():
        # Extend the list with individual letters from the word
        all_letters.extend(word)
    
    # Use Counter to count the frequency of each letter
    letter_frequency = Counter(all_letters)
    
    return letter_frequency