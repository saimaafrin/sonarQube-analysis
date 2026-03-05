
import json
import re
import pandas as pd

def task_func(json_str):
    # Load the JSON string into a dictionary
    data = json.loads(json_str)

    # Normalize the dictionary by doubling the numerical values
    for key, value in data.items():
        if isinstance(value, (int, float)):
            data[key] = value * 2
        elif isinstance(value, list):
            data[key] = [item * 2 for item in value]
        elif isinstance(value, str):
            match = re.search(r"[0-9\.]+", value)
            if match:
                data[key] = float(match.group(0)) * 2

    # Create a Pandas DataFrame from the dictionary
    df = pd.DataFrame(data)

    return df