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
        # If the file exists, delete it
        os.remove(filename)

    # Write the data to the file
    with open(filename, 'w') as f:
        json.dump(data, f)

    # Read the data back from the file
    with open(filename, 'r') as f:
        read_data = json.load(f)

    # Check if the data was written and read back correctly
    if data == read_data:
        # If the data was written and read back correctly, return a tuple with the success of the operation and the content that was written
        return True, data
    else:
        # If the data was not written or read back correctly, return a tuple with the success of the operation and the content that was written
        return False, data
data = {'name': 'John', 'age': 30, 'city': 'New York'}
filename = 'data.json'