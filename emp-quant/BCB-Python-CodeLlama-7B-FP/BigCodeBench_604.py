import subprocess
import logging
def task_func(filepath):
    """
    Attempts to compile a C++ file specified by 'filepath'.
    The output of the compilation process is logged, indicating whether the compilation was successful or not.
    This function is useful for automating the compilation of C++ code and tracking compilation results.
    The log should indicate whether the compilation was successful or if an error occurred.
    """
    try:
        # Compile the C++ file
        subprocess.check_call(["g++", filepath])
        logging.info("Compilation successful")
    except subprocess.CalledProcessError as e:
        logging.error("Compilation failed: %s", e)
    except FileNotFoundError as e:
        logging.error("Compiler not found: %s", e)