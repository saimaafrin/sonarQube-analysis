
import subprocess
import logging

def task_func(filepath):
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Check if the file exists
        with open(filepath, 'r') as file:
            pass
        
        # Compile the C++ file using g++
        result = subprocess.run(['g++', filepath], capture_output=True, text=True, check=True)
        
        # Log the success message
        logging.info("Compilation successful.")
        
    except FileNotFoundError:
        # Log the error message if the file is not found
        logging.error(f"The file {filepath} does not exist.")
        raise
    
    except subprocess.CalledProcessError as e:
        # Log the error message if the compilation fails
        logging.error(f"Compilation failed with error: {e.stderr}")
        raise