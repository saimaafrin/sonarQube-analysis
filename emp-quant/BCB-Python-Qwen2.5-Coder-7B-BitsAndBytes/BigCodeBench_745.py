
import subprocess
import random

# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'

def task_func():
    # Select a random script from the list
    selected_script = random.choice(SCRIPTS)
    
    # Construct the full path to the script
    script_path = f"{SCRIPTS_DIR}/{selected_script}"
    
    # Execute the script using subprocess
    try:
        result = subprocess.run(['bash', script_path], check=True, capture_output=True, text=True)
        print(f"Script executed successfully: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e.stderr}")
    
    return script_path