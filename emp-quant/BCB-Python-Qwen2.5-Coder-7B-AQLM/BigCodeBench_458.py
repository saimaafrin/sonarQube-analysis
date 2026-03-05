
import json
import re
import pandas as pd

def task_func(json_str):
    # Check if the input JSON string is empty
    if not json_str.strip():
        return pd.DataFrame()
    
    # Load the JSON string into a dictionary
    data_dict = json.loads(json_str)
    
    # Function to normalize numerical values
    def normalize_value(value):
        if isinstance(value, list):
            return [normalize_value(v) for v in value]
        elif isinstance(value, str):
            try:
                # Extract numbers from the string and double them
                numbers = re.findall(r'\d+', value)
                return [float(num) * 2 for num in numbers]
            except ValueError:
                return value
        elif isinstance(value, (int, float)):
            return value * 2
        else:
            return value
    
    # Normalize the dictionary
    normalized_dict = {key: normalize_value(value) for key, value in data_dict.items()}
    
    # Create a Pandas DataFrame from the normalized dictionary
    df = pd.DataFrame(normalized_dict)
    
    return df