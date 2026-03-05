import ast
import json
from collections import Counter
def task_func(file_pointer):
    # Initialize a Counter object to store key frequencies
    key_frequency = Counter()
    
    # Iterate over each line in the file pointer
    for line in file_pointer:
        # Try to evaluate the line as a dictionary
        try:
            data = ast.literal_eval(line)
        except (SyntaxError, ValueError):
            # Skip lines that cannot be evaluated as dictionaries
            continue
        
        # Check if the data is a dictionary
        if isinstance(data, dict):
            # Update the Counter object with keys from the dictionary
            key_frequency.update(data.keys())
    
    # Return the Counter object containing key frequencies
    return key_frequency