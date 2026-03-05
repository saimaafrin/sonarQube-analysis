import random
import string
def task_func(length: int, predicates: list, seed: int = None):
    """
    Generates a random string of specified length and evaluates it for specific characteristics.

    Parameters
    ----------
    length : int
        Length of the random string to be generated.
    predicates : list
        List of predicates to evaluate the generated string.
    seed : int, optional
        Seed for random number generation.

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
        raise ValueError("Length must be non-negative.")

    if predicates is None:
        predicates = []

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

    # Evaluate the string for the specified predicates
    characteristics = {}
    for predicate in predicates:
        if predicate == "length":
            characteristics[predicate] = len(random_string)
        elif predicate == "alphanumeric":
            characteristics[predicate] = random_string.isalnum()
        elif predicate == "alpha":
            characteristics[predicate] = random_string.isalpha()
        elif predicate == "digit":
            characteristics[predicate] = random_string.isdigit()
        elif predicate == "lower":
            characteristics[predicate] = random_string.islower()
        elif predicate == "upper":
            characteristics[predicate] = random_string.isupper()
        elif predicate == "punctuation":
            characteristics[predicate] = random_string.isalnum()
        else:
            raise KeyError(f"Predicate {predicate} is not recognized.")

    return (random_string, characteristics)