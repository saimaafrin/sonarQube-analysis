import random
import string
from collections import defaultdict
def task_func(n, seed=None):
    """
    Generate a dictionary with lists of random lowercase English letters.
    
    Each key in the dictionary represents a unique letter from the alphabet,
    and the associated value is a list containing randomly generated instances
    of that letter based on a seed. The function randomly selects 'n' letters
    from the alphabet (a-z) and places each occurrence in the corresponding
    list within the dictionary. The randomness is based on the provided seed
    value; the same seed will produce the same distribution of letters.
    
    Parameters:
    n (int): The number of letters to randomly select from the alphabet.
    seed (int, optional): The seed value for the random number generator.
    
    Returns:
    defaultdict: A dictionary where the keys are characters ('a' to 'z') and the
    values are lists of randomly generated letters. Each list may have 0 to 'n'
    occurrences of its associated letter, depending on the randomness and seed.
    """
    if seed is not None:
        random.seed(seed)
    
    alphabet = string.ascii_lowercase
    selected_letters = random.sample(alphabet, n)
    result = defaultdict(list)
    
    for letter in selected_letters:
        result[letter].extend([letter] * random.randint(1, n))
    
    return result