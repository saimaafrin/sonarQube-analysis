
import random
import string

def task_func(length: int, predicates: list, seed: int = None):
    if length < 0:
        raise ValueError("Length cannot be negative")
    
    if seed is not None:
        random.seed(seed)
    
    result = {}
    text = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, length))
    
    for predicate in predicates:
        if predicate == 'isalpha':
            result['isalpha'] = all(c.isalpha() for c in text)
        elif predicate == 'isalnum':
            result['isalnum'] = all(c.isalnum() for c in text)
        elif predicate == 'isdigit':
            result['isdigit'] = all(c.isdigit() for c in text)
        elif predicate == 'islower':
            result['islower'] = all(c.islower() for c in text)
        elif predicate == 'isupper':
            result['isupper'] = all(c.isupper() for c in text)
        elif predicate == 'isnumeric':
            result['isnumeric'] = all(c.isdigit() for c in text)
        elif predicate == 'isprintable':
            result['isprintable'] = all(c.isprintable() for c in text)
        elif predicate == 'isspace':
            result['isspace'] = all(c.isspace() for c in text)
        else:
            raise KeyError(f"Unrecognized predicate: {predicate}")
    
    return (text, result)