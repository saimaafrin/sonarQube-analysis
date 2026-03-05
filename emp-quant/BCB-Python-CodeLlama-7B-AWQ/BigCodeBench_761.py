import json
import re
from collections import Counter
REPLACE_NONE = "None"
def task_func(json_str):
    # Remove None values
    json_str = json.dumps(json_str)
    json_str = re.sub(r'"None"', '', json_str)

    # Count unique values
    value_counts = Counter()
    for key, value in json.loads(json_str).items():
        if value is not None:
            value_counts[value] += 1

    # Replace email addresses with placeholder
    json_str = re.sub(r'[\w\.]+@[\w\.]+', REPLACE_NONE, json_str)

    # Return processed JSON data and value counts
    return {
        "data": json.loads(json_str),
        "value_counts": value_counts
    }
json_str = '{"name": "John", "age": 32, "email": "john@example.com", "city": "New York"}'