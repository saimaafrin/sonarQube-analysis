import string
import random
def task_func(length, random_seed=None):
    """
    Generate a random string of a given length, with each character being either a parenthesis (from the set "(){}[]") or a lowercase English character.
    For function uses a optional random_seed when sampling characters.
    """
    if random_seed:
        random.seed(random_seed)
    BRACKETS = "(){}[]"
    STRING = ""
    for i in range(length):
        if random.randint(0, 1):
            STRING += random.choice(BRACKETS)
        else:
            STRING += random.choice(string.ascii_lowercase)
    return STRING