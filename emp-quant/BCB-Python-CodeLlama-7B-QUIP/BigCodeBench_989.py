
import random
import string

def task_func(length: int, predicates: list, seed: int = None):
    if length < 0:
        raise ValueError("Length must be non-negative")
    if predicates is None:
        predicates = []
    if seed is not None:
        random.seed(seed)
    text = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    characteristics = {}
    for predicate in predicates:
        if predicate == "length":
            characteristics["length"] = len(text)
        elif predicate == "uppercase":
            characteristics["uppercase"] = sum(1 for c in text if c.isupper())
        elif predicate == "lowercase":
            characteristics["lowercase"] = sum(1 for c in text if c.islower())
        elif predicate == "punctuation":
            characteristics["punctuation"] = sum(1 for c in text if c.isalpha() and not c.islower())
        else:
            raise KeyError("Invalid predicate")
    return text, characteristics