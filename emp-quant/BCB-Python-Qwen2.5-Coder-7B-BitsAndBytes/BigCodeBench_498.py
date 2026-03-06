
import xmltodict
import json

def task_func(s, save_json=False, json_file_path=None):
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace.")
    
    # Parse the XML string to a dictionary
    result_dict = xmltodict.parse(s)
    
    # Optionally save the dictionary as a JSON file
    if save_json:
        with open(json_file_path, 'w') as json_file:
            json.dump(result_dict, json_file, indent=4)
    
    return result_dict