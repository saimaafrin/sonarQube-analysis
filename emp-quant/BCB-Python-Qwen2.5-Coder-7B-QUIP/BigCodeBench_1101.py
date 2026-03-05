
import subprocess
import os
import glob
import time
def task_func(test_dir):
    script_times = {}
    for script in glob.glob(os.path.join(test_dir, '*.py')):
        start_time = time.time()
        subprocess.run(['python', script], check=True)
        end_time = time.time()
        script_times[script] = end_time - start_time
    return script_times