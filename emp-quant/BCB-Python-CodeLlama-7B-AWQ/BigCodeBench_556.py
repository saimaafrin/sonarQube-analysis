import numpy as np
import random
from difflib import SequenceMatcher
def task_func(s, min_length, max_length, letters):
    """
    Generates a random string of length between min_length and max_length, inclusive, using characters from letters, and evaluates its similarity to the provided string s. A similarity score of 0.5 or higher considered 'similar'.
    The function should output with:
        tuple: A tuple containing the generated string and a boolean indicating whether it's
        considered similar to s based on the similarity threshold.
    """
    # Generate a random string of length between min_length and max_length
    random_string = ''.join(random.choice(letters) for _ in range(random.randint(min_length, max_length)))

    # Evaluate the similarity between the generated string and the provided string s
    similarity = SequenceMatcher(None, random_string, s).ratio()

    # Return a tuple containing the generated string and a boolean indicating whether it's similar to s
    return (random_string, similarity >= 0.5)