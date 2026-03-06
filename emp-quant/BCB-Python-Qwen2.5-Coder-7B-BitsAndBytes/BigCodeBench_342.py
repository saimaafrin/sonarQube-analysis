
import string
import random
import re

def task_func(elements, pattern, seed=100):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Define the alphabet to choose from for replacement
    alphabet = string.ascii_letters + string.digits
    
    # Function to replace characters in an element with random ones
    def replace_chars(element):
        return ''.join(random.choice(alphabet) for _ in element)
    
    # Replace characters in each element and format it
    formatted_elements = ["%{}%".format(replace_chars(e)) for e in elements]
    
    # Concatenate all formatted elements into a single string
    concatenated_string = ''.join(formatted_elements)
    
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_string) is not None
    
    return formatted_elements, search_result