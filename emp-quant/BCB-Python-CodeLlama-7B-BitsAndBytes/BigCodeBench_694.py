
import itertools
import random

def task_func(t, n):
    """
    Generate all combinations from a tuple with length n and return a random combination of length n.
    """
    # Generate all combinations of length n from the input tuple
    combinations = itertools.combinations(t, n)

    # Randomly select a combination from the generated combinations
    random_combination = random.choice(list(combinations))

    return random_combination

# Generate all combinations of length 3 from the tuple
combinations = task_func(t, n)

# Print the generated combinations
print(combinations)

# Randomly select a combination from the generated combinations
random_combination = task_func(t, n)

# Print the randomly selected combination
print(random_combination)