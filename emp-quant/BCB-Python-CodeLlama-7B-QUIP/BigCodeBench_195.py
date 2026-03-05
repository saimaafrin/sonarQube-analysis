
import subprocess
import platform
import time

def task_func(url):
    # Open the web page in the default web browser
    if platform.system() == "Windows":
        subprocess.Popen(["start", url])
    else:
        subprocess.Popen(["xdg-open", url])
    return 0

# Call the function and wait for the process to finish
result = task_func(url)
print(result)