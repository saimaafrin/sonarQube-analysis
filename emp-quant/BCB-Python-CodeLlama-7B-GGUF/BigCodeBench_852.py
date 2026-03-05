
import random
import string

def task_func(max_length, n_samples, seed=None):
    if max_length < 1:
        raise ValueError("Max length must be greater than 0")

    if seed is not None:
        random.seed(seed)

    random_strings = []
    for _ in range(n_samples):
        string_length = random.randint(1, max_length)
        random_string = ''.join(random.choices(string.ascii_lowercase, k=string_length))
        random_strings.append(random_string)

    return random_strings