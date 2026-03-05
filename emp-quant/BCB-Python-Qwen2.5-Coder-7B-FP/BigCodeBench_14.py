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
    
    # Check if the project section exists
    if 'Project' not in config:
        raise Exception("The configuration file does not contain a 'Project' section.")
    
    # Get the project directory from the configuration
    project_dir = config['Project'].get('directory')
    
    # Check if the project directory exists
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f"The project directory {project_dir} does not exist.")
    
    # Create the archive directory if it does not exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Get the basename of the project directory
    project_name = os.path.basename(project_dir)
    
    # Create the path for the ZIP file
    zip_file_path = os.path.join(archive_dir, f"{project_name}.zip")
    
    # Archive the project directory into a ZIP file
    try:
        shutil.make_archive(zip_file_path, 'zip', project_dir)
    except Exception as e:
        raise Exception(f"Failed to create the ZIP archive: {e}")
    
    return True