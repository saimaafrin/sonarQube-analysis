from texttable import Texttable
import os
import psutil
def task_func():
    """
    Generates a table displaying the system's CPU usage, memory usage, and disk usage.
    """
    # Get system information
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Create table
    table = Texttable()
    table.set_cols_align(['l', 'r'])
    table.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', cpu_usage],
        ['Memory Usage (%)', memory_usage],
        ['Disk Usage (%)', disk_usage],
    ])

    # Print table
    print(table.draw())