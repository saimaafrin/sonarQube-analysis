import xmltodict
import json
def task_func(s, save_json=False, json_file_path=None):
    # Check if the input XML string is empty or contains only whitespace
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace.")
    
    # Convert the XML string to a dictionary
    xml_dict = xmltodict.parse(s)
    
    # Optionally save the dictionary as a JSON file
    if save_json:
        with open(json_file_path, 'w') as json_file:
            json.dump(xml_dict, json_file, indent=4)
    
    return xml_dict