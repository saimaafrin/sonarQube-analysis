import json
import pandas as pd
def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    """
    Save the list of dictionaries provided in the 'result' parameter to a CSV file (without index) and a JSON file.
    The function should output with:
        None
    """
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(result)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")

    # Save the JSON object to a file
    with open(json_file_path, "w") as f:
        f.write(json_data)

    # Output with None
    return None
result = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 35}
]