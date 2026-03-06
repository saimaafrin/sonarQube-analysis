
import subprocess
import logging

def task_func(filepath):
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Compile the C++ file
    try:
        subprocess.check_call(['g++', filepath])
        logger.info('Compilation successful')
    except subprocess.CalledProcessError as e:
        logger.error('Compilation failed: %s', e)
    except FileNotFoundError as e:
        logger.error('Compiler not found: %s', e)