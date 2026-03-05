import configparser
import os
import shutil
def task_func(config_file_path, archieve_dir ='/home/user/archive'):
    """
    Archive a specified project directory into a ZIP file based on the configuration specified in a config file.
    This function reads a configuration file to determine the project directory and archives this directory into a ZIP file.
    The ZIP file's name will be the project directory's basename, stored in the specified archive directory.
    Configuration File Format:
    [Project] directory=path_to_project_directory
    """
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Get the project directory from the configuration file
    project_dir = config['Project']['directory']

    # Check if the project directory exists
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f"Project directory '{project_dir}' does not exist.")

    # Create the ZIP archive
    zip_file_name = os.path.basename(project_dir) + '.zip'
    zip_file_path = os.path.join(archieve_dir, zip_file_name)
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        zip_file.write(project_dir, arcname=os.path.basename(project_dir))

    # Check if the ZIP archive was created successfully
    if not os.path.exists(zip_file_path):
        raise Exception(f"ZIP archive '{zip_file_path}' could not be created.")

    # Return True if the ZIP archive was created successfully
    return True
config_file_path = 'config.ini'
archieve_dir = '/home/user/archive'
project_dir = '/home/user/project'
config = configparser.ConfigParser()