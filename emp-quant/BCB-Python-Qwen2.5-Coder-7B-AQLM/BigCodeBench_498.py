
import xmltodict
import json

def task_func(s, save_json=False, json_file_path='output.json'):
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace.")
    
    # Convert XML string to dictionary
    xml_dict = xmltodict.parse(s)
    
    # Optionally save the dictionary as a JSON file
    if save_json:
        with open(json_file_path, 'w') as json_file:
            json.dump(xml_dict, json_file, indent=4)
    
    return xml_dict

# Save the parsed XML as a JSON file
task_func('<data><item>1</item><item>2</item></data>', save_json=True, json_file_path='data.json')
# A JSON file 'data.json' will be created with the parsed XML data.