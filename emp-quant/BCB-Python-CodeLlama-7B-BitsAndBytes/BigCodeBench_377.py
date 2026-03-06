
from texttable import Texttable
import os
import psutil

def task_func():
    # Get system information
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage(os.getcwd()).percent

    # Create table
    table = Texttable()
    table.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', cpu_usage],
        ['Memory Usage (%)', mem_usage],
        ['Disk Usage (%)', disk_usage]
    ])
    print(table.draw())

task_func()