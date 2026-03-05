import os
import glob
import shutil
def task_func(directory, archive_dir='archive'):
    """
    Archive all JSON files in a given directory by moving them to a specified archive directory.
    
    Parameters:
    directory (str): The directory containing JSON files to be archived.
    archive_dir (str): The directory where JSON files will be archived. Defaults to 'archive'.
    
    Returns:
    tuple: A tuple containing a boolean value and a list of error messages.
    The boolean is True if all files are successfully moved, and False otherwise.
    The list contains error messages for each file that failed to move.
    """
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    # List to hold error messages
    error_messages = []
    
    # Move each JSON file to the archive directory
    for json_file in json_files:
        try:
            shutil.move(json_file, os.path.join(archive_dir, os.path.basename(json_file)))
        except Exception as e:
            error_messages.append(f"Failed to move {json_file}: {str(e)}")
    
    # Return the result
    return (len(error_messages) == 0, error_messages)