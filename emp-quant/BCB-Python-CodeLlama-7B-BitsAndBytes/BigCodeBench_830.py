
import json
import os

def task_func(filename, data):
    # Check if the file exists
    if os.path.exists(filename):
        print(f"File {filename} already exists. Overwriting...")

    # Write the data to the file as JSON
    with open(filename, "w") as f:
        json.dump(data, f)

    # Read the data back from the file
    with open(filename, "r") as f:
        read_data = json.load(f)

    # Verify the content
    if data == read_data:
        print("Data written and read back successfully!")
        return True, data
    else:
        print("Data written and read back successfully, but the content is different!")
        return False, data