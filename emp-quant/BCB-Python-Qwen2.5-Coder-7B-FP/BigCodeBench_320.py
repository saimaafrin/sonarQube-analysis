import subprocess
import os
import random
def task_func(directory, file_list):
    if not file_list:
        return None

    # Select a random file from the list
    selected_file = random.choice(file_list)
    file_path = os.path.join(directory, selected_file)

    # Check if the selected file is executable
    if not os.access(file_path, os.X_OK):
        return None

    # Run the selected file as a subprocess
    try:
        process = subprocess.Popen(file_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return process.returncode
    except Exception as e:
        print(f"An error occurred: {e}")
        return None