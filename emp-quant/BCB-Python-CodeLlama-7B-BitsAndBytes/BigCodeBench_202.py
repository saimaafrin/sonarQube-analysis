
import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    # Parse the JSON string
    data = json.loads(json_str)

    # Extract all URLs from the data
    urls = re.findall(r'https?://\S+', data)

    # Create a Counter object to count the URLs
    counter = Counter(urls)

    # Return the top N URLs and their counts
    return {url: count for url, count in counter.most_common(top_n)}