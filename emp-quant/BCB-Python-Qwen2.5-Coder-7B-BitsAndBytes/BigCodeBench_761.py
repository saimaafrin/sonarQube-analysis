
import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def remove_none_values(data):
    if isinstance(data, dict):
        return {k: remove_none_values(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [remove_none_values(item) for item in data if item is not None]
    else:
        return data

def replace_emails_with_none(data):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if isinstance(data, str):
        return re.sub(email_pattern, REPLACE_NONE, data)
    elif isinstance(data, dict):
        return {k: replace_emails_with_none(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_emails_with_none(item) for item in data]
    else:
        return data

def count_value_frequencies(data):
    flattened_data = []
    def flatten(d):
        for key, value in d.items():
            if isinstance(value, dict):
                flatten(value)
            elif isinstance(value, list):
                for item in value:
                    flatten(item)
            else:
                flattened_data.append(value)
    flatten(data)
    return Counter(flattened_data)

def task_func(json_str):
    data = json.loads(json_str)
    cleaned_data = remove_none_values(data)
    cleaned_data = replace_emails_with_none(cleaned_data)
    value_counts = count_value_frequencies(cleaned_data)
    return {
        "data": cleaned_data,
        "value_counts": value_counts
    }