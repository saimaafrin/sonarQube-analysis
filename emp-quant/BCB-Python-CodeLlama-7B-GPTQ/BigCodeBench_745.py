import subprocess
import random
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'
def task_func():
    # Select a random script from the list
    script = random.choice(SCRIPTS)
    # Run the script
    subprocess.run([SCRIPTS_DIR + script], shell=True)
    # Return the full path of the script that was executed
    return SCRIPTS_DIR + script