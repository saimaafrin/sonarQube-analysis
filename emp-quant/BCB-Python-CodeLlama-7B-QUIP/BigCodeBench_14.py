
import configparser
import os
import shutil

def task_func(config_file_path, archive_dir ='/home/user/archive'):
    config = configparser.ConfigParser()
    config.read(config_file_path)
    project_dir = config['Project']['directory']
    if not os.path.exists(project_dir):
        raise FileNotFoundError("Project directory does not exist")
    if not os.path.exists(archive_dir):
        raise FileNotFoundError("Archive directory does not exist")
    zip_file_name = os.path.basename(project_dir) + '.zip'
    zip_file_path = os.path.join(archive_dir, zip_file_name)
    try:
        shutil.make_archive(zip_file_path, 'zip', project_dir)
    except shutil.Error:
        raise Exception("ZIP archive could not be created")
    return True