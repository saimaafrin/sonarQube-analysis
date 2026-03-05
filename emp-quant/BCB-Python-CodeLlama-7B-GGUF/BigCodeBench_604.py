
import subprocess
import logging

def task_func(filepath):
    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('compilation.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Compile the C++ file
    try:
        subprocess.run(['g++', filepath], check=True)
        logger.info('Compilation successful')
    except subprocess.CalledProcessError as e:
        logger.error('Compilation failed: %s', e)
    except FileNotFoundError as e:
        logger.error('Compiler not found: %s', e)