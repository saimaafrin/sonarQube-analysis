import psutil
import platform
def task_func():
    # Get the operating system name
    os_name = platform.system()
    
    # Get the system architecture
    architecture = platform.architecture()[0]
    
    # Get the memory details
    memory = psutil.virtual_memory()
    total_memory = memory.total
    used_memory = memory.used
    memory_usage_percent = (used_memory / total_memory) * 100
    
    # Format the memory usage as a percentage
    memory_usage_formatted = f"{memory_usage_percent:.2f}%"
    
    # Return the results in a dictionary
    return {
        'OS': os_name,
        'Architecture': architecture,
        'Memory Usage': memory_usage_formatted
    }