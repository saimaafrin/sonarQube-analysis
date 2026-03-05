
import configparser
import os
import shutil

def task_func(config_file_path, archive_dir='/home/user/archive'):
    # Read the configuration file
    config = configparser.ConfigParser()
    try:
        config.read(config_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {config_file_path}")

    # Get the project directory from the configuration
    project_dir = config['Project'].get('directory', None)
    if not project_dir:
        raise ValueError("Project directory not specified in the config file")

    # Ensure the project directory exists
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f"Project directory not found: {project_dir}")

    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Create the ZIP file
    zip_file_path = os.path.join(archive_dir, os.path.basename(project_dir) + '.zip')
    try:
        shutil.make_archive(zip_file_path, 'zip', root_dir=project_dir)
    except Exception as e:
        raise Exception(f"Failed to create ZIP archive: {e}")

    return True