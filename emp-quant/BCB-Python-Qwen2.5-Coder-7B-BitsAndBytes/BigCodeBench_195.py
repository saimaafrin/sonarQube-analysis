
import subprocess
import platform
import time

def task_func(url):
    # Determine the command to open the URL based on the operating system
    if platform.system() == "Windows":
        cmd = f'cmd /c start {url}'
    elif platform.system() == "Darwin":  # macOS
        cmd = f'open {url}'
    elif platform.system() == "Linux":
        cmd = f'xdg-open {url}'
    else:
        raise OSError("Unsupported operating system")

    # Start the subprocess
    process = subprocess.Popen(cmd, shell=True)

    # Wait for a short period to ensure the browser has started
    time.sleep(1)

    # Return the process ID (pid) as an integer
    return process.pid