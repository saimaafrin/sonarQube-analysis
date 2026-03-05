import subprocess
import random
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'
def task_func():
    # Run a random bash script from a list of scripts
    script = random.choice(SCRIPTS)
    script_path = os.path.join(SCRIPTS_DIR, script)
    subprocess.run(script_path, shell=True)
    return script