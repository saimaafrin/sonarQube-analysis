
import subprocess
import random

# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'

def task_func():
    # Select a random script from the list
    script = random.choice(SCRIPTS)
    # Execute the script
    subprocess.run([f'{SCRIPTS_DIR}/{script}'], shell=True)
    # Return the script that was executed
    return script