import os
import glob
import hashlib
def task_func(source_dir, target_dir, prefix='#Hash: '):
    """
    Computes the MD5 hash of each file's content in the specified `source_dir`, prepends the hash along with a prefix to the original content, and writes the modified content to new files in the `target_dir`. Existing files with the same name in `target_dir` are overwritten.
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

    # Create the target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Get a list of all files in the source directory
    files = glob.glob(os.path.join(source_dir, '*'))

    # Iterate over the files and compute the hash
    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
            hash = hashlib.md5(content).hexdigest()
            new_content = prefix + hash + content

        # Write the modified content to a new file in the target directory
        with open(os.path.join(target_dir, os.path.basename(file)), 'wb') as f:
            f.write(new_content)

    # Return a list of paths to the newly created files in the target directory
    return [os.path.join(target_dir, file) for file in os.listdir(target_dir)]
source_dir = 'source_dir'
target_dir = 'target_dir'
prefix = '#Hash: '