
from collections import Counter
import re

def task_func(result):
    url_values = [item['url'] for item in result if 'url' in item]
    most_common_urls = Counter(url_values).most_common()
    return dict(most_common_urls)