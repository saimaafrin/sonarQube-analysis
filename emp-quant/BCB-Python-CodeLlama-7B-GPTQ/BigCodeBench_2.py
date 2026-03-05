import random
import statistics
def task_func(LETTERS):
    """
    Create a dictionary in which keys are random letters and values are lists of random integers.
    The dictionary is then sorted by the mean of the values in descending order, demonstrating the use of the statistics library.
    """
    # Create a dictionary with random letters as keys and lists of random integers as values
    dictionary = {}
    for letter in LETTERS:
        dictionary[letter] = [random.randint(1, 100) for _ in range(10)]

    # Sort the dictionary by the mean of the values in descending order
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: statistics.mean(x[1]), reverse=True)

    # Print the sorted dictionary
    print("dict:", sorted_dictionary)
LETTERS = "abcdefghijklmnopqrstuvwxyz"