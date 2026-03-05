import os
import glob
import hashlib
def task_func(source_dir, target_dir, prefix='#Hash: '):
    """
    Computes the MD5 hash of each file's content in the specified `source_dir`, prepends the hash along with a prefix to the original content, and writes the modified content to new files in the `target_dir`. Existing files with the same name in `target_dir` are overwritten.
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory {source_dir} does not exist.")

    # Create a list of files in the source directory
    files = glob.glob(os.path.join(source_dir, '*'))

    # Create a list to store the paths of the newly created files in the target directory
    new_files = []

    # Iterate over the files in the source directory
    for file in files:
        # Compute the MD5 hash of the file's content
        with open(file, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        # Prepend the hash to the file's content
        with open(file, 'r') as f:
            content = f.read()
        with open(file, 'w') as f:
            f.write(f"{prefix}{file_hash}\n{content}")

        # Move the modified file to the target directory
        new_file = os.path.join(target_dir, os.path.basename(file))
        os.rename(file, new_file)
        new_files.append(new_file)

    return new_files
source_dir = 'source_dir'
target_dir = 'target_dir'
prefix = '#Hash: '