import random
import string
def task_func(max_length, n_samples, seed=None):
    """
    Generate a list containing random strings of lowercase letters. Each string's length varies from 1 to `max_length`. An optional seed can be set for the random number generator for reproducible results.
    """
    if max_length < 1:
        raise ValueError("max_length must be greater than or equal to 1")

    if seed is not None:
        random.seed(seed)

    # Generate random strings
    random_strings = [random.choices(string.ascii_lowercase, k=random.randint(1, max_length)) for _ in range(n_samples)]

    return random_strings