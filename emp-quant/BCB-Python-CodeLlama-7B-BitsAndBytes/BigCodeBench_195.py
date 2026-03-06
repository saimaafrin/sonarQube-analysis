
import subprocess
import platform
import time

def task_func(url):
    # Open the URL in the default web browser in a background process
    command = "start" if platform.system() == "Windows" else "open"
    subprocess.Popen([command, url], shell=True)

    # Wait for the process to finish
    time.sleep(5)

    # Get the return code of the process
    return_code = subprocess.Popen([command, url], shell=True).returncode

    # Print the return code
    print(return_code)

# Call the function with the URL to open
task_func("https://www.example.com")