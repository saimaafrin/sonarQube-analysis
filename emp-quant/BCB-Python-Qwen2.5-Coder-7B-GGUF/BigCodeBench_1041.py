
import re
import os

def task_func(request):
    # Define the base directory where files are stored
    base_directory = "/path/to/your/static/files"
    
    # Extract the filename from the request
    filename = re.search(r'GET /(.+) HTTP/1.1', request).group(1)
    
    # Construct the full path to the file
    file_path = os.path.join(base_directory, filename)
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Read the file content
        with open(file_path, 'rb') as file:
            file_content = file.read()
        
        # Prepare the HTTP response
        response = f"HTTP/1.1 200 OK\nContent-Length: {len(file_content)}\n\n{file_content}"
    else:
        # Prepare the HTTP response for file not found
        response = "HTTP/1.1 404 Not Found\n\nFile not found."
    
    return response