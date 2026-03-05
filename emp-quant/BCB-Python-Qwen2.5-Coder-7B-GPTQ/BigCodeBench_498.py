import xmltodict
import json
def task_func(s, save_json=False, json_file_path=None):
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace.")
    
    # Convert XML string to dictionary
    xml_dict = xmltodict.parse(s)
    
    if save_json:
        # Save the dictionary as a JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(xml_dict, json_file, indent=4)
    
    return xml_dict