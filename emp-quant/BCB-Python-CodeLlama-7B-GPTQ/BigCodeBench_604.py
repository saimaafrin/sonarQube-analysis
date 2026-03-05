import subprocess
import logging
def task_func(filepath):
    """
    Attempts to compile a C++ file specified by 'filepath'.
    The output of the compilation process is logged, indicating whether the compilation was successful or not.
    This function is useful for automating the compilation of C++ code and tracking compilation results.
    The log should indicate whether the compilation was successful or if an error occurred.
    """
    # Check if the file exists
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File '{filepath}' does not exist.")

    # Check if the compiler is installed
    compiler = "g++"
    if not shutil.which(compiler):
        raise FileNotFoundError(f"Compiler '{compiler}' is not installed.")

    # Compile the file
    try:
        subprocess.run([compiler, filepath], check=True)
        logging.info(f"Compilation of '{filepath}' was successful.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Compilation of '{filepath}' failed with error: {e}")
        raise
filepath = "example.cpp"