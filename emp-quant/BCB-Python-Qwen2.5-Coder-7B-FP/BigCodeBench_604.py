import subprocess
import logging
def task_func(filepath):
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    # Check if the file exists
    try:
        with open(filepath, 'r') as file:
            pass
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Attempt to compile the C++ file
    try:
        # Replace 'g++' with the actual compiler if different
        result = subprocess.run(['g++', filepath, '-o', 'output'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Compilation successful")
    except subprocess.CalledProcessError as e:
        logging.error(f"Compilation failed: {e.stderr.decode('utf-8')}")
        raise subprocess.CalledProcessError(e.returncode, e.cmd, e.output, e.stderr)