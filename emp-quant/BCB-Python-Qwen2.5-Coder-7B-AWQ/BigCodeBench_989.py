import random
import string
def task_func(length: int, predicates: list, seed: int = None):
    if length < 0:
        raise ValueError("Length cannot be negative")
    
    if seed is not None:
        random.seed(seed)
    
    characters = string.ascii_letters + string.digits + string.punctuation
    result_string = ''.join(random.choice(characters) for _ in range(length))
    
    result_dict = {}
    for predicate in set(predicates):  # Deduplicate predicates
        if predicate == 'isalpha':
            result_dict['isalpha'] = result_string.isalpha()
        elif predicate == 'isdigit':
            result_dict['isdigit'] = result_string.isdigit()
        elif predicate == 'isalnum':
            result_dict['isalnum'] = result_string.isalnum()
        elif predicate == 'islower':
            result_dict['islower'] = result_string.islower()
        elif predicate == 'isupper':
            result_dict['isupper'] = result_string.isupper()
        elif predicate == 'isspace':
            result_dict['isspace'] = result_string.isspace()
        elif predicate == 'istitle':
            result_dict['istitle'] = result_string.istitle()
        else:
            raise KeyError(f"Unrecognized predicate: {predicate}")
    
    return result_string, result_dict