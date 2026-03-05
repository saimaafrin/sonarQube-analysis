import string
import random
import re
def task_func(elements, pattern, seed=100):
    random.seed(seed)  # Set the seed for reproducibility
    formatted_elements = []
    for element in elements:
        # Replace each character in the element with a random character
        replaced_element = ''.join(random.choice(string.ascii_letters) for _ in element)
        # Format the element into the pattern "%{0}%"
        formatted_element = f"%{replaced_element}%"
        formatted_elements.append(formatted_element)
    
    # Concatenate all the formatted elements into a single string
    concatenated_string = ''.join(formatted_elements)
    
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_string) is not None
    
    return formatted_elements, search_result
elements = ["hello", "world"]
pattern = "world"