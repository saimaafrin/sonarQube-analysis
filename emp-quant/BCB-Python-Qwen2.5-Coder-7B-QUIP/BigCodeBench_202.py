
import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    # Extract the JSON data from the string
    json_data = json.loads(json_str)
    
    # Initialize a Counter to keep track of URL occurrences
    url_counter = Counter()
    
    # Define the regular expression pattern for URLs
    url_pattern = r'https?://[^\s<>]+'
    
    # Function to extract URLs from a given text
    def extract_urls(text):
        return re.findall(url_pattern, text)
    
    # Iterate over the values in the JSON data and extract URLs
    for key, value in json_data.items():
        if isinstance(value, str):
            url_counter.update(extract_urls(value))
    
    # Return the top_n most common URLs
    return dict(url_counter.most_common(top_n))