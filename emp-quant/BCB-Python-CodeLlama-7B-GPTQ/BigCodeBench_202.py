import re
import json
from collections import Counter
def task_func(json_str, top_n=10):
    """
    Extract all URLs from a string-serialized JSON dict using a specific URL pattern and return a dict with the URLs as keys and the number of times they appear as values.
    """
    # Load the JSON string into a Python dict
    data = json.loads(json_str)

    # Create a regular expression pattern to match URLs
    pattern = r"https?://\S+"

    # Create a counter to keep track of the number of times each URL appears
    counter = Counter()

    # Iterate over the keys in the JSON dict
    for key in data:
        # Check if the value associated with the key is a string
        if isinstance(data[key], str):
            # Use the regular expression to find all URLs in the string
            urls = re.findall(pattern, data[key])

            # Add the URLs to the counter
            for url in urls:
                counter[url] += 1

    # Return the top N URLs and their counts
    return {url: count for url, count in counter.most_common(top_n)}
json_str = '{"key1": "https://www.example1.com", "key2": "https://www.example2.com", "key3": "https://www.example3.com"}'