
import subprocess
import os
import glob

# Constants
ARCHIVE_DIR = '/tmp/archive'

def task_func(pattern):
    # Ensure the ARCHIVE_DIR exists
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Find all files matching the pattern
    files_to_archive = glob.glob(pattern)
    
    if not files_to_archive:
        raise FileNotFoundError(f"No files found matching the pattern: {pattern}")
    
    # Create an archive file name based on the current timestamp
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'archive_{timestamp}.tar.gz'
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)
    
    # Archive the files using tar command
    try:
        subprocess.run(['tar', '-czf', archive_path] + files_to_archive, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to create archive: {e}")
    
    # Delete the original files
    for file in files_to_archive:
        os.remove(file)
    
    return archive_path