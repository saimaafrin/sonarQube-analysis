import re
import random
import string
def task_func(n, pattern, seed=None):
    """
    Generate a random string of length 'n' and find all non-overlapping matches of the regex 'pattern'.
    The function generates a random string of ASCII Letters and Digits using the random module.
    By providing a seed the results are reproducable. Non overlapping matches of the provided pattern are then found using the re module.
    """
    if seed:
        random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    matches = re.findall(pattern, random_string)
    return matches