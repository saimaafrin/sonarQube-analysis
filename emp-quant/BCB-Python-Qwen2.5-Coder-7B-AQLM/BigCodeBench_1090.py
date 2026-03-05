
import ast
import json
from collections import Counter

def task_func(file_pointer):
    key_frequency = Counter()
    
    for line in file_pointer:
        try:
            # Evaluate the string as a dictionary
            data = ast.literal_eval(line)
            if isinstance(data, dict):
                # Update the key frequency counter
                key_frequency.update(data.keys())
        except (ValueError, SyntaxError):
            # Skip lines that cannot be evaluated as dictionaries
            continue
    
    return key_frequency