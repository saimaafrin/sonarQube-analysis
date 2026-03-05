
import random
import statistics

def task_func(letters):
    # Create a dictionary with random letters and values
    values = {letter: random.randint(1, 100) for letter in letters}

    # Calculate the mean of the values
    mean = statistics.mean(values.values())

    # Sort the dictionary by the mean values
    sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted dictionary
    return {letter: values[letter] for letter, values in sorted_values}