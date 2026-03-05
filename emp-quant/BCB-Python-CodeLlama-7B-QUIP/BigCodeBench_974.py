
import shutil
import pathlib

def task_func(source_path, destination_path):
    if not pathlib.Path(source_path).is_dir():
        raise ValueError("Source path must be a directory")
    filenames = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
    for filename in filenames:
        shutil.copy(os.path.join(source_path, filename), destination_path)
    return source_path, filenames