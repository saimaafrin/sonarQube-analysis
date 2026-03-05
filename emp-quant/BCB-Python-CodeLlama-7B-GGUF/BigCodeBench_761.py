
import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    # 1. Remove None values
    json_str = json.dumps(json_str)
    json_str = re.sub(r'"None"', '', json_str)

    # 2. Count the frequency of each unique value
    value_counts = Counter()
    for key, value in json.loads(json_str).items():
        if value is not None:
            value_counts[value] += 1

    # 3. Replace all email addresses with the placeholder "None"
    json_str = re.sub(r'[\w.-]+@[\w.-]+', REPLACE_NONE, json_str)

    # Return the processed JSON data and the value counts
    return {
        "data": json.loads(json_str),
        "value_counts": value_counts
    }