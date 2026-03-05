
import xmltodict
import json

def task_func(s, file_path):
    # Convert the XML string to a dictionary
    dict = xmltodict.parse(s)

    # Save the dictionary to a JSON file
    with open(file_path, 'w') as f:
        json.dump(dict, f, indent=4)

    return dict