import re
import json
from collections import Counter
def task_func(json_str, top_n=10):
    # Parse the JSON string into a Python dictionary
    data = json.loads(json_str)
    
    # Define the URL pattern
    url_pattern = re.compile(r'https?://[^\s]+')
    
    # Extract all URLs from the dictionary
    urls = []
    for key, value in data.items():
        if isinstance(value, str):
            urls.extend(url_pattern.findall(value))
    
    # Count the occurrences of each URL
    url_counts = Counter(urls)
    
    # Return the top_n most common URLs
    return dict(url_counts.most_common(top_n))