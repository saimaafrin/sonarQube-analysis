
from texttable import Texttable
import os
import psutil

def task_func():
    # Create a Texttable object
    table = Texttable()
    
    # Set the header of the table
    table.add_row(['Item', 'Value'])
    
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    table.add_row(['CPU Usage (%)', cpu_usage])
    
    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    table.add_row(['Memory Usage (%)', memory_usage])
    
    # Get disk usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    table.add_row(['Disk Usage (%)', disk_usage])
    
    # Return the table as a string
    return table.draw()