
import pandas as pd
import json

def task_func(data: dict, output_path: str = "./default_data_output.json") -> str:
    # Convert the DataFrame to a dictionary
    data_dict = data.to_dict()

    # Drop the column named 'c' if it exists
    if 'c' in data_dict:
        del data_dict['c']

    # Save the dictionary as a JSON file
    with open(output_path, 'w') as f:
        json.dump(data_dict, f)

    return output_path