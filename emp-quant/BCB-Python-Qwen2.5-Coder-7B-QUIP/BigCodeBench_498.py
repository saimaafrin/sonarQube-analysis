
import xmltodict
import json

def task_func(s, save_json, json_file_path):
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace.")
    
    # Convert XML string to dictionary
    result = xmltodict.parse(s)
    
    # Optionally save the dictionary as a JSON file
    if save_json:
        with open(json_file_path, 'w') as json_file:
            json.dump(result, json_file, indent=4)
    
    return result