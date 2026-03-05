
import string
import random
import re

def task_func(elements, pattern, seed=100):
    random.seed(seed)
    formatted_elements = []
    for element in elements:
        replaced_element = ''.join(random.choice(string.ascii_letters) for _ in element)
        formatted_element = f"%{replaced_element}%"
        formatted_elements.append(formatted_element)
    
    concatenated_string = ''.join(formatted_elements)
    search_result = re.search(pattern, concatenated_string) is not None
    
    return formatted_elements, search_result