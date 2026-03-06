
import psutil
import platform

def task_func():
    # Get OS name
    os_name = platform.system()
    
    # Get system architecture
    arch = platform.machine()
    
    # Get memory details
    memory = psutil.virtual_memory()
    memory_usage_percent = memory.percent
    
    # Format memory usage as a string
    memory_usage_str = f"{memory_usage_percent}%"
    
    # Create a dictionary to store the results
    result_dict = {
        'OS': os_name,
        'Architecture': arch,
        'Memory Usage': memory_usage_str
    }
    
    return result_dict