
from texttable import Texttable
import os
import psutil

def task_func():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent()

    # Get memory usage
    memory_usage = psutil.virtual_memory().percent

    # Get disk usage
    disk_usage = psutil.disk_usage('/').percent

    # Create a table
    t = Texttable()
    t.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', cpu_usage],
        ['Memory Usage (%)', memory_usage],
        ['Disk Usage (%)', disk_usage]
    ], header=True)

    # Print the table
    print(t.draw())