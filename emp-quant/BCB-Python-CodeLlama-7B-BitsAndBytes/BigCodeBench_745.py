
import subprocess
import random

# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'

def task_func():
    # Select a random script from the list
    script = random.choice(SCRIPTS)

    # Run the script
    subprocess.run(['bash', script], cwd=SCRIPTS_DIR)

    # Output the script that was executed
    print(f'Script: {script}')

# Call the function
task_func()