
import psutil
import platform

def task_func():
    # Get OS information
    os_name = platform.system()
    os_version = platform.version()
    os_info = f"{os_name} {os_version}"

    # Get architecture information
    architecture, _ = platform.architecture()
    arch_info = architecture

    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = (memory.used / memory.total) * 100
    memory_usage = f"{memory_usage:.2f}%"

    # Return the results in a dictionary
    return {
        'OS': os_info,
        'Architecture': arch_info,
        'Memory Usage': memory_usage
    }