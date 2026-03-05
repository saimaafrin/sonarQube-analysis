
import psutil
import platform

def task_func():
    # Get system details
    os_name = platform.system()
    arch = platform.architecture()[0]
    mem_usage = psutil.virtual_memory().percent

    # Create dictionary with system details
    system_details = {
        'OS': os_name,
        'Architecture': arch,
        'Memory Usage': f'{mem_usage:.2f}%'
    }

    return system_details