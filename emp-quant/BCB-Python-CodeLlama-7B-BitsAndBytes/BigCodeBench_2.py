
import random
import statistics

def task_func(LETTERS):
    # Create a dictionary with random letters as keys and lists of random integers as values
    d = {random.choice(LETTERS): [random.randint(1, 100) for _ in range(5)] for _ in range(10)}

    # Sort the dictionary by the mean of the values in descending order
    sorted_d = sorted(d.items(), key=lambda x: statistics.mean(x[1]), reverse=True)

    # Print the sorted dictionary
    print("dict:")
    for key, value in sorted_d:
        print(f"{key}: {value}")