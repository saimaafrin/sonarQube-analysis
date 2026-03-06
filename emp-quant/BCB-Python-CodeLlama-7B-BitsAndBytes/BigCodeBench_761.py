
import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    # 1. Remove None values
    json_data = json.loads(json_str)
    json_data = {k: v for k, v in json_data.items() if v is not None}

    # 2. Count the frequency of each unique value
    value_counts = Counter()
    for k, v in json_data.items():
        if isinstance(v, dict):
            value_counts.update(Counter(v))
        else:
            value_counts[v] += 1

    # 3. Replace all email addresses with the placeholder "None"
    for k, v in json_data.items():
        if isinstance(v, str) and re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", v):
            json_data[k] = REPLACE_NONE

    return {
        "data": json_data,
        "value_counts": value_counts
    }