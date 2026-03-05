import xmltodict
import json
def task_func(s, file_path):
    # Convert the XML string to a dictionary
    xml_dict = xmltodict.parse(s)
    
    # Write the dictionary to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(xml_dict, json_file, indent=4)
    
    # Return the dictionary representation of the XML string
    return xml_dict