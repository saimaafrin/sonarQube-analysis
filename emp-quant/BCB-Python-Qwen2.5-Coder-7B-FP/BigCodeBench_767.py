from collections import Counter
import random
import string
LETTERS = string.ascii_letters
def task_func(list_of_lists):
    """
    Replaces each sublist in the given list with a random letter and returns a count of each letter in the final list.
    
    Args:
    list_of_lists (list): A list containing sublists.
    
    Returns:
    dict: A dictionary containing the count of each letter in the list.
    """
    # Replace each sublist with a random letter
    random_letters = [random.choice(LETTERS) for _ in list_of_lists]
    
    # Count the occurrences of each letter
    letter_count = Counter(random_letters)
    
    return letter_count