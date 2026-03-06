import os
import csv
from collections import Counter
def task_func(file_path):
    """
    This function reads the specified CSV file, counts the frequency of each word, and returns the most common word 
    along with its frequency.

    Parameters:
    - file_path (str): The path to the CSV file.

    Requirements:
    - os
    - csv
    - collections

    Returns:
    - tuple: The most common word and its frequency, or None if the file doesn't exist or is empty.

    Example:
    >>> # Assuming 'example.txt' contains multiple repetitions of the word 'example'
    >>> task_func('example.txt')  # doctest: +SKIP
    ('example', <some_positive_integer>)

    Note:
    - The function specifically reads from the given file path.
    - This example uses +SKIP because it relies on external file content.
    """
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        words = [row[0] for row in reader]

    if not words:
        return None

    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0]
    most_common_word_count = word_counts[most_common_word]

    return most_common_word, most_common_word_count