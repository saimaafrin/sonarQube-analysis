
import json
import re
from collections import Counter
# Constants
REPLACE_NONE = "None"
def task_func(json_str):
    # Remove None values
    json_str = re.sub(r'"None"', "", json_str)
    # Count unique values
    value_counts = Counter(json_str)
    # Replace email addresses with "None"
    json_str = re.sub(r'"\w+@\w+\.com"', REPLACE_NONE, json_str)
    return {"data": json_str, "value_counts": value_counts}