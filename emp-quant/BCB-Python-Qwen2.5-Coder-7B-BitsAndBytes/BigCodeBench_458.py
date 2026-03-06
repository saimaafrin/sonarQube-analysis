
import json
import re
import pandas as pd

def task_func(json_str):
    # Check if the input JSON string is empty
    if not json_str.strip():
        return pd.DataFrame()
    
    try:
        # Load the JSON string into a dictionary
        data_dict = json.loads(json_str)
    except json.JSONDecodeError:
        return pd.DataFrame()
    
    def double_values(value):
        """Double the value if it's a number, otherwise leave it unchanged."""
        if isinstance(value, list):
            return [double_values(x) for x in value]
        elif isinstance(value, dict):
            return {k: double_values(v) for k, v in value.items()}
        elif isinstance(value, str):
            # Try to convert string to float and double it
            match = re.match(r'^-?\d+(\.\d+)?$', value)
            if match:
                return float(value) * 2
        elif isinstance(value, (int, float)):
            return value * 2
        return value
    
    # Normalize the dictionary by doubling the numerical values
    normalized_dict = double_values(data_dict)
    
    # Create a Pandas DataFrame from the normalized dictionary
    df = pd.DataFrame(normalized_dict)
    
    return df