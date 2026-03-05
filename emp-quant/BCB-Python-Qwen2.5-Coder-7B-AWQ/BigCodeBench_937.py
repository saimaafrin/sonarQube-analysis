import re
from collections import Counter
def task_func(input_str):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str).lower()
    # Count the frequency of each character
    frequency_dict = Counter(cleaned_str)
    return frequency_dict