import xmltodict
import json
def task_func(s, save_json, json_file_path):
    """
    Converts an XML string into a dictionary representation and optionally saves it as a JSON file.
    This function is useful for easily accessing data stored in XML format and saving it for future use.
    """
    if not s.strip():
        raise ValueError("Input XML string is empty or contains only whitespace.")

    # Convert the XML string to a dictionary
    result = xmltodict.parse(s)

    # Save the parsed XML as a JSON file
    if save_json:
        with open(json_file_path, "w") as f:
            json.dump(result, f, indent=4)

    return result
s = '<school><class><student>Emma</student></class></school>'