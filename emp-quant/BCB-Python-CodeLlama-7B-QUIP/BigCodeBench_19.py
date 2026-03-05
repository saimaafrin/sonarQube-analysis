
import os
import glob
import zipfile

def task_func(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError("Directory does not exist")
    file_list = glob.glob(os.path.join(directory, '*'))
    if not file_list:
        return None
    with zipfile.ZipFile('files.zip', 'w') as zf:
        for f in file_list:
            zf.write(f)
    return 'files.zip'