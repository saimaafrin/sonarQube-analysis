from collections import Counter
from operator import itemgetter
import itertools
def task_func(word_dict):
    # Initialize a Counter to keep track of letter frequencies
    letter_counter = Counter()
    
    # Iterate over each word and its corresponding letters in the dictionary
    for word, letters in word_dict.items():
        # Count the frequency of each letter in the letters string
        letter_counter.update(letters)
    
    # Return the dictionary with letter frequencies
    return dict(letter_counter)
word_dict = {
    "apple": "apple",
    "banana": "banana",
    "cherry": "cherry"
}