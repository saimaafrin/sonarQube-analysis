
import subprocess
import logging

def task_func(filepath):
    logging.basicConfig(level=logging.INFO)
    try:
        subprocess.check_call(["g++", filepath])
        logging.info("Compilation successful")
    except subprocess.CalledProcessError:
        logging.error("Compilation failed")
    except FileNotFoundError:
        logging.error("Compiler not found or file not found")