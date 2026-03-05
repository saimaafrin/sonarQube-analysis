import string
import random
def task_func(length, random_seed=None):
    """
    Generate a random string of a given length, with each character being either a parenthesis (from the set "(){}[]") or a lowercase English character.
    For function uses a optional random_seed when sampling characters.
    """
    if random_seed is not None:
        random.seed(random_seed)
    return ''.join(random.choice(string.ascii_letters + BRACKETS) for _ in range(length))