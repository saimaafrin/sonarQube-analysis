import json
import re
from collections import Counter
REPLACE_NONE = "None"
def task_func(json_str):
    # 1. Remove None values
    json_str = json.loads(json_str)
    json_str = {k: v for k, v in json_str.items() if v is not None}

    # 2. Count the frequency of each unique value
    value_counts = Counter()
    for k, v in json_str.items():
        if isinstance(v, list):
            for item in v:
                value_counts.update(item)
        else:
            value_counts.update(v)

    # 3. Replace all email addresses with the placeholder "None"
    json_str = json.dumps(json_str, indent=4)
    json_str = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", REPLACE_NONE, json_str)

    return {
        "data": json_str,
        "value_counts": value_counts,
    }
json_str = """
{
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "phone": "555-1234",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "hobbies": ["reading", "hiking", "photography"]
}
"""