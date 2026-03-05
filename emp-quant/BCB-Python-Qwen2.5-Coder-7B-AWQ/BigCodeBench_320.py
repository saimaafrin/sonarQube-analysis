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
        result = subprocess.run([file_path], check=True, capture_output=True, text=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        return e.returncode
    except FileNotFoundError:
        return None