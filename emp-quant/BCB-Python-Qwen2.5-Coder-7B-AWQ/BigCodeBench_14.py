import configparser
import os
import shutil
def task_func(config_file_path, archive_dir='/home/user/archive'):
    # Check if the config file exists
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"Config file not found: {config_file_path}")
    
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    
    # Check if the project directory is specified in the config file
    if 'Project' not in config or 'directory' not in config['Project']:
        raise ValueError("Project directory not specified in the config file")
    
    # Get the project directory from the config file
    project_dir = config['Project']['directory']
    
    # Check if the project directory exists
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f"Project directory not found: {project_dir}")
    
    # Get the basename of the project directory
    basename = os.path.basename(project_dir)
    
    # Create the archive directory if it does not exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Create the path for the ZIP archive
    zip_path = os.path.join(archive_dir, f"{basename}.zip")
    
    # Archive the project directory into a ZIP file
    try:
        shutil.make_archive(zip_path[:-4], 'zip', project_dir)
        return True
    except Exception as e:
        raise Exception(f"Failed to create ZIP archive: {e}")
config_file_path = 'path_to_config_file.ini'
archive_dir = '/home/user/archive'