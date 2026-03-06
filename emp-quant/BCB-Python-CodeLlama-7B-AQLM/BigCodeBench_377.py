from texttable import Texttable
import os
import psutil
def task_func():
    """
    Generates a table displaying the system's CPU usage, memory usage, and disk usage.

    Returns:
        A string representation of a table with the columns of 'Item' and 'Value',
        and the following system information:
        - CPU Usage (%)
        - Memory Usage (%)
        - Disk Usage (%)

    Requirements:
    - texttable.Texttable
    - os
    - psutil

    Examples:
    >>> table_str = task_func()
    >>> isinstance(table_str, str)
    True
    >>> 'CPU Usage (%)' in table_str and 'Memory Usage (%)' in table_str
    True
    """
    table = Texttable()
    table.set_cols_align(['l', 'r'])
    table.set_cols_valign(['t', 'm'])
    table.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', psutil.cpu_percent()],
        ['Memory Usage (%)', psutil.virtual_memory().percent],
        ['Disk Usage (%)', psutil.disk_usage('/').percent]
    ])
    return table.draw()