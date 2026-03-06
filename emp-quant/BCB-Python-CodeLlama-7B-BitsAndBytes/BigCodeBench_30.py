
import json
import os
import re

def task_func(file_path, attribute, INPUT_JSON, EMAIL_REGEX):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise ValueError("File does not exist")

    # Load the JSON data from the file
    with open(file_path, "r") as f:
        data = json.load(f)

    # Check if all required attributes are present
    for required_attribute in INPUT_JSON["required"]:
        if required_attribute not in data:
            raise ValueError(f"Required attribute {required_attribute} is missing")

    # Check if the attribute is of the correct type
    if attribute not in INPUT_JSON["properties"]:
        raise ValueError(f"Attribute {attribute} is not defined in the JSON schema")
    if not isinstance(data[attribute], INPUT_JSON["properties"][attribute]["type"]):
        raise ValueError(f"Attribute {attribute} is not of the correct type")

    # Check if the email format is valid
    if attribute == "email" and not re.match(EMAIL_REGEX, data[attribute]):
        raise ValueError(f"Email format is invalid")

    # Return the value of the specified attribute
    return data[attribute]

try:
    result = task_func(file_path, attribute, INPUT_JSON, EMAIL_REGEX)
    print(result)
except ValueError as e:
    print(e)