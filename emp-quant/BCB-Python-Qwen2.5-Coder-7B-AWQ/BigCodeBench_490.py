import xmltodict
import json
def task_func(s, file_path):
    # Convert XML string to dictionary
    xml_dict = xmltodict.parse(s)
    
    # Save the dictionary as a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(xml_dict, json_file, indent=4)
    
    # Return the dictionary representation of the XML string
    return xml_dict