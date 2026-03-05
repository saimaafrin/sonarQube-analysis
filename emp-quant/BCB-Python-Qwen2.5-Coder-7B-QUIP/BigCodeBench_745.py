
import subprocess
import random
# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'  

def task_func():
    # Generate a random index
    random_index = random.randint(0, len(SCRIPTS) - 1)
    # Select a random script
    selected_script = SCRIPTS[random_index]
    # Full path of the selected script
    full_path = f"{SCRIPTS_DIR}/{selected_script}"
    # Execute the script using subprocess
    result = subprocess.run(['bash', full_path], capture_output=True, text=True)
    # Output the full path of the script that was executed
    print(f"Script executed: {full_path}")
    return full_path