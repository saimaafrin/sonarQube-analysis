
from texttable import Texttable
import os
import psutil

def task_func():
    # Get the system's CPU usage, memory usage, and disk usage
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage(os.getcwd())

    # Create a table with the system information
    table = Texttable()
    table.set_cols_align(["l", "r"])
    table.set_cols_dtype(["t", "t"])
    table.add_rows_with_keys(["Item", "Value"],
                             ["CPU Usage", cpu_usage],
                             ["Memory Usage", memory_usage],
                             ["Disk Usage", disk_usage])

    # Print the table
    print(table.get_string())