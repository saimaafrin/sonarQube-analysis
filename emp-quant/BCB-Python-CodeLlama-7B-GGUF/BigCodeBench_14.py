
import configparser
import os
import shutil

def task_func(config_file_path, archive_dir='/home/user/archive'):
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Get the project directory from the configuration file
    project_dir = config['Project']['directory']

    # Check if the project directory exists
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f'Project directory {project_dir} does not exist')

    # Get the basename of the project directory
    project_basename = os.path.basename(project_dir)

    # Create the ZIP archive file name
    archive_file = os.path.join(archive_dir, f'{project_basename}.zip')

    # Create the ZIP archive
    try:
        shutil.make_archive(archive_file, 'zip', project_dir)
    except shutil.Error as e:
        raise Exception(f'Failed to create ZIP archive: {e}')

    # Return True if the ZIP archive is successfully created
    return True