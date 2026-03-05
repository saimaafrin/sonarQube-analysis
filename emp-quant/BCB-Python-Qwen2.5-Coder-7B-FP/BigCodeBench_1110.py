from collections import Counter
from operator import itemgetter
import itertools
def task_func(word_dict):
    # Initialize a Counter object to keep track of letter frequencies
    letter_freq = Counter()
    
    # Iterate over each word in the dictionary
    for word in word_dict.values():
        # Count the frequency of each letter in the word and update the overall frequency
        letter_freq.update(word)
    
    # Return the dictionary with letter frequencies
    return dict(letter_freq)
word_dict = {
    "apple": "a",
    "banana": "b",
    "cherry": "c",
    "date": "d",
    "elderberry": "e"
}