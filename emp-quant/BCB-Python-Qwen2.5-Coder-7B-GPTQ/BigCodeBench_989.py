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
    for predicate in predicates:
        if predicate == 'isalpha':
            characteristics['isalpha'] = result_string.isalpha()
        elif predicate == 'isdigit':
            characteristics['isdigit'] = result_string.isdigit()
        elif predicate == 'isalnum':
            characteristics['isalnum'] = result_string.isalnum()
        elif predicate == 'islower':
            characteristics['islower'] = result_string.islower()
        elif predicate == 'isupper':
            characteristics['isupper'] = result_string.isupper()
        elif predicate == 'isspace':
            characteristics['isspace'] = result_string.isspace()
        elif predicate == 'istitle':
            characteristics['istitle'] = result_string.istitle()
        else:
            raise KeyError(f"Invalid predicate: {predicate}")
    
    return result_string, characteristics