
import random
import string

def task_func(length: int, predicates: list, seed: int = None):
    """
    Generates a random string of specified length and evaluates it for specific characteristics.

    Parameters:
        length (int): The length of the random string to generate.
        predicates (list): A list of predicates to evaluate the generated string against.
        seed (int, optional): A random seed to use for generating the random string.

    Returns:
        tuple: A tuple containing the generated random string and a dictionary of its characteristics.

    Raises:
        ValueError: If the specified length is negative.
        KeyError: If any predicate is not recognized.
    """
    if length < 0:
        raise ValueError("Length must be non-negative")

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

    # Evaluate the string against the predicates
    characteristics = {}
    for predicate in predicates:
        if predicate == "length":
            characteristics[predicate] = len(random_string)
        elif predicate == "uppercase":
            characteristics[predicate] = sum(1 for c in random_string if c.isupper())
        elif predicate == "lowercase":
            characteristics[predicate] = sum(1 for c in random_string if c.islower())
        elif predicate == "digits":
            characteristics[predicate] = sum(1 for c in random_string if c.isdigit())
        elif predicate == "punctuation":
            characteristics[predicate] = sum(1 for c in random_string if c in string.punctuation)
        else:
            raise KeyError(f"Predicate {predicate} is not recognized")

    return random_string, characteristics