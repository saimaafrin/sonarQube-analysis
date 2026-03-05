import os
import csv
from collections import Counter
def task_func(file_path):
    """
    This function reads the specified CSV file, counts the frequency of each word, and returns the most common word along with its frequency.
    Note that:
        - The function specifically reads from the given file path.
        - This example uses +SKIP because it relies on external file content.
    The function should output with:
        - tuple: The most common word and its frequency, or None if the file doesn't exist or is empty.
    """
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        words = [word for row in reader for word in row]

    counter = Counter(words)
    most_common_word = counter.most_common(1)[0]

    return most_common_word