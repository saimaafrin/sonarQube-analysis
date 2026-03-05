
from collections import Counter
import re

def task_func(result):
    url_values = [item['url'] for item in result]
    most_common = Counter(url_values).most_common()
    return dict(most_common)