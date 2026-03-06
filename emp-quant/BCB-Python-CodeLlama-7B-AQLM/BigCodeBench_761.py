import json
import re
from collections import Counter
REPLACE_NONE = "None"
def task_func(json_str):
    """
    Process a JSON string by:
    1. Removing None values.
    2. Counting the frequency of each unique value.
    3. Replacing all email addresses with the placeholder "None".
    
    Parameters:
    json_str (str): The JSON string to be processed.
    
    Returns:
    dict: A dictionary containing:
        - "data": Processed JSON data.
        - "value_counts": A Counter object with the frequency of each unique value.
    
    Requirements:
    - json
    - re
    - collections.Counter
    
    Example:
    >>> json_str = '{"name": "John", "age": null, "email": "john@example.com"}'
    >>> task_func(json_str)
    {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
    """
    # Remove None values
    json_str = re.sub(r'null', REPLACE_NONE, json_str)
    
    # Count the frequency of each unique value
    value_counts = Counter()
    for key, value in json.loads(json_str).items():
        value_counts[value] += 1
    
    # Replace all email addresses with the placeholder "None"
    json_str = re.sub(r'\"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\"', REPLACE_NONE, json_str)
    
    # Return the processed JSON data and the frequency of each unique value
    return {"data": json.loads(json_str), "value_counts": value_counts}