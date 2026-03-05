import json
import re
from collections import Counter
REPLACE_NONE = "None"
def task_func(json_str):
    # Helper function to remove None values from a dictionary
    def remove_none_values(data):
        if isinstance(data, dict):
            return {k: remove_none_values(v) for k, v in data.items() if v is not None}
        elif isinstance(data, list):
            return [remove_none_values(item) for item in data if item is not None]
        else:
            return data

    # Helper function to replace email addresses with "None"
    def replace_emails(data):
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        if isinstance(data, dict):
            return {k: replace_emails(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [replace_emails(item) for item in data]
        elif isinstance(data, str):
            return email_pattern.sub(REPLACE_NONE, data)
        else:
            return data

    # Process the JSON string
    data = json.loads(json_str)
    cleaned_data = remove_none_values(data)
    replaced_data = replace_emails(cleaned_data)

    # Count the frequency of each unique value
    value_counts = Counter(replaced_data)

    # Return the result
    return {
        "data": replaced_data,
        "value_counts": value_counts
    }