import subprocess
import random
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'
def task_func():
    # Select a random script from the list
    script_name = random.choice(SCRIPTS)
    # Construct the full path to the script
    script_path = f"{SCRIPTS_DIR}/{script_name}"
    # Execute the script using subprocess
    subprocess.run(['bash', script_path], check=True)
    # Return the full path of the executed script
    return script_path