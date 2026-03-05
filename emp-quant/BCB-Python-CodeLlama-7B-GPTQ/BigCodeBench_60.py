import json
import pandas as pd
def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    # Save the list of dictionaries to a CSV file
    df = pd.DataFrame(result)
    df.to_csv(csv_file_path, index=False)

    # Save the list of dictionaries to a JSON file
    with open(json_file_path, "w") as f:
        json.dump(result, f)

    # Output with None
    return None
result = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 40},
]
csv_file_path = "test.csv"
json_file_path = "test.json"
df = pd.read_csv(csv_file_path)