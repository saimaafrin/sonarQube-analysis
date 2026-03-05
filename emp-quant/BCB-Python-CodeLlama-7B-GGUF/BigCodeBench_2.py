
import random
import statistics

def task_func(letters):
    # Create a dictionary with random letters as keys and lists of random integers as values
    data = {letter: random.sample(range(100), 5) for letter in letters}

    # Calculate the mean of each list of integers
    means = {letter: statistics.mean(integers) for letter, integers in data.items()}

    # Sort the dictionary by the mean values in descending order
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    return sorted_data