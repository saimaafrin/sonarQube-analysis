
import random
import string

def task_func(max_length, n_samples, seed=None):
    if max_length < 1:
        raise ValueError("Max length must be greater than 0")

    if seed is not None:
        random.seed(seed)

    letters = string.ascii_lowercase
    random_strings = []
    for _ in range(n_samples):
        random_string = ''.join(random.choices(letters, k=random.randint(1, max_length)))
        random_strings.append(random_string)

    return random_strings