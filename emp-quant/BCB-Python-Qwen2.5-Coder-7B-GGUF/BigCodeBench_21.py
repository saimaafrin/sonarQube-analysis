
import psutil
import platform

def task_func():
    # Get the operating system name
    os_name = platform.system()
    
    # Get the system architecture
    architecture = platform.architecture()[0]
    
    # Get the total and used memory
    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    
    # Calculate the memory usage percentage
    memory_usage = (used_memory / total_memory) * 100
    
    # Format the memory usage to two decimal places
    memory_usage_formatted = f"{memory_usage:.2f}%"
    
    # Return the dictionary with the gathered details
    return {
        'OS': os_name,
        'Architecture': architecture,
        'Memory Usage': memory_usage_formatted
    }