from collections import Counter
import random
import string
LETTERS = string.ascii_letters
def task_func(list_of_lists):
    """
    Replace each sublist with a random letter and return a count of each letter in the final list.
    """
    result = []
    for sublist in list_of_lists:
        random_letter = random.choice(LETTERS)
        result.append(random_letter)
    return Counter(result)