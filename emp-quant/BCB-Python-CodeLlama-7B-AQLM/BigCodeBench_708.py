import json
import csv
import os
import base64
def task_func(raw_string, filename, output_dir):
    """
    Processes a base64-encoded JSON string, stores the data in a CSV file, and returns the path of the file.

    Parameters:
    - raw_string (str): The base64 encoded JSON string.
    - filename (str): The name of the file to which the data should be saved (without extension).
    - output_dir (str): The path of the directory in which the file should be saved.

    Returns:
    - file_path (str): The path of the file.

    Requirements:
    - json
    - csv
    - os
    - base64

    Example:
    >>> task_func('eyJrZXkiOiAiVmFsdWUifQ==', 'data', './output')
    './output/data.csv'
    """
    # Decode the string
    decoded_string = base64.b64decode(raw_string)

    # Load the JSON
    json_data = json.loads(decoded_string)

    # Create the CSV file
    file_path = os.path.join(output_dir, filename + '.csv')
    with open(file_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(json_data.keys())
        csv_writer.writerow(json_data.values())

    return file_path