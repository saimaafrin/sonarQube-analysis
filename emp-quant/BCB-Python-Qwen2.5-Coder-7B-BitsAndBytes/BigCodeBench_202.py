
import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    # Define the URL pattern
    url_pattern = r'https?://[^\s]+'
    
    # Parse the JSON string into a dictionary
    data = json.loads(json_str)
    
    # Initialize an empty list to store all URLs
    urls = []
    
    # Helper function to extract URLs from nested dictionaries and lists
    def extract_urls(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                extract_urls(value)
        elif isinstance(obj, list):
            for item in obj:
                extract_urls(item)
        elif isinstance(obj, str):
            urls.extend(re.findall(url_pattern, obj))
    
    # Extract URLs from the parsed JSON data
    extract_urls(data)
    
    # Count the occurrences of each URL
    url_counts = Counter(urls)
    
    # Return the top N most common URLs
    return url_counts.most_common(top_n)

result = task_func(json_str, top_n=3)
print(result)