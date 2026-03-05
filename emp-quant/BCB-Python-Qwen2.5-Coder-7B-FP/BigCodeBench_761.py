import json
import re
from collections import Counter
REPLACE_NONE = "None"
def task_func(json_str):
    # Helper function to remove None values and replace email addresses
    def process_value(value):
        if value is None:
            return REPLACE_NONE
        elif isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value):
            return REPLACE_NONE
        elif isinstance(value, dict):
            return {k: process_value(v) for k, v in value.items() if v is not None}
        elif isinstance(value, list):
            return [process_value(v) for v in value if v is not None]
        return value

    # Process the JSON string
    data = json.loads(json_str)
    processed_data = process_value(data)

    # Count the frequency of each unique value
    value_counts = Counter(json.dumps(processed_data, sort_keys=True))

    return {
        "data": processed_data,
        "value_counts": value_counts
    }