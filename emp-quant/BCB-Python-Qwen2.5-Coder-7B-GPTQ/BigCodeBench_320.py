import subprocess
import os
import random
def task_func(directory, file_list):
    if not file_list:
        return None

    # Select a random file from the provided list
    selected_file = random.choice(file_list)
    file_path = os.path.join(directory, selected_file)

    # Check if the selected file exists
    if not os.path.isfile(file_path):
        return None

    # Run the selected file as a subprocess
    try:
        result = subprocess.run([file_path], check=True, capture_output=True, text=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        return e.returncode
    except FileNotFoundError:
        return None