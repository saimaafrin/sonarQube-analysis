
import xmltodict
import json

def task_func(s, save_json, json_file_path):
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace")

    xml_dict = xmltodict.parse(s)

    if save_json:
        with open(json_file_path, "w") as f:
            json.dump(xml_dict, f)

    return xml_dict