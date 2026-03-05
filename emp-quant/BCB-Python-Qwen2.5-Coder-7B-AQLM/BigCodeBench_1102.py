
import subprocess
import shlex
from datetime import datetime

def task_func(script_path: str) -> dict:
    start_time = datetime.now()
    process = subprocess.Popen(['Rscript', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = datetime.now()
    
    decoded_stdout = stdout.decode('utf-8')
    decoded_stderr = stderr.decode('utf-8')
    
    return {
        'start_time': start_time,
        'end_time': end_time,
        'stdout': decoded_stdout,
        'stderr': decoded_stderr
    }