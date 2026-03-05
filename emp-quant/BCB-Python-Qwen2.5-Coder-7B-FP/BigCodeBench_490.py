import xmltodict
import json
def task_func(s, file_path):
    # Convert the XML string to a dictionary
    xml_dict = xmltodict.parse(s)
    
    # Convert the dictionary to a JSON string
    json_str = json.dumps(xml_dict, indent=4)
    
    # Write the JSON string to a file
    with open(file_path, 'w') as json_file:
        json_file.write(json_str)
    
    # Return the dictionary representation of the XML string
    return xml_dict