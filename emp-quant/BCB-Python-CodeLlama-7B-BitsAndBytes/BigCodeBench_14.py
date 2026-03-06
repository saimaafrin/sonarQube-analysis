
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
        raise FileNotFoundError(f"Project directory '{project_dir}' does not exist")

    # Create the ZIP archive
    zip_file_name = os.path.basename(project_dir) + '.zip'
    zip_file_path = os.path.join(archive_dir, zip_file_name)
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(project_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, project_dir))

    # Return True if the ZIP archive is successfully created
    return True

try:
    task_func(config_file_path, archive_dir)
    print("ZIP archive created successfully")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")