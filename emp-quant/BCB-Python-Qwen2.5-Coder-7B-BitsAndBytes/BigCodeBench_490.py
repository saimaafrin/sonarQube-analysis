
import xmltodict
import json

def task_func(xml_string, file_path):
    # Convert XML string to dictionary
    xml_dict = xmltodict.parse(xml_string)
    
    # Save the dictionary to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(xml_dict, json_file, indent=4)
    
    return xml_dict

result_dict = task_func(xml_string, file_path)
print("Dictionary Representation:", result_dict)