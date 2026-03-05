from collections import Counter
import random
import string
LETTERS = string.ascii_letters
def task_func(list_of_lists):
    """
    Replace each sublist with a random letter and return a count of each letter in the final list.
    """
    # Initialize an empty dictionary to store the counts
    counts = {}

    # Iterate over the list of lists
    for sublist in list_of_lists:
        # Generate a random letter
        letter = random.choice(LETTERS)

        # Add the letter to the final list
        sublist.append(letter)

        # Increment the count of the letter in the counts dictionary
        counts[letter] = counts.get(letter, 0) + 1

    return counts
list_of_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]