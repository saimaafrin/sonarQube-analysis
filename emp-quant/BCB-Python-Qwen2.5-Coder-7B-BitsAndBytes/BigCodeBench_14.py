
import configparser
import os
import shutil

def task_func(config_file_path, archive_dir='/home/user/archive'):
    # Check if the config file exists
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"The configuration file {config_file_path} does not exist.")
    
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    
    # Extract the project directory from the configuration
    try:
        project_dir = config['Project']['directory']
    except KeyError as e:
        raise ValueError(f"Configuration error: {e}. Ensure the 'Project' section has a 'directory' key.")
    
    # Check if the project directory exists
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f"The project directory {project_dir} does not exist.")
    
    # Create the archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Generate the archive file path
    zip_file_name = os.path.basename(project_dir) + '.zip'
    zip_file_path = os.path.join(archive_dir, zip_file_name)
    
    # Archive the project directory
    try:
        shutil.make_archive(zip_file_path.replace('.zip', ''), 'zip', project_dir)
    except Exception as e:
        raise Exception(f"Failed to create the ZIP archive: {e}")
    
    return True