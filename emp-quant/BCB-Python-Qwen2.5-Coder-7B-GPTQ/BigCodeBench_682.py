from collections import Counter
import math
def task_func(nested_dict):
    # Initialize a Counter to aggregate values
    aggregated_values = Counter()
    
    # Iterate through the nested dictionary
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            # Recursively aggregate values if the value is another dictionary
            aggregated_values += task_func(value)
        else:
            # Aggregate the value if it's a single value
            aggregated_values[key] += value
    
    # Remove the "ele" key if it exists
    aggregated_values.pop("ele", None)
    
    # Create a new dictionary with the sine of each remaining key
    result_dict = {key: math.sin(math.radians(value)) for key, value in aggregated_values.items()}
    
    return result_dict