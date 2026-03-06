
import xmltodict
import json

def task_func(s, save_json, json_file_path):
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace")

    # Convert XML string to dictionary
    result = xmltodict.parse(s)

    # Save dictionary as JSON file if requested
    if save_json:
        with open(json_file_path, "w") as f:
            json.dump(result, f)

    return result