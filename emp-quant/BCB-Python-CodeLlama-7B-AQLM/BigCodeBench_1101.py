import subprocess
import os
import glob
import time
def task_func(test_dir):
    """
    Run all Python codes in a specific directory and return their execution times.

    Parameters:
    - script_path (str): Path to the directory for Python code(s) to be executed.
    
    Returns:
    dict: A dictionary with the script names as keys and their execution times as values.

    Requirements:
    - subprocess
    - os
    - glob
    - time

    Example:
    >>> task_func("/mnt/data/mix_files/")
    {'script1.py': 0.04103803634643555, "script2.py": 5}
    """
    script_list = glob.glob(os.path.join(test_dir, "*.py"))
    script_dict = {}
    for script in script_list:
        start_time = time.time()
        subprocess.call(["python", script])
        end_time = time.time()
        script_dict[script] = end_time - start_time
    return script_dict