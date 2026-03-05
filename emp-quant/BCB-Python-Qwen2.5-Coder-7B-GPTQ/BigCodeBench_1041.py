import re
import os
def task_func(request):
    # Define the base directory where files are stored
    base_dir = '/path/to/your/files'
    
    # Extract the filename from the request
    filename = re.search(r'GET /([^ ]+) HTTP/1.1', request).group(1)
    
    # Check if the filename is valid
    if not filename or not filename.strip():
        return "HTTP/1.1 400 Bad Request\n\nInvalid request"
    
    # Construct the full path to the file
    file_path = os.path.join(base_dir, filename)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        return "HTTP/1.1 404 Not Found\n\nFile not found"
    
    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Get the content length
    content_length = len(content)
    
    # Return the HTTP response
    return f"HTTP/1.1 200 OK\nContent-Length: {content_length}\n\n{content}"