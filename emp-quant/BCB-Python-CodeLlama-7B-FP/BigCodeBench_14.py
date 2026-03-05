import configparser
import os
import shutil
def task_func(config_file_path, archive_dir='/home/user/archive'):
    """
    Archive a specified project directory into a ZIP file based on the configuration specified in a config file.
    This function reads a configuration file to determine the project directory and archives this directory into a ZIP file.
    The ZIP file's name will be the project directory's basename, stored in the specified archive directory.
    Configuration File Format: [Project] directory=path_to_project_directory
    """
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Get the project directory from the configuration file
    project_dir = config['Project']['directory']

    # Check if the project directory exists
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f'Project directory {project_dir} does not exist')

    # Create the ZIP archive
    zip_file_name = os.path.basename(project_dir) + '.zip'
    zip_file_path = os.path.join(archive_dir, zip_file_name)
    try:
        shutil.make_archive(zip_file_path, 'zip', project_dir)
    except Exception as e:
        raise Exception(f'Failed to create ZIP archive: {e}')

    # Return True if the ZIP archive is successfully created
    return True
config_file_path = 'config.ini'
archive_dir = '/home/user/archive'
project_dir = '/home/user/project'
config = configparser.ConfigParser()