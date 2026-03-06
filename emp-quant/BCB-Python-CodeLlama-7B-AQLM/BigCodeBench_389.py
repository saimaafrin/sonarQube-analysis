import re
import os
import shutil
def task_func(directory):
    """
    Find the files with filenames that contain "like" or "what" in a directory, create a new subdirectory called "Interesting Files" 
    and move those files to the new subdirectory.

    Parameters:
    directory (str): The directory path.

    Returns:
    List of files moved

    Requirements:
    - re
    - os
    - shutil

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> files = ['file_with_like.txt', 'another_file_with_what.doc', 'file_without_keywords.jpg', 'hidden_what_in_name.whatever']
    >>> for file in files:
    ...     with open(os.path.join(temp_dir, file), 'w') as f:
    ...         _ = f.write("Dummy content for testing.")
    >>> task_func(temp_dir)
    ['another_file_with_what.doc', 'hidden_what_in_name.whatever', 'file_with_like.txt']
    """
    interesting_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(r"like|what", file):
                interesting_files.append(os.path.join(root, file))
    new_dir = os.path.join(directory, "Interesting Files")
    os.mkdir(new_dir)
    for file in interesting_files:
        shutil.move(file, new_dir)
    return interesting_files