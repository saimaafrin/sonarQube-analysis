
import subprocess
import os
import time
from datetime import datetime

def task_func(script_dir, scripts, delay):
    if delay < 0:
        raise ValueError("Delay must be non-negative")
    if not scripts:
        raise ValueError("No scripts provided")

    # Create a list to store the timestamps
    timestamps = []

    # Iterate over the scripts and execute them with a delay between each one
    for script in scripts:
        # Get the current timestamp
        timestamp = datetime.now()

        # Execute the script
        subprocess.run(f"{script_dir}/{script}", shell=True)

        # Add the timestamp to the list
        timestamps.append(timestamp)

        # Wait for the delay
        time.sleep(delay)

    # Return the list of timestamps
    return timestamps