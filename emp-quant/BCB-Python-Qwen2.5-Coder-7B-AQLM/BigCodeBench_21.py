
import psutil
import platform

def task_func():
    # Get the operating system name
    os_name = platform.system()
    
    # Get the system architecture
    architecture = platform.architecture()[0]
    
    # Get the memory usage details
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total
    used_memory = memory_info.used
    memory_usage_percent = (used_memory / total_memory) * 100
    
    # Format the memory usage percentage to two decimal places
    memory_usage_formatted = f"{memory_usage_percent:.2f}%"
    
    # Create a dictionary with the gathered information
    system_details = {
        'OS': os_name,
        'Architecture': architecture,
        'Memory Usage': memory_usage_formatted
    }
    
    return system_details