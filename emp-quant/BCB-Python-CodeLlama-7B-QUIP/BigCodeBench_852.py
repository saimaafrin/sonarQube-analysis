
import random
import string

def task_func(max_length, n_samples, seed=None):
    if max_length < 1:
        raise ValueError("max_length must be greater than 0")

    random.seed(seed)
    random_strings = [random.choice(string.ascii_lowercase) for _ in range(n_samples)]
    random_strings = [random.randint(1, max_length) for _ in range(n_samples)]

    return random_strings