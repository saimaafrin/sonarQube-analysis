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
        return value

    # Load JSON data
    data = json.loads(json_str)
    
    # Process the data
    processed_data = json.loads(json.dumps(data, default=process_value))
    
    # Count the frequency of each unique value
    value_counts = Counter(json.dumps(processed_data, sort_keys=True).split(','))
    
    # Return the result
    return {
        "data": processed_data,
        "value_counts": value_counts
    }
json_str = '{"name": "John", "age": None, "email": "john@example.com", "address": {"city": "New York", "zip": None}}'