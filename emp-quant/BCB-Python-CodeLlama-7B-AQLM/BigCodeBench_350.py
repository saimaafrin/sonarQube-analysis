import subprocess
import os
import shutil
from glob import glob
def task_func(src_folder, dst_folder):
    """Compress all files in the specified source folder and move the compressed files to a destination folder.
    This operation is executed as a background process using the 'gzip' command.

    Parameters:
    src_folder (str): The path of the source folder containing the files to be compressed.
    dst_folder (str): The path of the destination folder where the compressed files will be moved.

    Returns:
    dict: A dictionary containing:
        - 'success': A boolean indicating if all files were compressed and moved successfully.
        - 'message': A descriptive message about the operation's result.
        - 'failed_files': A list of filenames that failed to compress or move.

    Requirements:
    - subprocess
    - os
    - shutil
    - glob
    - gzip

    Example:
    >>> import tempfile
    >>> import os
    >>> src_folder = tempfile.mkdtemp()
    >>> dst_folder = tempfile.mkdtemp()
    >>> for i in range(3):
    ...     with open(os.path.join(src_folder, f'file{i}.txt'), 'w') as f:
    ...         _ = f.write(f'This is file {i}.')
    >>> task_func(src_folder, dst_folder)
    {'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}
    """
    # Check if the source folder exists
    if not os.path.exists(src_folder):
        return {'success': False, 'message': f'Source folder {src_folder} does not exist.', 'failed_files': []}

    # Check if the destination folder exists
    if not os.path.exists(dst_folder):
        return {'success': False, 'message': f'Destination folder {dst_folder} does not exist.', 'failed_files': []}

    # Get a list of all files in the source folder
    files = glob(os.path.join(src_folder, '*'))

    # Check if there are files to compress
    if len(files) == 0:
        return {'success': False, 'message': f'No files to compress in {src_folder}.', 'failed_files': []}

    # Compress all files in the source folder
    failed_files = []
    for file in files:
        try:
            subprocess.run(['gzip', file])
        except Exception as e:
            failed_files.append(file)

    # Move all compressed files to the destination folder
    for file in files:
        try:
            shutil.move(file + '.gz', dst_folder)
        except Exception as e:
            failed_files.append(file)

    # Check if all files were compressed and moved successfully
    if len(failed_files) == 0:
        return {'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}
    else:
        return {'success': False, 'message': f'Failed to compress and move {len(failed_files)} files.',
                'failed_files': failed_files}