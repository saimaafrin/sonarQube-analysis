import re
import json
from collections import Counter
def task_func(json_str, top_n=10):
    """
    Extract all URLs from a string-serialized JSON dict using a specific URL pattern and return a dict with the URLs as keys and the number of times they appear as values.
    """
    # Load the JSON string into a Python dict
    data = json.loads(json_str)

    # Create a regular expression object to match URLs
    url_pattern = re.compile(r'https?://\S+')

    # Create an empty dict to store the URLs and their counts
    url_counts = {}

    # Iterate over the data dict and extract URLs
    for key, value in data.items():
        if isinstance(value, str):
            urls = url_pattern.findall(value)
            for url in urls:
                if url not in url_counts:
                    url_counts[url] = 1
                else:
                    url_counts[url] += 1

    # Return the top N URLs and their counts
    return {url: count for url, count in url_counts.items() if count >= top_n}
json_str = '{"key1": "https://www.example1.com", "key2": "https://www.example2.com", "key3": "https://www.example3.com", "key4": "https://www.example4.com"}'