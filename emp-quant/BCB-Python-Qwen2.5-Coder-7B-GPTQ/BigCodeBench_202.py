import re
import json
from collections import Counter
def task_func(json_str, top_n=10):
    # Parse the JSON string into a Python dictionary
    data = json.loads(json_str)
    
    # Define the URL pattern
    url_pattern = re.compile(r'https?://[^\s]+')
    
    # Find all URLs in the JSON data
    urls = url_pattern.findall(json.dumps(data))
    
    # Count the occurrences of each URL
    url_counts = Counter(urls)
    
    # Return the top_n most common URLs
    return url_counts.most_common(top_n)