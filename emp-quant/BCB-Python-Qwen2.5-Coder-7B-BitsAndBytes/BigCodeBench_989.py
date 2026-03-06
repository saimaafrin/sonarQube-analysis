
import random
import string

def task_func(length: int, predicates: list, seed: int = None):
    if length < 0:
        raise ValueError("Length cannot be negative")
    
    if seed is not None:
        random.seed(seed)
    
    characters = string.ascii_letters + string.digits + string.punctuation
    result_string = ''.join(random.choice(characters) for _ in range(length))
    
    characteristics = {}
    valid_predicates = {
        'isalpha': str.isalpha,
        'isdigit': str.isdigit,
        'ispunct': str.ispunct,
        'islower': str.islower,
        'isupper': str.isupper,
        'istitle': str.istitle
    }
    
    for predicate in predicates:
        if predicate not in valid_predicates:
            raise KeyError(f"Invalid predicate: {predicate}")
        
        characteristic_name = predicate.replace('is', '')
        characteristics[characteristic_name] = valid_predicates[predicate](result_string)
    
    return (result_string, characteristics)