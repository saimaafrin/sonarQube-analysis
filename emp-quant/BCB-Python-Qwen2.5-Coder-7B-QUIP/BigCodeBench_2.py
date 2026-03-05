
import random
import statistics

def task_func(LETTERS):
    # Create a dictionary with random letters as keys and lists of random integers as values
    random_dict = {chr(i): [random.randint(1, 100) for _ in range(5)] for i in range(97, 97 + LETTERS)}

    # Sort the dictionary by the mean of the values in descending order
    sorted_dict = sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True)

    # Output the sorted dictionary
    print("dict:", sorted_dict)