
import string
import random
import re

def task_func(elements, pattern, seed=100):
    random.seed(seed)
    formatted_elements = []
    for element in elements:
        formatted_element = "%{" + str(random.randint(0, len(element) - 1)) + "}%"
        formatted_elements.append(formatted_element)
    formatted_elements = "".join(formatted_elements)
    search_result = re.search(pattern, formatted_elements)
    return formatted_elements, search_result