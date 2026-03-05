import json
import os
import re
def task_func(
    file_path,
    attribute,
    INPUT_JSON={
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    },
    EMAIL_REGEX=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"):
    """
    Validate the structure and contents of a JSON file against predefined schema rules and retrieve a specified attribute from the JSON object.
    Ensures that all required fields exist, match their defined types, and checks the validity of the email format using a regular expression.
    Errors:
    - Raises ValueError if the file does not exist, required attributes are missing, types do not match, or the email format is invalid.
    """
    if not os.path.exists(file_path):
        raise ValueError(f"File {file_path} does not exist")
    with open(file_path, "r") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"File {file_path} is not a JSON object")
    for key, value in INPUT_JSON["properties"].items():
        if key not in data:
            raise ValueError(f"Required attribute {key} is missing from {file_path}")
        if not isinstance(data[key], value["type"]):
            raise ValueError(f"Attribute {key} has invalid type in {file_path}")
    if "email" in data:
        if not re.match(EMAIL_REGEX, data["email"]):
            raise ValueError(f"Email format is invalid in {file_path}")
    return data[attribute]