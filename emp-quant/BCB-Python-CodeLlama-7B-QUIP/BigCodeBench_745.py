
import subprocess
import random
# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'
def task_func():
    script = random.choice(SCRIPTS)
    subprocess.run([SCRIPTS_DIR + script])
    return script