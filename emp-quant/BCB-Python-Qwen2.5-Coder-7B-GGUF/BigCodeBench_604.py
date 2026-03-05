
import subprocess
import logging

def task_func(filepath):
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO)
    
    # Check if the file exists
    try:
        with open(filepath, 'r') as file:
            pass
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Attempt to compile the C++ file
    try:
        # Replace 'g++' with the actual compiler if necessary
        result = subprocess.run(['g++', filepath, '-o', 'output'], check=True, capture_output=True, text=True)
        logging.info("Compilation successful.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Compilation failed with error: {e.stderr}")
        raise subprocess.CalledProcessError(e.returncode, e.cmd, e.output, e.stderr)