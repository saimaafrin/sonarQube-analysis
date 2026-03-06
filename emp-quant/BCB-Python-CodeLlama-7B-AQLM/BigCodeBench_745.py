import subprocess
import random
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'
def task_func():
    """
    Run a random bash script from a list of scripts.

    Parameters:
    - None

    Returns:
    - script (str): The full path of the script that was executed.

    Requirements:
    - subprocess
    - random

    Example:
    >>> task_func()
    """
    script = random.choice(SCRIPTS)
    script_path = SCRIPTS_DIR + script
    subprocess.call(script_path, shell=True)
    return script_path