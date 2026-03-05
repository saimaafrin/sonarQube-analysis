from collections import Counter
import re
def task_func(result):
    # Extract values associated with the 'url' key
    urls = [item['url'] for item in result if 'url' in item]
    
    # Count the occurrences of each URL
    url_counts = Counter(urls)
    
    # Return the dictionary with the most common values and their counts
    return dict(url_counts.most_common())