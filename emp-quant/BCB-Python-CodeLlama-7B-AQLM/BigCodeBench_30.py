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
    Validate the structure and contents of a JSON file against predefined schema rules and retrieve a specified attribute from the JSON object. Ensures that all required fields exist, match their defined types, and checks the validity of the email format using a regular expression.
    
    Parameters:
    file_path (str): The path to the JSON file.
    attribute (str): The attribute to retrieve from the JSON object.
    INPUT_JSON (dict): The input json to validate. The default value is:
    '{
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    }'.
    EMAIL_REGEX (str): The regex used to check the email validity. Default to 'r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")'

    Returns:
    Any: The value of the specified attribute, consistent with the type defined in the JSON schema.

    Requirements:
    - json
    - os
    - re

    Errors:
    - Raises ValueError if the file does not exist, required attributes are missing, types do not match, or the email format is invalid.

    Example:
    >>> task_func('/path/to/file.json', 'email')
    'john.doe@example.com'
    """
    if not os.path.exists(file_path):
        raise ValueError(f"File '{file_path}' does not exist.")

    with open(file_path, 'r') as f:
        data = json.load(f)

    try:
        json_schema = json.loads(json.dumps(INPUT_JSON))
    except:
        raise ValueError(f"Invalid JSON schema: '{INPUT_JSON}'")

    try:
        jsonschema.validate(data, json_schema)
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError(f"Invalid JSON: {e}")

    if attribute not in data:
        raise ValueError(f"Required attribute '{attribute}' is missing.")

    if not isinstance(data[attribute], type(json_schema['properties'][attribute]['type'])):
        raise ValueError(f"Type of '{attribute}' does not match the schema.")

    if attribute == 'email' and not re.match(EMAIL_REGEX, data[attribute]):
        raise ValueError(f"Invalid email format: '{data[attribute]}'")

    return data[attribute]