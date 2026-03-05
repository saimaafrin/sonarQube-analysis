
import json
import re
import pandas as pd

def task_func(json_str):
    # Load JSON string into dictionary
    data = json.loads(json_str)
    
    # Function to double numerical values
    def double_numerical_values(value):
        if isinstance(value, list):
            return [double_numerical_values(item) for item in value]
        elif isinstance(value, str):
            match = re.match(r'^-?\d+(?:\.\d+)?$', value)
            if match:
                return float(value) * 2
        elif isinstance(value, float) or isinstance(value, int):
            return value * 2
        return value
    
    # Normalize the dictionary by doubling numerical values
    normalized_data = double_numerical_values(data)
    
    # Create a Pandas DataFrame from the normalized dictionary
    df = pd.DataFrame(normalized_data, index=[0])
    
    # Return the DataFrame
    return df