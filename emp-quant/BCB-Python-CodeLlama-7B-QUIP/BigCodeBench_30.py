
import json
import os
import re

def task_func(file_path, attribute, INPUT_JSON, EMAIL_REGEX):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise ValueError("File does not exist")

    # Load the JSON data
    with open(file_path, "r") as f:
        data = json.load(f)

    # Check if all required fields are present
    for field in INPUT_JSON["required"]:
        if field not in data:
            raise ValueError(f"Required field {field} is missing")

    # Check if the types match the schema
    for field, type in INPUT_JSON["properties"].items():
        if type != data[field].__class__.__name__:
            raise ValueError(f"Type mismatch for field {field}")

    # Check if the email format is valid
    if "email" in data:
        if not re.match(EMAIL_REGEX, data["email"]):
            raise ValueError(f"Invalid email format for field {data['email']}")

    # Return the specified attribute
    return data[attribute]