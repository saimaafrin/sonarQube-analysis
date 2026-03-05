
import string
import random
import re

def task_func(elements, pattern, seed=100):
    random.seed(seed)
    formatted_elements = []
    for element in elements:
        replaced_element = ''.join(random.choice(string.ascii_letters) for _ in range(len(element)))
        formatted_elements.append('%{0}%'.format(replaced_element))
    search_result = re.search(pattern, ''.join(formatted_elements))
    return formatted_elements, search_result