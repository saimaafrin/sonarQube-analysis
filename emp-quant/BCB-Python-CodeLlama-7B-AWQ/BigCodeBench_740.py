from collections import Counter
import heapq
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def task_func(my_dict):
    """
    Create a dictionary in which the keys are letters and the values are random integers.
    Find the 3 most common letters in the dictionary.
    """
    # Create a dictionary with random integers as values
    my_dict = {letter: random.randint(1, 100) for letter in LETTERS}
    # Create a Counter object from the dictionary
    counter = Counter(my_dict)
    # Find the 3 most common letters
    most_common_letters = counter.most_common(3)
    # Print the result
    print(most_common_letters)