import json
import pandas as pd
def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    """
    Saves the list of dictionaries provided in the 'result' parameter to a CSV file (without index) and a JSON file.
    """
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(result)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    # Convert the DataFrame to a JSON string
    json_string = df.to_json(orient="records")

    # Save the JSON string to a file
    with open(json_file_path, "w") as f:
        f.write(json_string)
result = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 27},
    {"name": "Bob", "age": 35}
]