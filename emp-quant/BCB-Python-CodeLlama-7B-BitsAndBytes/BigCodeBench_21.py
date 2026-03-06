
import psutil
import platform

def task_func():
    # Get system details
    os_name = platform.system()
    architecture = platform.architecture()[0]
    memory_usage = psutil.virtual_memory().percent

    # Create dictionary with system details
    system_details = {
        'OS': os_name,
        'Architecture': architecture,
        'Memory Usage': f'{memory_usage:.2f}%'
    }

    return system_details