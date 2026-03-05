from collections import Counter
import math
def task_func(nested_dict):
    # Initialize a Counter to aggregate values
    aggregated_values = Counter()
    
    # Iterate through the nested dictionary
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            # If the value is a dictionary, recursively call task_func
            aggregated_values += task_func(value)
        else:
            # If the value is not a dictionary, add it to the Counter
            aggregated_values[key] += value
    
    # Remove the "ele" key if it exists
    aggregated_values.pop("ele", None)
    
    # Create a new dictionary with the sine of each key
    result_dict = {key: math.sin(value) for key, value in aggregated_values.items()}
    
    return result_dict