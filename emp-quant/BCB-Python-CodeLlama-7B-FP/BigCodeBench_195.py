import subprocess
import platform
import time
def task_func(url):
    """
    Open a web page in the default web browser in a background process.
    """
    if platform.system() == "Windows":
        # Windows
        subprocess.Popen(f"start {url}", shell=True)
    elif platform.system() == "Darwin":
        # macOS
        subprocess.Popen(f"open -g {url}", shell=True)
    else:
        # Linux
        subprocess.Popen(f"xdg-open {url}", shell=True)
    return 0
url = "https://www.example.com"