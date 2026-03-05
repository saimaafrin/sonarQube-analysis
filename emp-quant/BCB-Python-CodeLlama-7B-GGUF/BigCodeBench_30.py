
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

    if not os.path.exists(file_path):
        raise ValueError(f"File {file_path} does not exist")

    with open(file_path, "r") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Invalid JSON data: {data}")

    for key, value in INPUT_JSON["properties"].items():
        if key not in data:
            raise ValueError(f"Required attribute {key} is missing")
        if not isinstance(data[key], value["type"]):
            raise ValueError(f"Invalid type for attribute {key}: {data[key]}")

    if "email" in data and not re.match(EMAIL_REGEX, data["email"]):
        raise ValueError(f"Invalid email format: {data['email']}")

    return data[attribute]