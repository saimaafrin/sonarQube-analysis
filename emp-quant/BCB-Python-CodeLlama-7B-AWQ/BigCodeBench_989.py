import random
import string
def task_func(length: int, predicates: list, seed: int = None):
    """
    Generates a random string of specified length and evaluates it for specific characteristics.

    Parameters
    ----------
    length : int
        The length of the random string to generate.
    predicates : list
        A list of predicates to evaluate the generated string against.
    seed : int, optional
        A random seed to use for generating the random string.

    Returns
    -------
    tuple
        A tuple containing the generated random string and a dictionary of its characteristics.

    Raises
    ------
    ValueError
        If the specified length is negative.
    KeyError
        If any predicate is not recognized.
    """
    if length < 0:
        raise ValueError("Length must be non-negative")

    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Generate the random string
    text = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

    # Evaluate the string against the predicates
    characteristics = {}
    for predicate in predicates:
        if predicate == "length":
            characteristics[predicate] = len(text)
        elif predicate == "has_uppercase":
            characteristics[predicate] = any(c.isupper() for c in text)
        elif predicate == "has_lowercase":
            characteristics[predicate] = any(c.islower() for c in text)
        elif predicate == "has_digits":
            characteristics[predicate] = any(c.isdigit() for c in text)
        elif predicate == "has_punctuation":
            characteristics[predicate] = any(c in string.punctuation for c in text)
        else:
            raise KeyError(f"Predicate {predicate} is not recognized")

    return text, characteristics