import random
import string
def task_func(max_length, n_samples, seed=None):
    """
    Generate a list containing random strings of lowercase letters.
    
    Parameters:
    - max_length: int, the maximum length of the random strings.
    - n_samples: int, the number of random strings to generate.
    - seed: int, optional, seed for the random number generator for reproducibility.
    
    Returns:
    - list: A list containing random strings.
    
    Raises:
    - ValueError: If max_length is smaller than 1.
    """
    if max_length < 1:
        raise ValueError("max_length must be at least 1")
    
    if seed is not None:
        random.seed(seed)
    
    result = []
    for _ in range(n_samples):
        length = random.randint(1, max_length)
        random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
        result.append(random_string)
    
    return result