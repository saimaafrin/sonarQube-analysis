import random
import string
from collections import defaultdict
def task_func(n, seed=None):
    """
    Generate a dictionary with lists of random lowercase english letters. Each key in the dictionary 
    represents a unique letter from the alphabet, and the associated value is a list, containing randomly generated instances of that letter based on a seed. The function randomly selects 'n' letters from the alphabet (a-z) and places each occurrence in the corresponding list within the dictionary. The randomness is based on the provided seed value; the same seed will produce the same distribution of letters. The dictionary has only those keys for which a letter was generated.
    """
    if seed is None:
        seed = random.randint(0, 1000000)
    random.seed(seed)
    letters = string.ascii_lowercase
    result = defaultdict(list)
    for i in range(n):
        letter = random.choice(letters)
        result[letter].append(letter)
    return result