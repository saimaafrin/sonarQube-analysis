import re
import random
import string
def task_func(n, pattern, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Generate a random string of length 'n' using ASCII Letters and Digits
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    
    # Find all non-overlapping matches of the regex pattern in the generated string
    matches = re.findall(pattern, random_string)
    
    return matches