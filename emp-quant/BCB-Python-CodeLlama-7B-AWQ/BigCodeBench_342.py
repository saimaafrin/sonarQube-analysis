import string
import random
import re
def task_func(elements, pattern, seed=100):
    """
    Replace each character in each element of the Elements list with a random character and format the element into a pattern "%{0}%", where {0} is the replaced element. Finally, concatenate all the formatted elements into a single string and search for the regex pattern specified in the parameter pattern. Return the true or false value based on the search result.
    """
    random.seed(seed)
    formatted_elements = []
    for element in elements:
        formatted_element = "%{" + random.choice(string.ascii_letters) + "%}"
        formatted_elements.append(formatted_element)
    formatted_string = "".join(formatted_elements)
    search_result = re.search(pattern, formatted_string)
    return formatted_elements, search_result
elements = ["abc", "def", "ghi"]
pattern = "a"