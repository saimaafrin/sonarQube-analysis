
import string
import random
import re

def task_func(elements, pattern, seed=100):
    # Replace each character in each element of the Elements list with a random character
    replaced_elements = [element.replace(c, random.choice(string.ascii_letters)) for element in elements]

    # Format the elements into a pattern "%{0}%"
    formatted_elements = ["%{0}%".format(element) for element in replaced_elements]

    # Concatenate all the formatted elements into a single string
    concatenated_string = "".join(formatted_elements)

    # Search for the regex pattern specified in the parameter pattern
    search_result = re.search(pattern, concatenated_string)

    # Return the true or false value based on the search result
    return search_result is not None