
import xmltodict
import json

def task_func(s, file_path):
    # Convert the XML string to a dictionary
    xml_dict = xmltodict.parse(s)

    # Save the dictionary to a JSON file
    with open(file_path, 'w') as f:
        json.dump(xml_dict, f)

    return xml_dict