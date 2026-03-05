import pandas as pd
import json
def task_func(data: dict, output_path: str = "./default_data_output.json") -> str:
    """
    Converts the given DataFrame to a dictionary, dropping the column named 'c' if it exists, and then saves it as a JSON file.
    The function should output with:
        str: Path where the JSON file was saved.
    """
    # Convert the DataFrame to a dictionary
    data_dict = data.to_dict()

    # Drop the column named 'c' if it exists
    if 'c' in data_dict:
        del data_dict['c']

    # Save the dictionary as a JSON file
    with open(output_path, 'w') as f:
        json.dump(data_dict, f)

    return output_path
data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})