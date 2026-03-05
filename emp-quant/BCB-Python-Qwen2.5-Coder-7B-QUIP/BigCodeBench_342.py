
import string
import random
import re

def task_func(elements, pattern, seed=100):
    # Set the seed for random number generation
    random.seed(seed)

    # Replace each character in each element with a random character
    replaced_elements = []
    for element in elements:
        replaced_element = ''.join(random.choice(string.ascii_letters) for _ in element)
        replaced_elements.append(replaced_element)

    # Format the element into a pattern "%{0}%"
    formatted_elements = ['%{}%'.format(element) for element in replaced_elements]

    # Concatenate all the formatted elements into a single string
    concatenated_string = ''.join(formatted_elements)

    # Search for the regex pattern specified in the parameter pattern
    search_result = bool(re.search(pattern, concatenated_string))

    # Output the list of formatted elements with replaced characters and the search result
    return replaced_elements, search_result