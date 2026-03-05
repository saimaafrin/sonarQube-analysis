import json
import os
def task_func(filename, data):
    """
    Write a dictionary to a file as a JSON object and return the written content for verification.
    This function performs a write operation to store the dictionary data in JSON format and then reads it back to verify the content.
    Additionally, checks if the file exists using the os library.
    The function should output with:
        tuple: A tuple containing a boolean indicating the success of the operation and the content that was written.
        bool: indicating the success of the operation.
        written_data (json): the content that was written.
    """
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, read the content
        with open(filename, 'r') as f:
            written_data = json.load(f)
    else:
        # If the file does not exist, create it and write the content
        with open(filename, 'w') as f:
            json.dump(data, f)
            written_data = data

    # Verify the content
    if written_data == data:
        return True, written_data
    else:
        return False, written_data
data = {'key1': 'value1', 'key2': 'value2'}
filename = 'test.json'