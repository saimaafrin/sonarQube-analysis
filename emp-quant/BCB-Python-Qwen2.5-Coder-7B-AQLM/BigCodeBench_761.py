
import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    # Helper function to replace email addresses with REPLACE_NONE
    def replace_emails(value):
        if isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value):
            return REPLACE_NONE
        return value

    # Helper function to remove None values
    def remove_nones(value):
        if isinstance(value, dict):
            return {k: remove_nones(v) for k, v in value.items() if v is not None}
        elif isinstance(value, list):
            return [remove_nones(v) for v in value if v is not None]
        else:
            return value

    # Process the JSON string
    data = json.loads(json_str)
    processed_data = remove_nones(data)
    processed_data = json.dumps(processed_data, default=replace_emails)
    processed_data = json.loads(processed_data)

    # Count the frequency of each unique value
    value_counts = Counter(processed_data)

    return {
        "data": processed_data,
        "value_counts": value_counts
    }