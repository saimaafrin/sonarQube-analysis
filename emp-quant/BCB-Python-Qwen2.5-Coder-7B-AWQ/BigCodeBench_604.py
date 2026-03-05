import subprocess
import logging
def task_func(filepath):
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Attempt to compile the C++ file
        result = subprocess.run(['g++', filepath, '-o', 'output'], check=True, capture_output=True, text=True)
        logger.info("Compilation successful.")
        logger.info("Output: " + result.stdout)
    except subprocess.CalledProcessError as e:
        logger.error("Compilation failed with error: " + e.stderr)
        raise e
    except FileNotFoundError as e:
        logger.error("File not found or compiler not installed: " + str(e))
        raise e