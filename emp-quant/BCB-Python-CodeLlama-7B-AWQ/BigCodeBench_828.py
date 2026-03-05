import os
import errno
import shutil
def task_func(filename, dest_dir):
    """
    Copies a file to a specified destination directory and clears its contents.

    Args:
        filename (str): The path to the file to be copied.
        dest_dir (str): The path to the destination directory.

    Returns:
        str: The absolute path to the copied file within the destination directory.

    Raises:
        OSError: If the destination directory cannot be created and does not exist, or if the file cannot be copied for reasons other than a pre-existing directory.
    """
    # Check if the destination directory exists
    if not os.path.exists(dest_dir):
        raise OSError(errno.ENOENT, "Destination directory does not exist")

    # Check if the file exists
    if not os.path.exists(filename):
        raise OSError(errno.ENOENT, "File does not exist")

    # Get the file name and extension
    file_name, file_extension = os.path.splitext(filename)

    # Create a new file with the same name and extension in the destination directory
    new_file_path = os.path.join(dest_dir, file_name + file_extension)

    # Copy the file to the destination directory
    shutil.copyfile(filename, new_file_path)

    # Clear the contents of the original file
    with open(filename, "w") as f:
        f.truncate()

    return new_file_path