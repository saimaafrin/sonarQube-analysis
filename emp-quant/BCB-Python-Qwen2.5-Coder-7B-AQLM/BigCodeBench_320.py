
import subprocess
import os
import random

def task_func(directory, file_list):
    if not file_list:
        return None

    # Select a random file from the list
    selected_file = random.choice(file_list)

    # Construct the full path to the file
    file_path = os.path.join(directory, selected_file)

    # Check if the selected file exists
    if not os.path.isfile(file_path):
        return None

    # Run the selected file as a subprocess
    try:
        process = subprocess.Popen(file_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        exit_code = process.returncode
        return exit_code
    except Exception as e:
        print(f"An error occurred: {e}")
        return None