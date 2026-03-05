import string
import random
import re
def task_func(elements, pattern, seed=100):
    # Set the seed for random number generation for reproducibility
    random.seed(seed)
    
    # Initialize an empty list to store the formatted elements
    formatted_elements = []
    
    # Iterate over each element in the input list
    for element in elements:
        # Replace each character in the element with a random character
        replaced_element = ''.join(random.choice(string.ascii_letters) for _ in element)
        
        # Format the replaced element into the pattern "%{0}%"
        formatted_element = f"%{replaced_element}%"
        
        # Append the formatted element to the list
        formatted_elements.append(formatted_element)
    
    # Concatenate all the formatted elements into a single string
    concatenated_string = ''.join(formatted_elements)
    
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_string) is not None
    
    # Return the list of formatted elements and the search result
    return formatted_elements, search_result