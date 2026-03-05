
import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    # Parse the JSON string
    json_data = json.loads(json_str)

    # Extract all URLs from the JSON data
    urls = re.findall(r'https?://\S+', json_data)

    # Create a Counter object to count the URLs
    url_counter = Counter(urls)

    # Return the top N URLs and their counts
    return {url: count for url, count in url_counter.most_common(top_n)}