import binascii
import hashlib
import re
def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    """
    Searches for files within the specified directory matching a given regex pattern
    and computes a SHA256 hash of each file's content.

    Parameters:
    - directory (str): Directory to search for files.
    - pattern (str): Regex pattern that filenames must match. Default pattern matches 'AcroTray.exe'.

    Returns:
    - dict: A dictionary with file paths as keys and their SHA256 hashes as values.

    Requirements:
    - re
    - hashlib
    - binascii

    Example:
    >>> task_func(OUTPUT_DIR)
    {}
    """
    files = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(pattern, file):
                with open(os.path.join(root, file), 'rb') as f:
                    files[os.path.join(root, file)] = binascii.hexlify(hashlib.sha256(f.read()).digest()).decode()
    return files