import random
import string
def task_func(length: int, predicates: list, seed: int = None):
    if length < 0:
        raise ValueError("Length cannot be negative")
    
    if seed is not None:
        random.seed(seed)
    
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    result = {}
    for predicate in predicates:
        if predicate == 'isalpha':
            result['isalpha'] = random_string.isalpha()
        elif predicate == 'isdigit':
            result['isdigit'] = random_string.isdigit()
        elif predicate == 'isalnum':
            result['isalnum'] = random_string.isalnum()
        elif predicate == 'isspace':
            result['isspace'] = random_string.isspace()
        elif predicate == 'istitle':
            result['istitle'] = random_string.istitle()
        elif predicate == 'islower':
            result['islower'] = random_string.islower()
        elif predicate == 'isupper':
            result['isupper'] = random_string.isupper()
        elif predicate == 'isprintable':
            result['isprintable'] = random_string.isprintable()
        else:
            raise KeyError(f"Invalid predicate: {predicate}")
    
    return random_string, result