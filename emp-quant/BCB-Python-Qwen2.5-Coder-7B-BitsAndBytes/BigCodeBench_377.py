
from texttable import Texttable
import os
import psutil

def task_func():
    # Create a Texttable object
    t = Texttable()

    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # Get disk usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    # Add rows to the table
    t.add_row(['CPU Usage (%)', cpu_usage])
    t.add_row(['Memory Usage (%)', memory_usage])
    t.add_row(['Disk Usage (%)', disk_usage])

    # Set the header for the table
    t.header(['Item', 'Value'])

    # Return the string representation of the table
    return t.draw()

# Call the function and print the result
print(task_func())