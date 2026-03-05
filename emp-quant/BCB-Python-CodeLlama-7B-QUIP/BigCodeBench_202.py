
import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    # Load the JSON string into a Python dict
    data = json.loads(json_str)

    # Extract the URLs from the dict
    urls = re.findall(r"https?://\S+", json_str)

    # Create a Counter object to count the number of times each URL appears
    counter = Counter(urls)

    # Return the top N URLs and their counts
    return {url: counter[url] for url in counter if counter[url] >= top_n}