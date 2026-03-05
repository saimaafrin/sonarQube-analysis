
import psutil
import platform

def task_func():
    # Get system details
    system_details = {
        'OS': platform.system(),
        'Architecture': platform.architecture()[0],
        'Memory Usage': psutil.virtual_memory().percent,
    }

    return system_details