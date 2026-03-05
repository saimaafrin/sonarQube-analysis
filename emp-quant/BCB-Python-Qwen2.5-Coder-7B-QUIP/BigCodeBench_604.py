
import subprocess
import logging

def task_func(filepath):
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()

    # Check if the file exists
    try:
        with open(filepath, 'r') as f:
            pass
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"File not found: {filepath}")

    # Compile the C++ file
    try:
        result = subprocess.run(['g++', filepath, '-o', 'output'], capture_output=True, text=True, check=True)
        logger.info(f"Compilation successful: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Compilation failed: {e.stderr}")
        raise subprocess.CalledProcessError(e.returncode, e.cmd, e.stderr)