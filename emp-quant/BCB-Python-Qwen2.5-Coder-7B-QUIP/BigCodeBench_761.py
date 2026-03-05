
import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    # Step 1: Remove None values
    data = json.loads(json_str)
    processed_data = json.loads(json.dumps(data, default=lambda o: o if isinstance(o, (int, str, bool, None)) else None, sort_keys=True))

    # Step 2: Replace all email addresses with the placeholder "None"
    def replace_emails(obj):
        if isinstance(obj, dict):
            return {k: replace_emails(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [replace_emails(item) for item in obj]
        elif isinstance(obj, str) and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', obj):
            return REPLACE_NONE
        else:
            return obj

    processed_data = replace_emails(processed_data)

    # Step 3: Count the frequency of each unique value
    value_counts = Counter(processed_data)

    # Output
    return {
        "data": processed_data,
        "value_counts": value_counts
    }